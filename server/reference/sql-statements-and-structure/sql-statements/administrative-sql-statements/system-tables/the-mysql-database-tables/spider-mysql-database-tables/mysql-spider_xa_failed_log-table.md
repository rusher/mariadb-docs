
# mysql.spider_xa_failed_log Table

The `mysql.spider_xa_failed_log` table is installed by the [Spider storage engine](../../../../../../storage-engines/spider/README.md).


This table uses the [Aria](../../../../../../storage-engines/aria/README.md) storage engine.


It contains the following fields:



| Field | Type | Null | Key | Default | Description |
| --- | --- | --- | --- | --- | --- |
| Field | Type | Null | Key | Default | Description |
| format_id | int(11) | NO |  | 0 |  |
| gtrid_length | int(11) | NO |  | 0 |  |
| bqual_length | int(11) | NO |  | 0 |  |
| data | binary(128) | NO | MUL |  |  |
| scheme | char(64) | NO |  |  |  |
| host | char(64) | NO |  |  |  |
| port | char(5) | NO |  |  |  |
| socket | text | NO |  | NULL |  |
| username | char(64) | NO |  |  |  |
| password | char(64) | NO |  |  |  |
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
| thread_id | int(11) | YES |  | NULL |  |
| status | char(8) | NO |  |  |  |
| failed_time | timestamp | NO |  | current_timestamp() |  |


