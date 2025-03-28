# SET SQL_LOG_BIN

#

# Syntax

```
SET [SESSION] sql_log_bin = {0|1}
```

#

# Description

Sets the [sql_log_bin](../../../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md#sql_log_bin) system variable, which disables or enables [binary logging](../../../../../server-usage/programming-customizing-mariadb/stored-routines/binary-logging-of-stored-routines.md) for the current connection, if the client has the `SUPER` [privilege](../../account-management-sql-commands/grant.md). The statement is refused with an error if the client does not have that privilege.

Note that setting `sql_log_bin=1` has no effect if [log_bin](../../../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md#log_bin) variable, which enables global binary logging, is not set.

Before [MariaDB 5.5](/en/what-is-mariadb-55/) and before MySQL 5.6 one could also set `sql_log_bin` as a global variable. This was disabled as this was too dangerous as it could damage replication.