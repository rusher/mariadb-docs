# STOP SLAVE

The terms *master* and *slave* have historically been used in replication, and MariaDB has begun the process of adding *primary* and *replica* synonyms. The old terms will continue to be used to maintain backward compatibility - see [MDEV-18777](https://jira.mariadb.org/browse/MDEV-18777) to follow progress on this effort.

#

# Syntax

```
STOP SLAVE ["connection_name"] [thread_type [, thread_type] ... ] [FOR CHANNEL "connection_name"]

STOP ALL SLAVES [thread_type [, thread_type]]

STOP REPLICA ["connection_name"] [thread_type [, thread_type] ... ] -- from 10.5.1

STOP ALL REPLICAS [thread_type [, thread_type]] -- from 10.5.1

thread_type: IO_THREAD | SQL_THREAD
```

#

# Description

Stops the replica threads. `STOP SLAVE` requires the [SUPER](../../account-management-sql-commands/grant.md#super) privilege, or, from [MariaDB 10.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/release-notes-mariadb-105-series/mariadb-1052-release-notes), the [REPLICATION SLAVE ADMIN](../../account-management-sql-commands/grant.md#replication-slave-admin) privilege.

Like [START SLAVE](/kb/en/start-slave/), this statement may be used with the `IO_THREAD` and
`SQL_THREAD` options to name the thread or threads to be stopped. In almost all cases, one never need to use the `thread_type` options.

`STOP SLAVE` waits until any current replication event group affecting
one or more non-transactional tables has finished executing (if there
is any such replication group), or until the user issues a [KILL QUERY](/kb/en/kill-connection-query/) or [KILL CONNECTION](/kb/en/kill-connection-query/) statement.

Note that `STOP SLAVE` doesn't delete the connection permanently. Next time you execute [START SLAVE](/kb/en/start-slave/) or the MariaDB server restarts, the replica connection is restored with it's [original arguments](change-master-to.md). If you want to delete a connection, you should execute [RESET SLAVE](/kb/en/reset-slave/).

#

### STOP ALL SLAVES

`STOP ALL SLAVES` stops all your running replicas. It will give you a `note` for every stopped connection. You can check the notes with [SHOW WARNINGS](../show/show-warnings.md).

#

### connection_name

The `connection_name` option is used for [multi-source replication](../../../../../server-usage/replication-cluster-multi-master/standard-replication/multi-source-replication.md).

If there is only one nameless master, or the default master (as specified by the [default_master_connection](/kb/en/replication-and-binary-log-server-system-variables/#default_master_connection) system variable) is intended, `connection_name` can be omitted. If provided, the `STOP SLAVE` statement will apply to the specified master. `connection_name` is case-insensitive.

#

#### MariaDB starting with [10.7.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/release-notes-mariadb-10-7-series/mariadb-1070-release-notes)

The `FOR CHANNEL` keyword was added for MySQL compatibility. This is identical as
using the channel_name directly after `STOP SLAVE`.

#

### STOP REPLICA

#

#### MariaDB starting with [10.5.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/release-notes-mariadb-105-series/mariadb-1051-release-notes)

`STOP REPLICA` is an alias for `STOP SLAVE` from [MariaDB 10.5.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/release-notes-mariadb-105-series/mariadb-1051-release-notes).

#

# See Also

* [CHANGE MASTER TO](change-master-to.md) is used to create and change connections.
* [START SLAVE](/kb/en/start-slave/) is used to start a predefined connection.
* [RESET SLAVE](/kb/en/reset-slave/) is used to reset parameters for a connection and also to permanently delete a master connection.