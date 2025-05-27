
# Table Value Constructors

## Syntax


```
VALUES ( row_value[, row_value...]), (...)...
```

## Description



In Unions, Views, and sub-queries, a Table Value Constructor (TVC) allows you to inject arbitrary values into the result-set. The given values must have the same number of columns as the result-set, otherwise it returns Error 1222.


## Examples


Using TVC's with `[UNION](../sql-statements/data-manipulation/selecting-data/joins-subqueries/union.md)` operations:


```
CREATE TABLE test.t1 (val1 INT, val2 INT);
INSERT INTO test.t1 VALUES(5, 8), (3, 4), (1, 2);

SELECT * FROM test.t1
UNION
VALUES (70, 90), (100, 110);

+------+------+
| val1 | val2 |
+------+------+
|    5 |    8 | 
|    3 |    4 |
|    1 |    2 |
|   70 |   90 |
|  100 |  110 |
+------+------+
```

Using TVC's with a `[CREATE VIEW](../../../server-usage/programming-customizing-mariadb/views/create-view.md)` statement:


```
CREATE VIEW v1 AS VALUES (7, 9), (9, 10);

SELECT * FROM v1;
+---+----+
| 7 |  9 |
+---+----+
| 7 |  9 |
| 9 | 10 |
+---+----+
```

Using TVC with an `[ORDER BY](../sql-statements/data-manipulation/selecting-data/order-by.md)` clause:


```
SELECT * FROM test.t1
UNION
VALUES (10, 20), (30, 40), (50, 60), (70, 80)
ORDER BY val1 DESC;
```

Using TVC with `[LIMIT](../sql-statements/data-manipulation/selecting-data/limit.md)` clause:


```
SELECT * FROM test.t1
UNION
VALUES (10, 20), (30, 40), (50, 60), (70, 80)
LIMIT 2 OFFSET 4;

+------+------+
| val1 | val2 |
+------+------+
|   30 |   40 | 
|   50 |   60 |
+------+------+
```


CC BY-SA / Gnu FDL

