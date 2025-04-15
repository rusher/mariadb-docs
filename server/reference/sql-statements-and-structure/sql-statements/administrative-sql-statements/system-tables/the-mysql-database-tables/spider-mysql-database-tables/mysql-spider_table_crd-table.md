
# mysql.spider_table_crd Table

The `<code>mysql.spider_table_crd</code>` table is installed by the [Spider storage engine](../../../../../../storage-engines/spider/spider-functions/spider_copy_tables.md).


This table uses the [Aria](../../../../../../storage-engines/s3-storage-engine/aria_s3_copy.md) storage engine.


It contains the following fields:



| Field | Type | Null | Key | Default | Description |
| --- | --- | --- | --- | --- | --- |
| Field | Type | Null | Key | Default | Description |
| db_name | char(64) | NO | PRI |  |  |
| table_name | char(199) | NO | PRI |  |  |
| key_seq | int(10) unsigned | NO | PRI | 0 |  |
| cardinality | bigint(20) | NO |  | 0 |  |


