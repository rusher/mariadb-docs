# mysql.help_relation Table

`mysql.help_relation` is one of the four tables used by the [HELP command](../../help-command.md). It is populated when the server is installed by the `fill_help_tables.sql` script. The other help tables are [help_topic](/en/mysqlhelp_topic-table/), [help_category](/en/mysqlhelp_category-table/) and [help_keyword](/en/mysqlhelp_keyword-table/).

This table uses the [Aria](../../../../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/aria-encryption/aria-enabling-encryption.md) storage engine. Prior to [MariaDB 10.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/what-is-mariadb-104) it used the [MyISAM](../../../../../../clients-and-utilities/myisam-clients-and-utilities/myisamchk-table-information.md) engine.

The `mysql.help_relation` table contains the following fields:

| Field | Type | Null | Key | Default | Description |
| --- | --- | --- | --- | --- | --- |
| Field | Type | Null | Key | Default | Description |
| help_topic_id | int(10) unsigned | NO | PRI | NULL | |
| help_keyword_id | int(10) unsigned | NO | PRI | NULL | |

#

# Example

```
...
| 106 | 456 |
| 463 | 456 |
| 468 | 456 |
| 463 | 457 |
| 194 | 458 |
| 478 | 458 |
| 374 | 459 |
| 459 | 459 |
| 39 | 460 |
| 58 | 460 |
| 185 | 460 |
| 264 | 460 |
| 269 | 460 |
| 209 | 461 |
| 468 | 461 |
| 201 | 462 |
| 468 | 463 |
+---------------+-----------------+
```