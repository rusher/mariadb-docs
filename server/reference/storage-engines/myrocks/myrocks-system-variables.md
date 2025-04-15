
# MyRocks System Variables

This page documents system variables related to the [MyRocks](myrocks-in-mariadb-102-vs-mariadb-103.md) storage engine. See [Server System Variables](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md) for a complete list of system variables and instructions on setting them.


See also the [Full list of MariaDB options, system and status variables](../../../server-management/variables-and-modes/full-list-of-mariadb-options-system-and-status-variables.md).


#### `<code>rocksdb_access_hint_on_compaction_start</code>`


* Description: DBOptions::access_hint_on_compaction_start for RocksDB. Specifies the file access pattern, applied to all input files, once a compaction starts.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-access-hint-on-compaction-start=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value: `<code>1</code>`
* Range: `<code>0</code>` to `<code>3</code>`



#### `<code>rocksdb_advise_random_on_open</code>`


* Description: DBOptions::advise_random_on_open for RocksDB.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-advise-random-on-open={0|1}</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>boolean</code>`
* Default Value: `<code>ON</code>`



#### `<code>rocksdb_allow_concurrent_memtable_write</code>`


* Description: DBOptions::allow_concurrent_memtable_write for RocksDB.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-allow-concurrent-memtable-write={0|1}</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`



#### `<code>rocksdb_allow_mmap_reads</code>`


* Description: DBOptions::allow_mmap_reads for RocksDB
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-allow-mmap-reads={0|1}</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`



#### `<code>rocksdb_allow_mmap_writes</code>`


* Description: DBOptions::allow_mmap_writes for RocksDB
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-allow-mmap-writes={0|1}</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`



#### `<code>rocksdb_allow_to_start_after_corruption</code>`


* Description: Allow server still to start successfully even if RocksDB corruption is detected.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-allow-to-start-after-corruption={0|1}</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`
* Introduced: [MariaDB 10.3.7](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1037-release-notes.md), [MariaDB 10.2.15](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-10215-release-notes.md)



#### `<code>rocksdb_background_sync</code>`


* Description: Turns on background syncs for RocksDB
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-background-sync={0|1}</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`
* Removed: [MariaDB 10.3.1](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1031-release-notes.md), [MariaDB 10.2.8](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1028-release-notes.md)



#### `<code>rocksdb_base_background_compactions</code>`


* Description: DBOptions::base_background_compactions for RocksDB
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-base-background-compactions=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value: `<code>1</code>`
* Range: `<code>-1</code>` to `<code>64</code>`
* Removed: [MariaDB 10.3.1](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1031-release-notes.md), [MariaDB 10.2.8](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1028-release-notes.md)



#### `<code>rocksdb_blind_delete_primary_key</code>`


* Description: Deleting rows by primary key lookup, without reading rows (Blind Deletes). Blind delete is disabled if the table has secondary key.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-blind-delete-primary-key={0|1}</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`



#### `<code>rocksdb_block_cache_size</code>`


* Description: Block_cache size for RocksDB (block size 1024)
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-block-cache-size=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>536870912</code>`
* Range: `<code>1024</code>` to `<code>9223372036854775807</code>`


To see the statistics of block cache usage, check `<code>SHOW ENGINE ROCKSDB STATUS</code>` output
(search for lines starting with `<code>rocksdb.block.cache</code>`).


One can check the size of data of the block cache in `<code>DB_BLOCK_CACHE_USAGE</code>`
column of the `<code>INFORMATION_SCHEMA.ROCKSDB_DBSTATS</code>` table.



#### `<code>rocksdb_block_restart_interval</code>`


* Description: BlockBasedTableOptions::block_restart_interval for RocksDB
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-block-restart-interval=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value: `<code>16</code>`
* Range: `<code>1</code>` to `<code>2147483647</code>`



#### `<code>rocksdb_block_size</code>`


* Description: BlockBasedTableOptions::block_size for RocksDB
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-block-size=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value: `<code>4096</code>`
* Range: `<code>1</code>` to `<code>18446744073709551615</code>`



#### `<code>rocksdb_block_size_deviation</code>`


* Description: BlockBasedTableOptions::block_size_deviation for RocksDB
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-block-size-deviation=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value: `<code>10</code>`
* Range: `<code>0</code>` to `<code>2147483647</code>`



#### `<code>rocksdb_bulk_load</code>`


* Description: Use bulk-load mode for inserts. This disables unique_checks and enables rocksdb_commit_in_the_middle.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-bulk-load={0|1}</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`



#### `<code>rocksdb_bulk_load_allow_sk</code>`


* Description: Allow bulk loading of sk keys during bulk-load. Can be changed only when bulk load is disabled.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-bulk-load_allow_sk={0|1}</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`
* Introduced: [MariaDB 10.3.10](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-10310-release-notes.md), [MariaDB 10.2.18](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-10218-release-notes.md)



#### `<code>rocksdb_bulk_load_allow_unsorted</code>`


* Description: Allow unsorted input during bulk-load. Can be changed only when bulk load is disabled.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-bulk-load_allow_unsorted={0|1}</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`



#### `<code>rocksdb_bulk_load_size</code>`


* Description: Maximum number of records in a batch for bulk-load mode.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-bulk-load-size=#</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>1000</code>`
* Range: `<code>1</code>` to `<code>1073741824</code>`



#### `<code>rocksdb_bytes_per_sync</code>`


* Description: DBOptions::bytes_per_sync for RocksDB.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-bytes-per-sync=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>0</code>`
* Range: `<code>0</code>` to `<code>18446744073709551615</code>`



#### `<code>rocksdb_cache_dump</code>`


* Description: Include RocksDB block cache content in core dump.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-cache-dump={0|1}</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>ON</code>`
* Introduced: [MariaDB 10.4.7](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-4-series/mariadb-1047-release-notes.md), [MariaDB 10.3.17](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-10317-release-notes.md), [MariaDB 10.2.26](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-10226-release-notes.md)



