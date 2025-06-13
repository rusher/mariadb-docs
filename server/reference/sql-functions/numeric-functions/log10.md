
# LOG10

## Syntax


```
LOG10(X)
```

## Description


Returns the base-10 logarithm of X.


## Examples


```
SELECT LOG10(2);
+-------------------+
| LOG10(2)          |
+-------------------+
| 0.301029995663981 |
+-------------------+

SELECT LOG10(100);
+------------+
| LOG10(100) |
+------------+
|          2 |
+------------+

SELECT LOG10(-100);
+-------------+
| LOG10(-100) |
+-------------+
|        NULL |
+-------------+
```


<sub>_This page is licensed: GPLv2, originally from [fill\_help\_tables.sql](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)_</sub>


{% @marketo/form formId="4316" %}
