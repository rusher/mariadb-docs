
# Sys Schema sys_config Table


##### MariaDB starting with [10.6.0](../../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-1060-release-notes.md)
The Sys Schema *sys_config* table was added in [MariaDB 10.6.0](../../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-1060-release-notes.md).  The *sys_config* table is also backported to [MariaDB-10.5-enterprise](https://mariadb.com/kb/en/mariadb-server-releases-mariadb-enterprise-server-10-5/).


The *sys.sys_config* table holds configuration options for the [Sys Schema](sys-schema-views/sys-schema-views-host_summary_by_statement_latency-and-xhost_summary_by_sta.md).


This is a persistent table (using the [Aria](../../../../../storage-engines/s3-storage-engine/aria_s3_copy.md) storage engine), with the configuration persisting across upgrades (new options are added with [INSERT IGNORE](../../../data-manipulation/inserting-loading-data/insert-ignore.md).


The table also has two related triggers, which maintain the user that INSERTs or UPDATEs the configuration - sys_config_insert_set_user and sys_config_update_set_user respectively.


Its structure is as follows:


```
+----------+--------------+------+-----+-------------------+-----------------------------+
| Field    | Type         | Null | Key | Default           | Extra                       |
+----------+--------------+------+-----+-------------------+-----------------------------+
| variable | varchar(128) | NO   | PRI | NULL              |                             |
| value    | varchar(128) | YES  |     | NULL              |                             |
| set_time | timestamp    | NO   |     | CURRENT_TIMESTAMP | on update CURRENT_TIMESTAMP |
| set_by   | varchar(128) | YES  |     | NULL              |                             |
+----------+--------------+------+-----+-------------------+-----------------------------+
```

Note, when functions check for configuration options, they first check whether a similar named user variable exists with a value, and if this is not set then pull the configuration option from this table in to that named user variable. This is done for performance reasons (to not continually SELECT from the table), however this comes with the side effect that once inited, the values last with the session, somewhat like how session variables are inited from global variables. If the values within this table are changed, they will not take effect until the user logs in again.


### Options Included



| Variable | Default Value | Description |
| --- | --- | --- |
| Variable | Default Value | Description |
| statement_truncate_len | 64 | Sets the size to truncate statements to, for the [format_statement](sys-schema-stored-functions/format_statement.md) function. |
| statement_performance_analyzer.limit | 100 | The maximum number of rows to include for the views that does not have a built-in limit (e.g. the 95th percentile view). If not set the limit is 100. |
| statement_performance_analyzer.view | NULL | Used together with the 'custom' view. If the value contains a space, it is considered a query, otherwise it must be an existing view querying the performance_schema.events_statements_summary_by_digest table. |
| diagnostics.allow_i_s_tables | OFF | Specifies whether it is allowed to do table scan queries on information_schema.TABLES for the diagnostics procedure. |
| diagnostics.include_raw | OFF | Set to 'ON' to include the raw data (e.g. the original output of "SELECT * FROM sys.metrics") for the diagnostics procedure. |
| ps_thread_trx_info.max_length | 65535 | Sets the maximum output length for JSON object output by the ps_thread_trx_info() function. |



### Notes


Some early versions of *sys_config* were stored in [InnoDB](../../../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/innodb-upgrade-tests/README.md) format.

