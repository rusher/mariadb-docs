
# Aborting Statements that Exceed a Certain Time to Execute


## Overview


[MariaDB 10.1.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-1-release-notes) introduced the [max_statement_time](../system-variables/server-system-variables.md#max_statement_time) system variable. When set to a non-zero value, any queries taking longer than this time in seconds will be aborted. The default is zero, and no limits are then applied. The aborted query has no effect on any larger transaction or connection contexts. The variable is of type double, thus you can use subsecond timeout. For example you can use value 0.01 for 10 milliseconds timeout.


The value can be set globally or per session, as well as per user or per query (see below).
Replicas are not affected by this variable, however from [MariaDB 10.10](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/old-releases/release-notes-mariadb-10-10-series/what-is-mariadb-1010), there is [slave_max_statement_time](../../standard-replication/replication-and-binary-log-system-variables.md#slave_max_statement_time) which serves the same purpose on replicas only.


An associated status variable, [max_statement_time_exceeded](../system-variables/server-status-variables.md#max_statement_time_exceeded), stores the number of queries that have exceeded the execution time specified by [max_statement_time](../system-variables/server-system-variables.md#max_statement_time), and a `MAX_STATEMENT_TIME_EXCEEDED` column was added to the [CLIENT_STATISTICS](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-client_statistics-table.md) and [USER STATISTICS](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-user_statistics-table.md) Information Schema tables.


The feature was based upon a patch by Davi Arnaut.


## User [max_statement_time](../system-variables/server-system-variables.md#max_statement_time)


[max_statement_time](../system-variables/server-system-variables.md#max_statement_time) can be stored per user with the [GRANT ... MAX_STATEMENT_TIME](../../../../reference/sql-statements-and-structure/sql-statements/account-management-sql-commands/grant.md) syntax.


## Per-query [max_statement_time](../system-variables/server-system-variables.md#max_statement_time)


By using [max_statement_time](../system-variables/server-system-variables.md#max_statement_time) in conjunction with [SET STATEMENT](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/set-commands/set-statement.md), it is possible to limit the execution time of individual queries. For example:


```
SET STATEMENT max_statement_time=100 FOR 
  SELECT field1 FROM table_name ORDER BY field1;
```

max_statement_time per query
Individual queries can also be limited by adding a `MAX_STATEMENT_TIME` clause to the query. For example:

```
SELECT MAX_STATEMENT_TIME=2 * FROM t1;
```


## Limitations


* [max_statement_time](../system-variables/server-system-variables.md#max_statement_time) does not work in embedded servers.
* [max_statement_time](../system-variables/server-system-variables.md#max_statement_time) does not work for [COMMIT](../../../../reference/sql-statements-and-structure/sql-statements/transactions/commit.md) statements in a Galera cluster (see [MDEV-18673](https://jira.mariadb.org/browse/MDEV-18673) for discussion).


## Differences Between the MariaDB and MySQL Implementations


MySQL 5.7.4 introduced similar functionality, but the MariaDB implementation differs in a number of ways.


* The MySQL version of [max_statement_time](../system-variables/server-system-variables.md#max_statement_time) (`max_execution_time`) is defined in millseconds, not seconds
* MySQL's implementation can only kill SELECTs, while MariaDB's can kill any queries (excluding stored procedures).
* MariaDB only introduced the [max_statement_time_exceeded](../system-variables/server-status-variables.md#max_statement_time_exceeded) status variable, while MySQL also introduced a number of other variables which were not seen as necessary in MariaDB.
* The `SELECT MAX_STATEMENT_TIME = N ...` syntax is not valid in MariaDB. In MariaDB one should use `SET STATEMENT MAX_STATEMENT_TIME=N FOR...`.


## See Also


* [Query limits and timeouts](query-limits-and-timeouts.md)
* [lock_wait_timeout](../system-variables/server-system-variables.md#lock_wait_timeout) variable

