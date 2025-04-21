
# Performance Schema replication_applier_status_by_worker Table


##### MariaDB starting with [10.6.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-1060-release-notes)
The `replication_applier_status_by_worker` table was added in [MariaDB 10.6.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-1060-release-notes).


The [Performance Schema](../README.md) replication_applier_status_by_worker table displays replica worker thread specific information.


It contains the following fields.



| Column | Description |
| --- | --- |
| Column | Description |
| CHANNEL_NAME | Name of replication channel through which the transaction is received. |
| THREAD_ID | Thread_Id as displayed in the [performance_schema.threads](performance-schema-threads-table.md) table for thread with name 'thread/sql/rpl_parallel_thread'. THREAD_ID will be NULL when worker threads are stopped due to error/force stop. |
| SERVICE_STATE | Whether or not the thread is running. |
| LAST_SEEN_TRANSACTION | Last GTID executed by worker |
| LAST_ERROR_NUMBER | Last Error that occurred on a particular worker. |
| LAST_ERROR_MESSAGE | Last error specific message. |
| LAST_ERROR_TIMESTAMP | Time stamp of last error. |
| WORKER_IDLE_TIME | Total idle time in seconds that the worker thread has spent waiting for work from SQL thread. |
| LAST_TRANS_RETRY_COUNT | Total number of retries attempted by last transaction. |


