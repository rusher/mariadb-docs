
# mysql.spider_table_position_for_recovery Table

The `mysql.spider_table_position_for_recovery` table is installed by the [Spider storage engine](../../../../../../storage-engines/spider/spider-functions/spider_copy_tables.md).


This table uses the [Aria](../../../../../../storage-engines/s3-storage-engine/aria_s3_copy.md) storage engine.


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


