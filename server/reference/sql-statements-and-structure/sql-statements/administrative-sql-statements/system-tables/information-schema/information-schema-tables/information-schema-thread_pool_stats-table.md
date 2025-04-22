
# Information Schema THREAD_POOL_STATS Table


##### MariaDB starting with [10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-5-series/what-is-mariadb-105)
The [Information Schema](../README.md) `THREAD_POOL_STATS` table was introduced in [MariaDB 10.5.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-5-series/mariadb-1050-release-notes).


The table provides performance counter information for the [thread pool](../../../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/buffers-caches-and-threads/thread-pool/thread-pool-in-mariadb.md), and contains the following columns:



| Column | Description |
| --- | --- |
| Column | Description |
| GROUP_ID | the thread group this row is showing data for |
| THREAD_CREATIONS | number of threads created for this group so far |
| THREAD_CREATIONS_DUE_TO_STALL | number of threads created due to detected stalls |
| WAKES | standby thread wakeups |
| WAKES_DUE_TO_STALL | wakeups due to stalls |
| THROTTLES | how often thread creation was throttled, see also: [thread-creation-throttling](../../../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/buffers-caches-and-threads/thread-pool/thread-groups-in-the-unix-implementation-of-the-thread-pool.md#thread-creation-throttling) |
| STALLS | number of detected stalls |
| POLLS_BY_LISTENER |  |
| POLLS_BY_WORKER |  |
| DEQUEUES_BY_LISTENER |  |
| DEQUEUES_BY_WORKER |  |


