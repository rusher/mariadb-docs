
# TokuDB System Variables


TokuDB has been deprecated by its upstream maintainer. It is disabled from [MariaDB 10.5](../../../../release-notes/mariadb-community-server/what-is-mariadb-105.md) and has been been removed in [MariaDB 10.6](../../../../release-notes/mariadb-community-server/what-is-mariadb-106.md) - [MDEV-19780](https://jira.mariadb.org/browse/MDEV-19780). We recommend [MyRocks](../myrocks/myrocks-in-mariadb-102-vs-mariadb-103.md) as a long-term migration path.



This page lists system variables that are related to [TokuDB](tokudb-resources.md).


See [Server System Variables](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md) for a complete list of system variables and instructions on setting them, and [Full list of MariaDB options, system and status variables](../../../server-management/variables-and-modes/full-list-of-mariadb-options-system-and-status-variables.md) for a complete list of all options, statis variable and system variables in MariaDB.


## System Variables


#### `<code>tokudb_alter_print_error</code>`


* Description: Print errors for alter table operations.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: boolean
* Default Value: `<code>OFF</code>`



#### `<code>tokudb_analyze_time</code>`


* Description: Time in seconds that [ANALYZE](../../sql-statements-and-structure/sql-statements/table-statements/analyze-table.md) operations spend on each index when calculating cardinality. Accurate cardinality helps in particular with the performance of complex queries. If no analyzes are run, cardinality will be 1 for primary indexes, and unknown (NULL) for other types of indexes.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: numeric
* Default Value: `<code>5</code>`
* Range: `<code>0</code>` to `<code>4294967295</code>`



#### `<code>tokudb_block_size</code>`


* Description: Uncompressed size of internal fractal tree and leaf nodes. Changing will only affect tables created after the new setting is in effect. Existing tables will keep the setting they were created with unless the table is dumped and reloaded.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: numeric
* Default Value: `<code>4194304</code>` (4MB)
* Range: `<code>0</code>` to `<code>18446744073709551615</code>`



#### `<code>tokudb_bulk_fetch</code>`


* Description: If set to `<code>1</code>` (the default), the bulk fetch algorithm is used for SELECT's and DELETE's, including related statements such as INSERT INTO.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: boolean
* Default Value: `<code>ON</code>`



#### `<code>tokudb_cache_size</code>`


* Description: Size in bytes of the TokuDB cache. This variable is read-only and cannot be changed dynamically. To change the value, either set the value in the `<code>my.cnf</code>` file prior to loading TokuDB or
restart MariaDB after modifying the configuration. If you have loaded the
plugin but not used TokuDB yet, you can unload the plugin then reload it and
MariaDB will reload the plugin with the setting from the configuration file. Setting to at least half of the available memory is recommended, although if using directIO instead of buffered IO (see [tokudb_directio](#tokudb_directio)) , up to 80% of the available memory is recommended. Decrease if other applications require significant memory or swapping is degrading performance.
* Dynamic: No
* Data Type: numeric
* Default Value: Half of the total system memory



#### `<code>tokudb_check_jemalloc</code>`


* Description: Check if jemalloc is linked.
* Scope: Global
* Dynamic: Yes
* Data Type: numeric
* Default Value: `<code>1</code>`
* Valid Values: `<code>0</code>` and `<code>1</code>`



#### `<code>tokudb_checkpoint_lock</code>`


* Description: Mechanism to lock out TokuDB checkpoints. When set to `<code>1</code>`, TokuDB checkpoints are locked out. Setting to `<code>0</code>`, or disconnecting the client, releases the lock.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: boolean
* Default Value: `<code>OFF</code>`



#### `<code>tokudb_checkpoint_on_flush_logs</code>`


* Description: TokuDB checkpoint on flush logs.
* Scope: Global
* Dynamic: Yes
* Data Type: boolean
* Default Value: `<code>OFF</code>`



#### `<code>tokudb_checkpointing_period</code>`


* Description: Time in seconds between the beginning of each checkpoint. It is recommended to leave this at the default setting of 1 minute.
* Scope: Global
* Dynamic: Yes
* Data Type: numeric
* Default Value: `<code>60</code>`
* Range: `<code>0</code>` to `<code>4294967295</code>`



#### `<code>tokudb_cleaner_iterations</code>`


* Description: Number of internal nodes processed in each cleaner thread period (see [tokudb_cleaner_period](#tokudb_cleaner_period)). Setting to `<code>0</code>` turns off cleaner threads.
* Scope: Global
* Dynamic: Yes
* Data Type: numeric
* Default Value: `<code>5</code>`
* Range: `<code>0</code>` to `<code>18446744073709551615</code>`



#### `<code>tokudb_cleaner_period</code>`


* Description: Frequency in seconds for the running of the cleaner thread. Setting to `<code>0</code>` turns off cleaner threads.
* Scope: Global
* Dynamic: Yes
* Data Type: numeric
* Default Value: `<code>1</code>`
* Range: `<code>0</code>` to `<code>18446744073709551615</code>`



#### `<code>tokudb_commit_sync</code>`


* Description: Whether or not the transaction log is flushed upon transaction commit. Flushing has a minor performance penalty, but switching it off means that committed transactions may not survive a server crash.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: boolean
* Default Value: `<code>ON</code>`



#### `<code>tokudb_create_index_online</code>`


* Description: Whether indexes are hot or not. Hot, or online, indexes (the default) mean that the table is available for inserting and updates while the index is being created. It is slower to create hot indexes.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: boolean
* Default Value: `<code>ON</code>`



#### `<code>tokudb_data_dir</code>`


* Description: Directory where the TokuDB data is stored. By default the variable is empty, in which case the regular [datadir](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#datadir) is used.
* Dynamic: No
* Data Type: string
* Default Value: Empty (the MariaDB datadir is used)



#### `<code>tokudb_debug</code>`


* Description: Setting to a non-zero value turns on various TokuDB debug traces.
* Scope: Global
* Dynamic: Yes
* Data Type: numeric
* Default Value: `<code>0</code>`
* Range: `<code>0</code>` to `<code>18446744073709551615</code>`



#### `<code>tokudb_directio</code>`


* Description: When set to ON, TokuDB writes use Direct IO instead of Buffered IO. [tokudb_cache_size](#tokudb_cache_size) should be adjusted when using DirectIO.
* Dynamic: No
* Data Type: boolean
* Default Value: `<code>OFF</code>`



#### `<code>tokudb_disable_hot_alter</code>`


* Description: If set to `<code>ON</code>` (`<code>OFF</code>` is default), hot alter table is disabled.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: boolean
* Default Value: `<code>OFF</code>`



#### `<code>tokudb_disable_prefetching</code>`


* Description: If prefetching is not disabled (the default), range queries usually benefit from aggressive prefetching of blocks of rows. For range queries with LIMIT clauses, this can create unnecessary IO, and so prefetching can be disabled if these make up a majority of range queries.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: boolean
* Default Value: `<code>OFF</code>`



#### `<code>tokudb_disable_slow_alter</code>`


* Description: Usually, TokuDB permits column addition, deletion, expansion, and renaming with minimal locking, very quickly. This variable determines whether certain slow [alter|ALTER]] table statements that cannot take advantage of this feature are permitted. Statements that are slow are those that include a mix of column additions, deletions or expansions, for example, `<code>ALTER TABLE t1 ADD COLUMN c1 int, DROP COLUMN c2</code>`.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: boolean
* Default Value: `<code>OFF</code>`



#### `<code>tokudb_empty_scan</code>`


* Description: TokuDB algorithm to check if the table is empty when opened. Setting to `<code>disabled</code>` will reduce this overhead.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: enum
* Default Value: `<code>rl</code>`
* Valid Values: `<code>lr</code>`, `<code>rl</code>`, `<code>disabled</code>`



#### `<code>tokudb_fs_reserve_percent</code>`


* Description: If this percentage of the filesystem is not free, inserts will be prohibited. Recommended value is half the size of the available memory. Once disabled, inserts will be re-enabled once twice the reserve is available. TokuDB will freeze entirely if the disk becomes entirely full.
* Scope: Global
* Dynamic: No
* Data Type: numeric
* Default Value: `<code>5</code>`



#### `<code>tokudb_fsync_log_period</code>`


* Description: fsync() operations frequency in milliseconds. If set to `<code>0</code>`, the default, [tokudb_commit_sync](#tokudb_commit_sync) control fsync() behavior.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: numeric
* Default Value: `<code>0</code>`
* Range: `<code>0</code>` to `<code>18446744073709551615</code>`


**Warning**: currently values in the 1000-2000 range seem to cause server crashes, see [MDEV-16732](https://jira.mariadb.org/browse/MDEV-16732)



#### `<code>tokudb_hide_default_row_format</code>`


* Description: Hide the default row format.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: boolean
* Default Value: `<code>ON</code>`



#### `<code>tokudb_killed_time</code>`


* Description: Control lock tree kill callback frequency.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: numeric
* Default Value: `<code>4000</code>`
* Range: `<code>0</code>` to `<code>18446744073709551615</code>`
* Introduced: TokuDB 7.1.5



#### `<code>tokudb_last_lock_timeout</code>`


* Description: Empty by default, when a lock deadlock is detected, or a lock request times out, set to a JSON document describing the most recent lock conflict. Only set when the first bit of [tokudb_lock_timeout_debug](#tokudb_lock_timeout_debug) is set.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: text
* Default Value: Empty



#### `<code>tokudb_load_save_space</code>`


* Description: If set to `<code>1</code>`, the default, bulk loader intermediate data is compressed, otherwise it is uncompressed. Also see [tokudb_tmp_dir](#tokudb_tmp_dir).
* Scope: Global, Session
* Dynamic: Yes
* Data Type: boolean
* Default Value: `<code>ON</code>`



#### `<code>tokudb_loader_memory_size</code>`


* Description: Memory limit for each loader instance used by the TokuDB bulk loader. Memory is taken from the TokuDB cache ([tokudb_cache_size](#tokudb_cache_size)), so current cache data may need to be cleared for the loader to begin. Increase if tables are very larger, with multiple secondary indexes.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: numeric
* Default Value: `<code>100000000</code>` (100M)
* Range: `<code>0</code>` to `<code>18446744073709551615</code>`



#### `<code>tokudb_lock_timeout</code>`


* Description: Time in milliseconds that a transaction will wait for a lock held by another transaction to be released before timing out with a `<code>lock wait timeout</code>` error (-30994). Setting to `<code>0</code>` disables lock waits.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: numeric
* Default Value: `<code>4000</code>` (4 seconds)
* Range: `<code>0</code>` to `<code>18446744073709551615</code>`



#### `<code>tokudb_lock_timeout_debug</code>`


* Description: When bit zero is set (default `<code>1</code>`), a JSON document describing the most recent lock conflict is reported to [tokudb_last_lock_timeout](#tokudb_last_lock_timeout). When set to `<code>0</code>`, no lock conflicts are reported. When bit one is set, the JSON document is printed to the [error log](../../../server-management/server-monitoring-logs/error-log.md).
* Scope: Global, Session
* Dynamic: Yes
* Data Type: numeric
* Default Value: `<code>1</code>`



#### `<code>tokudb_log_dir</code>`


* Description: Directory where the TokuDB log files are stored. By default the variable is empty, in which case the regular [datadir](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#datadir) is used.
* Dynamic: No
* Data Type: string
* Default Value: Empty (the MariaDB datadir is used)



#### `<code>tokudb_max_lock_memory</code>`


* Description: Max memory for locks.
* Scope: Global, Session
* Dynamic: No
* Data Type: numeric
* Default Value: `<code>130653952</code>`



#### `<code>tokudb_optimize_index_fraction</code>`


* Description: When deleting a percentage of the tree (useful when the left side of the tree has many deletions, such as a pattern with increasing ids or dates), it's possible to optimize a subset of the fractal tree, as determined by the value of this variable, which ranges from `<code>0.0</code>` to `<code>1.0</code>` (indicating the whole tree).
* Scope: Global, Session
* Dynamic: Yes
* Data Type: numeric
* Default Value: `<code>1.000000</code>`
* Range: `<code>0.0</code>` to `<code>1.0</code>`
* Introduced: TokuDB 7.5.5



#### `<code>tokudb_optimize_index_name</code>`


* Description: If set to an index name, will optimize that single index in a table. Empty by default.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: string
* Default Value: None
* Introduced: TokuDB 7.5.5



#### `<code>tokudb_optimize_throttle</code>`


* Description: Table optimization utilizes all available resources by default. This variable allows the table optimization speed to be limited in order to reduce the overall resources used. The limit places an upper bound on the number of fractal tree leaf nodes that are optimized per second. `<code>0</code>`, the default, imposes no limit.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: numeric
* Default Value: `<code>0</code>`
* Range: `<code>0</code>` to `<code>18446744073709551615</code>`
* Introduced: TokuDB 7.5.5



#### `<code>tokudb_pk_insert_mode</code>`


* Description: Mode for primary key inserts using either [REPLACE INTO](../../sql-statements-and-structure/sql-statements/built-in-functions/string-functions/replace-function.md) or [INSERT IGNORE](../../sql-statements-and-structure/sql-statements/data-manipulation/inserting-loading-data/ignore.md) on tables with no secondary index, or where all columns in the secondary index are in the primary key. For example `<code>PRIMARY KEY (a,b,c), key (b,c)</code>`

  * `<code>0</code>`: Fast inserts. [Triggers](../../../server-usage/programming-customizing-mariadb/triggers-events/triggers/triggers-and-implicit-locks.md) may not work, and [row-based replication](../../../server-management/server-monitoring-logs/binary-log/binary-log-formats.md) will not work
  * `<code>1</code>`: Fast inserts if no triggers are defined, otherwise inserts may be slow. Row-based replication will not work.
  * `<code>2</code>`: Slow inserts. Triggers and row-based replication work normally.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: enumerated
* Default Value: `<code>1</code>`
* Valid Values: `<code>0</code>`, `<code>1</code>`, `<code>2</code>`



#### `<code>tokudb_prelock_empty</code>`


* Description: If set to `<code>0</code>` (`<code>1</code>` is default), fast bulk loading will be switched off. Usually, TokuDB obtains a table lock on empty tables. If, as is usual, only one transaction is loading the table, this speeds up the inserts. However, if many transactions are loading, only one can have access at a time, so setting this to `<code>0</code>`, avoiding the lock, will speed inserts up in that situation.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: boolean
* Default Value: `<code>ON</code>`



#### `<code>tokudb_read_block_size</code>`


* Description: Uncompressed size in bytes of the read blocks of the fractal tree leaves. Changing will only affect tables created after the new setting is in effect. Existing tables will keep the setting they were created with unless the table is dumped and reloaded. Larger values are better for large range scans and higher compressions, while smaller values are better for point and small range scans.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: numeric
* Default Value: `<code>65536</code>` (64KB)
* Range: `<code>4096</code>` to `<code>4294967295</code>`



#### `<code>tokudb_read_buf_size</code>`


* Description: Per-client size in bytes of the buffer used for storing bulk fetched values as part of a large range query. Reduce if there are many simultaneous clients. Setting to `<code>0</code>` disables bulk fetching.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: numeric
* Default Value: `<code>131072</code>` (128KB)
* Range: `<code>0</code>` to `<code>1048576</code>`



#### `<code>tokudb_read_status_frequency</code>`


* Description: Progress is measured every this many reads for display by [SHOW PROCESSLIST](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-processlist.md). Useful to set to `<code>1</code>` to examine slow queries.
* Scope: Global,
* Dynamic: Yes
* Data Type: numeric
* Default Value: `<code>10000</code>`
* Range: `<code>0</code>` to `<code>4294967295</code>`



#### `<code>tokudb_row_format</code>`


* Description: Compression algorithm used by default to compress data. Can be overridden by a row format specified in the [CREATE TABLE](../../sql-statements-and-structure/vectors/create-table-with-vectors.md) statement. note that the library can be specified directly, or an alias used, the mapping of which may change in future. Note that in [MariaDB 5.5](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5.md), and before [MariaDB 10.0.10](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-10010-release-notes.md), the compression type did not default to this value. See [TokuDB Differences](tokudb-differences.md).

  * `<code>tokudb_default</code>`, `<code>tokudb_zlib</code>`: Use the zlib library,
  * `<code>tokudb_fast</code>`, `<code>tokudb_quicklz</code>`: Use the quicklz library, the lightest compression with low CPU usage,
  * `<code>tokudb_small</code>`, `<code>tokudb_lzma</code>`: Use the lzma library. the highest compression and highest CPU usage
  * `<code>tokudb_uncompressed</code>`: No compression is used.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: enumerated
* Default Value: `<code>tokudb_zlib</code>`
* Valid Values: `<code>tokudb_default</code>`, `<code>tokudb_fast</code>`, `<code>tokudb_small</code>`, `<code>tokudb_zlib</code>`, `<code>tokudb_quicklz</code>`, `<code>tokudb_lzma</code>`, `<code>tokudb_uncompressed</code>`



#### `<code>tokudb_rpl_check_readonly</code>`


* Description: By default, when the slave is in read only mode, row events will be run from the binary log using TokuDB's read-free replication (RFR). Setting this variable to `<code>OFF</code>` turns off the slave read only check, allowing RFR to run when the slave is not read-only. Be careful that you understand the consequences if setting this variable.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: boolean
* Default Value: `<code>ON</code>`



#### `<code>tokudb_rpl_lookup_rows</code>`


* Description: If set to `<code>OFF</code>` (`<code>ON</code>` is default), and [binlog_format](../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md) to `<code>ROW</code>` and [read_only](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#read_only) to `<code>ON</code>`, TokuDB replication slaves will not perform row lookups for update or delete row log events, removing the need for the associated IO.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: boolean
* Default Value: `<code>ON</code>`



#### `<code>tokudb_rpl_lookup_rows_delay</code>`


* Description: Can be used to simulate long disk reads by sleeping for the specified time, in microseconds, before the row lookup query. Only useful to change in a test environment.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: numeric
* Default Value: `<code>0</code>`



#### `<code>tokudb_rpl_unique_checks</code>`


* Description: If set to `<code>OFF</code>` (`<code>ON</code>` is default), and [binlog_format](../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md) to `<code>ROW</code>` and [read_only](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#read_only) to `<code>ON</code>`, TokuDB replication slaves will skip uniqueness checks on inserts and updates, removing the associated IO.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: boolean
* Default Value: `<code>ON</code>`



#### `<code>tokudb_rpl_unique_checks_delay</code>`


* Description: Can be used to simulate long disk reads by sleeping for the specified time, in microseconds, before the row lookup query. Only useful to change in a test environment.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: numeric
* Default Value: `<code>0</code>`



#### `<code>tokudb_support_xa</code>`


* Description: Whether or not the prepare phase of an XA transaction performs an fsync().
* Scope: Global, Session
* Dynamic: Yes
* Data Type: boolean
* Default Value: `<code>ON</code>`



#### `<code>tokudb_tmp_dir</code>`


* Description: Directory where the TokuDB bulk loaders temporary files are stored. Can be very large, and useful to place on a separate disk. By default the variable is empty, in which case the regular [datadir](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#datadir) is used. [tokudb_load_save_space](#tokudb_load_save_space) determines whether the data is compressed or not. The error message `<code>ERROR 1030 (HY000): Got error 1 from storage engine</code>` could indicate that the disk has run out of space.
* Dynamic: No
* Data Type: `<code>directory name</code>`
* Default Value: Empty (the MariaDB datadir is used)



#### `<code>tokudb_version</code>`


* Description: The TokuDB version of the plugin included on MariaDB.
* Dynamic: No
* Data Type: `<code>string</code>`


#### `<code>tokudb_write_status_frequency</code>`


* Description: Progress is measured every this many writes for display by [SHOW PROCESSLIST](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-processlist.md). Useful to set to `<code>1</code>` to examine slow queries.
* Scope: Global,
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>1000</code>`
* Range: `<code>0</code>` to `<code>4294967295</code>`