#### `<code>rocksdb_cache_high_pri_pool_ratio</code>`


* Description: Specify the size of block cache high-pri pool.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-cache-high-pri-pool-ratio=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>double</code>`
* Default Value: `<code>0.000000</code>`
* Range: `<code>0</code>` to `<code>1</code>`
* Introduced: [MariaDB 10.4.7](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-4-series/mariadb-1047-release-notes.md), [MariaDB 10.3.17](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-10317-release-notes.md), [MariaDB 10.2.26](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-10226-release-notes.md)



#### `<code>rocksdb_cache_index_and_filter_blocks</code>`


* Description: BlockBasedTableOptions::cache_index_and_filter_blocks for RocksDB.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-cache-index-and-filter-blocks={0|1}</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>boolean</code>`
* Default Value: `<code>ON</code>`



#### `<code>rocksdb_cache_index_and_filter_with_high_priority</code>`


* Description: cache_index_and_filter_blocks_with_high_priority for RocksDB.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-cache-index-and-filter-with-high-priority={0|1}</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>boolean</code>`
* Default Value: `<code>ON</code>`
* Introduced: [MariaDB 10.4.7](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-4-series/mariadb-1047-release-notes.md), [MariaDB 10.3.17](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-10317-release-notes.md), [MariaDB 10.2.26](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-10226-release-notes.md)



#### `<code>rocksdb_checksums_pct</code>`


* Description: Percentage of rows to be checksummed.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-checksums-pct=#</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>100</code>`
* Range: `<code>0</code>` to `<code>100</code>`



#### `<code>rocksdb_collect_sst_properties</code>`


* Description: Enables collecting SST file properties on each flush.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-collect-sst-properties={0|1}</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>boolean</code>`
* Default Value: `<code>ON</code>`



#### `<code>rocksdb_commit_in_the_middle</code>`


* Description: Commit rows implicitly every rocksdb_bulk_load_size, on bulk load/insert, update and delete.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-commit-in-the-middle={0|1}</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`



#### `<code>rocksdb_commit_time_batch_for_recovery</code>`


* Description: TransactionOptions::commit_time_batch_for_recovery for RocksDB.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-commit-time-batch-for-recovery={0|1}</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`
* Introduced: [MariaDB 10.3.10](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-10310-release-notes.md), [MariaDB 10.2.18](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-10218-release-notes.md)



#### `<code>rocksdb_compact_cf</code>`


* Description: Compact column family.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-compact-cf=value</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>string</code>`
* Default Value: (Empty)



#### `<code>rocksdb_compaction_readahead_size</code>`


* Description: DBOptions::compaction_readahead_size for RocksDB.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-compaction-readahead-size=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>0</code>`
* Range: `<code>0</code>` to `<code>18446744073709551615</code>`



#### `<code>rocksdb_compaction_sequential_deletes</code>`


* Description: RocksDB will trigger compaction for the file if it has more than this number sequential deletes per window.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-compaction-sequential-deletes=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>0</code>`
* Range: `<code>0</code>` to `<code>2000000</code>`



#### `<code>rocksdb_compaction_sequential_deletes_count_sd</code>`


* Description: Counting SingleDelete as rocksdb_compaction_sequential_deletes.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-compaction-sequential-deletes-count-sd={0|1}</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`



#### `<code>rocksdb_compaction_sequential_deletes_file_size</code>`


* Description: Minimum file size required for compaction_sequential_deletes.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-compaction-sequential-deletes-file-size=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>0</code>`
* Range: `<code>-1</code>` to `<code>9223372036854775807</code>`



#### `<code>rocksdb_compaction_sequential_deletes_window</code>`


* Description: Size of the window for counting rocksdb_compaction_sequential_deletes.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-compaction-sequential-deletes-window=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>0</code>`
* Range: `<code>0</code>` to `<code>2000000</code>`



#### `<code>rocksdb_concurrent_prepare</code>`


* Description: DBOptions::concurrent_prepare for RocksDB.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-coconcurrent-prepare={0|1}</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>boolean</code>`
* Default Value: `<code>1</code>`
* Removed: [MariaDB 10.3.7](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1037-release-notes.md), [MariaDB 10.2.15](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-10215-release-notes.md)



#### `<code>rocksdb_create_checkpoint</code>`


* Description: Checkpoint directory.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-create-checkpoint=value</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>string</code>`
* Default Value: (Empty)



#### `<code>rocksdb_create_if_missing</code>`


* Description: DBOptions::create_if_missing for RocksDB.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-create-if-missing={0|1}</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>boolean</code>`
* Default Value: `<code>ON</code>`



#### `<code>rocksdb_create_missing_column_families</code>`


* Description: DBOptions::create_missing_column_families for RocksDB.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-create-missing-column-families={0|1}</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`



#### `<code>rocksdb_datadir</code>`


* Description: RocksDB data directory.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-datadir[=value]</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>string</code>`
* Default Value: `<code>./#rocksdb</code>`



#### `<code>rocksdb_db_write_buffer_size</code>`


* Description: DBOptions::db_write_buffer_size for RocksDB.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-db-write-buffer-size=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value: `<code>0</code>`
* Range: `<code>0</code>` to `<code>18446744073709551615</code>`



#### `<code>rocksdb_deadlock_detect</code>`


* Description: Enables deadlock detection.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-deadlock-detect={0|1}</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`



#### `<code>rocksdb_deadlock_detect_depth</code>`


* Description: Number of transactions deadlock detection will traverse through before assuming deadlock.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-deadlock-detect-depth=#</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>50</code>`
* Range: `<code>2</code>` to `<code>18446744073709551615</code>`



#### `<code>rocksdb_debug_manual_compaction_delay</code>`


