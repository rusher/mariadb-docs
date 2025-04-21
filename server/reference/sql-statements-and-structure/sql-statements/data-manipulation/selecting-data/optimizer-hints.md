
# Optimizer Hints

Optimizer hints are options available that affect the execution plan.


## SELECT Modifiers


### HIGH PRIORITY


`HIGH_PRIORITY` gives the statement a higher priority. If the table is locked, high priority `SELECT`s will be executed as soon as the lock is released, even if other statements are queued. `HIGH_PRIORITY` applies only if the storage engine only supports table-level locking (`MyISAM`, `MEMORY`, `MERGE`). See [HIGH_PRIORITY and LOW_PRIORITY clauses](../changing-deleting-data/high_priority-and-low_priority.md) for details.


### SQL_CACHE / SQL_NO_CACHE


If the [query_cache_type](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#query_cache_type) system variable is set to 2 or `DEMAND`, and the current statement is cacheable, `SQL_CACHE` causes the query to be cached and `SQL_NO_CACHE` causes the query not to be cached. For `UNION`s, `SQL_CACHE` or `SQL_NO_CACHE` should be specified for the first query. See also [The Query Cache](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/buffers-caches-and-threads/query-cache.md) for more detail and a list of the types of statements that aren't cacheable.


### SQL_BUFFER_RESULT


`SQL_BUFFER_RESULT` forces the optimizer to use a temporary table to process the result. This is useful to free locks as soon as possible.


### SQL_SMALL_RESULT / SQL_BIG_RESULT


`SQL_SMALL_RESULT` and `SQL_BIG_RESULT` tell the optimizer whether the result is very big or not. Usually, `GROUP BY` and `DISTINCT` operations are performed using a temporary table. Only if the result is very big, using a temporary table is not convenient. The optimizer automatically knows if the result is too big, but you can force the optimizer to use a temporary table with `SQL_SMALL_RESULT`, or avoid the temporary table using `SQL_BIG_RESULT`.


### STRAIGHT_JOIN


`STRAIGHT_JOIN` applies to the [JOIN](joins-subqueries/joins/join-syntax.md) queries, and tells the optimizer that the tables must be read in the order they appear in the `SELECT`. For `const` and `system` table this options is sometimes ignored.


### SQL_CALC_FOUND_ROWS


`SQL_CALC_FOUND_ROWS` is only applied when using the `LIMIT` clause. If this option is used, MariaDB will count how many rows would match the query, without the `LIMIT` clause. That number can be retrieved in the next query, using [FOUND_ROWS()](../../built-in-functions/secondary-functions/information-functions/found_rows.md).


### USE/FORCE/IGNORE INDEX


`USE INDEX`, `FORCE INDEX` and `IGNORE INDEX` constrain the query planning to a specific index.


For further information about some of these options, see [How to force query plans](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/query-optimizations/index-hints-how-to-force-query-plans.md).



##### MariaDB starting with [12.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/what-is-mariadb-120)

## Expanded Optimizer Hints

[MariaDB 12.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/what-is-mariadb-120) features an extensive expansion of optimizer hints.

### Syntax

1. Hint syntax
Hints are placed after the main statement verb

```
UPDATE /*+ hints */ table ...;
DELETE /*+ hints */ FROM table... ;
SELECT /*+ hints */  ...
```
or after the SELECT keyword in any subquery:

```
SELECT * FROM t1 WHERE a IN (SELECT /*+ hints */ ...)
```
There can be one or more hints separated with space

```
hints:  hint hint ...
```

### Description

Each individual hint is hint name and arguments. In case there are no arguments,
the () brackets are still present:

```
hint:  hint_name([arguments])
```
Incorrect hints produce warnings (a setting to make them errors is not implemented yet).
Hints that are not ignored are kept in the query text (you can see them in SHOW PROCESSLIST, Slow Query Log, EXPLAIN EXTENDED)
Hints that were incorrect and were ignored are removed from there.

#### Hint Hierarchy

Hints can be

* global - applies to whole query
* table-level - applies to a table
* index-level - applies to an index in a table


##### Table-Level Hints


```
hint_name([table_name [table_name [,...]] )
```

##### Index-Level Hints

Index-level hints apply to index(es).
Possible syntax variants:

```
hint_name(table_name [index_name [, index_name] ...])

hint_name(table_name@query_block [index_name [, index_name] ...])

hint_name(@query_block  table_name [index_name [, index_name] ...])
```

#### Query Block Naming

The `QB_NAME` hint is used to assign a name to the query block the hint is in. The Query Block is either a SELECT or a top-level construct of UPDATE or DELETE statement.

```
SELECT /*+ QB_NAME(foo) */ select_list FROM ...
```
The name can then can be used

* to refer to the query block
* to refer to a table in the query block as table_name@query_block_name.

Query block scope is the whole statement. It is invalid to use the same name for multiple query blocks.
One can refer to the query block "down into subquery", "down into derived table", "up to the parent" and "to a right sibling in the UNION". One cannot refer "to a left sibling in a UNION".
Hints inside VIEWs are not supported, yet. One can neither use hints in VIEW definitions, nor control query plans inside non-merged VIEWs (This is because QB_NAME binding is done "early", before we know that some tables are VIEWs)

##### SELECT#N NAMES

Besides the given name, any query block is given a name select#n. It is printed in EXPLAIN EXTENDED output:
Warnings:
Note	1003	select /*+ NO_RANGE_OPTIMIZATION(`t3`@`select#1` `PRIMARY`) */ ...
At the moment it is NOT yet possible to use it in the hint text:

```
SELECT /*+ BKA(tbl1@`select#1`) */ 1 FROM tbl1 ...;
```

##### QB_NAME in CTEs

Hints that control @name will control the first use of the CTE.

### Effect of Optimizer Hints

The optimizer can be controlled by

1. Server variables - optimizer_switch, join_cache_level, etc, etc
1. Old-style hints
1. New-style hints

Old-style hints did not overlap with server variable settings.
New-style hints are more specific than server variable settings, so they override the server variable settings.
Hints are "narrowly interpreted" and "best effort" - if a hint dictates to do something, like

```
SELECT  /*+ MRR(t1 t1_index1) */  ... FROM t1 ...
```
that means:
    When considering a query plan that involves using t1_index1 in a way that one can use MRR, use MRR.
if the query planning is such that use of t1_index1 doesn't allow to use MRR, it won't be used.
The optimizer may also consider using t1_index2 and pick that over using t1_index1.
In such cases the hint is effectively ignored and no warning is given.

### List of Hints


#### NO_RANGE_OPTIMIZATION

An index-level hint that disables range optimization for certain index(es):

```
SELECT /*+ NO_RANGE_OPTIMIZATION(tbl index1 index2) */  * FROM tbl ...
```

#### NO_ICP

Sn index-level hint that disables Index Condition Pushdown for the indexes. ICP+BKA is disabled as well.

```
SELECT /*+ NO_ICP(tbl index1 index2) */  * FROM tbl ...
```

#### MRR and NO_MRR

Index-level hints to force or disable use of MRR.

```
SELECT /*+ MRR(tbl index1 index2) */  * FROM tbl ... 

SELECT /*+ NO_MRR(tbl index1 index2) */  * FROM tbl ...
```
This controls:

* MRR optimization for range access ( mdev35483-mrr-is-narrow.sql )
* BKA mdev35483-mrr-controls-bka-partially.sql


#### BKA() and NO_BKA()

Query block or table-level hints.
BKA() also enables MRR to make BKA possible. (This is different from session variables, where one needs to enable MRR separately).
This also enables BKAH.

#### BNL() and NO_BNL()

Controls BNL-H.
The implementation is "BNL() hint effectively increases join_cache_level up to 4 " .. for the table(s) it applies to.

#### MAX_EXECUTION_TIME()

Global-level hint to limit query execution time

```
SELECT /*+ MAX_EXECUTION_TIME(milliseconds) */ ...  ;
```
A query that doesn't finish in the time specified will be aborted with an error.
If @@max_statement_time is set, the hint will be ignored and a warning produced. Note that this contradicts the stated principle that "New-style hints are more specific than server variable settings, so they override the server variable settings".

### Subquery Hints


#### SUBQUERY Hint

Query block-level hint.

```
SUBQUERY([@query_block_name] MATERIALIZATION)

SUBQUERY([@query_block_name] INTOEXISTS)
```
This controls non-semi-join subqueries. The parameter specifies which subquery to use. Use of this hint disables conversion of subquery into semi-join.

#### SEMIJOIN and NO_SEMIJOIN

Query block-level hints.
This controls the conversion of subqueries to semi-joins and which semi-join strategies are allowed.

```
[NO_]SEMIJOIN([@query_block_name] [strategy [, strategy] ...])
```
where the strategy is one of DUPSWEEDOUT, FIRSTMATCH, LOOSESCAN, MATERIALIZATION.


## See Also


* [Use optimizer_switch to enable/disable specific optimizations](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/query-optimizations/optimizer-switch.md)

