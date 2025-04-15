
# InnoDB Buffer Pool

The [InnoDB](../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/innodb-upgrade-tests/README.md) buffer pool is a key component for optimizing MariaDB. It stores data and indexes, and you usually want it as large as possible so as to keep as much of the data and indexes in memory, reducing disk IO, as main bottleneck.


## How the Buffer Pool Works


The buffer pool attempts to keep frequently-used blocks in the buffer, and so essentially works as two sublists, a *new* sublist of recently-used information, and an *old* sublist of older information. By default, 37% of the list is reserved for the old list.


When new information is accessed that doesn't appear in the list, it is placed at the top of the old list, the oldest item in the old list is removed, and everything else bumps back one position in the list.


When information is accessed that appears in the *old* list, it is moved to the top the new list, and everything above moves back one position.


## innodb_buffer_pool_size


The most important [server system variable](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md) is [innodb_buffer_pool_size](innodb-system-variables.md#innodb_buffer_pool_size). This size should contain most of the active data set of your server so that SQL request can work directly with information in the buffer pool cache. Starting at several gigabytes of memory is a good starting point if you have that RAM available. Once warmed up to its normal load there should be very few [innodb_buffer_pool_reads](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/innodb-status-variables.md#innodb_buffer_pool_reads) compared to [innodb_buffer_pool_read_requests](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/innodb-status-variables.md#innodb_buffer_pool_read_requests). Look how these values change over a minute. If the change in [innodb_buffer_pool_reads](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/innodb-status-variables.md#innodb_buffer_pool_reads) is less than 1% of the change in [innodb_buffer_pool_read_requests](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/innodb-status-variables.md#innodb_buffer_pool_read_requests) then you have a good amount of usage. If you are getting the status variable [innodb_buffer_pool_wait_free](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/innodb-status-variables.md#innodb_buffer_wait_free) increasing then you don't have enough buffer pool (or your flushing isn't occurring frequently enough).


Be aware that before [MariaDB 10.4.4](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-4-series/mariadb-1044-release-notes.md) the total memory allocated is about 10% more than the specified size as extra space is also reserved for control structures and buffers.


The larger the size, the longer it will take to initialize. On a modern 64-bit server with a 10GB memory pool, this can take five seconds or more. Increasing [innodb_buffer_pool_chunk_size](innodb-system-variables.md#innodb_buffer_pool_chunk_size) by several factors will reduce this significantly. [MariaDB 10.6](../../../../release-notes/mariadb-community-server/what-is-mariadb-106.md) could start up with a 96GB buffer pool in less than 1 second.


Make sure that the size is not too large, causing swapping. The benefit of a larger buffer pool size is more than undone if your operating system is regularly swapping.


The buffer pool can be set dynamically. See [Setting Innodb Buffer Pool Size Dynamically](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/setting-innodb-buffer-pool-size-dynamically.md).


## innodb_buffer_pool_instances


The functionality described below was disabled in [MariaDB 10.5](../../../../release-notes/mariadb-community-server/what-is-mariadb-105.md), and removed in [MariaDB 10.6](../../../../release-notes/mariadb-community-server/what-is-mariadb-106.md), as the original reasons for for splitting the buffer pool have mostly gone away.


If innodb_buffer_pool_size is set to more than 1GB, [innodb_buffer_pool_instances](innodb-system-variables.md#innodb_buffer_pool_instances) divides the InnoDB buffer pool into a specific number of instances. The default was 1 in [MariaDB 5.5](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5.md), but for large systems with buffer pools of many gigabytes, many instances can help reduce contention concurrency. The default is 8 in [MariaDB 10.0](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md), with the exception of 32-bit Windows, where it depends on the value of [innodb_buffer_pool_size](innodb-system-variables.md#innodb_buffer_pool_size). Each instance manages its own data structures and takes an equal portion of the total buffer pool size, so for example if innodb_buffer_pool_size is 4GB and innodb_buffer_pool_instances is set to 4, each instance will be 1GB. Each instance should ideally be at least 1GB in size.


## innodb_old_blocks_pct and innodb_old_blocks_time


The default 37% reserved for the old list can be adjusted by changing the value of [innodb_old_blocks_pct](innodb-system-variables.md#innodb_old_blocks_pct). It can accept anything between between 5% and 95%.


The [innodb_old_blocks_time](innodb-system-variables.md#innodb_old_blocks_time) variable specifies the delay before a block can be moved from the old to the new sublist. `<code>0</code>` means no delay, while the default has been set to `<code>1000</code>`.


Before changing either of these values from their defaults, make sure you understand the impact and how your system currently uses the buffer. Their main reason for existence is to reduce the impact of full table scans, which are usually infrequent, but large, and previously could clear everything from the buffer. Setting a non-zero delay could help in situations where full table scans are performed in quick succession.


Temporarily changing these values can also be useful to avoid the negative impact of a full table scan, as explained in [InnoDB logical backups](../../../server-management/backing-up-and-restoring-databases/backup-and-restore-overview.md#innodb-logical-backups).


## Dumping and Restoring the Buffer Pool


When the server starts, the buffer pool is empty. As it starts to access data, the buffer pool will slowly be populated. As more data will be accessed, the most frequently accessed data will be put into the buffer pool, and old data may be evicted. This means that a certain period of time is necessary before the buffer pool is really useful. This period of time is called the warmup.


Since [MariaDB 10.0](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md), InnoDB can dump the buffer pool before the server shuts down, and restore it when it starts again. If this feature is used (default since [MariaDB 10.2](../../../../release-notes/mariadb-community-server/what-is-mariadb-102.md)), no warmup is necessary. Use the [innodb_buffer_pool_dump_at_shutdown](innodb-system-variables.md#innodb_buffer_pool_dump_at_shutdown) and [innodb_buffer_pool_load_at_startup](innodb-system-variables.md#innodb_buffer_pool_load_at_startup) system variables to enable or disable the buffer pool dump at shutdown and the restore at startup respectively.


It is also possible to dump the InnoDB buffer pool at any moment while the server is running, and it is possible to restore the last buffer pool dump at any moment. To do this, the special [innodb_buffer_pool_dump_now](innodb-system-variables.md#innodb_buffer_pool_dump_now) and [innodb_buffer_pool_load_now](innodb-system-variables.md#innodb_buffer_pool_load_now) system variables can be set to ON. When selected, their value is always OFF.


A buffer pool restore, both at startup or at any other moment, can be aborted by setting [innodb_buffer_pool_load_abort](innodb-system-variables.md#innodb_buffer_pool_load_abort) to ON.


The file which contains the buffer pool dump is specified via the [innodb_buffer_pool_filename](innodb-system-variables.md#innodb_buffer_pool_filename) system variable.


## See Also


* [InnoDB Change Buffering](innodb-change-buffering.md)
* [Information Schema INNODB_BUFFER_POOL_STATS Table](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb_buffer_pool_stats-table.md)
* [Setting Innodb Buffer Pool Size Dynamically](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/setting-innodb-buffer-pool-size-dynamically.md)