* Description: For debugging purposes only. Sleeping specified seconds for simulating long running compactions.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-debug_manual_compaction_delay=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>0</code>`
* Range: `<code>0</code>` to `<code>4294967295</code>`
* Introduced: [MariaDB 10.3.10](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-10310-release-notes.md), [MariaDB 10.2.18](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-10218-release-notes.md)



#### `<code>rocksdb_debug_optimizer_no_zero_cardinality</code>`


* Description: If cardinality is zero, override it with some value.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-debug-optimizer-no-zero-cardinality={0|1}</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>ON</code>`



#### `<code>rocksdb_debug_ttl_ignore_pk</code>`


* Description: For debugging purposes only. If true, compaction filtering will not occur on PK TTL data. This variable is a no-op in non-debug builds.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-debug-ttl-ignore-pk={0|1}</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`



#### `<code>rocksdb_debug_ttl_read_filter_ts</code>`


* Description: For debugging purposes only. Overrides the TTL read filtering time to time + debug_ttl_read_filter_ts. A value of 0 denotes that the variable is not set. This variable is a no-op in non-debug builds.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-debug-ttl-read-filter-ts=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>0</code>`
* Range: `<code>-3600</code>` to `<code>3600</code>`
* Introduced: [MariaDB 10.3.1](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1031-release-notes.md), [MariaDB 10.2.8](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1028-release-notes.md)



#### `<code>rocksdb_debug_ttl_rec_ts</code>`


* Description: For debugging purposes only. Overrides the TTL of records to now() + debug_ttl_rec_ts. The value can be +/- to simulate a record inserted in the past vs a record inserted in the 'future'. A value of 0 denotes that the variable is not set. This variable is a no-op in non-debug builds.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-debug-ttl-read-filter-ts=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>0</code>`
* Range: `<code>-3600</code>` to `<code>3600</code>`
* Introduced: [MariaDB 10.3.1](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1031-release-notes.md), [MariaDB 10.2.8](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1028-release-notes.md)



#### `<code>rocksdb_debug_ttl_snapshot_ts</code>`


* Description: For debugging purposes only. Sets the snapshot during compaction to now() + debug_set_ttl_snapshot_ts. The value can be positive or negative to simulate a snapshot in the past vs a snapshot created in the 'future'. A value of 0 denotes that the variable is not set. This variable is a no-op in non-debug builds.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-debug-ttl-snapshot-ts=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>0</code>`
* Range: `<code>-3600</code>` to `<code>3600</code>`
* Introduced: [MariaDB 10.3.1](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1031-release-notes.md), [MariaDB 10.2.8](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1028-release-notes.md)



#### `<code>rocksdb_default_cf_options</code>`


* Description: Default cf options for RocksDB.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-default-cf-options=value</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>string</code>`
* Default Value: (Empty)



#### `<code>rocksdb_delayed_write_rate</code>`


* Description: DBOptions::delayed_write_rate.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-delayed-write-rate=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>0</code>` (Previously `<code>16777216</code>`)
* Range: `<code>0</code>` to `<code>18446744073709551615</code>`



#### `<code>rocksdb_delete_cf</code>`


* Description: Delete column family.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-delete-cf=val</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>string</code>`
* Default Value: (Empty string)
* Introduced: [MariaDB 10.4.7](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-4-series/mariadb-1047-release-notes.md), [MariaDB 10.3.17](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-10317-release-notes.md), [MariaDB 10.2.26](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-10226-release-notes.md)



#### `<code>rocksdb_delete_obsolete_files_period_micros</code>`


* Description: DBOptions::delete_obsolete_files_period_micros for RocksDB.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-delete-obsolete-files-period-micros=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value: `<code>21600000000</code>`
* Range: `<code>0</code>` to `<code>9223372036854775807</code>`



#### `<code>rocksdb_enable_2pc</code>`


* Description: Enable two phase commit for MyRocks. When set, MyRocks will keep its data consistent with the [binary log](../innodb/binary-log-group-commit-and-innodb-flushing-performance.md) (in other words, the server will be a crash-safe master). The consistency is achieved by doing two-phase XA commit with the binary log.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-enable-2pc={0|1}</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>ON</code>`



#### `<code>rocksdb_enable_bulk_load_api</code>`


* Description: Enables using SstFileWriter for bulk loading.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-enable-bulk-load-api={0|1}</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>boolean</code>`
* Default Value: `<code>ON</code>`



#### `<code>rocksdb_enable_insert_with_update_caching</code>`


* Description: Whether to enable optimization where we cache the read from a failed insertion attempt in [INSERT ON DUPLICATE KEY UPDATE](../../sql-statements-and-structure/sql-statements/data-manipulation/inserting-loading-data/insert-on-duplicate-key-update.md).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-enable-insert-with-update-caching={0|1}</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>ON</code>`
* Introduced: [MariaDB 10.4.7](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-4-series/mariadb-1047-release-notes.md), [MariaDB 10.3.17](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-10317-release-notes.md), [MariaDB 10.2.26](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-10226-release-notes.md)



#### `<code>rocksdb_enable_thread_tracking</code>`


* Description: DBOptions::enable_thread_tracking for RocksDB.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-enable-thread-tracking={0|1}</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`



#### `<code>rocksdb_enable_ttl</code>`


* Description: Enable expired TTL records to be dropped during compaction.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-enable-ttl={0|1}</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>ON</code>`
* Introduced: [MariaDB 10.3.1](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1031-release-notes.md), [MariaDB 10.2.8](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1028-release-notes.md)



#### `<code>rocksdb_enable_ttl_read_filtering</code>`


