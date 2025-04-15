
# MyRocks Status Variables


This page documents status variables related to the [MyRocks](myrocks-in-mariadb-102-vs-mariadb-103.md) storage engine. See [Server Status Variables](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-status-variables.md) for a complete list of status variables that can be viewed with [SHOW STATUS](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-status.md).


See also the [Full list of MariaDB options, system and status variables](../../../server-management/variables-and-modes/full-list-of-mariadb-options-system-and-status-variables.md).


#### `<code>Rocksdb_block_cache_add</code>`


* Description: Number of blocks added to the Block Cache.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`



#### `<code>Rocksdb_block_cache_add_failures</code>`


* Description: Number of failures when adding blocks to Block Cache.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`
* Introduced: [MariaDB 10.2.15](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-10215-release-notes.md), [MariaDB 10.3.7](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1037-release-notes.md)



#### `<code>Rocksdb_block_cache_bytes_read</code>`


* Description: Bytes read from Block Cache.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`
* Introduced: [MariaDB 10.2.15](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-10215-release-notes.md), [MariaDB 10.3.7](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1037-release-notes.md)



#### `<code>Rocksdb_block_cache_bytes_write</code>`


* Description: Bytes written to Block Cache.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`
* Introduced: [MariaDB 10.2.15](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-10215-release-notes.md), [MariaDB 10.3.7](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1037-release-notes.md)



#### `<code>Rocksdb_block_cache_data_add</code>`


* Description: Number of data blocks added to the Block Cache.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`
* Introduced: [MariaDB 10.2.15](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-10215-release-notes.md), [MariaDB 10.3.7](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1037-release-notes.md)



#### `<code>Rocksdb_block_cache_data_bytes_insert</code>`


* Description: Bytes added to the Block Cache.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`
* Introduced: [MariaDB 10.2.15](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-10215-release-notes.md), [MariaDB 10.3.7](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1037-release-notes.md)



#### `<code>Rocksdb_block_cache_data_hit</code>`


* Description: Number of hits when accessing the data block from the Block Cache.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`



#### `<code>Rocksdb_block_cache_data_miss</code>`


* Description: Number of misses when accessing the data block from the Block Cache.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`



#### `<code>Rocksdb_block_cache_filter_add</code>`


* Description: Number of bloom filter blocks added to the Block Cache.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`
* Introduced: [MariaDB 10.2.15](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-10215-release-notes.md), [MariaDB 10.3.7](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1037-release-notes.md)



#### `<code>Rocksdb_block_cache_filter_bytes_evict</code>`


* Description: Bytes of bloom filter blocks evicted from the Block Cache.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`
* Introduced: [MariaDB 10.2.15](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-10215-release-notes.md), [MariaDB 10.3.7](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1037-release-notes.md)



#### `<code>Rocksdb_block_cache_filter_bytes_insert</code>`


* Description: Bytes of bloom filter blocks added to the Block Cache.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`
* Introduced: [MariaDB 10.2.15](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-10215-release-notes.md), [MariaDB 10.3.7](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1037-release-notes.md)



#### `<code>Rocksdb_block_cache_filter_hit</code>`


* Description: Number of hits when accessing the filter block from the Block Cache.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`



#### `<code>Rocksdb_block_cache_filter_miss</code>`


* Description: Number of misses when accessing the filter block from the Block Cache.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`



#### `<code>Rocksdb_block_cache_hit</code>`


* Description: Total number of hits for the Block Cache.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`



#### `<code>Rocksdb_block_cache_index_add</code>`


* Description: Number of index blocks added to Block Cache index.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`
* Introduced: [MariaDB 10.2.15](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-10215-release-notes.md), [MariaDB 10.3.7](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1037-release-notes.md)



#### `<code>Rocksdb_block_cache_index_bytes_evict</code>`


* Description: Bytes of index blocks evicted from the Block Cache.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`
* Introduced: [MariaDB 10.2.15](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-10215-release-notes.md), [MariaDB 10.3.7](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1037-release-notes.md)



