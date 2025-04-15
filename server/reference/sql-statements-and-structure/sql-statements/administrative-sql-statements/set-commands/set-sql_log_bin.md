
# SET SQL_LOG_BIN

## Syntax


```
SET [SESSION] sql_log_bin = {0|1}
```

## Description


Sets the [sql_log_bin](../../../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md#sql_log_bin) system variable, which disables or enables [binary logging](../../../../storage-engines/innodb/binary-log-group-commit-and-innodb-flushing-performance.md) for the current connection, if the client has the `<code class="highlight fixed" style="white-space:pre-wrap">SUPER</code>` [privilege](../../account-management-sql-commands/grant.md). The statement is refused with an error if the client does not have that privilege.


Note that setting `<code>sql_log_bin=1</code>` has no effect if [log_bin](../../../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md#log_bin) variable, which enables global binary logging, is not set.


Before [MariaDB 5.5](../../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5.md) and before MySQL 5.6 one could also set `<code>sql_log_bin</code>` as a global variable. This was disabled as this was too dangerous as it could damage replication.

