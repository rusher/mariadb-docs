
# NOT IN

## Syntax


```
expr NOT IN (value,...)
```

## Description


This is the same as NOT (expr [IN](../../../../../columnstore/columnstore-getting-started/preparing-and-installing-mariadb-columnstore-11x/installing-and-configuring-a-multi-server-columnstore-system-11x.md) (value,...)).


## Examples


```
SELECT 2 NOT IN (0,3,5,7);
+--------------------+
| 2 NOT IN (0,3,5,7) |
+--------------------+
|                  1 |
+--------------------+
```

```
SELECT 'wefwf' NOT IN ('wee','wefwf','weg');
+--------------------------------------+
| 'wefwf' NOT IN ('wee','wefwf','weg') |
+--------------------------------------+
|                                    0 |
+--------------------------------------+
```

```
SELECT 1 NOT IN ('1', '2', '3');
+--------------------------+
| 1 NOT IN ('1', '2', '3') |
+--------------------------+
|                        0 |
+--------------------------+
```

NULL:


```
SELECT NULL NOT IN (1, 2, 3);
+-----------------------+
| NULL NOT IN (1, 2, 3) |
+-----------------------+
|                  NULL |
+-----------------------+

SELECT 1 NOT IN (1, 2, NULL);
+-----------------------+
| 1 NOT IN (1, 2, NULL) |
+-----------------------+
|                     0 |
+-----------------------+

SELECT 5 NOT IN (1, 2, NULL);
+-----------------------+
| 5 NOT IN (1, 2, NULL) |
+-----------------------+
|                  NULL |
+-----------------------+
```
