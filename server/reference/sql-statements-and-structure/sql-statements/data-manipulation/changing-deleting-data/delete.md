
# DELETE


## Syntax


Single-table syntax:


```
DELETE [LOW_PRIORITY] [QUICK] [IGNORE] 
  FROM tbl_name [PARTITION (partition_list)]
  [FOR PORTION OF period FROM expr1 TO expr2]
  [AS alias]                    -- from MariaDB 11.6
  [WHERE where_condition]
  [ORDER BY ...]
  [LIMIT row_count]
  [RETURNING select_expr 
    [, select_expr ...]]
```

Multiple-table syntax:


```
DELETE [LOW_PRIORITY] [QUICK] [IGNORE]
    tbl_name[.*] [, tbl_name[.*]] ...
    FROM table_references
    [WHERE where_condition]
```

Or:


```
DELETE [LOW_PRIORITY] [QUICK] [IGNORE]
    FROM tbl_name[.*] [, tbl_name[.*]] ...
    USING table_references
    [WHERE where_condition]
```

Trimming history:


```
DELETE HISTORY
  FROM tbl_name [PARTITION (partition_list)]
  [BEFORE SYSTEM_TIME [TIMESTAMP|TRANSACTION] expression]
```

## Description



| Option | Description |
| --- | --- |
| Option | Description |
| LOW_PRIORITY | Wait until all SELECT's are done before starting the statement. Used with storage engines that uses table locking (MyISAM, Aria etc). See [HIGH_PRIORITY and LOW_PRIORITY clauses](high_priority-and-low_priority.md) for details. |
| QUICK | Signal the storage engine that it should expect that a lot of rows are deleted. The storage engine engine can do things to speed up the DELETE like ignoring merging of data blocks until all rows are deleted from the block (instead of when a block is half full). This speeds up things at the expanse of lost space in data blocks. At least [MyISAM](../../../../storage-engines/myisam-storage-engine/myisam-system-variables.md) and [Aria](../../../../storage-engines/s3-storage-engine/aria_s3_copy.md) support this feature. |
| IGNORE | Don't stop the query even if a not-critical error occurs (like data overflow). See [How IGNORE works](../inserting-loading-data/ignore.md) for a full description. |



For the single-table syntax, the `<code class="fixed" style="white-space:pre-wrap">DELETE</code>` statement deletes rows
from tbl_name and returns a count of the number of deleted rows. This count can
be obtained by calling the [ROW_COUNT()](../../built-in-functions/secondary-functions/information-functions/row_count.md) function. The
`<code class="fixed" style="white-space:pre-wrap">WHERE</code>` clause, if given, specifies the conditions that identify
which rows to delete. With no `<code class="fixed" style="white-space:pre-wrap">WHERE</code>` clause, all rows are
deleted. If the [ORDER BY](../selecting-data/order-by.md) clause is specified, the rows are
deleted in the order that is specified. The [LIMIT](../../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/debugging-mariadb/limitationsdifferences-with-a-mariadb-server-compiled-for-debugging.md) clause
places a limit on the number of rows that can be deleted.


For the multiple-table syntax, `<code class="fixed" style="white-space:pre-wrap">DELETE</code>` deletes from each
`<code class="fixed" style="white-space:pre-wrap">tbl_name</code>` the rows that satisfy the conditions. In this case,
[ORDER BY](../selecting-data/order-by.md) and [LIMIT](../../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/debugging-mariadb/limitationsdifferences-with-a-mariadb-server-compiled-for-debugging.md)> cannot be used. A `<code>DELETE</code>` can also reference tables which are located in different databases; see [Identifier Qualifiers](../../../sql-language-structure/identifier-qualifiers.md) for the syntax.


`<code class="fixed" style="white-space:pre-wrap">where_condition</code>` is an expression that evaluates to true for
each row to be deleted. It is specified as described in [SELECT](../../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/benchmarks-and-long-running-tests/benchmark-results/select-random-ranges-and-select-random-point.md).


Currently, you cannot delete from a table and select from the same
table in a subquery.


You need the `<code class="fixed" style="white-space:pre-wrap">DELETE</code>` privilege on a table to delete rows from
it. You need only the `<code class="fixed" style="white-space:pre-wrap">SELECT</code>` privilege for any columns that
are only read, such as those named in the `<code class="fixed" style="white-space:pre-wrap">WHERE</code>` clause. See
[GRANT](../../account-management-sql-commands/grant.md).


