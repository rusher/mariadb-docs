
# mysql.help_relation Table

`mysql.help_relation` is one of the four tables used by the [HELP command](../../help-command.md). It is populated when the server is installed by the `fill_help_tables.sql` script. The other help tables are [help_topic](mysql-help_topic-table.md), [help_category](mysql-help_category-table.md) and [help_keyword](mysql-help_keyword-table.md).


This table uses the [Aria](../../../../../storage-engines/aria/README.md) storage engine. Prior to [MariaDB 10.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/what-is-mariadb-104) it used the [MyISAM](../../../../../storage-engines/myisam-storage-engine/README.md) engine.


The `mysql.help_relation` table contains the following fields:



| Field | Type | Null | Key | Default | Description |
| --- | --- | --- | --- | --- | --- |
| Field | Type | Null | Key | Default | Description |
| help_topic_id | int(10) unsigned | NO | PRI | NULL |  |
| help_keyword_id | int(10) unsigned | NO | PRI | NULL |  |



## Example


```
...
|           106 |             456 |
|           463 |             456 |
|           468 |             456 |
|           463 |             457 |
|           194 |             458 |
|           478 |             458 |
|           374 |             459 |
|           459 |             459 |
|            39 |             460 |
|            58 |             460 |
|           185 |             460 |
|           264 |             460 |
|           269 |             460 |
|           209 |             461 |
|           468 |             461 |
|           201 |             462 |
|           468 |             463 |
+---------------+-----------------+
```


CC BY-SA / Gnu FDL

