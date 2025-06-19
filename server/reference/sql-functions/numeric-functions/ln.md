
# LN

## Syntax


```
LN(X)
```

## Description


Returns the natural logarithm of X; that is, the base-e logarithm of X.
If X is less than or equal to 0, or `NULL`, then NULL is returned.


The inverse of this function is [EXP()](exp.md).


## Examples


```
SELECT LN(2);
+-------------------+
| LN(2)             |
+-------------------+
| 0.693147180559945 |
+-------------------+

SELECT LN(-2);
+--------+
| LN(-2) |
+--------+
|   NULL |
+--------+
```


<sub>_This page is licensed: GPLv2, originally from [fill\_help\_tables.sql](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)_</sub>


{% @marketo/form formId="4316" %}