As stated, a `<code class="highlight fixed" style="white-space:pre-wrap">DELETE</code>` statement with no `<code class="highlight fixed" style="white-space:pre-wrap">WHERE</code>`
clause deletes all rows. A faster way to do this, when you do not need to know
the number of deleted rows, is to use `<code class="highlight fixed" style="white-space:pre-wrap">TRUNCATE TABLE</code>`. However,
within a transaction or if you have a lock on the table, 
`<code class="fixed" style="white-space:pre-wrap">TRUNCATE TABLE</code>` cannot be used whereas `<code class="fixed" style="white-space:pre-wrap">DELETE</code>`
can. See [TRUNCATE TABLE](../../table-statements/truncate-table.md), and
[LOCK](../../transactions/lock-tables.md).


### AS



##### MariaDB starting with [11.6](../../../../../../release-notes/mariadb-community-server/what-is-mariadb-116.md)
From [MariaDB 11.6](../../../../../../release-notes/mariadb-community-server/what-is-mariadb-116.md), single table DELETEs support aliases. For example:

```
CREATE TABLE t1 (c1 INT);
INSERT INTO t1 VALUES (1), (2);

DELETE FROM t1 AS a1 WHERE a1.c1 = 2;
```


### PARTITION


See [Partition Pruning and Selection](../../../../../server-management/partitioning-tables/partition-pruning-and-selection.md) for details.


### FOR PORTION OF


See [Application Time Periods - Deletion by Portion](../../../temporal-tables/application-time-periods.md#deletion-by-portion).


### RETURNING


It is possible to return a resultset of the deleted rows for a single table to the client by using the syntax `<code>DELETE ... RETURNING select_expr [, select_expr2 ...]]</code>`


Any of SQL expression that can be calculated from a single row fields is allowed. Subqueries are allowed. The AS keyword is allowed, so it is possible to use aliases.


The use of aggregate functions is not allowed. RETURNING cannot be used in multi-table DELETEs.


### Same Source and Target Table


It is possible to delete from a table with the same source and target. For example:


```
DELETE FROM t1 WHERE c1 IN (SELECT b.c1 FROM t1 b WHERE b.c2=0);
```

### DELETE HISTORY


One can use `<code>DELETE HISTORY</code>` to delete historical information from [System-versioned tables](../../../temporal-tables/system-versioned-tables.md).


## Examples


How to use the [ORDER BY](../selecting-data/order-by.md) and [LIMIT](../../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/debugging-mariadb/limitationsdifferences-with-a-mariadb-server-compiled-for-debugging.md) clauses:


```
DELETE FROM page_hit ORDER BY timestamp LIMIT 1000000;
```

How to use the RETURNING clause:


```
DELETE FROM t RETURNING f1;
+------+
| f1   |
+------+
|    5 |
|   50 |
|  500 |
+------+
```

The following statement joins two tables: one is only used to satisfy a WHERE condition, but no row is deleted from it; rows from the other table are deleted, instead.


```
DELETE post FROM blog INNER JOIN post WHERE blog.id = post.blog_id;
```

### Deleting from the Same Source and Target


```
CREATE TABLE t1 (c1 INT, c2 INT);
DELETE FROM t1 WHERE c1 IN (SELECT b.c1 FROM t1 b WHERE b.c2=0);
```

Until [MariaDB 10.3.1](../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1031-release-notes.md), this returned:


```
ERROR 1093 (HY000): Table 't1' is specified twice, both as a target for 'DELETE' 
  and as a separate source for
```

From [MariaDB 10.3.1](../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1031-release-notes.md):


```
Query OK, 0 rows affected (0.00 sec)
```

## See Also


* [How IGNORE works](../inserting-loading-data/ignore.md)
* [SELECT](../../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/benchmarks-and-long-running-tests/benchmark-results/select-random-ranges-and-select-random-point.md)
* [ORDER BY](../selecting-data/order-by.md)
* [LIMIT](../../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/debugging-mariadb/limitationsdifferences-with-a-mariadb-server-compiled-for-debugging.md)
* [REPLACE ... RETURNING](replacereturning.md)
* [INSERT ... RETURNING](../inserting-loading-data/insertreturning.md)
* [Returning clause](https://www.youtube.com/watch?v=n-LTdEBeAT4) (video)

