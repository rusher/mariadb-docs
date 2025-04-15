
# mysql.help_relation Table

`<code>mysql.help_relation</code>` is one of the four tables used by the [HELP command](../../help-command.md). It is populated when the server is installed by the `<code>fill_help_tables.sql</code>` script. The other help tables are [help_topic](mysql-help_topic-table.md), [help_category](mysql-help_category-table.md) and [help_keyword](mysql-help_keyword-table.md).


This table uses the [Aria](../../../../../storage-engines/s3-storage-engine/aria_s3_copy.md) storage engine. Prior to [MariaDB 10.4](../../../../../../../release-notes/mariadb-community-server/what-is-mariadb-104.md) it used the [MyISAM](../../../../../storage-engines/myisam-storage-engine/myisam-system-variables.md) engine.


The `<code>mysql.help_relation</code>` table contains the following fields:



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
