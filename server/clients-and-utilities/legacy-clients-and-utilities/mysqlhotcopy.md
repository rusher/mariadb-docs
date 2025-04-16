
# mysqlhotcopy

mysqlhotcopy is deprecated and may be removed in a future release.


`mysqlhotcopy` uses [FLUSH TABLES](../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/flush-commands/flush-tables-for-export.md), [LOCK TABLES](../../reference/sql-statements-and-structure/sql-statements/transactions/lock-tables.md), and cp or scp to make a database backup.


From [MariaDB 10.5](../../../release-notes/mariadb-community-server/what-is-mariadb-105.md), the client is called `mariadb-hotcopy`. It can still be accessed under its original `mysqlhotcopy` name via a symlink in Linux, or an alternate binary in Windows.


See [mariadb-hotcopy](../backup-restore-and-import-clients/mariadb-hotcopy.md) for details.

