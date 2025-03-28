# RESET

#

# Syntax

```
RESET reset_option [, reset_option] ...
```

#

# Description

The `RESET` statement is used to clear the state of various server
operations. You must have the `[RELOAD privilege](../account-management-sql-commands/grant.md)` to execute
`RESET`.

`RESET` acts as a stronger version of the [FLUSH](flush-commands/flush-tables-for-export.md) statement.

The different `RESET` options are:

| Option | Description |
| --- | --- |
| Option | Description |
| [SLAVE ["connection_name"] [ALL](/kb/en/reset-slave/)] | Deletes all [relay logs](../../../../server-management/server-monitoring-logs/binary-log/relay-log.md) from the slave and reset the replication position in the master [binary log](../../../../server-usage/programming-customizing-mariadb/stored-routines/binary-logging-of-stored-routines.md). |
| [MASTER](replication-commands/reset-master.md) | Deletes all old binary logs, makes the binary index file ([--log-bin-index](/kb/en/mysqld-options-full-list/)) empty and creates a new binary log file. This is useful when you want to reset the master to an initial state. If you want to just delete old, not used binary logs, you should use the [PURGE BINARY LOGS](/kb/en/sql-commands-purge-logs/) command. |
| QUERY CACHE | Removes all queries from [the query cache](/kb/en/the-query-cache/). See also [FLUSH QUERY CACHE](flush-commands/flush-query-cache.md). |