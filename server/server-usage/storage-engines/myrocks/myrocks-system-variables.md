# System Variables

This page documents system variables related to the [MyRocks](./) storage engine. See [Server System Variables](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md) for a complete list of system variables and instructions on setting them.

See also the [Full list of MariaDB options, system and status variables](../../../reference/full-list-of-mariadb-options-system-and-status-variables.md).

#### `rocksdb_access_hint_on_compaction_start`

* Description: DBOptions::access\_hint\_on\_compaction\_start for RocksDB. Specifies the file access pattern, applied to all input files, once a compaction starts.
* Commandline: `--rocksdb-access-hint-on-compaction-start=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `1`
* Range: `0` to `3`

#### `rocksdb_advise_random_on_open`

* Description: DBOptions::advise\_random\_on\_open for RocksDB.
* Commandline: `--rocksdb-advise-random-on-open={0|1}`
* Scope: Global
* Dynamic: No
* Data Type: `boolean`
* Default Value: `ON`

#### `rocksdb_allow_concurrent_memtable_write`

* Description: DBOptions::allow\_concurrent\_memtable\_write for RocksDB.
* Commandline: `--rocksdb-allow-concurrent-memtable-write={0|1}`
* Scope: Global
* Dynamic: No
* Data Type: `boolean`
* Default Value: `OFF`

#### `rocksdb_allow_mmap_reads`

* Description: DBOptions::allow\_mmap\_reads for RocksDB
* Commandline: `--rocksdb-allow-mmap-reads={0|1}`
* Scope: Global
* Dynamic: No
* Data Type: `boolean`
* Default Value: `OFF`

#### `rocksdb_allow_mmap_writes`

* Description: DBOptions::allow\_mmap\_writes for RocksDB
* Commandline: `--rocksdb-allow-mmap-writes={0|1}`
* Scope: Global
* Dynamic: No
* Data Type: `boolean`
* Default Value: `OFF`

#### `rocksdb_allow_to_start_after_corruption`

* Description: Allow server still to start successfully even if RocksDB corruption is detected.
* Commandline: `--rocksdb-allow-to-start-after-corruption={0|1}`
* Scope: Global
* Dynamic: No
* Data Type: `boolean`
* Default Value: `OFF`
* Introduced: [MariaDB 10.3.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-1037-release-notes), [MariaDB 10.2.15](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-10215-release-notes)

#### `rocksdb_background_sync`

* Description: Turns on background syncs for RocksDB
* Commandline: `--rocksdb-background-sync={0|1}`
* Scope: Global
* Dynamic: No
* Data Type: `boolean`
* Default Value: `OFF`
* Removed: [MariaDB 10.3.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-1031-release-notes), [MariaDB 10.2.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1028-release-notes)

#### `rocksdb_base_background_compactions`

* Description: DBOptions::base\_background\_compactions for RocksDB
* Commandline: `--rocksdb-base-background-compactions=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `1`
* Range: `-1` to `64`
* Removed: [MariaDB 10.3.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-1031-release-notes), [MariaDB 10.2.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1028-release-notes)

#### `rocksdb_blind_delete_primary_key`

* Description: Deleting rows by primary key lookup, without reading rows (Blind Deletes). Blind delete is disabled if the table has secondary key.
* Commandline: `--rocksdb-blind-delete-primary-key={0|1}`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`

#### `rocksdb_block_cache_size`

* Description: Block\_cache size for RocksDB (block size 1024)
* Commandline: `--rocksdb-block-cache-size=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `536870912`
* Range: `1024` to `9223372036854775807`

To see the statistics of block cache usage, check `SHOW ENGINE ROCKSDB STATUS` output\
(search for lines starting with `rocksdb.block.cache`).

One can check the size of data of the block cache in `DB_BLOCK_CACHE_USAGE`\
column of the `INFORMATION_SCHEMA.ROCKSDB_DBSTATS` table.

#### `rocksdb_block_restart_interval`

* Description: BlockBasedTableOptions::block\_restart\_interval for RocksDB
* Commandline: `--rocksdb-block-restart-interval=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `16`
* Range: `1` to `2147483647`

#### `rocksdb_block_size`

* Description: BlockBasedTableOptions::block\_size for RocksDB
* Commandline: `--rocksdb-block-size=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `4096`
* Range: `1` to `18446744073709551615`

#### `rocksdb_block_size_deviation`

* Description: BlockBasedTableOptions::block\_size\_deviation for RocksDB
* Commandline: `--rocksdb-block-size-deviation=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `10`
* Range: `0` to `2147483647`

#### `rocksdb_bulk_load`

* Description: Use bulk-load mode for inserts. This disables unique\_checks and enables rocksdb\_commit\_in\_the\_middle.
* Commandline: `--rocksdb-bulk-load={0|1}`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`

#### `rocksdb_bulk_load_allow_sk`

* Description: Allow bulk loading of sk keys during bulk-load. Can be changed only when bulk load is disabled.
* Commandline: `--rocksdb-bulk-load_allow_sk={0|1}`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`
* Introduced: [MariaDB 10.3.10](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-10310-release-notes), [MariaDB 10.2.18](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-10218-release-notes)

#### `rocksdb_bulk_load_allow_unsorted`

* Description: Allow unsorted input during bulk-load. Can be changed only when bulk load is disabled.
* Commandline: `--rocksdb-bulk-load_allow_unsorted={0|1}`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`

#### `rocksdb_bulk_load_size`

* Description: Maximum number of records in a batch for bulk-load mode.
* Commandline: `--rocksdb-bulk-load-size=#`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `1000`
* Range: `1` to `1073741824`

#### `rocksdb_bytes_per_sync`

