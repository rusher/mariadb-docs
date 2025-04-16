
# mysql.spider_table_sts Table

The `mysql.spider_table_sts` table is installed by the [Spider storage engine](../../../../../../storage-engines/spider/spider-functions/spider_copy_tables.md).


This table uses the [Aria](../../../../../../storage-engines/s3-storage-engine/aria_s3_copy.md) storage engine.


It contains the following fields:



| Field | Type | Null | Key | Default | Description |
| --- | --- | --- | --- | --- | --- |
| Field | Type | Null | Key | Default | Description |
| db_name | char(64) | NO | PRI |  |  |
| table_name | char(199) | NO | PRI |  |  |
| data_file_length | bigint(20) unsigned | NO |  | 0 |  |
| max_data_file_length | bigint(20) unsigned | NO |  | 0 |  |
| index_file_length | bigint(20) unsigned | NO |  | 0 |  |
| records | bigint(20) unsigned | NO |  | 0 |  |
| mean_rec_length | bigint(20) unsigned | NO |  | 0 |  |
| check_time | datetime | NO |  | 0000-00-00 00:00:00 |  |
| create_time | datetime | NO |  | 0000-00-00 00:00:00 |  |
| update_time | datetime | NO |  | 0000-00-00 00:00:00 |  |
| checksum | bigint(20) unsigned | YES |  | NULL |  |


