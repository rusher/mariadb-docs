
# InnoDB System Variables

This page documents system variables related to the [InnoDB storage engine](../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/innodb-upgrade-tests/README.md). For options that are not system variables, see [InnoDB Options](../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md).


See [Server System Variables](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md) for a complete list of system variables and instructions on setting them.


Also see the [Full list of MariaDB options, system and status variables](../../../server-management/variables-and-modes/full-list-of-mariadb-options-system-and-status-variables.md).


#### `<code>have_innodb</code>`


* Description: If the server supports [InnoDB tables](../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/innodb-upgrade-tests/README.md), will be set to `<code>YES</code>`, otherwise will be set to `<code>NO</code>`. Removed in [MariaDB 10.0](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md), use the [Information Schema PLUGINS](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/plugins-table-information-schema.md) table or [SHOW ENGINES](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-engines.md) instead.
* Scope: Global
* Dynamic: No
* Removed: [MariaDB 10.0](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md)



#### `<code>ignore_builtin_innodb</code>`


* Description: Setting this to `<code>1</code>` results in the built-in InnoDB storage engine being ignored. In some versions of MariaDB, XtraDB is the default and is always present, so this variable is ignored and setting it results in a warning. From [MariaDB 10.0.1](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-1001-release-notes.md) to [MariaDB 10.0.8](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-1008-release-notes.md), when InnoDB was the default instead of XtraDB, this variable needed to be set. Usually used in conjunction with the [plugin-load=innodb=ha_innodb](../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md) option to use the InnoDB plugin.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--ignore-builtin-innodb</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`



#### `<code>innodb_adaptive_checkpoint</code>`


* Description: Replaced with [innodb_adaptive_flushing_method](#innodb_adaptive_flushing_method). Controls adaptive checkpointing. InnoDB's fuzzy checkpointing can cause stalls, as many dirty blocks are flushed at once as the checkpoint age nears the maximum. Adaptive checkpointing aims for more consistent flushing, approximately `<code>modified age / maximum checkpoint age</code>`. Can result in larger transaction log files

  * `<code>reflex</code>` Similar to [innodb_max_dirty_pages_pct](#innodb_max_dirty_pages_pct) flushing but flushes blocks constantly and contiguously based on the oldest modified age. If the age exceeds 1/2 of the maximum age capacity, flushing will be weak contiguous. If the age exceeds 3/4, flushing will be strong. Strength can be adjusted by the variable [innodb_io_capacity](#innodb_io_capacity).
  * `<code>estimate</code>` The default, and independent of [innodb_io_capacity](#innodb_io_capacity). If the oldest modified age exceeds 1/2 of the maximum age capacity, blocks will be flushed every second at a rate determined by the number of modified blocks, LSN progress speed and the average age of all modified blocks.
  * `<code>keep_average</code>` Attempts to keep the I/O rate constant by using a shorter loop cycle of one tenth of a second. Designed for SSD cards.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-adaptive-checkpoint=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>string</code>`
