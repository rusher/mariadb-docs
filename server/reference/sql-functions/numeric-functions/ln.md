
# LN

## Syntax


```
LN(X)
```

## Description


Returns the natural logarithm of X; that is, the base-e logarithm of X.
If X is less than or equal to 0, or `NULL`, then NULL is returned.


The inverse of this function is `[EXP()](exp.md)`.


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


GPLv2 fill_help_tables.sql


{% @marketo/form formId="4316" %}
