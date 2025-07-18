# mysqldump

mysqldump is used to dump a database or a collection of databases for backup or transfer to another database server.

From [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/what-is-mariadb-105), the client is called `mariadb-dump`. It can still be accessed under its original `mysqldump` name via a symlink in Linux, or an alternate binary in Windows.

**MariaDB starting with** [**11.0.1**](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-0-series/mariadb-11-0-1-release-notes)

From [MariaDB 11.0.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-0-series/mariadb-11-0-1-release-notes), `mysqldump` (the symlink) is deprecated and removed from the `mariadb` Docker Official Image. Use [mariadb-dump](../backup-restore-and-import-clients/mariadb-dump.md) instead.

See [mariadb-dump](../backup-restore-and-import-clients/mariadb-dump.md) for details.

<sub>_This page is licensed: GPLv2_</sub>

{% @marketo/form formId="4316" %}
