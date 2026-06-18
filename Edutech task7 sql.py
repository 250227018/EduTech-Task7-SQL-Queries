import sqlite3
import pandas as pd

# Database banao (automatically ban jayega)
conn = sqlite3.connect('ecommerce.db')
cursor = conn.cursor()

# Tables banao
cursor.executescript('''
CREATE TABLE IF NOT EXISTS customers (
    customer_id INT PRIMARY KEY,
    customer_name TEXT,
    city TEXT,
    country TEXT
);

CREATE TABLE IF NOT EXISTS orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date TEXT,
    amount REAL,
    category TEXT
);

INSERT OR IGNORE INTO customers VALUES
(1, 'Alice', 'New York', 'USA'),
(2, 'Bob', 'London', 'UK'),
(3, 'Charlie', 'Mumbai', 'India'),
(4, 'Diana', 'Delhi', 'India'),
(5, 'Eve', 'Paris', 'France');

INSERT OR IGNORE INTO orders VALUES
(101, 1, '2023-01-15', 500.00, 'Electronics'),
(102, 2, '2023-02-20', 300.00, 'Furniture'),
(103, 3, '2023-03-10', 150.00, 'Clothing'),
(104, 1, '2023-04-05', 700.00, 'Electronics'),
(105, 4, '2023-05-18', 200.00, 'Furniture'),
(106, 3, '2023-06-22', 450.00, 'Electronics'),
(107, 5, '2023-07-30', 600.00, 'Clothing');
''')

# Queries
print("=== SELECT ALL CUSTOMERS ===")
print(pd.read_sql("SELECT * FROM customers", conn))

print("\n=== INNER JOIN ===")
print(pd.read_sql("""
    SELECT c.customer_name, c.city, o.order_id, o.amount, o.category
    FROM customers c
    INNER JOIN orders o ON c.customer_id = o.customer_id
""", conn))

print("\n=== LEFT JOIN ===")
print(pd.read_sql("""
    SELECT c.customer_name, o.order_id, o.amount
    FROM customers c
    LEFT JOIN orders o ON c.customer_id = o.customer_id
""", conn))

print("\n=== GROUP BY (Category wise Sales) ===")
print(pd.read_sql("""
    SELECT category, COUNT(*) AS total_orders, SUM(amount) AS total_sales
    FROM orders
    GROUP BY category
""", conn))

print("\n=== SUBQUERY (High value customers) ===")
print(pd.read_sql("""
    SELECT customer_name FROM customers
    WHERE customer_id IN (
        SELECT customer_id FROM orders WHERE amount > 400
    )
""", conn))

conn.close()
print("\nDone!")