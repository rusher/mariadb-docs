
# RESET

## Syntax


```
RESET reset_option [, reset_option] ...
```

## Description


The `<code>RESET</code>` statement is used to clear the state of various server
operations. You must have the `<code>[RELOAD privilege](../account-management-sql-commands/grant.md)</code>` to execute
`<code>RESET</code>`.


`<code>RESET</code>` acts as a stronger version of the [FLUSH](flush-commands/flush-tables-for-export.md) statement.


The different `<code>RESET</code>` options are:



| Option | Description |
| --- | --- |
| Option | Description |
| [SLAVE ["connection_name"] [ALL](replication-statements/reset-replica.md)] | Deletes all [relay logs](../../../../server-management/server-monitoring-logs/binary-log/relay-log.md) from the slave and reset the replication position in the master [binary log](../../../storage-engines/innodb/binary-log-group-commit-and-innodb-flushing-performance.md). |
| [MASTER](replication-statements/reset-master.md) | Deletes all old binary logs, makes the binary index file ([--log-bin-index](../../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md)) empty and creates a new binary log file. This is useful when you want to reset the master to an initial state. If you want to just delete old, not used binary logs, you should use the [PURGE BINARY LOGS](purge-binary-logs.md) command. |
| QUERY CACHE | Removes all queries from [the query cache](../../../plugins/other-plugins/query-cache-information-plugin.md). See also [FLUSH QUERY CACHE](flush-commands/flush-query-cache.md). |


