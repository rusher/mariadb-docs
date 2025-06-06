# mysql.spider\_table\_crd Table

The `mysql.spider_table_crd` table is installed by the [Spider storage engine](../../../../../storage-engines/spider/).

This table uses the [Aria](../../../../../storage-engines/aria/) storage engine.

It contains the following fields:

| Field       | Type             | Null | Key | Default | Description |
| ----------- | ---------------- | ---- | --- | ------- | ----------- |
| Field       | Type             | Null | Key | Default | Description |
| db\_name    | char(64)         | NO   | PRI |         |             |
| table\_name | char(199)        | NO   | PRI |         |             |
| key\_seq    | int(10) unsigned | NO   | PRI | 0       |             |
| cardinality | bigint(20)       | NO   |     | 0       |             |

CC BY-SA / Gnu FDL
