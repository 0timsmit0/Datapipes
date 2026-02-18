"""Generate dummy seed data for the e-commerce database."""

import csv
import random
from datetime import datetime, timedelta
from pathlib import Path

random.seed(42)

FIRST_NAMES = [
    "James", "Mary", "Robert", "Patricia", "John", "Jennifer", "Michael", "Linda",
    "David", "Elizabeth", "William", "Barbara", "Richard", "Susan", "Joseph", "Jessica",
    "Thomas", "Sarah", "Christopher", "Karen", "Charles", "Lisa", "Daniel", "Nancy",
    "Matthew", "Betty", "Anthony", "Margaret", "Mark", "Sandra", "Donald", "Ashley",
    "Steven", "Kimberly", "Paul", "Emily", "Andrew", "Donna", "Joshua", "Michelle",
    "Kenneth", "Carol", "Kevin", "Amanda", "Brian", "Dorothy", "George", "Melissa",
    "Timothy", "Deborah", "Ronald", "Stephanie", "Edward", "Rebecca", "Jason", "Sharon",
    "Jeffrey", "Laura", "Ryan", "Cynthia", "Jacob", "Kathleen", "Gary", "Amy",
    "Nicholas", "Angela", "Eric", "Shirley", "Jonathan", "Anna", "Stephen", "Brenda",
    "Larry", "Pamela", "Justin", "Emma", "Scott", "Nicole", "Brandon", "Helen",
    "Benjamin", "Samantha", "Samuel", "Katherine", "Raymond", "Christine", "Gregory", "Debra",
    "Frank", "Rachel", "Alexander", "Carolyn", "Patrick", "Janet", "Jack", "Catherine",
]

LAST_NAMES = [
    "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis",
    "Rodriguez", "Martinez", "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson",
    "Thomas", "Taylor", "Moore", "Jackson", "Martin", "Lee", "Perez", "Thompson",
    "White", "Harris", "Sanchez", "Clark", "Ramirez", "Lewis", "Robinson", "Walker",
    "Young", "Allen", "King", "Wright", "Scott", "Torres", "Nguyen", "Hill", "Flores",
    "Green", "Adams", "Nelson", "Baker", "Hall", "Rivera", "Campbell", "Mitchell",
    "Carter", "Roberts", "Gomez", "Phillips", "Evans", "Turner", "Diaz", "Parker",
    "Cruz", "Edwards", "Collins", "Reyes", "Stewart", "Morris", "Morales", "Murphy",
    "Cook", "Rogers", "Gutierrez", "Ortiz", "Morgan", "Cooper", "Peterson", "Bailey",
    "Reed", "Kelly", "Howard", "Ramos", "Kim", "Cox", "Ward", "Richardson",
]

CITIES = [
    ("New York", "United States"), ("Los Angeles", "United States"),
    ("Chicago", "United States"), ("Houston", "United States"),
    ("London", "United Kingdom"), ("Manchester", "United Kingdom"),
    ("Toronto", "Canada"), ("Vancouver", "Canada"),
    ("Berlin", "Germany"), ("Munich", "Germany"),
    ("Paris", "France"), ("Lyon", "France"),
    ("Amsterdam", "Netherlands"), ("Rotterdam", "Netherlands"),
    ("Sydney", "Australia"), ("Melbourne", "Australia"),
    ("Tokyo", "Japan"), ("Madrid", "Spain"),
    ("Rome", "Italy"), ("Stockholm", "Sweden"),
]

CATEGORIES = {
    "Electronics": [
        "Wireless Bluetooth Headphones", "USB-C Charging Cable", "Portable Power Bank",
        "Smartphone Screen Protector", "Laptop Stand", "Mechanical Keyboard",
        "Wireless Mouse", "Webcam HD 1080p", "External SSD 1TB", "HDMI Cable",
        "Monitor Arm", "USB Hub 7-Port", "Noise Cancelling Earbuds", "Tablet Case",
        "Smart Watch Band", "Phone Car Mount", "LED Desk Lamp", "Surge Protector",
        "Ethernet Cable Cat6", "Wireless Charger Pad",
    ],
    "Clothing": [
        "Cotton T-Shirt", "Denim Jeans", "Wool Sweater", "Running Shoes",
        "Leather Belt", "Baseball Cap", "Winter Jacket", "Casual Shorts",
        "Dress Shirt", "Sneakers", "Socks Pack", "Hoodie", "Polo Shirt",
        "Chino Pants", "Rain Jacket", "Beanie Hat", "Scarf", "Gloves",
        "Flip Flops", "Swimwear",
    ],
    "Home & Kitchen": [
        "Stainless Steel Water Bottle", "Non-Stick Frying Pan", "Coffee Maker",
        "Kitchen Knife Set", "Cutting Board Bamboo", "Glass Food Containers",
        "Blender", "Toaster", "Tea Kettle", "Dish Rack",
        "Spice Rack", "Oven Mitts", "Measuring Cups", "Mixing Bowl Set",
        "Can Opener", "Wine Opener", "Ice Cube Tray", "Paper Towel Holder",
        "Salt and Pepper Mill", "Coaster Set",
    ],
    "Books": [
        "Python Programming Guide", "Data Science Handbook", "SQL Mastery",
        "Machine Learning Basics", "Web Development Bootcamp", "Cloud Architecture",
        "DevOps Handbook", "Algorithms Explained", "Clean Code", "Design Patterns",
        "The Pragmatic Programmer", "System Design Interview", "Docker in Action",
        "Kubernetes Up and Running", "Linux Command Line", "Git Version Control",
        "JavaScript The Good Parts", "React in Depth", "Database Internals",
        "Network Programming",
    ],
    "Sports": [
        "Yoga Mat", "Resistance Bands Set", "Jump Rope", "Foam Roller",
        "Dumbbell Set", "Water Bottle Sports", "Gym Bag", "Workout Gloves",
        "Tennis Balls", "Basketball", "Soccer Ball", "Running Armband",
        "Fitness Tracker Band", "Pull Up Bar", "Ab Wheel", "Kettlebell",
        "Boxing Gloves", "Swim Goggles", "Cycling Gloves", "Ankle Weights",
    ],
}

