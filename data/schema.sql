-- E-commerce database schema

CREATE SCHEMA IF NOT EXISTS dummyshop;

CREATE TABLE IF NOT EXISTS dummyshop.customers (
    id INTEGER PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20),
    address VARCHAR(200),
    city VARCHAR(50),
    country VARCHAR(50),
    created_at TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS dummyshop.products (
    id INTEGER PRIMARY KEY,
    name VARCHAR(150) NOT NULL,
    category VARCHAR(50) NOT NULL,
    price NUMERIC(10, 2) NOT NULL CHECK (price > 0),
    stock_quantity INTEGER NOT NULL DEFAULT 0,
    description TEXT,
    created_at TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS dummyshop.orders (
    id INTEGER PRIMARY KEY,
    customer_id INTEGER NOT NULL REFERENCES dummyshop.customers(id),
    product_id INTEGER NOT NULL REFERENCES dummyshop.products(id),
    quantity INTEGER NOT NULL CHECK (quantity > 0),
    total_amount NUMERIC(10, 2) NOT NULL,
    status VARCHAR(20) NOT NULL DEFAULT 'pending',
    order_date TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_orders_customer_id ON dummyshop.orders(customer_id);
CREATE INDEX IF NOT EXISTS idx_orders_product_id ON dummyshop.orders(product_id);
CREATE INDEX IF NOT EXISTS idx_orders_status ON dummyshop.orders(status);
CREATE INDEX IF NOT EXISTS idx_products_category ON dummyshop.products(category);
