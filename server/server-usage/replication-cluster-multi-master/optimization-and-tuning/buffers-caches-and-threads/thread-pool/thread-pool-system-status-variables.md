
# Thread Pool System and Status Variables


This article describes the system and status variables used by the MariaDB thread pool. For a full description, see [Thread Pool in MariaDB](thread-pool-in-mariadb-51-53.md).


## System variables


#### `<code>extra_max_connections</code>`


* Description: The number of connections on the `<code>[extra_port](#extra_port)</code>`.

  * See [Thread Pool in MariaDB: Configuring the Extra Port](thread-pool-in-mariadb-51-53.md#configuring-the-extra-port) for more information.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--extra-max-connections=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>1</code>`
* Range: `<code>1</code>` to `<code>100000</code>`



#### `<code>extra_port</code>`


* Description: Extra port number to use for TCP connections in a `<code>one-thread-per-connection</code>` manner. If set to `<code>0</code>`, then no extra port is used.

  * See [Thread Pool in MariaDB: Configuring the Extra Port](thread-pool-in-mariadb-51-53.md#configuring-the-extra-port) for more information.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--extra-port=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value: `<code>0</code>`



#### `<code>thread_handling</code>`


* Description: Determines how the server handles threads for client connections. In addition to threads for client connections, this also applies to certain internal server threads, such as [Galera slave threads](../../../galera-cluster/about-galera-replication.md#galera-slave-threads). On Windows, if you would like to use the thread pool, then you do not need to do anything, because the default for the thread_handling system variable is already preset to `<code>pool-of-threads</code>`. 

  * When the default `<code>one-thread-per-connection</code>` mode is enabled, the server uses one thread to handle each client connection.
  * When the `<code>pool-of-threads</code>` mode is enabled, the server uses the [thread pool](thread-pool-in-mariadb-51-53.md) for client connections.
  * When the `<code>no-threads</code>` mode is enabled, the server uses a single thread for all client connections, which is really only usable for debugging.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--thread-handling=name</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>enumeration</code>`
* Default Value: `<code>one-thread-per-connection</code>` (non-Windows), `<code>pool-of-threads</code>` (Windows)
* Valid Values: `<code>no-threads</code>`, `<code>one-thread-per-connection</code>`, `<code>pool-of-threads</code>`.
* Documentation: [Using the thread pool](thread-pool-in-mariadb-51-53.md).
* Notes: In MySQL, the thread pool is only available in MySQL Enterprise. In MariaDB it's available in all versions.



#### `<code>thread_pool_dedicated_listener</code>`


* Description: If set to 1, then each group will have its own dedicated listener, and the listener thread will not pick up work items. As a result, the queueing time in the [Information Schema Threadpool_Queues](../../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-thread_pool_queues-table.md) and the actual queue size in the [Information Schema Threadpool_Groups](../../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-thread_pool_groups-table.md) table will be more exact, since
IO requests are immediately dequeued from poll, without delay.

  * This system variable is only meaningful on Unix.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">thread-pool-dedicated-listener={0|1}</code>`
* Scope:
* Dynamic:
* Data Type: `<code>boolean</code>`
* Default Value: `<code>0</code>`
* Introduced: [MariaDB 10.5.0](../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1050-release-notes.md)



#### `<code>thread_pool_exact_stats</code>`


* Description: If set to 1, provides better queueing time statistics by using a high precision timestamp, at a small performance cost, for the time when the connection was added to the queue. This timestamp helps
calculate the queuing time shown in the [Information Schema Threadpool_Queues](../../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-thread_pool_queues-table.md) table.

  * This system variable is only meaningful on Unix.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">thread-pool-exact-stats={0|1}</code>`
* Scope:
* Dynamic:
* Data Type: `<code>boolean</code>`
* Default Value: `<code>0</code>`
* Introduced: [MariaDB 10.5.0](../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1050-release-notes.md)



#### `<code>thread_pool_idle_timeout</code>`


* Description: The number of seconds before an idle worker thread exits. The default value is `<code>60</code>`. If there is currently no work to do, how long should an idle thread wait before exiting?

  * This system variable is only meaningful on Unix.
  * The `<code>[thread_pool_min_threads](#thread_pool_min_threads)</code>` system variable is comparable for Windows.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">thread-pool-idle-timeout=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>60</code>`
* Documentation: [Using the thread pool](thread-pool-in-mariadb-51-53.md).



#### `<code>thread_pool_max_threads</code>`


* Description: The maximum number of threads in the [thread pool](thread-pool-in-mariadb-51-53.md). Once this limit is reached, no new threads will be created in most cases.

  * On Unix, in rare cases, the actual number of threads can slightly exceed this, because each [thread group](thread-groups-in-the-unix-implementation-of-the-thread-pool.md) needs at least two threads (i.e. at least one worker thread and at least one listener thread) to prevent deadlocks.
* Scope:
* Commandline: `<code class="fixed" style="white-space:pre-wrap">thread-pool-max-threads=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value:

  * `<code>65536</code>` (>= [MariaDB 10.2.4](../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1024-release-notes.md))
  * `<code>1000</code>` (<= [MariaDB 10.2.3](../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1023-release-notes.md), >= [MariaDB 10.1](../../../../../../release-notes/mariadb-community-server/what-is-mariadb-1010.md))
  * `<code>500</code>` (<= [MariaDB 10.0](../../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md))
* Range: `<code>1</code>` to `<code>65536</code>`
* Documentation: [Using the thread pool](thread-pool-in-mariadb-51-53.md).



#### `<code>thread_pool_min_threads</code>`


* Description: Minimum number of threads in the [thread pool](thread-pool-in-mariadb-51-53.md). In bursty environments, after a period of inactivity, threads would normally be retired. When the next burst arrives, it would take time to reach the optimal level. Setting this value higher than the default would prevent thread retirement even if inactive.

  * This system variable is only meaningful on Windows.
  * The `<code>[thread_pool_idle_timeout](#thread_pool_idle_timeout)</code>` system variable is comparable for Unix.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">thread-pool-min-threads=#</code>`
* Data Type: `<code>numeric</code>`
* Default Value: `<code>1</code>`
* Documentation: [Using the thread pool](thread-pool-in-mariadb-51-53.md).



#### `<code>thread_pool_oversubscribe</code>`


* Description: Determines how many worker threads in a thread group can remain active at the same time once a thread group is oversubscribed due to stalls. The default value is `<code>3</code>`. Usually, a thread group only has one active worker thread at a time. However, the timer thread can add more active worker threads to a thread group if it detects a stall. There are trade-offs to consider when deciding whether to allow only one thread per CPU to run at a time, or whether to allow more than one thread per CPU to run at a time. Allowing only one thread per CPU means that the thread can have unrestricted access to the CPU while its running, but it also means that there is additional overhead from putting threads to sleep or waking them up more frequently. Allowing more than one thread per CPU means that the threads have to share the CPU, but it also means that there is less overhead from putting threads to sleep or waking them up.

  * See [Thread Groups in the Unix Implementation of the Thread Pool: Thread Group Oversubscription](thread-groups-in-the-unix-implementation-of-the-thread-pool.md#thread-group-oversubscription) for more information.
  * This is primarily for internal use, and it is not meant to be changed for most users.
  * This system variable is only meaningful on Unix.
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>3</code>`
* Range: `<code>1</code>` to `<code>65536</code>`
* Documentation: [Using the thread pool](thread-pool-in-mariadb-51-53.md).



#### `<code>thread_pool_prio_kickup_timer</code>`


* Description: Time in milliseconds before a dequeued low-priority statement is moved to the high-priority queue.

  * This system variable is only meaningful on Unix.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">thread-pool-kickup-timer=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>1000</code>`
* Range: `<code>0</code>` to `<code>4294967295</code>`
* Introduced: [MariaDB 10.2.2](../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1022-release-notes.md)
* Documentation: [Using the thread pool](thread-pool-in-mariadb-51-53.md).



#### `<code>thread_pool_priority</code>`


* Description: [Thread pool](thread-pool-in-mariadb-51-53.md) priority. High-priority connections usually start executing earlier than low-priority.
If set to 'auto' (the default), the actual priority (low or high) is determined by whether or not the connection is inside a transaction.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--thread-pool-priority=#</code>`
* Scope: Global,Connection
* Data Type: `<code>enum</code>`
* Default Value: `<code>auto</code>`
* Valid Values: `<code>high</code>`, `<code>low</code>`, `<code>auto</code>`.
* Introduced: [MariaDB 10.2.2](../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1022-release-notes.md)
* Documentation: [Using the thread pool](thread-pool-in-mariadb-51-53.md).



#### `<code>thread_pool_size</code>`


* Description: The number of [thread groups](thread-groups-in-the-unix-implementation-of-the-thread-pool.md) in the [thread pool](thread-pool-in-mariadb-51-53.md), which determines how many statements can execute simultaneously. The default value is the number of CPUs on the system. When setting this system variable's value at system startup, the max value is 100000. However, it is not a good idea to set it that high. When setting this system variable's value dynamically, the max value is either 128 or the value that was set at system startup--whichever value is higher.

  * See [Thread Groups in the Unix Implementation of the Thread Pool](thread-groups-in-the-unix-implementation-of-the-thread-pool.md) for more information.
  * This system variable is only meaningful on Unix.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--thread-pool-size=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: Based on the number of processors (but see [MDEV-7806](https://jira.mariadb.org/browse/MDEV-7806)).
* Range: `<code>1</code>` to `<code>128</code>` (< [MariaDB 5.5.37](../../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/mariadb-5537-release-notes.md), [MariaDB 10.0.11](../../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-10011-release-notes.md)), `<code>1</code>` to `<code>100000</code>` (>= [MariaDB 5.5.37](../../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/mariadb-5537-release-notes.md), [MariaDB 10.0.11](../../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-10011-release-notes.md))
* Documentation: [Using the thread pool](thread-pool-in-mariadb-51-53.md).



#### `<code>thread_pool_stall_limit</code>`


* Description: The number of milliseconds between each stall check performed by the timer thread. The default value is `<code>500</code>`. Stall detection is used to prevent a single client connection from monopolizing a thread group. When the timer thread detects that a thread group is stalled, it wakes up a sleeping worker thread in the thread group, if one is available. If there isn't one, then it creates a new worker thread in the thread group. This temporarily allows several client connections in the thread group to run in parallel. However, note that the timer thread will not create a new worker thread if the number of threads in the thread pool is already greater than or equal to the maximum defined by the `<code>[thread_pool_max_threads](#thread_pool_max_threads)</code>` variable, unless the thread group does not already have a listener thread.

  * See [Thread Groups in the Unix Implementation of the Thread Pool: Thread Group Stalls](thread-groups-in-the-unix-implementation-of-the-thread-pool.md#thread-group-stalls) for more information.
  * This system variable is only meaningful on Unix.
  * Note that if you are migrating from the MySQL Enterprise thread pool plugin, then the unit used in their implementation is 10ms, not 1ms.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--thread-pool-stall-limit=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>500</code>`
* Range: `<code>10</code>` to `<code>4294967295</code>` (< [MariaDB 10.5](../../../../../../release-notes/mariadb-community-server/what-is-mariadb-105.md)), `<code>1</code>` to `<code>4294967295</code>` (>= [MariaDB 10.5](../../../../../../release-notes/mariadb-community-server/what-is-mariadb-105.md))
* Documentation: [Using the thread pool](thread-pool-in-mariadb-51-53.md).



## Status variables


#### `<code>Threadpool_idle_threads</code>`


* Description: Number of inactive threads in the [thread pool](thread-pool-in-mariadb-51-53.md). Threads become inactive for various reasons, such as by waiting for new work. However, an inactive thread is not necessarily one that has not been assigned work. Threads are also considered inactive if they are being blocked while waiting on disk I/O, or while waiting on a lock, etc.

  * This status variable is only meaningful on Unix.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`



#### `<code>Threadpool_threads</code>`


* Description: Number of threads in the [thread pool](thread-pool-in-mariadb-51-53.md). In rare cases, this can be slightly higher than `<code>[thread_pool_max_threads](#thread_pool_max_threads)</code>`, because each thread group needs at least two threads (i.e. at least one worker thread and at least one listener thread) to prevent deadlocks.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`



## See Also


* [Thread Pool in MariaDB](thread-pool-in-mariadb-51-53.md)

