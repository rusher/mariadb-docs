# Information Schema PROCESSLIST Table

The [Information Schema](/en/information_schema/) `PROCESSLIST` table contains information about running threads.

Similar information can also be returned with the [SHOW [FULL] PROCESSLIST](../../../show/show-processlist.md) statement, or the [mariadb-admin processlist](../../../../../../../clients-and-utilities/mariadb-admin.md) command.

It contains the following columns:

| Column | Description |
| --- | --- |
| Column | Description |
| ID | Connection identifier. |
| USER | MariaDB User. |
| HOST | The hostname from which this thread is connected.For Unix socket connections, localhost. For TCP/IP connections, the TCP port is appended (e.g. 192.168.1.17:58061 or other-host.company.com:58061). For system user, this column is blank (''). |
| DB | Default database, or NULL if none. |
| COMMAND | Type of command running, corresponding to the Com_ [status variables](../../../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-status-variables.md). See [Thread Command Values](../../../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/buffers-caches-and-threads/thread-command-values.md). |
| TIME | Seconds that the thread has spent on the current COMMAND so far. |
| STATE | Current state of the thread. See [Thread States](/en/thread-states/). |
| INFO | Statement the thread is executing, or NULL if none. |
| TIME_MS | Time in milliseconds with microsecond precision that the thread has spent on the current COMMAND so far ([see more](../time_ms-column-in-information_schemaprocesslist.md)). |
| STAGE | The stage the process is currently in. |
| MAX_STAGE | The maximum number of stages. |
| PROGRESS | The progress of the process within the current stage (0-100%). |
| MEMORY_USED | Memory in bytes used by the thread. |
| MAX_MEMORY_USED | Maximum memory in bytes used by the thread. |
| EXAMINED_ROWS | Rows examined by the thread. Only updated by UPDATE, DELETE, and similar statements. For SELECT and other statements, the value remains zero. |
| SENT_ROWS | Number of rows sent by the statement being executed. From [MariaDB 11.3.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-0-release-notes). |
| QUERY_ID | Query ID. |
| INFO_BINARY | Binary data information |
| TID | Thread ID ([MDEV-6756](https://jira.mariadb.org/browse/MDEV-6756)) |
| TMP_SPACE_USED | See [Limiting Size of Created Disk Temporary Files and Tables Overview](../../../../../../../security/user-account-management/limiting-size-of-created-disk-temporary-files-and-tables/limiting-size-of-created-disk-temporary-files-and-tables-overview.md). From [MariaDB 11.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/what-is-mariadb-115). |

Note that as a difference to MySQL, in MariaDB the `TIME`
column (and also the `TIME_MS` column) are not affected by
any setting of `[@TIMESTAMP](../../../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#timestamp)`. This means that it can be
reliably used also for threads that change `@TIMESTAMP` (such
as the [replication](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/mariadb-releases/compatibility-differences/replication-compatibility-between-mariadb-and-mysql) SQL thread). See also [MySQL Bug #22047](http://bugs.mysql.com/bug.php?id=22047).

As a consequence of this, the `TIME` column of 
`SHOW FULL PROCESSLIST` and
`INFORMATION_SCHEMA.PROCESSLIST` can not be used to determine
if a slave is lagging behind. For this, use instead the
`Seconds_Behind_Master` column in the output of 
[SHOW SLAVE STATUS](/en/show-slave-status/).

Note that the `PROGRESS` field from the information schema, and the `PROGRESS` field from `SHOW PROCESSLIST` display different results. `SHOW PROCESSLIST` shows the total progress, while the information schema shows the progress for the current stage only.. To retrieve a similar "total" Progress value from `information_schema.PROCESSLIST` as the one from `SHOW PROCESSLIST`, use

```
SELECT CASE WHEN Max_Stage < 2 THEN Progress ELSE (Stage-1)/Max_Stage*100+Progress/Max_Stage END 
 AS Progress FROM INFORMATION_SCHEMA.PROCESSLIST;
```

#

# Example

```
SELECT * FROM INFORMATION_SCHEMA.PROCESSLIST\G
*************************** 1. row ***************************
 ID: 9
 USER: msandbox
 HOST: localhost
 DB: NULL
 COMMAND: Query
 TIME: 0
 STATE: Filling schema table
 INFO: SELECT * FROM INFORMATION_SCHEMA.PROCESSLIST
 TIME_MS: 0.351
 STAGE: 0
 MAX_STAGE: 0
 PROGRESS: 0.000
 MEMORY_USED: 85392
EXAMINED_ROWS: 0
 QUERY_ID: 15
 INFO_BINARY: SELECT * FROM INFORMATION_SCHEMA.PROCESSLIST
 TID: 11838
*************************** 2. row ***************************
 ID: 5
 USER: system user
 HOST: 
 DB: NULL
 COMMAND: Daemon
 TIME: 0
 STATE: InnoDB shutdown handler
 INFO: NULL
 TIME_MS: 0.000
 STAGE: 0
 MAX_STAGE: 0
 PROGRESS: 0.000
 MEMORY_USED: 24160
EXAMINED_ROWS: 0
 QUERY_ID: 0
 INFO_BINARY: NULL
 TID: 3856
...
```

#

# See Also

* [TIME_MS column in Information Schema SHOW PROCESSLIST](../time_ms-column-in-information_schemaprocesslist.md)