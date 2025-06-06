# SHOW CLIENT\_STATISTICS

## Syntax

```
SHOW CLIENT_STATISTICS
```

## Description

The `SHOW CLIENT_STATISTICS` statement is part of the [User Statistics](../../../../ha-and-performance/optimization-and-tuning/query-optimizations/statistics-for-optimizing-queries/user-statistics.md) feature. It was removed as a separate statement in [MariaDB 10.1.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-1-release-notes), but effectively replaced by the generic [SHOW information\_schema\_table](../../../mariadb-internals/information-schema-plugins-show-and-flush-statements.md) statement. The [information\_schema.CLIENT\_STATISTICS](../system-tables/information-schema/information-schema-tables/information-schema-client_statistics-table.md) table holds statistics about client connections.

The [userstat](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#userstat) system variable must be set to 1 to activate this feature. See the [User Statistics](../../../../ha-and-performance/optimization-and-tuning/query-optimizations/statistics-for-optimizing-queries/user-statistics.md) and [information\_schema.CLIENT\_STATISTICS](../system-tables/information-schema/information-schema-tables/information-schema-client_statistics-table.md) articles for more information.

## Example

```
SHOW CLIENT_STATISTICS\G
*************************** 1. row ***************************
                Client: localhost
     Total_connections: 35
Concurrent_connections: 0
        Connected_time: 708
             Busy_time: 2.5557979999999985
              Cpu_time: 0.04123740000000002
        Bytes_received: 3883
            Bytes_sent: 21595
  Binlog_bytes_written: 0
             Rows_read: 18
             Rows_sent: 115
          Rows_deleted: 0
         Rows_inserted: 0
          Rows_updated: 0
       Select_commands: 70
       Update_commands: 0
        Other_commands: 0
   Commit_transactions: 1
 Rollback_transactions: 0
    Denied_connections: 0
      Lost_connections: 0
         Access_denied: 0
         Empty_queries: 35
```

CC BY-SA / Gnu FDL
