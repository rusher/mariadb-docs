
# TokuDB Status Variables


TokuDB has been deprecated by its upstream maintainer. It is disabled from [MariaDB 10.5](../../../../release-notes/mariadb-community-server/what-is-mariadb-105.md) and has been been removed in [MariaDB 10.6](../../../../release-notes/mariadb-community-server/what-is-mariadb-106.md) - [MDEV-19780](https://jira.mariadb.org/browse/MDEV-19780). We recommend [MyRocks](../myrocks/myrocks-in-mariadb-102-vs-mariadb-103.md) as a long-term migration path.



This page documents status variables related to the [TokuDB storage engine](tokudb-resources.md). See [Server Status Variables](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-status-variables.md) for a complete list of status variables that can be viewed with [SHOW STATUS](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-status.md).


See also the [Full list of MariaDB options, system and status variables](../../../server-management/variables-and-modes/full-list-of-mariadb-options-system-and-status-variables.md).


#### `<code>Tokudb_basement_deserialization_fixed_key</code>`


* Description: Number of deserialized basement nodes where all keys were the same size. This leaves the basement in an optimal format for in-memory workloads.



#### `<code>Tokudb_basement_deserialization_variable_key</code>`


* Description: Number of deserialized basement nodes where all keys had different size keys, which are not eligible for in-memory optimization.



#### `<code>Tokudb_basements_decompressed_for_write</code>`


* Description: Number of basement nodes decompressed for write operations.



#### `<code>Tokudb_basements_decompressed_prefetch</code>`


* Description: Number of basement nodes decompressed by a prefetch thread. See [tokudb_disable_prefetching](tokudb-system-variables.md#tokudb_disable_prefetching).



#### `<code>Tokudb_basements_decompressed_prelocked_range</code>`


* Description: Number of basement nodes aggressively decompressed by queries.



#### `<code>Tokudb_basements_decompressed_target_query</code>`


* Description: Number of basement nodes decompressed for queries



#### `<code>Tokudb_basements_fetched_for_write</code>`


* Description: Number of basement nodes fetched for writes off the disk.



#### `<code>Tokudb_basements_fetched_for_write_bytes</code>`


* Description: Total basement node bytes fetched for writes off the disk.



#### `<code>Tokudb_basements_fetched_for_write_seconds</code>`


* Description: Time in seconds spent waiting for IO while fetching basement nodes from disk for writes.



#### `<code>Tokudb_basements_fetched_prefetch</code>`


* Description: Number of basement nodes fetched off the disk by a prefetch thread.



#### `<code>Tokudb_basements_fetched_prefetch_bytes</code>`


* Description: Total basement node bytes fetched off the disk by a prefetch thread..



#### `<code>Tokudb_basements_fetched_prefetch_seconds</code>`


* Description: Time in seconds spent waiting for IO while fetching off the disk by a prefetch thread.



#### `<code>Tokudb_basements_fetched_prelocked_range</code>`


* Description: Number of basement nodes aggressively fetched from disk.



#### `<code>Tokudb_basements_fetched_prelocked_range_bytes</code>`


* Description: Total basement node bytes aggressively fetched off the disk.



#### `<code>Tokudb_basements_fetched_prelocked_range_seconds</code>`


* Description: Time in seconds spent waiting for IO while aggressively fetching basement nodes from disk.



#### `<code>Tokudb_basements_fetched_target_query</code>`


* Description: Number of basement nodes fetched for queries off the disk.



#### `<code>Tokudb_basements_fetched_target_query_bytes</code>`


* Description: Total basement node bytes fetched for queries off the disk.



#### `<code>Tokudb_basements_fetched_target_query_seconds</code>`


* Description: Time in seconds spent waiting for IO while fetching basement nodes from disk for queries.



#### `<code>Tokudb_broadcase_messages_injected_at_root</code>`


* Description: Number of broadcast messages injected at root.



#### `<code>Tokudb_buffers_decompressed_for_write</code>`


* Description: Number of buffers decompressed for writes.



#### `<code>Tokudb_buffers_decompressed_prefetch</code>`


* Description: Number of buffers decompressed by a prefetch thread.



#### `<code>Tokudb_buffers_decompressed_prelocked_range</code>`


* Description: Number of buffers decompressed for queries.



#### `<code>Tokudb_buffers_decompressed_target_query</code>`


* Description: Number of buffers aggressively decompressed by queries.



#### `<code>Tokudb_buffers_fetched_for_write</code>`


* Description: Number of buffers fetched for write off the disk.



#### `<code>Tokudb_buffers_fetched_for_write_bytes</code>`


* Description: Total buffer bytes fetched for writes off the disk.



#### `<code>Tokudb_buffers_fetched_for_write_seconds</code>`


* Description: Time in seconds spent waiting for IO while fetching buffers from disk for writes.



#### `<code>Tokudb_buffers_fetched_prefetch</code>`


* Description: Number of buffers fetched for queries off the disk by a prefetch thread.



#### `<code>Tokudb_buffers_fetched_prefetch_bytes</code>`


* Description: Total buffer bytes fetched for queries off the disk by a prefetch thread.



#### `<code>Tokudb_buffers_fetched_prefetch_seconds</code>`


* Description: Time in seconds spent waiting for IO while fetching buffers from disk for queries by a prefetch thread.



#### `<code>Tokudb_buffers_fetched_prelocked_range</code>`


* Description: Number of buffers aggressively fetched for queries off the disk.



#### `<code>Tokudb_buffers_fetched_prelocked_range_bytes</code>`


* Description: Total buffer bytes aggressively fetched for queries off the disk.



#### `<code>Tokudb_buffers_fetched_prelocked_range_seconds</code>`


* Description: Time in seconds spent waiting for IO while aggressively fetching buffers from disk for queries.



#### `<code>Tokudb_buffers_fetched_target_query</code>`


* Description: Number of buffers fetched for queries off the disk.



#### `<code>Tokudb_buffers_fetched_target_query_bytes</code>`


* Description: Total buffer bytes fetched for queries off the disk.



#### `<code>Tokudb_buffers_fetched_target_query_seconds</code>`


* Description: Time in seconds spent waiting for IO while fetching buffers from disk for queries.



#### `<code>Tokudb_cachetable_cleaner_executions</code>`


* Description: Number of times the cleaner thread loop has executed.



#### `<code>Tokudb_cachetable_cleaner_iterations</code>`


* Description: Number of cleaner operations performed each cleaner period.



#### `<code>Tokudb_cachetable_cleaner_period</code>`


* Description: Time in seconds between the end of a group of cleaner operations and the beginning of the next. The TokuDB cleaner thread runs in the background, optimizing indexes and performing work not needing to be done by the client thread.



#### `<code>Tokudb_cachetable_evictions</code>`


* Description: Number of blocks evicted from the cache.



#### `<code>Tokudb_cachetable_long_wait_pressure_count</code>`


* Description: Number of times a thread was stalled for more than one second due to cache pressure.



#### `<code>Tokudb_cachetable_long_wait_pressure_time</code>`


* Description: Time in microseconds spent waiting for more than one second for cache pressure to ease.



#### `<code>Tokudb_cachetable_miss</code>`


* Description: Number of times the system failed to access data in the internal cache.



#### `<code>Tokudb_cachetable_miss_time</code>`


* Description: Total time in microseconds spent waiting for disk reads (when the cache could not supply the data) to finish.



#### `<code>Tokudb_cachetable_prefetches</code>`


* Description: Total number of times that a block of memory was prefetched into the database cache. This happens when it's determined that a block of memory is likely to be accessed by the application.



#### `<code>Tokudb_cachetable_size_cachepressure</code>`


* Description: Size in bytes of data causing cache pressure, or the sum of the buffers and workdone counters.



#### `<code>Tokudb_cachetable_size_cloned</code>`


* Description: Memory in bytes currently used for cloned nodes. Dirty nodes are cloned before serialization/compression during checkpoint operations, after which they are written to disk and the memory freed for re-use.



#### `<code>Tokudb_cachetable_size_current</code>`


* Description: Size in bytes of the uncompressed data in the cache.



#### `<code>Tokudb_cachetable_size_leaf</code>`


* Description: Size in bytes of the leaf nodes in the cache.



#### `<code>Tokudb_cachetable_size_limit</code>`


* Description: Size in bytes of the uncompressed data that could fit in the cache.



#### `<code>Tokudb_cachetable_size_nonleaf</code>`


* Description: Size in bytes of the nonleaf nodes in the cache.



#### `<code>Tokudb_cachetable_size_rollback</code>`


* Description: Size in bytes of the rollback nodes in the cache.



#### `<code>Tokudb_cachetable_size_writing</code>`


* Description: Size in bytes currently queued to be written to disk.



#### `<code>Tokudb_cachetable_wait_pressure_count</code>`


* Description: Number of times a thread was stalled due to cache pressure.



#### `<code>Tokudb_cachetable_wait_pressure_time</code>`


* Description: Time in microseconds spent waiting for cache pressure to ease.



#### `<code>Tokudb_checkpoint_begin_time</code>`


* Description: Cumulative time in microseconds needed to mark all dirty nodes as pending a checkpoint.



#### `<code>Tokudb_checkpoint_duration</code>`


* Description: Time in seconds needed to complete all checkpoints.



#### `<code>Tokudb_checkpoint_duration_last</code>`


* Description: Time in seconds needed to complete the last checkpoint.



#### `<code>Tokudb_checkpoint_failed</code>`


* Description: Total number of checkpoints failed.



#### `<code>Tokudb_checkpoint_last_began</code>`


* Description: Date and time the most recent checkpoint began, for example `<code>Wed May 14 11:26:42 2014</code>` Will be `<code>Dec 31, 1969</code>` on Linux if no checkpoint has ever begun.



#### `<code>Tokudb_checkpoint_last_complete_began</code>`


* Description: Date and time the last complete checkpoint started.



#### `<code>Tokudb_checkpoint_last_complete_ended</code>`


* Description: Date and time the last complete checkpoint ended.



#### `<code>Tokudb_checkpoint_long_begin_count</code>`


* Description: Number of long checkpoint begins (checkpoint begins taking more than 1 second).



#### `<code>Tokudb_checkpoint_long_begin_time</code>`


* Description: Total time in microseconds of long checkpoint begins (checkpoint begins taking more than 1 second).



#### `<code>Tokudb_checkpoint_period</code>`


* Description: Time in seconds between the end of one automatic checkpoint and the beginning of the next.



#### `<code>Tokudb_checkpoint_taken</code>`


* Description: Total number of checkpoints taken.



#### `<code>Tokudb_cursor_skip_deleted_leaf_entry</code>`


* Description: Deleted leaf entries skipped during a range scan.
* Introduced: TokuDB 7.5.4



#### `<code>Tokudb_db_closes</code>`


* Description: Number of db_close operations.



#### `<code>Tokudb_db_open_current</code>`


* Description: Number of databases currently open.



#### `<code>Tokudb_db_open_max</code>`


* Description: Maximum of number of databases open at the same time.



#### `<code>Tokudb_db_opens</code>`


* Description: Number of db_open operations.



#### `<code>Tokudb_descriptor_set</code>`


* Description: Number of times a descriptor was updated when the entire dictionary was updated.



#### `<code>Tokudb_dictionary_broadcast_updates</code>`


* Description: Number of successful broadcast updates (an update that affects all rows in a dictionary).



#### `<code>Tokudb_dictionary_updates</code>`


* Description: Total number of rows updated in all primary and secondary indexes that have been done with a separate recovery log entry per index.



#### `<code>Tokudb_filesystem_fsync_num</code>`


* Description: Total number of times the database has flushed the operating system’s file buffers to
disk.



#### `<code>Tokudb_filesystem_fsync_time</code>`


* Description: Total time in microseconds used to fsync to disk.



#### `<code>Tokudb_filesystem_long_fsync_num</code>`


* Description: Total number of times the database has flushed the operating system’s file buffers to
disk when the operation took more than one second.



#### `<code>Tokudb_filesystem_long_fsync_time</code>`


* Description: Total time in microseconds used to fsync to disk when the operation took more than one second.



#### `<code>Tokudb_filesystem_threads_blocked_by_full_disk</code>`


* Description: Number of threads currently blocked due to attempting to write to a full disk. A warning appears in the `<code>disk free space</code>` field if not zero.



#### `<code>Tokudb_leaf_compression_to_memory_seconds</code>`


* Description: Time in seconds spent on compressing leaf nodes.



#### `<code>Tokudb_leaf_decompression_to_memory_seconds</code>`


* Description: Time in seconds spent on decompressing leaf nodes.



#### `<code>Tokudb_leaf_deserialization_to_memory_seconds</code>`


* Description: Time in seconds spent on deserializing leaf nodes.



#### `<code>Tokudb_leaf_node_compression_ratio</code>`


* Description: Ratio of uncompressed bytes in-memory to compressed bytes on-disk for leaf nodes.



#### `<code>Tokudb_leaf_node_full_evictions</code>`


* Description: Number of times a full leaf node was evicted from the cache.



#### `<code>Tokudb_leaf_node_full_evictions_bytes</code>`


* Description: Total bytes freed when a full leaf node was evicted from the cache.



#### `<code>Tokudb_leaf_node_partial_evictions</code>`


* Description: Number of times part of a leaf node (a partition) was evicted from the cache.



#### `<code>Tokudb_leaf_node_partial_evictions_bytes</code>`


* Description: Total bytes freed when part of a leaf node (a partition) was evicted from the cache.



#### `<code>Tokudb_leaf_nodes_created</code>`


* Description: Total number of leaf nodes created.



#### `<code>Tokudb_leaf_nodes_destroyed</code>`


* Description: Total number of leaf nodes destroyed.



#### `<code>Tokudb_leaf_nodes_flushed_checkpoint</code>`


* Description: Number of leaf nodes flushed to disk as part of a checkpoint.



#### `<code>Tokudb_leaf_nodes_flushed_checkpoint_bytes</code>`


* Description: Size in bytes of leaf nodes flushed to disk as part of a checkpoint.



#### `<code>Tokudb_leaf_nodes_flushed_checkpoint_seconds</code>`


* Description: Time in seconds spent waiting for IO while writing leaf nodes flushed to disk as part of a checkpoint.



#### `<code>Tokudb_leaf_nodes_flushed_checkpoint_uncompressed_bytes</code>`


* Description: Size in uncompressed bytes of leaf nodes flushed to disk as part of a checkpoint.



#### `<code>Tokudb_leaf_nodes_flushed_not_checkpoint</code>`


* Description: Number of leaf nodes flushed to disk not as part of a checkpoint.



#### `<code>Tokudb_leaf_nodes_flushed_not_checkpoint_bytes</code>`


* Description: Size in bytes of leaf nodes flushed to disk not as part of a checkpoint.



#### `<code>Tokudb_leaf_nodes_flushed_not_checkpoint_seconds</code>`


* Description: Time in seconds spent waiting for IO while writing leaf nodes flushed to disk not as part of a checkpoint.



#### `<code>Tokudb_leaf_nodes_flushed_not_checkpoint_uncompressed_bytes</code>`


* Description: Size in uncompressed bytes of leaf nodes flushed to disk not as part of a checkpoint.



#### `<code>Tokudb_leaf_serialization_to_memory_seconds</code>`


* Description: Time in seconds spent on serializing leaf nodes.



#### `<code>Tokudb_loader_num_created</code>`


* Description: Number of times a loader has been created.



#### `<code>Tokudb_loader_num_current</code>`


* Description: Number of currently existing loaders.



#### `<code>Tokudb_loader_num_max</code>`


* Description: Maximum number of loaders that existed at one time.



#### `<code>Tokudb_locktree_escalation_num</code>`


* Description: Number of times the locktree needed reduce its memory footprint by running lock escalation.



#### `<code>Tokudb_locktree_escalation_seconds</code>`


* Description: Time in seconds spent performing locktree escalation.



#### `<code>Tokudb_locktree_latest_post_escalation_memory_size</code>`


* Description: Memory size in bytes of the locktree after most recent locktree escalation.



#### `<code>Tokudb_locktree_long_wait_count</code>`


* Description: Number of times of more than one second duration that a lock could not be acquired as a result of a conflict with another transaction.



#### `<code>Tokudb_locktree_long_wait_escalation_count</code>`


* Description: Number of times a client thread waited for more than one second for lock escalation to free up memory.



#### `<code>Tokudb_locktree_long_wait_escalation_time</code>`


* Description: Time in microseconds of long waits (more than one second) for lock escalation to free up memory.



#### `<code>Tokudb_locktree_long_wait_time</code>`


* Description:Total time in microseconds spent by clients waiting for more than one second for a lock conflict to be resolved.



#### `<code>Tokudb_locktree_memory_size</code>`


* Description: Memory in bytes currently being used by the locktree.



#### `<code>Tokudb_locktree_memory_size_limit</code>`


* Description: Maximum memory in bytes the locktree can use.



#### `<code>Tokudb_locktree_open_current</code>`


* Description: Number of currently open locktrees.



#### `<code>Tokudb_locktree_pending_lock_requests</code>`


* Description: Number of requests waiting for a lock to be granted.



#### `<code>Tokudb_locktree_sto_eligible_num</code>`


* Description: Number of locktrees eligible for single transaction optimizations.



#### `<code>Tokudb_locktree_sto_ended_num</code>`


* Description: Total number of times a single transaction optimization completed early as a result of another transaction beginning.



#### `<code>Tokudb_locktree_sto_ended_seconds</code>`


* Description: Time in seconds spent ending single transaction optimizations.



#### `<code>Tokudb_locktree_timeout_count</code>`


* Description: Number of times a lock request timed out.



#### `<code>Tokudb_locktree_wait_count</code>`


* Description: Number of times a lock could not be acquired as a result of a conflict with another transaction.



#### `<code>Tokudb_locktree_wait_escalation_count</code>`


* Description: Number of times a client thread has waited on lock escalation. Lock escalation is run on a background thread when the sum of the acquired lock sizes reaches the lock tree limit.



#### `<code>Tokudb_locktree_wait_escalation_time</code>`


* Description: Time in microseconds that a client thread spent waiting for lock escalation.



#### `<code>Tokudb_locktree_wait_time</code>`


* Description: Total time in microseconds spent by clients waiting for a lock conflict to be resolved.



#### `<code>Tokudb_logger_wait_long</code>`


* Description:



#### `<code>Tokudb_logger_writes</code>`


* Description: Number of times the logger has written to disk.



#### `<code>Tokudb_logger_writes_bytes</code>`


* Description: Total bytes the logger has written to disk.



#### `<code>Tokudb_logger_writes_seconds</code>`


* Description: Time in seconds spent waiting for IO while writing logs to disk.



#### `<code>Tokudb_logger_writes_uncompressed_bytes</code>`


* Description: Total uncompressed bytes the logger has written to disk.



#### `<code>Tokudb_mem_estimated_maximum_memory_footprint</code>`


* Description:



#### `<code>Tokudb_messages_flushed_from_h1_to_leaves_bytes</code>`


* Description: Total bytes of the messages flushed from h1 nodes to leaves.



#### `<code>Tokudb_messages_ignored_by_leaf_due_to_msn</code>`


* Description: Number of messages ignored by a leaf because it had already been applied.



#### `<code>Tokudb_messages_in_trees_estimate_bytes</code>`


* Description: Estimate of the total bytes of messages currently in trees.



#### `<code>Tokudb_messages_injected_at_root</code>`


* Description: Number of messages injected at root.



#### `<code>Tokudb_messages_injected_at_root_bytes</code>`


* Description: Total bytes of messages injected at root for all trees.



#### `<code>Tokudb_nonleaf_compression_to_memory_seconds</code>`


* Description: Time in seconds spent on compressing non-leaf nodes.



#### `<code>Tokudb_nonleaf_decompression_to_memory_seconds</code>`


* Description: Time in seconds spent on decompressing non-leaf nodes.



#### `<code>Tokudb_nonleaf_deserialization_to_memory_seconds</code>`


* Description: Time in seconds spent on deserializing non-leaf nodes.



#### `<code>Tokudb_nonleaf_node_compression_ratio</code>`


* Description: Ratio of uncompressed bytes in-memory to compressed bytes on-disk for nonleaf nodes.



#### `<code>Tokudb_nonleaf_node_full_evictions</code>`


* Description: Number of times a full non-leaf node was evicted from the cache.



#### `<code>Tokudb_nonleaf_node_full_evictions_bytes</code>`


* Description: Total bytes freed when a full non-leaf node was evicted from the cache.



#### `<code>Tokudb_nonleaf_node_partial_evictions</code>`


* Description: Number of times part of a non-leaf node (a partition) was evicted from the cache.



#### `<code>Tokudb_nonleaf_node_partial_evictions_bytes</code>`


* Description: Total bytes freed when part of a non-leaf node (a partition) was evicted from the cache.



#### `<code>Tokudb_nonleaf_nodes_created</code>`


* Description: Total number of non-leaf nodes created.



#### `<code>Tokudb_nonleaf_nodes_destroyed</code>`


* Description: Total number of non-leaf nodes destroyed.



#### `<code>Tokudb_nonleaf_nodes_flushed_to_disk_checkpoint</code>`


* Description: Number of non-leaf nodes flushed to disk as part of a checkpoint.



#### `<code>Tokudb_nonleaf_nodes_flushed_to_disk_checkpoint_bytes</code>`


* Description: Size in bytes of non-leaf nodes flushed to disk as part of a checkpoint.



#### `<code>Tokudb_nonleaf_nodes_flushed_to_disk_checkpoint_seconds</code>`


* Description: Time in seconds spent waiting for IO while writing non-leaf nodes flushed to disk as part of a checkpoint.



#### `<code>Tokudb_nonleaf_nodes_flushed_to_disk_checkpoint_uncompressed_bytes</code>`


* Description: Size in uncompressed bytes of non-leaf nodes flushed to disk as part of a checkpoint.



#### `<code>Tokudb_nonleaf_nodes_flushed_to_disk_not_checkpoint</code>`


* Description: Number of non-leaf nodes flushed to disk not as part of a checkpoint.



#### `<code>Tokudb_nonleaf_nodes_flushed_to_disk_not_checkpoint_bytes</code>`


* Description: Size in bytes of non-leaf nodes flushed to disk not as part of a checkpoint.



#### `<code>Tokudb_nonleaf_nodes_flushed_to_disk_not_checkpoint_seconds</code>`


* Description: Time in seconds spent waiting for IO while writing non-leaf nodes flushed to disk not as part of a checkpoint.



#### `<code>Tokudb_nonleaf_nodes_flushed_to_disk_not_checkpoint_uncompressed_bytes</code>`


* Description: Size in uncompressed bytes of non-leaf nodes flushed to disk not as part of a checkpoint.



#### `<code>Tokudb_nonleaf_serialization_to_memory_seconds</code>`


* Description: Time in seconds spent on serializing nonleaf nodes.



#### `<code>Tokudb_overall_node_compression_ratio</code>`


* Description: Ratio of uncompressed bytes in-memory to compressed bytes on-disk for all nodes.



#### `<code>Tokudb_pivots_fetched_for_query</code>`


* Description: Total number of pivot nodes fetched for queries.



#### `<code>Tokudb_pivots_fetched_for_query_bytes</code>`


* Description: Number of bytes of pivot nodes fetched for queries.



#### `<code>Tokudb_pivots_fetched_for_query_seconds</code>`


* Description: Time in seconds spent waiting for IO while fetching pivot nodes for queries.



#### `<code>Tokudb_pivots_fetched_for_prefetch</code>`


* Description: Total number of pivot nodes fetched by a prefetch thread.



#### `<code>Tokudb_pivots_fetched_for_prefetch_bytes</code>`


* Description: Number of bytes of pivot nodes fetched by a prefetch thread.



#### `<code>Tokudb_pivots_fetched_for_prefetch_seconds</code>`


* Description: Time in seconds spent waiting for IO while fetching pivot nodes by a prefetch thread.



#### `<code>Tokudb_pivots_fetched_for_write</code>`


* Description: Total number of pivot nodes fetched for writes.



#### `<code>Tokudb_pivots_fetched_for_write_bytes</code>`


* Description: Number of bytes of pivot nodes fetched for writes.



#### `<code>Tokudb_pivots_fetched_for_write_seconds</code>`


* Description: Time in seconds spent waiting for IO while fetching pivot nodes for writes.



#### `<code>Tokudb_promotion_h1_roots_injected_into</code>`


* Description: Number of times a message stopped at a root with a height of 1.



#### `<code>Tokudb_promotion_injections_at_depth_0</code>`


* Description: Number of times a message stopped at a depth of zero.



#### `<code>Tokudb_promotion_injections_at_depth_1</code>`


* Description: Number of times a message stopped at a depth of one.



#### `<code>Tokudb_promotion_injections_at_depth_2</code>`


* Description: Number of times a message stopped at a depth of two.



#### `<code>Tokudb_promotion_injections_at_depth_3</code>`


* Description: Number of times a message stopped at a depth of three.



#### `<code>Tokudb_promotion_injections_lower_than_depth_3</code>`


* Description: Number of times a message stopped at a depth of greater than three.



#### `<code>Tokudb_promotion_leaf_roots_injected_into</code>`


* Description: Number of times a message stopped at a root with a height of 0.



#### `<code>Tokudb_promotion_roots_split</code>`


* Description: Number of times the root split during promotion.



#### `<code>Tokudb_promotion_stopped_after_locking_child</code>`


* Description: Number of times a message stopped before a locked child.



#### `<code>Tokudb_promotion_stopped_at_height_1</code>`


* Description: Number of times a message stopped due to reaching a height of one.



#### `<code>Tokudb_promotion_stopped_child_locked_or_not_in_memory</code>`


* Description: Number of times a message stopped due to being unable to cheaply access (locked or not stored in memory) a child.



#### `<code>Tokudb_promotion_stopped_child_not_fully_in_memory</code>`


* Description: Number of times a message stopped due to being unable to cheaply access (not fully stored in memory) a child.



#### `<code>Tokudb_promotion_stopped_nonempty_buffer</code>`


* Description: Number of times a message stopped due to reaching a buffer that wasn't empty.



#### `<code>Tokudb_txn_aborts</code>`


* Description: Number of transactions that have been aborted.



#### `<code>Tokudb_txn_begin</code>`


* Description: Number of transactions that have been started.



#### `<code>Tokudb_txn_begin_read_only</code>`


* Description: Number of read-only transactions that have been started.



#### `<code>Tokudb_txn_commits</code>`


* Description: Number of transactions that have been committed.