#### `<code>Rocksdb_block_cache_index_bytes_insert</code>`


* Description: Bytes of index blocks added to the Block Cache.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`
* Introduced: [MariaDB 10.2.15](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-10215-release-notes.md), [MariaDB 10.3.7](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1037-release-notes.md)



#### `<code>Rocksdb_block_cache_index_hit</code>`


* Description: Number of hits for the Block Cache index.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`



#### `<code>Rocksdb_block_cache_index_miss</code>`


* Description: Number of misses for the Block Cache index.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`



#### `<code>Rocksdb_block_cache_miss</code>`


* Description: Total number of misses for the Block Cache.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`



#### `<code>Rocksdb_block_cachecompressed_hit</code>`


* Description: Number of hits for the compressed Block Cache.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`



#### `<code>Rocksdb_block_cachecompressed_miss</code>`


* Description: Number of misses for the compressed Block Cache.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`



#### `<code>Rocksdb_bloom_filter_full_positive</code>`


* Description:
* Scope: Global, Session
* Data Type: `<code>numeric</code>`
* Introduced: [MariaDB 10.2.18](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-10218-release-notes.md), [MariaDB 10.3.10](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-10310-release-notes.md)



#### `<code>Rocksdb_bloom_filter_full_true_positive</code>`


* Description:
* Scope: Global, Session
* Data Type: `<code>numeric</code>`
* Introduced: [MariaDB 10.2.18](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-10218-release-notes.md), [MariaDB 10.3.10](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-10310-release-notes.md)



#### `<code>Rocksdb_bloom_filter_prefix_checked</code>`


* Description: Number of times the Bloom Filter checked before creating an iterator on a file.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`



#### `<code>Rocksdb_bloom_filter_prefix_useful</code>`


* Description: Number of times the Bloom Filter check used to avoid creating an iterator on a file.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`



#### `<code>Rocksdb_bloom_filter_useful</code>`


* Description: Number of times the Bloom Filter used instead of reading form file.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`



#### `<code>Rocksdb_bytes_read</code>`


* Description: Total number of uncompressed bytes read from memtables, cache or table files.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`



#### `<code>Rocksdb_bytes_written</code>`


* Description: Total number of uncompressed bytes written.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`



#### `<code>Rocksdb_compact_read_bytes</code>`


* Description: Number of bytes read during compaction.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`



#### `<code>Rocksdb_compact_write_bytes</code>`


* Description: Number of bytes written during compaction.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`



#### `<code>Rocksdb_compaction_key_drop_new</code>`


* Description: Number of keys dropped during compaction due their being overwritten by new values.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`



#### `<code>Rocksdb_compaction_key_drop_obsolete</code>`


* Description: Number of keys dropped during compaction due to their being obsolete.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`



#### `<code>Rocksdb_compaction_key_drop_user</code>`


* Description: Number of keys dropped during compaction due to user compaction.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`



#### `<code>Rocksdb_covered_secondary_key_lookups</code>`


* Description: Incremented when avoiding reading a record via a keyread. This indicates lookups that were performed via a secondary index containing a field that is only a prefix of the [VARCHAR](../../data-types/string-data-types/varchar.md) column, and that could return all requested fields directly from the secondary index.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`



#### `<code>Rocksdb_flush_write_bytes</code>`


* Description: Number of bytes written during flush.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`



#### `<code>Rocksdb_get_hit_l0</code>`


* Description: Number of times reads got data from the L0 compaction layer.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`
* Introduced: [MariaDB 10.2.15](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-10215-release-notes.md), [MariaDB 10.3.7](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1037-release-notes.md)



#### `<code>Rocksdb_get_hit_l1</code>`


* Description: Number of times reads got data from the L1 compaction layer.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`
* Introduced: [MariaDB 10.2.15](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-10215-release-notes.md), [MariaDB 10.3.7](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1037-release-notes.md)



#### `<code>Rocksdb_get_hit_l2_and_up</code>`


