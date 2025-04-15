
# ANALYZE FORMAT=JSON

`<code>ANALYZE FORMAT=JSON</code>` is a mix of the [EXPLAIN FORMAT=JSON](../../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/outdated-pages/explain-formatjson-in-mysql.md) and [ANALYZE](analyze-statement.md) statement features. The `<code>ANALYZE FORMAT=JSON $statement</code>` will execute `<code>$statement</code>`, and then print the output of `<code>EXPLAIN FORMAT=JSON</code>`, amended with data from the query execution.


## Basic Execution Data


You can get the following also from tabular `<code>ANALYZE</code>` statement form:


* `<code>r_rows</code>` is provided for any node that reads rows. It shows how many rows were read, on average
* `<code>r_filtered</code>` is provided whenever there is a condition that is checked. It shows the percentage of rows left after checking the condition.


## Advanced Execution Data


The most important data not available in the regular tabular `<code>ANALYZE</code>` statement are:


* `<code>r_loops</code>` field. This shows how many times the node was executed. Most query plan elements have this field.
* `<code>r_total_time_ms</code>` field. It shows how much time in total, in milliseconds, was spent executing this node. If the node has subnodes, their execution time is included.

  * For UPDATE and DELETE statements, top-level `<code>query_block.r_total_time_ms</code>` does include the time to make row deletions/updates but does NOT include the time to commit the changes.
* `<code>r_buffer_size</code>` field. Query plan nodes that make use of buffers report the size of buffer that was was used.


### InnoDB engine statistics


Starting from [MariaDB 10.6.15](../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-10-6-15-release-notes.md), [MariaDB 10.8.8](../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-8-series/mariadb-10-8-8-release-notes.md), [MariaDB 10.9.8](../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-9-series/mariadb-10-9-8-release-notes.md), [MariaDB 10.10.6](../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-10-series/mariadb-10-10-6-release-notes.md), [MariaDB 10.11.5](../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-11-series/mariadb-10-11-5-release-notes.md), [MariaDB 11.0.3](../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-0-series/mariadb-11-0-3-release-notes.md), [MariaDB 11.1.2](../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-1-series/mariadb-11-1-2-release-notes.md) and [MariaDB 11.2.1](../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-2-series/mariadb-11-2-1-release-notes.md) ([MDEV-31577](https://jira.mariadb.org/browse/MDEV-31577)), the following statistics are reported for InnoDB tables:


```
"r_engine_stats": {
        "pages_accessed":  integer,
        "pages_updated": integer,
        "pages_read_count": integer,
        "pages_prefetch_read_count": integer,
        "pages_read_time_ms": double,
        "old_rows_read": integer
      }
```

Only non-zero members are printed.


* `<code>pages_accessed</code>` is the total number of buffer pool pages accessed when reading this table.
* `<code>pages_updated</code>` is the total number of buffer pool pages that were modified during the execution of the statement.
* `<code>pages_read_count</code>` is the number of pages that InnoDB had to read from disk for this table. If the query touches "hot" data in the InnoDB buffer pool, this value will be 0 and not present.
* `<code>pages_prefetch_read_count</code>` Number of pages for which read-ahead was initiated. Not all such pages will necessarily be accessed.
* `<code>pages_read_time_ms</code>` is the total time spent reading the table.
* `<code>old_rows_read</code>` is the number of old row versions that InnoDB had to read. Old row version is the version of the row that is not visible to this transaction.


## SHOW ANALYZE FORMAT=JSON



##### MariaDB starting with [10.9](../../../../../../release-notes/mariadb-community-server/what-is-mariadb-109.md)
`<code>SHOW ANALYZE FORMAT=JSON for &lt;connection_id&gt;</code>`
extends `<code>ANALYZE [FORMAT=JSON] &lt;select&gt;</code>` to allow one to analyze a query currently running in another connection.


## Data About Individual Query Plan Nodes


* `<code>filesort</code>` node reports whether sorting was done with `<code>LIMIT n</code>` parameter, and how many rows were in the sort result.
* `<code>block-nl-join</code>` node has `<code>r_loops</code>` field, which allows to tell whether `<code>Using join buffer</code>` was efficient
* `<code>range-checked-for-each-record</code>` reports counters that show the result of the check.
* `<code>expression-cache</code>` is used for subqueries, and it reports how many times the cache was used, and what cache hit ratio was.
* `<code>union_result</code>` node has `<code>r_rows</code>` so one can see how many rows were produced after UNION operation
* and so forth


## Use Cases


See [Examples of ANALYZE FORMAT=JSON](analyze-formatjson-examples.md).

