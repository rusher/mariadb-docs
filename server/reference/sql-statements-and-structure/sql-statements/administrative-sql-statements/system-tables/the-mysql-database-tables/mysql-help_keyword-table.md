# mysql.help_keyword Table

`mysql.help_keyword` is one of the four tables used by the [HELP command](../../help-command.md). It is populated when the server is installed by the `fill_help_tables.sql` script. The other help tables are [help_relation](/en/mysqlhelp_relation-table/), [help_category](/en/mysqlhelp_category-table/) and [help_topic](/en/mysqlhelp_topic-table/).

This table uses the [Aria](../../../../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/aria-encryption/aria-enabling-encryption.md) storage engine. Prior to [MariaDB 10.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/what-is-mariadb-104) it used the [MyISAM](../../../../../../clients-and-utilities/myisam-clients-and-utilities/myisamchk-table-information.md) engine.

The `mysql.help_keyword` table contains the following fields:

| Field | Type | Null | Key | Default | Description |
| --- | --- | --- | --- | --- | --- |
| Field | Type | Null | Key | Default | Description |
| help_keyword_id | int(10) unsigned | NO | PRI | NULL | |
| name | char(64) | NO | UNI | NULL | |

#

# Example

```
SELECT * FROM help_keyword;
+-----------------+-------------------------------+
| help_keyword_id | name |
+-----------------+-------------------------------+
| 0 | JOIN |
| 1 | HOST |
| 2 | REPEAT |
| 3 | SERIALIZABLE |
| 4 | REPLACE |
| 5 | AT |
| 6 | SCHEDULE |
| 7 | RETURNS |
| 8 | STARTS |
| 9 | MASTER_SSL_CA |
| 10 | NCHAR |
| 11 | COLUMNS |
| 12 | COMPLETION |
...
```