* Description: Number of times reads got data from the L2 and up compaction layer.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`
* Introduced: [MariaDB 10.2.15](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-10215-release-notes.md), [MariaDB 10.3.7](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1037-release-notes.md)



#### `<code>Rocksdb_getupdatessince_calls</code>`


* Description: Number of calls to the `<code>GetUpdatesSince</code>` function. You may find this useful when monitoring refreshes of the transaction log.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`



#### `<code>Rocksdb_iter_bytes_read</code>`


* Description: Total uncompressed bytes read from an iterator, including the size of both key and value.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`
* Introduced: [MariaDB 10.2.15](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-10215-release-notes.md), [MariaDB 10.3.7](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1037-release-notes.md)



#### `<code>Rocksdb_l0_num_files_stall_micros</code>`


* Description: Shows how long in microseconds throttled due to too mnay files in L0.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`
* Removed: [MariaDB 10.3.1](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1031-release-notes.md), [MariaDB 10.2.8](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1028-release-notes.md)



#### `<code>Rocksdb_l0_slowdown_micros</code>`


* Description: Total time spent waiting in microseconds while performing L0-L1 compactions.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`
* Removed: [MariaDB 10.3.1](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1031-release-notes.md), [MariaDB 10.2.8](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1028-release-notes.md)



#### `<code>Rocksdb_manual_compactions_processed</code>`


* Description:
* Scope: Global, Session
* Data Type: `<code>numeric</code>`
* Introduced: [MariaDB 10.2.18](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-10218-release-notes.md), [MariaDB 10.3.10](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-10310-release-notes.md)



#### `<code>Rocksdb_manual_compactions_running</code>`


* Description:
* Scope: Global, Session
* Data Type: `<code>numeric</code>`
* Introduced: [MariaDB 10.2.18](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-10218-release-notes.md), [MariaDB 10.3.10](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-10310-release-notes.md)



#### `<code>Rocksdb_memtable_compaction_micros</code>`


* Description:
* Scope: Global, Session
* Data Type: `<code>numeric</code>`
* Removed: [MariaDB 10.3.1](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1031-release-notes.md), [MariaDB 10.2.8](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1028-release-notes.md)



#### `<code>Rocksdb_memtable_hit</code>`


* Description: Number of memtable hits.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`



#### `<code>Rocksdb_memtable_miss</code>`


* Description: Number of memtable misses.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`



#### `<code>Rocksdb_memtable_total</code>`


* Description: Memory used, in bytes, of all memtables.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`



#### `<code>Rocksdb_memtable_unflushed</code>`


* Description: Memory used, in bytes, of all unflushed memtables.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`



#### `<code>Rocksdb_no_file_closes</code>`


* Description: Number of times files were closed.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`



#### `<code>Rocksdb_no_file_errors</code>`


* Description: Number of errors encountered while trying to read data from an SST file.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`



#### `<code>Rocksdb_no_file_opens</code>`


* Description: Number of times files were opened.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`



#### `<code>Rocksdb_num_iterators</code>`


* Description: Number of iterators currently open.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`



#### `<code>Rocksdb_number_block_not_compressed</code>`


* Description: Number of uncompressed blocks.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`



#### `<code>Rocksdb_number_db_next</code>`


* Description: Number of `<code>next</code>` calls.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`
* Introduced: [MariaDB 10.2.15](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-10215-release-notes.md), [MariaDB 10.3.7](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1037-release-notes.md)



#### `<code>Rocksdb_number_db_next_found</code>`


* Description: Number of `<code>next</code>` calls that returned data.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`
* Introduced: [MariaDB 10.2.15](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-10215-release-notes.md), [MariaDB 10.3.7](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1037-release-notes.md)



#### `<code>Rocksdb_number_db_prev</code>`


* Description: Number of `<code>prev</code>` calls.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`
* Introduced: [MariaDB 10.2.15](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-10215-release-notes.md), [MariaDB 10.3.7](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1037-release-notes.md)



#### `<code>Rocksdb_number_db_prev_found</code>`


* Description: Number of `<code>prev</code>` calls that returned data.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`
* Introduced: [MariaDB 10.2.15](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-10215-release-notes.md), [MariaDB 10.3.7](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1037-release-notes.md)



