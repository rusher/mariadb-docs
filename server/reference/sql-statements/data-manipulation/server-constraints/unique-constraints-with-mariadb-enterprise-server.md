# unique-constraints-with-mariadb-enterprise-server

## UNIQUE Constraints with MariaDB Enterprise Server

## Overview

MariaDB Enterprise Server supports `UNIQUE` constraints to ensure that a column's value is unique within a table:

* Enterprise Server uses unique indexes to speed up query execution and enforce unique constraints
* Enterprise Server supports single column and composite (multi-column) unique indexes
* MariaDB Community Server can have up to 64 total indexes for a given table.
* MariaDB Enterprise Server can have up to 128 total indexes for a given table.
* InnoDB stores unique indexes in the same tablespace file as the clustered index and data.
* Unique indexes are B+ trees, which are very efficient for searching for exact values, performing range scans, and checking uniqueness.
* If no primary key is defined for a table, then InnoDB will use the table's first `NOT NULL` unique index as the table's primary key.
* If no primary key or `NOT NULL` unique index is defined for a table, then InnoDB will automatically create a primary key called `GEN_CLUST_INDEX`, using an internal `48-bit DB_ROW_ID` column as the key. Replication with such tables can be very slow, especially when [binlog\_format](../../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#binlog_format) is `MIXED or ROW`.

## unique\_checks System Variable

MariaDB Enterprise Server provides the [unique\_checks system variable](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#unique_checks), which can be used to disable unique checks.

When unique checks are disabled, the InnoDB change buffer is used for inserts into unique indexes, and duplicate values will not be detected.

Disabling unique checks can speed up bulk data loads, but it is dangerous to do so.

## Creating an InnoDB Table with a Single Column Unique Index

Let's create an InnoDB table with a single column unique index after confirming that the default storage engine is InnoDB:

1. Connect to the server using MariaDB Client:

```
$ mariadb --user=root
```

2. Confirm that the default storage engine is InnoDB by checking the [default\_storage\_engine system variable](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#default_storage_engine) using the [SHOW SESSION VARIABLES](../../administrative-sql-statements/show/show-variables.md) statement:

```
SHOW SESSION VARIABLES
   LIKE 'default_storage_engine';
```

```
+------------------------+--------+
| Variable_name          | Value  |
+------------------------+--------+
| default_storage_engine | InnoDB |
+------------------------+--------+
```

3. If the database does not exist, then create the database for the table using the [CREATE DATABASE](../../data-definition/create/create-database.md) statement:

```
CREATE DATABASE hq_sales;
```

4. Create the table using the [CREATE TABLE](../../data-definition/create/create-table.md) statement and specify the unique index with the `UNIQUE INDEX()` clause:

```
CREATE TABLE hq_sales.customers (
   customer_id BIGINT AUTO_INCREMENT NOT NULL,
   customer_name VARCHAR(500),
   customer_email VARCHAR(200),
   PRIMARY KEY(customer_id),
   UNIQUE INDEX(customer_email)
);
```

5. For a single column unique index, the unique index can also be specified with the `UNIQUE` column option:

```
CREATE TABLE hq_sales.customers (
   customer_id BIGINT AUTO_INCREMENT NOT NULL,
   customer_name VARCHAR(500),
   customer_email VARCHAR(200) UNIQUE,
   PRIMARY KEY(customer_id)
);
```

## Creating an InnoDB Table with a Composite Unique Index

Let's create an InnoDB table with a composite (multi-column) unique index after confirming that the default storage engine is InnoDB:

1. Connect to the server using MariaDB Client:

```
$ mariadb --user=root
```

2. Confirm that the default storage engine is InnoDB by checking the [default\_storage\_engine system variable](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#default_storage_engine) using the [SHOW SESSION VARIABLES](../../administrative-sql-statements/show/show-variables.md) statement:

```
SHOW SESSION VARIABLES
   LIKE 'default_storage_engine';
```

```
+------------------------+--------+
| Variable_name          | Value  |
+------------------------+--------+
| default_storage_engine | InnoDB |
+------------------------+--------+
```

3. If the database does not exist, then create the database for the table using the [CREATE DATABASE](../../data-definition/create/create-database.md) statement:

```
CREATE DATABASE hq_sales;
```

4. Create the table using the [CREATE TABLE](../../data-definition/create/create-table.md) statement and specify the unique index with the UNIQUE INDEX() clause:

```
CREATE TABLE hq_sales.invoices (
   invoice_id BIGINT UNSIGNED NOT NULL,
   branch_id INT NOT NULL,
   customer_id INT,
   invoice_date DATETIME(6),
   invoice_total DECIMAL(13, 2),
   payment_method ENUM('NONE', 'CASH', 'WIRE_TRANSFER', 'CREDIT_CARD', 'GIFT_CARD'),
   PRIMARY KEY(invoice_id),
   UNIQUE INDEX(invoice_date, customer_id, branch_id)
);
```

## Creating an InnoDB Table with a Unique Index on a Column Prefix

Let's create an InnoDB table with a unique index on a single column prefix after confirming that the default storage engine is InnoDB:

1. Connect to the server using MariaDB Client:

```
$ mariadb --user=root
```

2. Confirm that the default storage engine is InnoDB by checking the [default\_storage\_engine system variable](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#default_storage_engine) using the [SHOW SESSION VARIABLES](../../administrative-sql-statements/show/show-variables.md) statement:

```
SHOW SESSION VARIABLES
   LIKE 'default_storage_engine';
```

```
+------------------------+--------+
| Variable_name          | Value  |
+------------------------+--------+
| default_storage_engine | InnoDB |
+------------------------+--------+
```

3. If the database does not exist, then create the database for the table using the [CREATE DATABASE](../../data-definition/create/create-database.md) statement:

```
CREATE DATABASE hq_sales;
```

4. Create the table using the [CREATE TABLE](../../data-definition/create/create-table.md) statement and specify the unique index with the `UNIQUE INDEX()` clause:

```
CREATE TABLE hq_sales.products (
   product_id BIGINT AUTO_INCREMENT NOT NULL,
   product_name VARCHAR(500),
   product_brand VARCHAR(500),
   product_description TEXT,
   PRIMARY KEY(product_id),
   UNIQUE INDEX(product_description(1000))
);
```

The unique index is specified with the `product_description(1000)` prefix, so only the first 1000 characters of the `product_description` column for each row will be indexed and checked for uniqueness.

## Adding a Unique Index to an InnoDB Table

Let's create an InnoDB table without a unique index, and then add a unique index to it:

1. Connect to the server using MariaDB Client:

```
$ mariadb --user=root
```

2. Confirm that the default storage engine is InnoDB by checking the [default\_storage\_engine system variable](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#default_storage_engine) using the [SHOW SESSION VARIABLES](../../administrative-sql-statements/show/show-variables.md) statement:

```
SHOW SESSION VARIABLES
   LIKE 'default_storage_engine';
```

```
+------------------------+--------+
| Variable_name          | Value  |
+------------------------+--------+
| default_storage_engine | InnoDB |
+------------------------+--------+
```

3. If the database does not exist, then create the database for the table using the [CREATE DATABASE](../../data-definition/create/create-database.md) statement:

```
CREATE DATABASE hq_sales;
```

4. Create the table without a primary key using the [CREATE TABLE](../../data-definition/create/create-table.md) statement:

```
CREATE TABLE hq_sales.customers (
   customer_id BIGINT AUTO_INCREMENT NOT NULL,
   customer_name VARCHAR(500),
   customer_email VARCHAR(200),
   PRIMARY KEY(customer_id)
);
```

5. Alter the table using the [ALTER TABLE](../../data-definition/alter/alter-table.md) statement and specify the new unique index with the `ADD UNIQUE INDEX()` clause:

```
ALTER TABLE hq_sales.customers ADD UNIQUE INDEX (customer_email);
```

## Dropping a Unique Index from an InnoDB Table

Let's drop the unique index from the table created in the [Creating an InnoDB Table with a Single Column Unique Index](unique-constraints-with-mariadb-enterprise-server.md#creating-an-innodb-table-with-a-single-column-unique-index) section:

1. Obtain the name of the index by joining the [information\_schema.INNODB\_SYS\_INDEXES](../../administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb_sys_indexes-table.md), [information\_schema.INNODB\_SYS\_TABLES](../../administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb_sys_tables-table.md), and [information\_schema.INNODB\_SYS\_FIELDS](../../administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb_sys_fields-table.md) tables:

```
SELECT isi.NAME AS index_name, isf.NAME AS index_column
FROM information_schema.INNODB_SYS_INDEXES isi
JOIN information_schema.INNODB_SYS_TABLES ist
ON isi.TABLE_ID = ist.TABLE_ID
JOIN information_schema.INNODB_SYS_FIELDS isf
ON isi.INDEX_ID = isf.INDEX_ID
WHERE ist.NAME = 'hq_sales/customers'
ORDER BY isf.INDEX_ID, isf.POS;
```

```
+----------------+----------------+
| index_name     | index_column   |
+----------------+----------------+
| PRIMARY        | customer_id    |
| customer_email | customer_email |
+----------------+----------------+
```

2. Alter the table using the [ALTER TABLE](../../data-definition/alter/alter-table.md) statement and specify the `DROP INDEX` clause:

```
ALTER TABLE hq_sales.customers DROP INDEX customer_email;
```

## Rebuilding a Unique Index in an InnoDB Table

Let's rebuild the unique index in the table created in the [Creating an InnoDB Table with a Single Column Unique Index](unique-constraints-with-mariadb-enterprise-server.md#creating-an-innodb-table-with-a-single-column-unique-index) section:

1. Obtain the name of the index by joining the [information\_schema.INNODB\_SYS\_INDEXES](../../administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb_sys_indexes-table.md), [information\_schema.INNODB\_SYS\_TABLES](../../administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb_sys_tables-table.md), and [information\_schema.INNODB\_SYS\_FIELDS](../../administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb_sys_fields-table.md) tables:

```
SELECT isi.NAME AS index_name, isf.NAME AS index_column
FROM information_schema.INNODB_SYS_INDEXES isi
JOIN information_schema.INNODB_SYS_TABLES ist
ON isi.TABLE_ID = ist.TABLE_ID
JOIN information_schema.INNODB_SYS_FIELDS isf
ON isi.INDEX_ID = isf.INDEX_ID
WHERE ist.NAME = 'hq_sales/customers'
ORDER BY isf.INDEX_ID, isf.POS;
```

```
+----------------+----------------+
| index_name     | index_column   |
+----------------+----------------+
| PRIMARY        | customer_id    |
| customer_email | customer_email |
+----------------+----------------+
```

2. Alter the table using the [ALTER TABLE](../../data-definition/alter/alter-table.md) statement and specify the `DROP INDEX` clause:

```
ALTER TABLE hq_sales.customers DROP INDEX customer_email;
```

3. Alter the table using the [ALTER TABLE](../../data-definition/alter/alter-table.md) statement and specify the unique index with the `ADD UNIQUE INDEX()` clause:

```
ALTER TABLE hq_sales.customers ADD UNIQUE INDEX (customer_email);
```

Copyright © 2025 MariaDB
