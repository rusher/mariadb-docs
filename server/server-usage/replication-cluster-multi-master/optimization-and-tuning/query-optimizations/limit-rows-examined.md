
# LIMIT ROWS EXAMINED

## Syntax


```
SELECT ... FROM ... WHERE ...
[group_clause] [order_clause]
LIMIT [[offset,] row_count] ROWS EXAMINED rows_limit;
```

Similar to the parameters of `<code>LIMIT</code>`, *`<code>rows_limit</code>`* can be both a
prepared statement parameter, or a stored program parameter.


## Description


The purpose of this optimization is to provide the means to terminate the
execution of `<code>[SELECT](../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/benchmarks-and-long-running-tests/benchmark-results/select-random-ranges-and-select-random-point.md)</code>` statements which examine too many rows, and
thus use too many resources. This is achieved through an extension of the
`<code>[LIMIT](../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/benchmarks-and-long-running-tests/benchmark-results/select-random-ranges-and-select-random-point.md#limit)</code>` clause —
`<code class="fixed" style="white-space:pre-wrap">LIMIT ROWS EXAMINED number_of_rows </code>`. Whenever possible the
semantics of `<code>LIMIT ROWS EXAMINED</code>` is the same as that of normal `<code>LIMIT</code>`
(for instance for aggregate functions).


The `<code>LIMIT ROWS EXAMINED</code>` clause is taken into account by the query engine
only during query execution. Thus the clause is ignored in the following cases:


* If a query is `<code>[EXPLAIN](../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/outdated-pages/explain-formatjson-in-mysql.md)</code>`-ed.
* During query optimization.
* During auxiliary operations such as writing to system tables (e.g. logs).


The clause is not applicable to `<code>[DELETE](../../../../reference/sql-statements-and-structure/sql-statements/data-manipulation/changing-deleting-data/delete.md)</code>` or `<code>[UPDATE](../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/tools/buildbot/buildbot-setup/buildbot-setup-for-virtual-machines/buildbot-setup-for-virtual-machines-additional-steps/update-debian-4-mirrors-for-buildbot-vms.md)</code>`
statements, and if used in those statements produces a syntax error.


The effects of this clause are as follows:


* The server counts the number of read, inserted, modified, and deleted rows
 during query execution. This takes into account the use of temporary tables,
 and sorting for intermediate query operations.
* Once the counter exceeds the value specified in the LIMIT ROWS EXAMINED
 clause, query execution is terminated as soon as possible.
* The effects of terminating the query because of LIMIT ROWS EXAMINED are as
 follows:

  * The result of the query is a subset of the complete query, depending on when
 the query engine detected that the limit was reached. The result may be
 empty if no result rows could be computed before reaching the limit.
  * A warning is generated of the form: "Query execution was interrupted. The
 query examined at least 100 rows, which exceeds LIMIT ROWS EXAMINED (20).
 The query result may be incomplete."
  * If query processing was interrupted during filesort, an error is returned in
 addition to the warning.
  * If a UNION was interrupted during execution of one of its queries, the last
 step of the UNION is still executed in order to produce a partial result.
  * Depending on the join and other execution strategies used for a query, the
 same query may produce no result at all, or a different subset of the
 complete result when terminated due to LIMIT ROWS EXAMINED.
  * If the query contains a GROUP BY clause, the last group where the limit was
 reached will be discarded.


The `<code>LIMIT ROWS EXAMINED</code>` clause cannot be specified on a per-subquery basis.
There can be only one `<code>LIMIT ROWS EXAMINED</code>` clause for the whole `<code>SELECT</code>`
statement. If a `<code>SELECT</code>` statement contains several subqueries
with `<code>LIMIT ROWS EXAMINED</code>`, the one that is parsed last is taken into
account.


## Examples


A simple example of the clause is:


```
SELECT * from t1, t2 LIMIT 10 ROWS EXAMINED 10000;
```

The `<code>LIMIT ROWS EXAMINED</code>` clause is global for the whole statement.


If a composite query (such as `<code>UNION</code>`, or query with derived tables or with
subqueries) contains more than one `<code>LIMIT ROWS EXAMINED</code>`, the last one parsed
is taken into account. In this manner either the last or the outermost one is
taken into account. For instance, in the query:


```
SELECT * FROM t1
WHERE c1 IN (SELECT * FROM t2 WHERE c2 > ' ' LIMIT ROWS EXAMINED 0)
LIMIT ROWS EXAMINED 11;
```

The limit that is taken into account is 11, not 0.

