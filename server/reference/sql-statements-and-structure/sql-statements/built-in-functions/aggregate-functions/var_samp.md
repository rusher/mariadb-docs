# VAR_SAMP

#

# Syntax

```
VAR_SAMP(expr)
```

#

# Description

Returns the sample variance of *`expr`*. That is, the denominator is the number of rows minus one.

It is an [aggregate function](../special-functions/window-functions/aggregate-functions-as-window-functions.md), and so can be used with the [GROUP BY](../../data-manipulation/selecting-data/group-by.md) clause.

VAR_SAMP() can be used as a [window function](../special-functions/window-functions/window-functions-overview.md).

VAR_SAMP() returns `NULL` if there were no matching rows.

#

# Examples

As an [aggregate function](../special-functions/window-functions/aggregate-functions-as-window-functions.md):

```
CREATE OR REPLACE TABLE stats (category VARCHAR(2), x INT);

INSERT INTO stats VALUES 
 ('a',1),('a',2),('a',3),
 ('b',11),('b',12),('b',20),('b',30),('b',60);

SELECT category, STDDEV_POP(x), STDDEV_SAMP(x), VAR_POP(x) 
 FROM stats GROUP BY category;
+----------+---------------+----------------+------------+
| category | STDDEV_POP(x) | STDDEV_SAMP(x) | VAR_POP(x) |
+----------+---------------+----------------+------------+
| a | 0.8165 | 1.0000 | 0.6667 |
| b | 18.0400 | 20.1693 | 325.4400 |
+----------+---------------+----------------+------------+
```

As a [window function](../special-functions/window-functions/window-functions-overview.md):

```
CREATE OR REPLACE TABLE student_test (name CHAR(10), test CHAR(10), score TINYINT);

INSERT INTO student_test VALUES 
 ('Chun', 'SQL', 75), ('Chun', 'Tuning', 73), 
 ('Esben', 'SQL', 43), ('Esben', 'Tuning', 31), 
 ('Kaolin', 'SQL', 56), ('Kaolin', 'Tuning', 88), 
 ('Tatiana', 'SQL', 87);

SELECT name, test, score, VAR_SAMP(score) 
 OVER (PARTITION BY test) AS variance_results FROM student_test;
+---------+--------+-------+------------------+
| name | test | score | variance_results |
+---------+--------+-------+------------------+
| Chun | SQL | 75 | 382.9167 |
| Chun | Tuning | 73 | 873.0000 |
| Esben | SQL | 43 | 382.9167 |
| Esben | Tuning | 31 | 873.0000 |
| Kaolin | SQL | 56 | 382.9167 |
| Kaolin | Tuning | 88 | 873.0000 |
| Tatiana | SQL | 87 | 382.9167 |
+---------+--------+-------+------------------+
```

#

# See Also

* [VAR_POP](var_pop.md) (variance)
* [STDDEV_POP](stddev_pop.md) (population standard deviation)