* Description: DBOptions::bytes\_per\_sync for RocksDB.
* Commandline: `--rocksdb-bytes-per-sync=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `0`
* Range: `0` to `18446744073709551615`

#### `rocksdb_cache_dump`

* Description: Include RocksDB block cache content in core dump.
* Commandline: `--rocksdb-cache-dump={0|1}`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `ON`
* Introduced: [MariaDB 10.4.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/mariadb-1047-release-notes), [MariaDB 10.3.17](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-10317-release-notes), [MariaDB 10.2.26](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-10226-release-notes)

#### `rocksdb_cache_high_pri_pool_ratio`

* Description: Specify the size of block cache high-pri pool.
* Commandline: `--rocksdb-cache-high-pri-pool-ratio=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `double`
* Default Value: `0.000000`
* Range: `0` to `1`
* Introduced: [MariaDB 10.4.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/mariadb-1047-release-notes), [MariaDB 10.3.17](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-10317-release-notes), [MariaDB 10.2.26](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-10226-release-notes)

#### `rocksdb_cache_index_and_filter_blocks`

* Description: BlockBasedTableOptions::cache\_index\_and\_filter\_blocks for RocksDB.
* Commandline: `--rocksdb-cache-index-and-filter-blocks={0|1}`
* Scope: Global
* Dynamic: No
* Data Type: `boolean`
* Default Value: `ON`

#### `rocksdb_cache_index_and_filter_with_high_priority`

* Description: cache\_index\_and\_filter\_blocks\_with\_high\_priority for RocksDB.
* Commandline: `--rocksdb-cache-index-and-filter-with-high-priority={0|1}`
* Scope: Global
* Dynamic: No
* Data Type: `boolean`
* Default Value: `ON`
* Introduced: [MariaDB 10.4.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/mariadb-1047-release-notes), [MariaDB 10.3.17](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-10317-release-notes), [MariaDB 10.2.26](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-10226-release-notes)

#### `rocksdb_checksums_pct`

* Description: Percentage of rows to be checksummed.
* Commandline: `--rocksdb-checksums-pct=#`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `100`
* Range: `0` to `100`

#### `rocksdb_collect_sst_properties`

* Description: Enables collecting SST file properties on each flush.
* Commandline: `--rocksdb-collect-sst-properties={0|1}`
* Scope: Global
* Dynamic: No
* Data Type: `boolean`
* Default Value: `ON`

#### `rocksdb_commit_in_the_middle`

* Description: Commit rows implicitly every rocksdb\_bulk\_load\_size, on bulk load/insert, update and delete.
* Commandline: `--rocksdb-commit-in-the-middle={0|1}`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`

#### `rocksdb_commit_time_batch_for_recovery`

* Description: TransactionOptions::commit\_time\_batch\_for\_recovery for RocksDB.
* Commandline: `--rocksdb-commit-time-batch-for-recovery={0|1}`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`
* Introduced: [MariaDB 10.3.10](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-10310-release-notes), [MariaDB 10.2.18](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-10218-release-notes)

#### `rocksdb_compact_cf`

* Description: Compact column family.
* Commandline: `--rocksdb-compact-cf=value`
* Scope: Global
* Dynamic: Yes
* Data Type: `string`
* Default Value: (Empty)

#### `rocksdb_compaction_readahead_size`

* Description: DBOptions::compaction\_readahead\_size for RocksDB.
* Commandline: `--rocksdb-compaction-readahead-size=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `0`
* Range: `0` to `18446744073709551615`

#### `rocksdb_compaction_sequential_deletes`

* Description: RocksDB will trigger compaction for the file if it has more than this number sequential deletes per window.
* Commandline: `--rocksdb-compaction-sequential-deletes=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `0`
* Range: `0` to `2000000`

#### `rocksdb_compaction_sequential_deletes_count_sd`

* Description: Counting SingleDelete as rocksdb\_compaction\_sequential\_deletes.
* Commandline: `--rocksdb-compaction-sequential-deletes-count-sd={0|1}`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`

#### `rocksdb_compaction_sequential_deletes_file_size`

* Description: Minimum file size required for compaction\_sequential\_deletes.
* Commandline: `--rocksdb-compaction-sequential-deletes-file-size=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `0`
* Range: `-1` to `9223372036854775807`

#### `rocksdb_compaction_sequential_deletes_window`

* Description: Size of the window for counting rocksdb\_compaction\_sequential\_deletes.
* Commandline: `--rocksdb-compaction-sequential-deletes-window=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `0`
* Range: `0` to `2000000`

#### `rocksdb_concurrent_prepare`

* Description: DBOptions::concurrent\_prepare for RocksDB.
* Commandline: `--rocksdb-coconcurrent-prepare={0|1}`
* Scope: Global
* Dynamic: No
* Data Type: `boolean`
* Default Value: `1`
* Removed: [MariaDB 10.3.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-1037-release-notes), [MariaDB 10.2.15](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-10215-release-notes)

#### `rocksdb_create_checkpoint`

* Description: Checkpoint directory.
* Commandline: `--rocksdb-create-checkpoint=value`
* Scope: Global
* Dynamic: Yes
* Data Type: `string`
* Default Value: (Empty)

#### `rocksdb_create_if_missing`

* Description: DBOptions::create\_if\_missing for RocksDB.
* Commandline: `--rocksdb-create-if-missing={0|1}`
* Scope: Global
* Dynamic: No
* Data Type: `boolean`
* Default Value: `ON`

#### `rocksdb_create_missing_column_families`

* Description: DBOptions::create\_missing\_column\_families for RocksDB.
* Commandline: `--rocksdb-create-missing-column-families={0|1}`
* Scope: Global
* Dynamic: No
* Data Type: `boolean`
* Default Value: `OFF`

#### `rocksdb_datadir`

* Description: RocksDB data directory.
* Commandline: `--rocksdb-datadir[=value]`
* Scope: Global
* Dynamic: No
* Data Type: `string`
* Default Value: `./#rocksdb`

#### `rocksdb_db_write_buffer_size`

* Description: DBOptions::db\_write\_buffer\_size for RocksDB.
* Commandline: `--rocksdb-db-write-buffer-size=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `0`
* Range: `0` to `18446744073709551615`

#### `rocksdb_deadlock_detect`

* Description: Enables deadlock detection.
* Commandline: `--rocksdb-deadlock-detect={0|1}`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`

#### `rocksdb_deadlock_detect_depth`

