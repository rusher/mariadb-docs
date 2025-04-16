
# Performance Schema replication_applier_status_by_coordinator Table


##### MariaDB starting with [10.5.2](../../../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1052-release-notes.md)
The `replication_applier_status_by_coordinator` table was added in [MariaDB 10.5.2](../../../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1052-release-notes.md).


The [Performance Schema](performance-schema-table_handles-table.md) replication_applier_status_by_coordinator table displays the status of the coordinator thread used in multi-threaded replicas to manage multiple worker threads.


It contains the following fields.



| Column | Type | Null | Description |
| --- | --- | --- | --- |
| Column | Type | Null | Description |
| CHANNEL_NAME | varchar(256) | NO | Replication channel name. |
| THREAD_ID | bigint(20) unsigned | YES | The SQL/coordinator thread ID. |
| SERVICE_STATE | enum('ON','OFF') | NO | ON (thread exists and is active or idle) or OFF (thread no longer exists). |
| LAST_ERROR_NUMBER | int(11) | NO | Last error number that caused the SQL/coordinator thread to stop. |
| LAST_ERROR_MESSAGE | varchar(1024) | NO | Last error message that caused the SQL/coordinator thread to stop. |
| LAST_ERROR_TIMESTAMP | timestamp | NO | Timestamp that shows when the most recent SQL/coordinator error occured. |
| LAST_SEEN_TRANSACTION | char(57) | NO | The transaction the worker has last seen. |
| LAST_TRANS_RETRY_COUNT | int(11) | NO | Total number of retries attempted by last transaction. |


