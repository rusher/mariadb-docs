
# mysql.help_keyword Table

`mysql.help_keyword` is one of the four tables used by the [HELP command](../../help-command.md). It is populated when the server is installed by the `fill_help_tables.sql` script. The other help tables are [help_relation](mysql-help_relation-table.md), [help_category](mysql-help_category-table.md) and [help_topic](mysql-help_topic-table.md).


This table uses the [Aria](../../../../../storage-engines/aria/README.md) storage engine. Prior to [MariaDB 10.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/old-releases/release-notes-mariadb-10-4-series/what-is-mariadb-104) it used the [MyISAM](../../../../../storage-engines/myisam-storage-engine/README.md) engine.


The `mysql.help_keyword` table contains the following fields:



| Field | Type | Null | Key | Default | Description |
| --- | --- | --- | --- | --- | --- |
| Field | Type | Null | Key | Default | Description |
| help_keyword_id | int(10) unsigned | NO | PRI | NULL |  |
| name | char(64) | NO | UNI | NULL |  |



## Example


```
SELECT * FROM help_keyword;
+-----------------+-------------------------------+
| help_keyword_id | name                          |
+-----------------+-------------------------------+
|               0 | JOIN                          |
|               1 | HOST                          |
|               2 | REPEAT                        |
|               3 | SERIALIZABLE                  |
|               4 | REPLACE                       |
|               5 | AT                            |
|               6 | SCHEDULE                      |
|               7 | RETURNS                       |
|               8 | STARTS                        |
|               9 | MASTER_SSL_CA                 |
|              10 | NCHAR                         |
|              11 | COLUMNS                       |
|              12 | COMPLETION                    |
...
```
