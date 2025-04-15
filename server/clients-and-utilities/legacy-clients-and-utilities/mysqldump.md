
# mysqldump

mysqldump is used to dump a database or a collection of databases for backup or transfer to another database server.


From [MariaDB 10.5](../../../release-notes/mariadb-community-server/what-is-mariadb-105.md), the client is called `<code>mariadb-dump</code>`. It can still be accessed under its original `<code>mysqldump</code>` name via a symlink in Linux, or an alternate binary in Windows.



##### MariaDB starting with [11.0.1](../../../release-notes/mariadb-community-server/release-notes-mariadb-11-0-series/mariadb-11-0-1-release-notes.md)
From [MariaDB 11.0.1](../../../release-notes/mariadb-community-server/release-notes-mariadb-11-0-series/mariadb-11-0-1-release-notes.md), `<code>mysqldump</code>` (the symlink) is deprecated and removed from the `<code>mariadb</code>` Docker Official Image. Use `<code>[mariadb-dump](../backup-restore-and-import-clients/mariadb-dump.md)</code>` instead.


See [mariadb-dump](../backup-restore-and-import-clients/mariadb-dump.md) for details.

