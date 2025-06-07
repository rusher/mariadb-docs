# STOP REPLICA

The terms _master_ and _slave_ have historically been used in replication, and MariaDB has begun the process of adding _primary_ and _replica_ synonyms. The old terms will continue to be used to maintain backward compatibility - see [MDEV-18777](https://jira.mariadb.org/browse/MDEV-18777) to follow progress on this effort.

## Syntax

```
STOP { SLAVE | REPLICA } ["connection_name"] [thread_type [, thread_type] ... ] [FOR CHANNEL "connection_name"]

STOP ALL { SLAVES | REPLICAS } [thread_type [, thread_type]]

STOP { SLAVE | REPLICA } ["connection_name"] [thread_type [, thread_type] ... ]

STOP ALL { SLAVES | REPLICAS } [thread_type [, thread_type]] 

thread_type: IO_THREAD | SQL_THREAD
```

## Description

Stops the replica threads. `STOP REPLICA` requires the [SUPER](../../../reference/sql-statements/account-management-sql-statements/grant.md#super) privilege, or, from [MariaDB 10.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/mariadb-1052-release-notes), the [REPLICATION SLAVE ADMIN](../../../reference/sql-statements/account-management-sql-statements/grant.md#replication-slave-admin) privilege.

Like [START REPLICA](../../../reference/sql-statements/administrative-sql-statements/replication-statements/start-replica.md), this statement may be used with the `IO_THREAD` and`SQL_THREAD` options to name the thread or threads to be stopped. In almost all cases, one never need to use the `thread_type` options.

`STOP REPLICA` waits until any current replication event group affecting\
one or more non-transactional tables has finished executing (if there\
is any such replication group), or until the user issues a [KILL QUERY](../../../reference/sql-statements/administrative-sql-statements/kill.md) or [KILL CONNECTION](../../../reference/sql-statements/administrative-sql-statements/kill.md) statement.

Note that `STOP REPLICA` doesn't delete the connection permanently. Next time you execute [START REPLICA](../../../reference/sql-statements/administrative-sql-statements/replication-statements/start-replica.md) or the MariaDB server restarts, the replica connection is restored with it's [original arguments](../../../reference/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md). If you want to delete a connection, you should execute [RESET REPLICA](../../../reference/sql-statements/administrative-sql-statements/replication-statements/reset-replica.md).

#### STOP ALL REPLICAS

`STOP ALL REPLICAS` stops all your running replicas. It will give you a `note` for every stopped connection. You can check the notes with [SHOW WARNINGS](../../../reference/sql-statements/administrative-sql-statements/show/show-warnings.md).

#### connection\_name

The `connection_name` option is used for [multi-source replication](../multi-source-replication.md).

If there is only one nameless master, or the default master (as specified by the [default\_master\_connection](../replication-and-binary-log-system-variables.md) system variable) is intended, `connection_name` can be omitted. If provided, the `STOP REPLICA` statement will apply to the specified master. `connection_name` is case-insensitive.

**MariaDB starting with** [**10.7.0**](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-7-series/mariadb-1070-release-notes)

The `FOR CHANNEL` keyword was added for MySQL compatibility. This is identical as\
using the channel\_name directly after `STOP REPLICA`.

## See Also

* [CHANGE MASTER TO](../../../reference/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md) is used to create and change connections.
* [START REPLICA](../../../reference/sql-statements/administrative-sql-statements/replication-statements/start-replica.md) is used to start a predefined connection.
* [RESET REPLICA](../../../reference/sql-statements/administrative-sql-statements/replication-statements/reset-replica.md) is used to reset parameters for a connection and also to permanently delete a master connection.

GPLv2 fill\_help\_tables.sql
