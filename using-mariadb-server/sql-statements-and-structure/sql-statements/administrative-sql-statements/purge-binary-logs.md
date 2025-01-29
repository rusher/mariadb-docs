# PURGE BINARY LOGS

### Syntax <a href="#syntax" id="syntax"></a>

```
PURGE { BINARY | MASTER } LOGS
    { TO 'log_name' | BEFORE datetime_expr }
```

### Description <a href="#description" id="description"></a>

The `PURGE BINARY LOGS` statement deletes all the [binary log](https://mariadb.com/kb/en/binary-log/) files listed in the log index file prior to the specified log file name or date. `BINARY` and `MASTER` are synonyms. Deleted log files also are removed from the list recorded in the index file, so that the given log file becomes the first in the list.

The datetime expression is in the format 'YYYY-MM-DD hh:mm:ss'.

{% hint style="info" %}
If a replica is active but has yet to read from a binary log file you attempt to delete, the statement will fail with an error. However, if the replica is not connected and has yet to read from a log file you delete, the file will be deleted, but the replica will be unable to continue replicating once it connects again.
{% endhint %}

This statement has no effect if the server was not started with the [--log-bin](https://mariadb.com/kb/en/replication-and-binary-log-system-variables/#log_bin) option to enable binary logging.

To list the binary log files on the server, use [SHOW BINARY LOGS](https://mariadb.com/kb/en/show-binary-logs/). To see which files they are reading, use [SHOW SLAVE STATUS](https://mariadb.com/kb/en/show-slave-status/) (or [SHOW REPLICA STATUS](https://mariadb.com/kb/en/show-replica-status/) from [MariaDB 10.5.1](https://mariadb.com/kb/en/mariadb-1051-release-notes/)). You can only delete the files that are older than the oldest file that is used by the slaves.

To delete all binary log files, use [RESET MASTER](https://mariadb.com/kb/en/reset-master/). To move to a new log file (for example if you want to remove the current log file), use [FLUSH LOGS](https://mariadb.com/kb/en/flush/) before you execute `PURGE LOGS`.

If the [expire\_logs\_days](https://mariadb.com/kb/en/server-system-variables/#expire_logs_days) server system variable is not set to 0, the server automatically deletes binary log files after the given number of days. From [MariaDB 10.6](https://mariadb.com/kb/en/what-is-mariadb-106/), the [binlog\_expire\_logs\_seconds](https://mariadb.com/kb/en/replication-and-binary-log-system-variables/#binlog_expire_logs_seconds) variable allows more precise control over binlog deletion, and takes precedence if both are non-zero.

Requires the [SUPER](https://mariadb.com/kb/en/purge-binary-logs/super) privilege or, from [MariaDB 10.5.2](https://mariadb.com/kb/en/mariadb-1052-release-notes/), the [BINLOG ADMIN](https://mariadb.com/kb/en/grant/#binlog-admin) privilege, to run.

### Examples <a href="#examples" id="examples"></a>

```
PURGE BINARY LOGS TO 'mariadb-bin.000063';
```

```
PURGE BINARY LOGS BEFORE '2013-04-21';
```

```
PURGE BINARY LOGS BEFORE '2013-04-22 09:55:22';
```

### See Also <a href="#see-also" id="see-also"></a>

* [Using and Maintaining the Binary Log](https://mariadb.com/kb/en/using-and-maintaining-the-binary-log/)
* [FLUSH LOGS](https://mariadb.com/kb/en/flush/).
