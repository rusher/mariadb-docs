
# Information Schema THREAD_POOL_QUEUES Table


##### MariaDB starting with [10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-5-series/what-is-mariadb-105)
The [Information Schema](../README.md) `THREAD_POOL_QUEUES` table was introduced in [MariaDB 10.5.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-5-series/mariadb-1050-release-notes).


The table provides information about [thread pool](../../../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/buffers-caches-and-threads/thread-pool/thread-pool-in-mariadb.md) queues, and contains the following columns:



| Column | Description |
| --- | --- |
| Column | Description |
| GROUP_ID | the thread group this row is showing data for |
| POSITION | position in the groups queue |
| PRIORITY | request priority, see [priority scheduling](../../../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/buffers-caches-and-threads/thread-pool/thread-pool-in-mariadb.md#configuring-priority-scheduling) |
| CONNECTION_ID | ID of the client connection that submitted the queued request |
| QUEUEING_TIME_MICROSECONDS | how long the request has already been waiting in the queue in microseconds |



Setting [thread_poll_exact_stats](../../../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/buffers-caches-and-threads/thread-pool/thread-pool-system-status-variables.md#thread_pool_exact_stats) will provides better queueing time statistics by using a high precision timestamp, at a small performance cost, for the time when the connection was added to the queue. This timestamp helps calculate the queuing time shown in the table.


Setting [thread_pool_dedicated_listener](../../../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/buffers-caches-and-threads/thread-pool/thread-pool-system-status-variables.md#thread_pool_dedicated_listener) will give each group its own dedicated listener, and the listener thread will not pick up work items. As a result, the queueing time in the table will be more exact, since IO requests are immediately dequeued from poll, without delay.