* Description: Number of transactions deadlock detection will traverse through before assuming deadlock.
* Commandline: `--rocksdb-deadlock-detect-depth=#`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `50`
* Range: `2` to `18446744073709551615`

#### `rocksdb_debug_manual_compaction_delay`

* Description: For debugging purposes only. Sleeping specified seconds for simulating long running compactions.
* Commandline: `--rocksdb-debug_manual_compaction_delay=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `0`
* Range: `0` to `4294967295`
* Introduced: [MariaDB 10.3.10](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-10310-release-notes), [MariaDB 10.2.18](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-10218-release-notes)

#### `rocksdb_debug_optimizer_no_zero_cardinality`

* Description: If cardinality is zero, override it with some value.
* Commandline: `--rocksdb-debug-optimizer-no-zero-cardinality={0|1}`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `ON`

#### `rocksdb_debug_ttl_ignore_pk`

* Description: For debugging purposes only. If true, compaction filtering will not occur on PK TTL data. This variable is a no-op in non-debug builds.
* Commandline: `--rocksdb-debug-ttl-ignore-pk={0|1}`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`

#### `rocksdb_debug_ttl_read_filter_ts`

* Description: For debugging purposes only. Overrides the TTL read filtering time to time + debug\_ttl\_read\_filter\_ts. A value of 0 denotes that the variable is not set. This variable is a no-op in non-debug builds.
* Commandline: `--rocksdb-debug-ttl-read-filter-ts=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `0`
* Range: `-3600` to `3600`
* Introduced: [MariaDB 10.3.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-1031-release-notes), [MariaDB 10.2.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1028-release-notes)

#### `rocksdb_debug_ttl_rec_ts`

* Description: For debugging purposes only. Overrides the TTL of records to now() + debug\_ttl\_rec\_ts. The value can be +/- to simulate a record inserted in the past vs a record inserted in the 'future'. A value of 0 denotes that the variable is not set. This variable is a no-op in non-debug builds.
* Commandline: `--rocksdb-debug-ttl-read-filter-ts=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `0`
* Range: `-3600` to `3600`
* Introduced: [MariaDB 10.3.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-1031-release-notes), [MariaDB 10.2.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1028-release-notes)

#### `rocksdb_debug_ttl_snapshot_ts`

* Description: For debugging purposes only. Sets the snapshot during compaction to now() + debug\_set\_ttl\_snapshot\_ts. The value can be positive or negative to simulate a snapshot in the past vs a snapshot created in the 'future'. A value of 0 denotes that the variable is not set. This variable is a no-op in non-debug builds.
* Commandline: `--rocksdb-debug-ttl-snapshot-ts=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `0`
* Range: `-3600` to `3600`
* Introduced: [MariaDB 10.3.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-1031-release-notes), [MariaDB 10.2.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1028-release-notes)

#### `rocksdb_default_cf_options`

* Description: Default cf options for RocksDB.
* Commandline: `--rocksdb-default-cf-options=value`
* Scope: Global
* Dynamic: No
* Data Type: `string`
* Default Value: (Empty)

#### `rocksdb_delayed_write_rate`

* Description: DBOptions::delayed\_write\_rate.
* Commandline: `--rocksdb-delayed-write-rate=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `0` (Previously `16777216`)
* Range: `0` to `18446744073709551615`

#### `rocksdb_delete_cf`

* Description: Delete column family.
* Commandline: `--rocksdb-delete-cf=val`
* Scope: Global
* Dynamic: No
* Data Type: `string`
* Default Value: (Empty string)
* Introduced: [MariaDB 10.4.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/mariadb-1047-release-notes), [MariaDB 10.3.17](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-10317-release-notes), [MariaDB 10.2.26](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-10226-release-notes)

#### `rocksdb_delete_obsolete_files_period_micros`

* Description: DBOptions::delete\_obsolete\_files\_period\_micros for RocksDB.
* Commandline: `--rocksdb-delete-obsolete-files-period-micros=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `21600000000`
* Range: `0` to `9223372036854775807`

#### `rocksdb_enable_2pc`

* Description: Enable two phase commit for MyRocks. When set, MyRocks will keep its data consistent with the [binary log](../../../server-management/server-monitoring-logs/binary-log/) (in other words, the server will be a crash-safe master). The consistency is achieved by doing two-phase XA commit with the binary log.
* Commandline: `--rocksdb-enable-2pc={0|1}`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `ON`

#### `rocksdb_enable_bulk_load_api`

* Description: Enables using SstFileWriter for bulk loading.
* Commandline: `--rocksdb-enable-bulk-load-api={0|1}`
* Scope: Global
* Dynamic: No
* Data Type: `boolean`
* Default Value: `ON`

#### `rocksdb_enable_insert_with_update_caching`

* Description: Whether to enable optimization where we cache the read from a failed insertion attempt in [INSERT ON DUPLICATE KEY UPDATE](../../../reference/sql-statements/data-manipulation/inserting-loading-data/insert-on-duplicate-key-update.md).
* Commandline: `--rocksdb-enable-insert-with-update-caching={0|1}`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `ON`
* Introduced: [MariaDB 10.4.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/mariadb-1047-release-notes), [MariaDB 10.3.17](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-10317-release-notes), [MariaDB 10.2.26](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-10226-release-notes)

#### `rocksdb_enable_thread_tracking`

* Description: DBOptions::enable\_thread\_tracking for RocksDB.
* Commandline: `--rocksdb-enable-thread-tracking={0|1}`
* Scope: Global
* Dynamic: No
* Data Type: `boolean`
* Default Value: `OFF`

#### `rocksdb_enable_ttl`

* Description: Enable expired TTL records to be dropped during compaction.
* Commandline: `--rocksdb-enable-ttl={0|1}`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `ON`
* Introduced: [MariaDB 10.3.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-1031-release-notes), [MariaDB 10.2.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1028-release-notes)

#### `rocksdb_enable_ttl_read_filtering`

* Description: For tables with TTL, expired records are skipped/filtered out during processing and in query results. Disabling this will allow these records to be seen, but as a result rows may disappear in the middle of transactions as they are dropped during compaction. Use with caution.
* Commandline: `--rocksdb-enable-ttl-read-filtering={0|1}`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `ON`
* Introduced: [MariaDB 10.3.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-1031-release-notes), [MariaDB 10.2.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1028-release-notes)

#### `rocksdb_enable_write_thread_adaptive_yield`

* Description: DBOptions::enable\_write\_thread\_adaptive\_yield for RocksDB.
* Commandline: `--rocksdb-enable-write-thread-adaptive-yield={0|1}`
* Scope: Global
* Dynamic: No
* Data Type: `boolean`
* Default Value: `OFF`

#### `rocksdb_error_if_exists`

* Description: DBOptions::error\_if\_exists for RocksDBB.
* Commandline: `--rocksdb-error-if-exists={0|1}`
* Scope: Global
* Dynamic: No
* Data Type: `boolean`
* Default Value: `OFF`

#### `rocksdb_error_on_suboptimal_collation`

* Description: Raise an error instead of warning if a sub-optimal collation is used.
* Commandline: `--rocksdb-error-on-suboptimal-collation={0|1}`
* Scope: Global
* Dynamic: No
* Data Type: `boolean`
* Default Value: `ON`
* Introduced: [MariaDB 10.3.10](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-10310-release-notes), [MariaDB 10.2.18](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-10218-release-notes)

#### `rocksdb_flush_log_at_trx_commit`

* Description: Sync on transaction commit. Similar to [innodb\_flush\_log\_at\_trx\_commit](../innodb/innodb-system-variables.md#innodb_flush_log_at_trx_commit). One can check the flushing by examining the [rocksdb\_wal\_synced](myrocks-status-variables.md#rocksdb_wal_synced) and [rocksdb\_wal\_bytes](myrocks-status-variables.md#rocksdb_wal_bytes) status variables.
  * 1: Always sync on commit (the default).
  * 0: Never sync.
  * 2: Sync based on a timer controlled via rocksdb-background-sync.
* Commandline: `--rocksdb-flush-log-at-trx-commit=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `1`
* Range: `0` to `2`

