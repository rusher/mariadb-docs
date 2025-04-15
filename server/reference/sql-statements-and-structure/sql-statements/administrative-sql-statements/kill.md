
# KILL [CONNECTION | QUERY]

## Syntax


```
KILL [HARD | SOFT] { {CONNECTION|QUERY} thread_id | QUERY ID query_id | USER user_name }
```


## Description


Each connection to mariadbd runs in a separate thread. You can see which threads
are running with the `<code class="fixed" style="white-space:pre-wrap">SHOW PROCESSLIST</code>` statement and kill a
thread with the `<code class="fixed" style="white-space:pre-wrap">KILL thread_id</code>` statement. 
`<code class="fixed" style="white-space:pre-wrap">KILL</code>` allows the optional `<code class="fixed" style="white-space:pre-wrap">CONNECTION</code>` or
`<code class="fixed" style="white-space:pre-wrap">QUERY</code>` modifier:


* `<code class="fixed" style="white-space:pre-wrap">KILL CONNECTION</code>` is the same as `<code class="fixed" style="white-space:pre-wrap">KILL</code>` with no
 modifier: It terminates the connection associated with the given thread or query id.
* `<code class="fixed" style="white-space:pre-wrap">KILL QUERY</code>` terminates the statement that the connection thread_id is
 currently executing, but leaves the connection itself intact.
* `<code class="fixed" style="white-space:pre-wrap">KILL QUERY ID</code>` terminates the query by query_id, leaving the connection intact.


If a connection is terminated that has an active transaction, the transaction will be rolled back. If only a query is killed, the current transaction will stay active. See also [idle_transaction_timeout](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#idle_transaction_timeout).


If you have the [PROCESS](../account-management-sql-commands/grant.md#process) privilege, you can see all threads. If
you have the [SUPER](../account-management-sql-commands/grant.md#super) privilege, or, from [MariaDB 10.5.2](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1052-release-notes.md), the [CONNECTION ADMIN](../account-management-sql-commands/grant.md#connection-admin) privilege, you can kill all threads and
statements. Otherwise, you can see and kill only your own threads and
statements.


Killing queries that repair or create indexes on MyISAM and Aria tables may result in corrupted tables. Use the `<code>SOFT</code>` option to avoid this!


The `<code class="fixed" style="white-space:pre-wrap">HARD</code>` option (default) kills a command as soon as possible. If you use
`<code class="fixed" style="white-space:pre-wrap">SOFT</code>`, then critical operations that may leave a table in an
inconsistent state will not be interrupted. Such operations include `<code>REPAIR</code>` and `<code>INDEX</code>` creation for [MyISAM](../../../storage-engines/myisam-storage-engine/myisam-system-variables.md) and [Aria](../../../storage-engines/s3-storage-engine/aria_s3_copy.md) tables ([REPAIR TABLE](../table-statements/repair-table.md), [OPTIMIZE TABLE](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/optimizing-tables/optimize-table.md)).


`<code class="fixed" style="white-space:pre-wrap">KILL ... USER username</code>` will kill all connections/queries for a
given user. `<code class="fixed" style="white-space:pre-wrap">USER</code>` can be specified one of the following ways:


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

To obtain a list of existing sessions, use the [SHOW PROCESSLIST](show/show-processlist.md) statement or query the [Information Schema](../../../mariadb-internals/information-schema-plugins-show-and-flush-statements.md) [PROCESSLIST](system-tables/information-schema/information-schema-tables/information-schema-processlist-table.md) table.


**Note:** You cannot use `<code class="fixed" style="white-space:pre-wrap">KILL</code>` with the Embedded MariaDB Server
library because the embedded server merely runs inside the threads of the host
application. It does not create any connection threads of its own.


**Note:** You can also use 
`<code class="fixed" style="white-space:pre-wrap">mariadb-admin kill thread_id [,thread_id...]</code>`
to kill connections. To get a list of running queries,
use `<code class="fixed" style="white-space:pre-wrap">mariadb-admin processlist</code>`. See [mariadb-admin](../../../../clients-and-utilities/mariadb-admin.md).


[Percona Toolkit](https://www.percona.com/doc/percona-toolkit/) contains a program, [pt-kill](https://www.percona.com/doc/percona-toolkit/pt-kill.html) that can be used to automatically kill connections that match certain criteria. For example, it can be used to terminate idle connections, or connections that have been busy for more than 60 seconds.


## See Also


* [Query limits and timeouts](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/query-optimizations/query-limits-and-timeouts.md)
* [Aborting statements that exceed a certain time to execute](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/query-optimizations/aborting-statements.md)
* [idle_transaction_timeout](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#idle_transaction_timeout)

