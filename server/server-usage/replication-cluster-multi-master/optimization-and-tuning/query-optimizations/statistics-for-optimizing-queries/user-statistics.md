
# User Statistics

The User Statistics (userstat) plugin creates the [USER_STATISTICS](../../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-user_statistics-table.md), [CLIENT_STATISTICS](../../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-client_statistics-table.md), the [INDEX_STATISTICS](../../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-index_statistics-table.md), and the [TABLE_STATISTICS](../../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-table_statistics-table.md) tables in the [INFORMATION_SCHEMA](../../../../../reference/mariadb-internals/information-schema-plugins-show-and-flush-statements.md) database. As an alternative to these tables, the plugin also adds the [SHOW USER_STATISTICS](../../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-user-statistics.md), the [SHOW CLIENT_STATISTICS](../../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-client-statistics.md), the [SHOW INDEX_STATISTICS](../../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-index-statistics.md), and the [SHOW TABLE_STATISTICS](../../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-table-statistics.md) statements.


These tables and commands can be used to understand the server activity better and to identify the sources of your database's load.


The plugin also adds the [FLUSH USER_STATISTICS](../../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/flush-commands/flush-tables-for-export.md), [FLUSH CLIENT_STATISTICS](../../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/flush-commands/flush-tables-for-export.md), [FLUSH INDEX_STATISTICS](../../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/flush-commands/flush-tables-for-export.md), and [FLUSH TABLE_STATISTICS](../../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/flush-commands/flush-tables-for-export.md) statements.


