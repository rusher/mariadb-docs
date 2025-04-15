# Information Schema USER_STATISTICS Table

The [Information Schema](/kb/en/information_schema/) `USER_STATISTICS` table holds statistics about user activity. This is part of the [User Statistics](../../../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/query-optimizations/statistics-for-optimizing-queries/user-statistics.md) feature, which is not enabled by default.

You can use this table to find out such things as which user is causing the most load and which users are being abusive. You can also use this table to measure how close to capacity the server may be.

It contains the following columns:

| Field | Type | Notes |
| --- | --- | --- |
| Field | Type | Notes |
| USER | varchar(48) | The username. The value '#mysql_system_user#' appears when there is no username (such as for the slave SQL thread). |
| TOTAL_CONNECTIONS | int(11) | The number of connections created for this user. |
| CONCURRENT_CONNECTIONS | int(11) | The number of concurrent connections for this user. |
| CONNECTED_TIME | int(11) | The cumulative number of seconds elapsed while there were connections from this user. |
| BUSY_TIME | double | The cumulative number of seconds there was activity on connections from this user. |
| CPU_TIME | double | The cumulative CPU time elapsed while servicing this user's connections. |
| BYTES_RECEIVED | bigint(21) | The number of bytes received from this user's connections. |
| BYTES_SENT | bigint(21) | The number of bytes sent to this user's connections. |
| BINLOG_BYTES_WRITTEN | bigint(21) | The number of bytes written to the [binary log](../../../../../../../server-usage/programming-customizing-mariadb/stored-routines/binary-logging-of-stored-routines.md) from this user's connections. |
| ROWS_READ | bigint(21) | The number of rows read by this user's connections. |
| ROWS_SENT | bigint(21) | The number of rows sent by this user's connections. |
| ROWS_DELETED | int(21) | The number of rows deleted by this user's connections. |
| ROWS_INSERTED | bigint(21) | The number of rows inserted by this user's connections. |
| ROWS_UPDATED | bigint(21) | The number of rows updated by this user's connections. |
| KEY_READ_HITS | bigint(21) | From [MariaDB 11.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/what-is-mariadb-115) |
| KEY_READ_MISSES | bigint(21) | From [MariaDB 11.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/what-is-mariadb-115) |
| SELECT_COMMANDS | bigint(21) | The number of [SELECT](../../../../../../../server-usage/replication-cluster-multi-master/standard-replication/selectively-skipping-replication-of-binlog-events.md) commands executed from this user's connections. |
| UPDATE_COMMANDS | bigint(21) | The number of [UPDATE](../../../../data-manipulation/changing-deleting-data/update.md) commands executed from this user's connections. |
| OTHER_COMMANDS | bigint(21) | The number of other commands executed from this user's connections. |
| COMMIT_TRANSACTIONS | bigint(21) | The number committed transactions. Note that in autocommit mode every statement is a separate transaction. |
| ROLLBACK_TRANSACTIONS | bigint(21) | The number of transactions that were rolled back. |
| DENIED_CONNECTIONS | bigint(21) | The number of connections denied to this user. |
| LOST_CONNECTIONS | bigint(21) | The number of this user's connections that were terminated uncleanly. |
| ACCESS_DENIED | bigint(21) | The number of times this user's connections issued commands that were denied. |
| EMPTY_QUERIES | bigint(21) | The number of times this user's connections sent queries to the server that did not return data to the client (a per-user aggregate of the [empty_queries](../../../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-status-variables.md#empty_queries) status variable). |
| TOTAL_SSL_CONNECTIONS | bigint(21) | The number of [TLS connections](../../../../../../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/secure-connections-overview.md) created for this user. |
| MAX_STATEMENT_TIME_EXCEEDED | bigint(21) | The number of times a statement was aborted, because it was executed longer than its [MAX_STATEMENT_TIME](/kb/en/aborting-statements-that-take-longer-than-a-certain-time-to-execute/) threshold. |

#

# Example

```
SELECT * FROM information_schema.USER_STATISTICS\G
*************************** 1. row ***************************
 USER: root
 TOTAL_CONNECTIONS: 1
CONCURRENT_CONNECTIONS: 0
 CONNECTED_TIME: 297
 BUSY_TIME: 0.001725
 CPU_TIME: 0.001982
 BYTES_RECEIVED: 388
 BYTES_SENT: 2327
 BINLOG_BYTES_WRITTEN: 0
 ROWS_READ: 0
 ROWS_SENT: 12
 ROWS_DELETED: 0
 ROWS_INSERTED: 13
 ROWS_UPDATED: 0
 SELECT_COMMANDS: 4
 UPDATE_COMMANDS: 0
 OTHER_COMMANDS: 3
 COMMIT_TRANSACTIONS: 0
 ROLLBACK_TRANSACTIONS: 0
 DENIED_CONNECTIONS: 0
 LOST_CONNECTIONS: 0
 ACCESS_DENIED: 0
 EMPTY_QUERIES: 1
```