ORDER_STATUSES = ["pending", "confirmed", "shipped", "delivered", "cancelled"]


def random_phone() -> str:
    return f"+1-{random.randint(200,999)}-{random.randint(100,999)}-{random.randint(1000,9999)}"


def random_address() -> str:
    return f"{random.randint(1, 9999)} {random.choice(LAST_NAMES)} {random.choice(['St', 'Ave', 'Blvd', 'Rd', 'Ln', 'Dr'])}"


def random_date(start: datetime, end: datetime) -> datetime:
    delta = end - start
    random_seconds = random.randint(0, int(delta.total_seconds()))
    return start + timedelta(seconds=random_seconds)


def generate(output_dir: Path):
    """Generate CSV files for customers, products, and orders."""
    now = datetime(2025, 1, 15)
    customer_start = now - timedelta(days=730)

    # --- Customers ---
    customers_file = output_dir / "customers.csv"
    used_emails = set()
    with open(customers_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "first_name", "last_name", "email", "phone", "address", "city", "country", "created_at"])
        for i in range(1, 501):
            first = random.choice(FIRST_NAMES)
            last = random.choice(LAST_NAMES)
            email_base = f"{first.lower()}.{last.lower()}"
            email = f"{email_base}@example.com"
            counter = 1
            while email in used_emails:
                email = f"{email_base}{counter}@example.com"
                counter += 1
            used_emails.add(email)

            phone = random_phone()
            address = random_address()
            city, country = random.choice(CITIES)
            created = random_date(customer_start, now)
            writer.writerow([i, first, last, email, phone, address, city, country, created.strftime("%Y-%m-%d %H:%M:%S")])
    print(f"Generated: {customers_file}")

    # --- Products ---
    products_file = output_dir / "products.csv"
    product_prices = []
    with open(products_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "name", "category", "price", "stock_quantity", "description", "created_at"])
        for i in range(1, 1001):
            category = random.choice(list(CATEGORIES.keys()))
            base_name = random.choice(CATEGORIES[category])
            variant = random.choice(["", " Pro", " Plus", " Lite", " Max", " Mini", " XL", " V2", " Elite", " Basic"])
            color = random.choice(["", " - Black", " - White", " - Blue", " - Red", " - Green", " - Gray", " - Silver"])
            name = f"{base_name}{variant}{color}"

            price_ranges = {
                "Electronics": (9.99, 299.99),
                "Clothing": (12.99, 149.99),
                "Home & Kitchen": (7.99, 89.99),
                "Books": (9.99, 59.99),
                "Sports": (8.99, 129.99),
            }
            lo, hi = price_ranges[category]
            price = round(random.uniform(lo, hi), 2)
            product_prices.append(price)
            stock = random.randint(0, 500)
            desc = f"High quality {base_name.lower()} in the {category.lower()} category."
            created = random_date(customer_start, now)
            writer.writerow([i, name, category, price, stock, desc, created.strftime("%Y-%m-%d %H:%M:%S")])
    print(f"Generated: {products_file}")

    # --- Orders ---
    orders_file = output_dir / "orders.csv"
    order_start = now - timedelta(days=365)
    with open(orders_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "customer_id", "product_id", "quantity", "total_amount", "status", "order_date"])
        for i in range(1, 1001):
            customer_id = random.randint(1, 500)
            product_id = random.randint(1, 1000)
            quantity = random.choices([1, 2, 3, 4, 5], weights=[50, 25, 15, 7, 3])[0]
            total = round(product_prices[product_id - 1] * quantity, 2)
            status = random.choices(ORDER_STATUSES, weights=[10, 15, 20, 50, 5])[0]
            order_date = random_date(order_start, now)
            writer.writerow([i, customer_id, product_id, quantity, total, status, order_date.strftime("%Y-%m-%d %H:%M:%S")])
    print(f"Generated: {orders_file}")


if __name__ == "__main__":
    output_dir = Path(__file__).parent / "raw"
    output_dir.mkdir(parents=True, exist_ok=True)
    generate(output_dir)
    print("Seed data generation complete.")