#### `rocksdb_flush_memtable_on_analyze`

* Description: Forces memtable flush on ANALZYE table to get accurate cardinality.
* Commandline: `--rocksdb-flush-memtable-on-analyze={0|1}`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `ON`
* Removed: [MariaDB 10.3.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-1037-release-notes), [MariaDB 10.2.15](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-10215-release-notes)

#### `rocksdb_force_compute_memtable_stats`

* Description: Force to always compute memtable stats.
* Commandline: `--rocksdb-force-compute-memtable-stats={0|1}`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `ON`

#### `rocksdb_force_compute_memtable_stats_cachetime`

* Description: Time in usecs to cache memtable estimates.
* Commandline: `--rocksdb-force-compute-memtable-stats-cachetime=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `60000000`
* Range: `0` to `2147483647`

#### `rocksdb_force_flush_memtable_and_lzero_now`

* Description: Acts similar to force\_flush\_memtable\_now, but also compacts all L0 files.
* Commandline: `--rocksdb-force-flush-memtable-and-lzero-now={0|1}`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`
* Introduced: [MariaDB 10.3.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-1031-release-notes), [MariaDB 10.2.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1028-release-notes)

#### `rocksdb_force_flush_memtable_now`

* Description: Forces memstore flush which may block all write requests so be careful.
* Commandline: `--rocksdb-force-flush-memtable-now={0|1}`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`

#### `rocksdb_force_index_records_in_range`

* Description: Used to override the result of records\_in\_range() when [FORCE INDEX](../../../ha-and-performance/optimization-and-tuning/query-optimizations/force-index.md) is used.
* Commandline: `--rocksdb-force-index-records-in-range=#`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `0`
* Range: `0` to `2147483647`

#### `rocksdb_git_hash`

* Description: Git revision of the RocksDB library used by MyRocks.
* Commandline: `--rocksdb-git-hash=value=#`
* Scope: Global
* Dynamic: No
* Data Type: `string`
* Default Value: As per git revision.

#### `rocksdb_hash_index_allow_collision`

* Description: BlockBasedTableOptions::hash\_index\_allow\_collision for RocksDB.
* Commandline: `--rocksdb-hash-index-allow-collision={0|1}`
* Scope: Global
* Dynamic: No
* Data Type: `boolean`
* Default Value: `ON`

#### `rocksdb_ignore_unknown_options`

* Description: Enable ignoring unknown options passed to RocksDB.
* Commandline: `--rocksdb-ignore-unknown-options={0|1}`
* Scope: Global
* Dynamic: No
* Data Type: `boolean`
* Default Value: `ON`
* Introduced: [MariaDB 10.3.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-1037-release-notes), [MariaDB 10.2.15](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-10215-release-notes)

#### `rocksdb_index_type`

* Description: BlockBasedTableOptions::index\_type for RocksDB.
* Commandline: `--rocksdb-index-type=value`
* Scope: Global
* Dynamic: No
* Data Type: `enum`
* Default Value: `kBinarySearch`
* Valid Values: `kBinarySearch`, `kHashSearch`

#### `rocksdb_info_log_level`

* Description: Filter level for info logs to be written mysqld error log. Valid values include 'debug\_level', 'info\_level', 'warn\_level', 'error\_level' and 'fatal\_level'.
* Commandline: `--rocksdb-info-log-level=value`
* Scope: Global
* Dynamic: Yes
* Data Type: `enum`
* Default Value: `error_level`
* Valid Values: `error_level`, `debug_level`, `info_level`, `warn_level`, `fatal_level`

#### `rocksdb_io_write_timeout`

* Description: Timeout for experimental I/O watchdog.
* Commandline: `--rocksdb-io-write-timeout=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `0`
* Valid Values: `0` to `4294967295`
* Introduced: [MariaDB 10.3.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-1031-release-notes), [MariaDB 10.2.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1028-release-notes)

#### `rocksdb_is_fd_close_on_exec`

* Description: DBOptions::is\_fd\_close\_on\_exec for RocksDB.
* Commandline: `--rocksdb-is-fd-close-on-exec={0|1}`
* Scope: Global
* Dynamic: No
* Data Type: `boolean`
* Default Value: `ON`

#### `rocksdb_keep_log_file_num`

* Description: DBOptions::keep\_log\_file\_num for RocksDB.
* Commandline: `--rocksdb-keep-log-file-num=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `1000`
* Range: `0` to `18446744073709551615`

