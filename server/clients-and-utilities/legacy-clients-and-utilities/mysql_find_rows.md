# mysql_find_rows

`mysql_find_rows` reads files containing SQL statements and extracts statements that match a given regular expression or that contain [USE db_name](../../security/user-account-management/user-password-expiry.md) or [SET](../../server-usage/replication-cluster-multi-master/standard-replication/setting-up-replication.md) statements.

From [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/what-is-mariadb-105), the client is called `mariadb-find-rows`. It can still be accessed under its original `mysql_find_rows` name via a symlink in Linux, or an alternate binary in Windows.

See [mariadb-find-rows](../mariadb-find-rows.md) for details.