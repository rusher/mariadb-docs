
# mysql.slow_log Table

**System tables should not normally be edited directly. Use the related SQL statements instead.**



The `<code>mysql.slow_log</code>` table stores the contents of the [Slow Query Log](../../../../../../server-management/server-monitoring-logs/slow-query-log/slow-query-log-overview.md) if slow logging is active and the output is being written to table (see [Writing logs into tables](../../../../../../server-management/server-monitoring-logs/writing-logs-into-tables.md)).


It contains the following fields:



| Field | Type | Null | Key | Default | Description |
| --- | --- | --- | --- | --- | --- |
| Field | Type | Null | Key | Default | Description |
| start_time | timestamp(6) | NO |  | CURRENT_TIMESTAMP(6) | Time the query began. |
| user_host | mediumtext | NO |  | NULL | User and host combination. |
| query_time | time(6) | NO |  | NULL | Total time the query took to execute. |
| lock_time | time(6) | NO |  | NULL | Total time the query was locked. |
| rows_sent | int(11) | NO |  | NULL | Number of rows sent. |
| rows_examined | int(11) | NO |  | NULL | Number of rows examined. |
| db | varchar(512) | NO |  | NULL | Default database. |
| last_insert_id | int(11) | NO |  | NULL | [last_insert_id](../../../built-in-functions/secondary-functions/information-functions/last_insert_id.md). |
| insert_id | int(11) | NO |  | NULL | Insert id. |
| server_id | int(10) unsigned | NO |  | NULL | The server's id. |
| sql_text | mediumtext | NO |  | NULL | Full query. |
| thread_id | bigint(21) unsigned | NO |  | NULL | Thread id. |
| rows_affected | int(11) | NO |  | NULL | Number of rows affected by an [UPDATE](../../../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/tools/buildbot/buildbot-setup/buildbot-setup-for-virtual-machines/buildbot-setup-for-virtual-machines-additional-steps/update-debian-4-mirrors-for-buildbot-vms.md) or [DELETE](../../../data-manipulation/changing-deleting-data/delete.md) (from [MariaDB 10.1.2](../../../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-2-release-notes.md)) |



## Example


```
SELECT * FROM mysql.slow_log\G
...
*************************** 2. row ***************************
    start_time: 2014-11-11 07:56:28.721519
     user_host: root[root] @ localhost []
    query_time: 00:00:12.000215
     lock_time: 00:00:00.000000
     rows_sent: 1
 rows_examined: 0
            db: test
last_insert_id: 0
     insert_id: 0
     server_id: 1
      sql_text: SELECT SLEEP(12)
     thread_id: 74
...
```
