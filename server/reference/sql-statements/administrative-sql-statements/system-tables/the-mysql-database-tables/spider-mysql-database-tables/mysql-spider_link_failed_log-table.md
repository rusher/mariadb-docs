# mysql.spider\_link\_failed\_log Table

The `mysql.spider_link_failed_log` table is installed by the [Spider storage engine](../../../../../storage-engines/spider/).

This table uses the [Aria](../../../../../storage-engines/aria/) storage engine.

It contains the following fields:

| Field        | Type      | Null | Key | Default              | Description |
| ------------ | --------- | ---- | --- | -------------------- | ----------- |
| Field        | Type      | Null | Key | Default              | Description |
| db\_name     | char(64)  | NO   |     |                      |             |
| table\_name  | char(199) | NO   |     |                      |             |
| link\_id     | char(64)  | NO   |     |                      |             |
| failed\_time | timestamp | NO   |     | current\_timestamp() |             |

CC BY-SA / Gnu FDL
