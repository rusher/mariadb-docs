
# InnoDB Buffer Pool

The InnoDB storage engine in MariaDB Enterprise Server utilizes the Buffer Pool as a crucial in-memory cache. This Buffer Pool stores recently accessed data pages, enabling faster retrieval for subsequent requests. Recognizing patterns of access, InnoDB also employs predictive prefetching, caching nearby pages when sequential access is detected. To manage memory efficiently, a least recently used (LRU) algorithm is used to evict older, less frequently accessed pages.


To optimize server restarts, the Buffer Pool's contents can be preserved across shutdowns. At shutdown, the page numbers of all pages residing in the Buffer Pool are recorded. Upon the next startup, InnoDB reads this dump of page numbers and reloads the corresponding data pages from their respective data files, effectively avoiding a "cold" cache scenario.


The size of each individual page within the Buffer Pool is determined by the setting of the innodb_page_size system variable.


## How the Buffer Pool Works


The buffer pool attempts to keep frequently-used blocks in the buffer, and so essentially works as two sublists, a *new* sublist of recently-used information, and an *old* sublist of older information. By default, 37% of the list is reserved for the old list.


When new information is accessed that doesn't appear in the list, it is placed at the top of the old list, the oldest item in the old list is removed, and everything else bumps back one position in the list.


When information is accessed that appears in the *old* list, it is moved to the top the new list, and everything above moves back one position.


## innodb_buffer_pool_size


The most important [server system variable](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md) is [innodb_buffer_pool_size](innodb-system-variables.md#innodb_buffer_pool_size). This size should contain most of the active data set of your server so that SQL request can work directly with information in the buffer pool cache. Starting at several gigabytes of memory is a good starting point if you have that RAM available. Once warmed up to its normal load there should be very few [innodb_buffer_pool_reads](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/innodb-status-variables.md#innodb_buffer_pool_reads) compared to [innodb_buffer_pool_read_requests](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/innodb-status-variables.md#innodb_buffer_pool_read_requests). Look how these values change over a minute. If the change in [innodb_buffer_pool_reads](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/innodb-status-variables.md#innodb_buffer_pool_reads) is less than 1% of the change in [innodb_buffer_pool_read_requests](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/innodb-status-variables.md#innodb_buffer_pool_read_requests) then you have a good amount of usage. If you are getting the status variable [innodb_buffer_pool_wait_free](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/innodb-status-variables.md#innodb_buffer_wait_free) increasing then you don't have enough buffer pool (or your flushing isn't occurring frequently enough).


The larger the size, the longer it will take to initialize. On a modern 64-bit server with a 10GB memory pool, this can take five seconds or more. Increasing [innodb_buffer_pool_chunk_size](innodb-system-variables.md#innodb_buffer_pool_chunk_size) by several factors will reduce this significantly. [MariaDB 10.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-6-series/what-is-mariadb-106) could start up with a 96GB buffer pool in less than 1 second.


Make sure that the size is not too large, causing swapping. The benefit of a larger buffer pool size is more than undone if your operating system is regularly swapping.


The buffer pool can be set dynamically. See [Setting Innodb Buffer Pool Size Dynamically](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/setting-innodb-buffer-pool-size-dynamically.md).


## innodb_buffer_pool_instances


The functionality described below was disabled in [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-5-series/what-is-mariadb-105), and removed in [MariaDB 10.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-6-series/what-is-mariadb-106), as the original reasons for for splitting the buffer pool have mostly gone away.


## innodb_old_blocks_pct and innodb_old_blocks_time


The default 37% reserved for the old list can be adjusted by changing the value of [innodb_old_blocks_pct](innodb-system-variables.md#innodb_old_blocks_pct). It can accept anything between between 5% and 95%.


The [innodb_old_blocks_time](innodb-system-variables.md#innodb_old_blocks_time) variable specifies the delay before a block can be moved from the old to the new sublist. `0` means no delay, while the default has been set to `1000`.


Before changing either of these values from their defaults, make sure you understand the impact and how your system currently uses the buffer. Their main reason for existence is to reduce the impact of full table scans, which are usually infrequent, but large, and previously could clear everything from the buffer. Setting a non-zero delay could help in situations where full table scans are performed in quick succession.


Temporarily changing these values can also be useful to avoid the negative impact of a full table scan, as explained in [InnoDB logical backups](../../../server-management/backing-up-and-restoring-databases/backup-and-restore-overview.md#innodb-logical-backups).


## Dumping and Restoring the Buffer Pool


When the server starts, the buffer pool is empty. As it starts to access data, the buffer pool will slowly be populated. As more data will be accessed, the most frequently accessed data will be put into the buffer pool, and old data may be evicted. This means that a certain period of time is necessary before the buffer pool is really useful. This period of time is called the warmup.


InnoDB can dump the buffer pool before the server shuts down, and restore it when it starts again. If this feature is used, no warmup is necessary. Use the [innodb_buffer_pool_dump_at_shutdown](innodb-system-variables.md#innodb_buffer_pool_dump_at_shutdown) and [innodb_buffer_pool_load_at_startup](innodb-system-variables.md#innodb_buffer_pool_load_at_startup) system variables to enable or disable the buffer pool dump at shutdown and the restore at startup respectively.


It is also possible to dump the InnoDB buffer pool at any moment while the server is running, and it is possible to restore the last buffer pool dump at any moment. To do this, the special [innodb_buffer_pool_dump_now](innodb-system-variables.md#innodb_buffer_pool_dump_now) and [innodb_buffer_pool_load_now](innodb-system-variables.md#innodb_buffer_pool_load_now) system variables can be set to ON. When selected, their value is always OFF.


A buffer pool restore, both at startup or at any other moment, can be aborted by setting [innodb_buffer_pool_load_abort](innodb-system-variables.md#innodb_buffer_pool_load_abort) to ON.


The file which contains the buffer pool dump is specified via the [innodb_buffer_pool_filename](innodb-system-variables.md#innodb_buffer_pool_filename) system variable.


## See Also


* [InnoDB Change Buffering](innodb-change-buffering.md)
* [Information Schema INNODB_BUFFER_POOL_STATS Table](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb_buffer_pool_stats-table.md)
* [Setting Innodb Buffer Pool Size Dynamically](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/setting-innodb-buffer-pool-size-dynamically.md)


CC BY-SA / Gnu FDL

