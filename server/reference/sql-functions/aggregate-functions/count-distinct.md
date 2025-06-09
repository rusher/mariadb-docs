# COUNT DISTINCT

## Syntax

```
COUNT(DISTINCT expr,[expr...])
```

## Description

Returns a count of the number of different non-NULL values.

COUNT(DISTINCT) returns 0 if there were no matching rows.

Although, from [MariaDB 10.2.0](broken-reference), [COUNT](count.md) can be used as a [window function](../special-functions/window-functions/), COUNT DISTINCT cannot be.

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

GPLv2 fill\_help\_tables.sql

{% @marketo/form formId="4316" %}