* Default Value: `<code>estimate</code>`
* Valid Values: `<code>none</code>` or `<code>0</code>`, `<code>reflex</code>` or `<code>1</code>`, `<code>estimate</code>` or `<code>2</code>`, `<code>keep_average</code>` or `<code>3</code>`
* Removed: XtraDB 5.5 - replaced with [innodb_adaptive_flushing_method](#innodb_adaptive_flushing_method)



#### `<code>innodb_adaptive_flushing</code>`


* Description: If set to `<code>1</code>`, the default, the server will dynamically adjust the flush rate of dirty pages in the [InnoDB buffer pool](innodb-buffer-pool.md). This assists to reduce brief bursts of I/O activity. If set to `<code>0</code>`, adaptive flushing will only take place when the limit specified by [innodb_adaptive_flushing_lwm](#innodb_adaptive_flushing_lwm) is reached.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-adaptive-flushing={0|1}</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>ON</code>`



#### `<code>innodb_adaptive_flushing_lwm</code>`


* Description: Adaptive flushing is enabled when this low water mark percentage of the [InnoDB redo log](innodb-redo-log.md) capacity is reached. Takes effect even if [innodb_adaptive_flushing](#innodb_adaptive_flushing) is disabled.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-adaptive-flushing-lwm=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>double</code>`
* Default Value: `<code>10.000000</code>`
* Range: `<code>0</code>` to `<code>70</code>`



#### `<code>innodb_adaptive_flushing_method</code>`


* Description: Determines the method of flushing dirty blocks from the InnoDB [buffer pool](innodb-buffer-pool.md). If set to `<code>native</code>` or `<code>0</code>`, the original InnoDB method is used. The maximum checkpoint age is determined by the total length of all transaction log files. When the checkpoint age reaches the maximum checkpoint age, blocks are flushed. This can cause lag if there are many updates per second and many blocks with an almost identical age need to be flushed. If set to `<code>estimate</code>` or `<code>1</code>`, the default, the oldest modified age will be compared with the maximum age capacity. If it's more than 1/4 of this age, blocks are flushed every second. The number of blocks flushed is determined by the number of modified blocks, the LSN progress speed and the average age of all modified blocks. It's therefore independent of the [innodb_io_capacity](#innodb_io_capacity) for the 1-second loop, but not entirely so for the 10-second loop. If set to `<code>keep_average</code>` or `<code>2</code>`, designed specifically for SSD cards, a shorter loop cycle is used in an attempt to keep the I/O rate constant. Removed in [MariaDB 10.0](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md)/XtraDB 5.6 and replaced with InnoDB flushing method from MySQL 5.6.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">innodb-adaptive-flushing-method=value</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>enumeration</code>`
* Default Value: `<code>estimate</code>`
* Valid Values: `<code>native</code>` or `<code>0</code>`, `<code>estimate</code>` or `<code>1</code>`, `<code>keep_average</code>` or `<code>2</code>`
* Removed: [MariaDB 10.0](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md) - replaced with InnoDB flushing method from MySQL 5.6



#### `<code>innodb_adaptive_hash_index</code>`


* Description: If set to `<code>1</code>`, the default until [MariaDB 10.5](../../../../release-notes/mariadb-community-server/what-is-mariadb-105.md), the [InnoDB](../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/innodb-upgrade-tests/README.md) hash index is enabled. Based on performance testing ([MDEV-17492](https://jira.mariadb.org/browse/MDEV-17492)), the InnoDB adaptive hash index helps performance in mostly read-only workloads, and could slow down performance in other environments, especially [DROP TABLE](../../sql-statements-and-structure/sql-statements/data-definition/drop/drop-tablespace.md), [TRUNCATE TABLE](../../sql-statements-and-structure/sql-statements/table-statements/truncate-table.md), [ALTER TABLE](../../sql-statements-and-structure/sql-statements/data-definition/alter/alter-tablespace.md), or [DROP INDEX](../../sql-statements-and-structure/sql-statements/data-definition/drop/drop-index.md) operations.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-adaptive-hash-index={0|1}</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>` (>= [MariaDB 10.5](../../../../release-notes/mariadb-community-server/what-is-mariadb-105.md)), `<code>ON</code>` (<= [MariaDB 10.4](../../../../release-notes/mariadb-community-server/what-is-mariadb-104.md))



#### `<code>innodb_adaptive_hash_index_partitions</code>`


* Description: Specifies the number of partitions for use in adaptive searching. If set to `<code>1</code>`, no extra partitions are created. XtraDB-only. From [MariaDB 10.2.6](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1026-release-notes.md) (which uses InnoDB as default instead of XtraDB), this is an alias for [innodb_adaptive_hash_index_parts](#innodb_adaptive_hash_index_parts) to allow for easier upgrades.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">innodb-adaptive-hash-index-partitions=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value: `<code>1</code>`
* Range: `<code>1</code>` to `<code>64</code>`



#### `<code>innodb_adaptive_hash_index_parts</code>`


* Description: Specifies the number of partitions for use in adaptive searching. If set to `<code>1</code>`, no extra partitions are created.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">innodb-adaptive-hash-index-parts=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value: `<code>8</code>`
* Range: `<code>1</code>` to `<code>512</code>`



#### `<code>innodb_adaptive_max_sleep_delay</code>`


* Description: Maximum time in microseconds to automatically adjust the [innodb_thread_sleep_delay](#innodb_thread_sleep_delay) value to, based on the workload. Useful in extremely busy systems with hundreds of thousands of simultaneous connections. `<code>0</code>` disables any limit. Deprecated and ignored from [MariaDB 10.5.5](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1055-release-notes.md).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-adaptive-max-sleep-delay=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value:

  * `<code>0</code>` (>= [MariaDB 10.5.5](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1055-release-notes.md))
  * `<code>150000</code>` (<= [MariaDB 10.5.4](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1054-release-notes.md))
* Range: `<code>0</code>` to `<code>1000000</code>`
* Introduced: [MariaDB 10.0](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md)
* Deprecated: [MariaDB 10.5.5](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1055-release-notes.md)
* Removed: [MariaDB 10.6.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-1060-release-notes.md)



#### `<code>innodb_additional_mem_pool_size</code>`


* Description: Size in bytes of the [InnoDB](../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/innodb-upgrade-tests/README.md) memory pool used for storing information about internal data structures. Defaults to 8MB, if your application has many tables and a large structure, and this is exceeded, operating system memory will be allocated and warning messages written to the error log, in which case you should increase this value. Deprecated in [MariaDB 10.0](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md) and removed in [MariaDB 10.2](../../../../release-notes/mariadb-community-server/what-is-mariadb-102.md) along with InnoDB's internal memory allocator.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-additional-mem-pool-size=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value: `<code>8388608</code>`
* Range: `<code>2097152</code>` to `<code>4294967295</code>`
* Deprecated: [MariaDB 10.0](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md)
* Removed: [MariaDB 10.2.2](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1022-release-notes.md)



#### `<code>innodb_alter_copy_bulk</code>`


* Description: Allow bulk insert operation for copy alter operation.
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>ON</code>`
* Introduced: [MariaDB 10.11.9](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-11-series/mariadb-10-11-9-release-notes.md), [MariaDB 11.1.6](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-1-series/mariadb-11-1-6-release-notes.md), [MariaDB 11.2.5](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-2-series/mariadb-11-2-5-release-notes.md), [MariaDB 11.4.3](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-4-series/mariadb-11-4-3-release-notes.md), [MariaDB 11.5.2](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-5-rolling-releases/mariadb-11-5-2-release-notes.md), [MariaDB 11.6.1](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-6-rolling-releases/mariadb-11-6-1-release-notes.md)



#### `<code>innodb_api_bk_commit_interval</code>`


* Description: Time in seconds between auto-commits for idle connections using the InnoDB memcached interface (not implemented in MariaDB).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-api-bk-commit-interval=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>5</code>`
* Range: `<code>1</code>` to `<code>1073741824</code>`
* Introduced: [MariaDB 10.0](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md)
* Removed: [MariaDB 10.2.4](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1024-release-notes.md)



#### `<code>innodb_api_disable_rowlock</code>`


* Description: For use with MySQL's memcached (not implemented in MariaDB)
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-api-disable-rowlock={0|1}</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`
* Introduced: [MariaDB 10.0](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md)
* Removed: [MariaDB 10.2.4](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1024-release-notes.md)



#### `<code>innodb_api_enable_binlog</code>`


* Description: For use with MySQL's memcached (not implemented in MariaDB)
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-api-enable-binlog={0|1}</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`
* Introduced: [MariaDB 10.0](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md)
* Removed: [MariaDB 10.2.4](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1024-release-notes.md)



#### `<code>innodb_api_enable_mdl</code>`


* Description: For use with MySQL's memcached (not implemented in MariaDB)
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-api-enable-mdl={0|1}</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`
* Introduced: [MariaDB 10.0](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md)
* Removed: [MariaDB 10.2.4](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1024-release-notes.md)



#### `<code>innodb_api_trx_level</code>`


* Description: For use with MySQL's memcached (not implemented in MariaDB)
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-api-trx-level=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>0</code>`
* Introduced: [MariaDB 10.0](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md)
* Removed: [MariaDB 10.2.4](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1024-release-notes.md)



#### `<code>innodb_auto_lru_dump</code>`


* Description: Renamed [innodb_buffer_pool_restore_at_startup](#innodb_buffer_pool_restore_at_startup) since XtraDB 5.5.10-20.1, which was in turn replaced by [innodb_buffer_pool_load_at_startup](#innodb_buffer_pool_load_at_startup) in [MariaDB 10.0](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-auto-lru-dump=#</code>`
* Removed: XtraDB 5.5.10-20.1



#### `<code>innodb_autoextend_increment</code>`


* Description: Size in MB to increment an auto-extending shared tablespace file when it becomes full. If [innodb_file_per_table](#innodb_file_per_table) was set to `<code>1</code>`, this setting does not apply to the resulting per-table tablespace files, which are automatically extended in their own way.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-autoextend-increment=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>64</code>` (from [MariaDB 10.0](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md)) `<code>8</code>` (before [MariaDB 10.0](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md)),
* Range: `<code>1</code>` to `<code>1000</code>`



#### `<code>innodb_autoinc_lock_mode</code>`


* Description: The lock mode that is used when generating `<code>[AUTO_INCREMENT](auto_increment-handling-in-innodb.md)</code>` values for InnoDB tables. 

  * Valid values are:

    * `<code>0</code>` is the traditional lock mode.
    * `<code>1</code>` is the consecutive lock mode.
    * `<code>2</code>` is the interleaved lock mode.
  * In order to use [Galera Cluster](../../sql-statements-and-structure/sql-statements/built-in-functions/special-functions/galera-functions/README.md), the lock mode needs to be set to `<code>2</code>`.
  * See [AUTO_INCREMENT Handling in InnoDB: AUTO_INCREMENT Lock Modes](auto_increment-handling-in-innodb.md) for more information.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-autoinc-lock-mode=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value: `<code>1</code>`
* Range: `<code>0</code>` to `<code>2</code>`



#### `<code>innodb_background_scrub_data_check_interval</code>`


* Description: Check if spaces needs scrubbing every [innodb_background_scrub_data_check_interval](#innodb_background_scrub_data_check_interval) seconds. See [Data Scrubbing](innodb-data-scrubbing.md). Deprecated and ignored from [MariaDB 10.5.2](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1052-release-notes.md).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-background-scrub-data-check-interval=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>3600</code>`
* Range: `<code>1</code>` to `<code>4294967295</code>`
* Deprecated: [MariaDB 10.5.2](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1052-release-notes.md)
* Removed: [MariaDB 10.6.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-1060-release-notes.md)



#### `<code>innodb_background_scrub_data_compressed</code>`


* Description: Enable scrubbing of compressed data by background threads (same as encryption_threads). See [Data Scrubbing](innodb-data-scrubbing.md). Deprecated and ignored from [MariaDB 10.5.2](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1052-release-notes.md).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-background-scrub-data-compressed={0|1}</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>0</code>`
* Deprecated: [MariaDB 10.5.2](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1052-release-notes.md)
* Removed: [MariaDB 10.6.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-1060-release-notes.md)



#### `<code>innodb_background_scrub_data_interval</code>`


* Description: Scrub spaces that were last scrubbed longer than this number of seconds ago. See [Data Scrubbing](innodb-data-scrubbing.md). Deprecated and ignored from [MariaDB 10.5.2](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1052-release-notes.md).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-background-scrub-data-interval=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>604800</code>`
* Range: `<code>1</code>` to `<code>4294967295</code>`
* Deprecated: [MariaDB 10.5.2](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1052-release-notes.md)
* Removed: [MariaDB 10.6.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-1060-release-notes.md)



#### `<code>innodb_background_scrub_data_uncompressed</code>`


* Description: Enable scrubbing of uncompressed data by background threads (same as encryption_threads). See [Data Scrubbing](innodb-data-scrubbing.md). Deprecated and ignored from [MariaDB 10.5.2](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1052-release-notes.md).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-background-scrub-data-uncompressed={0|1}</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>0</code>`
* Deprecated: [MariaDB 10.5.2](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1052-release-notes.md)
* Removed: [MariaDB 10.6.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-1060-release-notes.md)



#### `<code>innodb_blocking_buffer_pool_restore</code>`


* Description: If set to `<code>1</code>` (`<code>0</code>` is default), XtraDB will wait until the least-recently used (LRU) dump is completely restored upon restart before reporting back to the server that it has successfully started up. Available with XtraDB only, not InnoDB.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">innodb-blocking-buffer-pool-restore={0|1}</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`
* Removed: [MariaDB 10.0.0](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-1000-release-notes.md)



#### `<code>innodb_buf_dump_status_frequency</code>`


* Description: Determines how often (as a percent) the buffer pool dump status should be printed in the logs. For example, `<code>10</code>` means that the buffer pool dump status is printed when every 10% of the number of buffer pool pages are dumped. The default is `<code>0</code>` (only start and end status is printed).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-buf-dump-status-frequency=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>0</code>`
* Range: `<code>0</code>` to `<code>100</code>`



#### `<code>innodb_buffer_pool_chunk_size</code>`


* Description: Chunk size used for dynamically resizing the [buffer pool](innodb-buffer-pool.md). Note that changing this setting can change the size of the buffer pool. When [large-pages](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#large_pages) is used this value is effectively rounded up to the next multiple of [large-page-size](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#large_page_size). See [Setting Innodb Buffer Pool Size Dynamically](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/setting-innodb-buffer-pool-size-dynamically.md). From [MariaDB 10.8.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-8-series/mariadb-10-8-0-release-notes.md), the variable is autosized based on the [buffer pool size](innodb-buffer-pool.md).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-buffer-pool-chunk-size=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value:

  * `<code>autosize (0)</code>`, resulting in [innodb_buffer_pool_size](#innodb_buffer_pool_size)/64, if [large_pages](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#large_pages) round down to multiple of largest page size, with 1MiB minimum (>= [MariaDB 10.8.1](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-8-series/mariadb-1081-release-notes.md))
  * `<code>134217728</code>` (<= [MariaDB 10.8.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-8-series/mariadb-10-8-0-release-notes.md))
* Range:

  * `<code>0</code>`, as autosize, and then `<code>1048576</code>` to `<code>18446744073709551615</code>` (>= [MariaDB 10.8](../../../../release-notes/mariadb-community-server/what-is-mariadb-108.md))
  * `<code>1048576</code>` to [innodb_buffer_pool_size](#innodb_buffer_pool_size)/[innodb_buffer_pool_instances](#innodb_buffer_pool_instances) (<= [MariaDB 10.7](../../../../release-notes/mariadb-community-server/what-is-mariadb-107.md))
* Block size: `<code>1048576</code>`



#### `<code>innodb_buffer_pool_dump_at_shutdown</code>`


* Description: Whether to record pages cached in the [buffer pool](innodb-buffer-pool.md) on server shutdown, which reduces the length of the warmup the next time the server starts. The related [innodb_buffer_pool_load_at_startup](#innodb_buffer_pool_load_at_startup) specifies whether the buffer pool is automatically warmed up at startup.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-buffer-pool-dump-at-shutdown={0|1}</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>ON</code>`



#### `<code>innodb_buffer_pool_dump_now</code>`


* Description: Immediately records pages stored in the [buffer pool](innodb-buffer-pool.md). The related [innodb_buffer_pool_load_now](#innodb_buffer_pool_load_now) does the reverse, and will immediately warm up the buffer pool.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-buffer-pool-dump-now={0|1}</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`
* Introduced: [MariaDB 10.0](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md)



#### `<code>innodb_buffer_pool_dump_pct</code>`


* Description: Dump only the hottest N% of each [buffer pool](innodb-buffer-pool.md).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-buffer-pool-dump-pct={0|1}</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value:

  * `<code>25</code>`
* Range: `<code>1</code>` to `<code>100</code>`



#### `<code>innodb_buffer_pool_evict</code>`


* Description: Evict pages from the buffer pool. If set to "uncompressed" then all uncompressed pages are evicted from the buffer pool. Variable to be used only for testing. Only exists in DEBUG builds.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-buffer-pool-evict=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>string</code>`
* Default Value: `<code>""</code>`
* Valid Values: "" or "uncompressed"



#### `<code>innodb_buffer_pool_filename</code>`


* Description: The file that holds the [buffer pool](innodb-buffer-pool.md) list of page numbers set by [innodb_buffer_pool_dump_at_shutdown](#innodb_buffer_pool_dump_at_shutdown) and [innodb_buffer_pool_dump_now](#innodb_buffer_pool_dump_now).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-buffer-pool-filename=file</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>string</code>`
* Default Value: `<code>ib_buffer_pool</code>`
* Introduced: [MariaDB 10.0](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md)



#### `<code>innodb_buffer_pool_instances</code>`


* Description: If [innodb_buffer_pool_size](#innodb_buffer_pool_size) is set to more than 1GB, innodb_buffer_pool_instances divides the [InnoDB](../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/innodb-upgrade-tests/README.md) buffer pool into the specified number of instances. The default was 1 in [MariaDB 5.5](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5.md), but for large systems with buffer pools of many gigabytes, many instances could help reduce contention concurrency through [MariaDB 10.2](../../../../release-notes/mariadb-community-server/what-is-mariadb-102.md). The default is 8 in MariaDB 10 (except on Windows 32-bit, where it varies according to [innodb_buffer_pool_size](#innodb_buffer_pool_size), or from [MariaDB 10.2.2](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1022-release-notes.md), where it is set to 1 if [innodb_buffer_pool_size](#innodb_buffer_pool_size) < 1GB). Each instance manages its own data structures and takes an equal portion of the total buffer pool size, so for example if innodb_buffer_pool_size is 4GB and innodb_buffer_pool_instances is set to 4, each instance will be 1GB. Each instance should ideally be at least 1GB in size. 
Starting with [MariaDB 10.3](../../../../release-notes/mariadb-community-server/what-is-mariadb-103.md), performance improvements intended to reduce the overhead of context-switching between buffer pools changed the recommended number of innodb_buffer_pool_instances to one for every 128GB of buffer pool size. Based on these changes, the variable is deprecated and ignored from [MariaDB 10.5.1](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1051-release-notes.md), where the buffer pool runs in a single instance regardless of size.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-buffer-pool-instances=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value: >= [MariaDB 10.0.4](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-1004-release-notes.md): `<code>8</code>`, `<code>1</code>` (>= [MariaDB 10.2.2](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1022-release-notes.md) if [innodb_buffer_pool_size](#innodb_buffer_pool_size) < 1GB), or dependent on [innodb_buffer_pool_size](#innodb_buffer_pool_size) (Windows 32-bit)
* Deprecated: [MariaDB 10.5.1](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1051-release-notes.md)
* Removed: [MariaDB 10.6.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-1060-release-notes.md)



#### `<code>innodb_buffer_pool_load_abort</code>`


* Description: Aborts the process of restoring [buffer pool](innodb-buffer-pool.md) contents started by [innodb_buffer_pool_load_at_startup](#innodb_buffer_pool_load_at_startup) or [innodb_buffer_pool_load_now](#innodb_buffer_pool_load_now).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-buffer-pool-load-abort={0|1}</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`



#### `<code>innodb_buffer_pool_load_at_startup</code>`


* Description: Specifies whether the [buffer pool](innodb-buffer-pool.md) is automatically warmed up when the server starts by loading the pages held earlier. The related [innodb_buffer_pool_dump_at_shutdown](#innodb_buffer_pool_dump_at_shutdown) specifies whether pages are saved at shutdown. If the buffer pool is large and taking a long time to load, increasing [innodb_io_capacity](#innodb_io_capacity) at startup may help.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-buffer-pool-load-at-startup={0|1}</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>boolean</code>`
* Default Value: `<code>ON</code>`



#### `<code>innodb_buffer_pool_load_now</code>`


* Description: Immediately warms up the [buffer pool](innodb-buffer-pool.md) by loading the stored data pages. The related [innodb_buffer_pool_dump_now](#innodb_buffer_pool_dump_now) does the reverse, and immediately records pages stored in the buffer pool.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-buffer-pool-load-now={0|1}</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`



#### `<code>innodb_buffer_pool_load_pages_abort</code>`


* Description: Number of pages during a buffer pool load to process before signaling [innodb_buffer_pool_load_abort=1](#innodb_buffer_pool_load_abort). Debug builds only.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-buffer-pool-load-pages-abort=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>9223372036854775807</code>`
* Range: `<code>1</code>` to `<code>9223372036854775807</code>`



#### `<code>innodb_buffer_pool_populate</code>`


* Description: When set to `<code>1</code>` (`<code>0</code>` is default), XtraDB will preallocate pages in the buffer pool on starting up so that NUMA allocation decisions are made while the buffer cache is still clean. XtraDB only. This option was made ineffective in [MariaDB 10.0.23](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-10023-release-notes.md). Added as a deprecated and ignored option in [MariaDB 10.2.6](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1026-release-notes.md) (which uses InnoDB as default instead of XtraDB) to allow for easier upgrades.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">innodb-buffer-pool-populate={0|1}</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`
* Deprecated: [MariaDB 10.0.23](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-10023-release-notes.md)
* Removed: [MariaDB 10.3.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1030-release-notes.md)



#### `<code>innodb_buffer_pool_restore_at_startup</code>`


* Description: Time in seconds between automatic buffer pool dumps. If set to a non-zero value, XtraDB will also perform an automatic restore of the [buffer pool](innodb-buffer-pool.md) at startup. If set to `<code>0</code>`, automatic dumps are not performed, nor automatic restores on startup. Replaced by [innodb_buffer_pool_load_at_startup](#innodb_buffer_pool_load_at_startup) in [MariaDB 10.0](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">innodb-buffer-pool-restore-at-startup</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>0</code>`
* Range - 32 bit: `<code>0</code>` to `<code>4294967295</code>`
* Range - 64 bit: `<code>0</code>` to `<code>18446744073709547520</code>`
* Removed: [MariaDB 10.0](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md) - replaced by [innodb_buffer_pool_load_at_startup](#innodb_buffer_pool_load_at_startup)



#### `<code>innodb_buffer_pool_shm_checksum</code>`


* Description: Used with Percona's SHM buffer pool patch in XtraDB 5.5. Was shortly deprecated and removed in XtraDB 5.6. XtraDB only.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">innodb-buffer-pool-shm-checksum={0|1}</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>boolean</code>`
* Default Value: `<code>ON</code>`
* Removed: [MariaDB 10.0](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md)



#### `<code>innodb_buffer_pool_shm_key</code>`


* Description: Used with Percona's SHM buffer pool patch in XtraDB 5.5. Later deprecated in XtraDB 5.5, and removed in XtraDB 5.6.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">innodb-buffer-pool-shm-key={0|1}</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>boolean</code>`
* Default Value: `<code>0</code>`
* Removed: [MariaDB 10.0](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md)



#### `<code>innodb_buffer_pool_size</code>`


* Description: InnoDB buffer pool size in bytes. The primary value to adjust on a database server with entirely/primarily [InnoDB](../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/innodb-upgrade-tests/README.md) tables, can be set up to 80% of the total memory in these environments. See the [InnoDB Buffer Pool](innodb-buffer-pool.md) for more on setting this variable, and also [Setting InnoDB Buffer Pool Size Dynamically](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/setting-innodb-buffer-pool-size-dynamically.md) if doing so dynamically.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-buffer-pool-size=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>134217728</code>` (128MiB)
* Range:

  * Minimum: `<code>5242880</code>` (5MiB ) for [InnoDB Page Size](#innodb_page_size) <= 16k otherwise `<code>25165824</code>` (24MiB) for [InnoDB Page Size](#innodb_page_size) > 16k (for versions less than next line)
  * Minimium: `<code>2MiB</code>` [InnoDB Page Size](#innodb_page_size) = 4k, `<code>3MiB</code>` [InnoDB Page Size](#innodb_page_size) = 8k, `<code>5MiB</code>` [InnoDB Page Size](#innodb_page_size) = 16k, `<code>10MiB</code>` [InnoDB Page Size](#innodb_page_size) = 32k, `<code>20MiB</code>` [InnoDB Page Size](#innodb_page_size) = 64k, (>= [MariaDB 10.2.42](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-10242-release-notes.md), >= [MariaDB 10.3.33](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-10333-release-notes.md), >= [MariaDB 10.4.23](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-4-series/mariadb-10423-release-notes.md), >= [MariaDB 10.5.14](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-10514-release-notes.md), >= [MariaDB 10.6.6](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-1066-release-notes.md), >= [MariaDB 10.7.2](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-7-series/mariadb-1072-release-notes.md))
  * Minimum: 1GiB for [innodb_buffer_pool_instances](#innodb_buffer_pool_instances) > 1 (<= [MariaDB 10.7](../../../../release-notes/mariadb-community-server/what-is-mariadb-107.md))
  * Maximium: `<code>9223372036854775807</code>` (8192PB) (all versions)
* Block size: `<code>1048576</code>`



#### `<code>innodb_change_buffer_dump</code>`


* Description: If set, causes the contents of the InnoDB change buffer to be dumped to the server error log at startup. Only available in debug builds.
* Scope: Global
* Dynamic: No
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`
* Introduced: [MariaDB 10.2.28](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-10228-release-notes.md), [MariaDB 10.3.19](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-10319-release-notes.md), [MariaDB 10.4.9](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-4-series/mariadb-1049-release-notes.md)



#### `<code>innodb_change_buffer_max_size</code>`


* Description: Maximum size of the [InnoDB Change Buffer](innodb-change-buffering.md) as a percentage of the total buffer pool. The default is 25%, and this can be increased up to 50% for servers with high write activity, and lowered down to 0 for servers used exclusively for reporting.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-change-buffer-max-size=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>25</code>`
* Range: `<code>0</code>` to `<code>50</code>`
* Introduced: [MariaDB 10.0](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md)
* Deprecated: [MariaDB 10.9.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-9-series/mariadb-1090-release-notes.md)
* Removed: [MariaDB 11.0.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-0-series/mariadb-11-0-0-release-notes.md)



#### `<code>innodb_change_buffering</code>`


* Description: Sets how [InnoDB](../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/innodb-upgrade-tests/README.md) change buffering is performed. See [InnoDB Change Buffering](innodb-change-buffering.md) for details on the settings. Deprecated and ignored from [MariaDB 10.9.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-9-series/mariadb-1090-release-notes.md).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-change-buffering=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>enumeration</code>` (>= [MariaDB 10.3.7](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1037-release-notes.md)), `<code>string</code>` (<= [MariaDB 10.3.6](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1036-release-notes.md))
* Default Value:

  * >= [MariaDB 10.5.15](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-10515-release-notes.md), [MariaDB 10.6.7](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-1067-release-notes.md), [MariaDB 10.7.3](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-7-series/mariadb-1073-release-notes.md), [MariaDB 10.8.2](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-8-series/mariadb-1082-release-notes.md): `<code>none</code>`
  * <= [MariaDB 10.5.14](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-10514-release-notes.md), [MariaDB 10.6.6](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-1066-release-notes.md), [MariaDB 10.7.2](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-7-series/mariadb-1072-release-notes.md), [MariaDB 10.8.1](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-8-series/mariadb-1081-release-notes.md):`<code>all</code>`
* Valid Values: `<code>inserts</code>`, `<code>none</code>`, `<code>deletes</code>`, `<code>purges</code>`, `<code>changes</code>`, `<code>all</code>`
* Deprecated: [MariaDB 10.9.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-9-series/mariadb-1090-release-notes.md)
* Removed: [MariaDB 11.0.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-0-series/mariadb-11-0-0-release-notes.md)



#### `<code>innodb_change_buffering_debug</code>`


* Description: If set to `<code>1</code>`, an [InnoDB Change Buffering](innodb-change-buffering.md) debug flag is set. `<code>1</code>` forces all changes to the change buffer, while `<code>2</code>` causes a crash at merge. `<code>0</code>`, the default, indicates no flag is set. Only available in debug builds.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-change-buffering-debug=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>0</code>`
* Range: `<code>0</code>` to `<code>2</code>`



#### `<code>innodb_checkpoint_age_target</code>`


* Description: The maximum value of the checkpoint age. If set to `<code>0</code>`, has no effect. Removed in [MariaDB 10.0](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md)/XtraDB 5.6 and replaced with InnoDB flushing method from MySQL 5.6.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">innodb-checkpoint-age-target=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>0</code>`
* Range: `<code>0</code>` upwards
* Removed: [MariaDB 10.0](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md) - replaced with InnoDB flushing method from MySQL 5.6.



#### `<code>innodb_checksum_algorithm</code>`


* Description: Specifies how the InnoDB tablespace checksum is generated and verified.

  * `<code>innodb</code>`: Backwards compatible with earlier versions (<= [MariaDB 5.5](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5.md)). Deprecated in [MariaDB 10.3.29](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-10329-release-notes.md), [MariaDB 10.4.19](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-4-series/mariadb-10419-release-notes.md), [MariaDB 10.5.10](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-10510-release-notes.md) and removed in [MariaDB 10.6](../../../../release-notes/mariadb-community-server/what-is-mariadb-106.md). If really needed, data files can still be converted with [innochecksum](../../../clients-and-utilities/innochecksum.md).
  * `<code>crc32</code>`: A newer, faster algorithm, but incompatible with earlier versions. Tablespace blocks will be converted to the new format over time, meaning that a mix of checksums may be present.
  * `<code>full_crc32</code>` and `<code>strict_full_crc32</code>`: From [MariaDB 10.4.3](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-4-series/mariadb-1043-release-notes.md). Permits encryption to be supported over a [SPATIAL INDEX](../../sql-statements-and-structure/geographic-geometric-features/spatial-index.md), which `<code>crc32</code>` does not support. Newly-created data files will carry a flag that indicates that all pages of the file will use a full CRC-32C checksum over the entire page contents (excluding the bytes where the checksum is stored, at the very end of the page). Such files will always use that checksum, no matter what parameter `<code>innodb_checksum_algorithm</code>` is assigned to. Even if `<code>innodb_checksum_algorithm</code>` is modified later, the same checksum will continue to be used. A special flag will be set in the FSP_SPACE_FLAGS in the first data page to indicate the new format of checksum and encryption/page_compressed. ROW_FORMAT=COMPRESSED tables will only use the old format.
These tables do not support new features, such as larger innodb_page_size or instant ADD/DROP COLUMN. Also cleans up the MariaDB tablespace flags - flags are reserved to store the page_compressed compression algorithm, and to store the compressed payload length, so that checksum can be computed over the compressed (and possibly encrypted) stream and can be validated without decrypting or decompressing the page. In the full_crc32 format, there no longer are separate before-encryption and after-encryption checksums for pages. The single checksum is computed on the page contents that is written to the file.See [MDEV-12026](https://jira.mariadb.org/browse/MDEV-12026) for details.
  * `<code>none</code>`: Writes a constant rather than calculate a checksum. Deprecated in [MariaDB 10.3.29](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-10329-release-notes.md), [MariaDB 10.4.19](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-4-series/mariadb-10419-release-notes.md), [MariaDB 10.5.10](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-10510-release-notes.md) and removed in [MariaDB 10.6](../../../../release-notes/mariadb-community-server/what-is-mariadb-106.md) as was mostly used to disable the original, slow, page checksum for benchmarking purposes.
  * `<code>strict_crc32</code>`, `<code>strict_innodb</code>` and `<code>strict_none</code>`: The options are the same as the regular options, but InnoDB will halt if it comes across a mix of checksum values. These are faster, as both new and old checksum values are not required, but can only be used when setting up tablespaces for the first time.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-checksum-algorithm=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>enumeration</code>`
* Default Value:

  * `<code>full_crc32</code>` (>= [MariaDB 10.5.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1050-release-notes.md))
  * `<code>crc32</code>` (>= [MariaDB 10.2.2](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1022-release-notes.md) to <= [MariaDB 10.4](../../../../release-notes/mariadb-community-server/what-is-mariadb-104.md))
  * `<code>innodb</code>` (<= [MariaDB 10.2.1](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1021-release-notes.md))
* Valid Values:

  * >= [MariaDB 10.6.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-1060-release-notes.md): `<code>crc32</code>`, `<code>full_crc32</code>`, `<code>strict_crc32</code>`, `<code>strict_full_crc32</code>`
  * [MariaDB 10.5](../../../../release-notes/mariadb-community-server/what-is-mariadb-105.md), >= [MariaDB 10.4.3](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-4-series/mariadb-1043-release-notes.md): `<code>innodb</code>`, `<code>crc32</code>`, `<code>full_crc32</code>`, `<code>none</code>`, `<code>strict_innodb</code>`, `<code>strict_crc32</code>`, `<code>strict_none</code>`, `<code>strict_full_crc32</code>`
  * <= [MariaDB 10.4.2](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-4-series/mariadb-1042-release-notes.md): `<code>innodb</code>`, `<code>crc32</code>`, `<code>none</code>`, `<code>strict_innodb</code>`, `<code>strict_crc32</code>`, `<code>strict_none</code>`



#### `<code>innodb_checksums</code>`


* Description: By default, [InnoDB](../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/innodb-upgrade-tests/README.md) performs checksum validation on all pages read from disk, which provides extra fault tolerance. You would usually want this set to `<code>1</code>` in production environments, although setting it to `<code>0</code>` can provide marginal performance improvements. Deprecated and functionality replaced by [innodb_checksum_algorithm](#innodb_checksum_algorithm) in [MariaDB 10.0](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md), and should be removed to avoid conflicts. `<code>ON</code>` is equivalent to `<code class="fixed" style="white-space:pre-wrap">--innodb_checksum_algorithm=innodb</code>` and `<code>OFF</code>` to `<code class="fixed" style="white-space:pre-wrap">--innodb_checksum_algorithm=none</code>`.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-checksums</code>`, `<code class="fixed" style="white-space:pre-wrap">--skip-innodb-checksums</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>boolean</code>`
* Default Value: `<code>ON</code>`
* Deprecated: [MariaDB 10.0](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md)
* Removed: [MariaDB 10.5.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1050-release-notes.md)



#### `<code>innodb_cleaner_lsn_age_factor</code>`


* Description: XtraDB has enhanced page cleaner heuristics, and with these in place, the default InnoDB adaptive flushing may be too aggressive. As a result, a new LSN age factor formula has been introduced, controlled by this variable. The default setting, `<code>high_checkpoint</code>`, uses the new formula, while the alternative, `<code>legacy</code>`, uses the original algorithm. XtraDB only. Added as a deprecated and ignored option in [MariaDB 10.2.6](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1026-release-notes.md) (which uses InnoDB as default instead of XtraDB) to allow for easier upgrades.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-cleaner-lsn-age-factor=value</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>enum</code>`
* Default Value:

  * `<code>deprecated</code>`
* Valid Values:

  * `<code>deprecated</code>`, `<code>high_checkpoint</code>`, `<code>legacy</code>`
* Deprecated: [MariaDB 10.2.6](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1026-release-notes.md)
* Removed: [MariaDB 10.3.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1030-release-notes.md)



#### `<code>innodb_cmp_per_index_enabled</code>`


* Description: If set to `<code>ON</code>` (`<code>OFF</code>` is default), per-index compression statistics are stored in the [INFORMATION_SCHEMA.INNODB_CMP_PER_INDEX](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb-tables-information-schema-innodb_cmp_per_index-an.md) table. These are expensive to record, so this setting should only be changed with care, such as for performance tuning on development or replica servers.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-cmp-per-index-enabled={0|1}</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`
* Introduced: [MariaDB 10.0](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md)



#### `<code>innodb_commit_concurrency</code>`


* Description: Limit to the number of transaction threads that can can commit simultaneously. 0, the default, imposes no limit. While you can change from one positive limit to another at runtime, you cannot set this variable to 0, or change it from 0, while the server is running. Deprecated and ignored from [MariaDB 10.5.5](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1055-release-notes.md).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-commit-concurrency=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>0</code>`
* Range: `<code>0</code>` to `<code>1000</code>`
* Deprecated: [MariaDB 10.5.5](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1055-release-notes.md)
* Removed: [MariaDB 10.6.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-1060-release-notes.md)



#### `<code>innodb_compression_algorithm</code>`


* Description: Compression algorithm used for [InnoDB page compression](innodb-page-compression.md). The supported values are:

  * `<code>none</code>`: Pages are not compressed.
  * `<code>zlib</code>`: Pages are compressed using the bundled `<code>[zlib](https://www.zlib.net/)</code>` compression algorithm.
  * `<code>lz4</code>`: Pages are compressed using the `<code>[lz4](https://code.google.com/p/lz4/)</code>` compression algorithm.
  * `<code>lzo</code>`: Pages are compressed using the `<code>[lzo](https://www.oberhumer.com/opensource/lzo/)</code>` compression algorithm.
  * `<code>lzma</code>`: Pages are compressed using the `<code>[lzma](https://tukaani.org/xz/)</code>` compression algorithm.
  * `<code>bzip2</code>`: Pages are compressed using the `<code>[bzip2](https://www.bzip.org/)</code>` compression algorithm.
  * `<code>snappy</code>`: Pages are compressed using the `<code>[snappy](https://google.github.io/snappy/)</code>` algorithm.
  * On many distributions, MariaDB may not support all page compression algorithms by default. From [MariaDB 10.7](../../../../release-notes/mariadb-community-server/what-is-mariadb-107.md), libraries can be installed as a plugin. See [Compression Plugins](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/optimization-and-tuning-compression/compression-plugins.md).
  * See [InnoDB Page Compression: Configuring the InnoDB Page Compression Algorithm](innodb-page-compression.md#configuring-the-innodb-page-compression-algorithm) for more information.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-compression-algorithm=value</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>enum</code>`
* Default Value: `<code>zlib</code>`
* Valid Values:`<code>none</code>`, `<code>zlib</code>`, `<code>lz4</code>`, `<code>lzo</code>`, `<code>lzma</code>`, `<code>bzip2</code>` or `<code>snappy</code>`



#### `<code>innodb_compression_default</code>`


* Description: Whether or not [InnoDB page compression](innodb-page-compression.md) is enabled by default for new tables.

  * The default value is `<code>OFF</code>`, which means new tables are not compressed.
  * See [InnoDB Page Compression: Enabling InnoDB Page Compression by Default](innodb-page-compression.md#enabling-innodb-page-compression-by-default) for more information.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-compression-default={0|1}</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`



#### `<code>innodb_compression_failure_threshold_pct</code>`


* Description: Specifies the percentage cutoff for expensive compression failures during updates to a table that uses [InnoDB page compression](innodb-page-compression.md), after which free space is added to each new compressed page, dynamically adjusted up to the level set by [innodb_compression_pad_pct_max](#innodb_compression_pad_pct_max). Zero disables checking of compression efficiency and adjusting padding.

  * See [InnoDB Page Compression: Configuring the Failure Threshold and Padding](innodb-page-compression.md#configuring-the-failure-threshold-and-padding) for more information.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-compression-failure-threshold-pct=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>5</code>`
* Range: `<code>0</code>` to `<code>100</code>`
* Introduced: [MariaDB 10.0](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md)



#### `<code>innodb_compression_level</code>`


* Description: Specifies the default level of compression for tables that use [InnoDB page compression](innodb-page-compression.md).

  * Only a subset of InnoDB page compression algorithms support compression levels. If an InnoDB page compression algorithm does not support compression levels, then the compression level value is ignored.
  * The compression level can be set to any value between `<code>1</code>` and `<code>9</code>`. The default compression level is `<code>6</code>`. The range goes from the fastest to the most compact, which means that `<code>1</code>` is the fastest and `<code>9</code>` is the most compact.
  * See [InnoDB Page Compression: Configuring the Default Compression Level](innodb-page-compression.md#configuring-the-default-compression-level) for more information.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-compression-level=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>6</code>`
* Range: `<code>1</code>` to `<code>9</code>`
* Introduced: [MariaDB 10.0](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md)



#### `<code>innodb_compression_pad_pct_max</code>`


* Description: The maximum percentage of reserved free space within each compressed page for tables that use [InnoDB page compression](innodb-page-compression.md). Reserved free space is used when the page's data is reorganized and might be recompressed. Only used when [innodb_compression_failure_threshold_pct](#innodb_compression_failure_threshold_pct) is not zero, and the rate of compression failures exceeds its setting.

  * See [InnoDB Page Compression: Configuring the Failure Threshold and Padding](innodb-page-compression.md#configuring-the-failure-threshold-and-padding) for more information.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-compression-pad-pct-max=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>50</code>`
* Range: `<code>0</code>` to `<code>75</code>`
* Introduced: [MariaDB 10.0](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md)



#### `<code>innodb_concurrency_tickets</code>`


* Description: Number of times a newly-entered thread can enter and leave [InnoDB](../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/innodb-upgrade-tests/README.md) until it is again subject to the limitations of [innodb_thread_concurrency](#innodb_thread_concurrency) and may possibly be queued. Deprecated and ignored from [MariaDB 10.5.5](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1055-release-notes.md).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-concurrency-tickets=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value:

  * `<code>0</code>` (>= [MariaDB 10.5.5](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1055-release-notes.md))
  * `<code>5000</code>` (<= [MariaDB 10.5.4](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1054-release-notes.md))
* Range: `<code>1</code>` to `<code>18446744073709551615</code>`
* Deprecated: [MariaDB 10.5.5](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1055-release-notes.md)
* Removed: [MariaDB 10.6.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-1060-release-notes.md)



#### `<code>innodb_corrupt_table_action</code>`


* Description: What action to perform when a corrupt table is found. XtraDB only.

  * When set to `<code>assert</code>`, the default, XtraDB will intentionally crash the server when it detects corrupted data in a single-table tablespace, with an assertion failure.
  * When set to `<code>warn</code>`, it will pass corruption as corrupt table instead of crashing, and disable all further I/O (except for deletion) on the table file.
  * If set to `<code>salvage</code>`, read access is permitted, but corrupted pages are ignored. [innodb_file_per_table](#innodb_file_per_table) must be enabled for this option. Previously named `<code>innodb_pass_corrupt_table</code>`.
  * Added as a deprecated and ignored option in [MariaDB 10.2.6](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1026-release-notes.md) (which uses InnoDB as default instead of XtraDB) to allow for easier upgrades.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">innodb-corrupt-table-action=value</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>enumeration</code>`
* Default Value:

  * `<code>assert</code>` (<= [MariaDB 10.1](../../../../release-notes/mariadb-community-server/what-is-mariadb-1010.md))
  * `<code>deprecated</code>` (<= [MariaDB 10.2.6](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1026-release-notes.md))
* Valid Values:

  * `<code>deprecated</code>`, `<code>assert</code>`, `<code>warn</code>`, `<code>salvage</code>`
* Deprecated: [MariaDB 10.2.6](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1026-release-notes.md)
* Removed: [MariaDB 10.3.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1030-release-notes.md)



#### `<code>innodb_data_file_buffering</code>`


* Description: Whether to enable the file system cache for data files. Set to `<code>OFF</code>` by default, will be set to `<code>ON</code>` if [innodb_flush_method](#innodb_flush_method) is set to `<code>fsync</code>`, `<code>littlesync</code>`, `<code>nosync</code>`, or (Windows specific) `<code>normal</code>`.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-data-file-buffering={0|1}</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`
* Introduced: [MariaDB 11.0.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-0-series/mariadb-11-0-0-release-notes.md)



#### `<code>innodb_data_file_path</code>`


* Description: Individual [InnoDB](../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/innodb-upgrade-tests/README.md) data files, paths and sizes. The value of [innodb_data_home_dir](#innodb_data_home_dir) is joined to each path specified by innodb_data_file_path to get the full directory path. If innodb_data_home_dir is an empty string, absolute paths can be specified here. A file size is specified (with K for kilobytes, M for megabytes and G for gigabytes). Also whether or not to `<code>autoextend</code>` the data file, and whether or not to `<code>[autoshrink](innodb-tablespaces/innodb-system-tablespaces.md#decreasing-the-size)</code>` on startup may also be specified.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-data-file-path=name</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value: `<code>ibdata1:12M:autoextend</code>` (from [MariaDB 10.0](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md)), `<code>ibdata1:10M:autoextend</code>` (before [MariaDB 10.0](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md))



#### `<code>innodb_data_file_write_through</code>`


* Description: Whether writes to InnoDB data files (including the temporary tablespace) are write through. Set to `<code>OFF</code>` by default, will be set to `<code>ON</code>` if [innodb_flush_method](#innodb_flush_method) is set to `<code>O_DSYNC</code>`. On systems that support FUA it may make sense to enable write-through, to avoid extra system calls.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-data-file-write-through={0|1}</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`
* Introduced: [MariaDB 11.0.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-0-series/mariadb-11-0-0-release-notes.md)



#### `<code>innodb_data_home_dir</code>`


* Description: Directory path for all [InnoDB](../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/innodb-upgrade-tests/README.md) data files in the shared tablespace (assuming [innodb_file_per_table](#innodb_file_per_table) is not enabled). File-specific information can be added in [innodb_data_file_path](#innodb_data_file_path), as well as absolute paths if innodb_data_home_dir is set to an empty string.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-data-home-dir=path</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>directory name</code>`
* Default Value: `<code>The MariaDB data directory</code>`



#### `<code>innodb_deadlock_detect</code>`


* Description: By default, the InnoDB deadlock detector is enabled. If set to off, deadlock detection is disabled and MariaDB will rely on [innodb_lock_wait_timeout](#innodb_lock_wait_timeout) instead. This may be more efficient in systems with high concurrency as deadlock detection can cause a bottleneck when a number of threads have to wait for the same lock.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-deadlock-detect</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>1</code>`



#### `<code>innodb_deadlock_report</code>`


* Description: How to report deadlocks (if [innodb_deadlock_detect=ON](#innodb_deadlock_detect)).

  * `<code>off</code>`: Do not report any details of deadlocks.
  * `<code>basic</code>`: Report transactions and waiting locks.
  * `<code>full</code>`: Default. Report transactions, waiting locks and blocking locks.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-deadlock-report=val</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>enum</code>`
* Default Value: `<code>full</code>`
* Valid Values: `<code>off</code>`, `<code>basic</code>`, `<code>full</code>`
* Introduced: [MariaDB 10.6.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-1060-release-notes.md)



#### `<code>innodb_default_page_encryption_key</code>`


* Description: Encryption key used for page encryption.

  * See [Data-at-Rest Encryption](../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/data-at-rest-encryption-overview.md) and [InnoDB Encryption Keys](../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/innodb-encryption/innodb-encryption-keys.md) for more information.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-default-page-encryption-key=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>1</code>`
* Range: `<code>1</code>` to `<code>255</code>`
* Introduced: [MariaDB 10.1.3](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-3-release-notes.md)
* Removed: [MariaDB 10.1.4](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-4-release-notes.md)



#### `<code>innodb_default_encryption_key_id</code>`


* Description: ID of encryption key used by default to encrypt InnoDB tablespaces.

  * See [Data-at-Rest Encryption](../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/data-at-rest-encryption-overview.md) and [InnoDB Encryption Keys](../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/innodb-encryption/innodb-encryption-keys.md) for more information.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-default-encryption-key-id=#</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>1</code>`
* Range: `<code>1</code>` to `<code>4294967295</code>`



#### `<code>innodb_default_row_format</code>`


* Description: Specifies the default [row format](innodb-row-formats/innodb-row-formats-overview.md) to be used for InnoDB tables. The compressed row format cannot be set as the default.

  * See [InnoDB Row Formats Overview: Default Row Format](innodb-row-formats/innodb-row-formats-overview.md#default-row-format) for more information.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-default-row-format=value</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>enum</code>`
* Default Value: `<code>dynamic</code>`
* Valid Values: `<code>redundant</code>`, `<code>compact</code>` or `<code>dynamic</code>`



#### `<code>innodb_defragment</code>`


* Description: When set to `<code>1</code>` (the default is `<code>0</code>`), InnoDB defragmentation is enabled. When set to FALSE, all existing defragmentation will be paused and new defragmentation commands will fail. Paused defragmentation commands will resume when this variable is set to true again. See [Defragmenting InnoDB Tablespaces](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/optimizing-tables/defragmenting-innodb-tablespaces.md).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-defragment={0|1}</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`
* Deprecated: [MariaDB 11.0.1](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-0-series/mariadb-11-0-1-release-notes.md)
* Removed: [MariaDB 11.1.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-1-series/mariadb-11-1-0-release-notes.md)



#### `<code>innodb_defragment_fill_factor</code>`


* Description:. Indicates how full defragmentation should fill a page. Together with [innodb_defragment_fill_factor_n_recs](#innodb_defragment_fill_factor_n_recs) ensures defragmentation won’t pack the page too full and cause page split on the next insert on every page. The variable indicating more defragmentation gain is the one effective. See [Defragmenting InnoDB Tablespaces](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/optimizing-tables/defragmenting-innodb-tablespaces.md).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-defragment-fill-factor=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>double</code>`
* Default Value: `<code>0.9</code>`
* Range: `<code>0.7</code>` to `<code>1</code>`
* Deprecated: [MariaDB 11.0.1](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-0-series/mariadb-11-0-1-release-notes.md)
* Removed: [MariaDB 11.1.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-1-series/mariadb-11-1-0-release-notes.md)



#### `<code>innodb_defragment_fill_factor_n_recs</code>`


* Description: Number of records of space that defragmentation should leave on the page. This variable, together with [innodb_defragment_fill_factor](#innodb_defragment_fill_factor), is introduced so defragmentation won't pack the page too full and cause page split on the next insert on every page. The variable indicating more defragmentation gain is the one effective. See [Defragmenting InnoDB Tablespaces](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/optimizing-tables/defragmenting-innodb-tablespaces.md).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-defragment-fill-factor-n-recs=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>20</code>`
* Range: `<code>1</code>` to `<code>100</code>`
* Deprecated: [MariaDB 11.0.1](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-0-series/mariadb-11-0-1-release-notes.md)
* Removed: [MariaDB 11.1.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-1-series/mariadb-11-1-0-release-notes.md)



#### `<code>innodb_defragment_frequency</code>`


* Description: Maximum times per second for defragmenting a single index. This controls the number of times the defragmentation thread can request X_LOCK on an index. The defragmentation thread will check whether 1/defragment_frequency (s) has passed since it last worked on this index, and put the index back in the queue if not enough time has passed. The actual frequency can only be lower than this given number. See [Defragmenting InnoDB Tablespaces](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/optimizing-tables/defragmenting-innodb-tablespaces.md).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-defragment-frequency=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>integer</code>`
* Default Value: `<code>40</code>`
* Range: `<code>1</code>` to `<code>1000</code>`
* Deprecated: [MariaDB 11.0.1](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-0-series/mariadb-11-0-1-release-notes.md)
* Removed: [MariaDB 11.1.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-1-series/mariadb-11-1-0-release-notes.md)



#### `<code>innodb_defragment_n_pages</code>`


* Description: Number of pages considered at once when merging multiple pages to defragment. See [Defragmenting InnoDB Tablespaces](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/optimizing-tables/defragmenting-innodb-tablespaces.md).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-defragment-n-pages=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>7</code>`
* Range: `<code>2</code>` to `<code>32</code>`
* Deprecated: [MariaDB 11.0.1](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-0-series/mariadb-11-0-1-release-notes.md)
* Removed: [MariaDB 11.1.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-1-series/mariadb-11-1-0-release-notes.md)



#### `<code>innodb_defragment_stats_accuracy</code>`


* Description: Number of defragment stats changes there are before the stats are written to persistent storage. Defaults to zero, meaning disable defragment stats tracking. See [Defragmenting InnoDB Tablespaces](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/optimizing-tables/defragmenting-innodb-tablespaces.md).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-defragment-stats-accuracy=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>0</code>`
* Range: `<code>0</code>` to `<code>4294967295</code>`
* Deprecated: [MariaDB 11.0.1](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-0-series/mariadb-11-0-1-release-notes.md)
* Removed: [MariaDB 11.1.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-1-series/mariadb-11-1-0-release-notes.md)



#### `<code>innodb_dict_size_limit</code>`


* Description: Size in bytes of a soft limit the memory used by tables in the data dictionary. Once this limit is reached, XtraDB will attempt to remove unused entries. If set to `<code>0</code>`, the default and standard InnoDB behavior, there is no limit to memory usage. Removed in [MariaDB 10.0](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md)/XtraDB 5.6 and replaced by MySQL 5.6's new [table_definition_cache](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#table_definition_cache) implementation.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">innodb-dict-size-limit=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>0</code>`
* Default Value - 32 bit: `<code>2147483648</code>`
* Default Value - 64 bit: `<code>9223372036854775807</code>`
* Removed: [MariaDB 10.0](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md) - replaced by MySQL 5.6's [table_definition_cache](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#table_definition_cache) implementation.



#### `<code>innodb_disable_sort_file_cache</code>`


* Description: If set to `<code>1</code>` (`<code>0</code>` is default), the operating system file system cache for merge-sort temporary files is disabled.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-disable-sort-file-cache={0|1}</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`



#### `<code>innodb_disallow_writes</code>`


* Description: Tell InnoDB to stop any writes to disk.
* Commandline: None
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`
* Removed: [MariaDB 10.3.35](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-10335-release-notes.md), [MariaDB 10.4.25](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-4-series/mariadb-10425-release-notes.md), [MariaDB 10.5.16](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-10516-release-notes.md), [MariaDB 10.6.8](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-1068-release-notes.md), [MariaDB 10.7.4](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-7-series/mariadb-1074-release-notes.md)



#### `<code>innodb_doublewrite</code>`


* Description: If set to `<code>1</code>`, the default, to improve fault tolerance [InnoDB](../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/innodb-upgrade-tests/README.md) first stores data to a [doublewrite buffer](innodb-doublewrite-buffer.md) before writing it to data file. Disabling will provide a marginal peformance improvement.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-doublewrite</code>`, `<code class="fixed" style="white-space:pre-wrap">--skip-innodb-doublewrite</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>boolean</code>`
* Default Value: `<code>ON</code>`



#### `<code>innodb_doublewrite_file</code>`


* Description: The absolute or relative path and filename to a dedicated tablespace for the [doublewrite buffer](innodb-doublewrite-buffer.md). In heavy workloads, the doublewrite buffer can impact heavily on the server, and moving it to a different drive will reduce contention on random reads. Since the doublewrite buffer is mostly sequential writes, a traditional HDD is a better choice than SSD. This Percona XtraDB variable has not been ported to XtraDB 5.6.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">innodb-doublewrite-file=filename</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>filename</code>`
* Default Value: `<code>NULL</code>`
* Removed: [MariaDB 10.0](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md)



#### `<code>innodb_empty_free_list_algorithm</code>`


* Description: XtraDB 5.6.13-61 introduced an algorithm to assist with reducing mutex contention when the buffer pool free list is empty, controlled by this variable. If set to `<code>backoff</code>`, the default until [MariaDB 10.1.24](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10124-release-notes.md), the new algorithm will be used. If set to `<code>legacy</code>`, the original InnoDB algorithm will be used. XtraDB only. Added as a deprecated and ignored option in [MariaDB 10.2.6](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1026-release-notes.md) (which uses InnoDB as default instead of XtraDB) to allow for easier upgrades. See [#1651657](https://bugs.launchpad.net/percona-server/+bug/1651657) for the reasons this was changed back to `<code>legacy</code>` in XtraDB 5.6.36-82.0. When upgrading from 10.0 to 10.1 (>= 10.1.24), for large buffer pools the default will remain `<code>backoff</code>`, while for small ones it will be changed to `<code>legacy</code>`.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">innodb-empty-free-list-algorithm=value</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>enum</code>`
* Default Value:

  * `<code>deprecated</code>`
* Valid Values:

  * `<code>deprecated</code>`, `<code>backoff</code>`, `<code>legacy</code>`
* Deprecated: [MariaDB 10.2.6](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1026-release-notes.md)
* Removed: [MariaDB 10.3.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1030-release-notes.md)



#### `<code>innodb_enable_unsafe_group_commit</code>`


* Description: Unneeded after XtraDB 1.0.5. If set to `<code>0</code>`, the default, InnoDB will keep transactions between the transaction log and [binary log](binary-log-group-commit-and-innodb-flushing-performance.md)s in the same order. Safer, but slower. If set to `<code>1</code>`, transactions can be group-committed, but there is no guarantee of the order being kept, and a small risk of the two logs getting out of sync. In write-intensive environments, can lead to a significant improvement in performance.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-enable-unsafe-group-commit</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>0</code>`
* Range: `<code>0</code>` to `<code>1</code>`
* Removed: Not needed after XtraDB 1.0.5



#### `<code>innodb_encrypt_log</code>`


* Description: Enables encryption of the [InnoDB redo log](innodb-redo-log.md). This also enables encryption of some temporary files created internally by InnoDB, such as those used for merge sorts and row logs.

  * See [Data-at-Rest Encryption](../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/data-at-rest-encryption-overview.md) and [Enabling InnoDB Encryption: Enabling Encryption for the Redo Log](../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/innodb-encryption/innodb-enabling-encryption.md#enabling-encryption-for-the-redo-log) for more information.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-encrypt-log</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`



#### `<code>innodb_encrypt_tables</code>`


* Description: Enables automatic encryption of all InnoDB tablespaces.

  * `<code>OFF</code>` - Disables table encryption for all new and existing tables that have the `<code>[ENCRYPTED](../../sql-statements-and-structure/vectors/create-table-with-vectors.md#encrypted)</code>` table option set to `<code>DEFAULT</code>`.
  * `<code>ON</code>` - Enables table encryption for all new and existing tables that have the `<code>[ENCRYPTED](../../sql-statements-and-structure/vectors/create-table-with-vectors.md#encrypted)</code>` table option set to `<code>DEFAULT</code>`, but allows unencrypted tables to be created.
  * `<code>FORCE</code>` - Enables table encryption for all new and existing tables that have the `<code>[ENCRYPTED](../../sql-statements-and-structure/vectors/create-table-with-vectors.md#encrypted)</code>` table option set to `<code>DEFAULT</code>`, and doesn't allow unencrypted tables to be created (CREATE TABLE ... ENCRYPTED=NO will fail).
  * See [Data-at-Rest Encryption](../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/data-at-rest-encryption-overview.md) and [Enabling InnoDB Encryption: Enabling Encryption for Automatically Encrypted Tablespaces](../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/innodb-encryption/innodb-enabling-encryption.md#enabling-encryption-for-automatically-encrypted-tablespaces) for more information.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-encrypt-tables={0|1}</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`
* Valid Values: `<code>ON</code>`, `<code>OFF</code>`, `<code>FORCE</code>`



#### `<code>innodb_encrypt_temporary_tables</code>`


* Description: Enables automatic encryption of the InnoDB [temporary tablespace](innodb-tablespaces/innodb-temporary-tablespaces.md).

  * See [Data-at-Rest Encryption](../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/data-at-rest-encryption-overview.md) and [InnoDB Enabling Encryption: Enabling Encryption for Temporary Tablespaces](../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/innodb-encryption/innodb-enabling-encryption.md#enabling-encryption-for-temporary-tablespaces) for more information.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-encrypt-temporary-tables={0|1}</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`
* Valid Values: `<code>ON</code>`, `<code>OFF</code>`
* Introduced: [MariaDB 10.2.26](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-10226-release-notes.md), [MariaDB 10.3.17](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-10317-release-notes.md), [MariaDB 10.4.7](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-4-series/mariadb-1047-release-notes.md)



#### `<code>innodb_encryption_rotate_key_age</code>`


* Description: Re-encrypt in background any page having a key older than this number of key versions. When setting up encryption, this variable must be set to a non-zero value. Otherwise, when you enable encryption through `<code>[innodb_encrypt_tables](#innodb_encrypt_tables)</code>` MariaDB won't be able to automatically encrypt any unencrypted tables.

  * See [Data-at-Rest Encryption](../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/data-at-rest-encryption-overview.md) and [InnoDB Encryption Keys: Key Rotation](../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/innodb-encryption/innodb-encryption-keys.md#key-rotation) for more information.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-encryption-rotate-key-age=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>1</code>`
* Range: `<code>0</code>` to `<code>4294967295</code>`



#### `<code>innodb_encryption_rotation_iops</code>`


* Description: Use this many iops for background key rotation operations performed by the background encryption threads.

  * See [Data-at-Rest Encryption](../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/data-at-rest-encryption-overview.md) and [InnoDB Encryption Keys: Key Rotation](../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/innodb-encryption/innodb-encryption-keys.md#key-rotation) for more information.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-encryption-rotation_iops=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>100</code>`
* Range: `<code>0</code>` to `<code>4294967295</code>`



#### `<code>innodb_encryption_threads</code>`


* Description: Number of background encryption threads threads performing background key rotation and [scrubbing](innodb-data-scrubbing.md). When setting up encryption, this variable must be set to a non-zero value. Otherwise, when you enable encryption through [innodb_encrypt_tables](#innodb_encrypt_tables) MariaDB won't be able to automatically encrypt any unencrypted tables. Recommended never be set higher than 255.

  * See [Data-at-Rest Encryption](../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/data-at-rest-encryption-overview.md) and [InnoDB Background Encryption Threads](../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/innodb-encryption/innodb-background-encryption-threads.md) for more information.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-encryption-threads=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>0</code>`
* Range:

  * `<code>0</code>` to `<code>4294967295</code>` (<= [MariaDB 10.1.45](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10145-release-notes.md), [MariaDB 10.2.32](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-10232-release-notes.md), [MariaDB 10.3.23](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-10323-release-notes.md), [MariaDB 10.4.13](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-4-series/mariadb-10413-release-notes.md), [MariaDB 10.5.3](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1053-release-notes.md))
  * `<code>0</code>` to `<code>255</code>` (>= [MariaDB 10.1.46](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10146-release-notes.md), [MariaDB 10.2.33](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-10233-release-notes.md), [MariaDB 10.3.24](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-10324-release-notes.md), [MariaDB 10.4.14](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-4-series/mariadb-10414-release-notes.md), [MariaDB 10.5.4](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1054-release-notes.md))



#### `<code>innodb_extra_rsegments</code>`


* Description: Removed in XtraDB 5.5 and replaced by [innodb_rollback_segments](#innodb_rollback_segments). Usually there is one rollback segment protected by single mutex, a source of contention in high write environments. This option specifies a number of extra user rollback segments. Changing the default will make the data readable by XtraDB only, and is incompatible with InnoDB. After modifying, the server must be slow-shutdown. If there is existing data, it must be dumped before changing, and re-imported after the change has taken effect.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-extra-rsegments=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value: `<code>0</code>`
* Range: `<code>0</code>` to `<code>126</code>`
* Removed: XtraDB 5.5 - replaced by [innodb_rollback_segments](#innodb_rollback_segments)



#### `<code>innodb_extra_undoslots</code>`


* Description: Usually, InnoDB has 1024 undo slots in its rollback segment, so 1024 transactions can run in parallel. New transactions will fail if all slots are used. Setting this variable to `<code>1</code>` expands the available undo slots to 4072. Not recommended unless you get the `<code>Warning: cannot find a free slot for an undo log</code>` error in the error log, as it makes data files unusable for ibbackup, or MariaDB servers not run with this option. See also [undo log](innodb-undo-log.md).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-extra-undoslots={0|1}</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`
* Removed: XtraDB 5.5



#### `<code>innodb_fake_changes</code>`


* Description: From [MariaDB 5.5](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5.md) until [MariaDB 10.1](../../../../release-notes/mariadb-community-server/what-is-mariadb-1010.md), XtraDB-only option that enables the fake changes feature. In [replication](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/README.md), setting up or restarting a replica can cause a replication reads to perform more slowly, as MariaDB is single-threaded and needs to read the data before it can execute the queries. This can be speeded up by prefetching threads to warm the server, replaying the statements and then rolling back at commit. This however has an overhead from locking rows only then to undo changes at rollback. Fake changes attempts to reduce this overhead by reading the rows for INSERT, UPDATE and DELETE statements but not updating them. The rollback is then very fast with little or nothing to do. Added as a deprecated and ignored option in [MariaDB 10.2.6](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1026-release-notes.md) (which uses InnoDB as default instead of XtraDB) to allow for easier upgrades. Not present in [MariaDB 10.3](../../../../release-notes/mariadb-community-server/what-is-mariadb-103.md) and beyond.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-fake-changes={0|1}</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`
* Deprecated: [MariaDB 10.2.6](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1026-release-notes.md)
* Removed: [MariaDB 10.3.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1030-release-notes.md)



#### `<code>innodb_fast_checksum</code>`


* Description: Implements a more CPU efficient XtraDB checksum algorithm, useful for write-heavy loads with high I/O. If set to `<code>1</code>` on a server with tables that have been created with it set to `<code>0</code>`, reads will be slower, so tables should be recreated (dumped and reloaded). XtraDB will fail to start if set to `<code>0</code>` and there are tables created while set to `<code>1</code>`. Replaced with [innodb_checksum_algorithm](#innodb_checksum_algorithm) in [MariaDB 10.0](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md)/XtraDB 5.6.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-fast-checksum={0|1}</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`
* Removed: [MariaDB 10.0](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md)/XtraDB 5.6 - replaced with [innodb_checksum_algorithm](#innodb_checksum_algorithm)



#### `<code>innodb_fast_shutdown</code>`


* Description: The shutdown mode. 

  * `<code>0</code>` - InnoDB performs a slow shutdown, including full purge (before [MariaDB 10.3.6](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1036-release-notes.md), not always, due to [MDEV-13603](https://jira.mariadb.org/browse/MDEV-13603)) and change buffer merge. Can be very slow, even taking hours in extreme cases.
  * `<code>1</code>` - the default, [InnoDB](../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/innodb-upgrade-tests/README.md) performs a fast shutdown, not performing a full purge or an insert buffer merge.
  * `<code>2</code>`, the [InnoDB redo log](innodb-redo-log.md) is flushed and a cold shutdown takes place, similar to a crash. The resulting startup then performs crash recovery. Extremely fast, in cases of emergency, but risks corruption. Not suitable for upgrades between major versions!
  * `<code>3</code>` (from [MariaDB 10.3.6](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1036-release-notes.md)) - active transactions will not be rolled back, but all changed pages will be written to data files. The active transactions will be rolled back by a background thread on a subsequent startup. The fastest option that will not involve [InnoDB redo log](innodb-redo-log.md) apply on subsequent startup. See [MDEV-15832](https://jira.mariadb.org/browse/MDEV-15832).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-fast-shutdown[=#]</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>1</code>`
* Range: `<code>0</code>` to `<code>3</code>` (>= [MariaDB 10.3.6](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1036-release-notes.md)), `<code>0</code>` to `<code>2</code>` (<= [MariaDB 10.3.5](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1035-release-notes.md))



#### `<code>innodb_fatal_semaphore_wait_threshold</code>`


* Description: In MariaDB, the fatal semaphore timeout is configurable. This variable sets the maximum number of seconds for semaphores to time out in InnoDB.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-fatal-semaphore-wait-threshold=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value: `<code>600</code>`
* Range: `<code>1</code>` to `<code>4294967295</code>`



#### `<code>innodb_file_format</code>`


* Description: File format for new [InnoDB](../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/innodb-upgrade-tests/README.md) tables. Can either be `<code>Antelope</code>`, the default and the original format, or `<code>Barracuda</code>`, which supports [compression](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/optimization-and-tuning-compression/compression-plugins.md). Note that this value is also used when a table is re-created with an [ALTER TABLE](../../sql-statements-and-structure/sql-statements/data-definition/alter/alter-tablespace.md) which requires a table copy. See [XtraDB/InnoDB File Format](innodb-file-format.md) for more on the file formats. Removed in 10.3.1 and restored as a deprecated and unused variable in 10.4.3 for compatibility purposes.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-file-format=value</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>string</code>`
* Default Value:

  * `<code>Barracuda</code>`
* Valid Values: `<code>Antelope</code>`, `<code>Barracuda</code>`
* Deprecated: [MariaDB 10.2](../../../../release-notes/mariadb-community-server/what-is-mariadb-102.md)
* Removed: [MariaDB 10.3.1](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1031-release-notes.md)
* Re-introduced: [MariaDB 10.4.3](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-4-series/mariadb-1043-release-notes.md) (for compatibility purposes)
* Removed: [MariaDB 10.6.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-1060-release-notes.md)



#### `<code>innodb_file_format_check</code>`


* Description: If set to `<code>1</code>`, the default, [InnoDB](../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/innodb-upgrade-tests/README.md) checks the shared tablespace file format tag. If this is higher than the current version supported by XtraDB/InnoDB (for example Barracuda when only Antelope is supported), XtraDB/InnoDB will will not start. If it the value is not higher, XtraDB/InnoDB starts correctly and the [innodb_file_format_max](#innodb_file_format_max) value is set to this value. If innodb_file_format_check is set to `<code>0</code>`, no checking is performed. See [XtraDB/InnoDB File Format](innodb-file-format.md) for more on the file formats.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-file-format-check={0|1}</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>boolean</code>`
* Default Value: `<code>ON</code>`
* Deprecated: [MariaDB 10.2](../../../../release-notes/mariadb-community-server/what-is-mariadb-102.md)
* Removed: [MariaDB 10.3.1](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1031-release-notes.md)



#### `<code>innodb_file_format_max</code>`


* Description: The highest [XtraDB/InnoDB](../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/innodb-upgrade-tests/README.md) file format. This is set to the value of the file format tag in the shared tablespace on startup (see [innodb_file_format_check](#innodb_file_format_check)). If the server later creates a higher table format, innodb_file_format_max is set to that value. See [XtraDB/InnoDB File Format](innodb-file-format.md) for more on the file formats.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-file-format-max=value</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>string</code>`
* Default Value: `<code>Antelope</code>`
* Valid Values: `<code>Antelope</code>`, `<code>Barracuda</code>`
* Deprecated: [MariaDB 10.2](../../../../release-notes/mariadb-community-server/what-is-mariadb-102.md)
* Removed: [MariaDB 10.3.1](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1031-release-notes.md)



#### `<code>innodb_file_per_table</code>`


* Description: If set to `<code>ON</code>`, then new [InnoDB](../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/innodb-upgrade-tests/README.md) tables are created with their own [InnoDB file-per-table tablespaces](innodb-tablespaces/innodb-file-per-table-tablespaces.md). If set to `<code>OFF</code>`, then new tables are created in the [InnoDB system tablespace](innodb-tablespaces/innodb-system-tablespaces.md) instead. [Page compression](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/optimization-and-tuning-compression/compression-plugins.md) is only available with file-per-table tablespaces. Note that this value is also used when a table is re-created with an [ALTER TABLE](../../sql-statements-and-structure/sql-statements/data-definition/alter/alter-tablespace.md) which requires a table copy. Deprecated in [MariaDB 11.0](/kb/en/what-is-mariadb-11-0/) as there's no benefit to setting to `<code>OFF</code>`, the original InnoDB default.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-file-per-table</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>ON</code>`
* Deprecated: [MariaDB 11.0.1](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-0-series/mariadb-11-0-1-release-notes.md)



#### `<code>innodb_fill_factor</code>`


* Description: Percentage of B-tree page filled during bulk insert (sorted index build). Used as a hint rather than an absolute value. Setting to `<code>70</code>`, for example, reserves 30% of the space on each B-tree page for the index to grow in future.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-fill-factor=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>100</code>`
* Range: `<code>10</code>` to `<code>100</code>`



#### `<code>innodb_flush_log_at_timeout</code>`


* Description: Interval in seconds to write and flush the [InnoDB redo log](innodb-redo-log.md). Before MariaDB 10, this was fixed at one second, which is still the default, but this can now be changed. It's usually increased to reduce flushing and avoid impacting performance of binary log group commit.
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>1</code>`
* Range: `<code>0</code>` to `<code>2700</code>`



#### `<code>innodb_flush_log_at_trx_commit</code>`


* Description: Set to `<code>1</code>`, along with [sync_binlog=1](../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md) for the greatest level of fault tolerance. The value of [innodb_use_global_flush_log_at_trx_commit](#innodb_use_global_flush_log_at_trx_commit) determines whether this variable can be reset with a SET statement or not.

  * `<code>1</code>` The default, the log buffer is written to the [InnoDB redo log](innodb-redo-log.md) file and a flush to disk performed after each transaction. This is required for full ACID compliance.
  * `<code>0</code>` Nothing is done on commit; rather the log buffer is written and flushed to the [InnoDB redo log](innodb-redo-log.md) once a second. This gives better performance, but a server crash can erase the last second of transactions.
  * `<code>2</code>` The log buffer is written to the [InnoDB redo log](innodb-redo-log.md) after each commit, but flushing takes place every [innodb_flush_log_at_timeout](#innodb_flush_log_at_timeout) seconds (by default once a second). Performance is slightly better, but a OS or power outage can cause the last second's transactions to be lost.
  * `<code>3</code>` Emulates [MariaDB 5.5](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5.md) [group commit](../../../server-management/server-monitoring-logs/binary-log/group-commit-for-the-binary-log.md) (3 syncs per group commit). See [Binlog group commit and innodb_flush_log_at_trx_commit](binary-log-group-commit-and-innodb-flushing-performance.md). This option has not been working correctly since 10.2 and may be removed in future, see [1873](https://github.com/MariaDB/server/pull/1873)
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-flush-log-at-trx-commit[=#]</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>enumeration</code>`
* Default Value: `<code>1</code>`
* Valid Values: `<code>0</code>`, `<code>1</code>`, `<code>2</code>` or `<code>3</code>`



#### `<code>innodb_flush_method</code>`


* Description: [InnoDB](../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/innodb-upgrade-tests/README.md) flushing method. Windows always uses async_unbuffered and this variable then has no effect. On Unix, before [MariaDB 10.6.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-1060-release-notes.md), by default fsync() is used to flush data and logs. Adjusting this variable can give performance improvements, but behavior differs widely on different filesystems, and changing from the default has caused problems in some situations, so test and benchmark carefully before adjusting. In MariaDB, Windows recognises and correctly handles the Unix methods, but if none are specified it uses own default - unbuffered write (analog of O_DIRECT) + syncs (e.g FileFlushBuffers()) for all files.

  * `<code>O_DSYNC</code>` - O_DSYNC is used to open and flush logs, and fsync() to flush the data files.
  * `<code>O_DIRECT</code>` - O_DIRECT or directio(), is used to open data files, and fsync() to flush data and logs. Default on Unix from [MariaDB 10.6.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-1060-release-notes.md).
  * `<code>fsync</code>` - Default on Unix until [MariaDB 10.5](../../../../release-notes/mariadb-community-server/what-is-mariadb-105.md). Can be specified directly, but if the variable is unset on Unix, fsync() will be used by default.
  * `<code>O_DIRECT_NO_FSYNC</code>` - introduced in [MariaDB 10.0](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md). Uses O_DIRECT during flushing I/O, but skips fsync() afterwards. Not suitable for XFS filesystems. Generally not recommended over O_DIRECT, as does not get the benefit of [innodb_use_native_aio=ON](#innodb_use_native_aio).
  * `<code>ALL_O_DIRECT</code>` - introduced in [MariaDB 5.5](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5.md) and available with XtraDB only. Uses O_DIRECT for opening both data and logs and fsync() to flush data but not logs. Use with large InnoDB files only, otherwise may cause a performance degradation. Set [innodb_log_block_size](#innodb_log_block_size) to 4096 on ext4 filesystems. This is the default log block size on ext4 and will avoid unaligned AIO/DIO warnings.
  * `<code>unbuffered</code>` - Windows-only default
  * `<code>async_unbuffered</code>` - Windows-only, alias for `<code>unbuffered</code>`
  * `<code>normal</code>` - Windows-only, alias for `<code>fsync</code>`
  * `<code>littlesync</code>` - for internal testing only
  * `<code>nosync</code>` - for internal testing only
* Deprecated in [MariaDB 11.0](../../../../release-notes/mariadb-community-server/what-is-mariadb-110.md) and replaced by four boolean dynamic variables that can be changed while the server is running: [innodb_log_file_buffering](#innodb_log_file_buffering) (disable O_DIRECT, added by [MDEV-28766](https://jira.mariadb.org/browse/MDEV-28766) in 10.8.4, 10.9.2), [innodb_data_file_buffering](#innodb_data_file_buffering) (disable O_DIRECT on data files), [innodb_log_file_write_through](#innodb_log_file_write_through) (enable O_DSYNC on the log), [innodb_data_file_write_through](#innodb_data_file_write_through) (enable O_DSYNC on persistent data files)From [MariaDB 11.0](../../../../release-notes/mariadb-community-server/what-is-mariadb-110.md), if set to one of the following values, then the values of the four boolean flags will be set as follows:

  * `<code>O_DSYNC</code>`: [innodb_log_file_write_through=ON](#innodb_log_file_write_through), [innodb_data_file_write_through=ON](#innodb_data_file_write_through),
[innodb_data_file_buffering=OFF](#innodb_data_file_buffering), and (if supported) [innodb_log_file_buffering=OFF](#innodb_log_file_buffering).
  * `<code>fsync</code>`, `<code>littlesync</code>`, `<code>nosync</code>`, or (Microsoft Windows specific) `<code>normal</code>`: [innodb_log_file_write_through=OFF](#innodb_log_file_write_through), [innodb_data_file_write_through=OFF](#innodb_data_file_write_through), and [innodb_data_file_buffering=ON](#innodb_data_file_buffering).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-flush-method=name</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>enumeration</code>` (>= [MariaDB 10.3.7](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1037-release-notes.md)), `<code>string</code>` (<= [MariaDB 10.3.6](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1036-release-notes.md))
* Default Value:

  * `<code>O_DIRECT</code>` (Unix, >= [MariaDB 10.6.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-1060-release-notes.md))
  * `<code>fsync</code>` (Unix, >= [MariaDB 10.3.7](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1037-release-notes.md), <= [MariaDB 10.5](../../../../release-notes/mariadb-community-server/what-is-mariadb-105.md))
  * Not set (<= [MariaDB 10.3.6](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1036-release-notes.md))
* Valid Values:

  * Unix: `<code>fsync</code>`, `<code>O_DSYNC</code>`, `<code>littlesync</code>`, `<code>nosync</code>`. `<code>O_DIRECT</code>`, `<code>O_DIRECT_NO_FSYNC</code>`
  * Windows: `<code>unbuffered</code>`, `<code>async_unbuffered</code>`, `<code>normal</code>`
* Deprecated: [MariaDB 11.0](../../../../release-notes/mariadb-community-server/what-is-mariadb-110.md)



#### `<code>innodb_flush_neighbor_pages</code>`


* Description: Determines whether, when dirty pages are flushed to the data file, neighboring pages in the data file are flushed at the same time. If set to `<code>none</code>`, the feature is disabled. If set to `<code>area</code>`, the default, the standard InnoDB behavior is used. For each page to be flushed, dirty neighboring pages are flushed too. If there's little head seek delay, such as SSD or large enough write buffer, one of the other two options may be more efficient. If set to `<code>cont</code>`, for each page to be flushed, neighboring contiguous blocks are flushed at the same time. Being contiguous, a sequential I/O is used, unlike the random I/O used in `<code>area</code>`. Replaced by [innodb_flush_neighbors](#innodb_flush_neighbors) in [MariaDB 10.0](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md)/XtraDB 5.6.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">innodb-flush-neighbor-pages=value</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>enumeration</code>`
* Default Value: `<code>area</code>`
* Valid Values: `<code>none</code>` or `<code>0</code>`, `<code>area</code>` or `<code>1</code>`, `<code>cont</code>` or `<code>2</code>`
* Removed: [MariaDB 10.0](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md)/XtraDB 5.6 - replaced by [innodb_flush_neighbors](#innodb_flush_neighbors)



#### `<code>innodb_flush_neighbors</code>`


* Description: Determines whether flushing a page from the [buffer pool](innodb-buffer-pool.md) will flush other dirty pages in the same group of pages (extent). In high write environments, if flushing is not aggressive enough, it can fall behind resulting in higher memory usage, or if flushing is too aggressive, cause excess I/O activity. SSD devices, with low seek times, would be less likely to require dirty neighbor flushing to be set. Since [MariaDB 10.4.4](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-4-series/mariadb-1044-release-notes.md) an attempt is made under Windows and Linux to determine SSD status which was exposed in [information_schema.innodb_tablespaces_scrubbing_table](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb_tablespaces_scrubbing-table.md). This variable is ignored for table spaces that are detected as stored on SSD (and the `<code>0</code>` behavior applies).

  * `<code>1</code>`: The default, flushes contiguous dirty pages in the same extent from the buffer pool.
  * `<code>0</code>`: No other dirty pages are flushed.
  * `<code>2</code>`: Flushes dirty pages in the same extent from the buffer pool.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-flush-neighbors=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>enumeration</code>`
* Default Value: `<code>1</code>`
* Valid Values: `<code>0</code>`, `<code>1</code>`, `<code>2</code>`



#### `<code>innodb_flush_sync</code>`


* Description: If set to `<code>ON</code>`, the default, the [innodb_io_capacity](#innodb_io_capacity) setting is ignored for I/O bursts occuring at checkpoints.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-flush-sync={0|1}</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>ON</code>`



#### `<code>innodb_flushing_avg_loops</code>`


* Description: Determines how quickly adaptive flushing will respond to changing workloads. The value is the number of iterations that a previously calculated flushing state snapshot is kept. Increasing the value smooths and slows the rate that the flushing operations change, while decreasing it causes flushing activity to spike quickly in response to workload changes.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-flushing-avg-loops=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>30</code>`
* Range: `<code>1</code>` to `<code>1000</code>`



#### `<code>innodb_force_load_corrupted</code>`


* Description: Set to `<code>0</code>` by default, if set to `<code>1</code>`, [InnoDB](../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/innodb-upgrade-tests/README.md) will be permitted to load tables marked as corrupt. Only use this to recover data you can't recover any other way, or in troubleshooting. Always restore to `<code>0</code>` when the returning to regular use. Given that [MDEV-11412](https://jira.mariadb.org/browse/MDEV-11412) in [MariaDB 10.5.4](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1054-release-notes.md) aims to allow any metadata for a missing or corrupted table to be dropped, and given that [MDEV-17567](https://jira.mariadb.org/browse/MDEV-17567) and [MDEV-25506](https://jira.mariadb.org/browse/MDEV-25506) and related tasks made DDL operations crash-safe, the parameter no longer serves any purpose and was removed in [MariaDB 10.6.6](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-1066-release-notes.md).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-force-load-corrupted</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`
* Removed: [MariaDB 10.6.6](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-1066-release-notes.md)



#### `<code>innodb_force_primary_key</code>`


* Description: If set to `<code>1</code>` (`<code>0</code>` is default) CREATE TABLEs without a primary or unique key where all keyparts are NOT NULL will not be accepted, and will return an error.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-force-primary-key</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`



#### `<code>innodb_force_recovery</code>`


* Description: [InnoDB](../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/innodb-upgrade-tests/README.md) crash recovery mode. `<code>0</code>` is the default. The other modes are for recovery purposes only, and no data can be changed while another mode is active. Some queries relying on indexes are also blocked. See [InnoDB Recovery Modes](innodb-troubleshooting/innodb-recovery-modes.md) for more on mode specifics.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-force-recovery=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>enumeration</code>`
* Default Value: `<code>0</code>`
* Range: `<code>0</code>` to `<code>6</code>`



#### `<code>innodb_foreground_preflush</code>`


* Description: Before XtraDB 5.6.13-61.0, if the checkpoint age is in the sync preflush zone while a thread is writing to the [XtraDB redo log](innodb-redo-log.md), it will try to advance the checkpoint by issuing a flush list flush batch if this is not already being done. XtraDB has enhanced page cleaner tuning, and may already be performing furious flushing, resulting in the flush simply adding unneeded mutex pressure. Instead, the thread now waits for the flushes to finish, and then has two options, controlled by this variable. XtraDB only. Added as a deprecated and ignored option in [MariaDB 10.2.6](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1026-release-notes.md) (which uses InnoDB as default instead of XtraDB) to allow for easier upgrades.

  * `<code>exponential_backoff</code>` - thread sleeps while it waits for the flush list flush to occur. The sleep time randomly progressively increases, periodically reset to avoid runaway sleeps.
  * `<code>sync_preflush</code>` - thread issues a flush list batch, and waits for it to complete. This is the same as is used when the page cleaner thread is not running.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">innodb-foreground-preflush=value</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>enum</code>`
* Default Value:

  * `<code>deprecated</code>`
* Valid Values:

  * `<code>deprecated</code>`, `<code>exponential_backoff</code>`, `<code>sync_preflush</code>`
* Deprecated: [MariaDB 10.2.6](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1026-release-notes.md)
* Removed: [MariaDB 10.3.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1030-release-notes.md)



#### `<code>innodb_ft_aux_table</code>`


* Description: Diagnostic variable intended only to be set at runtime. It specifies the qualified name (for example `<code>test/ft_innodb</code>`) of an InnoDB table that has a [FULLTEXT index](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/optimization-and-indexes/full-text-indexes/README.md), and after being set the INFORMATION_SCHEMA tables [INNODB_FT_INDEX_TABLE](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb_ft_index_table-table.md), [INNODB_FT_INDEX_CACHE](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb_ft_index_cache-table.md), INNODB_FT_CONFIG, [INNODB_FT_DELETED](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb_ft_deleted-table.md), and [INNODB_FT_BEING_DELETED](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb_ft_being_deleted-table.md) will contain search index information for the specified table.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-ft-aux-table=value</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>string</code>`



#### `<code>innodb_ft_cache_size</code>`


* Description: Cache size available for a parsed document while creating an InnoDB [FULLTEXT index](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/optimization-and-indexes/full-text-indexes/README.md).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-ft-cache-size=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value: `<code>8000000</code>`



#### `<code>innodb_ft_enable_diag_print</code>`


* Description: If set to `<code>1</code>`, additional [full-text](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/optimization-and-indexes/full-text-indexes/README.md) search diagnostic output is enabled.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-ft-enable-diag-print={0|1}</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`



#### `<code>innodb_ft_enable_stopword</code>`


* Description: If set to `<code>1</code>`, the default, a set of [stopwords](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/optimization-and-indexes/full-text-indexes/full-text-index-stopwords.md) is associated with an InnoDB [FULLTEXT index](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/optimization-and-indexes/full-text-indexes/README.md) when it is created. The stopword list comes from the table set by the session variable [innodb_ft_user_stopword_table](#innodb_ft_user_stopword_table), if set, otherwise the global variable [innodb_ft_server_stopword_table](#innodb_ft_server_stopword_table), if that is set, or the [built-in list](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/optimization-and-indexes/full-text-indexes/full-text-index-stopwords.md) if neither variable is set.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-ft-enable-stopword={0|1}</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>ON</code>`



#### `<code>innodb_ft_max_token_size</code>`


* Description: Maximum length of words stored in an InnoDB [FULLTEXT index](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/optimization-and-indexes/full-text-indexes/README.md). A larger limit will increase the size of the index, slowing down queries, but permit longer words to be searched for. In most normal situations, longer words are unlikely search terms.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-ft-max-token-size=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value: `<code>84</code>`
* Range: `<code>10</code>` to `<code>84</code>`



#### `<code>innodb_ft_min_token_size</code>`


* Description: Minimum length of words stored in an InnoDB [FULLTEXT index](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/optimization-and-indexes/full-text-indexes/README.md). A smaller limit will increase the size of the index, slowing down queries, but permit shorter words to be searched for. For data stored in a Chinese, Japanese or Korean [character set](../../data-types/string-data-types/character-sets/README.md), a value of 1 should be specified to preserve functionality.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-ft-min-token-size=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value: `<code>3</code>`
* Range: `<code>0</code>` to `<code>16</code>`



#### `<code>innodb_ft_num_word_optimize</code>`


* Description: Number of words processed during each [OPTIMIZE TABLE](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/optimizing-tables/optimize-table.md) on an InnoDB [FULLTEXT index](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/optimization-and-indexes/full-text-indexes/README.md). To ensure all changes are incorporated, multiple OPTIMIZE TABLE statements could be run in case of a substantial change to the index.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-ft-num-word-optimize=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>2000</code>`
* Range: `<code>1000</code>` to `<code>10000</code>`



#### `<code>innodb_ft_result_cache_limit</code>`


* Description: Limit in bytes of the InnoDB [FULLTEXT index](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/optimization-and-indexes/full-text-indexes/README.md) query result cache per fulltext query. The latter stages of the full-text search are handled in memory, and limiting this prevents excess memory usage. If the limit is exceeded, the query returns an error.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-ft-result-cache-limit=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>2000000000</code>`
* Range: `<code>1000000</code>` to `<code>18446744073709551615</code>`



#### `<code>innodb_ft_server_stopword_table</code>`


* Description: Table name containing a list of stopwords to ignore when creating an InnoDB [FULLTEXT index](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/optimization-and-indexes/full-text-indexes/README.md), in the format db_name/table_name. The specified table must exist before this option is set, and must be an InnoDB table with a single column, a [VARCHAR](../../data-types/string-data-types/varchar.md) named VALUE. See also [innodb_ft_enable_stopword](#innodb_ft_enable_stopword).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-ft-server-stopword-table=db_name/table_name</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>string</code>`
* Default Value: Empty



#### `<code>innodb_ft_sort_pll_degree</code>`


* Description: Number of parallel threads used when building an InnoDB [FULLTEXT index](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/optimization-and-indexes/full-text-indexes/README.md). See also [innodb_sort_buffer_size](#innodb_sort_buffer_size).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-ft-sort-pll-degree=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value: `<code>2</code>`
* Range: `<code>1</code>` to `<code>32</code>`



#### `<code>innodb_ft_total_cache_size</code>`


* Description:Total memory allocated for the cache for all InnoDB [FULLTEXT index](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/optimization-and-indexes/full-text-indexes/README.md) tables. A force sync is triggered if this limit is exceeded.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-ft-total-cache-size=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value: `<code>640000000</code>`
* Range: `<code>32000000</code>` to `<code>1600000000</code>`
* Introduced: [MariaDB 10.0.9](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-1009-release-notes.md)



#### `<code>innodb_ft_user_stopword_table</code>`


* Description: Table name containing a list of stopwords to ignore when creating an InnoDB [FULLTEXT index](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/optimization-and-indexes/full-text-indexes/README.md), in the format db_name/table_name. The specified table must exist before this option is set, and must be an InnoDB table with a single column, a [VARCHAR](../../data-types/string-data-types/varchar.md) named VALUE. See also [innodb_ft_enable_stopword](#innodb_ft_enable_stopword).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-ft-user-stopword-table=db_name/table_name</code>`
* Scope: Session
* Dynamic: Yes
* Data Type: `<code>string</code>`
* Default Value: Empty



#### `<code>innodb_ibuf_accel_rate</code>`


* Description: Allows the insert buffer activity to be adjusted. The following formula is used: [real activity] = [default activity] * (innodb_io_capacity/100) * (innodb_ibuf_accel_rate/100). As `<code>innodb_ibuf_accel_rate</code>` is increased from its default value of `<code>100</code>`, the lowest setting, insert buffer activity is increased. See also [innodb_io_capacity](#innodb_io_capacity). This Percona XtraDB variable has not been ported to XtraDB 5.6.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">innodb-ibuf-accel-rate=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>100</code>`
* Range: `<code>100</code>` to `<code>999999999</code>`
* Removed: [MariaDB 10.0](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md)



#### `<code>innodb_ibuf_active_contract</code>`


* Description: Specifies whether the insert buffer can be processed before it's full. If set to `<code>0</code>`, the standard InnoDB method is used, and the buffer is not processed until it's full. If set to `<code>1</code>`, the default, the insert buffer can be processed before it is full. This Percona XtraDB variable has not been ported to XtraDB 5.6.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">innodb-ibuf-active-contract=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>1</code>`
* Range: `<code>0</code>` to `<code>1</code>`
* Removed: [MariaDB 10.0](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md)



#### `<code>innodb_ibuf_max_size</code>`


* Description: Maximum size in bytes of the insert buffer. Defaults to half the size of the [buffer pool](innodb-buffer-pool.md) so you may want to reduce if you have a very large buffer pool. If set to `<code>0</code>`, the insert buffer is disabled, which will cause all secondary index updates to be performed synchronously, usually at a cost to performance. This Percona XtraDB variable has not been ported to XtraDB 5.6.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">innodb-ibuf-max-size=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value: 1/2 the size of the InnoDB buffer pool
* Range: `<code>0</code>` to 1/2 the size of the InnoDB buffer pool
* Removed: [MariaDB 10.0](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md)



#### `<code>innodb_idle_flush_pct</code>`


* Description: Up to what percentage of dirty pages should be flushed when innodb finds it has spare resources to do so. Has had no effect since merging InnoDB 5.7 from mysql-5.7.9 ([MariaDB 10.2.2](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1022-release-notes.md)). Deprecated in [MariaDB 10.2.37](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-10237-release-notes.md), [MariaDB 10.3.28](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-10328-release-notes.md), [MariaDB 10.4.18](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-4-series/mariadb-10418-release-notes.md) and removed in [MariaDB 10.5.9](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1059-release-notes.md).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-idle-flush-pct=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>100</code>`
* Range: `<code>0</code>` to `<code>100</code>`
* Deprecated: [MariaDB 10.2.37](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-10237-release-notes.md), [MariaDB 10.3.28](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-10328-release-notes.md), [MariaDB 10.4.18](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-4-series/mariadb-10418-release-notes.md)
* Removed: [MariaDB 10.5.9](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1059-release-notes.md)



#### `<code>innodb_immediate_scrub_data_uncompressed</code>`


* Description: Enable scrubbing of data. See [Data Scrubbing](innodb-data-scrubbing.md).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-immediate-scrub-data-uncompressed={0|1}</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`



#### `<code>innodb_import_table_from_xtrabackup</code>`


* Description: If set to `<code>1</code>`, permits importing of .ibd files exported with the [XtraBackup](../../../clients-and-utilities/legacy-clients-and-utilities/backing-up-and-restoring-databases-percona-xtrabackup/percona-xtrabackup-overview.md) --export option. Previously named `<code>innodb_expand_import</code>`. Removed in [MariaDB 10.0](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md)/XtraDB 5.6 and replaced with MySQL 5.6's transportable tablespaces.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">innodb-import-table-from-xtrabackup=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>0</code>`
* Range: `<code>0</code>` to `<code>1</code>`
* Removed: [MariaDB 10.0](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md)



#### `<code>innodb_instant_alter_column_allowed</code>`


* Description:

  * If a table is altered using ALGORITHM=INSTANT, it can force the table to use a non-canonical
format: A hidden metadata record at the start of the clustered index is used to store each column's DEFAULT value. This makes it possible to add new columns that have default values without rebuilding the table. Starting with [MariaDB 10.4](../../../../release-notes/mariadb-community-server/what-is-mariadb-104.md), a BLOB in the hidden metadata record is used to store column mappings. This makes
it possible to drop or reorder columns without rebuilding the table. This also makes it possible to add columns to any position or drop columns from any position in the table without rebuilding the table. If a column is dropped without rebuilding the table, old records will contain garbage in that column's former position, and new records
will be written with NULL values, empty strings, or dummy values.
  * This is generally not a problem. However, there may be cases where
you want to avoid putting a table into this format.
For example, to ensure that future UPDATE operations
after an ADD COLUMN will be performed in-place, to reduce write
amplification. (Instantly added columns are essentially always
variable-length.) Also avoid bugs similar to
[MDEV-19916](https://jira.mariadb.org/browse/MDEV-19916), or to be able to export tables to
older versions of the server.
  * This variable has been introduced as a result, with the following values:
  * `<code>never</code>` (0): Do not allow instant add/drop/reorder,
to maintain format compatibility with MariaDB 10.x and MySQL 5.x.
If the table (or partition) is not in the canonical format, then
any ALTER TABLE (even one that does not involve instant column
operations) will force a table rebuild.
  * `<code>add_last</code>` (1, default in 10.3): Store a hidden metadata record that
allows columns to be appended to the table instantly ([MDEV-11369](https://jira.mariadb.org/browse/MDEV-11369)).
In 10.4 or later, if the table (or partition) is not in this format,
then any ALTER TABLE (even one that does not involve column changes)
will force a table rebuild.
  * `<code>add_drop_reorder</code>` (2, default): From [MariaDB 10.4](../../../../release-notes/mariadb-community-server/what-is-mariadb-104.md) only. Like 'add_last', but allow the
metadata record to store a column map, to support instant
add/drop/reorder of columns.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-instant-alter-column-allowed=value</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>enum</code>`
* Valid Values:

  * <= [MariaDB 10.3](../../../../release-notes/mariadb-community-server/what-is-mariadb-103.md): `<code>never</code>`, `<code>add_last</code>`
  * >= [MariaDB 10.4](../../../../release-notes/mariadb-community-server/what-is-mariadb-104.md): `<code>never</code>`, `<code>add_last</code>`, `<code>add_drop_reorder</code>`
* Default Value:

  * <= [MariaDB 10.3](../../../../release-notes/mariadb-community-server/what-is-mariadb-103.md): `<code>add_last</code>`
  * >= [MariaDB 10.4](../../../../release-notes/mariadb-community-server/what-is-mariadb-104.md): `<code>add_drop_reorder</code>`
* Introduced: [MariaDB 10.3.23](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-10323-release-notes.md), [MariaDB 10.4.13](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-4-series/mariadb-10413-release-notes.md), [MariaDB 10.5.3](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1053-release-notes.md)



#### `<code>innodb_instrument_semaphores</code>`


* Description: Enable semaphore request instrumentation. This could have some effect on performance but allows better information on long semaphore wait problems.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-instrument-semaphores={0|1}</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`
* Deprecated: [MariaDB 10.2.5](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1025-release-notes.md) (treated as if `<code>OFF</code>`)
* Removed: [MariaDB 10.3.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1030-release-notes.md)



#### `<code>innodb_io_capacity</code>`


* Description: Limit on I/O activity for InnoDB background tasks, including merging data from the insert buffer and flushing pages. Should be set to around the number of I/O operations per second that system can handle, based on the type of drive/s being used. You can also set it higher when the server starts to help with the extra workload at that time, and then reduce for normal use. Ideally, opt for a lower setting, as at higher value data is removed from the buffers too quickly, reducing the effectiveness of caching. See also [innodb_flush_sync](#innodb_flush_sync).

  * See [InnoDB Page Flushing: Configuring the InnoDB I/O Capacity](innodb-page-flushing.md#configuring-the-innodb-io-capacity) for more information.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-io-capacity=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>200</code>`
* Range: `<code>100</code>` to `<code>18446744073709551615</code>` (264-1)



#### `<code>innodb_io_capacity_max</code>`


* Description: Upper limit to which InnoDB can extend [innodb_io_capacity](#innodb_io_capacity) in case of emergency. See [InnoDB Page Flushing: Configuring the InnoDB I/O Capacity](innodb-page-flushing.md#configuring-the-innodb-io-capacity) for more information.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-io-capacity-max=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>2000</code>` or twice [innodb_io_capacity](#innodb_io_capacity), whichever is higher.
* Range : `<code>100</code>` to `<code>18446744073709551615</code>` (264-1)



#### `<code>innodb_kill_idle_transaction</code>`


* Description: Time in seconds before killing an idle XtraDB transaction. If set to `<code>0</code>` (the default), the feature is disabled. Used to prevent accidental user locks. XtraDB only. Added as a deprecated and ignored option in [MariaDB 10.2.6](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1026-release-notes.md) (which uses InnoDB as default instead of XtraDB) to allow for easier upgrades.
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>0</code>`
* Range: `<code>0</code>` to `<code>9223372036854775807</code>`
* Deprecated: [MariaDB 10.2.6](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1026-release-notes.md)
* Removed: [MariaDB 10.3.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1030-release-notes.md)



#### `<code>innodb_large_prefix</code>`


* Description: If set to `<code>1</code>`, tables that use specific [row formats](innodb-row-formats/innodb-row-formats-overview.md) are permitted to have index key prefixes up to 3072 bytes (for 16k pages, [smaller otherwise](innodb-limitations.md#page-sizes)). If not set, the limit is 767 bytes.

  * This applies to the `<code>[DYNAMIC](innodb-row-formats/innodb-dynamic-row-format.md)</code>` and `<code>[COMPRESSED](innodb-row-formats/innodb-compressed-row-format.md)</code>` row formats.
  * Removed in 10.3.1 and restored as a deprecated and unused variable in 10.4.3 for compatibility purposes.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-large-prefix</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value:

  * `<code>ON</code>`
* Deprecated: [MariaDB 10.2](../../../../release-notes/mariadb-community-server/what-is-mariadb-102.md)
* Removed: [MariaDB 10.3.1](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1031-release-notes.md)
* Re-introduced: [MariaDB 10.4.3](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-4-series/mariadb-1043-release-notes.md) (for compatibility purposes)
* Removed: [MariaDB 10.6.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-1060-release-notes.md)



#### `<code>innodb_lazy_drop_table</code>`


* Description: Deprecated and removed in XtraDB 5.6. [DROP TABLE](../../sql-statements-and-structure/sql-statements/data-definition/drop/drop-tablespace.md) processing can take a long time when [innodb_file_per_table](#innodb_file_per_table) is set to 1 and there's a large [buffer pool](innodb-buffer-pool.md). If `<code>innodb_lazy_drop_table</code>` is set to `<code>1</code>` (`<code>0</code>` is default), XtraDB attempts to optimize [DROP TABLE](../../sql-statements-and-structure/sql-statements/data-definition/drop/drop-tablespace.md) processing by deferring the dropping of related pages from the [buffer pool](innodb-buffer-pool.md) until there is time, only initially marking them.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">innodb-lazy-drop-table={0|1}</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>0</code>`
* Deprecated: XtraDB 5.5.30-30.2
* Removed: [MariaDB 10.0.0](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-1000-release-notes.md)



#### `<code>innodb_lock_schedule_algorithm</code>`


* Description: Removed in [MariaDB 10.6.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-1060-release-notes.md) due to problems with the VATS implementation ([MDEV-16664](https://jira.mariadb.org/browse/MDEV-16664)). Specifies the algorithm that InnoDB uses to decide which of the waiting transactions should be granted the lock once it has been released. The possible values are: `<code>FCFS</code>` (First-Come-First-Served) where locks are granted in the order they appear in the lock queue and `<code>VATS</code>` (Variance-Aware-Transaction-Scheduling) where locks are granted based on the Eldest-Transaction-First heuristic. Note that `<code>VATS</code>` should not be used with [Galera](../../sql-statements-and-structure/sql-statements/built-in-functions/special-functions/galera-functions/README.md), and InnoDB will refuse to start if `<code>VATS</code>` is used with Galera. It is also not recommended to set to `<code>VATS</code>` even in the general case ([MDEV-16664](https://jira.mariadb.org/browse/MDEV-16664)). From [MariaDB 10.2.12](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-10212-release-notes.md), the value was changed to `<code>FCFS</code>` and a warning produced when using Galera.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-lock-schedule-algorithm=#</code>`
* Scope: Global
* Dynamic: No (>= [MariaDB 10.2.12](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-10212-release-notes.md), [MariaDB 10.1.30](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10130-release-notes.md)), Yes (<= [MariaDB 10.2.11](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-10211-release-notes.md), [MariaDB 10.1.29](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10129-release-notes.md))
* Data Type: `<code>enum</code>`
* Valid Values: `<code>FCFS</code>`, `<code>VATS</code>`
* Default Value: `<code>FCFS</code>` ([MariaDB 10.3.9](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1039-release-notes.md), [MariaDB 10.2.17](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-10217-release-notes.md)), `<code>VATS</code>` ([MariaDB 10.2.3](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1023-release-notes.md)), `<code>FCFS</code>` ([MariaDB 10.1](../../../../release-notes/mariadb-community-server/what-is-mariadb-1010.md))
* Deprecated: [MariaDB 10.5.7](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1057-release-notes.md), [MariaDB 10.4.16](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-4-series/mariadb-10416-release-notes.md), [MariaDB 10.3.26](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-10326-release-notes.md), [MariaDB 10.2.35](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-10235-release-notes.md)
* Removed: [MariaDB 10.6.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-1060-release-notes.md)



#### `<code>innodb_lock_wait_timeout</code>`


* Description: Time in seconds that an InnoDB transaction waits for an InnoDB record lock (or table lock) before giving up with the error `<code class="fixed" style="white-space:pre-wrap">ERROR 1205 (HY000): Lock wait timeout exceeded; try restarting transaction</code>`. When this occurs, the statement (not transaction) is rolled back. The whole transaction can be rolled back if the [innodb_rollback_on_timeout](#innodb_rollback_on_timeout) option is used. Increase this for data warehousing applications or where other long-running operations are common, or decrease for OLTP and other highly interactive applications. This setting does not apply to deadlocks, which InnoDB detects immediately, rolling back a deadlocked transaction. `<code>0</code>` means no wait. See [WAIT and NOWAIT](../../sql-statements-and-structure/sql-statements/transactions/wait-and-nowait.md). Setting to `<code>100000000</code>` or more (from [MariaDB 10.6.3](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-1063-release-notes.md), `<code>100000000</code>` is the maximum) means the timeout is infinite.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-lock-wait-timeout=#</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>INT UNSIGNED</code>` (>= [MariaDB 10.6.3](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-1063-release-notes.md)), `<code>BIGINT UNSIGNED</code>` (<= [MariaDB 10.6.2](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-1062-release-notes.md))
* Default Value: `<code>50</code>`
* Range:

  * `<code>0</code>` to `<code>100000000</code>` (>= [MariaDB 10.6.3](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-1063-release-notes.md))
  * `<code>0</code>` to `<code>1073741824</code>` (>= [MariaDB 10.3](../../../../release-notes/mariadb-community-server/what-is-mariadb-103.md) to <= [MariaDB 10.6.2](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-1062-release-notes.md))



#### `<code>innodb_locking_fake_changes</code>`


* Description: From [MariaDB 5.5](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5.md) to [MariaDB 10.1](../../../../release-notes/mariadb-community-server/what-is-mariadb-1010.md), XtraDB-only option that if set to `<code>OFF</code>`, fake transactions (see [innodb_fake_changes](#innodb_fake_changes)) don't take row locks. This is an experimental feature to attempt to deal with drawbacks in fake changes blocking real locks. It is not safe for use in all environments. Added as a deprecated and ignored option in [MariaDB 10.2.6](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1026-release-notes.md) (which uses InnoDB as default instead of XtraDB) to allow for easier upgrades.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-locking-fake-changes</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>ON</code>`
* Deprecated: [MariaDB 10.2.6](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1026-release-notes.md)
* Removed: [MariaDB 10.3.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1030-release-notes.md)



#### `<code>innodb_locks_unsafe_for_binlog</code>`


* Description: Set to `<code>0</code>` by default, in which case XtraDB/InnoDB uses [gap locking](innodb-lock-modes.md). If set to `<code>1</code>`, gap locking is disabled for searches and index scans. Deprecated in [MariaDB 10.0](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md), and removed in [MariaDB 10.5](../../../../release-notes/mariadb-community-server/what-is-mariadb-105.md), use [READ COMMITTED transaction isolation level](../../sql-statements-and-structure/sql-statements/transactions/set-transaction.md#read-committed) instead.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-locks-unsafe-for-binlog</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`
* Deprecated: [MariaDB 10.0](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md)
* Removed: [MariaDB 10.5.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1050-release-notes.md)



#### `<code>innodb_log_arch_dir</code>`


* Description: The directory for [XtraDB redo log](innodb-redo-log.md) archiving. XtraDB only. Added as a deprecated and ignored option in [MariaDB 10.2.6](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1026-release-notes.md) (which uses InnoDB as default instead of XtraDB) to allow for easier upgrades.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-log-arch-dir=name</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>string</code>`
* Default Value: `<code>./</code>`
* Deprecated: [MariaDB 10.2.6](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1026-release-notes.md)
* Removed: [MariaDB 10.3.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1030-release-notes.md)



#### `<code>innodb_log_arch_expire_sec</code>`


* Description: Time in seconds since the last change after which the archived [XtraDB redo log](innodb-redo-log.md) should be deleted. XtraDB only. Added as a deprecated and ignored option in [MariaDB 10.2.6](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1026-release-notes.md) (which uses InnoDB as default instead of XtraDB) to allow for easier upgrades.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-log-arch-expire-sec=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>0</code>`
* Deprecated: [MariaDB 10.2.6](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1026-release-notes.md)
* Removed: [MariaDB 10.3.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1030-release-notes.md)



#### `<code>innodb_log_archive</code>`


* Description: Whether or not [XtraDB redo log](innodb-redo-log.md) archiving is enabled. XtraDB only. Added as a deprecated and ignored option in [MariaDB 10.2.6](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1026-release-notes.md) (which uses InnoDB as default instead of XtraDB) to allow for easier upgrades.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-log-archive={0|1}</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`
* Deprecated: [MariaDB 10.2.6](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1026-release-notes.md)
* Removed: [MariaDB 10.3.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1030-release-notes.md)



#### `<code>innodb_log_block_size</code>`


* Description: Size in bytes of the [XtraDB redo log](innodb-redo-log.md) records. Generally `<code>512</code>`, the default, or `<code>4096</code>`, are the only two useful values. If the server is restarted and this value is changed, all old log files need to be removed. Should be set to `<code>4096</code>` for SSD cards or if [innodb_flush_method](#innodb_flush_method) is set to `<code>ALL_O_DIRECT</code>` on ext4 filesystems. XtraDB only. Added as a deprecated and ignored option in [MariaDB 10.2.6](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1026-release-notes.md) (which uses InnoDB as default instead of XtraDB) to allow for easier upgrades.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">innodb-log-block-size=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value: `<code>512</code>`
* Deprecated: [MariaDB 10.2.6](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1026-release-notes.md)
* Removed: [MariaDB 10.3.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1030-release-notes.md)



#### `<code>innodb_log_buffer_size</code>`


* Description: Size in bytes of the buffer for writing [InnoDB redo log](innodb-redo-log.md) files to disk. Increasing this means larger transactions can run without needing to perform disk I/O before committing.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-log-buffer-size=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value: `<code>16777216</code>` (16MB)
* Range: `<code>262144</code>` to `<code>2147479552</code>` (256KB to 2GB - 4K) (>= [MariaDB 10.11.8](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-11-series/mariadb-10-11-8-release-notes.md))
* Range: `<code>262144</code>` to `<code>18446744073709551615</code>` (<= [MariaDB 10.11.7](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-11-series/mariadb-10-11-7-release-notes.md)) - limit to the above maximium because this is an operating system limit.
* Block size: `<code>4096</code>`



#### `<code>innodb_log_checksum_algorithm</code>`


* Description: Experimental feature (as of [MariaDB 10.0.9](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-1009-release-notes.md)), this variable specifies how to generate and verify [XtraDB redo log](innodb-redo-log.md) checksums. XtraDB only. Added as a deprecated and ignored option in [MariaDB 10.2.6](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1026-release-notes.md) (which uses InnoDB as default instead of XtraDB) to allow for easier upgrades.

  * `<code>none</code>` - No checksum. A constant value is instead written to logs, and no checksum validation is performed.
  * `<code>innodb</code>` - The default, and the original InnoDB algorithm. This is inefficient, but compatible with all MySQL, MariaDB and Percona versions that don't support other checksum algorithms.
  * `<code>crc32</code>` - CRC32© is used for log block checksums, which also permits recent CPUs to use hardware acceleration (on SSE4.2 x86 machines and Power8 or later) for the checksums.
  * `<code>strict_*</code>` - Whether or not to accept checksums from other algorithms. If strict mode is used, checksums blocks will be considered corrupt if they don't match the specified algorithm. Normally they are considered corrupt only if no other algorithm matches.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">innodb-log-checksum-algorithm=value</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>enum</code>`
* Default Value:

  * `<code>deprecated</code>` (>= [MariaDB 10.2.6](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1026-release-notes.md))
  * `<code>innodb</code>` (<= [MariaDB 10.1](../../../../release-notes/mariadb-community-server/what-is-mariadb-1010.md))
* Valid Values:

  * `<code>deprecated</code>`, `<code>innodb</code>`, `<code>none</code>`, `<code>crc32</code>`, `<code>strict_none</code>`, `<code>strict_innodb</code>`, `<code>strict_crc32</code>` (>= [MariaDB 10.2.6](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1026-release-notes.md))
  * `<code>innodb</code>`, `<code>none</code>`, `<code>crc32</code>`, `<code>strict_none</code>`, `<code>strict_innodb</code>`, `<code>strict_crc32</code>` (<= [MariaDB 10.1](../../../../release-notes/mariadb-community-server/what-is-mariadb-1010.md))
* Deprecated: [MariaDB 10.2.6](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1026-release-notes.md)
* Removed: [MariaDB 10.3.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1030-release-notes.md)



#### `<code>innodb_log_checksums</code>`


* Description: If set to `<code>1</code>`, the CRC32C for Innodb or `<code>innodb_log_checksum_algorithm</code>` for XtraDB algorithm is used for [InnoDB redo log](innodb-redo-log.md) pages. If disabled, the checksum field contents are ignored. From [MariaDB 10.5.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1050-release-notes.md), the variable is deprecated, and checksums are always calculated, as previously, the InnoDB redo log used the slow innodb algorithm, but with hardware or SIMD assisted CRC-32C computation being available, there is no reason to allow checksums to be disabled on the redo log.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">innodb-log-checksums={0|1}</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>ON</code>`
* Deprecated: [MariaDB 10.5.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1050-release-notes.md)
* Removed: [MariaDB 10.6.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-1060-release-notes.md)



#### `<code>innodb_log_compressed_pages</code>`


* Description: Whether or not images of recompressed pages are stored in the [InnoDB redo log](innodb-redo-log.md). Deprecated and ignored from [MariaDB 10.5.3](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1053-release-notes.md).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-log-compressed-pages={0|1}</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value:

  * `<code>ON</code>`
* Deprecated: [MariaDB 10.5.3](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1053-release-notes.md)
* Removed: [MariaDB 10.6.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-1060-release-notes.md)



#### `<code>innodb_log_file_buffering</code>`


* Description: Whether the file system cache for ib_logfile0 is enabled. In [MariaDB 10.8.3](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-8-series/mariadb-1083-release-notes.md), MariaDB disabled the file system cache on the InnoDB write-ahead log file (ib_logfile0) by default on Linux. With [innodb_flush_trx_log_at_commit=2](#innodb_flush_log_at_trx_commit) in particular, writing to the log via the file system cache typically improves throughput, especially on slow storage or at a small number of concurrent transactions. For other values of innodb_flush_log_at_trx_commit, direct writes were observed to be mostly but not always faster. Whether it pays off to disable the file system cache on the log may depend on the type of storage, the workload, and the operating system kernel version. If the server is started up with [innodb_flush_log_at_trx_commit=2](#innodb_flush_log_at_trx_commit), the value will be changed to `<code>ON</code>`. Will be set to `<code>OFF</code>` if [innodb_flush_method](#innodb_flush_method) is set to `<code>O_DSYNC</code>`. On Linux, when the physical block size cannot be determined to be a power of 2 between 64 and 4096 bytes, the file system cache cannot be disabled, and innodb_log_file_buffering=ON cannot be changed. Linux and Windows only.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-log-file-buffering={0|1}</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`
* Introduced: [MariaDB 10.8.4](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-8-series/mariadb-1084-release-notes.md), [MariaDB 10.9.2](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-9-series/mariadb-1092-release-notes.md)



#### `<code>innodb_log_file_mmap</code>`


* Description: Whether ib_logfile0 resides in persistent memory or should initially be memory-mapped. When using the default innodb_log_buffer_size=2m, mariadb-backup --backup would spend a lot of time re-reading and re-parsing the log. For reading the log file during mariadb-backup --backup, it is beneficial to memory-map the entire ib_logfile0 to the address space (typically 48 bits or 256 TiB) and read it from there,
both during --backup and --prepare. OFF by default on most platforms, to avoid aggressive read-ahead of the entire ib_logfile0 in when only a tiny portion would be accessed. On Linux and FreeBSD the default is innodb_log_file_mmap=ON, because those platforms define a specific mmap(2) option for enabling such read-ahead and therefore it can be assumed that the default wouldbe on-demand paging. This parameter will only have impact on the initial InnoDB startup and recovery. Any writes to the log will use regular I/O, except when the ib_logfile0 is stored in a specially configured file system that is backed by persistent memory (Linux "mount -o dax").
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-log-file-mmap{=0|1}</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>boolean</code>`
* Default Value: `<code>ON</code>` (Linux, FreeBSD), `<code>OFF</code>` (Other platforms)
* Introduced: [MariaDB 10.11.10](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-11-series/mariadb-10-11-10-release-notes.md), [MariaDB 11.2.6](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-2-series/mariadb-11-2-6-release-notes.md), [MariaDB 11.4.4](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-4-series/mariadb-11-4-4-release-notes.md), [MariaDB 11.6.2](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-6-rolling-releases/mariadb-11-6-2-release-notes.md), [MariaDB 11.7.1](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-7-rolling-releases/mariadb-11-7-1-release-notes.md)



#### `<code>innodb_log_file_size</code>`


* Description: Size in bytes of each [InnoDB redo log](innodb-redo-log.md) file in the log group. The combined size can be no more than 512GB. Larger values mean less disk I/O due to less flushing checkpoint activity, but also slower recovery from a crash. In [MariaDB 10.5](../../../../release-notes/mariadb-community-server/what-is-mariadb-105.md), crash recovery has been improved and shouldn't run out of memory, so the default has been increased. It can safely be set higher to reduce checkpoint flushing, even larger than [innodb_buffer_pool_size](#innodb_buffer_pool_size).From [MariaDB 10.9](../../../../release-notes/mariadb-community-server/what-is-mariadb-109.md) the variable is dynamic, and the server no longer needs to be restarted for the resizing to take place. Unless the log is located in a persistent memory file system (PMEM), an attempt to [SET GLOBAL](../../../../connectors/mariadb-connector-cpp/setup-for-connector-cpp-examples.md) innodb_log_file_size to less than [innodb_log_buffer_size](#innodb_log_buffer_size) will be refused. Log resizing can be aborted by killing the connection that is executing the SET GLOBAL statement.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-log-file-size=#</code>`
* Scope: Global
* Dynamic: Yes (>= [MariaDB 10.9](../../../../release-notes/mariadb-community-server/what-is-mariadb-109.md)), No (<= [MariaDB 10.8](../../../../release-notes/mariadb-community-server/what-is-mariadb-108.md))
* Data Type: `<code>numeric</code>`
* Default Value: `<code>100663296</code>` (96MB) (>= [MariaDB 10.5](../../../../release-notes/mariadb-community-server/what-is-mariadb-105.md)), `<code>50331648</code>` (48MB) (<= [MariaDB 10.4](../../../../release-notes/mariadb-community-server/what-is-mariadb-104.md))
* Range:

  * >= [MariaDB 10.8.3](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-8-series/mariadb-1083-release-notes.md): `<code>4194304</code>` to `<code>512GB</code>` (4MB to 512GB)
  * <= [MariaDB 10.8.2](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-8-series/mariadb-1082-release-notes.md): `<code>1048576</code>` to `<code>512GB</code>` (1MB to 512GB)
* Block size: `<code>4096</code>`



#### `<code>innodb_log_file_write_through</code>`


* Description: Whether each write to ib_logfile0 is write through (disabling any caching, as in O_SYNC or O_DSYNC). Set to `<code>OFF</code>` by default, will be set to `<code>ON</code>` if [innodb_flush_method](#innodb_flush_method) is set to `<code>O_DSYNC</code>`. On systems that support FUA it may make sense to enable write-through, to avoid extra system calls.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-log-file-write-through={0|1}</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`
* Introduced: [MariaDB 11.0.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-0-series/mariadb-11-0-0-release-notes.md)



#### `<code>innodb_log_files_in_group</code>`


* Description: Number of physical files in the [InnoDB redo log](innodb-redo-log.md). Deprecated and ignored from [MariaDB 10.5.2](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1052-release-notes.md)
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-log-files-in-group=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value: `<code>1</code>` (>= [MariaDB 10.5](../../../../release-notes/mariadb-community-server/what-is-mariadb-105.md)), `<code>2</code>` (<= [MariaDB 10.4](../../../../release-notes/mariadb-community-server/what-is-mariadb-104.md))
* Range: `<code>1</code>` to `<code>100</code>` (>= [MariaDB 10.2.4](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1024-release-notes.md))
* Deprecated: [MariaDB 10.5.2](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1052-release-notes.md)
* Removed: [MariaDB 10.6.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-1060-release-notes.md)



#### `<code>innodb_log_group_home_dir</code>`


* Description: Path to the [InnoDB redo log](innodb-redo-log.md) files. If none is specified, [innodb_log_files_in_group](#innodb_log_files_in_group) files named ib_logfile0 and so on, with a size of [innodb_log_file_size](#innodb_log_file_size) are created in the data directory.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-log-group-home-dir=path</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>directory name</code>`



#### `<code>innodb_log_optimize_ddl</code>`


* Description: Whether [InnoDB redo log](innodb-redo-log.md) activity should be reduced when natively creating indexes or rebuilding tables. Reduced logging requires additional page flushing and interferes with [Mariabackup](../../../server-management/backing-up-and-restoring-databases/mariabackup/mariabackup-and-backup-stage-commands.md). Enabling this may slow down backup and cause delay due to page flushing. Deprecated and ignored from [MariaDB 10.5.1](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1051-release-notes.md). Deprecated (but not ignored) from [MariaDB 10.4.16](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-4-series/mariadb-10416-release-notes.md), [MariaDB 10.3.26](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-10326-release-notes.md) and [MariaDB 10.2.35](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-10235-release-notes.md).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-log-optimize-ddl={0|1}</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value:

  * `<code>OFF</code>` (>= [MariaDB 10.5.1](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1051-release-notes.md), [MariaDB 10.4.16](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-4-series/mariadb-10416-release-notes.md), [MariaDB 10.3.26](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-10326-release-notes.md), [MariaDB 10.2.35](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-10235-release-notes.md))
  * `<code>ON</code>` (<= [MariaDB 10.5.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1050-release-notes.md), [MariaDB 10.4.15](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-4-series/mariadb-10415-release-notes.md), [MariaDB 10.3.25](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-10325-release-notes.md), [MariaDB 10.2.34](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-10234-release-notes.md))
* Introduced: [MariaDB 10.2.17](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-10217-release-notes.md), [MariaDB 10.3.9](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1039-release-notes.md)
* Deprecated: [MariaDB 10.5.1](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1051-release-notes.md), [MariaDB 10.4.16](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-4-series/mariadb-10416-release-notes.md), [MariaDB 10.3.26](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-10326-release-notes.md), [MariaDB 10.2.35](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-10235-release-notes.md)
* Removed: [MariaDB 10.6.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-1060-release-notes.md)



#### `<code>innodb_log_spin_wait_delay</code>`


* Description: Delay between log buffer spin lock polls (0 to use a blocking latch). Specifically, enables a spin lock that will execute that many MY_RELAX_CPU() operations (such as the x86 PAUSE instruction) between successive attempts of acquiring the spin lock. On some hardware with certain workloads (observed on write intensive workloads on NUMA systems), the default setting results in a significant amount of time being spent in native_queued_spin_lock_slowpath() in the Linux kernel, plus context switching between user and kernel address space, in which case changing from the default (for example, setting to `<code>50</code>`), may result in a performance improvement.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-log-spin-wait-delay=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>0</code>`
* Range: `<code>0</code>` to `<code>6000</code>`
* Introduced: [MariaDB 10.11.8](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-11-series/mariadb-10-11-8-release-notes.md), [MariaDB 11.0.6](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-0-series/mariadb-11-0-6-release-notes.md), [MariaDB 11.1.5](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-1-series/mariadb-11-1-5-release-notes.md), [MariaDB 11.2.4](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-2-series/mariadb-11-2-4-release-notes.md), [MariaDB 11.4.2](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-4-series/mariadb-11-4-2-release-notes.md), [MariaDB 11.5.1](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-5-rolling-releases/mariadb-11-5-1-release-notes.md)



#### `<code>innodb_log_write_ahead_size</code>`


* Description: [InnoDB redo log](innodb-redo-log.md) write ahead unit size to avoid read-on-write. Should match the OS cache block IO size. Removed in [MariaDB 10.8](../../../../release-notes/mariadb-community-server/what-is-mariadb-108.md), and instead on Linux and Windows, the physical block size of the underlying storage is detected and used. Reintroduced in [MariaDB 10.11.9](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-11-series/mariadb-10-11-9-release-notes.md) and later versions. On Linux and Windows, the default or the specified innodb_log_write_ahead_size will be automatically adjusted to not be less than the physical block size (if it can be determined).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-log-write-ahead-size=#</code>`
* Scope: Global
* Dynamic: No (>= [MariaDB 10.11.9](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-11-series/mariadb-10-11-9-release-notes.md)), Yes (<= [MariaDB 10.7](../../../../release-notes/mariadb-community-server/what-is-mariadb-107.md))
* Data Type: `<code>numeric</code>`
* Default Value: `<code>512</code>` (>= [MariaDB 10.11.9](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-11-series/mariadb-10-11-9-release-notes.md)), `<code>8192</code>` (<= [MariaDB 10.7](../../../../release-notes/mariadb-community-server/what-is-mariadb-107.md))
* Range:

  * `<code>512</code>` to `<code>4096</code>` (>= [MariaDB 10.11.9](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-11-series/mariadb-10-11-9-release-notes.md))
  * `<code>512</code>` to [innodb_page_size](#innodb_page_size) (<= [MariaDB 10.7](../../../../release-notes/mariadb-community-server/what-is-mariadb-107.md))
* Removed: [MariaDB 10.8](../../../../release-notes/mariadb-community-server/what-is-mariadb-108.md)
* Re-introduced: [MariaDB 10.11.9](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-11-series/mariadb-10-11-9-release-notes.md), [MariaDB 11.1.6](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-1-series/mariadb-11-1-6-release-notes.md), [MariaDB 11.2.5](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-2-series/mariadb-11-2-5-release-notes.md), [MariaDB 11.4.3](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-4-series/mariadb-11-4-3-release-notes.md), [MariaDB 11.5.2](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-5-rolling-releases/mariadb-11-5-2-release-notes.md)



#### `<code>innodb_lru_flush_size</code>`


* Description: Number of pages to flush on LRU eviction. Changes in [MariaDB 10.6.18](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-10-6-18-release-notes.md), [MariaDB 10.11.8](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-11-series/mariadb-10-11-8-release-notes.md), [MariaDB 11.0.6](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-0-series/mariadb-11-0-6-release-notes.md), [MariaDB 11.1.5](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-1-series/mariadb-11-1-5-release-notes.md), [MariaDB 11.2.4](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-2-series/mariadb-11-2-4-release-notes.md) and [MariaDB 11.4.2](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-4-series/mariadb-11-4-2-release-notes.md) made this setting superfluous, and it is no longer used.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-lru-flush-size=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>32</code>`
* Range: `<code>1</code>` to `<code>18446744073709551615</code>`
* Introduced: [MariaDB 10.5.7](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1057-release-notes.md)
* Deprecated: [MariaDB 10.6.20](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-10-6-20-release-notes.md), [MariaDB 10.11.10](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-11-series/mariadb-10-11-10-release-notes.md), [MariaDB 11.2.6](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-2-series/mariadb-11-2-6-release-notes.md) and [MariaDB 11.4.4](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-4-series/mariadb-11-4-4-release-notes.md). [MariaDB 11.6.1](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-6-rolling-releases/mariadb-11-6-1-release-notes.md), [MariaDB 11.7.1](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-7-rolling-releases/mariadb-11-7-1-release-notes.md)



#### `<code>innodb_lru_scan_depth</code>`


* Description: Specifies how far down the buffer pool least-recently used (LRU) list the cleaning thread should look for dirty pages to flush. This process is performed once a second. In an I/O intensive-workload, can be increased if there is spare I/O capacity, or decreased if in a write-intensive workload with little spare I/O capacity.

  * See [InnoDB Page Flushing](innodb-page-flushing.md) for more information.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-lru-scan-depth=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value:

  * `<code>1536</code>` (>= [MariaDB 10.5.7](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1057-release-notes.md))
  * `<code>1024</code>` (<= [MariaDB 10.5.6](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1056-release-notes.md))
* Range - 32bit: `<code>100</code>` to `<code>2<sup>32</sup>-1</code>`
* Range - 64bit: `<code>100</code>` to `<code>2<sup>64</sup>-1</code>`



#### `<code>innodb_max_bitmap_file_size</code>`


* Description: Limit in bytes of the changed page bitmap files. For faster incremental backup with [Xtrabackup](../../../clients-and-utilities/legacy-clients-and-utilities/backing-up-and-restoring-databases-percona-xtrabackup/percona-xtrabackup-overview.md), XtraDB tracks pages with changes written to them according to the [XtraDB redo log](innodb-redo-log.md) and writes the information to special changed page bitmap files. These files are rotated when the server restarts or when this limit is reached. XtraDB only. See also [innodb_track_changed_pages](#innodb_track_changed_pages) and [innodb_max_changed_pages](#innodb_max_changed_pages). 

  * Deprecated and ignored in [MariaDB 10.2.6](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1026-release-notes.md) (which uses InnoDB as default instead of XtraDB) to allow for easier upgrades.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">innodb-max-bitmap-file-size=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>4096</code>` (4KB)
* Range: `<code>4096</code>` (4KB) to `<code>18446744073709551615</code>` (16EB)
* Deprecated: [MariaDB 10.2.6](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1026-release-notes.md)



#### `<code>innodb_max_changed_pages</code>`


* Description: Limit to the number of changed page bitmap files (stored in the [Information Schema INNODB_CHANGED_PAGES table](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb_changed_pages-table.md)). Zero is unlimited. See [innodb_max_bitmap_file_size](#innodb_max_bitmap_file_size) and [innodb_track_changed_pages](#innodb_track_changed_pages). Previously named `<code>innodb_changed_pages_limit</code>`. XtraDB only.

  * Deprecated and ignored in [MariaDB 10.2.6](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1026-release-notes.md) (which uses InnoDB as default instead of XtraDB) to allow for easier upgrades.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">innodb-max-changed-pages=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>1000000</code>`
* Range: `<code>0</code>` to `<code>18446744073709551615</code>`
* Deprecated: [MariaDB 10.2.6](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1026-release-notes.md)



#### `<code>innodb_max_dirty_pages_pct</code>`


* Description: Maximum percentage of unwritten (dirty) pages in the buffer pool.

  * See [InnoDB Page Flushing](innodb-page-flushing.md) for more information.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-max-dirty-pages-pct=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value:

  * `<code>90.000000</code>` (>= [MariaDB 10.5.7](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1057-release-notes.md))
  * `<code>75.000000</code>` (<= [MariaDB 10.5.6](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1056-release-notes.md))
* Range: `<code>0</code>` to `<code>99.999</code>`



#### `<code>innodb_max_dirty_pages_pct_lwm</code>`


* Description: Low water mark percentage of dirty pages that will enable preflushing to lower the dirty page ratio. The value 0 (default) means 'refer to [innodb_max_dirty_pages_pct](#innodb_max_dirty_pages_pct)'. (Note that 0 meant 0 in 10.5.7 to 10.5.8, but was then reverted back to "same as innodb_max_dirty_pages_pct" again in 10.5.9)

  * See [InnoDB Page Flushing](innodb-page-flushing.md) for more information.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-max-dirty-pages-pct-lwm=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value:

  * `<code>0</code>` (>= [MariaDB 10.2.1](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1021-release-notes.md))
  * `<code>0.001</code>` (<= [MariaDB 10.2.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1020-release-notes.md))
* Range: `<code>0</code>` to `<code>99.999</code>`



#### `<code>innodb_max_purge_lag</code>`


* Description: When purge operations are lagging on a busy server, setting innodb_max_purge_lag can help. By default set to `<code>0</code>`, no lag, the figure is used to calculate a time lag for each INSERT, UPDATE, and DELETE when the system is lagging. InnoDB keeps a list of transactions with delete-marked index records due to UPDATE and DELETE statements. The length of this list is `<code>purge_lag</code>`, and the calculation, performed every ten seconds, is as follows: ((purge_lag/innodb_max_purge_lag)×10)–5 microseconds.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-max-purge-lag=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>0</code>`
* Range: `<code>0</code>` to `<code>4294967295</code>`



#### `<code>innodb_max_purge_lag_delay</code>`


* Description: Maximum delay in milliseconds imposed by the [innodb_max_purge_lag](#innodb_max_purge_lag) setting. If set to `<code>0</code>`, the default, there is no maximum.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-max-purge-lag-delay=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>0</code>`



#### `<code>innodb_max_purge_lag_wait</code>`


* Description: Wait until History list length is below the specified limit.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-max-purge-wait=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>4294967295</code>`
* Range: `<code>0</code>` to `<code>4294967295</code>`
* Introduced: [MariaDB 10.5.7](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1057-release-notes.md), [MariaDB 10.4.16](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-4-series/mariadb-10416-release-notes.md), [MariaDB 10.3.26](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-10326-release-notes.md), [MariaDB 10.2.35](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-10235-release-notes.md)



#### `<code>innodb_max_undo_log_size</code>`


* Description: If an undo tablespace is larger than this, it will be marked for truncation if [innodb_undo_log_truncate](#innodb_undo_log_truncate) is set.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-max-undo-log-size=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value:

  * `<code>10485760</code>`
* Range: `<code>10485760</code>` to `<code>18446744073709551615</code>`



#### `<code>innodb_merge_sort_block_size</code>`


* Description: Size in bytes of the block used for merge sorting in fast index creation. Replaced in [MariaDB 10.0](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md)/XtraDB 5.6 by [innodb_sort_buffer_size](#innodb_sort_buffer_size).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">innodb-merge-sort-block-size=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>1048576</code>` (1M)
* Range: `<code>1048576</code>` (1M) to `<code>1073741824</code>` (1G)
* Removed: [MariaDB 10.0](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md) - replaced by [innodb_sort_buffer_size](#innodb_sort_buffer_size)



#### `<code>innodb_mirrored_log_groups</code>`


* Description: Unused. Restored as a deprecated and ignored option in [MariaDB 10.2.6](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1026-release-notes.md) (which uses InnoDB as default instead of XtraDB) to allow for easier upgrades.
* Deprecated: [MariaDB 10.0](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md)
* Removed: [MariaDB 10.2.2](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1022-release-notes.md) - [MariaDB 10.2.5](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1025-release-notes.md)



#### `<code>innodb_mtflush_threads</code>`


* Description: Sets the number of threads to use in Multi-Threaded Flush operations. For more information, see [Fusion-io Multi-threaded Flush](innodb-page-flushing.md).

  * InnoDB's multi-thread flush feature was deprecated in [MariaDB 10.2.9](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1029-release-notes.md) and removed from [MariaDB 10.3.2](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1032-release-notes.md). In later versions of MariaDB, use `<code>[innodb_page_cleaners](#innodb_page_cleaners)</code>` system variable instead.
  * See [InnoDB Page Flushing: Page Flushing with Multi-threaded Flush Threads](innodb-page-flushing.md#page-flushing-with-multi-threaded-flush-threads) for more information.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-mtflush-threads=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value: `<code>8</code>`
* Range: `<code>1</code>` to `<code>64</code>`
* Deprecated: [MariaDB 10.2.9](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1029-release-notes.md)
* Removed: [MariaDB 10.3.2](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1032-release-notes.md)



#### `<code>innodb_monitor_disable</code>`


* Description: Disables the specified counters in the [INFORMATION_SCHEMA.INNODB_METRICS](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb_metrics-table.md) table.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-monitor-disable=string</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>string</code>`



#### `<code>innodb_monitor_enable</code>`


* Description: Enables the specified counters in the [INFORMATION_SCHEMA.INNODB_METRICS](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb_metrics-table.md) table.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-monitor-enable=string</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>string</code>`



#### `<code>innodb_monitor_reset</code>`


* Description: Resets the count value of the specified counters in the [INFORMATION_SCHEMA.INNODB_METRICS](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb_metrics-table.md) table to zero.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-monitor-reset=string</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>string</code>`



#### `<code>innodb_monitor_reset_all</code>`


* Description: Resets all values for the specified counters in the [INFORMATION_SCHEMA.INNODB_METRICS](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb_metrics-table.md) table.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">---innodb-monitor-reset-all=string</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>string</code>`



#### `<code>innodb_numa_interleave</code>`


* Description: Whether or not to use the NUMA interleave memory policy to allocate the [InnoDB buffer pool](innodb-buffer-pool.md). Before [MariaDB 10.2.4](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1024-release-notes.md), required that MariaDB be compiled on a NUMA-enabled Linux system.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">innodb-numa-interleave={0|1}</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`
* Removed: [MariaDB 10.2.23](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-10223-release-notes.md), [MariaDB 10.3.14](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-10314-release-notes.md), [MariaDB 10.4.4](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-4-series/mariadb-1044-release-notes.md)



#### `<code>innodb_old_blocks_pct</code>`


* Description: Percentage of the [buffer pool](innodb-buffer-pool.md) to use for the old block sublist.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-old-blocks-pct=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>37</code>`
* Range: `<code>5</code>` to `<code>95</code>`



#### `<code>innodb_old_blocks_time</code>`


* Description: Time in milliseconds an inserted block must stay in the old sublist after its first access before it can be moved to the new sublist. '0' means "no delay". Setting a non-zero value can help prevent full table scans clogging the [buffer pool](innodb-buffer-pool.md). See also [innodb_old_blocks_pct](#innodb_old_blocks_pct).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-old-blocks-time=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>1000</code>`
* Range: `<code>0</code>` to `<code>2<sup>32</sup>-1</code>`



#### `<code>innodb_online_alter_log_max_size</code>`


* Description: The maximum size for temporary log files during online DDL (data and index structure changes). The temporary log file is used for each table being altered, or index being created, to store data changes to the table while the process is underway. The table is extended by [innodb_sort_buffer_size](#innodb_sort_buffer_size) up to the limit set by this variable. If this limit is exceeded, the online DDL operation fails and all uncommitted changes are rolled back. A lower value reduces the time a table could lock at the end of the operation to apply all the log's changes, but also increases the chance of the online DDL changes failing.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-online-alter-log-max-size=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>134217728</code>`
* Range: `<code>65536</code>` to `<code>2<sup>64</sup>-1</code>`



#### `<code>innodb_open_files</code>`


* Description: Maximum .ibd files MariaDB can have open at the same time. Only applies to systems with multiple XtraDB/InnoDB tablespaces, and is separate to the table cache and [open_files_limit](#open_files_limit). The default, if [innodb_file_per_table](#innodb_file_per_table) is disabled, is 300 or the value of [table_open_cache](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#table_open_cache), whichever is higher. It will also auto-size up to the default value if it is set to a value less than `<code>10</code>`.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-open-files=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value: `<code>autosized</code>`
* Range: `<code>10</code>` to `<code>4294967295</code>`



#### `<code>innodb_optimize_fulltext_only</code>`


* Description: When set to `<code>1</code>` (`<code>0</code>` is default), [OPTIMIZE TABLE](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/optimizing-tables/optimize-table.md) will only process InnoDB [FULLTEXT index](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/optimization-and-indexes/full-text-indexes/README.md) data. Only intended for use during fulltext index maintenance.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-optimize-fulltext-only={0|1}</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`



#### `<code>innodb_page_cleaners</code>`


* Description: Number of page cleaner threads. The default is `<code>4</code>`, but the value will be set to the number of [innodb_buffer_pool_instances](#innodb_buffer_pool_instances) if this is lower. If set to `<code>1</code>`, only a single cleaner thread is used, as was the case until [MariaDB 10.2.1](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1021-release-notes.md). Cleaner threads flush dirty pages from the [buffer pool](innodb-buffer-pool.md), performing flush list and least-recently used (LRU) flushing. Deprecated and ignored from [MariaDB 10.5.1](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1051-release-notes.md), as the original reasons for for splitting the buffer pool have mostly gone away.

  * See [InnoDB Page Flushing: Page Flushing with Multiple InnoDB Page Cleaner Threads](innodb-page-flushing.md#page-flushing-with-multiple-innodb-page-cleaner-threads) for more information.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-page-cleaners=#</code>`
* Scope: Global
* Dynamic: Yes (>= [MariaDB 10.3.3](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1033-release-notes.md)), No (<= [MariaDB 10.3.2](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1032-release-notes.md))
* Data Type: `<code>numeric</code>`
* Default Value: `<code>4</code>` (or set to [innodb_buffer_pool_instances](#innodb_buffer_pool_instances) if lower)
* Range: `<code>1</code>` to `<code>64</code>`
* Deprecated: [MariaDB 10.5.1](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1051-release-notes.md)
* Removed: [MariaDB 10.6.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-1060-release-notes.md)



#### `<code>innodb_page_size</code>`


* Description: Specifies the page size in bytes for all InnoDB tablespaces. The default, `<code>16k</code>`, is suitable for most uses.

  * A smaller InnoDB page size might work more effectively in a situation with many small writes (OLTP), or with SSD storage, which usually has smaller block sizes.
  * A larger InnoDB page size can provide a larger [maximum row size](innodb-row-formats/innodb-row-formats-overview.md#maximum-row-size).
  * InnoDB's page size can be as large as `<code>64k</code>` for tables using the following [row formats](innodb-row-formats/innodb-row-formats-overview.md): [DYNAMIC](innodb-row-formats/innodb-dynamic-row-format.md), [COMPACT](innodb-row-formats/innodb-compact-row-format.md), and [REDUNDANT](innodb-row-formats/innodb-redundant-row-format.md).
  * InnoDB's page size must still be `<code>16k</code>` or less for tables using the [COMPRESSED](innodb-row-formats/innodb-compressed-row-format.md) row format.
  * This system variable's value cannot be changed after the `<code>datadir</code>` has been initialized. InnoDB's page size is set when a MariaDB instance starts, and it remains constant afterwards.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-page-size=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>enumeration</code>`
* Default Value: `<code>16384</code>`
* Valid Values: `<code>4k</code>` or `<code>4096</code>`, `<code>8k</code>` or `<code>8192</code>`, `<code>16k</code>` or `<code>16384</code>`, `<code>32k</code>` and `<code>64k</code>`.



#### `<code>innodb_pass_corrupt_table</code>`


* Removed: XtraDB 5.5 - renamed [innodb_corrupt_table_action](#innodb_corrupt_table_action).



#### `<code>innodb_prefix_index_cluster_optimization</code>`


* Description: Enable prefix optimization to sometimes avoid cluster index lookups. Deprecated and ignored from [MariaDB 10.10](../../../../release-notes/mariadb-community-server/what-is-mariadb-1010.md), as the optimization is now always enabled.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-prefix-index-cluster-optimization={0|1}</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`
* Deprecated: [MariaDB 10.10.1](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-10-series/mariadb-10101-release-notes.md)



#### `<code>innodb_print_all_deadlocks</code>`


* Description: If set to `<code>1</code>` (`<code>0</code>` is default), all InnoDB transaction deadlock information is written to the [error log](../../../server-management/server-monitoring-logs/error-log.md).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-print-all-deadlocks={0|1}</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`



#### `<code>innodb_purge_batch_size</code>`


* Description: Number of [InnoDB undo log](innodb-undo-log.md) pages to purge in one batch from the history list. Together with [innodb_purge_threads](#innodb_purge_threads) has a small effect on tuning.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-purge-batch-size=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value:

  * `<code>127</code>` (>= [MariaDB 10.6.20](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-10-6-20-release-notes.md), [MariaDB 10.11.10](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-11-series/mariadb-10-11-10-release-notes.md), [MariaDB 11.2.6](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-2-series/mariadb-11-2-6-release-notes.md), [MariaDB 11.4.4](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-4-series/mariadb-11-4-4-release-notes.md), [MariaDB 11.6.2](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-6-rolling-releases/mariadb-11-6-2-release-notes.md))
  * `<code>1000</code>` (>= [MariaDB 10.6.16](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-10-6-16-release-notes.md), [MariaDB 10.10.7](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-10-series/mariadb-10-10-7-release-notes.md), [MariaDB 10.11.6](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-11-series/mariadb-10-11-6-release-notes.md), [MariaDB 11.0.4](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-0-series/mariadb-11-0-4-release-notes.md), [MariaDB 11.1.3](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-1-series/mariadb-11-1-3-release-notes.md) [MariaDB 11.2.2](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-2-series/mariadb-11-2-2-release-notes.md))
  * `<code>300</code>` (<= [MariaDB 10.6.15](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-10-6-15-release-notes.md), [MariaDB 10.10.6](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-10-series/mariadb-10-10-6-release-notes.md), [MariaDB 10.11.5](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-11-series/mariadb-10-11-5-release-notes.md), [MariaDB 11.0.3](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-0-series/mariadb-11-0-3-release-notes.md), [MariaDB 11.1.2](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-1-series/mariadb-11-1-2-release-notes.md) [MariaDB 11.2.1](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-2-series/mariadb-11-2-1-release-notes.md))
* Range: `<code>1</code>` to `<code>5000</code>`



#### `<code>innodb_purge_rseg_truncate_frequency</code>`


* Description: Frequency with which undo records are purged. Set by default to every 128 times, reducing this increases the frequency at which rollback segments are freed. See also [innodb_undo_log_truncate](#innodb_undo_log_truncate). The motivation for introducing this in MySQL seems to have been to avoid stalls due to freeing undo log pages or truncating undo log tablespaces. In MariaDB, [innodb_undo_log_truncate=ON](#innodb_undo_log_truncate) should be a much lighter operation because it will not involve any log checkpoint, hence this is deprecated and ignored from [MariaDB 10.6.16](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-10-6-16-release-notes.md), [MariaDB 10.10.7](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-10-series/mariadb-10-10-7-release-notes.md), [MariaDB 10.11.6](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-11-series/mariadb-10-11-6-release-notes.md), [MariaDB 11.0.4](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-0-series/mariadb-11-0-4-release-notes.md), [MariaDB 11.1.3](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-1-series/mariadb-11-1-3-release-notes.md) and [MariaDB 11.2.2](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-2-series/mariadb-11-2-2-release-notes.md). ([MDEV-32050](https://jira.mariadb.org/browse/MDEV-32050))
* Commandline: `<code class="fixed" style="white-space:pre-wrap">-- innodb-purge-rseg-truncate-frequency=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>128</code>`
* Range: `<code>1</code>` to `<code>128</code>`
* Deprecated: [MariaDB 10.6.16](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-10-6-16-release-notes.md), [MariaDB 10.10.7](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-10-series/mariadb-10-10-7-release-notes.md), [MariaDB 10.11.6](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-11-series/mariadb-10-11-6-release-notes.md), [MariaDB 11.0.4](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-0-series/mariadb-11-0-4-release-notes.md), [MariaDB 11.1.3](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-1-series/mariadb-11-1-3-release-notes.md), [MariaDB 11.2.2](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-2-series/mariadb-11-2-2-release-notes.md)



#### `<code>innodb_purge_threads</code>`


* Description: Number of background threads dedicated to InnoDB purge operations. The range is `<code>1</code>` to `<code>32</code>`. At least one background thread is always used. Setting to a value greater than 1 creates that many separate purge threads. This can improve efficiency in some cases, such as when performing DML operations on many tables. See also [innodb_purge_batch_size](#innodb_purge_batch_size).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-purge-threads=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value: `<code>4</code>`
* Range: `<code>1</code>` to `<code>32</code>`



#### `<code>innodb_random_read_ahead</code>`


* Description: Originally, random read-ahead was always set as an optimization technique, but was removed in [MariaDB 5.5](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5.md). `<code>innodb_random_read_ahead</code>` permits it to be re-instated if set to `<code>1</code>` (`<code>0</code>`) is default.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-random-read-ahead={0|1}</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`



#### `<code>innodb_read_ahead</code>`


* Description: If set to `<code>linear</code>`, the default, XtraDB/InnoDB will automatically fetch remaining pages if there are enough within the same extent that can be accessed sequentially. If set to `<code>none</code>`, read-ahead is disabled. `<code>random</code>` has been removed and is now ignored, while `<code>both</code>` sets to both `<code>linear</code>` and `<code>random</code>`. Also see [innodb_read_ahead_threshold](#innodb_read_ahead_threshold) for more control on read-aheads. Removed in [MariaDB 10.0](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md)/XtraDB 5.6 and replaced by MySQL 5.6's [innodb_random_read_ahead](#innodb_random_read_ahead).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">innodb-read-ahead=value</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>enumeration</code>`
* Default Value: `<code>linear</code>`
* Valid Values: `<code>none</code>`, `<code>random</code>`, `<code>linear</code>`, `<code>both</code>`
* Removed: [MariaDB 10.0](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md)/XtraDB 5.6 - replaced by MySQL 5.6's [innodb_random_read_ahead](#innodb_random_read_ahead)



#### `<code>innodb_read_ahead_threshold</code>`


* Description: Minimum number of pages InnoDB must read sequentially from an extent of 64 before initiating an asynchronous read for the following extent.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-read-ahead-threshold=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>56</code>`
* Range: `<code>0</code>` to `<code>64</code>`



#### `<code>innodb_read_io_threads</code>`


* Description: Prior to [MariaDB 10.5](../../../../release-notes/mariadb-community-server/what-is-mariadb-105.md), this was simply the number of I/O threads for InnoDB reads. From [MariaDB 10.5](../../../../release-notes/mariadb-community-server/what-is-mariadb-105.md), asynchronous I/O functionality in the InnoDB Background Thread Pool replaces the old InnoDB I/O Threads. This variable is now multipled by 256 to determine the maximum number of concurrent asynchronous I/O read requests that can be completed by the Background Thread Pool. The default is therefore 4*256 = 1024 conccurrent asynchronous read requests. You may on rare occasions need to reduce this default on Linux systems running multiple MariaDB servers to avoid exceeding system limits, or increase if spending too much time waiting on I/O requests.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-read-io-threads=#</code>`
* Scope: Global
* Dynamic: Yes (>= [MariaDB 10.11](../../../../release-notes/mariadb-community-server/what-is-mariadb-1011.md)), No (<= [MariaDB 10.10](../../../../release-notes/mariadb-community-server/what-is-mariadb-1010.md))
* Data Type: `<code>numeric</code>`
* Default Value: `<code>4</code>`
* Range: `<code>1</code>` to `<code>64</code>`



#### `<code>innodb_read_only</code>`


* Description: If set to `<code>1</code>` (`<code>0</code>` is default), the server will be read-only. For use in distributed applications, data warehouses or read-only media.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-read-only={0|1}</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`



#### `<code>innodb_read_only_compressed</code>`


* Description: If set (the default before [MariaDB 10.6.6](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-1066-release-notes.md)), [ROW_FORMAT=COMPRESSED](innodb-row-formats/innodb-compressed-row-format.md) tables will be read-only. This was intended to be the first step towards removing write support and deprecating the feature, but this plan has been abandoned.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-read-only-compressed</code>`, `<code class="fixed" style="white-space:pre-wrap">--skip-innodb-read-only-compressed</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>` (>= [MariaDB 10.6.6](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-1066-release-notes.md)), `<code>ON</code>` (<= [MariaDB 10.6.5](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-1065-release-notes.md))
* Introduced: [MariaDB 10.6.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-1060-release-notes.md)



#### `<code>innodb_recovery_stats</code>`


* Description: If set to `<code>1</code>` (`<code>0</code>` is default) and recovery is necessary on startup, the server will write detailed recovery statistics to the error log at the end of the recovery process. This Percona XtraDB variable has not been ported to XtraDB 5.6.
* Commandline: No
* Scope: Global
* Dynamic: No
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`
* Removed: [MariaDB 10.0](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md)



#### `<code>innodb_recovery_update_relay_log</code>`


* Description: If set to `<code>1</code>` (`<code>0</code>` is default), the relay log info file will be overwritten on crash recovery if the information differs from the InnoDB record. Should not be used if multiple storage engine types are being replicated. Previously named `<code>innodb_overwrite_relay_log_info</code>`. Removed in [MariaDB 10.0](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md)/XtraDB 5.6 and replaced by MySQL 5.6's `<code>relay-log-recovery</code>`
* Commandline: `<code class="fixed" style="white-space:pre-wrap">innodb-recovery-update-relay-log={0|1}</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`
* Removed: [MariaDB 10.0](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md) - replaced by MySQL 5.6's `<code>relay-log-recovery</code>`



#### `<code>innodb_replication_delay</code>`


* Description: Time in milliseconds for the replica server to delay the replication thread if [innodb_thread_concurrency](#innodb_thread_concurrency) is reached. Deprecated and ignored from [MariaDB 10.5.5](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1055-release-notes.md).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-replication-delay=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>0</code>`
* Range: `<code>0</code>` to `<code>4294967295</code>`
* Deprecated: [MariaDB 10.5.5](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1055-release-notes.md)
* Removed: [MariaDB 10.6.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-1060-release-notes.md)



#### `<code>innodb_rollback_on_timeout</code>`


* Description: InnoDB usually rolls back the last statement of a transaction that's been timed out (see [innodb_lock_wait_timeout](#innodb_lock_wait_timeout)). If innodb_rollback_on_timeout is set to 1 (0 is default), InnoDB will roll back the entire transaction. Before [MariaDB 5.5](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5.md), rolling back the entire transaction was the default behavior.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-rollback-on-timeout</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>boolean</code>`
* Default Value: `<code>0</code>`



#### `<code>innodb_rollback_segments</code>`


* Description: Specifies the number of rollback segments that XtraDB/InnoDB will use within a transaction (see [undo log](innodb-undo-log.md)). Deprecated and replaced by [innodb_undo_logs](#innodb_undo_logs) in [MariaDB 10.0](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md). Removed in [MariaDB 10.5](../../../../release-notes/mariadb-community-server/what-is-mariadb-105.md) as part of an InnoDB cleanup, as it makes sense to always create and use the maximum number of rollback segments. |
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-rollback-segments=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>128</code>`
* Range: `<code>1</code>` to `<code>128</code>`
* Deprecated: [MariaDB 10.0](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md)
* Removed: [MariaDB 10.5.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1050-release-notes.md)



#### `<code>innodb_safe_truncate</code>`


* Description: Use a backup-safe [TRUNCATE TABLE](../../sql-statements-and-structure/sql-statements/table-statements/truncate-table.md) implementation and crash-safe rename operations inside InnoDB. This is not compatible with hot backup tools other than [Mariabackup](../../../server-management/backing-up-and-restoring-databases/mariabackup/mariabackup-overview.md). Users who need to use such tools may set this to `<code>OFF</code>`.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-safe-truncate={0|1}</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>boolean</code>`
* Default Value: `<code>ON</code>`
* Introduced: [MariaDB 10.2.19](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-10219-release-notes.md)
* Removed: [MariaDB 10.3.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1030-release-notes.md)



#### `<code>innodb_scrub_log</code>`


* Description: Enable [InnoDB redo log](innodb-redo-log.md) scrubbing. See [Data Scrubbing](innodb-data-scrubbing.md). Deprecated and ignored from [MariaDB 10.5.2](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1052-release-notes.md), as never really worked ([MDEV-13019](https://jira.mariadb.org/browse/MDEV-13019) and [MDEV-18370](https://jira.mariadb.org/browse/MDEV-18370)). If old log contents should be kept secret, then enabling [innodb_encrypt_log](innodb-system-variables.md#innodb_encrypt_log) or setting a smaller [innodb_log_file_size](innodb-system-variables.md#innodb_log_file_size) could help.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-scrub-log</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`
* Deprecated: [MariaDB 10.5.2](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1052-release-notes.md)
* Removed: [MariaDB 10.6.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-1060-release-notes.md)



#### `<code>innodb_scrub_log_interval</code>`


* Description: Used with [Data Scrubbing](innodb-data-scrubbing.md) in 10.1.3 only - replaced in 10.1.4 by [innodb_scrub_log_speed](#innodb_scrub_log_speed). [InnoDB redo log](innodb-redo-log.md) scrubbing interval in milliseconds.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-scrub-log-interval=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>56</code>`
* Range: `<code>0</code>` to `<code>50000</code>`
* Introduced: [MariaDB 10.1.3](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-3-release-notes.md)
* Removed: [MariaDB 10.1.4](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-4-release-notes.md)



#### `<code>innodb_scrub_log_speed</code>`


* Description: [InnoDB redo log](innodb-redo-log.md) scrubbing speed in bytes/sec. See [Data Scrubbing](innodb-data-scrubbing.md). Deprecated and ignored from [MariaDB 10.5.2](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1052-release-notes.md).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-scrub-log-speed=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>256</code>`
* Range: `<code>1</code>` to `<code>50000</code>`
* Deprecated: [MariaDB 10.5.2](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1052-release-notes.md)
* Removed: [MariaDB 10.6.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-1060-release-notes.md)



#### `<code>innodb_sched_priority_cleaner</code>`


* Description: Set a thread scheduling priority for cleaner and least-recently used (LRU) manager threads. The range from `<code>0</code>` to `<code>39</code>` corresponds in reverse order to Linux nice values of `<code>-20</code>` to `<code>19</code>`. So `<code>0</code>` is the lowest priority (Linux nice value `<code>19</code>`) and `<code>39</code>` is the highest priority (Linux nice value `<code>-20</code>`). XtraDB only. Added as a deprecated and ignored option in [MariaDB 10.2.6](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1026-release-notes.md) (which uses InnoDB as default instead of XtraDB) to allow for easier upgrades.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">innodb-sched-priority-cleaner=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>19</code>`
* Range: `<code>0</code>` to `<code>39</code>`
* Deprecated: [MariaDB 10.2.6](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1026-release-notes.md)
* Removed: [MariaDB 10.3.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1030-release-notes.md)



#### `<code>innodb_show_locks_held</code>`


* Description: Specifies the number of locks held for each InnoDB transaction to be displayed in [SHOW ENGINE INNODB STATUS](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-engine-innodb-status.md) output. XtraDB only. Added as a deprecated and ignored option in [MariaDB 10.2.6](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1026-release-notes.md) (which uses InnoDB as default instead of XtraDB) to allow for easier upgrades.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">innodb-show-locks-held=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>10</code>`
* Range: `<code>0</code>` to `<code>1000</code>`
* Deprecated: [MariaDB 10.2.6](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1026-release-notes.md)
* Removed: [MariaDB 10.3.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1030-release-notes.md)



#### `<code>innodb_show_verbose_locks</code>`


* Description: If set to `<code>1</code>`, and [innodb_status_output_locks](#innodb_status_output_locks) is also ON, the traditional InnoDB behavior is followed and locked records will be shown in [SHOW ENGINE INNODB STATUS](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-engine-innodb-status.md) output. If set to `<code>0</code>`, the default, only high-level information about the lock is shown. XtraDB only. Added as a deprecated and ignored option in [MariaDB 10.2.6](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1026-release-notes.md) (which uses InnoDB as default instead of XtraDB) to allow for easier upgrades.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">innodb-show-verbose-locks=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>0</code>`
* Range: `<code>0</code>` to `<code>1</code>`
* Deprecated: [MariaDB 10.2.6](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1026-release-notes.md)
* Removed: [MariaDB 10.3.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1030-release-notes.md)



#### `<code>innodb_simulate_comp_failures</code>`


* Description: Simulate compression failures. Used for testing robustness against random compression failures. XtraDB only.
* Commandline: None
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>0</code>`
* Range: `<code>0</code>` to `<code>99</code>`



#### `<code>innodb_snapshot_isolation</code>`


* Description: Use snapshot isolation (write-write conflict detection). If set, if an attempt to acquire a lock on a record that does not exist in the current read view is made, an error DB_RECORD_CHANGED (HA_ERR_RECORD_CHANGED, ER_CHECKREAD) will be raised. This error will be treated in the same way as a deadlock and the transaction will be rolled back. When set, the default isolation level, [REPEATABLE READ](../../sql-statements-and-structure/sql-statements/transactions/set-transaction.md#repeatable-read) will become Snapshot Isolation. Prior to [MariaDB 11.6.2](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-6-rolling-releases/mariadb-11-6-2-release-notes.md), the default is OFF for backwards compatibility.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-snapshot-isolation={0|1}</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>ON</code>` (>= [MariaDB 11.6.2](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-6-rolling-releases/mariadb-11-6-2-release-notes.md)), `<code>OFF</code>` (<= [MariaDB 11.6.1](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-6-rolling-releases/mariadb-11-6-1-release-notes.md))
* Introduced: [MariaDB 10.6.18](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-10-6-18-release-notes.md), [MariaDB 10.11.8](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-11-series/mariadb-10-11-8-release-notes.md), [MariaDB 11.0.6](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-0-series/mariadb-11-0-6-release-notes.md), [MariaDB 11.1.5](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-1-series/mariadb-11-1-5-release-notes.md), [MariaDB 11.2.4](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-2-series/mariadb-11-2-4-release-notes.md), [MariaDB 11.4.2](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-4-series/mariadb-11-4-2-release-notes.md)



#### `<code>innodb_sort_buffer_size</code>`


* Description: Size of the sort buffers used for sorting data when an InnoDB index is created, as well as the amount by which the temporary log file is extended during online DDL operations to record concurrent writes. The larger the setting, the fewer merge phases are required between buffers while sorting. When a [CREATE TABLE](../../sql-statements-and-structure/vectors/create-table-with-vectors.md) or [ALTER TABLE](../../sql-statements-and-structure/sql-statements/data-definition/alter/alter-tablespace.md) creates a new index, three buffers of this size are allocated, as well as pointers for the rows in the buffer.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-sort-buffer-size=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value: `<code>1048576</code>` (1M)
* Range: `<code>65536</code>` to `<code>67108864</code>`



#### `<code>innodb_log_spin_wait_delay</code>`


* Description: Maximum delay (not strictly corresponding to a time unit) between spin lock polls. Default changed from `<code>6</code>` to `<code>4</code>` in [MariaDB 10.3.5](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1035-release-notes.md), as this was verified to give the best throughput by OLTP update index and read-write benchmarks on Intel Broadwell (2/20/40) and ARM (1/46/46).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-log-spin-wait-delay=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>4</code>` (>= [MariaDB 10.3.5](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1035-release-notes.md)), `<code>6</code>` (<= [MariaDB 10.3.4](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1034-release-notes.md))
* Range: `<code>0</code>` to `<code>4294967295</code>`



#### `<code>innodb_stats_auto_recalc</code>`


* Description: If set to `<code>1</code>` (the default), persistent statistics are automatically recalculated when the table changes significantly (more than 10% of the rows). Affects tables created or altered with STATS_PERSISTENT=1 (see [CREATE TABLE](../../sql-statements-and-structure/vectors/create-table-with-vectors.md)), or when [innodb_stats_persistent](#innodb_stats_persistent) is enabled. [innodb_stats_persistent_sample_pages](#innodb_stats_persistent_sample_pages) determines how much data to sample when recalculating. See [InnoDB Persistent Statistics](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/query-optimizations/statistics-for-optimizing-queries/innodb-persistent-statistics.md).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-stats-auto-recalc={0|1}</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>ON</code>`



#### `<code>innodb_stats_auto_update</code>`


* Description: If set to `<code>0</code>` (`<code>1</code>` is default), index statistics will not be automatically calculated except when an [ANALYZE TABLE](../../sql-statements-and-structure/sql-statements/table-statements/analyze-table.md) is run, or the table is first opened. Replaced by [innodb_stats_auto_recalc](#innodb_stats_auto_recalc) in [MariaDB 10.0](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md)/XtraDB 5.6.
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>1</code>`
* Removed: [MariaDB 10.0](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md) - replaced by [innodb_stats_auto_recalc](#innodb_stats_auto_recalc).



#### `<code>innodb_stats_include_delete_marked</code>`


* Description: Include delete marked records when calculating persistent statistics.
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`



#### `<code>innodb_stats_method</code>`


* Description: Determines how NULLs are treated for InnoDB index statistics purposes. 

  * `<code>nulls_equal</code>`: The default, all NULL index values are treated as a single group. This is usually fine, but if you have large numbers of NULLs the average group size is slanted higher, and the optimizer may miss using the index for ref accesses when it would be useful.
  * `<code>nulls_unequal</code>`: The opposite approach to `<code>nulls_equal</code>` is taken, with each NULL forming its own group of one. Conversely, the average group size is slanted lower, and the optimizer may use the index for ref accesses when not suitable.
  * `<code>nulls_ignored</code>`: Ignore NULLs altogether from index group calculations.
  * See also [Index Statistics](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/optimization-and-indexes/index-statistics.md), [aria_stats_method](../aria/aria-system-variables.md) and [myisam_stats_method](../myisam-storage-engine/myisam-system-variables.md).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-stats-method=name</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>enumeration</code>`
* Default Value: `<code>nulls_equal</code>`
* Valid Values: `<code>nulls_equal</code>`, `<code>nulls_unequal</code>`, `<code>nulls_ignored</code>`



#### `<code>innodb_stats_modified_counter</code>`


* Description: The number of rows modified before we calculate new statistics. If set to `<code>0</code>`, the default, current limits are used.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-stats-modified-counter=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>0</code>`
* Range: `<code>0</code>` to `<code>18446744073709551615</code>`



#### `<code>innodb_stats_on_metadata</code>`


* Description: If set to `<code>1</code>`, the default, XtraDB/InnoDB updates statistics when accessing the INFORMATION_SCHEMA.TABLES or INFORMATION_SCHEMA.STATISTICS tables, and when running metadata statements such as [SHOW INDEX](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-index.md) or [SHOW TABLE STATUS](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-table-status.md). If set to `<code>0</code>`, statistics are not updated at those times, which can reduce the access time for large schemas, as well as make execution plans more stable.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-stats-on-metadata</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`



#### `<code>innodb_stats_persistent</code>`


* Description: [ANALYZE TABLE](../../sql-statements-and-structure/sql-statements/table-statements/analyze-table.md) produces index statistics, and this setting determines whether they will be stored on disk, or be required to be recalculated more frequently, such as when the server restarts. This information is stored for each table, and can be set with the STATS_PERSISTENT clause when creating or altering tables (see [CREATE TABLE](../../sql-statements-and-structure/vectors/create-table-with-vectors.md)). See [InnoDB Persistent Statistics](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/query-optimizations/statistics-for-optimizing-queries/innodb-persistent-statistics.md).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-stats-persistent={0|1}</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>ON</code>`



#### `<code>innodb_stats_persistent_sample_pages</code>`


* Description: Number of index pages sampled when estimating cardinality and statistics for indexed columns. Increasing this value will increases index statistics accuracy, but use more I/O resources when running [ANALYZE TABLE](../../sql-statements-and-structure/sql-statements/table-statements/analyze-table.md). See [InnoDB Persistent Statistics](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/query-optimizations/statistics-for-optimizing-queries/innodb-persistent-statistics.md).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-stats-persistent-sample-pages=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>20</code>`



#### `<code>innodb_stats_sample_pages</code>`


* Description: Gives control over the index distribution statistics by determining the number of index pages to sample. Higher values produce more disk I/O, but, especially for large tables, produce more accurate statistics and therefore make more effective use of the query optimizer. Lower values than the default are not recommended, as the statistics can be quite inaccurate.

  * If [innodb_stats_traditional](#innodb_stats_traditional) is enabled, then the exact number of pages configured by this system variable will be sampled for statistics.
  * If [innodb_stats_traditional](#innodb_stats_traditional) is disabled, then the number of pages to sample for statistics is calculated using a logarithmic algorithm, so the exact number can change depending on the size of the table. This means that more samples may be used for larger tables.
  * If [persistent statistics](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/query-optimizations/statistics-for-optimizing-queries/innodb-persistent-statistics.md) are enabled, then the [innodb_stats_persistent_sample_pages](#innodb_stats_persistent_sample_pages) system variable applies instead. [persistent statistics](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/query-optimizations/statistics-for-optimizing-queries/innodb-persistent-statistics.md) are enabled with the [innodb_stats_persistent](#innodb_stats_persistent) system variable.
  * This system variable has been deprecated. The [innodb_stats_transient_sample_pages](#innodb_stats_transient_sample_pages) system variable should be used instead.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-stats-sample-pages=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>8</code>`
* Range: `<code>1</code>` to `<code>2<sup>64</sup>-1</code>`
* Deprecated: [MariaDB 10.0](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md)
* Removed: [MariaDB 10.5.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1050-release-notes.md)



#### `<code>innodb_stats_traditional</code>`


* Description: This system variable affects how the number of pages to sample for transient statistics is determined, in particular how [innodb_stats_transient_sample_pages](#innodb_stats_transient_sample_pages) is used.

  * If [innodb_stats_traditional](#innodb_stats_traditional) is enabled, then the exact number of pages configured by the system variable will be sampled for statistics.
  * If [innodb_stats_traditional](#innodb_stats_traditional) is disabled, then the number of pages to sample for statistics is calculated using a logarithmic algorithm, so the exact number can change depending on the size of the table. This means that more samples may be used for larger tables.
  * This system variable does not affect the calculation of [persistent statistics](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/query-optimizations/statistics-for-optimizing-queries/innodb-persistent-statistics.md).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-stats-traditional={0|1}</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>ON</code>`



#### `<code>innodb_stats_transient_sample_pages</code>`


* Description: Gives control over the index distribution statistics by determining the number of index pages to sample. Higher values produce more disk I/O, but, especially for large tables, produce more accurate statistics and therefore make more effective use of the query optimizer. Lower values than the default are not recommended, as the statistics can be quite inaccurate.

  * If `<code>[innodb_stats_traditional](#innodb_stats_traditional)</code>` is enabled, then the exact number of pages configured by this system variable will be sampled for statistics.
  * If `<code>[innodb_stats_traditional](#innodb_stats_traditional)</code>` is disabled, then the number of pages to sample for statistics is calculated using a logarithmic algorithm, so the exact number can change depending on the size of the table. This means that more samples may be used for larger tables.
  * If [persistent statistics](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/query-optimizations/statistics-for-optimizing-queries/innodb-persistent-statistics.md) are enabled, then the `<code>[innodb_stats_persistent_sample_pages](#innodb_stats_persistent_sample_pages)</code>` system variable applies instead. [persistent statistics](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/query-optimizations/statistics-for-optimizing-queries/innodb-persistent-statistics.md) are enabled with the `<code>[innodb_stats_persistent](#innodb_stats_persistent)</code>` system variable.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-stats-transient-sample-pages=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>8</code>`
* Range: `<code>1</code>` to `<code>2<sup>64</sup>-1</code>`



#### `<code>innodb_stats_update_need_lock</code>`


* Description: Setting to `<code>0</code>` (`<code>1</code>` is default) may help reduce contention of the `<code>&dict_operation_lock</code>`, but also disables the Data_free option in [SHOW TABLE STATUS](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-table-status.md). This Percona XtraDB variable has not been ported to XtraDB 5.6.
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>1</code>`
* Removed: [MariaDB 10.0](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md)/XtraDB 5.6



#### `<code>innodb_status_output</code>`


* Description: Enable [InnoDB monitor](innodb-monitors.md) output to the [error log](../../../server-management/server-monitoring-logs/error-log.md).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-status-output={0|1}</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`



#### `<code>innodb_status_output_locks</code>`


* Description: Enable [InnoDB lock monitor](innodb-monitors.md) output to the [error log](../../../server-management/server-monitoring-logs/error-log.md) and [SHOW ENGINE INNODB STATUS](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-engine-innodb-status.md). Also requires [innodb_status_output=ON](#innodb_status_output) to enable output to the error log.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-status-output-locks={0|1}</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`



#### `<code>innodb_strict_mode</code>`


* Description: If set to `<code>1</code>` (the default), InnoDB will return errors instead of warnings in certain cases, similar to strict SQL mode. See [InnoDB Strict Mode](innodb-strict-mode.md) for details.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-strict-mode={0|1}</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>ON</code>`



#### `<code>innodb_support_xa</code>`


* Description: If set to `<code>1</code>`, the default, [XA transactions](../../sql-statements-and-structure/sql-statements/transactions/xa-transactions.md) are supported. XA support ensures data is written to the [binary log](binary-log-group-commit-and-innodb-flushing-performance.md) in the same order to the actual database, which is critical for [replication](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/README.md) and disaster recovery, but comes at a small performance cost. If your database is set up to only permit one thread to change data (for example, on a replication replica with only the replication thread writing), it is safe to turn this option off. Removed in [MariaDB 10.3](../../../../release-notes/mariadb-community-server/what-is-mariadb-103.md), XA transactions are always supported.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-support-xa</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>ON</code>`
* Deprecated: [MariaDB 10.2](../../../../release-notes/mariadb-community-server/what-is-mariadb-102.md)
* Removed: [MariaDB 10.3.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1030-release-notes.md)



#### `<code>innodb_sync_array_size</code>`


* Description: By default `<code>1</code>`, can be increased to split internal thread co-ordinating, giving higher concurrency when there are many waiting threads.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-sync-array-size=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value: `<code>1</code>`
* Range: `<code>1</code>` to `<code>1024</code>`
* Removed: [MariaDB 10.6.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-1060-release-notes.md)



#### `<code>innodb_sync_spin_loops</code>`


* Description: The number of times a thread waits for an InnoDB mutex to be freed before the thread is suspended.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-sync-spin-loops=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>30</code>`
* Range: `<code>0</code>` to `<code>4294967295</code>`



#### `<code>innodb_table_locks</code>`


* Description: If [autocommit](#autocommit) is set to to `<code>0</code>` (`<code>1</code>` is default), setting innodb_table_locks to `<code>1</code>`, the default, will cause InnoDB to lock a table internally upon a [LOCK TABLE](https://mariadb.com/kb/en/LOCK_TABLES).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-table-locks</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>ON</code>`



#### `<code>innodb_thread_concurrency</code>`


* Description: Once this number of threads is reached (excluding threads waiting for locks), XtraDB/InnoDB will place new threads in a wait state in a first-in, first-out queue for execution, in order to limit the number of threads running concurrently. A setting of `<code>0</code>`, the default, permits as many threads as necessary. A suggested setting is twice the number of CPU's plus the number of disks. Deprecated and ignored from [MariaDB 10.5.5](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1055-release-notes.md).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-thread-concurrency=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>0</code>`
* Range: `<code>0</code>` to `<code>1000</code>`
* Deprecated: [MariaDB 10.5.5](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1055-release-notes.md)
* Removed: [MariaDB 10.6.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-1060-release-notes.md)



#### `<code>innodb_thread_concurrency_timer_based</code>`


* Description: If set to `<code>1</code>`, thread concurrency will be handled in a lock-free timer-based manner rather than the default mutex-based method. Depends on atomic op builtins being available. This Percona XtraDB variable has not been ported to XtraDB 5.6.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">innodb-thread-concurrency-timer-based={0|1}</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`
* Removed: [MariaDB 10.0](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md)/XtraDB 5.6



#### `<code>innodb_thread_sleep_delay</code>`


* Description: Time in microseconds that InnoDB threads sleep before joining the queue. Setting to `<code>0</code>` disables sleep. Deprecated and ignored from [MariaDB 10.5.5](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1055-release-notes.md)
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-thread-sleep-delay=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value:

  * `<code>0</code>` (>= [MariaDB 10.5.5](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1055-release-notes.md).)
  * `<code>10000</code>` (<= [MariaDB 10.5.4](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1054-release-notes.md))
* Range: `<code>0</code>` to `<code>1000000</code>`
* Deprecated: [MariaDB 10.5.5](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1055-release-notes.md)
* Removed: [MariaDB 10.6.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-1060-release-notes.md)



#### `<code>innodb_temp_data_file_path</code>`


* Description: Path where to store data for [InnoDB](../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/innodb-upgrade-tests/README.md) temporary tables. Argument is `<code>filename:size</code>` followed by options separated by ':' Multiple paths can be given separated by ';' A file size is specified (with K for kilobytes, M for megabytes and G for gigabytes). Also whether or not to `<code>autoextend</code>` the data file, `<code>max</code>` size and whether or not to `<code>[autoshrink](innodb-tablespaces/innodb-system-tablespaces.md#decreasing-the-size)</code>` on startup may also be specified.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-temp-data-file-path=path</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>string</code>`
* Default Value: `<code>ibtmp1:12M:autoextend</code>`
* Documentation & examples: [innodb-temporary-tablespaces](innodb-tablespaces/innodb-temporary-tablespaces.md)



#### `<code>innodb_tmpdir</code>`


* Description: Allows an alternate location to be set for temporary non-tablespace files. If not set (the default), files will be created in the usual [tmpdir](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#tmpdir) location.
Alternate location must be outside of `<code>datadir</code>`
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-tmpdir=path</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>string</code>`
* Default Value: Empty



#### `<code>innodb_track_changed_pages</code>`


* Description: For faster incremental backup with [Xtrabackup](../../../clients-and-utilities/legacy-clients-and-utilities/backing-up-and-restoring-databases-percona-xtrabackup/percona-xtrabackup-overview.md), XtraDB tracks pages with changes written to them according to the [XtraDB redo log](innodb-redo-log.md) and writes the information to special changed page bitmap files. This read-only variable is used for controlling this feature. See also [innodb_max_changed_pages](#innodb_max_changed_pages) and [innodb_max_bitmap_file_size](#innodb_max_bitmap_file_size). XtraDB only. Added as a deprecated and ignored option in [MariaDB 10.2.6](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1026-release-notes.md) (which uses InnoDB as default instead of XtraDB) to allow for easier upgrades.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">innodb-track-changed-pages={0|1}</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`
* Deprecated: [MariaDB 10.2.6](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1026-release-notes.md)



#### `<code>innodb_track_redo_log_now</code>`


* Description: Available on debug builds only. XtraDB only. Added as a deprecated and ignored option in [MariaDB 10.2.6](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1026-release-notes.md) (which uses InnoDB as default instead of XtraDB) to allow for easier upgrades.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">innodb-track-redo-log-now={0|1}</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`
* Deprecated: [MariaDB 10.2.6](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1026-release-notes.md)



#### `<code>innodb_truncate_temporary_tablespace_now</code>`


* Description: Set to ON to shrink the temporary tablespace.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">innodb-truncate-temporary-tablespace-now={0|1}</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`
* Introduced: [MariaDB 11.3.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-0-release-notes.md)



#### `<code>innodb_undo_directory</code>`


* Description: Path to the directory (relative or absolute) that InnoDB uses to create separate tablespaces for the [undo logs](innodb-undo-log.md). `<code>.</code>` (the default value before 10.2.2) leaves the undo logs in the same directory as the other log files. From [MariaDB 10.2.2](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1022-release-notes.md), the default value is NULL, and if no path is specified, undo tablespaces will be created in the directory defined by [datadir](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#datadir). Use together with [innodb_undo_logs](#innodb_undo_logs) and [innodb_undo_tablespaces](#innodb_undo_tablespaces). Undo logs are most usefully placed on a separate storage device.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-undo-directory=name</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>string</code>`
* Default Value: NULL



#### `<code>innodb_undo_log_truncate</code>`


* Description: When enabled, [innodb_undo_tablespaces](#innodb_undo_tablespaces) that are larger than [innodb_max_undo_log_size](#innodb_max_undo_log_size) will be marked for truncation. See also [innodb_purge_rseg_truncate_frequency](#innodb_purge_rseg_truncate_frequency). Enabling this setting may cause stalls during heavy write workloads.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-undo-log-truncate[={0|1}]</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`



#### `<code>innodb_undo_logs</code>`


* Description: Specifies the number of rollback segments that XtraDB/InnoDB will use within a transaction (or the number of active [undo logs](innodb-undo-log.md)). By default set to the maximum, `<code>128</code>`, it can be reduced to avoid allocating unneeded rollback segments. See the [Innodb_available_undo_logs](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/innodb-status-variables.md) status variable for the number of undo logs available. See also [innodb_undo_directory](#innodb_undo_directory) and [innodb_undo_tablespaces](#innodb_undo_tablespaces). Replaced [innodb_rollback_segments](#innodb_rollback_segments) in [MariaDB 10.0](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md). The [Information Schema XTRADB_RSEG Table](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-xtradb-tables/information-schema-xtradb_rseg-table.md) contains information about the XtraDB rollback segments. Deprecated and ignored in [MariaDB 10.5.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1050-release-notes.md), as it always makes sense to use the maximum number of rollback segments.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-undo-logs=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>128</code>`
* Range: `<code>0</code>` to `<code>128</code>`
* Deprecated: [MariaDB 10.5.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1050-release-notes.md)
* Removed: [MariaDB 10.6.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-1060-release-notes.md)



#### `<code>innodb_undo_tablespaces</code>`


* Description: Number of tablespaces files used for dividing up the [undo logs](innodb-undo-log.md). Zero (the default before [MariaDB 11.0](../../../../release-notes/mariadb-community-server/what-is-mariadb-110.md)) means that undo logs are all part of the system tablespace, which contains one undo tablespace more than the `<code>innodb_undo_tablespaces</code>` setting. A value of 1 is reset to 0 as 2 or more are needed for separate tablespaces. When the undo logs can grow large, splitting them over multiple tablespaces will reduce the size of any single tablespace. Until [MariaDB 10.11.1](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-11-series/mariadb-10-11-1-release-notes.md), must be set before InnoDB is initialized, or else MariaDB will fail to start, with an error saying that `<code>InnoDB did not find the expected number of undo tablespaces</code>`. The files are created in the directory specified by [innodb_undo_directory](#innodb_undo_directory), and are named `<code>undoN</code>`, N being an integer. The default size of an undo tablespace is 10MB.From [MariaDB 11.0](../../../../release-notes/mariadb-community-server/what-is-mariadb-110.md), multiple undo tablespaces are enabled by default, and the default is changed to 3 so that the space occupied by possible bursts of undo log records can be reclaimed after [innodb_undo_log_truncate](#innodb_undo_log_truncate) is set. Before [MariaDB 10.6](../../../../release-notes/mariadb-community-server/what-is-mariadb-106.md), [innodb_undo_logs](#innodb_undo_logs) must have a non-zero setting for `<code>innodb_undo_tablespaces</code>` to take effect.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-undo-tablespaces=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value: `<code>3</code>` (>= [MariaDB 11.0](../../../../release-notes/mariadb-community-server/what-is-mariadb-110.md)), `<code>0</code>` (<= [MariaDB 10.11](../../../../release-notes/mariadb-community-server/what-is-mariadb-1011.md))
* Range: `<code>0</code>`, or `<code>2</code>` to `<code>95</code>`



#### `<code>innodb_use_atomic_writes</code>`


* Description: Implement atomic writes on supported SSD devices. See [atomic write support](../../../server-management/getting-installing-and-upgrading-mariadb/mariadb-performance-advanced-configurations/atomic-write-support.md) for other variables affected when this is set.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">innodb-use-atomic-writes={0|1}</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>boolean</code>`
* Default Value: `<code>ON</code>`



#### `<code>innodb_use_fallocate</code>`


* Description: Preallocate files fast, using operating system functionality. On POSIX systems, posix_fallocate system call is used.

  * Automatically set to `<code>1</code>` when [innodb_use_atomic_writes](#innodb_use_atomic_writes) is set - see [FusionIO DirectFS atomic write support](../../../server-management/getting-installing-and-upgrading-mariadb/mariadb-performance-advanced-configurations/atomic-write-support.md).
  * See [InnoDB Page Compression: Saving Storage Space with Sparse Files](innodb-page-compression.md#saving-storage-space-with-sparse-files) for more information.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">innodb-use-fallocate={0|1}</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`
* Deprecated: [MariaDB 10.2.5](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1025-release-notes.md) (treated as if `<code>ON</code>`)
* Removed: [MariaDB 10.3.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1030-release-notes.md)



#### `<code>innodb_use_global_flush_log_at_trx_commit</code>`


* Description: Determines whether a user can set the variable [innodb_flush_log_at_trx_commit](#innodb_flush_log_at_trx_commit). If set to `<code>1</code>`, a user cannot reset the value with a SET command, while if set to `<code>1</code>`, a user can reset the value of `<code>innodb_flush_log_at_trx_commit</code>`. XtraDB only. Added as a deprecated and ignored option in [MariaDB 10.2.6](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1026-release-notes.md) (which uses InnoDB as default instead of XtraDB) to allow for easier upgrades.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">innodb-use-global-flush-log-at-trx_commit={0|1}</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>ON</code>`
* Deprecated: [MariaDB 10.2.6](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1026-release-notes.md)
* Removed: [MariaDB 10.3.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1030-release-notes.md)



#### `<code>innodb_use_mtflush</code>`


* Description: Whether to enable Multi-Threaded Flush operations.
For more information, see Fusion. 

  * InnoDB's multi-thread flush feature was deprecated in [MariaDB 10.2.9](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1029-release-notes.md) and removed from [MariaDB 10.3.2](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1032-release-notes.md). In later versions of MariaDB, use `<code>[innodb_page_cleaners](#innodb_page_cleaners)</code>` system variable instead.
  * See [InnoDB Page Flushing: Page Flushing with Multi-threaded Flush Threads](innodb-page-flushing.md#page-flushing-with-multi-threaded-flush-threads) for more information.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-use-mtflush={0|1}</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`
* Deprecated: [MariaDB 10.2.9](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1029-release-notes.md)
* Removed: [MariaDB 10.3.2](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1032-release-notes.md)



#### `<code>innodb_use_native_aio</code>`


* Description: For Linux systems only, specified whether to use Linux's asynchronous I/O subsystem. Set to `<code>ON</code>` by default, it may be changed to `<code>0</code>` at startup if InnoDB detects a problem, or from [MariaDB 10.6.5](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-1065-release-notes.md)/[MariaDB 10.7.1](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-7-series/mariadb-1071-release-notes.md), if a 5.11 - 5.15 Linux kernel is detected, to avoid an io-uring bug/incompatibility ([MDEV-26674](https://jira.mariadb.org/browse/MDEV-26674)). MariaDB-10.6.6/MariaDB-10.7.2 and later also consider 5.15.3+ as a fixed kernel and default to `<code>ON</code>`. To really benefit from the setting, the files should be opened in O_DIRECT mode ([innodb_flush_method=O_DIRECT](#innodb_flush_method), default from [MariaDB 10.6](../../../../release-notes/mariadb-community-server/what-is-mariadb-106.md)), to bypass the file system cache. In this way, the reads and writes can be submitted with DMA, using the InnoDB buffer pool directly, and no processor cycles need to be used for copying data.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-use-native-aio={0|1}</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>boolean</code>`
* Default Value: `<code>ON</code>`



#### `<code>innodb_use_purge_thread</code>`


* Description: Usually with InnoDB, data changed by a transaction is written to an undo space to permit read consistency, and freed when the transaction is complete. Many, or large, transactions, can cause the main tablespace to grow dramatically, reducing performance. This option, introduced in XtraDB 5.1 and removed for 5.5, allows multiple threads to perform the purging, resulting in slower, but much more stable performance.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-use-purge-thread=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value: `<code>1</code>`
* Range: `<code>0</code>` to `<code>32</code>`
* Removed: XtraDB 5.5



#### `<code>innodb_use_stacktrace</code>`


* Description: If set to `<code>ON</code>` (`<code>OFF</code>` is default), a signal handler for SIGUSR2 is installed when the InnoDB server starts. When a long semaphore wait is detected at sync/sync0array.c, a SIGUSR2 signal is sent to the waiting thread and thread that has acquired the RW-latch. For both threads a full stacktrace is produced as well as if possible. XtraDB only. Added as a deprecated and ignored option in [MariaDB 10.2.6](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1026-release-notes.md) (which uses InnoDB as default instead of XtraDB) to allow for easier upgrades.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-use-stacktrace={0|1}</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`
* Deprecated: [MariaDB 10.2.6](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1026-release-notes.md)
* Removed: [MariaDB 10.3.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1030-release-notes.md)



#### `<code>innodb_use_sys_malloc</code>`


* Description: If set the `<code>1</code>`, the default, XtraDB/InnoDB will use the operating system's memory allocator. If set to `<code>0</code>` it will use its own. Deprecated in [MariaDB 10.0](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md) and removed in [MariaDB 10.2](../../../../release-notes/mariadb-community-server/what-is-mariadb-102.md) along with InnoDB's internal memory allocator.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-use-sys-malloc={0|1}</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>boolean</code>`
* Default Value: `<code>ON</code>`
* Deprecated: [MariaDB 10.0](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md)
* Removed: [MariaDB 10.2.2](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1022-release-notes.md)



#### `<code>innodb_use_sys_stats_table</code>`


* Description: If set to `<code>1</code>` (`<code>0</code>` is default), XtraDB will use the SYS_STATS system table for extra table index statistics. When a table is opened for the first time, statistics will then be loaded from SYS_STATS instead of sampling the index pages. Statistics are designed to be maintained only by running an [ANALYZE TABLE](../../sql-statements-and-structure/sql-statements/table-statements/analyze-table.md). Replaced by MySQL 5.6's Persistent Optimizer Statistics.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">innodb-use-sys-stats-table={0|1}</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>boolean</code>`
* Default Value: `<code>0</code>`
* Removed: [MariaDB 10.0](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md)/XtraDB 5.6



#### `<code>innodb_use_trim</code>`


* Description: Use trim to free up space of compressed blocks.

  * See [InnoDB Page Compression: Saving Storage Space with Sparse Files](innodb-page-compression.md#saving-storage-space-with-sparse-files) for more information.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-use-trim={0|1}</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>boolean</code>`
* Default Value: `<code>ON</code>`
* Deprecated: [MariaDB 10.2.4](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1024-release-notes.md)
* Removed: [MariaDB 10.3.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1030-release-notes.md)



#### `<code>innodb_version</code>`


* Description: InnoDB version number. From [MariaDB 10.3.7](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1037-release-notes.md), as the InnoDB implementation in MariaDB has diverged from MySQL, the MariaDB version is instead reported. For example, the InnoDB version reported in [MariaDB 10.1](../../../../release-notes/mariadb-community-server/what-is-mariadb-1010.md) (which is based on MySQL 5.6) included encryption and variable-size page compression before MySQL 5.7 introduced them. [MariaDB 10.2](../../../../release-notes/mariadb-community-server/what-is-mariadb-102.md) (based on MySQL 5.7) introduced persistent AUTO_INCREMENT ([MDEV-6076](https://jira.mariadb.org/browse/MDEV-6076)) in a GA release before MySQL 8.0. [MariaDB 10.3](../../../../release-notes/mariadb-community-server/what-is-mariadb-103.md) (based on MySQL 5.7) introduced instant ADD COLUMN ([MDEV-11369](https://jira.mariadb.org/browse/MDEV-11369)) before MySQL.
* Scope: Global
* Dynamic: No
* Data Type: `<code>string</code>`
* Removed: [MariaDB 10.10](../../../../release-notes/mariadb-community-server/what-is-mariadb-1010.md)



#### `<code>innodb_write_io_threads</code>`


* Description: Prior to [MariaDB 10.5](../../../../release-notes/mariadb-community-server/what-is-mariadb-105.md), this was simply the number of I/O threads for InnoDB writes. From [MariaDB 10.5](../../../../release-notes/mariadb-community-server/what-is-mariadb-105.md), asynchronous I/O functionality in the InnoDB Background Thread Pool replaces the old InnoDB I/O Threads. This variable is now multipled by 256 to determine the maximum number of concurrent asynchronous I/O write requests that can be completed by the Background Thread Pool. The default is therefore 4*256 = 1024 conccurrent asynchronous write requests. You may on rare occasions need to reduce this default on Linux systems running multiple MariaDB servers to avoid exceeding system limits, or increase if spending too much time waiting on I/O requests.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-write-io-threads=#</code>`
* Scope: Global
* Dynamic: Yes (>= [MariaDB 10.11](../../../../release-notes/mariadb-community-server/what-is-mariadb-1011.md)), No (<= [MariaDB 10.10](../../../../release-notes/mariadb-community-server/what-is-mariadb-1010.md))
* Data Type: `<code>numeric</code>`
* Default Value: `<code>4</code>`
* Range: `<code>1</code>` to `<code>64</code>`


