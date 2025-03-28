# mysqlbinlog

`mysqlbinlog` was a utility included with MariaDB for processing [binary log](../../server-usage/programming-customizing-mariadb/stored-routines/binary-logging-of-stored-routines.md) and [relay log](../../server-management/server-monitoring-logs/binary-log/relay-log.md) files.

From [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/what-is-mariadb-105), the client is called `mariadb-binlog`. It can still be accessed under its original `mysqladmin` name via a symlink in Linux, or an alternate binary in Windows.

See [mariadb-binlog](mariadb-binlog-options.md) for details.