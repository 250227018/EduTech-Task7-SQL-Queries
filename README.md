# EduTech-Task7-SQL-Queries
# Task 7 - SQL Queries for Data Extraction

## Tool Used
Python (SQLite3) + Pandas

## Dataset
Custom Relational Database (Customers + Orders tables) created using SQLite

## Tables Created
- **customers** - customer_id, customer_name, city, country
- **orders** - order_id, customer_id, order_date, amount, category

## Queries Written
1. **SELECT** - Basic data retrieval from customers table
2. **INNER JOIN** - Customers with their respective orders
3. **LEFT JOIN** - All customers including those without orders
4. **GROUP BY** - Category wise total orders and sales
5. **Subquery** - Customers who placed orders above 400

## How to Run
```bash
python task7_sql.py
```

## Interview Answers
**Inner vs Left Join?**
INNER JOIN sirf wahi rows deta hai jo dono tables mein match karti hain.
LEFT JOIN left table ki saari rows deta hai, right table mein match na ho to NULL aata hai.

**What is a subquery?**
Subquery ek query ke andar likhi dusri query hoti hai. Outer query, inner query ke result ko filter karne ke liye use karti hai.
