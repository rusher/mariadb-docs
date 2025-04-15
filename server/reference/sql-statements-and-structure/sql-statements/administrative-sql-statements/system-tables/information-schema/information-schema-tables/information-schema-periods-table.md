# Information Schema PERIODS Table

#

#### MariaDB starting with [11.4.1](/en/mariadb-1141-release-notes/)

The [Information Schema](/en/information_schema/) `PERIODS` table provides information about [Application-Time Periods](../../../../../temporal-tables/application-time-periods.md).

It contains the following columns:

| Column | Description |
| --- | --- |
| Column | Description |
| TABLE_CATALOG | Always contains the string 'def'. |
| TABLE_SCHEMA | Database name. |
| TABLE_NAME | Table name. |
| PERIOD | Period name. |
| START_COLUMN_NAME | Name of the column that starts the period. |
| END_COLUMN_NAME | Name of the column that ends the period. |

#

# Example

```
CREATE OR REPLACE TABLE t1(
 name VARCHAR(50), 
 date_1 DATE, 
 date_2 DATE, 
 PERIOD FOR date_period(date_1, date_2)
);

SELECT * FROM INFORMATION_SCHEMA.PERIODS;
+---------------+--------------+------------+-------------+-------------------+-----------------+
| TABLE_CATALOG | TABLE_SCHEMA | TABLE_NAME | PERIOD | START_COLUMN_NAME | END_COLUMN_NAME |
+---------------+--------------+------------+-------------+-------------------+-----------------+
| def | test | t1 | date_period | date_1 | date_2 |
+---------------+--------------+------------+-------------+-------------------+-----------------+
```