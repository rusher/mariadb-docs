
# SHOW BINLOG EVENTS

## Syntax


```
SHOW BINLOG EVENTS
   [IN 'log_name'] [FROM pos] [LIMIT [offset,] row_count]
```

## Description


Shows the events in the [binary log](../../../../storage-engines/innodb/binary-log-group-commit-and-innodb-flushing-performance.md). If you do not specify '`log_name`',
the first binary log is displayed.


Requires the [BINLOG MONITOR](../../account-management-sql-commands/grant.md#binlog-monitor) privilege (>= [MariaDB 10.5.2](../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1052-release-notes.md)) or the [REPLICATION SLAVE](../../account-management-sql-commands/grant.md#replication-slave) privilege (<= [MariaDB 10.5.1](../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1051-release-notes.md)).


## Example


```
SHOW BINLOG EVENTS IN 'mysql_sandbox10019-bin.000002';
+-------------------------------+-----+-------------------+-----------+-------------+------------------------------------------------+
| Log_name                      | Pos | Event_type        | Server_id | End_log_pos | Info                                           |
+-------------------------------+-----+-------------------+-----------+-------------+------------------------------------------------+
| mysql_sandbox10019-bin.000002 |   4 | Format_desc       |         1 |         248 | Server ver: 10.0.19-MariaDB-log, Binlog ver: 4 |
| mysql_sandbox10019-bin.000002 | 248 | Gtid_list         |         1 |         273 | []                                             |
| mysql_sandbox10019-bin.000002 | 273 | Binlog_checkpoint |         1 |         325 | mysql_sandbox10019-bin.000002                  |
| mysql_sandbox10019-bin.000002 | 325 | Gtid              |         1 |         363 | GTID 0-1-1                                     |
| mysql_sandbox10019-bin.000002 | 363 | Query             |         1 |         446 | CREATE DATABASE blog                           |
| mysql_sandbox10019-bin.000002 | 446 | Gtid              |         1 |         484 | GTID 0-1-2                                     |
| mysql_sandbox10019-bin.000002 | 484 | Query             |         1 |         571 | use `blog`; CREATE TABLE bb (id INT)           |
+-------------------------------+-----+-------------------+-----------+-------------+------------------------------------------------+
```
