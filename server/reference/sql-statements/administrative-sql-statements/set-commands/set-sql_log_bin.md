# SET SQL\_LOG\_BIN

## Syntax

```
SET [SESSION] sql_log_bin = {0|1}
```

## Description

Sets the [sql\_log\_bin](../../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#sql_log_bin) system variable, which disables or enables [binary logging](../../../../server-management/server-monitoring-logs/binary-log/) for the current connection, if the client has the `SUPER` [privilege](../../account-management-sql-statements/grant.md). The statement is refused with an error if the client does not have that privilege.

Note that setting `sql_log_bin=1` has no effect if [log\_bin](../../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#log_bin) variable, which enables global binary logging, is not set.

Before [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5) and before MySQL 5.6 one could also set `sql_log_bin` as a global variable. This was disabled as this was too dangerous as it could damage replication.

GPLv2 fill\_help\_tables.sql

{% @marketo/form formId="4316" %}