#### `rocksdb_large_prefix`

* Description: Support large index prefix length of 3072 bytes. If off, the maximum index prefix length is 767.
* Commandline: `--rocksdb-large_prefix={0|1}`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`

#### `rocksdb_lock_scanned_rows`

* Description: Take and hold locks on rows that are scanned but not updated.
* Commandline: `--rocksdb-lock-scanned-rows={0|1}`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`

#### `rocksdb_lock_wait_timeout`

* Description: Number of seconds to wait for lock.
* Commandline: `--rocksdb-lock-wait-timeout=#`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `1`
* Range: `1` to `1073741824`

#### `rocksdb_log_dir`

* Description: DBOptions::log\_dir for RocksDB. Where the log files are stored. An empty value implies `rocksdb_datadir` is used as the directory.
* Commandline: `--rocksdb-log-dir=#`
* Scope: Global
* Dynamic: No
* Data Type: `string`
* Default Value: (Empty)
* Introduced: [MariaDB 10.9.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-9-series/mariadb-1091-release-notes)

#### `rocksdb_log_file_time_to_roll`

* Description: DBOptions::log\_file\_time\_to\_roll for RocksDB.
* Commandline: `--rocksdb-log-file-time-to_roll=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `0`
* Range: `0` to `18446744073709551615`

#### `rocksdb_manifest_preallocation_size`

* Description: DBOptions::manifest\_preallocation\_size for RocksDB.
* Commandline: `--rocksdb-manifest-preallocation-size=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `4194304`
* Range: `0` to `18446744073709551615`

#### `rocksdb_manual_compaction_threads`

* Description: How many rocksdb threads to run for manual compactions.
* Commandline: `--rocksdb-manual-compation-threads=#`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `0`
* Range: `0` to `128`
* Introduced: [MariaDB 10.3.10](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-10310-release-notes), [MariaDB 10.2.18](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-10218-release-notes)

#### `rocksdb_manual_wal_flush`

* Description: DBOptions::manual\_wal\_flush for RocksDB.
* Commandline: `--rocksdb-manual-wal-flush={0|1}`
* Scope: Global
* Dynamic: No
* Data Type: `boolean`
* Default Value: `ON`

#### `rocksdb_master_skip_tx_api`

* Description: Skipping holding any lock on row access. Not effective on slave.
* Commandline: `--rocksdb-master-skip-tx-api={0|1}`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`

#### `rocksdb_max_background_compactions`

* Description: DBOptions::max\_background\_compactions for RocksDB.
* Commandline: `--rocksdb-max-background-compactions=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `1`
* Range: `1` to `64`
* Removed: [MariaDB 10.3.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-1031-release-notes), [MariaDB 10.2.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1028-release-notes)

#### `rocksdb_max_background_flushes`

* Description: DBOptions::max\_background\_flushes for RocksDB.
* Commandline: `--rocksdb-max-background-flushes=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `1`
* Range: `1` to `64`
* Removed: [MariaDB 10.3.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-1031-release-notes), [MariaDB 10.2.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1028-release-notes)

#### `rocksdb_max_background_jobs`

* Description: DBOptions::max\_background\_jobs for RocksDB.
* Commandline: `--rocksdb-max-background-jobs=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `2`
* Range: `-1` to `64`
* Introduced: [MariaDB 10.3.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-1031-release-notes), [MariaDB 10.2.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1028-release-notes)

#### `rocksdb_max_latest_deadlocks`

* Description: Maximum number of recent deadlocks to store.
* Commandline: `--rocksdb-max-latest-deadlocks=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `5`
* Range: `0` to `4294967295`

#### `rocksdb_max_log_file_size`

* Description: DBOptions::max\_log\_file\_size for RocksDB.
* Commandline: `--rocksdb-max-log-file-size=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `0`
* Range: `0` to `18446744073709551615`

#### `rocksdb_max_manifest_file_size`

* Description: DBOptions::max\_manifest\_file\_size for RocksDB.
* Commandline: `--rocksdb-manifest-log-file-size=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `1073741824`
* Range: `0` to `18446744073709551615`

#### `rocksdb_max_manual_compactions`

* Description: Maximum number of pending + ongoing number of manual compactions..
* Commandline: `--rocksdb-manual_compactions=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `10`
* Range: `0` to `4294967295`
* Introduced: [MariaDB 10.3.10](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-10310-release-notes), [MariaDB 10.2.18](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-10218-release-notes)

#### `rocksdb_max_open_files`

* Description: DBOptions::max\_open\_files for RocksDB.
* Commandline: `--rocksdb-max-open-files=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `-2`
* Range: `-2` to `2147483647`

#### `rocksdb_max_row_locks`

* Description: Maximum number of locks a transaction can have.
* Commandline: `--rocksdb-max-row-locks=#`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `1048576`
* Range:
  * `1` to `1073741824` (>= [MariaDB 10.3.10](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-10310-release-notes), [MariaDB 10.2.18](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-10218-release-notes))
  * `1` to `1048576` (<= [MariaDB 10.3.9](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-1039-release-notes), [MariaDB 10.2.17](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-10217-release-notes))

#### `rocksdb_max_subcompactions`

* Description: DBOptions::max\_subcompactions for RocksDB.
* Commandline: `--rocksdb-max-subcompactions=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `1`
* Range: `1` to `64`

#### `rocksdb_max_total_wal_size`

* Description: DBOptions::max\_total\_wal\_size for RocksDB. The maximum size limit for write-ahead-log files. Once this limit is reached, RocksDB forces the flushing of memtables.
* Commandline: `--rocksdb-max-total-wal-size=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `0`
* Range: `0` to `9223372036854775807`

#### `rocksdb_merge_buf_size`

