
# Overview of MariaDB Logs

There are many variables in MariaDB that you can use to define what to log and when to log.


This article will give you an overview of the different logs and how to enable/disable logging to these.


Note that storage engines can have their logs too: for example, InnoDB keeps an [Undo Log](../../reference/storage-engines/innodb/innodb-undo-log.md) and a Redo Log which are used for rollback and crash recovery. However, this page only lists MariaDB server logs.


### [Error Log](error-log.md)


* Always enabled
* Usually a file in the data directory, but some distributions may move this to other locations.
* All critical errors are logged here.
* One can get warnings to be logged by setting [log_warnings](../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#log_warnings).
* With the [mysqld_safe](../../clients-and-utilities/legacy-clients-and-utilities/mariadbd_safe.md) `--syslog` option one can duplicate the messages to the system's syslog.


### [General Query Log](general-query-log.md)


* Enabled with [--general-log](../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#general_log)
* Logs all queries to a [file or table](../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#log_output).
* Useful for debugging or auditing queries.
* The super user can disable logging to it for a connection by setting [SQL_LOG_OFF](../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#sql_log_off) to 1.


### [Slow Query Log](slow-query-log/slow-query-log-overview.md)


* Enabled by starting mysqld with [--slow-query-log](../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#slow_query_log)
* Logs all queries to a [file or table](../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#log_output).
* Useful to find queries that causes performance problems.
* Logs all queries that takes more than [long_query_time](../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#long_query_time) to run.
* One can decide what to log with the options [--log-slow-admin-statements](../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#log_slow_admin_statements), [--log-slow-slave-statements](../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#log_slow_slave_statements), [log_slow_filter](../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#log_slow_filter) or [log_slow_rate_limit](../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#log_slow_rate_limit).
* One can change what is logged by setting [log_slow_verbosity](../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#log_slow_verbosity).
* One can disable it globally by setting [global.slow_query_log](../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#slow_query_log) to 0
* In 10.1 one can disable it for a connection by setting [local.slow_query_log](../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#slow_query_log) to 0.


### [Binary Log](binary-log/overview-of-the-binary-log.md)


* Enabled by starting mysqld with [--log-bin](../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md)
* Used on machines that are, or may become, replication masters.
* Required for point-in-time recovery.
* Binary log files are mainly used by replication and can also be used with [mariadb-binlog](../../../connectors/mariadb-connector-c/mariadb-binlogreplication-api-reference.md) to apply on a backup to get the database up to date.
* One can decide what to log with [--binlog-ignore-db=database_name](../getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md) or [--binlog-do-db=database_name](../getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md).
* The super user can disable logging for a connection by [setting SQL_LOG_BIN](../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/set-commands/set-sql_log_bin.md) to 0. However while this is 0, no changes done in this connection will be replicated to the slaves!
* For examples, see [Using and Maintaining the Binary Log](binary-log/using-and-maintaining-the-binary-log.md).


### Examples


If you know that your next query will be slow and you don't want to log it in the slow query log, do:


```
SET LOCAL SLOW_QUERY_LOG=0;
```

If you are a super user running a log batch job that you don't want to have logged (for example mariadb-dump), do:


```
SET LOCAL SQL_LOG_OFF=1, LOCAL SLOW_QUERY_LOG=0;
```

[mariadb-dump](../../clients-and-utilities/backup-restore-and-import-clients/mariadb-dump.md) (previously mysqldump) since [MariaDB 10.1](../../../release-notes/mariadb-community-server/what-is-mariadb-1010.md) will add this automatically to your dump file if you run it with the `--skip-log-queries` option.


## See Also


* [MariaDB audit plugin](../../reference/plugins/mariadb-audit-plugin/release-notes-mariadb-audit-plugin/mariadb-audit-plugin-113-release-notes.md)

<span></span>
