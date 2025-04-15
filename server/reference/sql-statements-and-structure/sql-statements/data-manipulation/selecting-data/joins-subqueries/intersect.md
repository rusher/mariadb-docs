
# INTERSECT

The result of an intersect is the intersection of right and left `<code>SELECT</code>` results, i.e. only records that are present in both result sets will be included in the result of the operation.


## Syntax


```
SELECT ...
(INTERSECT [ALL | DISTINCT] | EXCEPT [ALL | DISTINCT] | UNION [ALL | DISTINCT]) SELECT ...
[(INTERSECT [ALL | DISTINCT] | EXCEPT [ALL | DISTINCT] | UNION [ALL | DISTINCT]) SELECT ...]
[ORDER BY [column [, column ...]]]
[LIMIT {[offset,] row_count | row_count OFFSET offset}]
```


## Description


MariaDB has supported `<code>INTERSECT</code>` (as well as [EXCEPT](except.md)) in addition to [UNION](union.md) since [MariaDB 10.3](../../../../../../../release-notes/mariadb-community-server/what-is-mariadb-103.md).


All behavior for naming columns, `<code class="fixed" style="white-space:pre-wrap">ORDER BY</code>` and `<code class="fixed" style="white-space:pre-wrap">LIMIT</code>` is the same as for [UNION](union.md).


`<code>INTERSECT</code>` implicitly supposes a `<code>DISTINCT</code>` operation.


The result of an intersect is the intersection of right and left `<code>SELECT</code>` results, i.e. only records that are present in both result sets will be included in the result of the operation.


`<code>INTERSECT</code>` has higher precedence than `<code>UNION</code>` and `<code>EXCEPT</code>` (unless running [running in Oracle mode](../../../../../../../release-notes/mariadb-community-server/compatibility-and-differences/sql_modeoracle.md), in which case all three have the same precedence). If possible it will be executed linearly but if not it will be translated to a subquery in the `<code>FROM</code>` clause:


```
(select a,b from t1)
union
(select c,d from t2)
intersect
(select e,f from t3)
union
(select 4,4);
```

will be translated to:


```
(select a,b from t1)
union
select c,d from
  ((select c,d from t2)
   intersect
   (select e,f from t3)) dummy_subselect
union
(select 4,4)
```




### Parentheses


Parentheses can be used to specify precedence. Prior to [MariaDB 10.4](../../../../../../../release-notes/mariadb-community-server/what-is-mariadb-104.md), a syntax error would be returned.



##### MariaDB starting with [10.5.0](../../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1050-release-notes.md)

### ALL/DISTINCT

`<code>INTERSECT ALL</code>` and `<code>INTERSECT DISTINCT</code>` were introduced in [MariaDB 10.5.0](../../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1050-release-notes.md). The `<code>ALL</code>` operator leaves duplicates intact, while the `<code>DISTINCT</code>` operator removes duplicates. `<code>DISTINCT</code>` is the default behavior if neither operator is supplied, and the only behavior prior to [MariaDB 10.5](../../../../../../../release-notes/mariadb-community-server/what-is-mariadb-105.md).  


## Examples


Show customers which are employees:


```
(SELECT e_name AS name, email FROM employees)
INTERSECT
(SELECT c_name AS name, email FROM customers);
```

Difference between [UNION](union.md), [EXCEPT](except.md) and INTERSECT. `<code>INTERSECT ALL</code>` and `<code>EXCEPT ALL</code>` are available from [MariaDB 10.5.0](../../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1050-release-notes.md).


```
CREATE TABLE seqs (i INT);
INSERT INTO seqs VALUES (1),(2),(2),(3),(3),(4),(5),(6);

SELECT i FROM seqs WHERE i <= 3 UNION SELECT i FROM seqs WHERE i>=3;
+------+
| i    |
+------+
|    1 |
|    2 |
|    3 |
|    4 |
|    5 |
|    6 |
+------+

SELECT i FROM seqs WHERE i <= 3 UNION ALL SELECT i FROM seqs WHERE i>=3;
+------+
| i    |
+------+
|    1 |
|    2 |
|    2 |
|    3 |
|    3 |
|    3 |
|    3 |
|    4 |
|    5 |
|    6 |
+------+

SELECT i FROM seqs WHERE i <= 3 EXCEPT SELECT i FROM seqs WHERE i>=3;
+------+
| i    |
+------+
|    1 |
|    2 |
+------+

SELECT i FROM seqs WHERE i <= 3 EXCEPT ALL SELECT i FROM seqs WHERE i>=3;
+------+
| i    |
+------+
|    1 |
|    2 |
|    2 |
+------+

SELECT i FROM seqs WHERE i <= 3 INTERSECT SELECT i FROM seqs WHERE i>=3;
+------+
| i    |
+------+
|    3 |
+------+

SELECT i FROM seqs WHERE i <= 3 INTERSECT ALL SELECT i FROM seqs WHERE i>=3;
+------+
| i    |
+------+
|    3 |
|    3 |
+------+
```

Parentheses for specifying precedence:


```
CREATE OR REPLACE TABLE t1 (a INT);
CREATE OR REPLACE TABLE t2 (b INT);
CREATE OR REPLACE TABLE t3 (c INT);

INSERT INTO t1 VALUES (1),(2),(3),(4);
INSERT INTO t2 VALUES (5),(6);
INSERT INTO t3 VALUES (1),(6);

((SELECT a FROM t1) UNION (SELECT b FROM t2)) INTERSECT (SELECT c FROM t3);
+------+
| a    |
+------+
|    1 |
|    6 |
+------+

(SELECT a FROM t1) UNION ((SELECT b FROM t2) INTERSECT (SELECT c FROM t3));
+------+
| a    |
+------+
|    1 |
|    2 |
|    3 |
|    4 |
|    6 |
+------+
```

## See Also


* [UNION](union.md)
* [EXCEPT](except.md)
* [Get Set for Set Theory: UNION, INTERSECT and EXCEPT in SQL](https://www.youtube.com/watch?v=UNi-fVSpRm0) (video tutorial)

