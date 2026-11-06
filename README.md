# Supabase Database Fundamentals — Milestone 3

## Project Overview

This project demonstrates database fundamentals using **Supabase (PostgreSQL)** and **Python**.

It was developed as part of Milestone 3, focusing on relational database design, SQL operations, database security, and Python integration.

## Technologies Used

- Supabase
- PostgreSQL
- Python 3
- Supabase Python Client
- SQL

## Database Architecture

The project contains two related tables:

### 1. Customers

| Column | Description |
|---|---|
| id | Primary key |
| name | Customer name |
| email | Customer email |

### 2. Orders

| Column | Description |
|---|---|
| id | Primary key |
| customer_id | Foreign key referencing customers.id |
| product | Product or service |
| amount | Order amount |

### Database Relationship

One customer can have multiple orders.

`orders.customer_id` references `customers.id`, establishing a one-to-many relationship.

## SQL Operations Demonstrated

- **SELECT:** Retrieve database records.
- **INSERT:** Add new customer records.
- **WHERE:** Filter records using conditions.
- **JOIN:** Combine customer and order information.

### Example JOIN Query

```sql
SELECT
    customers.name AS customer_name,
    customers.email,
    orders.product,
    orders.amount
FROM public.customers
JOIN public.orders
    ON customers.id = orders.customer_id;
```

## Python Integration

The Python script connects to Supabase using the Supabase Python client.

It demonstrates:
- Establishing a database connection.
- Checking whether a test customer exists.
- Inserting the test customer if necessary.
- Retrieving the customer record.

## Security

Row-Level Security (RLS) is enabled with policies restricting access to the designated test customer.

API credentials should be stored securely and must never be committed to GitHub.

## Project Structure

```text
milestone3-supabase/
│
├── milestone3.py
└── README.md
```

## Project Objectives

- Create a relational PostgreSQL database.
- Establish primary and foreign key relationships.
- Practise essential SQL queries.
- Connect Python to Supabase.
- Demonstrate data insertion and retrieval.
- Apply database access controls using RLS.

## Author

**Roudy Douaihy**

Database Fundamentals — Milestone 3
