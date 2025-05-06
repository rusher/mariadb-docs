
# mysql.spider_table_position_for_recovery Table

The `mysql.spider_table_position_for_recovery` table is installed by the [Spider storage engine](../../../../../../storage-engines/spider/README.md).


This table uses the [Aria](../../../../../../storage-engines/aria/README.md) storage engine.


It contains the following fields:



| Field | Type | Null | Key | Default | Description |
| --- | --- | --- | --- | --- | --- |
| Field | Type | Null | Key | Default | Description |
| db_name | char(64) | NO | PRI |  |  |
| table_name | char(199) | NO | PRI |  |  |
| failed_link_id | int(11) | NO | PRI | 0 |  |
| source_link_id | int(11) | NO | PRI | 0 |  |
| file | text | YES |  | NULL |  |
| position | text | YES |  | NULL |  |
| gtid | text | YES |  | NULL |  |




CC BY-SA / Gnu FDL

