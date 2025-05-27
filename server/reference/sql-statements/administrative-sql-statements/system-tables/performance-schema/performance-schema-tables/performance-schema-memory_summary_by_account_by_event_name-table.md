
# Performance Schema memory_summary_by_account_by_event_name Table


##### MariaDB starting with [10.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-5-series/mariadb-1052-release-notes)
The memory_summary_by_account_by_event_name table was introduced in [MariaDB 10.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-5-series/mariadb-1052-release-notes).


There are five memory summary tables in the Performance Schema that share a number of fields in common. These include:


* memory_summary_by_account_by_event_name
* [memory_summary_by_host_by_event_name](performance-schema-memory_summary_by_host_by_event_name-table.md)
* [memory_summary_by_thread_by_event_name](performance-schema-memory_summary_by_thread_by_event_name-table.md)
* [memory_summary_by_user_by_event_name](performance-schema-memory_summary_by_user_by_event_name-table.md)
* [memory_global_by_event_name](performance-schema-memory_summary_global_by_event_name-table.md)


The `memory_summary_by_account_by_event_name` table contains memory usage statistics aggregated by account and event.


The table contains the following columns:



| Field | Type | Null | Default | Description |
| --- | --- | --- | --- | --- |
| Field | Type | Null | Default | Description |
| USER | char(32) | YES | NULL | User portion of the account. |
| HOST | char(60) | YES | NULL | Host portion of the account. |
| EVENT_NAME | varchar(128) | NO | NULL | Event name. |
| COUNT_ALLOC | bigint(20) unsigned | NO | NULL | Total number of allocations to memory. |
| COUNT_FREE | bigint(20) unsigned | NO | NULL | Total number of attempts to free the allocated memory. |
| SUM_NUMBER_OF_BYTES_ALLOC | bigint(20) unsigned | NO | NULL | Total number of bytes allocated. |
| SUM_NUMBER_OF_BYTES_FREE | bigint(20) unsigned | NO | NULL | Total number of bytes freed |
| LOW_COUNT_USED | bigint(20) | NO | NULL | Lowest number of allocated blocks (lowest value of CURRENT_COUNT_USED). |
| CURRENT_COUNT_USED | bigint(20) | NO | NULL | Currently allocated blocks that have not been freed (COUNT_ALLOC minus COUNT_FREE). |
| HIGH_COUNT_USED | bigint(20) | NO | NULL | Highest number of allocated blocks (highest value of CURRENT_COUNT_USED). |
| LOW_NUMBER_OF_BYTES_USED | bigint(20) | NO | NULL | Lowest number of bytes used. |
| CURRENT_NUMBER_OF_BYTES_USED | bigint(20) | NO | NULL | Current number of bytes used (total allocated minus total freed). |
| HIGH_NUMBER_OF_BYTES_USED | bigint(20) | NO | NULL | Highest number of bytes used. |




CC BY-SA / Gnu FDL

