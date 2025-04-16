
# LN

## Syntax


```
LN(X)
```

## Description


Returns the natural logarithm of X; that is, the base-e logarithm of X.
If X is less than or equal to 0, or `NULL`, then NULL is returned.


The inverse of this function is `[EXP()](../../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/outdated-pages/explain-formatjson-in-mysql.md)`.


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
