
# SELECT ... OFFSET ... FETCH


##### MariaDB starting with [10.6.0](../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-1060-release-notes.md)
`<code>SELECT ... OFFSET ... FETCH</code>` was introduced in [MariaDB 10.6](../../../../../../release-notes/mariadb-community-server/what-is-mariadb-106.md).


## Syntax


```
OFFSET start { ROW | ROWS }
FETCH { FIRST | NEXT } [ count ] { ROW | ROWS } { ONLY | WITH TIES }
```

## Description


The `<code>OFFSET</code>` clause allows one to return only those elements of a resultset that come after a specified offset. The `<code>FETCH</code>` clause specifies the number of rows to return, while `<code>ONLY</code>` or `<code>WITH TIES</code>` specifies whether or not to also return any further results that tie for last place according to the ordered resultset.


Either the singular `<code>ROW</code>` or the plural `<code>ROWS</code>` can be used after the `<code>OFFSET</code>` and `<code>FETCH</code>` clauses; the choice has no impact on the results.


`<code>FIRST</code>` and `<code>NEXT</code>` gives the same result.


In the case of `<code>WITH TIES</code>`, an [ORDER BY](order-by.md) clause is required, otherwise an ERROR will be returned.


```
SELECT i FROM t1 FETCH FIRST 2 ROWS WITH TIES;
ERROR 4180 (HY000): FETCH ... WITH TIES requires ORDER BY clause to be present
```

## Examples


Given a table with 6 rows:


```
CREATE OR REPLACE TABLE t1 (i INT);
INSERT INTO t1 VALUES (1),(2),(3),(4), (4), (5);
SELECT i FROM t1 ORDER BY i ASC;
+------+
| i    |
+------+
|    1 |
|    2 |
|    3 |
|    4 |
|    4 |
|    5 |
+------+
```

`<code>OFFSET 2</code>` allows one to skip the first two results.


```
SELECT i FROM t1 ORDER BY i ASC OFFSET 2 ROWS;
+------+
| i    |
+------+
|    3 |
|    4 |
|    4 |
|    5 |
+------+
```

`<code>FETCH FIRST 3 ROWS ONLY</code>` limits the results to three rows only


```
SELECT i FROM t1 ORDER BY i ASC OFFSET 1 ROWS FETCH FIRST 3 ROWS ONLY;
+------+
| i    |
+------+
|    2 |
|    3 |
|    4 |
+------+
```

The same outcome can also be achieved with the [LIMIT](../../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/debugging-mariadb/limitationsdifferences-with-a-mariadb-server-compiled-for-debugging.md) clause:


```
SELECT i FROM t1 ORDER BY i ASC LIMIT 3 OFFSET 1;
+------+
| i    |
+------+
|    2 |
|    3 |
|    4 |
+------+
```

`<code>WITH TIES</code>` ensures the tied result `<code>4</code>` is also returned.


```
SELECT i FROM t1 ORDER BY i ASC OFFSET 1 ROWS FETCH FIRST 3 ROWS WITH TIES;
+------+
| i    |
+------+
|    2 |
|    3 |
|    4 |
|    4 |
+------+
```

## See Also


* [LIMIT](../../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/debugging-mariadb/limitationsdifferences-with-a-mariadb-server-compiled-for-debugging.md)
* [ORDER BY](order-by.md)
* [SELECT](../../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/benchmarks-and-long-running-tests/benchmark-results/select-random-ranges-and-select-random-point.md)

