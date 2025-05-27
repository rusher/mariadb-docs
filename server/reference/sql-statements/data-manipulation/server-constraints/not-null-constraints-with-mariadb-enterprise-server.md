
# NOT NULL Constraints with MariaDB Enterprise Server


# Overview


MariaDB Enterprise Server supports `NOT NULL` constraints to ensure that a column's value is not set to `NULL`:


When a column is declared with a `NOT NULL` constraint, Enterprise Server rejects operations that would write a NULL value to the column


# CREATE TABLE


## CREATE TABLE and NOT NULL Constraints


With MariaDB Enterprise Server, the [CREATE TABLE](../../data-definition/create/create-table.md) statement can be used to create a new table with a `NOT NULL` constraint on one or more columns:


```
CREATE TABLE hq_sales.invoices (
   invoice_id BIGINT UNSIGNED NOT NULL,
   branch_id INT NOT NULL,
   customer_id INT,
   invoice_date DATETIME(6),
   invoice_total DECIMAL(13, 2),
   payment_method ENUM('NONE', 'CASH', 'WIRE_TRANSFER', 'CREDIT_CARD', 'GIFT_CARD'),
   PRIMARY KEY (invoice_id)
);
```

# ALTER TABLE


## ALTER TABLE .. MODIFY COLUMN .. NOT NULL


With MariaDB Enterprise Server, the [ALTER TABLE](../../data-definition/alter/alter-table.md) statement can be used to add the `NOT NULL` constraint to a column using the `MODIFY COLUMN` clause:


```
ALTER TABLE hq_sales.invoices
   MODIFY COLUMN customer_id INT NOT NULL;
ALTER TABLE .. MODIFY COLUMN .. NULL
```

With MariaDB Enterprise Server, the [ALTER TABLE](../../data-definition/alter/alter-table.md) statement can be used to remove the `NOT NULL` constraint from a column using the `MODIFY COLUMN` clause:


```
ALTER TABLE hq_sales.invoices
   MODIFY COLUMN customer_id INT NULL;
```


Copyright © 2025 MariaDB