#### `<code>Rocksdb_number_db_seek</code>`


* Description: Number of `<code>seek</code>` calls.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`
* Introduced: [MariaDB 10.2.15](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-10215-release-notes.md), [MariaDB 10.3.7](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1037-release-notes.md)



#### `<code>Rocksdb_number_db_seek_found</code>`


* Description: Number of `<code>seek</code>` calls that returned data.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`
* Introduced: [MariaDB 10.2.15](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-10215-release-notes.md), [MariaDB 10.3.7](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1037-release-notes.md)



#### `<code>Rocksdb_number_deletes_filtered</code>`


* Description: Number of deleted records were not written to storage due to a nonexistent key.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`



#### `<code>Rocksdb_number_keys_read</code>`


* Description: Number of keys have been read.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`



#### `<code>Rocksdb_number_keys_updated</code>`


* Description: Number of keys have been updated.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`



#### `<code>Rocksdb_number_keys_written</code>`


* Description: Number of keys have been written.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`



#### `<code>Rocksdb_number_merge_failures</code>`


* Description: Number of failures encountered while performing merge operator actions.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`



#### `<code>Rocksdb_number_multiget_bytes_read</code>`


* Description: Number of bytes read during RocksDB `<code>MultiGet()</code>` calls.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`



#### `<code>Rocksdb_number_multiget_get</code>`


* Description: Number of RocksDB `<code>MultiGet()</code>` requests made.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`



#### `<code>Rocksdb_number_multiget_keys_read</code>`


* Description: Number of keys read through RocksDB `<code>MultiGet()</code>` calls.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`



#### `<code>Rocksdb_number_reseeks_iteration</code>`


* Description: Number of reseeks that have occurred inside an iteration that skipped over a large number of keys with the same user key.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`



#### `<code>Rocksdb_number_sst_entry_delete</code>`


* Description: Number of delete markers written.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`



#### `<code>Rocksdb_number_sst_entry_merge</code>`


* Description: Number of merge keys written.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`



#### `<code>Rocksdb_number_sst_entry_other</code>`


* Description: Number of keys written that are not delete, merge or put keys.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`



#### `<code>Rocksdb_number_sst_entry_put</code>`


* Description: Number of put keys written.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`



#### `<code>Rocksdb_number_sst_entry_singledelete</code>`


* Description: Number of single-delete keys written.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`



#### `<code>Rocksdb_number_superversion_acquires</code>`


* Description: Number of times the superversion structure acquired. This is useful when tracking files for the database.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`



#### `<code>Rocksdb_number_superversion_cleanups</code>`


* Description: Number of times the superversion structure performed cleanups.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`



#### `<code>Rocksdb_number_superversion_releases</code>`


* Description: Number of times the superversion structure released.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`



#### `<code>Rocksdb_queries_point</code>`


* Description: Number of single-row queries.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`



#### `<code>Rocksdb_queries_range</code>`


* Description: Number of multi-row queries.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`



#### `<code>Rocksdb_row_lock_deadlocks</code>`


* Description: Number of deadlocks.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`
* Introduced: [MariaDB 10.2.15](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-10215-release-notes.md), [MariaDB 10.3.7](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1037-release-notes.md)



#### `<code>Rocksdb_row_lock_wait_timeouts</code>`


* Description: Number of row lock wait timeouts.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`
* Introduced: [MariaDB 10.2.15](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-10215-release-notes.md), [MariaDB 10.3.7](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1037-release-notes.md)



#### `<code>Rocksdb_rows_deleted</code>`


* Description: Number of rows deleted.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`



#### `<code>Rocksdb_rows_deleted_blind</code>`


* Description:
* Scope: Global, Session
* Data Type: `<code>numeric</code>`



#### `<code>Rocksdb_rows_expired</code>`


