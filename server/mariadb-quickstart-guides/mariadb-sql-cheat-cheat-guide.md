---
description: Core SQL Statements Guide
icon: rabbit-running
---

# Basic SQL Statements Guide

This guide provides a quick overview of essential SQL statements in MariaDB, categorized by their function in data definition, data manipulation, and transaction control. Find brief descriptions and links to detailed documentation for each statement, along with a simple illustrative example sequence.

_(If you need a basic tutorial on how to use the MariaDB database server and execute simple commands, see_ [_A MariaDB Primer_](https://www.google.com/search?q=link_to_A_MariaDB_Primer_docs)_. Also see_ [_Essential Queries Guide_](https://www.google.com/search?q=link_to_Essential_Queries_Guide_docs) _for examples of commonly-used queries.)_

### Defining How Your Data Is Stored (Data Definition Language - DDL)

* [**CREATE DATABASE**](https://www.google.com/search?q=link_to_CREATE_DATABASE_docs): Used to create a new, empty database.
* [**DROP DATABASE**](https://www.google.com/search?q=link_to_DROP_DATABASE_docs): Used to completely destroy an existing database.
* [**USE**](https://www.google.com/search?q=link_to_USE_docs): Used to select a default database for subsequent statements.
* [**CREATE TABLE**](https://www.google.com/search?q=link_to_CREATE_TABLE_docs): Used to create a new table, which is where your data is actually stored.
* [**ALTER TABLE**](https://www.google.com/search?q=link_to_ALTER_TABLE_docs): Used to modify an existing table's definition (e.g., add/remove columns, change types).
* [**DROP TABLE**](https://www.google.com/search?q=link_to_DROP_TABLE_docs): Used to completely destroy an existing table and all its data.
* [**DESCRIBE**](https://www.google.com/search?q=link_to_DESCRIBE_docs) (or `DESC`): Shows the structure of a table (columns, data types, etc.).

### Manipulating Your Data (Data Manipulation Language - DML)

* [**SELECT**](https://www.google.com/search?q=link_to_SELECT_docs): Used when you want to read (or select) your data from one or more tables.
* [**INSERT**](https://www.google.com/search?q=link_to_INSERT_docs): Used when you want to add (or insert) new rows of data into a table.
* [**UPDATE**](https://www.google.com/search?q=link_to_UPDATE_docs): Used when you want to change (or update) existing data in a table.
* [**DELETE**](https://www.google.com/search?q=link_to_DELETE_docs): Used when you want to remove (or delete) existing rows of data from a table.
* [**REPLACE**](https://www.google.com/search?q=link_to_REPLACE_docs): Works like `INSERT`, but if an old row in the table has the same value as a new row for a `PRIMARY KEY` or a `UNIQUE` index, the old row is deleted before the new row is inserted.
* [**TRUNCATE TABLE**](https://www.google.com/search?q=link_to_TRUNCATE_TABLE_docs): Used to quickly remove all data from a table, resetting any `AUTO_INCREMENT` values. It is faster than `DELETE` without a `WHERE` clause for emptying a table.

### Transactions (Transaction Control Language - TCL)

* [**START TRANSACTION**](https://www.google.com/search?q=link_to_START_TRANSACTION_docs) (or `BEGIN`): Used to begin a new transaction, allowing multiple SQL statements to be treated as a single atomic unit.
* [**COMMIT**](https://www.google.com/search?q=link_to_COMMIT_docs): Used to save all changes made during the current transaction, making them permanent.
* [**ROLLBACK**](https://www.google.com/search?q=link_to_ROLLBACK_docs): Used to discard all changes made during the current transaction, reverting the database to its state before the transaction began.

### A Simple Example Sequence

This example demonstrates several of the statements in action:

SQL

```
-- Create a new database
CREATE DATABASE mydb;

-- Select the new database to use
USE mydb;

-- Create a new table
CREATE TABLE mytable (
    id INT PRIMARY KEY,
    name VARCHAR(20)
);

-- Insert some data
INSERT INTO mytable VALUES (1, 'Will');
INSERT INTO mytable VALUES (2, 'Marry');
INSERT INTO mytable VALUES (3, 'Dean');

-- Select specific data
SELECT id, name FROM mytable WHERE id = 1;

-- Update existing data
UPDATE mytable SET name = 'Willy' WHERE id = 1;

-- Select all data to see changes
SELECT id, name FROM mytable;

-- Delete specific data
DELETE FROM mytable WHERE id = 1;

-- Select all data again
SELECT id, name FROM mytable;

-- Drop the database (removes the database and its tables)
DROP DATABASE mydb;
```

Common Query: Counting Rows

To count the number of records in a table:

SQL

```
SELECT COUNT(*) FROM mytable; -- Or SELECT COUNT(1) FROM mytable;
```

_(Note: This query would typically be run on an existing table, for example, before it or its database is dropped.)_

CC BY-SA / Gnu FDL
