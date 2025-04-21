
# Slow Query Log Overview


The slow query log is a record of SQL queries that took a long time to perform.


Note that, if your queries contain user's passwords, the slow query log may contain passwords too. Thus, it should be protected.


The number of rows affected by the slow query are also recorded in the slow query log.


## Enabling the Slow Query Log


The slow query log is disabled by default.


To enable the slow query log, set the [slow_query_log](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#slow_query_log) system variable (or, from [MariaDB 10.11](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/release-notes-mariadb-10-11-series/what-is-mariadb-1011), [log_slow_query](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#log_slow_query)) to `1`. It can be changed dynamically with [SET GLOBAL](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/set-commands/set.md#global-session). For example:


```
SET GLOBAL slow_query_log=1;
```

It can also be set in a server [option group](../../getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md) prior to starting up the server. For example:


```
[mariadb]
...
slow_query_log
```

## Configuring the Slow Query Log Filename


By default, the slow query log is written to `${hostname}-slow.log` in the [datadir](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#datadir) directory. However, this can be changed.


One way to configure the slow query log filename is to set the [slow_query_log_file](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#slow_query_log_file) system variable (or, from [MariaDB 10.11](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/release-notes-mariadb-10-11-series/what-is-mariadb-1011), [log_slow_query_file](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#log_slow_query_file)). It can be changed dynamically with [SET GLOBAL](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/set-commands/set.md#global-session). For example:


```
SET GLOBAL slow_query_log_file='mariadb-slow.log';
```

It can also be set in a server [option group](../../getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md) prior to starting up the server. For example:


```
[mariadb]
...
slow_query_log
slow_query_log_file=mariadb-slow.log
```

If it is a relative path, then the [slow_query_log_file](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#slow_query_log_file) is relative to the [datadir](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#datadir) directory.


However, the [slow_query_log_file](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#slow_query_log_file) system variable can also be an absolute path. For example:


```
[mariadb]
...
slow_query_log
slow_query_log_file=/var/log/mysql/mariadb-slow.log
```

Another way to configure the slow query log filename is to set the [log-basename](../../getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md#-log-basename) option, which configures MariaDB to use a common prefix for all log files (e.g. slow query log, [general query log](../general-query-log.md), [error log](../error-log.md), [binary logs](../binary-log/README.md), etc.). The slow query log filename will be built by adding `-slow.log` to this prefix. This option cannot be set dynamically. It can be set in a server [option group](../../getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md) prior to starting up the server. For example:


```
[mariadb]
...
log-basename=mariadb
slow_query_log
```

The [log-basename](../../getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md) cannot be an absolute path. The log file name is relative to the [datadir](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#datadir) directory.


## Choosing the Slow Query Log Output Destination


The slow query log can either be written to a file on disk, or it can be written to the [slow_log](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/the-mysql-database-tables/mysql-slow_log-table.md) table in the [mysql](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/the-mysql-database-tables/README.md) database. To choose the slow query log output destination, set the [log_output](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#log_output) system variable.


### Writing the Slow Query Log to a File


The slow query log is output to a file by default. However, it can be explicitly chosen by setting the [log_output](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#log_output) system variable to `FILE`. It can be changed dynamically with [SET GLOBAL](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/set-commands/set.md#global-session). For example:


```
SET GLOBAL log_output='FILE';
```

It can also be set in a server [option group](../../getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md) prior to starting up the server. For example:


```
[mariadb]
...
log_output=FILE
slow_query_log
slow_query_log_file=slow-queries.log
```

### Writing the Slow Query Log to a Table


The slow query log can either be written to the [slow_log](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/the-mysql-database-tables/mysql-slow_log-table.md) table in the [mysql](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/the-mysql-database-tables/README.md) database by setting the [log_output](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#log_output) system variable to `TABLE`. It can be changed dynamically with [SET GLOBAL](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/set-commands/set.md#global-session). For example:


```
SET GLOBAL log_output='TABLE';
```

It can also be set in a server [option group](../../getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md) prior to starting up the server. For example:


```
[mariadb]
...
log_output=TABLE
slow_query_log
```

Some rows in this table might look like this:


```
SELECT * FROM mysql.slow_log\G
...
*************************** 2. row ***************************
    start_time: 2014-11-11 07:56:28.721519
     user_host: root[root] @ localhost []
    query_time: 00:00:12.000215
     lock_time: 00:00:00.000000
     rows_sent: 1
 rows_examined: 0
            db: test
last_insert_id: 0
     insert_id: 0
     server_id: 1
      sql_text: SELECT SLEEP(12)
     thread_id: 74
...
```

See [Writing logs into tables](../writing-logs-into-tables.md) for more information.


## Disabling the Slow Query Log for a Session


A user can disable logging to the slow query log for a connection by setting the [slow_query_log](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#slow_query_log) system variable (or, from [MariaDB 10.11](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/release-notes-mariadb-10-11-series/what-is-mariadb-1011), [log_slow_query](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#log_slow_query)) to `0`. For example:


```
SET SESSION slow_query_log=0;
```

## Disabling the Slow Query Log for Specific Statements


It is possible to disable logging to the slow query log for specific types of statements by setting the [log_slow_disabled_statements](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#log_slow_disabled_statements) system variable. This option cannot be set dynamically. It can be set in a server [option group](../../getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md) prior to starting up the server. For example:


```
[mariadb]
...
log_output=FILE
general_log
general_log_file=queries.log
log_slow_disabled_statements='admin,call,slave,sp'
```

## Configuring the Slow Query Log Time


The time that defines a slow query can be configured by setting the [long_query_time](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#long_query_time) system variable (or, from [MariaDB 10.11](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/release-notes-mariadb-10-11-series/what-is-mariadb-1011), [log_slow_query_time](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#log_slow_query_time)). It uses a units of seconds, with an optional milliseconds component. The default value is `10`. It can be changed dynamically with [SET GLOBAL](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/set-commands/set.md#global-session). For example:


```
SET GLOBAL long_query_time=5.0;
```

It can also be set in a server [option group](../../getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md) prior to starting up the server. For example:


```
[mariadb]
...
log_output=FILE
slow_query_log
slow_query_log_file=slow-queries.log
long_query_time=5.0
```

## Logging Queries That Don't Use Indexes


It can be beneficial to log queries that don't use indexes to the slow query log, since queries that don't use indexes can usually be optimized either by adding an index or by doing a slight rewrite. The slow query log can be configured to log queries that don't use indexes regardless of their execution time by adding the option "not_using_index" to [log_slow_filter](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#log_slow_filter) or setting the [log_queries_not_using_indexes](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#log_queries_not_using_indexes) system variable to 1. It can be changed dynamically with [SET GLOBAL](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/set-commands/set.md#global-session).
Some examples:


```
SET @@log_slow_filter=concat(@@log_slow_filter,",not_using_index");
SET GLOBAL log_queries_not_using_indexes=ON;
```

It can also be set in a server [option group](../../getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md) prior to starting up the server. For example:


```
[mariadb]
...
log_output=FILE
slow_query_log
slow_query_log_file=slow-queries.log
long_query_time=5.0
log_queries_not_using_indexes=ON
```

As a significant number of queries can run quickly even without indexes, you can use the [min_examined_row_limit](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#min_examined_row_limit) system variable (or, from [MariaDB 10.11](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/release-notes-mariadb-10-11-series/what-is-mariadb-1011), [log_slow_min_examined_row_limit](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#log_slow_min_examined_row_limit)) with [log_queries_not_using_indexes](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#log_queries_not_using_indexes) to limit the logged queries to those having a material impact on the server.


## Excluding Queries That Examine Fewer Than a Minimum Row Limit


It can be beneficial to exclude queries that examine fewer than a minimum number of rows from the log. This can be done by setting the [min_examined_row_limit](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#min_examined_row_limit) system variable, or, from [MariaDB 10.11](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/release-notes-mariadb-10-11-series/what-is-mariadb-1011), [log_slow_min_examined_row_limit](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#log_slow_min_examined_row_limit). It can be changed dynamically with [SET GLOBAL](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/set-commands/set.md#global-session). For example:


```
SET GLOBAL min_examined_row_limit=100000;
```

It can also be set in a server [option group](../../getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md) prior to starting up the server. For example:


```
[mariadb]
...
log_output=FILE
slow_query_log
slow_query_log_file=slow-queries.log
long_query_time=5.0
min_examined_row_limit=100000
```

## Logging Slow Administrative Statements


By default, the Slow Query Log logs administrative statements. To disable logging of administrative statements, remove "admin" from the [log_slow_filter](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#log_slow_filter) system variable or alternatively 
set the [log_slow_admin_statements](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#log_slow_admin_statements) system variable to OFF. The Slow Query Log considers the following statements administrative: [ALTER TABLE](../../../reference/sql-statements-and-structure/sql-statements/data-definition/alter/alter-table.md), [ANALYZE TABLE](../../../reference/sql-statements-and-structure/sql-statements/table-statements/analyze-table.md), [CHECK TABLE](../../../reference/sql-statements-and-structure/sql-statements/table-statements/check-table.md), [CREATE INDEX](../../../reference/sql-statements-and-structure/sql-statements/data-definition/create/create-index.md), [DROP INDEX](../../../reference/sql-statements-and-structure/sql-statements/data-definition/drop/drop-index.md), [OPTIMIZE TABLE](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/optimizing-tables/optimize-table.md), and [REPAIR TABLE](../../../reference/sql-statements-and-structure/sql-statements/table-statements/repair-table.md). In [MariaDB 10.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/old-releases/release-notes-mariadb-10-3-series/what-is-mariadb-103) and later, this also includes [ALTER SEQUENCE](../../../reference/sql-statements-and-structure/sequences/alter-sequence.md) statements.


You can dynamically enable this feature using a [SET GLOBAL](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/set-commands/set.md#global-session) statement and setting it for just the current connection with LOCAL. Some examples:


```
SET SESSION log_slow_filter=replace(@@log_slow_filter,"admin","");
SET GLOBAL log_slow_admin_statements=ON;
```

It can also be set in a server [option group](../../getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md) prior to starting up the server. For example:


```
[mariadb]
...
log_output=FILE
slow_query_log
slow_query_log_file=slow-queries.log
long_query_time=5.0
log_slow_admin_statements=ON
```

## Enabling the Slow Query Log for Specific Criteria


It is possible to enable logging to the slow query log for queries that meet specific criteria by configuring the [log_slow_filter](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#log_slow_filter) system variable. It can be changed dynamically with [SET GLOBAL](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/set-commands/set.md#global-session). For example:


```
SET GLOBAL log_slow_filter='filesort,filesort_on_disk,tmp_table,tmp_table_on_disk';
```

It can also be set in a server [option group](../../getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md) prior to starting up the server. For example:


```
[mariadb]
...
log_output=FILE
slow_query_log
slow_query_log_file=slow-queries.log
long_query_time=5.0
log_slow_filter=filesort,filesort_on_disk,tmp_table,tmp_table_on_disk
```

You can find all options for log_slow_filter at [log_slow_filter system variable](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#log_slow_filter) or at [Slow Query Log Extended Statistics](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/query-optimizations/statistics-for-optimizing-queries/slow-query-log-extended-statistics.md#log_slow_filter).


## Throttling the Slow Query Log


The slow query log can create a lot of I/O, so it can be beneficial to throttle it in some cases. The slow query log can be throttled by configuring the [log_slow_rate_limit](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#log_slow_rate_limit) system variable. It can be changed dynamically with [SET GLOBAL](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/set-commands/set.md#global-session). For example:


```
SET GLOBAL log_slow_rate_limit=5;
```

It can also be set in a server [option group](../../getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md) prior to starting up the server. For example:


```
[mariadb]
...
log_output=FILE
slow_query_log
slow_query_log_file=slow-queries.log
long_query_time=5.0
log_slow_rate_limit=5
```

## Configuring the Slow Query Log Verbosity


There are a few optional pieces of information that can be included in the slow query log for each query. This optional information can be included by configuring the [log_slow_verbosity](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#log_slow_verbosity) system variable. It can be changed dynamically with [SET GLOBAL](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/set-commands/set.md#global-session). For example:


```
SET GLOBAL log_slow_verbosity='full';
```

It can also be set in a server [option group](../../getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md) prior to starting up the server. For example:


```
[mariadb]
...
log_output=FILE
slow_query_log
slow_query_log_file=slow-queries.log
long_query_time=5.0
log_slow_verbosity=query_plan,explain,engine
```

It is possible to have [EXPLAIN output printed in the slow query log](explain-in-the-slow-query-log.md).


## Viewing the Slow Query Log


Slow query logs written to file can be viewed with any text editor, or you can use the [mariadb-dumpslow](../../../clients-and-utilities/mariadb-dumpslow.md) tool to ease the process by summarizing the information.


Queries that you find in the log are key queries to try to optimize by constructing a [more efficient query](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/query-optimizations/README.md) or by making [better use of indexes](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/optimization-and-indexes/README.md).


For queries that appear in the log that cannot be optimized in the above ways, perhaps because they are simply very large selects, due to slow hardware, or very high lock/cpu/io contention, using shard/clustering/load balancing solutions, better hardware, or stats tables may help to improve these queries.


Slow query logs written to table can be viewed by querying the [slow_log](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/the-mysql-database-tables/mysql-slow_log-table.md) table.


## Variables Related to the Slow Query Log


* [slow_query_log](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#slow_query_log) - enable/disable the slow query log. Renamed to [log_slow_query](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#log_slow_query) from [MariaDB 10.11](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/release-notes-mariadb-10-11-series/what-is-mariadb-1011).
* [log_output](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#log_output) - how the output will be written
* [log_slow_admin_statements](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#log_slow_admin_statements). Whether to log OPTIMIZE, ANALYZE, ALTER and other administrative statements to the slow log. Deprecated from [MariaDB 11.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/old-releases/release-notes-mariadb-11-0-series/what-is-mariadb-110), use [log_slow_filter](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#log_slow_filter) without admin.
* [slow_query_log_file](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#slow_query_log_file) - name of the slow query log file. Renamed to [log_slow_query_file_name](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#log_slow_query_file_name) from [MariaDB 10.11.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/release-notes-mariadb-10-11-series/mariadb-10-11-0-release-notes).
* [long_query_time](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#long_query_time) - time in seconds/microseconds defining a slow query. Renamed to [log_slow_query_time](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#log_slow_query_time) from [MariaDB 10.11.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/release-notes-mariadb-10-11-series/mariadb-10-11-0-release-notes).
* [log_queries_not_using_indexes](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#log_queries_not_using_indexes) - whether to log queries that don't use indexes
* [log_slow_admin_statements](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#log_slow_admin_statements) - whether to log certain admin statements
* [log_slow_disabled_statements](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#log_slow_disabled_statements) - types of statements that should not be logged in the slow query log
* [min_examined_row_limit](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#min_examined_row_limit) - minimum rows a query must examine to be slow. Renamed to [log_slow_min_examined_row_limit](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#log_slow_min_examined_row_limit) from [MariaDB 10.11.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/release-notes-mariadb-10-11-series/mariadb-10-11-0-release-notes).
* [log_slow_rate_limit](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#log_slow_rate_limit) - permits a fraction of slow queries to be logged
* [log_slow_verbosity](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#log_slow_verbosity) - amount of detail in the log
* [log_slow_filter](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#log_slow_filter) - limit which queries to log
* [log_slow_slave_statements](../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md#log_slow_slave_statements) - log slow statements executed by replica thread to the slow log if it is open.


## Rotating the Slow Query Log on Unix and Linux


Unix and Linux distributions offer the [logrotate](https://linux.die.net/man/8/logrotate) utility, which makes it very easy to rotate log files. See [Rotating Logs on Unix and Linux](../rotating-logs-on-unix-and-linux.md) for more information on how to use this utility to rotate the slow query log.