* Description: Size to allocate for merge sort buffers written out to disk during inplace index creation.
* Commandline: `--rocksdb-merge-buf-size=#`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `67108864`
* Range: `100` to `18446744073709551615`

#### `rocksdb_merge_combine_read_size`

* Description: Size that we have to work with during combine (reading from disk) phase of external sort during fast index creation.
* Commandline: `--rocksdb-merge-combine-read-size=#`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `1073741824`
* Range: `100` to `18446744073709551615`

#### `rocksdb_merge_tmp_file_removal_delay_ms`

* Description: Fast index creation creates a large tmp file on disk during index creation. Removing this large file all at once when index creation is complete can cause trim stalls on Flash. This variable specifies a duration to sleep (in milliseconds) between calling chsize() to truncate the file in chunks. The chunk size is the same as merge\_buf\_size.
* Commandline: `--rocksdb-merge-tmp-file-removal-delay-ms=#`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `0`
* Range: `0` to `18446744073709551615`

#### `rocksdb_new_table_reader_for_compaction_inputs`

* Description: DBOptions::new\_table\_reader\_for\_compaction\_inputs for RocksDB.
* Commandline: `--rocksdb-new-table-reader-for-compaction-inputs={0|1}`
* Scope: Global
* Dynamic: No
* Data Type: `boolean`
* Default Value: `OFF`

#### `rocksdb_no_block_cache`

* Description: BlockBasedTableOptions::no\_block\_cache for RocksDB.
* Commandline: `--rocksdb-no-block-cache={0|1}`
* Scope: Global
* Dynamic: No
* Data Type: `boolean`
* Default Value: `OFF`

#### `rocksdb_override_cf_options`

* Description: Option overrides per cf for RocksDB. Note that the `rocksdb-override-cf-options` syntax is quite strict, and any typos will result in a parse error, and the MyRocks plugin will not be loaded. Depending on your configuration, the server may still start. If it does start, you can use this command to check if the plugin is loaded: `select * from information_schema.plugins where plugin_name='ROCKSDB'` (note that you need the "ROCKSDB" plugin. Other auxiliary plugins like "ROCKSDB\_TRX" might still get loaded). Another way is to detect the error is check the error log.
* Commandline: `--rocksdb-override-cf-options=value`
* Scope: Global
* Dynamic: No
* Data Type: `string`
* Default Value: (Empty)

#### `rocksdb_paranoid_checks`

* Description: DBOptions::paranoid\_checks for RocksDB.
* Commandline: `--rocksdb-paranoid-checks={0|1}`
* Scope: Global
* Dynamic: No
* Data Type: `boolean`
* Default Value: `ON`

#### `rocksdb_pause_background_work`

* Description: Disable all rocksdb background operations.
* Commandline: `--rocksdb-pause-background-work={0|1}`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`

#### `rocksdb_perf_context_level`

* Description: Perf Context Level for rocksdb internal timer stat collection.
* Commandline: `--rocksdb-perf-context-level=#`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `0`
* Range: `0` to `5`

#### `rocksdb_persistent_cache_path`

* Description: Path for BlockBasedTableOptions::persistent\_cache for RocksDB.
* Commandline: `--rocksdb-persistent-cache-path=value`
* Scope: Global
* Dynamic: No
* Data Type: `string`
* Default Value: (Empty)

#### `rocksdb_persistent_cache_size_mb`

* Description: Size of cache in MB for BlockBasedTableOptions::persistent\_cache for RocksDB.
* Commandline: `--rocksdb-persistent-cache-size-mb=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `0`
* Range: `0` to `18446744073709551615`

#### `rocksdb_pin_l0_filter_and_index_blocks_in_cache`

* Description: pin\_l0\_filter\_and\_index\_blocks\_in\_cache for RocksDB.
* Commandline: `--rocksdb-pin-l0-filter-and-index-blocks-in-cache={0|1}`
* Scope: Global
* Dynamic: No
* Data Type: `boolean`
* Default Value: `ON`

#### `rocksdb_print_snapshot_conflict_queries`

* Description: Logging queries that got snapshot conflict errors into \*.err log.
* Commandline: `--rocksdb-print-snapshot-conflict-queries={0|1}`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`

#### `rocksdb_rate_limiter_bytes_per_sec`

* Description: DBOptions::rate\_limiter bytes\_per\_sec for RocksDB.
* Commandline: `--rocksdb-rate-limiter-bytes-per-sec=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `0`
* Range: `0` to `9223372036854775807`

#### `rocksdb_read_free_rpl_tables`

* Description: List of tables that will use read-free replication on the slave (i.e. not lookup a row during replication).
* Commandline: `--rocksdb-read-free-rpl-tables=value`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `string`
* Default Value: (Empty)
* Removed: [MariaDB 10.4.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/mariadb-1047-release-notes), [MariaDB 10.3.17](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-10317-release-notes), [MariaDB 10.2.26](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-10226-release-notes)

#### `rocksdb_records_in_range`

* Description: Used to override the result of records\_in\_range(). Set to a positive number to override.
* Commandline: `--rocksdb-records-in-range=#`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `0`
* Range: `0` to `2147483647`

#### `rocksdb_remove_mariabackup_checkpoint`

* Description: Remove [mariabackup](../../backing-up-and-restoring-databases/mariabackup/) checkpoint.
* Commandline: `--rocksdb-remove-mariabackup-checkpoint={0|1}`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`
* Introduced: [MariaDB 10.3.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-1038-release-notes), [MariaDB 10.2.16](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-10216-release-notes)

#### `rocksdb_reset_stats`

* Description: Reset the RocksDB internal statistics without restarting the DB.
* Commandline: `--rocksdb-reset-stats={0|1}`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`
* Introduced: [MariaDB 10.3.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-1031-release-notes), [MariaDB 10.2.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1028-release-notes)

#### `rocksdb_rollback_on_timeout`

