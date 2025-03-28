# mysqldump

mysqldump is used to dump a database or a collection of databases for backup or transfer to another database server.

From [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/what-is-mariadb-105), the client is called `mariadb-dump`. It can still be accessed under its original `mysqldump` name via a symlink in Linux, or an alternate binary in Windows.

#

#### MariaDB starting with [11.0.1](/kb/en/mariadb-1101-release-notes/)

From [MariaDB 11.0.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/release-notes-mariadb-11-0-series/mariadb-11-0-1-release-notes), `mysqldump` (the symlink) is deprecated and removed from the `mariadb` Docker Official Image. Use `[mariadb-dump](../mariadb-dumpslow.md)` instead.

See [mariadb-dump](../mariadb-dumpslow.md) for details.