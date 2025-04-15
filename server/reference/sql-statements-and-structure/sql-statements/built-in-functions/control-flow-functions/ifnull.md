
# IFNULL

## Syntax


```
IFNULL(expr1,expr2)
NVL(expr1,expr2)
```


## Description


If *`<code>expr1</code>`* is not NULL, IFNULL() returns *`<code>expr1</code>`*; otherwise it returns
*`<code>expr2</code>`*. IFNULL() returns a numeric or string value, depending on the
context in which it is used.


From [MariaDB 10.3](../../../../../../release-notes/mariadb-community-server/what-is-mariadb-103.md), NVL() is an alias for IFNULL().


## Examples


```
SELECT IFNULL(1,0); 
+-------------+
| IFNULL(1,0) |
+-------------+
|           1 |
+-------------+

SELECT IFNULL(NULL,10);
+-----------------+
| IFNULL(NULL,10) |
+-----------------+
|              10 |
+-----------------+

SELECT IFNULL(1/0,10);
+----------------+
| IFNULL(1/0,10) |
+----------------+
|        10.0000 |
+----------------+

SELECT IFNULL(1/0,'yes');
+-------------------+
| IFNULL(1/0,'yes') |
+-------------------+
| yes               |
+-------------------+
```

## See Also


* [NULL values](../../../../data-types/null-values.md)
* [IS NULL operator](../../../operators/comparison-operators/is-null.md)
* [IS NOT NULL operator](../../../operators/comparison-operators/is-not-null.md)
* [COALESCE function](../../../operators/comparison-operators/coalesce.md)
* [NULLIF function](nullif.md)
* [CONNECT data types](../../../../storage-engines/connect/connect-data-types.md#null-handling)

