
# Information Schema CLIENT_STATISTICS Table

The [Information Schema](../../../../../../mariadb-internals/information-schema-plugins-show-and-flush-statements.md) `<code>CLIENT_STATISTICS</code>` table holds statistics about client connections. This is part of the [User Statistics](../../../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/query-optimizations/statistics-for-optimizing-queries/user-statistics.md) feature, which is not enabled by default.


It contains the following columns:



| Field | Type | Notes |
| --- | --- | --- |
| Field | Type | Notes |
| CLIENT | VARCHAR(64) | The IP address or hostname the connection originated from. |
| TOTAL_CONNECTIONS | BIGINT(21) | The number of connections created for this client. |
| CONCURRENT_CONNECTIONS | BIGINT(21) | The number of concurrent connections for this client. |
| CONNECTED_TIME | BIGINT(21) | The cumulative number of seconds elapsed while there were connections from this client. |
| BUSY_TIME | DOUBLE | The cumulative number of seconds there was activity on connections from this client. |
| CPU_TIME | DOUBLE | The cumulative CPU time elapsed while servicing this client's connections. Note that this number may be wrong on SMP system if there was a CPU migration for the thread during the execution of the query. |
| BYTES_RECEIVED | BIGINT(21) | The number of bytes received from this client's connections. |
| BYTES_SENT | BIGINT(21) | The number of bytes sent to this client's connections. |
| BINLOG_BYTES_WRITTEN | BIGINT(21) | The number of bytes written to the [binary log](../../../../../../storage-engines/innodb/binary-log-group-commit-and-innodb-flushing-performance.md) from this client's connections. |
| ROWS_READ | BIGINT(21) | The number of rows read by this client's connections. |
| ROWS_SENT | BIGINT(21) | The number of rows sent by this client's connections. |
| ROWS_DELETED | BIGINT(21) | The number of rows deleted by this client's connections. |
| ROWS_INSERTED | BIGINT(21) | The number of rows inserted by this client's connections. |
| ROWS_UPDATED | BIGINT(21) | The number of rows updated by this client's connections. |
| KEY_READ_HITS | BIGINT(21) | From [MariaDB 11.5](../../../../../../../../release-notes/mariadb-community-server/what-is-mariadb-115.md) |
| KEY_READ_MISSES | BIGINT(21) | From [MariaDB 11.5](../../../../../../../../release-notes/mariadb-community-server/what-is-mariadb-115.md) |
| SELECT_COMMANDS | BIGINT(21) | The number of [SELECT](../../../../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/benchmarks-and-long-running-tests/benchmark-results/select-random-ranges-and-select-random-point.md) commands executed from this client's connections. |
| UPDATE_COMMANDS | BIGINT(21) | The number of [UPDATE](../../../../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/tools/buildbot/buildbot-setup/buildbot-setup-for-virtual-machines/buildbot-setup-for-virtual-machines-additional-steps/update-debian-4-mirrors-for-buildbot-vms.md) commands executed from this client's connections. |
| OTHER_COMMANDS | BIGINT(21) | The number of other commands executed from this client's connections. |
| COMMIT_TRANSACTIONS | BIGINT(21) | The number of [COMMIT](../../../../transactions/commit.md) commands issued by this client's connections. |
| ROLLBACK_TRANSACTIONS | BIGINT(21) | The number of [ROLLBACK](../../../../transactions/rollback.md) commands issued by this client's connections. |
| DENIED_CONNECTIONS | BIGINT(21) | The number of connections denied to this client. |
| LOST_CONNECTIONS | BIGINT(21) | The number of this client's connections that were terminated uncleanly. |
| ACCESS_DENIED | BIGINT(21) | The number of times this client's connections issued commands that were denied. |
| EMPTY_QUERIES | BIGINT(21) | The number of times this client's connections sent queries that returned no results to the server. |
| TOTAL_SSL_CONNECTIONS | BIGINT(21) | The number of [TLS connections](../../../../../../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/secure-connections-overview.md) created for this client. (>= [MariaDB 10.1.1](../../../../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-1-release-notes.md)) |
| MAX_STATEMENT_TIME_EXCEEDED | BIGINT(21) | The number of times a statement was aborted, because it was executed longer than its [MAX_STATEMENT_TIME](../../../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/query-optimizations/aborting-statements.md) threshold. (>= [MariaDB 10.1.1](../../../../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-1-release-notes.md)) |



#### Example


```
SELECT * FROM information_schema.CLIENT_STATISTICS\G
*************************** 1. row ***************************
                CLIENT: localhost
     TOTAL_CONNECTIONS: 3
CONCURRENT_CONNECTIONS: 0
        CONNECTED_TIME: 4883
             BUSY_TIME: 0.009722
              CPU_TIME: 0.0102131
        BYTES_RECEIVED: 841
            BYTES_SENT: 13897
  BINLOG_BYTES_WRITTEN: 0
             ROWS_READ: 0
             ROWS_SENT: 214
          ROWS_DELETED: 0
         ROWS_INSERTED: 207
          ROWS_UPDATED: 0
       SELECT_COMMANDS: 10
       UPDATE_COMMANDS: 0
        OTHER_COMMANDS: 13
   COMMIT_TRANSACTIONS: 0
 ROLLBACK_TRANSACTIONS: 0
    DENIED_CONNECTIONS: 0
      LOST_CONNECTIONS: 0
         ACCESS_DENIED: 0
         EMPTY_QUERIES: 1
```