* Description: Whether to roll back the complete transaction or a single statement on lock wait timeout (a single statement by default).
* Commandline: `--rocksdb-rollback-on-timeout={0|1}`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`
* Introduced: [MariaDB 10.4.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/mariadb-1047-release-notes), [MariaDB 10.3.17](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-10317-release-notes), [MariaDB 10.2.26](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-10226-release-notes)

#### `rocksdb_seconds_between_stat_computes`

* Description: Sets a number of seconds to wait between optimizer stats recomputation. Only changed indexes will be refreshed.
* Commandline: `--rocksdb-seconds-between-stat-computes=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `3600`
* Range: `0` to `4294967295`

#### `rocksdb_signal_drop_index_thread`

* Description: Wake up drop index thread.
* Commandline: `--rocksdb-signal-drop-index-thread={0|1}`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`

#### `rocksdb_sim_cache_size`

* Description: Simulated cache size for RocksDB.
* Commandline: `--rocksdb-sim-cache-size=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `0`
* Range: `0` to `9223372036854775807`

#### `rocksdb_skip_bloom_filter_on_read`

* Description: Skip using bloom filter for reads.
* Commandline: `--rocksdb-skip-bloom-filter-on_read={0|1}`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`

#### `rocksdb_skip_fill_cache`

* Description: Skip filling block cache on read requests.
* Commandline: `--rocksdb-skip-fill-cache={0|1}`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`

#### `rocksdb_skip_unique_check_tables`

* Description: Skip unique constraint checking for the specified tables.
* Commandline: `--rocksdb-skip-unique-check-tables=value`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `string`
* Default Value: `.*`

#### `rocksdb_sst_mgr_rate_bytes_per_sec`

* Description: DBOptions::sst\_file\_manager rate\_bytes\_per\_sec for RocksDB
* Commandline: `--rocksdb-sst-mgr-rate-bytes-per-sec=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `0`
* Range: `0` to `18446744073709551615`

#### `rocksdb_stats_dump_period_sec`

* Description: DBOptions::stats\_dump\_period\_sec for RocksDB.
* Commandline: `--rocksdb-stats-dump-period-sec=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `600`
* Range: `0` to `2147483647`

#### `rocksdb_stats_level`

* Description: Statistics Level for RocksDB. Default is 0 (kExceptHistogramOrTimers).
* Commandline: `--rocksdb-stats-level=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `0`
* Range: `0` to `4`
* Introduced: [MariaDB 10.4.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/mariadb-1047-release-notes), [MariaDB 10.3.17](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-10317-release-notes), [MariaDB 10.2.26](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-10226-release-notes)

#### `rocksdb_stats_recalc_rate`

* Description: The number of indexes per second to recalculate statistics for. 0 to disable background recalculation.
* Commandline: `--rocksdb-stats-recalc_rate=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `0`
* Range: `0` to `4294967295`
* Introduced: [MariaDB 10.3.10](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-10310-release-notes) [MariaDB 10.2.18](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-10218-release-notes)

#### `rocksdb_store_row_debug_checksums`

* Description: Include checksums when writing index/table records.
* Commandline: `--rocksdb-store-row-debug-checksums={0|1}`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`

#### `rocksdb_strict_collation_check`

* Description: Enforce case sensitive collation for MyRocks indexes.
* Commandline: `--rocksdb-strict-collation-check={0|1}`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `ON`

#### `rocksdb_strict_collation_exceptions`

* Description: List of tables (using regex) that are excluded from the case sensitive collation enforcement.
* Commandline: `--rocksdb-strict-collation-exceptions=value`
* Scope: Global
* Dynamic: Yes
* Data Type: `string`
* Default Value: (Empty)

#### `rocksdb_supported_compression_types`

* Description: Compression algorithms supported by RocksDB. Note that RocksDB does not make use of [MariaDB 10.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-7-series/what-is-mariadb-107) [compression-plugins](../../../ha-and-performance/optimization-and-tuning/optimization-and-tuning-compression/compression-plugins.md).
* Commandline: `--rocksdb-supported-compression-types=value`
* Scope: Global
* Dynamic: No
* Data Type: `string`
* Default Value: `Snappy,Zlib,ZSTDNotFinal`

#### `rocksdb_table_cache_numshardbits`

* Description: DBOptions::table\_cache\_numshardbits for RocksDB.
* Commandline: `--rocksdb-table-cache-numshardbits=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `6`
* Range: `0` to `19`

#### `rocksdb_table_stats_sampling_pct`

* Description: Percentage of entries to sample when collecting statistics about table properties. Specify either 0 to sample everything or percentage \[1..100]. By default 10% of entries are sampled.
* Commandline: `--rocksdb-table-stats-sampling-pct=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `10`
* Range: `0` to `100`

#### `rocksdb_tmpdir`

* Description: Directory for temporary files during DDL operations.
* Commandline: `--rocksdb-tmpdir[=value]`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `string`
* Default Value: (Empty)

#### `rocksdb_trace_sst_api`

* Description: Generate trace output in the log for each call to the SstFileWriter.
* Commandline: `--rocksdb-trace-sst-api={0|1}`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`

#### `rocksdb_two_write_queues`

* Description: DBOptions::two\_write\_queues for RocksDB.
* Commandline: `--rocksdb-two-write-queues={0|1}`
* Scope: Global,
* Dynamic: No
* Data Type: `boolean`
* Default Value: `ON`
* Introduced: [MariaDB 10.3.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-1037-release-notes), [MariaDB 10.2.15](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-10215-release-notes)

#### `rocksdb_unsafe_for_binlog`

