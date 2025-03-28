# SHOW RELAYLOG EVENTS

The terms *master* and *slave* have historically been used in replication, and MariaDB has begun the process of adding *primary* and *replica* synonyms. The old terms will continue to be used to maintain backward compatibility - see [MDEV-18777](https://jira.mariadb.org/browse/MDEV-18777) to follow progress on this effort.

#

# Syntax

```
SHOW RELAYLOG ['connection_name'] EVENTS
 [IN 'log_name'] [FROM pos] [LIMIT [offset,] row_count]
 [ FOR CHANNEL 'channel_name']
```

#

# Description

On [replicas](/en/standard-replication/), this command shows the events in the [relay log](../../../../../server-management/server-monitoring-logs/binary-log/relay-log.md). If `'log_name'` is not specified, the first relay log is shown.

Syntax for the `LIMIT` clause is the same as for [SELECT ... LIMIT](../../../../../server-usage/replication-cluster-multi-master/standard-replication/selectively-skipping-replication-of-binlog-events.md#limit).

Using the `LIMIT` clause is highly recommended because the `SHOW RELAYLOG EVENTS` command returns the complete contents of the relay log, which can be quite large.

This command does not return events related to setting user and system variables. If you need those, use [mariadb-binlog](../../../../../clients-and-utilities/mariadb-binlog/mariadb-binlog-options.md).

On the primary, this command does nothing.

Requires the [REPLICA MONITOR](../../account-management-sql-commands/grant.md#replica-monitor) privilege (>= [MariaDB 10.5.9](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/release-notes-mariadb-105-series/mariadb-1059-release-notes)), the [REPLICATION SLAVE ADMIN](../../account-management-sql-commands/grant.md#replication-slave-admin) privilege (>= [MariaDB 10.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/release-notes-mariadb-105-series/mariadb-1052-release-notes)) or the [REPLICATION SLAVE](../../account-management-sql-commands/grant.md#replication-slave) privilege (<= [MariaDB 10.5.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/release-notes-mariadb-105-series/mariadb-1051-release-notes)).

#

### connection_name

If there is only one nameless primary, or the default primary (as specified by the [default_master_connection](/en/replication-and-binary-log-server-system-variables/#default_master_connection) system variable) is intended, `connection_name` can be omitted. If provided, the `SHOW RELAYLOG` statement will apply to the specified primary. `connection_name` is case-insensitive.

#

#### MariaDB starting with [10.7.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/release-notes-mariadb-10-7-series/mariadb-1070-release-notes)

The `FOR CHANNEL` keyword was added for MySQL compatibility. This is identical as
using the channel_name directly after `SHOW RELAYLOG`.