The MariaDB implementation of this plugin is based on the [userstatv2 patch](https://www.percona.com/docs/wiki/patches:userstatv2) from Percona and Ourdelta. The original code comes from Google (Mark Callaghan's team) with additional work from Percona, Ourdelta, and Weldon Whipple. The MariaDB implementation provides the same functionality as the userstatv2 patch but a lot of changes have been made to make it faster and to better fit the MariaDB infrastructure.



## How it Works


The `<code>userstat</code>` plugin works by keeping several hash tables in memory. All variables are incremented while the query is running. At the end of each statement the global values are updated.


## Enabling the Plugin


By default statistics are not collected. This is to ensure that statistics collection does not cause any extra load on the server unless desired.


Set the [userstat=ON](#userstat) system variable in a relevant server [option group](../../../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md) to enable the plugin. For example:


```
[mariadb]
...
userstat = 1
```

The value can also be changed dynamically. For example:


```
SET GLOBAL userstat=1;
```

## Using the Plugin


### Using the Information Schema Table


The `<code>userstat</code>` plugin creates the [USER_STATISTICS](../../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-user_statistics-table.md), [CLIENT_STATISTICS](../../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-client_statistics-table.md), the [INDEX_STATISTICS](../../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-index_statistics-table.md), and the [TABLE_STATISTICS](../../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-table_statistics-table.md) tables in the [INFORMATION_SCHEMA](../../../../../reference/mariadb-internals/information-schema-plugins-show-and-flush-statements.md) database.


```
SELECT * FROM INFORMATION_SCHEMA.USER_STATISTICS\G
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

```
SELECT * FROM INFORMATION_SCHEMA.CLIENT_STATISTICS\G
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
1 row in set (0.00 sec)
```

```
SELECT * FROM INFORMATION_SCHEMA.INDEX_STATISTICS WHERE TABLE_NAME = "author";
+--------------+------------+------------+-----------+
| TABLE_SCHEMA | TABLE_NAME | INDEX_NAME | ROWS_READ |
+--------------+------------+------------+-----------+
| books        | author     | by_name    |        15 |
+--------------+------------+------------+-----------+
```

```
SELECT * FROM INFORMATION_SCHEMA.TABLE_STATISTICS WHERE TABLE_NAME='user';
+--------------+------------+-----------+--------------+------------------------+
| TABLE_SCHEMA | TABLE_NAME | ROWS_READ | ROWS_CHANGED | ROWS_CHANGED_X_INDEXES |
+--------------+------------+-----------+--------------+------------------------+
| mysql        | user       |         5 |            2 |                      2 |
+--------------+------------+-----------+--------------+------------------------+
```

### Using the SHOW Statements


As an alternative to the [INFORMATION_SCHEMA](../../../../../reference/mariadb-internals/information-schema-plugins-show-and-flush-statements.md) tables, the `<code>userstat</code>` plugin also adds the [SHOW USER_STATISTICS](../../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-user-statistics.md), the [SHOW CLIENT_STATISTICS](../../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-client-statistics.md), the [SHOW INDEX_STATISTICS](../../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-index-statistics.md), and the [SHOW TABLE_STATISTICS](../../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-table-statistics.md) statements.


These commands are another way to display the information stored in the information schema tables. WHERE clauses are accepted. LIKE clauses are accepted but ignored.


```
SHOW USER_STATISTICS
SHOW CLIENT_STATISTICS
SHOW INDEX_STATISTICS
SHOW TABLE_STATISTICS
```

### Flushing Plugin Data


The `<code>userstat</code>` plugin also adds the [FLUSH USER_STATISTICS](../../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/flush-commands/flush-tables-for-export.md), [FLUSH CLIENT_STATISTICS](../../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/flush-commands/flush-tables-for-export.md), [FLUSH INDEX_STATISTICS](../../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/flush-commands/flush-tables-for-export.md), and [FLUSH TABLE_STATISTICS](../../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/flush-commands/flush-tables-for-export.md) statements, which discard the information stored in the specified information schema table.


```
FLUSH USER_STATISTICS
FLUSH CLIENT_STATISTICS
FLUSH INDEX_STATISTICS
FLUSH TABLE_STATISTICS
```

## Versions


### USER_STATISTICS



| Version | Status | Introduced |
| --- | --- | --- |
| Version | Status | Introduced |
| 2.0 | Stable | [MariaDB 10.1.18](../../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10118-release-notes.md) |
| 2.0 | Gamma | [MariaDB 10.1.1](../../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-1-release-notes.md) |



### CLIENT_STATISTICS



| Version | Status | Introduced |
| --- | --- | --- |
| Version | Status | Introduced |
| 2.0 | Stable | [MariaDB 10.1.13](../../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10113-release-notes.md) |
| 2.0 | Gamma | [MariaDB 10.1.1](../../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-1-release-notes.md) |



### INDEX_STATISTICS



| Version | Status | Introduced |
| --- | --- | --- |
| Version | Status | Introduced |
| 2.0 | Stable | [MariaDB 10.1.13](../../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10113-release-notes.md) |
| 2.0 | Gamma | [MariaDB 10.1.1](../../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-1-release-notes.md) |



### TABLE_STATISTICS



| Version | Status | Introduced |
| --- | --- | --- |
| Version | Status | Introduced |
| 2.0 | Stable | [MariaDB 10.1.18](../../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10118-release-notes.md) |
| 2.0 | Gamma | [MariaDB 10.1.1](../../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-1-release-notes.md) |



## System Variables


### `<code>userstat</code>`


* Description: If set to `<code>1</code>`, user statistics will be activated.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--userstat=1</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`



## Status Variables


User Statistics introduced a number of new status variables:


* [access_denied_errors](../../system-variables/server-status-variables.md#access_denied_errors)
* [binlog_bytes_written](../../system-variables/server-status-variables.md#binlog_bytes_written)
* [busy_time](../../system-variables/server-status-variables.md#busy_time) (requires [userstat](#userstat) to be set to be recorded)
* [cpu_time](../../system-variables/server-status-variables.md#cpu_time) (requires [userstat](#userstat) to be set to be recorded)
* [empty_queries](../../system-variables/server-status-variables.md#empty_queries)
* [rows_read](../../system-variables/server-status-variables.md#rows_read)
* [rows_sent](../../system-variables/server-status-variables.md#rows_sent)

