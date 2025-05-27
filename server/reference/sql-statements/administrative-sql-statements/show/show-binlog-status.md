# SHOW MASTER STATUS

## Syntax

```
SHOW MASTER STATUS
SHOW BINLOG STATUS -- From MariaDB 10.5.2
```

## Description

Provides status information about the [binary log](../../../../server-management/server-monitoring-logs/binary-log/) files of the primary.

This statement requires the [SUPER](../../account-management-sql-commands/grant.md#super) privilege, the [REPLICATION\_CLIENT](../../account-management-sql-commands/grant.md#replication-client) privilege, or, from [MariaDB 10.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-5-series/mariadb-1052-release-notes), the [BINLOG MONITOR](../../account-management-sql-commands/grant.md#binlog-monitor) privilege.

To see information about the current [GTIDs](../../../../ha-and-performance/standard-replication/gtid.md) in the binary log, use the[gtid\_binlog\_pos](../../../../ha-and-performance/standard-replication/gtid.md) variable.

`SHOW MASTER STATUS` was renamed to `SHOW BINLOG STATUS` in [MariaDB 10.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-5-series/mariadb-1052-release-notes), but the old name remains an alias for compatibility purposes.

## Example

```
SHOW MASTER STATUS;
+--------------------+----------+--------------+------------------+
| File               | Position | Binlog_Do_DB | Binlog_Ignore_DB |
+--------------------+----------+--------------+------------------+
| mariadb-bin.000016 |      475 |              |                  |
+--------------------+----------+--------------+------------------+
SELECT @@global.gtid_binlog_pos;
+--------------------------+
| @@global.gtid_binlog_pos |
+--------------------------+
| 0-1-2                    |
+--------------------------+
```

## See Also

* [MariaDB replication](../../../../ha-and-performance/standard-replication/)
* [Using and Maintaining the Binary Log](../../../../server-management/server-monitoring-logs/binary-log/using-and-maintaining-the-binary-log.md)
* [The gtid\_binlog\_pos variable](../../../../ha-and-performance/standard-replication/gtid.md)

GPLv2 fill\_help\_tables.sql
