
# mysql.spider_xa Table

The `<code>mysql.spider_xa</code>` table is installed by the [Spider storage engine](../../../../../../storage-engines/spider/spider-functions/spider_copy_tables.md).


This table uses the [Aria](../../../../../../storage-engines/s3-storage-engine/aria_s3_copy.md) storage engine.


It contains the following fields:



| Field | Type | Null | Key | Default | Description |
| --- | --- | --- | --- | --- | --- |
| Field | Type | Null | Key | Default | Description |
| format_id | int(11) | NO | PRI | 0 |  |
| gtrid_length | int(11) | NO | PRI | 0 |  |
| bqual_length | int(11) | NO |  | 0 |  |
| data | binary(128) | NO | PRI |  |  |
| status | char(8) | NO | MUL |  |  |


