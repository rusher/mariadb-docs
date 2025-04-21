
# KILL [CONNECTION | QUERY]

## Syntax


```
KILL [HARD | SOFT] { {CONNECTION|QUERY} thread_id | QUERY ID query_id | USER user_name }
```


## Description


Each connection to mariadbd runs in a separate thread. You can see which threads
are running with the `SHOW PROCESSLIST` statement and kill a
thread with the `KILL thread_id` statement. 
`KILL` allows the optional `CONNECTION` or
`QUERY` modifier:


* `KILL CONNECTION` is the same as `KILL` with no
 modifier: It terminates the connection associated with the given thread or query id.
* `KILL QUERY` terminates the statement that the connection thread_id is
 currently executing, but leaves the connection itself intact.
* `KILL QUERY ID` terminates the query by query_id, leaving the connection intact.


If a connection is terminated that has an active transaction, the transaction will be rolled back. If only a query is killed, the current transaction will stay active. See also [idle_transaction_timeout](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#idle_transaction_timeout).


If you have the [PROCESS](../account-management-sql-commands/grant.md#process) privilege, you can see all threads. If
you have the [SUPER](../account-management-sql-commands/grant.md#super) privilege, or, from [MariaDB 10.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1052-release-notes), the [CONNECTION ADMIN](../account-management-sql-commands/grant.md#connection-admin) privilege, you can kill all threads and
statements. Otherwise, you can see and kill only your own threads and
statements.


Killing queries that repair or create indexes on MyISAM and Aria tables may result in corrupted tables. Use the `SOFT` option to avoid this!


The `HARD` option (default) kills a command as soon as possible. If you use
`SOFT`, then critical operations that may leave a table in an
inconsistent state will not be interrupted. Such operations include `REPAIR` and `INDEX` creation for [MyISAM](../../../storage-engines/myisam-storage-engine/README.md) and [Aria](../../../storage-engines/aria/README.md) tables ([REPAIR TABLE](../table-statements/repair-table.md), [OPTIMIZE TABLE](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/optimizing-tables/optimize-table.md)).


`KILL ... USER username` will kill all connections/queries for a
given user. `USER` can be specified one of the following ways:


* username (Kill without regard to hostname)
* username@hostname
* [CURRENT_USER](../built-in-functions/secondary-functions/information-functions/current_user.md) or [CURRENT_USER()](../built-in-functions/secondary-functions/information-functions/current_user.md)


If you specify a thread id and that thread does not exist, you get the following error:


```
ERROR 1094 (HY000): Unknown thread id: <thread_id>
```

If you specify a query id that doesn't exist, you get the following error:


```
ERROR 1957 (HY000): Unknown query id: <query_id>
```

However, if you specify a user name, no error is issued for non-connected (or even non-existing) users. To check if the connection/query has been killed, you can use the [ROW_COUNT()](../built-in-functions/secondary-functions/information-functions/row_count.md) function.


A client whose connection is killed receives the following error:


```
ERROR 1317 (70100): Query execution was interrupted
```

To obtain a list of existing sessions, use the [SHOW PROCESSLIST](show/show-processlist.md) statement or query the [Information Schema](system-tables/information-schema/README.md) [PROCESSLIST](system-tables/information-schema/information-schema-tables/information-schema-processlist-table.md) table.


**Note:** You cannot use `KILL` with the Embedded MariaDB Server
library because the embedded server merely runs inside the threads of the host
application. It does not create any connection threads of its own.


**Note:** You can also use 
`mariadb-admin kill thread_id [,thread_id...]`
to kill connections. To get a list of running queries,
use `mariadb-admin processlist`. See [mariadb-admin](../../../../clients-and-utilities/mariadb-admin.md).


[Percona Toolkit](https://www.percona.com/doc/percona-toolkit/) contains a program, [pt-kill](https://www.percona.com/doc/percona-toolkit/pt-kill.html) that can be used to automatically kill connections that match certain criteria. For example, it can be used to terminate idle connections, or connections that have been busy for more than 60 seconds.


## See Also


* [Query limits and timeouts](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/query-optimizations/query-limits-and-timeouts.md)
* [Aborting statements that exceed a certain time to execute](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/query-optimizations/aborting-statements.md)
* [idle_transaction_timeout](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#idle_transaction_timeout)

