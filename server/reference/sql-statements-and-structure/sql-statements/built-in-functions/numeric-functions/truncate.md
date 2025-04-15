
# TRUNCATE

This page documents the TRUNCATE function. See [TRUNCATE TABLE](../../table-statements/truncate-table.md) for the DDL statement.


## Syntax


```
TRUNCATE(X,D)
```


## Description


Returns the number X, truncated to D decimal places. If D is 0, the
result has no decimal point or fractional part. D can be negative to
cause D digits left of the decimal point of the value X to become
zero.


## Examples


```
SELECT TRUNCATE(1.223,1);
+-------------------+
| TRUNCATE(1.223,1) |
+-------------------+
|               1.2 |
+-------------------+

SELECT TRUNCATE(1.999,1);
+-------------------+
| TRUNCATE(1.999,1) |
+-------------------+
|               1.9 |
+-------------------+

SELECT TRUNCATE(1.999,0); 
+-------------------+
| TRUNCATE(1.999,0) |
+-------------------+
|                 1 |
+-------------------+

SELECT TRUNCATE(-1.999,1);
+--------------------+
| TRUNCATE(-1.999,1) |
+--------------------+
|               -1.9 |
+--------------------+

SELECT TRUNCATE(122,-2);
+------------------+
| TRUNCATE(122,-2) |
+------------------+
|              100 |
+------------------+

SELECT TRUNCATE(10.28*100,0);
+-----------------------+
| TRUNCATE(10.28*100,0) |
+-----------------------+
|                  1028 |
+-----------------------+
```

## See Also


* [TRUNCATE TABLE](../../table-statements/truncate-table.md)

