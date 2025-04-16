
# Information Schema THREAD_POOL_GROUPS Table


##### MariaDB starting with [10.5](../../../../../../../../release-notes/mariadb-community-server/what-is-mariadb-105.md)
The [Information Schema](../../../../../../mariadb-internals/information-schema-plugins-show-and-flush-statements.md) `THREAD_POOL_GROUPS` table was introduced in [MariaDB 10.5.0](../../../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1050-release-notes.md).


The table provides information about [thread pool](../../../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/buffers-caches-and-threads/thread-pool/thread-pool-in-mariadb-51-53.md) groups, and contains the following columns:



| Column | Description |
| --- | --- |
| Column | Description |
| GROUP_ID | the thread group this row is showing data for |
| CONNECTIONS | the number of clients currently connected to this thread group |
| THREADS | total number of threads in this group (ACTIVE+STANDBY+LISTENER) |
| ACTIVE_THREADS | number of threads currently executing a query |
| STANDBY_THREADS | number of threads in reserve that do not currently execute anything |
| QUEUE_LENGTH | number of client requests waiting for execution |
| HAS_LISTENER | whether there is an active listener thread right now, always 1 if [thread_pool_dedicated_listener](../../../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/buffers-caches-and-threads/thread-pool/thread-pool-system-status-variables.md#thread_pool_dedicated_listener) is ON |
| IS_STALLED | whether there's currently an active worker thread in this group that has exceeded [thread_pool_stall_limit time](../../../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/buffers-caches-and-threads/thread-pool/thread-pool-system-status-variables.md#thread_pool_stall_limit_time) |



Setting [thread_pool_dedicated_listener](../../../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/buffers-caches-and-threads/thread-pool/thread-pool-system-status-variables.md#thread_pool_dedicated_listener) will give each group its own dedicated listener, and the listener thread will not pick up work items. As a result, the actual queue size in the table will be more exact, since IO requests are immediately dequeued from poll, without delay.

