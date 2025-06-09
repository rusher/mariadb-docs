# mysql.ndb\_binlog\_index Table

The `mysql.ndb_binlog_index` table is not used by MariaDB. It was kept for MySQL compatibility reasons, and is used there for MySQL Cluster. It was removed in [MariaDB 10.0.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/mariadb-1004-release-notes).

For MariaDB clustering, see [Galera](../../../../../../../kb/en/galera/).

The table contains the following fields:

| Field     | Type                | Null | Key | Default |
| --------- | ------------------- | ---- | --- | ------- |
| Field     | Type                | Null | Key | Default |
| Position  | bigint(20) unsigned | NO   |     | NULL    |
| File      | varchar(255)        | NO   |     | NULL    |
| epoch     | bigint(20) unsigned | NO   | PRI | NULL    |
| inserts   | bigint(20) unsigned | NO   |     | NULL    |
| updates   | bigint(20) unsigned | NO   |     | NULL    |
| deletes   | bigint(20) unsigned | NO   |     | NULL    |
| schemaops | bigint(20) unsigned | NO   |     | NULL    |

CC BY-SA / Gnu FDL

{% @marketo/form formId="4316" %}