* Description: Allowing statement based binary logging which may break consistency.
* Commandline: `--rocksdb-unsafe-for-binlog={0|1}`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`

#### `rocksdb_update_cf_options`

* Description: Option updates per column family for RocksDB.
* Commandline: `--rocksdb-update-cf-options=value`
* Scope: Global
* Dynamic: Yes
* Data Type: `varchar`
* Default Value: (Empty)
* Introduced: [MariaDB 10.3.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-1031-release-notes), [MariaDB 10.2.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1028-release-notes)

#### `rocksdb_use_adaptive_mutex`

* Description: DBOptions::use\_adaptive\_mutex for RocksDB.
* Commandline: `--rocksdb-use-adaptive-mutex={0|1}`
* Scope: Global
* Dynamic: No
* Data Type: `boolean`
* Default Value: `OFF`

#### `rocksdb_use_clock_cache`

* Description: Use ClockCache instead of default LRUCache for RocksDB.
* Commandline: `--rocksdb-use-clock-cache={0|1}`
* Scope: Global
* Dynamic: No
* Data Type: `boolean`
* Default Value: `OFF`

#### `rocksdb_use_direct_io_for_flush_and_compaction`

* Description: DBOptions::use\_direct\_io\_for\_flush\_and\_compaction for RocksDB.
* Commandline: `--rocksdb-use-direct-io-for-flush-and-compaction={0|1}`
* Scope: Global
* Dynamic: No
* Data Type: `boolean`
* Default Value: `OFF`
* Introduced: [MariaDB 10.3.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-1031-release-notes), [MariaDB 10.2.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1028-release-notes)

#### `rocksdb_use_direct_reads`

* Description: DBOptions::use\_direct\_reads for RocksDB.
* Commandline: `--rocksdb-use-direct-reads={0|1}`
* Scope: Global
* Dynamic: No
* Data Type: `boolean`
* Default Value: `OFF`

#### `rocksdb_use_direct_writes`

* Description: DBOptions::use\_direct\_writes for RocksDB.
* Commandline: `--rocksdb-use-direct-reads={0|1}`
* Scope: Global
* Dynamic: No
* Data Type: `boolean`
* Default Value: `OFF`
* Removed: [MariaDB 10.3.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-1031-release-notes), [MariaDB 10.2.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1028-release-notes)

#### `rocksdb_use_fsync`

* Description: DBOptions::use\_fsync for RocksDB.
* Commandline: `--rocksdb-use-fsync={0|1}`
* Scope: Global
* Dynamic: No
* Data Type: `boolean`
* Default Value: `OFF`

#### `rocksdb_validate_tables`

* Description: Verify all .frm files match all RocksDB tables (0 means no verification, 1 means verify and fail on error, and 2 means verify but continue.
* Commandline: `--rocksdb-validate-tables=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `1`
* Range: `0` to `2`

#### `rocksdb_verify_row_debug_checksums`

* Description: Verify checksums when reading index/table records.
* Commandline: `--rocksdb-verify-row-debug-checksums={0|1}`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`

#### `rocksdb_wal_bytes_per_sync`

* Description: DBOptions::wal\_bytes\_per\_sync for RocksDB.
* Commandline: `--rocksdb-wal-bytes-per-sync=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `0`
* Range: `0` to `18446744073709551615`

#### `rocksdb_wal_dir`

* Description: DBOptions::wal\_dir for RocksDB. Directory where the write-ahead-log files are stored.
* Commandline: `--rocksdb-wal-dir=value`
* Scope: Global
* Dynamic: No
* Data Type: `string`
* Default Value: (Empty)

#### `rocksdb_wal_recovery_mode`

* Description: DBOptions::wal\_recovery\_mode for RocksDB. Default is kAbsoluteConsistency. Records that are not yet committed are stored in the Write-Ahead-Log (WAL). If the server is not cleanly shut down, the recovery mode will determine the WAL recovery behavior.
  * 1: kAbsoluteConsistency. Will not start if any corrupted entries (including incomplete writes) are detected (the default).
  * 0: kTolerateCorruptedTailRecords. Ignores any errors found at the end of the WAL
  * 2: kPointInTimeRecovery. Replay of the WAL is halted after finding an error. The system will be recovered to the latest consistent point-in-time. Data from a replica can used to replay past the point-in-time.
  * 3: kSkipAnyCorruptedRecords. A risky option where any corrupted entries are skipped while subsequent healthy WAL entries are applied.
* Commandline: `--rocksdb-wal-recovery-mode=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `1`
* Range: `0` to `3`

#### `rocksdb_wal_size_limit_mb`

* Description: DBOptions::WAL\_size\_limit\_MB for RocksDB. Write-ahead-log files are moved to an archive directory once their memtables are flushed. This variable specifies the largest size, in MB, that the archive can be.
* Commandline: `--rocksdb-wal-size-limit-mb=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `0`
* Range: `0` to `9223372036854775807`

#### `rocksdb_wal_ttl_seconds`

* Description: DBOptions::WAL\_ttl\_seconds for RocksDB. Oldest time, in seconds, that a write-ahead-log file should exist.
* Commandline: `--rocksdb-wal-ttl-seconds=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `0`
* Range: `0` to `9223372036854775807`

#### `rocksdb_whole_key_filtering`

* Description: BlockBasedTableOptions::whole\_key\_filtering for RocksDB. If set (the default), the bloomfilter to use the whole key (rather than only the prefix) for filtering is enabled. Lookups should use the whole key for matching to make best use of this setting.
* Commandline: `--rocksdb-whole-key-filtering={0|1}`
* Scope: Global
* Dynamic: No
* Data Type: `boolean`
* Default Value: `ON`

#### `rocksdb_write_batch_max_bytes`

* Description: Maximum size of write batch in bytes. 0 means no limit.
* Commandline: `--rocksdb-write-batch-max-bytes=#`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `0`
* Range: `0` to `18446744073709551615`

#### `rocksdb_write_disable_wal`

* Description: WriteOptions::disableWAL for RocksDB.
* Commandline: `--rocksdb-write-disable-wal={0|1}`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`

#### `rocksdb_write_ignore_missing_column_families`

* Description: WriteOptions::ignore\_missing\_column\_families for RocksDB.
* Commandline: `--rocksdb-write-ignore-missing-column-families={0|1}`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`

#### `rocksdb_write_policy`

* Description: DBOptions::write\_policy for RocksDB.
* Commandline: `--rocksdb-write-policy=val`
* Scope: Global
* Dynamic: No
* Data Type: `enum`
* Default Value: `write_committed`
* Valid Values: `write_committed`, `write_prepared`, `write_unprepared`
* Introduced: [MariaDB 10.3.10](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-10310-release-notes), [MariaDB 10.2.18](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-10218-release-notes)

CC BY-SA / Gnu FDL

{% @marketo/form formId="4316" %}
