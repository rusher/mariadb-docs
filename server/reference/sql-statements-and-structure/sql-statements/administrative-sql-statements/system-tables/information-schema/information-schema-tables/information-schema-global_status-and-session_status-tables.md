
# Information Schema GLOBAL_STATUS and SESSION_STATUS Tables

The [Information Schema](../../../../../../mariadb-internals/information-schema-plugins-show-and-flush-statements.md) `<code>GLOBAL_STATUS</code>` and `<code>SESSION_STATUS</code>` tables store a record of all [status variables](../../../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-status-variables.md) and their global and session values respectively. This is the same information as displayed by the `<code>[SHOW STATUS](../../../show/show-status.md)</code>` commands `<code>SHOW GLOBAL STATUS</code>` and `<code>SHOW SESSION STATUS</code>`.


They contain the following columns:



| Column | Description |
| --- | --- |
| Column | Description |
| VARIABLE_NAME | Status variable name. |
| VARIABLE_VALUE | Global or session value. |



## Example


```
SELECT * FROM information_schema.GLOBAL_STATUS;
+-----------------------------------------------+--------------------+
| VARIABLE_NAME                                 | VARIABLE_VALUE     |
+-----------------------------------------------+--------------------+
...
| BINLOG_SNAPSHOT_FILE                          | mariadb-bin.000208 |
| BINLOG_SNAPSHOT_POSITION                      | 369                |
...
| THREADS_CONNECTED                             | 1                  |
| THREADS_CREATED                               | 1                  |
| THREADS_RUNNING                               | 1                  |
| UPTIME                                        | 57358              |
| UPTIME_SINCE_FLUSH_STATUS                     | 57358              |
+-----------------------------------------------+--------------------+
```
