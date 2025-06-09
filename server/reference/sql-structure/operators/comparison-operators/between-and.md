# BETWEEN AND

## Syntax

```
expr BETWEEN min AND max
```

## Description

If expr is greater than or equal to min and expr is less than or equal\
to max, BETWEEN returns 1, otherwise it returns 0. This is equivalent\
to the expression (min <= expr AND expr <= max) if all the arguments\
are of the same type. Otherwise type conversion takes place according\
to the rules described at [Type Conversion](../../../sql-functions/string-functions/type-conversion.md), but\
applied to all the three arguments.

## Examples

```
SELECT 1 BETWEEN 2 AND 3;
+-------------------+
| 1 BETWEEN 2 AND 3 |
+-------------------+
|                 0 |
+-------------------+
```

```
SELECT 'b' BETWEEN 'a' AND 'c';
+-------------------------+
| 'b' BETWEEN 'a' AND 'c' |
+-------------------------+
|                       1 |
+-------------------------+
```

```
SELECT 2 BETWEEN 2 AND '3';
+---------------------+
| 2 BETWEEN 2 AND '3' |
+---------------------+
|                   1 |
+---------------------+
```

```
SELECT 2 BETWEEN 2 AND 'x-3';
+-----------------------+
| 2 BETWEEN 2 AND 'x-3' |
+-----------------------+
|                     0 |
+-----------------------+
1 row in set, 1 warning (0.00 sec)

Warning (Code 1292): Truncated incorrect DOUBLE value: 'x-3'
```

NULL:

```
SELECT 1 BETWEEN 1 AND NULL;
+----------------------+
| 1 BETWEEN 1 AND NULL |
+----------------------+
|                 NULL |
+----------------------+
```

DATE, DATETIME and TIMESTAMP examples. Omitting the time component compares against `00:00`, so later times on the same date are not returned:

```
CREATE TABLE `x` (
  a date ,
  b datetime,
  c timestamp
)

INSERT INTO x VALUES 
 ('2018-11-11', '2018-11-11 05:15', '2018-11-11 05:15'), 
 ('2018-11-12', '2018-11-12 05:15', '2018-11-12 05:15'); 

SELECT * FROM x WHERE a BETWEEN '2018-11-11' AND '2018-11-12';
+------------+---------------------+---------------------+
| a          | b                   | c                   |
+------------+---------------------+---------------------+
| 2018-11-11 | 2018-11-11 05:15:00 | 2018-11-11 05:15:00 |
| 2018-11-12 | 2018-11-12 05:15:00 | 2018-11-12 05:15:00 |
+------------+---------------------+---------------------+

SELECT * FROM x WHERE b BETWEEN '2018-11-11' AND '2018-11-12';
+------------+---------------------+---------------------+
| a          | b                   | c                   |
+------------+---------------------+---------------------+
| 2018-11-11 | 2018-11-11 05:15:00 | 2018-11-11 05:15:00 |
+------------+---------------------+---------------------+

SELECT * FROM x WHERE c BETWEEN '2018-11-11' AND '2018-11-12';
+------------+---------------------+---------------------+
| a          | b                   | c                   |
+------------+---------------------+---------------------+
| 2018-11-11 | 2018-11-11 05:15:00 | 2018-11-11 05:15:00 |
+------------+---------------------+---------------------+
```

## See Also

* [Operator Precedence](../operator-precedence.md)

GPLv2 fill\_help\_tables.sql

{% @marketo/form formId="4316" %}
