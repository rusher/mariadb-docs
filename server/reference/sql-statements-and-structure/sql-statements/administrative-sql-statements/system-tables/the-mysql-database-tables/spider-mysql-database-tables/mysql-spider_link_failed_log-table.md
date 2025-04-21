
# mysql.spider_link_failed_log Table

The `mysql.spider_link_failed_log` table is installed by the [Spider storage engine](../../../../../../storage-engines/spider/README.md).


This table uses the [Aria](../../../../../../storage-engines/aria/README.md) storage engine.


It contains the following fields:



| Field | Type | Null | Key | Default | Description |
| --- | --- | --- | --- | --- | --- |
| Field | Type | Null | Key | Default | Description |
| db_name | char(64) | NO |  |  |  |
| table_name | char(199) | NO |  |  |  |
| link_id | char(64) | NO |  |  |  |
| failed_time | timestamp | NO |  | current_timestamp() |  |


