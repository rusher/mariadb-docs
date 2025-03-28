# mysql.spider_xa_member Table

The `mysql.spider_xa_member` table is installed by the [Spider storage engine](../../../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/spider-status-variables.md).

In [MariaDB 10.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/what-is-mariadb-104) and later, this table uses the [Aria](../../../../../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/aria-encryption/aria-enabling-encryption.md) storage engine.

It contains the following fields:

| Field | Type | Null | Key | Default | Description |
| --- | --- | --- | --- | --- | --- |
| Field | Type | Null | Key | Default | Description |
| format_id | int(11) | NO | | 0 | |
| gtrid_length | int(11) | NO | | 0 | |
| bqual_length | int(11) | NO | | 0 | |
| data | binary(128) | NO | MUL | | |
| scheme | char(64) | NO | | | |
| host | char(64) | NO | | | |
| port | char(5) | NO | | | |
| socket | text | NO | | NULL | |
| username | char(64) | NO | | | |
| password | char(64) | NO | | | |
| ssl_ca | text | YES | | NULL | |
| ssl_capath | text | YES | | NULL | |
| ssl_cert | text | YES | | NULL | |
| ssl_cipher | char(64) | YES | | NULL | |
| ssl_key | text | YES | | NULL | |
| ssl_verify_server_cert | tinyint(4) | NO | | 0 | |
| default_file | text | YES | | NULL | |
| default_group | char(64) | YES | | NULL | |
| dsn | char(64) | YES | | NULL | |
| filedsn | text | YES | | NULL | |
| driver | char(64) | YES | | NULL | |