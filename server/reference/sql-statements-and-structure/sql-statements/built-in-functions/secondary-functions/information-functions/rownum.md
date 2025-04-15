
# ROWNUM


##### MariaDB starting with [10.6.1](../../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-1061-release-notes.md)
From [MariaDB 10.6.1](../../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-1061-release-notes.md), the `<code class="fixed" style="white-space:pre-wrap">ROWNUM()</code>` function is supported.



## Syntax


```
ROWNUM()
```

In [Oracle mode](../../../../../../../release-notes/mariadb-community-server/compatibility-and-differences/sql_modeoracle.md) one can just use `<code class="fixed" style="white-space:pre-wrap">ROWNUM</code>`, without the parentheses.


## Description


`<code class="fixed" style="white-space:pre-wrap">ROWNUM()</code>` returns the current number of accepted rows in the
current context. It main purpose is to emulate the `<code class="fixed" style="white-space:pre-wrap">ROWNUM</code>`
[pseudo column in Oracle](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/ROWNUM-Pseudocolumn.html#GUID-2E40EC12-3FCF-4A4F-B5F2-6BC669021726). For MariaDB native applications, we recommend the usage of [LIMIT](../../../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/debugging-mariadb/limitationsdifferences-with-a-mariadb-server-compiled-for-debugging.md), as it is easier to use and gives more predictable results than the usage of `<code class="fixed" style="white-space:pre-wrap">ROWNUM()</code>`.


The main difference between using `<code class="fixed" style="white-space:pre-wrap">LIMIT</code>` and
`<code class="fixed" style="white-space:pre-wrap">ROWNUM()</code>` to limit the rows in the result is that
`<code class="fixed" style="white-space:pre-wrap">LIMIT</code>` works on the result set while `<code class="fixed" style="white-space:pre-wrap">ROWNUM</code>`
works on the number of accepted rows (before any `<code class="fixed" style="white-space:pre-wrap">ORDER</code>` or
`<code class="fixed" style="white-space:pre-wrap">GROUP BY</code>` clauses).


The following queries will return the same results:


```
SELECT * from t1 LIMIT 10;
SELECT * from t1 WHERE ROWNUM() <= 10;
```

While the following may return different results based on in which orders the rows are found:


```
SELECT * from t1 ORDER BY a LIMIT 10;
SELECT * from t1 ORDER BY a WHERE ROWNUM() <= 10;
```

The recommended way to use `<code class="fixed" style="white-space:pre-wrap">ROWNUM</code>` to limit the number of returned rows and get predictable results is to have the query in a subquery and test for `<code class="fixed" style="white-space:pre-wrap">ROWNUM()</code>` in the outer query:


```
SELECT * FROM (select * from t1 ORDER BY a) WHERE ROWNUM() <= 10;
```

`<code class="fixed" style="white-space:pre-wrap">ROWNUM()</code>` can be used in the following contexts:


* [SELECT](../../../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/benchmarks-and-long-running-tests/benchmark-results/select-random-ranges-and-select-random-point.md)
* [INSERT](../../string-functions/insert-function.md)
* [UPDATE](../../../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/tools/buildbot/buildbot-setup/buildbot-setup-for-virtual-machines/buildbot-setup-for-virtual-machines-additional-steps/update-debian-4-mirrors-for-buildbot-vms.md)
* [DELETE](../../../data-manipulation/changing-deleting-data/delete.md)
* [LOAD DATA INFILE](../../../data-manipulation/inserting-loading-data/load-data-into-tables-or-index/load-data-infile.md)


Used in other contexts, `<code class="fixed" style="white-space:pre-wrap">ROWNUM()</code>` will return 0.


## Examples


```
INSERT INTO t1 VALUES (1,ROWNUM()),(2,ROWNUM()),(3,ROWNUM());

INSERT INTO t1 VALUES (1),(2) returning a, ROWNUM();

UPDATE t1 SET row_num_column=ROWNUM();

DELETE FROM t1 WHERE a < 10 AND ROWNUM() < 2;

LOAD DATA INFILE 'filename' into table t1 fields terminated by ',' 
  lines terminated by "\r\n" (a,b) set c=ROWNUM();
```

## Optimizations


In many cases where `<code class="fixed" style="white-space:pre-wrap">ROWNUM()</code>` is used, MariaDB will use the same optimizations it uses with [LIMIT](../../../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/debugging-mariadb/limitationsdifferences-with-a-mariadb-server-compiled-for-debugging.md).


`<code class="fixed" style="white-space:pre-wrap">LIMIT</code>` optimization is possible when using `<code class="fixed" style="white-space:pre-wrap">ROWNUM</code>` in the following manner:


* When one is in a top level `<code class="fixed" style="white-space:pre-wrap">WHERE</code>` clause comparing `<code class="fixed" style="white-space:pre-wrap">ROWNUM()</code>` with a numerical constant using any of the following expressions:

  * `<code class="fixed" style="white-space:pre-wrap">ROWNUM()</code>` < number
  * `<code class="fixed" style="white-space:pre-wrap">ROWNUM()</code>` <= number
  * `<code class="fixed" style="white-space:pre-wrap">ROWNUM()</code>` = 1
`<code class="fixed" style="white-space:pre-wrap">ROWNUM()</code>` can be also be the right argument to the comparison function.


In the above cases, `<code class="fixed" style="white-space:pre-wrap">LIMIT</code>` optimization can be done in the
following cases:


* For the current sub query when the ROWNUM comparison is done on the top level:


```
SELECT * from t1 WHERE ROWNUM() <= 2 AND t1.a > 0
```

* For an inner sub query, when the upper level has only a `<code class="fixed" style="white-space:pre-wrap">ROWNUM()</code>` comparison in the `<code class="fixed" style="white-space:pre-wrap">WHERE</code>` clause:


```
SELECT * from (select * from t1) as t WHERE ROWNUM() <= 2
```

## Other Changes Related to ROWNUM


When `<code class="fixed" style="white-space:pre-wrap">ROWNUM()</code>` is used anywhere in a query, the optimization to ignore `<code>ORDER BY</code>` in subqueries are disabled.


This was done to get the following common Oracle query to work as expected:


```
select * from (select * from t1 order by a desc) as t where rownum() <= 2;
```

By default MariaDB ignores any `<code>ORDER BY</code>` in subqueries both because the SQL standard defines results sets in subqueries to be un-ordered and because of performance reasons (especially when using views in subqueries). See [MDEV-3926](https://jira.mariadb.org/browse/MDEV-3926) "Wrong result with GROUP BY ... WITH ROLLUP" for a discussion of this topic.


## Other Considerations


While MariaDB tries to emulate Oracle's usage of `<code class="fixed" style="white-space:pre-wrap">ROWNUM()</code>` as closely as possible, there are cases where the result is different:


* When the optimizer finds rows in a different order (because of different storage methods or optimization). This may also happen in Oracle if one adds or deletes an index, in which case the rows may be found in a different order.


Note that usage of `<code class="fixed" style="white-space:pre-wrap">ROWNUM()</code>` in functions or [stored procedures](../../../../../../server-usage/programming-customizing-mariadb/stored-routines/stored-procedures/README.md) will use their own context, not the caller's context.


## See Also


* [MDEV-24089](https://jira.mariadb.org/browse/MDEV-24089) support oracle syntax: rownum
* [LIMIT clause](../../../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/debugging-mariadb/limitationsdifferences-with-a-mariadb-server-compiled-for-debugging.md)