* Description: Number of expired rows.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`



#### `<code>Rocksdb_rows_filtered</code>`


* Description: Number of TTL filtered rows.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`
* Introduced: [MariaDB 10.2.15](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-10215-release-notes.md), [MariaDB 10.3.7](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1037-release-notes.md)



#### `<code>Rocksdb_rows_inserted</code>`


* Description: Number of rows inserted.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`



#### `<code>Rocksdb_rows_read</code>`


* Description: Number of rows read.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`



#### `<code>Rocksdb_rows_updated</code>`


* Description: Number of rows updated.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`



#### `<code>Rocksdb_snapshot_conflict_errors</code>`


* Description: Number of snapshot conflict errors that have occurred during transactions that forced a rollback.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`



#### `<code>Rocksdb_stall_l0_file_count_limit_slowdowns</code>`


* Description: Write slowdowns due to L0 being near to full.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`



#### `<code>Rocksdb_stall_l0_file_count_limit_stops</code>`


* Description: Write stops due to L0 being to full.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`



#### `<code>Rocksdb_stall_locked_l0_file_count_limit_slowdowns</code>`


* Description: Write slowdowns due to L0 being near to full and L0 compaction in progress.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`



#### `<code>Rocksdb_stall_locked_l0_file_count_limit_stops</code>`


* Description: Write stops due to L0 being full and L0 compaction in progress.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`



#### `<code>Rocksdb_stall_memtable_limit_slowdowns</code>`


* Description: Write slowdowns due to approaching maximum permitted number of memtables.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`
* Introduced: [MariaDB 10.2.10](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-10210-release-notes.md), [MariaDB 10.3.3](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1033-release-notes.md)



#### `<code>Rocksdb_stall_memtable_limit_stops</code>`


* Description: * Description: Write stops due to reaching maximum permitted number of memtables.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`
* Introduced: [MariaDB 10.2.10](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-10210-release-notes.md), [MariaDB 10.3.3](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1033-release-notes.md)



#### `<code>Rocksdb_stall_micros</code>`


* Description: Time in microseconds that the writer had to wait for the compaction or flush to complete.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`



#### `<code>Rocksdb_stall_pending_compaction_limit_slowdowns</code>`


* Description: Write slowdowns due to nearing the limit for the maximum number of pending compaction bytes.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`



#### `<code>Rocksdb_stall_pending_compaction_limit_stops</code>`


* Description: Write stops due to reaching the limit for the maximum number of pending compaction bytes.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`



#### `<code>Rocksdb_stall_total_slowdowns</code>`


* Description: Total number of write slowdowns.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`



#### `<code>Rocksdb_stall_total_stops</code>`


* Description: Total number of write stops.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`



#### `<code>Rocksdb_system_rows_deleted</code>`


* Description: Number of rows deleted from system tables.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`



#### `<code>Rocksdb_system_rows_inserted</code>`


* Description: Number of rows inserted into system tables.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`



#### `<code>Rocksdb_system_rows_read</code>`


* Description: Number of rows read from system tables.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`



#### `<code>Rocksdb_system_rows_updated</code>`


* Description: Number of rows updated for system tables.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`



#### `<code>Rocksdb_wal_bytes</code>`


* Description: Number of bytes written to WAL.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`



#### `<code>Rocksdb_wal_group_syncs</code>`


* Description: Number of group commit WAL file syncs have occurred. This is provided by MyRocks and is not a view of a RocksDB counter. Increased in `<code>rocksdb_flush_wal()</code>` when doing the `<code>rdb->FlushWAL()</code>` call.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`



#### `<code>Rocksdb_wal_synced</code>`


* Description: Number of syncs made on RocksDB WAL file.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`



#### `<code>Rocksdb_write_other</code>`


* Description: Number of writes processed by a thread other than the requesting thread.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`



#### `<code>Rocksdb_write_self</code>`


* Description: Number of writes processed by requesting thread.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`



#### `<code>Rocksdb_write_timedout</code>`


* Description: Number of writes that timed out.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`



#### `<code>Rocksdb_write_wal</code>`


* Description: Number of write calls that requested WAL.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`


