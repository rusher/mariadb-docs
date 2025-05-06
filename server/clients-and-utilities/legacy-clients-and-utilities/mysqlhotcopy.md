
# mysqlhotcopy

mysqlhotcopy is deprecated and may be removed in a future release.


`mysqlhotcopy` uses [FLUSH TABLES](../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/flush-commands/flush.md), [LOCK TABLES](../../reference/sql-statements-and-structure/sql-statements/transactions/lock-tables.md), and cp or scp to make a database backup.


From [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-5-series/what-is-mariadb-105), the client is called `mariadb-hotcopy`. It can still be accessed under its original `mysqlhotcopy` name via a symlink in Linux, or an alternate binary in Windows.


See [mariadb-hotcopy](../backup-restore-and-import-clients/mariadb-hotcopy.md) for details.


GPLv2

