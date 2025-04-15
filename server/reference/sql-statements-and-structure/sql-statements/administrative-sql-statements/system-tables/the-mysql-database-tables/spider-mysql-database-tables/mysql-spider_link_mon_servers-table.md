
# mysql.spider_link_mon_servers Table

The `<code>mysql.spider_link_mon_servers</code>` table is installed by the [Spider storage engine](../../../../../../storage-engines/spider/spider-functions/spider_copy_tables.md).


This table uses the [Aria](../../../../../../storage-engines/s3-storage-engine/aria_s3_copy.md) storage engine.


It contains the following fields:



| Field | Type | Null | Key | Default | Description |
| --- | --- | --- | --- | --- | --- |
| Field | Type | Null | Key | Default | Description |
| db_name | char(64) | NO | PRI |  |  |
| table_name | char(199) | NO | PRI |  |  |
| link_id | char(64) | NO | PRI |  |  |
| sid | int(10) unsigned | NO | PRI | 0 |  |
| server | char(64) | YES |  | NULL |  |
| scheme | char(64) | YES |  | NULL |  |
| host | char(64) | YES |  | NULL |  |
| port | char(5) | YES |  | NULL |  |
| socket | text | YES |  | NULL |  |
| username | char(64) | YES |  | NULL |  |
| password | char(64) | YES |  | NULL |  |
| ssl_ca | text | YES |  | NULL |  |
| ssl_capath | text | YES |  | NULL |  |
| ssl_cert | text | YES |  | NULL |  |
| ssl_cipher | char(64) | YES |  | NULL |  |
| ssl_key | text | YES |  | NULL |  |
| ssl_verify_server_cert | tinyint(4) | NO |  | 0 |  |
| default_file | text | YES |  | NULL |  |
| default_group | char(64) | YES |  | NULL |  |
| dsn | char(64) | YES |  | NULL |  |
| filedsn | text | YES |  | NULL |  |
| driver | char(64) | YES |  | NULL |  |


