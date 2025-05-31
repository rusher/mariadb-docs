# Information Schema THREAD\_POOL\_GROUPS Table

**MariaDB starting with** [**10.5**](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-5-series/what-is-mariadb-105)

The [Information Schema](../) `THREAD_POOL_GROUPS` table was introduced in [MariaDB 10.5.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-5-series/mariadb-1050-release-notes).

The table provides information about [thread pool](../../../../../../ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/thread-pool/thread-pool-in-mariadb.md) groups, and contains the following columns:

| Column           | Description                                                                                                                                                                                                                                                                                  |
| ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Column           | Description                                                                                                                                                                                                                                                                                  |
| GROUP\_ID        | the thread group this row is showing data for                                                                                                                                                                                                                                                |
| CONNECTIONS      | the number of clients currently connected to this thread group                                                                                                                                                                                                                               |
| THREADS          | total number of threads in this group (ACTIVE+STANDBY+LISTENER)                                                                                                                                                                                                                              |
| ACTIVE\_THREADS  | number of threads currently executing a query                                                                                                                                                                                                                                                |
| STANDBY\_THREADS | number of threads in reserve that do not currently execute anything                                                                                                                                                                                                                          |
| QUEUE\_LENGTH    | number of client requests waiting for execution                                                                                                                                                                                                                                              |
| HAS\_LISTENER    | whether there is an active listener thread right now, always 1 if [thread\_pool\_dedicated\_listener](../../../../../../ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/thread-pool/thread-pool-system-status-variables.md#thread_pool_dedicated_listener) is ON       |
| IS\_STALLED      | whether there's currently an active worker thread in this group that has exceeded [thread\_pool\_stall\_limit time](../../../../../../ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/thread-pool/thread-pool-system-status-variables.md#thread_pool_stall_limit_time) |

Setting [thread\_pool\_dedicated\_listener](../../../../../../ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/thread-pool/thread-pool-system-status-variables.md#thread_pool_dedicated_listener) will give each group its own dedicated listener, and the listener thread will not pick up work items. As a result, the actual queue size in the table will be more exact, since IO requests are immediately dequeued from poll, without delay.

CC BY-SA / Gnu FDL
