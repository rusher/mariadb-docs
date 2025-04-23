# MariaDB Usage

## MariaDB Quickstart Guide

This guide provides a brief introduction to using the `mariadb` command-line client to interact with a MariaDB database.

### 1. Logging into MariaDB

To connect to your MariaDB server:

```bash
mariadb -u user_name -p -h ip_address db_name
```

* Replace `user_name` with your database username.
* Replace `ip_address` with your server's hostname or IP address.
* Replace `db_name` with the name of the database you wish to access.

If you're accessing MariaDB from the same server it's hosted on, you can omit the `-h ip_address` part.

Upon successful login, you'll see a prompt like:

```bash
MariaDB [test]>
```

### 2. Setting Up the Database

To create a sample database and tables:

```sql
CREATE DATABASE IF NOT EXISTS test;
USE test;

CREATE TABLE IF NOT EXISTS books (
  BookID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
  Title VARCHAR(100) NOT NULL,
  SeriesID INT,
  AuthorID INT
);

CREATE TABLE IF NOT EXISTS authors (
  id INT NOT NULL PRIMARY KEY AUTO_INCREMENT
);

CREATE TABLE IF NOT EXISTS series (
  id INT NOT NULL PRIMARY KEY AUTO_INCREMENT
);

INSERT INTO books (Title, SeriesID, AuthorID)
VALUES
  ('The Fellowship of the Ring', 1, 1),
  ('The Two Towers', 1, 1),
  ('The Return of the King', 1, 1),
  ('The Sum of All Men', 2, 2),
  ('Brotherhood of the Wolf', 2, 2),
  ('Wizardborn', 2, 2),
  ('The Hobbbit', 0, 1);
```

Note: The `test` database may not exist by default on some systems.

### 3. Viewing Tables and Data

To list tables in the current database:

```sql
SHOW TABLES;
```

To view the structure of the `books` table:

```sql
DESCRIBE books;
```

To retrieve all records from the `books` table:

```sql
SELECT * FROM books;
```

### 4. Inserting and Modifying Data

To insert a new book into the `books` table:

```sql
INSERT INTO books (Title, SeriesID, AuthorID)
VALUES ('Lair of Bones', 2, 2);
```

To correct a typo in a book title:

```sql
UPDATE books
SET Title = 'The Hobbit'
WHERE BookID = 7;
```

### 5. Additional Resources

* [MariaDB Basics](https://mariadb.com/kb/en/mariadb-basics/)
* [Beginner MariaDB Articles](https://mariadb.com/kb/en/beginner-mariadb-articles/)

***

For a more detailed walkthrough, refer to the original article: [A MariaDB Primer](https://mariadb.com/kb/en/a-mariadb-primer/).

If you have another page you'd like converted into a quickstart guide, please provide the link.