* Description: For tables with TTL, expired records are skipped/filtered out during processing and in query results. Disabling this will allow these records to be seen, but as a result rows may disappear in the middle of transactions as they are dropped during compaction. Use with caution.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-enable-ttl-read-filtering={0|1}</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>ON</code>`
* Introduced: [MariaDB 10.3.1](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1031-release-notes.md), [MariaDB 10.2.8](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1028-release-notes.md)



#### `<code>rocksdb_enable_write_thread_adaptive_yield</code>`


* Description: DBOptions::enable_write_thread_adaptive_yield for RocksDB.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-enable-write-thread-adaptive-yield={0|1}</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`



#### `<code>rocksdb_error_if_exists</code>`


* Description: DBOptions::error_if_exists for RocksDBB.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-error-if-exists={0|1}</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`



#### `<code>rocksdb_error_on_suboptimal_collation</code>`


* Description: Raise an error instead of warning if a sub-optimal collation is used.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-error-on-suboptimal-collation={0|1}</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>boolean</code>`
* Default Value: `<code>ON</code>`
* Introduced: [MariaDB 10.3.10](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-10310-release-notes.md), [MariaDB 10.2.18](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-10218-release-notes.md)



#### `<code>rocksdb_flush_log_at_trx_commit</code>`


* Description: Sync on transaction commit. Similar to [innodb_flush_log_at_trx_commit](../innodb/innodb-system-variables.md#innodb_flush_log_at_trx_commit). One can check the flushing by examining the [rocksdb_wal_synced](myrocks-status-variables.md#rocksdb_wal_synced) and [rocksdb_wal_bytes](myrocks-status-variables.md#rocksdb_wal_bytes) status variables.

  * 1: Always sync on commit (the default).
  * 0: Never sync.
  * 2: Sync based on a timer controlled via rocksdb-background-sync.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-flush-log-at-trx-commit=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>1</code>`
* Range: `<code>0</code>` to `<code>2</code>`



#### `<code>rocksdb_flush_memtable_on_analyze</code>`


* Description: Forces memtable flush on ANALZYE table to get accurate cardinality.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-flush-memtable-on-analyze={0|1}</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>ON</code>`
* Removed: [MariaDB 10.3.7](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1037-release-notes.md), [MariaDB 10.2.15](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-10215-release-notes.md)



#### `<code>rocksdb_force_compute_memtable_stats</code>`


* Description: Force to always compute memtable stats.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-force-compute-memtable-stats={0|1}</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>ON</code>`



#### `<code>rocksdb_force_compute_memtable_stats_cachetime</code>`


* Description: Time in usecs to cache memtable estimates.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-force-compute-memtable-stats-cachetime=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>60000000</code>`
* Range: `<code>0</code>` to `<code>2147483647</code>`



#### `<code>rocksdb_force_flush_memtable_and_lzero_now</code>`


* Description: Acts similar to force_flush_memtable_now, but also compacts all L0 files.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-force-flush-memtable-and-lzero-now={0|1}</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`
* Introduced: [MariaDB 10.3.1](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1031-release-notes.md), [MariaDB 10.2.8](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1028-release-notes.md)



#### `<code>rocksdb_force_flush_memtable_now</code>`


* Description: Forces memstore flush which may block all write requests so be careful.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-force-flush-memtable-now={0|1}</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`



#### `<code>rocksdb_force_index_records_in_range</code>`


* Description: Used to override the result of records_in_range() when [FORCE INDEX](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/query-optimizations/force-index.md) is used.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-force-index-records-in-range=#</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>0</code>`
* Range: `<code>0</code>` to `<code>2147483647</code>`



#### `<code>rocksdb_git_hash</code>`


* Description: Git revision of the RocksDB library used by MyRocks.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-git-hash=value=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>string</code>`
* Default Value: As per git revision.



#### `<code>rocksdb_hash_index_allow_collision</code>`


* Description: BlockBasedTableOptions::hash_index_allow_collision for RocksDB.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-hash-index-allow-collision={0|1}</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>boolean</code>`
* Default Value: `<code>ON</code>`



#### `<code>rocksdb_ignore_unknown_options</code>`


* Description: Enable ignoring unknown options passed to RocksDB.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-ignore-unknown-options={0|1}</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>boolean</code>`
* Default Value: `<code>ON</code>`
* Introduced: [MariaDB 10.3.7](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1037-release-notes.md), [MariaDB 10.2.15](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-10215-release-notes.md)



#### `<code>rocksdb_index_type</code>`


* Description: BlockBasedTableOptions::index_type for RocksDB.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-index-type=value</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>enum</code>`
* Default Value: `<code>kBinarySearch</code>`
* Valid Values: `<code>kBinarySearch</code>`, `<code>kHashSearch</code>`



#### `<code>rocksdb_info_log_level</code>`


* Description: Filter level for info logs to be written mysqld error log. Valid values include 'debug_level', 'info_level', 'warn_level', 'error_level' and 'fatal_level'.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-info-log-level=value</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>enum</code>`
* Default Value: `<code>error_level</code>`
* Valid Values: `<code>error_level</code>`, `<code>debug_level</code>`, `<code>info_level</code>`, `<code>warn_level</code>`, `<code>fatal_level</code>`



#### `<code>rocksdb_io_write_timeout</code>`


* Description: Timeout for experimental I/O watchdog.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-io-write-timeout=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>0</code>`
* Valid Values: `<code>0</code>` to `<code>4294967295</code>`
* Introduced: [MariaDB 10.3.1](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1031-release-notes.md), [MariaDB 10.2.8](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1028-release-notes.md)



#### `<code>rocksdb_is_fd_close_on_exec</code>`


* Description: DBOptions::is_fd_close_on_exec for RocksDB.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-is-fd-close-on-exec={0|1}</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>boolean</code>`
* Default Value: `<code>ON</code>`



#### `<code>rocksdb_keep_log_file_num</code>`


* Description: DBOptions::keep_log_file_num for RocksDB.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-keep-log-file-num=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value: `<code>1000</code>`
* Range: `<code>0</code>` to `<code>18446744073709551615</code>`



#### `<code>rocksdb_large_prefix</code>`


* Description: Support large index prefix length of 3072 bytes. If off, the maximum index prefix length is 767.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-large_prefix={0|1}</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`



#### `<code>rocksdb_lock_scanned_rows</code>`


* Description: Take and hold locks on rows that are scanned but not updated.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-lock-scanned-rows={0|1}</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`



#### `<code>rocksdb_lock_wait_timeout</code>`


* Description: Number of seconds to wait for lock.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-lock-wait-timeout=#</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>1</code>`
* Range: `<code>1</code>` to `<code>1073741824</code>`



#### `<code>rocksdb_log_dir</code>`


* Description: DBOptions::log_dir for RocksDB. Where the log files are stored. An empty value implies `<code>rocksdb_datadir</code>` is used as the directory.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-log-dir=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>string</code>`
* Default Value: (Empty)
* Introduced: [MariaDB 10.9.1](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-9-series/mariadb-1091-release-notes.md)



#### `<code>rocksdb_log_file_time_to_roll</code>`


* Description: DBOptions::log_file_time_to_roll for RocksDB.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-log-file-time-to_roll=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value: `<code>0</code>`
* Range: `<code>0</code>` to `<code>18446744073709551615</code>`



#### `<code>rocksdb_manifest_preallocation_size</code>`


* Description: DBOptions::manifest_preallocation_size for RocksDB.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-manifest-preallocation-size=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value: `<code>4194304</code>`
* Range: `<code>0</code>` to `<code>18446744073709551615</code>`



#### `<code>rocksdb_manual_compaction_threads</code>`


* Description: How many rocksdb threads to run for manual compactions.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-manual-compation-threads=#</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>0</code>`
* Range: `<code>0</code>` to `<code>128</code>`
* Introduced: [MariaDB 10.3.10](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-10310-release-notes.md), [MariaDB 10.2.18](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-10218-release-notes.md)



#### `<code>rocksdb_manual_wal_flush</code>`


* Description: DBOptions::manual_wal_flush for RocksDB.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-manual-wal-flush={0|1}</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>boolean</code>`
* Default Value: `<code>ON</code>`



#### `<code>rocksdb_master_skip_tx_api</code>`


* Description: Skipping holding any lock on row access. Not effective on slave.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-master-skip-tx-api={0|1}</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`



#### `<code>rocksdb_max_background_compactions</code>`


* Description: DBOptions::max_background_compactions for RocksDB.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-max-background-compactions=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>1</code>`
* Range: `<code>1</code>` to `<code>64</code>`
* Removed: [MariaDB 10.3.1](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1031-release-notes.md), [MariaDB 10.2.8](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1028-release-notes.md)



#### `<code>rocksdb_max_background_flushes</code>`


* Description: DBOptions::max_background_flushes for RocksDB.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-max-background-flushes=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value: `<code>1</code>`
* Range: `<code>1</code>` to `<code>64</code>`
* Removed: [MariaDB 10.3.1](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1031-release-notes.md), [MariaDB 10.2.8](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1028-release-notes.md)



#### `<code>rocksdb_max_background_jobs</code>`


* Description: DBOptions::max_background_jobs for RocksDB.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-max-background-jobs=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>2</code>`
* Range: `<code>-1</code>` to `<code>64</code>`
* Introduced: [MariaDB 10.3.1](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1031-release-notes.md), [MariaDB 10.2.8](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1028-release-notes.md)



#### `<code>rocksdb_max_latest_deadlocks</code>`


* Description: Maximum number of recent deadlocks to store.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-max-latest-deadlocks=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>5</code>`
* Range: `<code>0</code>` to `<code>4294967295</code>`



#### `<code>rocksdb_max_log_file_size</code>`


* Description: DBOptions::max_log_file_size for RocksDB.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-max-log-file-size=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value: `<code>0</code>`
* Range: `<code>0</code>` to `<code>18446744073709551615</code>`



#### `<code>rocksdb_max_manifest_file_size</code>`


* Description: DBOptions::max_manifest_file_size for RocksDB.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-manifest-log-file-size=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value: `<code>1073741824</code>`
* Range: `<code>0</code>` to `<code>18446744073709551615</code>`



#### `<code>rocksdb_max_manual_compactions</code>`


* Description: Maximum number of pending + ongoing number of manual compactions..
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-manual_compactions=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>10</code>`
* Range: `<code>0</code>` to `<code>4294967295</code>`
* Introduced: [MariaDB 10.3.10](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-10310-release-notes.md), [MariaDB 10.2.18](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-10218-release-notes.md)



#### `<code>rocksdb_max_open_files</code>`


* Description: DBOptions::max_open_files for RocksDB.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-max-open-files=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value: `<code>-2</code>`
* Range: `<code>-2</code>` to `<code>2147483647</code>`



#### `<code>rocksdb_max_row_locks</code>`


* Description: Maximum number of locks a transaction can have.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-max-row-locks=#</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>1048576</code>`
* Range:

  * `<code>1</code>` to `<code>1073741824</code>` (>= [MariaDB 10.3.10](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-10310-release-notes.md), [MariaDB 10.2.18](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-10218-release-notes.md))
  * `<code>1</code>` to `<code>1048576</code>` (<= [MariaDB 10.3.9](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1039-release-notes.md), [MariaDB 10.2.17](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-10217-release-notes.md))



#### `<code>rocksdb_max_subcompactions</code>`


* Description: DBOptions::max_subcompactions for RocksDB.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-max-subcompactions=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value: `<code>1</code>`
* Range: `<code>1</code>` to `<code>64</code>`



#### `<code>rocksdb_max_total_wal_size</code>`


* Description: DBOptions::max_total_wal_size for RocksDB. The maximum size limit for write-ahead-log files. Once this limit is reached, RocksDB forces the flushing of memtables.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-max-total-wal-size=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value: `<code>0</code>`
* Range: `<code>0</code>` to `<code>9223372036854775807</code>`



#### `<code>rocksdb_merge_buf_size</code>`


* Description: Size to allocate for merge sort buffers written out to disk during inplace index creation.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-merge-buf-size=#</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>67108864</code>`
* Range: `<code>100</code>` to `<code>18446744073709551615</code>`



#### `<code>rocksdb_merge_combine_read_size</code>`


* Description: Size that we have to work with during combine (reading from disk) phase of external sort during fast index creation.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-merge-combine-read-size=#</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>1073741824</code>`
* Range: `<code>100</code>` to `<code>18446744073709551615</code>`



#### `<code>rocksdb_merge_tmp_file_removal_delay_ms</code>`


* Description: Fast index creation creates a large tmp file on disk during index creation. Removing this large file all at once when index creation is complete can cause trim stalls on Flash. This variable specifies a duration to sleep (in milliseconds) between calling chsize() to truncate the file in chunks. The chunk size is the same as merge_buf_size.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-merge-tmp-file-removal-delay-ms=#</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>0</code>`
* Range: `<code>0</code>` to `<code>18446744073709551615</code>`



#### `<code>rocksdb_new_table_reader_for_compaction_inputs</code>`


* Description: DBOptions::new_table_reader_for_compaction_inputs for RocksDB.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-new-table-reader-for-compaction-inputs={0|1}</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`



#### `<code>rocksdb_no_block_cache</code>`


* Description: BlockBasedTableOptions::no_block_cache for RocksDB.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-no-block-cache={0|1}</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`



#### `<code>rocksdb_override_cf_options</code>`


* Description: Option overrides per cf for RocksDB. Note that the `<code>rocksdb-override-cf-options</code>` syntax is quite strict, and any typos will result in a parse error, and the MyRocks plugin will not be loaded. Depending on your configuration, the server may still start. If it does start, you can use this command to check if the plugin is loaded: `<code>select * from information_schema.plugins where plugin_name='ROCKSDB'</code>` (note that you need the "ROCKSDB" plugin. Other auxiliary plugins like "ROCKSDB_TRX" might still get loaded). Another way is to detect the error is check the error log.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-override-cf-options=value</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>string</code>`
* Default Value: (Empty)



#### `<code>rocksdb_paranoid_checks</code>`


* Description: DBOptions::paranoid_checks for RocksDB.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-paranoid-checks={0|1}</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>boolean</code>`
* Default Value: `<code>ON</code>`



#### `<code>rocksdb_pause_background_work</code>`


* Description: Disable all rocksdb background operations.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-pause-background-work={0|1}</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`



#### `<code>rocksdb_perf_context_level</code>`


* Description: Perf Context Level for rocksdb internal timer stat collection.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-perf-context-level=#</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>0</code>`
* Range: `<code>0</code>` to `<code>5</code>`



#### `<code>rocksdb_persistent_cache_path</code>`


* Description: Path for BlockBasedTableOptions::persistent_cache for RocksDB.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-persistent-cache-path=value</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>string</code>`
* Default Value: (Empty)



#### `<code>rocksdb_persistent_cache_size_mb</code>`


* Description: Size of cache in MB for BlockBasedTableOptions::persistent_cache for RocksDB.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-persistent-cache-size-mb=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value: `<code>0</code>`
* Range: `<code>0</code>` to `<code>18446744073709551615</code>`



#### `<code>rocksdb_pin_l0_filter_and_index_blocks_in_cache</code>`


* Description: pin_l0_filter_and_index_blocks_in_cache for RocksDB.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-pin-l0-filter-and-index-blocks-in-cache={0|1}</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>boolean</code>`
* Default Value: `<code>ON</code>`



#### `<code>rocksdb_print_snapshot_conflict_queries</code>`


* Description: Logging queries that got snapshot conflict errors into *.err log.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-print-snapshot-conflict-queries={0|1}</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`



#### `<code>rocksdb_rate_limiter_bytes_per_sec</code>`


* Description: DBOptions::rate_limiter bytes_per_sec for RocksDB.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-rate-limiter-bytes-per-sec=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>0</code>`
* Range: `<code>0</code>` to `<code>9223372036854775807</code>`



#### `<code>rocksdb_read_free_rpl_tables</code>`


* Description: List of tables that will use read-free replication on the slave (i.e. not lookup a row during replication).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-read-free-rpl-tables=value</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>string</code>`
* Default Value: (Empty)
* Removed: [MariaDB 10.4.7](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-4-series/mariadb-1047-release-notes.md), [MariaDB 10.3.17](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-10317-release-notes.md), [MariaDB 10.2.26](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-10226-release-notes.md)



#### `<code>rocksdb_records_in_range</code>`


* Description: Used to override the result of records_in_range(). Set to a positive number to override.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-records-in-range=#</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>0</code>`
* Range: `<code>0</code>` to `<code>2147483647</code>`



#### `<code>rocksdb_remove_mariabackup_checkpoint</code>`


* Description: Remove [mariabackup](../../../server-management/backing-up-and-restoring-databases/mariabackup/mariabackup-and-backup-stage-commands.md) checkpoint.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-remove-mariabackup-checkpoint={0|1}</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`
* Introduced: [MariaDB 10.3.8](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1038-release-notes.md), [MariaDB 10.2.16](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-10216-release-notes.md)



#### `<code>rocksdb_reset_stats</code>`


* Description: Reset the RocksDB internal statistics without restarting the DB.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-reset-stats={0|1}</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`
* Introduced: [MariaDB 10.3.1](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1031-release-notes.md), [MariaDB 10.2.8](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1028-release-notes.md)



#### `<code>rocksdb_rollback_on_timeout</code>`


* Description: Whether to roll back the complete transaction or a single statement on lock wait timeout (a single statement by default).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-rollback-on-timeout={0|1}</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`
* Introduced: [MariaDB 10.4.7](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-4-series/mariadb-1047-release-notes.md), [MariaDB 10.3.17](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-10317-release-notes.md), [MariaDB 10.2.26](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-10226-release-notes.md)



#### `<code>rocksdb_seconds_between_stat_computes</code>`


* Description: Sets a number of seconds to wait between optimizer stats recomputation. Only changed indexes will be refreshed.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-seconds-between-stat-computes=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>3600</code>`
* Range: `<code>0</code>` to `<code>4294967295</code>`



#### `<code>rocksdb_signal_drop_index_thread</code>`


* Description: Wake up drop index thread.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-signal-drop-index-thread={0|1}</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`



#### `<code>rocksdb_sim_cache_size</code>`


* Description: Simulated cache size for RocksDB.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-sim-cache-size=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value: `<code>0</code>`
* Range: `<code>0</code>` to `<code>9223372036854775807</code>`



#### `<code>rocksdb_skip_bloom_filter_on_read</code>`


* Description: Skip using bloom filter for reads.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-skip-bloom-filter-on_read={0|1}</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`



#### `<code>rocksdb_skip_fill_cache</code>`


* Description: Skip filling block cache on read requests.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-skip-fill-cache={0|1}</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`



#### `<code>rocksdb_skip_unique_check_tables</code>`


* Description: Skip unique constraint checking for the specified tables.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-skip-unique-check-tables=value</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>string</code>`
* Default Value: `<code>.*</code>`



#### `<code>rocksdb_sst_mgr_rate_bytes_per_sec</code>`


* Description: DBOptions::sst_file_manager rate_bytes_per_sec for RocksDB
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-sst-mgr-rate-bytes-per-sec=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>0</code>`
* Range: `<code>0</code>` to `<code>18446744073709551615</code>`



#### `<code>rocksdb_stats_dump_period_sec</code>`


* Description: DBOptions::stats_dump_period_sec for RocksDB.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-stats-dump-period-sec=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value: `<code>600</code>`
* Range: `<code>0</code>` to `<code>2147483647</code>`



#### `<code>rocksdb_stats_level</code>`


* Description: Statistics Level for RocksDB. Default is 0 (kExceptHistogramOrTimers).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-stats-level=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>0</code>`
* Range: `<code>0</code>` to `<code>4</code>`
* Introduced: [MariaDB 10.4.7](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-4-series/mariadb-1047-release-notes.md), [MariaDB 10.3.17](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-10317-release-notes.md), [MariaDB 10.2.26](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-10226-release-notes.md)



#### `<code>rocksdb_stats_recalc_rate</code>`


* Description: The number of indexes per second to recalculate statistics for. 0 to disable background recalculation.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-stats-recalc_rate=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>0</code>`
* Range: `<code>0</code>` to `<code>4294967295</code>`
* Introduced: [MariaDB 10.3.10](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-10310-release-notes.md) [MariaDB 10.2.18](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-10218-release-notes.md)



#### `<code>rocksdb_store_row_debug_checksums</code>`


* Description: Include checksums when writing index/table records.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-store-row-debug-checksums={0|1}</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`



#### `<code>rocksdb_strict_collation_check</code>`


* Description: Enforce case sensitive collation for MyRocks indexes.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-strict-collation-check={0|1}</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>ON</code>`



#### `<code>rocksdb_strict_collation_exceptions</code>`


* Description: List of tables (using regex) that are excluded from the case sensitive collation enforcement.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-strict-collation-exceptions=value</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>string</code>`
* Default Value: (Empty)



#### `<code>rocksdb_supported_compression_types</code>`


* Description: Compression algorithms supported by RocksDB. Note that RocksDB does not make use of [MariaDB 10.7](../../../../release-notes/mariadb-community-server/what-is-mariadb-107.md) [compression-plugins](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/optimization-and-tuning-compression/compression-plugins.md).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-supported-compression-types=value</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>string</code>`
* Default Value: `<code>Snappy,Zlib,ZSTDNotFinal</code>`



#### `<code>rocksdb_table_cache_numshardbits</code>`


* Description: DBOptions::table_cache_numshardbits for RocksDB.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-table-cache-numshardbits=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value: `<code>6</code>`
* Range: `<code>0</code>` to `<code>19</code>`



#### `<code>rocksdb_table_stats_sampling_pct</code>`


* Description: Percentage of entries to sample when collecting statistics about table properties. Specify either 0 to sample everything or percentage [1..100]. By default 10% of entries are sampled.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-table-stats-sampling-pct=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>10</code>`
* Range: `<code>0</code>` to `<code>100</code>`



#### `<code>rocksdb_tmpdir</code>`


* Description: Directory for temporary files during DDL operations.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-tmpdir[=value]</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>string</code>`
* Default Value: (Empty)



#### `<code>rocksdb_trace_sst_api</code>`


* Description: Generate trace output in the log for each call to the SstFileWriter.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-trace-sst-api={0|1}</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`



#### `<code>rocksdb_two_write_queues</code>`


* Description: DBOptions::two_write_queues for RocksDB.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-two-write-queues={0|1}</code>`
* Scope: Global,
* Dynamic: No
* Data Type: `<code>boolean</code>`
* Default Value: `<code>ON</code>`
* Introduced: [MariaDB 10.3.7](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1037-release-notes.md), [MariaDB 10.2.15](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-10215-release-notes.md)



#### `<code>rocksdb_unsafe_for_binlog</code>`


* Description: Allowing statement based binary logging which may break consistency.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-unsafe-for-binlog={0|1}</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`



#### `<code>rocksdb_update_cf_options</code>`


* Description: Option updates per column family for RocksDB.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-update-cf-options=value</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>varchar</code>`
* Default Value: (Empty)
* Introduced: [MariaDB 10.3.1](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1031-release-notes.md), [MariaDB 10.2.8](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1028-release-notes.md)



#### `<code>rocksdb_use_adaptive_mutex</code>`


* Description: DBOptions::use_adaptive_mutex for RocksDB.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-use-adaptive-mutex={0|1}</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`



#### `<code>rocksdb_use_clock_cache</code>`


* Description: Use ClockCache instead of default LRUCache for RocksDB.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-use-clock-cache={0|1}</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`



#### `<code>rocksdb_use_direct_io_for_flush_and_compaction</code>`


* Description: DBOptions::use_direct_io_for_flush_and_compaction for RocksDB.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-use-direct-io-for-flush-and-compaction={0|1}</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`
* Introduced: [MariaDB 10.3.1](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1031-release-notes.md), [MariaDB 10.2.8](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1028-release-notes.md)



#### `<code>rocksdb_use_direct_reads</code>`


* Description: DBOptions::use_direct_reads for RocksDB.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-use-direct-reads={0|1}</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`



#### `<code>rocksdb_use_direct_writes</code>`


* Description: DBOptions::use_direct_writes for RocksDB.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-use-direct-reads={0|1}</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`
* Removed: [MariaDB 10.3.1](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1031-release-notes.md), [MariaDB 10.2.8](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1028-release-notes.md)



#### `<code>rocksdb_use_fsync</code>`


* Description: DBOptions::use_fsync for RocksDB.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-use-fsync={0|1}</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`



#### `<code>rocksdb_validate_tables</code>`


* Description: Verify all .frm files match all RocksDB tables (0 means no verification, 1 means verify and fail on error, and 2 means verify but continue.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-validate-tables=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value: `<code>1</code>`
* Range: `<code>0</code>` to `<code>2</code>`



#### `<code>rocksdb_verify_row_debug_checksums</code>`


* Description: Verify checksums when reading index/table records.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-verify-row-debug-checksums={0|1}</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`



#### `<code>rocksdb_wal_bytes_per_sync</code>`


* Description: DBOptions::wal_bytes_per_sync for RocksDB.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-wal-bytes-per-sync=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>0</code>`
* Range: `<code>0</code>` to `<code>18446744073709551615</code>`



#### `<code>rocksdb_wal_dir</code>`


* Description: DBOptions::wal_dir for RocksDB. Directory where the write-ahead-log files are stored.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-wal-dir=value</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>string</code>`
* Default Value: (Empty)



#### `<code>rocksdb_wal_recovery_mode</code>`


* Description: DBOptions::wal_recovery_mode for RocksDB. Default is kAbsoluteConsistency. Records that are not yet committed are stored in the Write-Ahead-Log (WAL). If the server is not cleanly shut down, the recovery mode will determine the WAL recovery behavior.

  * 1: kAbsoluteConsistency. Will not start if any corrupted entries (including incomplete writes) are detected (the default).
  * 0: kTolerateCorruptedTailRecords. Ignores any errors found at the end of the WAL
  * 2: kPointInTimeRecovery. Replay of the WAL is halted after finding an error. The system will be recovered to the latest consistent point-in-time. Data from a replica can used to replay past the point-in-time.
  * 3: kSkipAnyCorruptedRecords. A risky option where any corrupted entries are skipped while subsequent healthy WAL entries are applied.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-wal-recovery-mode=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>1</code>`
* Range: `<code>0</code>` to `<code>3</code>`



#### `<code>rocksdb_wal_size_limit_mb</code>`


* Description: DBOptions::WAL_size_limit_MB for RocksDB. Write-ahead-log files are moved to an archive directory once their memtables are flushed. This variable specifies the largest size, in MB, that the archive can be.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-wal-size-limit-mb=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value: `<code>0</code>`
* Range: `<code>0</code>` to `<code>9223372036854775807</code>`



#### `<code>rocksdb_wal_ttl_seconds</code>`


* Description: DBOptions::WAL_ttl_seconds for RocksDB. Oldest time, in seconds, that a write-ahead-log file should exist.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-wal-ttl-seconds=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value: `<code>0</code>`
* Range: `<code>0</code>` to `<code>9223372036854775807</code>`



#### `<code>rocksdb_whole_key_filtering</code>`


* Description: BlockBasedTableOptions::whole_key_filtering for RocksDB. If set (the default), the bloomfilter to use the whole key (rather than only the prefix) for filtering is enabled. Lookups should use the whole key for matching to make best use of this setting.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-whole-key-filtering={0|1}</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>boolean</code>`
* Default Value: `<code>ON</code>`



#### `<code>rocksdb_write_batch_max_bytes</code>`


* Description: Maximum size of write batch in bytes. 0 means no limit.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-write-batch-max-bytes=#</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>0</code>`
* Range: `<code>0</code>` to `<code>18446744073709551615</code>`



#### `<code>rocksdb_write_disable_wal</code>`


* Description: WriteOptions::disableWAL for RocksDB.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-write-disable-wal={0|1}</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`



#### `<code>rocksdb_write_ignore_missing_column_families</code>`


* Description: WriteOptions::ignore_missing_column_families for RocksDB.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-write-ignore-missing-column-families={0|1}</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`



#### `<code>rocksdb_write_policy</code>`


* Description: DBOptions::write_policy for RocksDB.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rocksdb-write-policy=val</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>enum</code>`
* Default Value: `<code>write_committed</code>`
* Valid Values: `<code>write_committed</code>`, `<code>write_prepared</code>`, `<code>write_unprepared</code>`
* Introduced: [MariaDB 10.3.10](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-10310-release-notes.md), [MariaDB 10.2.18](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-10218-release-notes.md)


