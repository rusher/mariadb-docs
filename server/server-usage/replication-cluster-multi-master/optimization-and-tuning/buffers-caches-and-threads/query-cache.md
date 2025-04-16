
# Query Cache

The query cache stores results of SELECT queries so that if the identical query is received in future, the results can be quickly returned.


This is extremely useful in high-read, low-write environments (such as most websites). It does not scale well in environments with high throughput on multi-core machines, so it is disabled by default.


Note that the query cache cannot be enabled in certain environments. See [Limitations](#limitations).


## Setting Up the Query Cache


Unless MariaDB has been specifically built without the query cache, the query cache will always be available, although inactive. The [have_query_cache](../system-variables/server-system-variables.md#have_query_cache) server variable will show whether the query cache is available.


```
SHOW VARIABLES LIKE 'have_query_cache';
+------------------+-------+
| Variable_name    | Value |
+------------------+-------+
| have_query_cache | YES   |
+------------------+-------+
```

If this is set to `NO`, you cannot enable the query cache unless you rebuild or reinstall a version of MariaDB with the cache available.


To see if the cache is enabled, view the [query_cache_type](../system-variables/server-system-variables.md#query_cache_type) server variable. It is enabled by default in MariaDB versions up to 10.1.6, but disabled starting with [MariaDB 10.1.7](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-7-release-notes.md) - if needed enable it by setting `query_cache_type` to `1`.


Although enabled in versions prior to [MariaDB 10.1.7](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-7-release-notes.md), the [query_cache_size](../system-variables/server-system-variables.md#query_cache_size) is by default 0KB there, which effectively disables the query cache. From 10.1.7 on the cache size defaults to 1MB. If needed set the cache to a size large enough amount, for example:


```
SET GLOBAL query_cache_size = 1000000;
```

Starting from [MariaDB 10.1.7](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-7-release-notes.md), `query_cache_type` is automatically set to ON if the server is started with the `query_cache_size` set to a non-zero (and non-default) value.


See [Limiting the size of the Query Cache](#limiting-the-size-of-the-query-cache) below for details.


## How the Query Cache Works


When the query cache is enabled and a new SELECT query is processed, the query cache is examined to see if the query appears in the cache.


Queries are considered identical if they use the same database, same protocol version and same default character set. Prepared statements are always considered as different to non-prepared statements, see [Query cache internal structure](#query-cache-internal-structure) for more info.


If the identical query is not found in the cache, the query will be processed normally and then stored, along with its result set, in the query cache. If the query is found in the cache, the results will be pulled from the cache, which is much quicker than processing it normally.


Queries are examined in a case-sensitive manner, so :


```
SELECT * FROM t
```

Is different from :


```
select * from t
```

Comments are also considered and can make the queries differ, so :


```
/* retry */SELECT * FROM t
```

Is different from :


```
/* retry2 */SELECT * FROM t
```

See the [query_cache_strip_comments](../system-variables/server-system-variables.md#query_cache_strip_comments) server variable for an option to strip comments before searching.


Each time changes are made to the data in a table, all affected results in the query cache are cleared. It is not possible to retrieve stale data from the query cache.


When the space allocated to query cache is exhausted, the oldest results will be dropped from the cache.


When using `query_cache_type=ON`, and the query specifies `SQL_NO_CACHE` (case-insensitive), the server will not cache the query and will not fetch results from the query cache.


When using `query_cache_type=DEMAND` (after [MDEV-6631](https://jira.mariadb.org/browse/MDEV-6631) feature request) and the query specifies `SQL_CACHE`, the server will cache the query.


One important point of [MDEV-6631](https://jira.mariadb.org/browse/MDEV-6631) is : switching between `query_cache_type=ON` and `query_cache_type=DEMAND` can "turn off" query cache of old queries without the `SQL_CACHE` string, that's not yet defined if we should include another `query_cache_type` (DEMAND_NO_PRUNE) value or not to allow use of old queries


## Queries Stored in the Query Cache


If the [query_cache_type](../system-variables/server-system-variables.md#query_cache_type) system variable is set to `1`, or `ON`, all queries fitting the size constraints will be stored in the cache unless they contain a `SQL_NO_CACHE` clause, or are of a nature that caching makes no sense, for example making use of a function that returns the current time. Queries with `SQL_NO_CACHE` will not attempt to acquire query cache lock.


If any of the following functions are present in a query, it will not be cached. Queries with these functions are sometimes called 'non-deterministic' - don't get confused with the use of this term in other contexts.



|   |   |
| --- | --- |
| [BENCHMARK()](../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/benchmarks-and-long-running-tests/benchmarks/benchmark-builds.md) | [CONNECTION_ID()](../../../../reference/sql-statements-and-structure/sql-statements/built-in-functions/secondary-functions/information-functions/connection_id.md) |
| [CONVERT_TZ()](../../../../reference/sql-statements-and-structure/sql-statements/built-in-functions/date-time-functions/convert_tz.md) | [CURDATE()](../../../../reference/sql-statements-and-structure/sql-statements/built-in-functions/date-time-functions/curdate.md) |
| [CURRENT_DATE()](../../../../reference/sql-statements-and-structure/sql-statements/built-in-functions/date-time-functions/current_date.md) | [CURRENT_TIME()](../../../../reference/sql-statements-and-structure/sql-statements/built-in-functions/date-time-functions/current_time.md) |
| [CURRENT_TIMESTAMP()](../../../../reference/sql-statements-and-structure/sql-statements/built-in-functions/date-time-functions/current_timestamp.md) | [CURTIME()](../../../../reference/sql-statements-and-structure/sql-statements/built-in-functions/date-time-functions/curtime.md) |
| [DATABASE()](../../../../../general-resources/learning-and-training/training-and-tutorials/intermediate-mariadb-articles/database-theory/database-normalization/database-normalization-2nd-normal-form.md) | [ENCRYPT()](../../../../reference/mariadb-internals/encryption-plugin-api.md) (one parameter) |
| [FOUND_ROWS()](../../../../reference/sql-statements-and-structure/sql-statements/built-in-functions/secondary-functions/information-functions/found_rows.md) | [GET_LOCK()](../../../../reference/sql-statements-and-structure/sql-statements/built-in-functions/secondary-functions/miscellaneous-functions/get_lock.md) |
| [LAST_INSERT_ID()](../../../../reference/sql-statements-and-structure/sql-statements/built-in-functions/secondary-functions/information-functions/last_insert_id.md) | [LOAD_FILE()](../../../../reference/sql-statements-and-structure/sql-statements/built-in-functions/string-functions/load_file.md) |
| [MASTER_POS_WAIT()](../../../../reference/sql-statements-and-structure/sql-statements/built-in-functions/secondary-functions/miscellaneous-functions/master_pos_wait.md) | [NOW()](../../../../reference/sql-statements-and-structure/sql-statements/built-in-functions/date-time-functions/now.md) |
| [RAND()](../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/random-query-generator-tests.md) | [RELEASE_LOCK()](../../../../reference/sql-statements-and-structure/sql-statements/built-in-functions/secondary-functions/miscellaneous-functions/release_lock.md) |
| [SLEEP()](../../../../reference/sql-statements-and-structure/sql-statements/built-in-functions/secondary-functions/miscellaneous-functions/sleep.md) | [SYSDATE()](../../../../reference/sql-statements-and-structure/sql-statements/built-in-functions/date-time-functions/sysdate.md) |
| [UNIX_TIMESTAMP()](../../../../reference/sql-statements-and-structure/sql-statements/built-in-functions/date-time-functions/unix_timestamp.md) (no parameters) | [USER()](../../../../reference/plugins/other-plugins/user-variables-plugin.md) |
| [UUID()](../../../../reference/sql-statements-and-structure/sql-statements/built-in-functions/secondary-functions/miscellaneous-functions/uuid.md) | [UUID_SHORT()](../../../../reference/sql-statements-and-structure/sql-statements/built-in-functions/secondary-functions/miscellaneous-functions/uuid_short.md) |



A query will also not be added to the cache if:


* It is of the form:

  * SELECT SQL_NO_CACHE ...
  * SELECT ... INTO OUTFILE ...
  * SELECT ... INTO DUMPFILE ...
  * SELECT ... FOR UPDATE
  * SELECT * FROM ... WHERE autoincrement_column IS NULL
  * SELECT ... LOCK IN SHARE MODE
* It uses TEMPORARY table
* It uses no tables at all
* It generates a warning
* The user has a column-level privilege on any table in the query
* It accesses a table from INFORMATION_SCHEMA, mysql or the performance_schema database
* It makes use of user or local variables
* It makes use of stored functions
* It makes use of user-defined functions
* It is inside a transaction with the SERIALIZABLE isolation level
* It is quering a table inside a transaction after the same table executed a query cache invalidation using INSERT, UPDATE or DELETE


The query itself can also specify that it is not to be stored in the cache by using the `SQL_NO_CACHE` attribute. Query-level control is an effective way to use the cache more optimally.


It is also possible to specify that *no* queries must be stored in the cache unless the query requires it. To do this, the [query_cache_type](../system-variables/server-system-variables.md#query_cache_type) server variable must be set to `2`, or `DEMAND`. Then, only queries with the `SQL_CACHE` attribute are cached.


## Limiting the Size of the Query Cache


There are two main ways to limit the size of the query cache. First, the overall size in bytes is determined by the [query_cache_size](../system-variables/server-system-variables.md#query_cache_size) server variable. About 40KB is needed for various query cache structures.


The query cache size is allocated in 1024 byte-blocks, thus it should be set to a multiple of 1024.


The query result is stored using a minimum block size of [query_cache_min_res_unit](../system-variables/server-system-variables.md#query_cache_min_res_unit). Check two conditions to use a good value of this variable: Query cache insert result blocks with locks, each new block insert lock query cache, a small value will increase locks and fragmentation and waste less memory for small results, a big value will increase memory use wasting more memory for small results but it reduce locks. Test with your workload for fine tune this variable.


If the [strict mode](../../../../server-management/variables-and-modes/sql-mode.md) is enabled, setting the query cache size to an invalid value will cause an error. Otherwise, it will be set to the nearest permitted value, and a warning will be triggered.


```
SHOW VARIABLES LIKE 'query_cache_size';
+------------------+----------+
| Variable_name    | Value    |
+------------------+----------+
| query_cache_size | 67108864 |
+------------------+----------+

SET GLOBAL query_cache_size = 8000000;
Query OK, 0 rows affected, 1 warning (0.03 sec)

SHOW VARIABLES LIKE 'query_cache_size';
+------------------+---------+
| Variable_name    | Value   |
+------------------+---------+
| query_cache_size | 7999488 |
+------------------+---------+
```

The ideal size of the query cache is very dependent on the specific needs of each system. Setting a value too small will result in query results being dropped from the cache when they could potentially be re-used later. Setting a value too high could result in reduced performance due to lock contention, as the query cache is locked during updates.


The second way to limit the cache is to have a maximum size for each set of query results. This prevents a single query with a huge result set taking up most of the available memory and knocking a large number of smaller queries out of the cache. This is determined by the [query_cache_limit](../system-variables/server-system-variables.md#query_cache_limit) server variable.


If you attempt to set a query cache that is too small (the amount depends on the architecture), the resizing will fail and the query cache will be set to zero, for example :


```
SET GLOBAL query_cache_size=40000;
Query OK, 0 rows affected, 2 warnings (0.03 sec)

SHOW WARNINGS;
+---------+------+-----------------------------------------------------------------+
| Level   | Code | Message                                                         |
+---------+------+-----------------------------------------------------------------+
| Warning | 1292 | Truncated incorrect query_cache_size value: '40000'             |
| Warning | 1282 | Query cache failed to set size 39936; new query cache size is 0 |
+---------+------+-----------------------------------------------------------------+
```

## Examining the Query Cache


A number of status variables provide information about the query cache.


```
SHOW STATUS LIKE 'Qcache%';
+-------------------------+----------+
| Variable_name           | Value    |
+-------------------------+----------+
| Qcache_free_blocks      | 1158     |
| Qcache_free_memory      | 3760784  |
| Qcache_hits             | 31943398 |
| Qcache_inserts          | 42998029 |
| Qcache_lowmem_prunes    | 34695322 |
| Qcache_not_cached       | 652482   |
| Qcache_queries_in_cache | 4628     |
| Qcache_total_blocks     | 11123    |
+-------------------------+----------+
```

`Qcache_inserts` contains the number of queries added to the query cache, `Qcache_hits` contains the number of queries that have made use of the query cache, while `Qcache_lowmem_prunes` contains the number of queries that were dropped from the cache due to lack of memory.


The above example could indicate a poorly performing cache. More queries have been added, and more queries have been dropped, than have actually been used.


Note that before [MariaDB 5.5](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5.md), queries returned from the query cache did not increment the [Com_select](../system-variables/server-status-variables.md#com_select) status variable, so to find the total number of valid queries run on the server, add [Com_select](../system-variables/server-status-variables.md#com_select) to [Qcache_hits](../system-variables/server-status-variables.md#qcache_hits). Starting from [MariaDB 5.5](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5.md), results returned by the query cache count towards `Com_select` (see [MDEV-4981](https://jira.mariadb.org/browse/MDEV-4981)).


The [QUERY_CACHE_INFO plugin](../../../../reference/plugins/other-plugins/query-cache-information-plugin.md) creates the [QUERY_CACHE_INFO](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-query_cache_info-table.md) table in the [INFORMATION_SCHEMA](../../../../reference/mariadb-internals/information-schema-plugins-show-and-flush-statements.md), allowing you to examine the contents of the query cache.


## Query Cache Fragmentation


The Query Cache uses blocks of variable length, and over time may become fragmented. A high `Qcache_free_blocks` relative to `Qcache_total_blocks` may indicate fragmentation. [FLUSH QUERY CACHE](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/flush-commands/flush-query-cache.md) will defragment the query cache without dropping any queries :


```
FLUSH QUERY CACHE;
```

After this, there will only be one free block :


```
SHOW STATUS LIKE 'Qcache%';
+-------------------------+----------+
| Variable_name           | Value    |
+-------------------------+----------+
| Qcache_free_blocks      | 1        |
| Qcache_free_memory      | 6101576  |
| Qcache_hits             | 31981126 |
| Qcache_inserts          | 43002404 |
| Qcache_lowmem_prunes    | 34696486 |
| Qcache_not_cached       | 655607   |
| Qcache_queries_in_cache | 4197     |
| Qcache_total_blocks     | 8833     |
+-------------------------+----------+
```

## Emptying and disabling the Query Cache


To empty or clear all results from the query cache, use [RESET QUERY CACHE](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/reset-master.md). [FLUSH TABLES](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/flush-commands/flush-tables-for-export.md) will have the same effect.


Setting either [query_cache_type](../system-variables/server-system-variables.md#query_cache_type) or [query_cache_size](../system-variables/server-system-variables.md#query_cache_size) to `0` will disable the query cache, but to free up the most resources, set both to `0` when you wish to disable caching.


## Limitations


* The query cache needs to be disabled in order to use [OQGRAPH](../../../../reference/storage-engines/oqgraph-storage-engine/oqgraph-examples.md).
* The query cache is not used by the [Spider](../../../../reference/storage-engines/spider/spider-functions/spider_copy_tables.md) storage engine (amongst others).
* The query cache also needs to be disabled for MariaDB [Galera](../../../../reference/sql-statements-and-structure/sql-statements/built-in-functions/special-functions/galera-functions/README.md) cluster versions prior to "5.5.40-galera", "10.0.14-galera" and "10.1.2".


## LOCK TABLES and the Query Cache


The query cache can be used when tables have a write lock (which may seem confusing since write locks should avoid table reads). This behaviour can be changed by setting the [query_cache_wlock_invalidate](../system-variables/server-system-variables.md#query_cache_wlock_invalidate) system variable to `ON`, in which case each write lock will invalidate the table query cache. Setting to `OFF`, the default, means that cached queries can be returned even when a table lock is being held. For example:


```
1> SELECT * FROM T1
+---+
| a |
+---+
| 1 |
+---+
-- Here the query is cached

-- From another connection execute:
2> LOCK TABLES T1 WRITE;

-- Expected result with: query_cache_wlock_invalidate = OFF
1> SELECT * FROM T1
+---+
| a |
+---+
| 1 |
+---+
-- read from query cache


-- Expected result with: query_cache_wlock_invalidate = ON
1> SELECT * FROM T1
-- Waiting Table Write Lock
```

## Transactions and the Query Cache


The query cache handles transactions. Internally a flag (FLAGS_IN_TRANS) is set to 0 when a query was executed outside a transaction, and to 1 when the query was inside a transaction ([beginner-books.md](../../../../../general-resources/learning-and-training/training-and-tutorials/books/beginner-books.md) / [COMMIT](../../../../reference/sql-statements-and-structure/sql-statements/transactions/commit.md) / [ROLLBACK](../../../../reference/sql-statements-and-structure/sql-statements/transactions/rollback.md)). This flag is part of the "query cache hash", in others words one query inside a transaction is different from a query outside a transaction.


Queries that change rows ([INSERT](../../../../reference/sql-statements-and-structure/sql-statements/built-in-functions/string-functions/insert-function.md) / [UPDATE](../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/tools/buildbot/buildbot-setup/buildbot-setup-for-virtual-machines/buildbot-setup-for-virtual-machines-additional-steps/update-debian-4-mirrors-for-buildbot-vms.md) / [DELETE](../../../../reference/sql-statements-and-structure/sql-statements/data-manipulation/changing-deleting-data/delete.md) / [TRUNCATE](../../../../reference/sql-statements-and-structure/sql-statements/table-statements/truncate-table.md)) inside a transaction will invalidate all queries from the table, and turn off the query cache to the changed table. Transactions that don't end with COMMIT / ROLLBACK check that even without COMMIT / ROLLBACK, the query cache is turned off to allow row level locking and consistency level.


Examples:


```
SELECT * FROM T1 <first insert to query cache, using FLAGS_IN_TRANS=0>
+---+
| a |
+---+
| 1 |
+---+
```

```
BEGIN;
SELECT * FROM T1 <first insert to query cache, using FLAGS_IN_TRANS=1>
+---+
| a |
+---+
| 1 |
+---+
```

```
SELECT * FROM T1 <result from query cache, using FLAGS_IN_TRANS=1>
+---+
| a |
+---+
| 1 |
+---+
```

```
INSERT INTO T1 VALUES(2);  <invalidate queries from table T1 and disable query cache to table T1>
```

```
SELECT * FROM T1 <don't use query cache, a normal query from innodb table>
+---+
| a |
+---+
| 1 |
| 2 |
+---+
```

```
SELECT * FROM T1 <don't use query cache, a normal query from innodb table>
+---+
| a |
+---+
| 1 |
| 2 |
+---+
```

```
COMMIT;  <query cache is now turned on to T1 table>
```

```
SELECT * FROM T1 <first insert to query cache, using FLAGS_IN_TRANS=0>
+---+
| a |
+---+
| 1 |
+---+
```

```
SELECT * FROM T1 <result from query cache, using FLAGS_IN_TRANS=0>
+---+
| a |
+---+
| 1 |
+---+
```

## Query Cache Internal Structure


Internally, each flag that can change a result using the same query is a different query. For example, using the latin1 charset and using the utf8 charset with the same query are treated as different queries by the query cache.


Some fields that differentiate queries are (from "Query_cache_query_flags" internal structure) :


* query (string)
* current database schema name (string)
* client long flag (0/1)
* client protocol 4.1 (0/1)
* protocol type (internal value)
* more results exists (protocol flag)
* in trans (inside transaction or not)
* autocommit ([autocommit](../system-variables/server-system-variables.md#autocommit) session variable)
* pkt_nr (protocol flag)
* character set client ([character_set_client](../system-variables/server-system-variables.md#character_set_client) session variable)
* character set results ([character_set_results](../system-variables/server-system-variables.md#character_set_results) session variable)
* collation connection ([collation_connection](../system-variables/server-system-variables.md#collation_connection) session variable)
* limit ([sql_select_limit](../system-variables/server-system-variables.md#sql_select_limit) session variable)
* time zone ([time_zone](../system-variables/server-system-variables.md#time_zone) session variable)
* sql_mode ([sql_mode](../system-variables/server-system-variables.md#sql_mode) session variable)
* max_sort_length ([max_sort_length](../system-variables/server-system-variables.md#max_sort_length) session variable)
* group_concat_max_len ([group_concat_max_len](../system-variables/server-system-variables.md#group_concat_max_len) session variable)
* default_week_format ([default_week_format](../system-variables/server-system-variables.md#default_week_format) session variable)
* div_precision_increment ([div_precision_increment](../system-variables/server-system-variables.md#div_precision_increment) session variable)
* lc_time_names ([lc_time_names](../system-variables/server-system-variables.md#lc_time_names) session variable)


More information can be found by viewing the source code ([MariaDB 10.1](../../../../../release-notes/mariadb-community-server/what-is-mariadb-1010.md)) :


* [sql_cache.cc](https://github.com/MariaDB/server/blob/10.1/sql/sql_cache.cc)
* [sql_cache.h](https://github.com/MariaDB/server/blob/10.1/sql/sql_cache.h)


## Timeout and Mutex Contention


When searching for a query inside the query cache, a try_lock function waits with a timeout of 50ms. If the lock fails, the query isn't executed via the query cache. This timeout is hard coded ([MDEV-6766](https://jira.mariadb.org/browse/MDEV-6766) include two variables to tune this timeout).


From the sql_cache.cc, function "try_lock" using TIMEOUT :


```
struct timespec waittime;
        set_timespec_nsec(waittime,(ulong)(50000000L));  /* Wait for 50 msec */
        int res= mysql_cond_timedwait(&COND_cache_status_changed,
                                      &structure_guard_mutex, &waittime);
        if (res == ETIMEDOUT)
          break;
```

When inserting a query inside the query cache or aborting a query cache insert (using the [KILL](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/kill.md) command for example), a try_lock function waits until the query cache returns; no timeout is used in this case.


When two processes execute the same query, only the last process stores the query result. All other processes increase the [Qcache_not_cached](../system-variables/server-status-variables.md#qcache_not_cached) status variable.


## SQL_NO_CACHE and SQL_CACHE


There are two aspects to the query cache: placing a query in the cache, and retrieving it from the cache.


1. Adding a query to the query cache. This is done automatically for cacheable queries (see ([Queries Stored in the Query Cache](#queries-stored-in-the-query-cache)) when the [query_cache_type](../system-variables/server-system-variables.md#query_cache_type) system variable is set to `1`, or `ON` and the query contains no SQL_NO_CACHE clause, or when the [query_cache_type](../system-variables/server-system-variables.md#query_cache_type) system variable is set to `2`, or `DEMAND`, and the query contains the SQL_CACHE clause.
1. Retrieving a query from the cache. This is done after the server receives the query and before the query parser. In this case one point should be considered:


When using SQL_NO_CACHE, it should be after the first SELECT hint, for example :


```
SELECT SQL_NO_CACHE .... FROM (SELECT SQL_CACHE ...) AS temp_table
```

instead of


```
SELECT SQL_CACHE .... FROM (SELECT SQL_NO_CACHE ...) AS temp_table
```

The second query will be checked. The query cache only checks if SQL_NO_CACHE/SQL_CACHE exists after the first SELECT. (More info at [MDEV-6631](https://jira.mariadb.org/browse/MDEV-6631))

<span></span>
