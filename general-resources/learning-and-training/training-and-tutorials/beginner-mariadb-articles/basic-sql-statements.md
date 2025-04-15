
# Basic SQL Statements

This page lists the most important SQL statements and contains links to their documentation pages. If you need a basic tutorial on how to use the MariaDB database server and how to execute simple commands, see [A MariaDB Primer](a-mariadb-primer.md).


Also see [Common MariaDB Queries](useful-mariadb-queries.md) for examples of commonly-used queries.


## Defining How Your Data Is Stored


* [CREATE DATABASE](../../../../server/reference/sql-statements-and-structure/sql-statements/data-definition/create/create-database.md) is used to create a new, empty database.
* [DROP DATABASE](../../../../server/reference/sql-statements-and-structure/sql-statements/data-definition/drop/drop-database.md) is used to completely destroy an existing database.
* [USE](useful-mariadb-queries.md) is used to select a default database.
* [CREATE TABLE](../../../../server/reference/sql-statements-and-structure/vectors/create-table-with-vectors.md) is used to create a new table, which is where your data is actually stored.
* [ALTER TABLE](../../../../server/reference/sql-statements-and-structure/sql-statements/data-definition/alter/alter-tablespace.md) is used to modify an existing table's definition.
* [DROP TABLE](../../../../server/reference/sql-statements-and-structure/sql-statements/data-definition/drop/drop-tablespace.md) is used to completely destroy an existing table.
* [DESCRIBE](../../../../server/reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/describe.md) shows the structure of a table.


## Manipulating Your Data


* [SELECT](../advanced-mariadb-articles/development-articles/quality/benchmarks-and-long-running-tests/benchmark-results/select-random-ranges-and-select-random-point.md) is used when you want to read (or select) your data.
* [INSERT](../../../../server/reference/sql-statements-and-structure/sql-statements/built-in-functions/string-functions/insert-function.md) is used when you want to add (or insert) new data.
* [UPDATE](../advanced-mariadb-articles/development-articles/tools/buildbot/buildbot-setup/buildbot-setup-for-virtual-machines/buildbot-setup-for-virtual-machines-additional-steps/update-debian-4-mirrors-for-buildbot-vms.md) is used when you want to change (or update) existing data.
* [DELETE](../../../../server/reference/sql-statements-and-structure/sql-statements/data-manipulation/changing-deleting-data/delete.md) is used when you want to remove (or delete) existing data.
* [REPLACE](../../../../server/reference/sql-statements-and-structure/sql-statements/built-in-functions/string-functions/replace-function.md) is used when you want to add or change (or replace) new or existing data.
* [TRUNCATE](../../../../server/reference/sql-statements-and-structure/sql-statements/table-statements/truncate-table.md) is used when you want to empty (or delete) all data from the template.


## Transactions


* [START TRANSACTION](../../../../server/reference/sql-statements-and-structure/sql-statements/transactions/start-transaction.md) is used to begin a transaction.
* [COMMIT](../../../../server/reference/sql-statements-and-structure/sql-statements/transactions/commit.md) is used to apply changes and end transaction.
* [ROLLBACK](../../../../server/reference/sql-statements-and-structure/sql-statements/transactions/rollback.md) is used to discard changes and end transaction.


### A Simple Example


```
CREATE DATABASE mydb;
USE mydb;
CREATE TABLE mytable ( id INT PRIMARY KEY, name VARCHAR(20) );
INSERT INTO mytable VALUES ( 1, 'Will' );
INSERT INTO mytable VALUES ( 2, 'Marry' );
INSERT INTO mytable VALUES ( 3, 'Dean' );
SELECT id, name FROM mytable WHERE id = 1;
UPDATE mytable SET name = 'Willy' WHERE id = 1;
SELECT id, name FROM mytable;
DELETE FROM mytable WHERE id = 1;
SELECT id, name FROM mytable;
DROP DATABASE mydb;
SELECT count(1) from mytable; gives the number of records in the table
```

*The first version of this article was copied, with permission, from [Basic_SQL_Statements](https://hashmysql.org/wiki/Basic_SQL_Statements) on 2012-10-05.*

