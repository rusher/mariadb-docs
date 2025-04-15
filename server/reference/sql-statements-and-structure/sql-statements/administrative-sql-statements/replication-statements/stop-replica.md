
# STOP REPLICA

The terms *master* and *slave* have historically been used in replication, and MariaDB has begun the process of adding *primary* and *replica* synonyms. The old terms will continue to be used to maintain backward compatibility - see [MDEV-18777](https://jira.mariadb.org/browse/MDEV-18777) to follow progress on this effort.



## Syntax


```
STOP REPLICA ["connection_name"] [thread_type [, thread_type] ... ] [FOR CHANNEL "connection_name"]

STOP ALL REPLICAS [thread_type [, thread_type]]

STOP REPLICA ["connection_name"] [thread_type [, thread_type] ... ]

STOP ALL REPLICAS [thread_type [, thread_type]] 

thread_type: IO_THREAD | SQL_THREAD
```


## Description


Stops the replica threads. `<code>STOP REPLICA</code>` requires the [SUPER](../../account-management-sql-commands/grant.md#super) privilege, or, from [MariaDB 10.5.2](../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1052-release-notes.md), the [REPLICATION SLAVE ADMIN](../../account-management-sql-commands/grant.md#replication-slave-admin) privilege.


Like [START REPLICA](start-replica.md), this statement may be used with the `<code>IO_THREAD</code>` and
`<code>SQL_THREAD</code>` options to name the thread or threads to be stopped. In almost all cases, one never need to use the `<code>thread_type</code>` options.


`<code>STOP REPLICA</code>` waits until any current replication event group affecting
one or more non-transactional tables has finished executing (if there
is any such replication group), or until the user issues a [KILL QUERY](../kill.md) or [KILL CONNECTION](../kill.md) statement.


Note that `<code>STOP REPLICA</code>` doesn't delete the connection permanently. Next time you execute [START REPLICA](start-replica.md) or the MariaDB server restarts, the replica connection is restored with it's [original arguments](change-master-to.md). If you want to delete a connection, you should execute [RESET REPLICA](reset-replica.md).


#### STOP ALL REPLICAS


`<code class="highlight fixed" style="white-space:pre-wrap">STOP ALL REPLICAS</code>` stops all your running replicas. It will give you a `<code class="highlight fixed" style="white-space:pre-wrap">note</code>` for every stopped connection. You can check the notes with [SHOW WARNINGS](../show/show-warnings.md).


#### connection_name


The `<code>connection_name</code>` option is used for [multi-source replication](../../../../../server-usage/replication-cluster-multi-master/standard-replication/multi-source-replication.md).


If there is only one nameless master, or the default master (as specified by the [default_master_connection](../../../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md) system variable) is intended, `<code>connection_name</code>` can be omitted. If provided, the `<code>STOP REPLICA</code>` statement will apply to the specified master. `<code>connection_name</code>` is case-insensitive.



##### MariaDB starting with [10.7.0](../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-7-series/mariadb-1070-release-notes.md)
The `<code>FOR CHANNEL</code>` keyword was added for MySQL compatibility. This is identical as
using the channel_name directly after `<code>STOP REPLICA</code>`.


## See Also


* [CHANGE MASTER TO](change-master-to.md) is used to create and change connections.
* [START REPLICA](start-replica.md) is used to start a predefined connection.
* [RESET REPLICA](reset-replica.md) is used to reset parameters for a connection and also to permanently delete a master connection.

