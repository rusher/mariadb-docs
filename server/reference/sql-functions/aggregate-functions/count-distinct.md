# COUNT DISTINCT

## Syntax

```
COUNT(DISTINCT expr,[expr...])
```

## Description

Returns a count of the number of different non-NULL values.

COUNT(DISTINCT) returns 0 if there were no matching rows.

Although, from [MariaDB 10.2.0](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/sql-functions/aggregate-functions/broken-reference/README.md), [COUNT](count.md) can be used as a [window function](../special-functions/window-functions/), COUNT DISTINCT cannot be.

## Examples

```
CREATE TABLE student (name CHAR(10), test CHAR(10), score TINYINT); 

INSERT INTO student VALUES 
  ('Chun', 'SQL', 75), ('Chun', 'Tuning', 73), 
  ('Esben', 'SQL', 43), ('Esben', 'Tuning', 31), 
  ('Kaolin', 'SQL', 56), ('Kaolin', 'Tuning', 88), 
  ('Tatiana', 'SQL', 87), ('Tatiana', 'Tuning', 83);

SELECT COUNT(*) FROM student;
+----------+
| COUNT(*) |
+----------+
|        8 |
+----------+

SELECT COUNT(DISTINCT (name)) FROM student;
+------------------------+
| COUNT(DISTINCT (name)) |
+------------------------+
|                      4 |
+------------------------+
```

## See Also

* [SELECT](../../sql-statements/data-manipulation/selecting-data/select.md)
* [COUNT](count.md)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
