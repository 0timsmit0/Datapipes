from datetime import datetime, timedelta
import csv
import os

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook

# DAG configuration
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

# Path to data files (mounted through Docker)
DATA_PATH = '/opt/airflow/data/raw'

def extract_csv(filename: str) -> list:
    """Extract records from a CSV file."""
    filepath = os.path.join(DATA_PATH, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return list(reader)


def validate_customers(records: list) -> list:
    """Validate customer records."""
    valid = []
    for record in records:
        if record.get('email') and '@' in record['email']:
            valid.append(record)
    return valid


def load_customers(**context):
    """Extract, validate, and load customers to Postgres."""
    records = extract_csv('customers.csv')
    valid_records = validate_customers(records)

    hook = PostgresHook(postgres_conn_id='postgres_default')
    conn = hook.get_conn()
    cursor = conn.cursor()

    for record in valid_records:
        cursor.execute(
            """
            INSERT INTO dummyshop.customers
                (id, first_name, last_name, email, phone, address, city, country, created_at)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT (id) DO UPDATE SET
                first_name = EXCLUDED.first_name,
                last_name = EXCLUDED.last_name,
                email = EXCLUDED.email,
                phone = EXCLUDED.phone,
                address = EXCLUDED.address,
                city = EXCLUDED.city,
                country = EXCLUDED.country,
                created_at = EXCLUDED.created_at
            """,
            (
                record['id'],
                record['first_name'],
                record['last_name'],
                record['email'],
                record['phone'],
                record['address'],
                record['city'],
                record['country'],
                record['created_at'],
            )
        )

    conn.commit()
    cursor.close()
    print(f"Loaded {len(valid_records)} customers")
    return len(valid_records)

with DAG(
    'dummyshop_etl',
    default_args=default_args,
    description='Load dummy shop customer data from CSV to Postgres',
    schedule_interval=None,  # Manual trigger only for learning
    start_date=datetime(2026, 1, 1),
    catchup=False,
    tags=['dummyshop', 'etl'],
) as dag:
    load_customers_task = PythonOperator(
        task_id='load_customers',
        python_callable=load_customers,
    )
