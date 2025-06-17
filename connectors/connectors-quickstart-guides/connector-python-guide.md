---
description: Quickstart guide for MariaDB Connector/Python
---

# Connector/Python Guide

### Quickstart Guide: MariaDB Connector/Python

MariaDB Connector/Python is the official Python client library for connecting applications to MariaDB and MySQL databases. It implements the Python DB API 2.0 (PEP-249) standard, ensuring compatibility with common Python database programming patterns. The connector is written in C and Python and relies on the MariaDB Connector/C client library for efficient client-server communication.

#### 1. Prerequisites

Before installing MariaDB Connector/Python, ensure you have:

* **Python:** Version 3.7 or later.
* **MariaDB Connector/C:** Version 3.1.5 or later (for Connector/Python 1.0) or 3.3.1 or later (for Connector/Python 1.1+). On Windows, this is often handled by the `pip` installation; on Linux/macOS, you typically need to install `libmariadb-dev` or equivalent development packages via your system's package manager.

#### 2. Installation

The easiest way to install MariaDB Connector/Python is using `pip`, Python's package installer:

```bash
pip install mariadb
# Or specifically for Python 3:
# pip3 install mariadb
```

This command downloads and installs the latest stable version of the connector from PyPI.

#### 3. Basic Usage

Here's a simple Python example demonstrating how to connect to MariaDB, execute queries, and manage transactions.

```python
import mariadb
import sys

# 1. Database Connection Parameters
db_config = {
    'host': 'localhost',
    'port': 3306,
    'user': 'your_username',
    'password': 'your_password',
    'database': 'your_database_name'
}

def run_db_operations():
    conn = None
    cursor = None
    try:
        # 2. Establish a Connection
        print("Connecting to MariaDB...")
        conn = mariadb.connect(**db_config)
        print("Connection successful!")

        # 3. Create a Cursor Object
        cursor = conn.cursor()

        # --- Example: Create a Table (if it doesn't exist) ---
        try:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(255) NOT NULL,
                    email VARCHAR(255) UNIQUE
                )
            """)
            conn.commit() # Commit the transaction for DDL
            print("Table 'users' created or already exists.")
        except mariadb.Error as e:
            print(f"Error creating table: {e}")
            conn.rollback() # Rollback in case of DDL error

        # --- Example: Insert Data (Parameterized Query) ---
        print("\nInserting data...")
        insert_query = "INSERT INTO users (name, email) VALUES (?, ?)"
        try:
            cursor.execute(insert_query, ("Alice Wonderland", "alice@example.com"))
            cursor.execute(insert_query, ("Bob Builder", "bob@example.com"))
            conn.commit() # Commit the transaction for DML
            print(f"Inserted {cursor.rowcount} rows.")
            print(f"Last inserted ID: {cursor.lastrowid}")
        except mariadb.IntegrityError as e:
            print(f"Error inserting data (might be duplicate email): {e}")
            conn.rollback()
        except mariadb.Error as e:
            print(f"Error inserting data: {e}")
            conn.rollback()

        # --- Example: Select Data ---
        print("\nSelecting data...")
        select_query = "SELECT id, name, email FROM users WHERE name LIKE ?"
        cursor.execute(select_query, ("%Alice%",)) # Note the comma for single parameter tuple
        
        print("Fetched data:")
        for row in cursor:
            print(f"ID: {row[0]}, Name: {row[1]}, Email: {row[2]}")

        # --- Example: Update Data ---
        print("\nUpdating data...")
        update_query = "UPDATE users SET name = ? WHERE email = ?"
        cursor.execute(update_query, ("Alicia Wonderland", "alice@example.com"))
        conn.commit()
        print(f"Rows updated: {cursor.rowcount}")

        # --- Example: Delete Data ---
        print("\nDeleting data...")
        delete_query = "DELETE FROM users WHERE name = ?"
        cursor.execute(delete_query, ("Bob Builder",))
        conn.commit()
        print(f"Rows deleted: {cursor.rowcount}")

    except mariadb.Error as e:
        print(f"An error occurred: {e}")
        sys.exit(1)
    finally:
        # 4. Close Cursor and Connection
        if cursor:
            cursor.close()
            print("Cursor closed.")
        if conn:
            conn.close()
            print("Connection closed.")

if __name__ == "__main__":
    run_db_operations()
```

**Before Running:**

1. Replace `your_username`, `your_password`, and `your_database_name` with your actual MariaDB server credentials.
2. Ensure you have a MariaDB server running and the specified database exists.
3. The example assumes `your_table_name` is `users` with columns `id`, `name`, `email`. Adjust the table/column names as needed.

#### Important Notes:

* **Parameterized Queries:** Always use parameterized queries (e.g., `VALUES (?, ?)`) to prevent SQL injection vulnerabilities. Parameters are passed as a tuple or list to the `execute()` method.
* **Transactions (`conn.commit()` / `conn.rollback()`):** By default, MariaDB Connector/Python may have autocommit enabled. If you need explicit transaction control, ensure you call `conn.commit()` to save changes or `conn.rollback()` to undo them.
* **Error Handling:** Use `try...except mariadb.Error` blocks to gracefully handle database-related exceptions.
* **Resource Management:** Always close your `cursor` and `connection` objects in a `finally` block to ensure resources are released, even if errors occur.

#### Further Resources:

* [PyPI MariaDB Connector/Python](https://pypi.org/project/mariadb/)
* [MariaDB Connector/Python Documentation (GitHub Pages)](https://mariadb-corporation.github.io/mariadb-connector-python/usage.html)
* [MariaDB Developers Python Quickstart (GitHub)](https://github.com/mariadb-developers/python-quickstart)
