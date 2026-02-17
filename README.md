Environment: Windows

Ensuring docker desktop is running first, start up container with:

```bash
docker compose up -d
```

Load up ```http://localhost:8080/``` with password and username as per ```docker-comepose.yaml``` file (default: both ```airflow```).










Used ```docker-compose.yaml``` file from ```curl -o docker-compose.yaml 'https://airflow.apache.org/docs/apache-airflow/2.4.0/docker-compose.yaml```