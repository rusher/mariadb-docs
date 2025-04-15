
# SHOW PROCESSLIST

## Syntax


```
SHOW [FULL] PROCESSLIST
```

## Description


`<code class="highlight fixed" style="white-space:pre-wrap">SHOW PROCESSLIST</code>` shows you which threads are running. You
can also get this information from the
[information_schema.PROCESSLIST](../system-tables/information-schema/information-schema-tables/information-schema-processlist-table.md) table or the [mariadb-admin processlist](../../../../../clients-and-utilities/mariadb-admin.md) command. If you have the 
`<code class="highlight fixed" style="white-space:pre-wrap">[PROCESS privilege](show-privileges.md)</code>`, you can see all threads.
Otherwise, you can see only your own threads (that is, threads associated with
the MariaDB account that you are using). If you do not use the
`<code class="highlight fixed" style="white-space:pre-wrap">FULL</code>` keyword, only the first 100 characters of each
statement are shown in the Info field.


The columns shown in `<code>SHOW PROCESSLIST</code>` are:



| Name | Description |
| --- | --- |
| Name | Description |
| ID | The client's process ID. |
| USER | The username associated with the process. |
| HOST | The host the client is connected to. |
| DB | The default database of the process (NULL if no default). |
| COMMAND | The command type. See [Thread Command Values](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/buffers-caches-and-threads/thread-command-values.md). |
| TIME | The amount of time, in seconds, the process has been in its current state. For a replica SQL thread before [MariaDB 10.1](../../../../../../release-notes/mariadb-community-server/what-is-mariadb-1010.md), this is the time in seconds between the last replicated event's timestamp and the replica machine's real time. |
| STATE | See [Thread States](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/buffers-caches-and-threads/thread-states/README.md). |
| INFO | The statement being executed. |
| PROGRESS | The total progress of the process (0-100%) (see [Progress Reporting](../../../../mariadb-internals/using-mariadb-with-your-programs-api/progress-reporting.md)). |



The [information_schema.PROCESSLIST](../system-tables/information-schema/information-schema-tables/information-schema-processlist-table.md) table contains a number of additional columns. See `<code>TIME_MS</code>` column in [information_schema.PROCESSLIST](../system-tables/information-schema/time_ms-column-in-information_schemaprocesslist.md) for differences in the `<code>TIME</code>` column between MariaDB and MySQL.


Note that the `<code>PROGRESS</code>` field from the information schema, and the `<code>PROGRESS</code>` field from `<code>SHOW PROCESSLIST</code>` display different results. `<code>SHOW PROCESSLIST</code>` shows the total progress, while the information schema shows the progress for the current stage only.


Threads can be killed using their thread_id or their query_id, with the [KILL](../kill.md) statement.


Since queries on this table are locking, if the [performance_schema](../system-tables/performance-schema/performance-schema-tables/performance-schema-table_handles-table.md) is enabled, you may want to query the [THREADS](../system-tables/performance-schema/performance-schema-tables/performance-schema-threads-table.md) table instead.


## Examples


```
SHOW PROCESSLIST;
+----+-----------------+-----------+------+---------+------+------------------------+------------------+----------+
| Id | User            | Host      | db   | Command | Time | State                  | Info             | Progress |
+----+-----------------+-----------+------+---------+------+------------------------+------------------+----------+
|  2 | event_scheduler | localhost | NULL | Daemon  | 2693 | Waiting on empty queue | NULL             |    0.000 |
|  4 | root            | localhost | NULL | Query   |    0 | Table lock             | SHOW PROCESSLIST |    0.000 |
+----+-----------------+-----------+------+---------+------+------------------------+------------------+----------+
```

## See Also


[CONNECTION_ID()](../../built-in-functions/secondary-functions/information-functions/connection_id.md)

