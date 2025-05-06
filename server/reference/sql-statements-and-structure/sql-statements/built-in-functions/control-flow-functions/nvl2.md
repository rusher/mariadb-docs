
# NVL2

## Syntax


```
NVL2(expr1,expr2,expr3)
```


## Description


The `NVL2` function returns a value based on whether a specified expression is NULL or not. If *expr1* is not NULL, then NVL2 returns *expr2*. If *expr1* is NULL, then NVL2 returns *expr3*.


## Examples


```
SELECT NVL2(NULL,1,2);
+----------------+
| NVL2(NULL,1,2) |
+----------------+
|              2 |
+----------------+

SELECT NVL2('x',1,2);
+---------------+
| NVL2('x',1,2) |
+---------------+
|             1 |
+---------------+
```

## See Also


* [IFNULL (or NVL)](ifnull.md)


CC BY-SA / Gnu FDL

