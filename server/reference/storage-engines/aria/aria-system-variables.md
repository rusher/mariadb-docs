
# Aria System Variables

This page documents system variables related to the [Aria storage engine](../s3-storage-engine/aria_s3_copy.md). For options that are not system variables, see [Aria Options](../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md).


See [Server System Variables](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md) for a complete list of system variables and instructions on setting system variables.


Also see the [Full list of MariaDB options, system and status variables](../../../server-management/variables-and-modes/full-list-of-mariadb-options-system-and-status-variables.md).


#### `<code>aria_block_size</code>`


* Description: Block size to be used for Aria index pages. Changing this requires dumping, deleting old tables and deleting all log files, and then restoring your Aria tables. If key lookups take too long (and one has to search roughly 8192/2 by default to find each key), can be made smaller, e.g. `<code>4096</code>`.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--aria-block-size=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value: `<code>8192</code>`
* Range:

  * >= [MariaDB 10.4.7](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-4-series/mariadb-1047-release-notes.md): `<code>4096</code>` to `<code>32768</code>` in increments of `<code>1024</code>`
  * <= [MariaDB 10.4.6](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-4-series/mariadb-1046-release-notes.md): `<code>1024</code>` to `<code>32768</code>` in increments of `<code>1024</code>`



#### `<code>aria_checkpoint_interval</code>`


* Description: Interval in seconds between automatic checkpoints. 0 means 'no automatic checkpoints' which makes sense only for testing.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--aria-checkpoint-interval=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>30</code>`
* Range: `<code>0</code>` to `<code>4294967295</code>`



#### `<code>aria_checkpoint_log_activity</code>`


* Description: Number of bytes that the transaction log has to grow between checkpoints before a new checkpoint is written to the log.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">aria-checkpoint-log-activity=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>1048576</code>`
* Range `<code>0</code>` to `<code>4294967295</code>`



#### `<code>aria_encrypt_tables</code>`


* Description: Enables automatic encryption of all user-created Aria tables that have the `<code>[ROW_FORMAT](../../sql-statements-and-structure/vectors/create-table-with-vectors.md#row_format)</code>` table option set to `<code>[PAGE](aria-storage-formats.md#page)</code>`. See [Data at Rest Encryption](../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/data-at-rest-encryption-overview.md) and [Enabling Encryption for User-created Tables](../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/aria-encryption/aria-encryption-overview.md).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">aria-encrypt-tables={0|1}</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`



#### `<code>aria_force_start_after_recovery_failures</code>`


* Description: Number of consecutive log recovery failures after which logs will be automatically deleted to cure the problem; 0 (the default) disables the feature.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--aria-force-start-after-recovery-failures=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value: `<code>0</code>`



#### `<code>aria_group_commit</code>`


* Description: Specifies Aria [group commit mode](aria-group-commit.md).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--aria_group_commit="value"</code>`
* Alias: `<code>maria_group_commit</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>string</code>`
* Valid values:

  * `<code>none</code>` - Group commit is disabled.
  * `<code>hard</code>` - Wait the number of microseconds specified by
 aria_group_commit_interval before actually doing the commit. If the interval
 is 0 then just check if any other threads have requested a commit during the
 time this commit was preparing (just before sync() file) and send their data to
 disk also before sync().
  * `<code>soft</code>` - The service thread will wait the specified time and then sync()
 to the log. If the interval is 0 then it won't wait for any commits (this is
 dangerous and should generally not be used in production)
* Default Value: `<code>none</code>`



#### `<code>aria_group_commit_interval</code>`


* Description: Interval between [Aria group commits](aria-group-commit.md) in microseconds (1/1000000 second) for other threads to come and do a commit in "hard" mode and sync()/commit at all in "soft" mode. Option only has effect if [aria_group_commit](#aria_group_commit) is used.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--aria_group_commit_interval=#</code>`
* Alias: `<code>maria_group_commit_interval</code>`
* Scope: Global
* Dynamic: No
* Type: numeric
* Valid Values:

  * Default Value: `<code>0</code>` (no waiting)
  * Range: `<code>0-4294967295</code>`



#### `<code>aria_log_dir_path</code>`


* Description: Path to the directory where transactional log should be stored
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--aria-log-dir-path=value</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>string</code>`
* Default Value: Same as DATADIR
* Introduced: [MariaDB 10.5.20](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-10-5-20-release-notes.md), [MariaDB 10.6.13](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-10-6-13-release-notes.md), [MariaDB 10.11.3](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-11-series/mariadb-10-11-3-release-notes.md) (as a system variable, existed as an option only before that)



#### `<code>aria_log_file_size</code>`


* Description: Limit for Aria transaction log size
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--aria-log-file-size=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>1073741824</code>`



#### `<code>aria_log_purge_type</code>`


* Description: Specifies how the Aria transactional log will be purged. Set to `<code>at_flush</code>` to keep a copy of the transaction logs (good as an extra backup). The logs will stay until the next [FLUSH LOGS](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/flush-commands/flush-tables-for-export.md);
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--aria-log-purge-type=name</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>enumeration</code>`
* Default Value: `<code>immediate</code>`
* Valid Values: `<code>immediate</code>`, `<code>external</code>`, `<code>at_flush</code>`



#### `<code>aria_max_sort_file_size</code>`


* Description: Don't use the fast sort index method to created index if the temporary file would get bigger than this.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--aria-max-sort-file-size=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>9223372036853727232</code>`
* Range: `<code>0</code>` to `<code>9223372036854775807</code>`



#### `<code>aria_page_checksum</code>`


* Description: Determines whether index and data should use page checksums for extra safety. Can be overridden per table with PAGE_CHECKSUM clause in [CREATE TABLE](../../sql-statements-and-structure/vectors/create-table-with-vectors.md).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--aria-page-checksum=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>ON</code>`



#### `<code>aria_pagecache_age_threshold</code>`


* Description: This characterizes the number of hits a hot block has to be untouched until it is considered aged enough to be downgraded to a warm block. This specifies the percentage ratio of that number of hits to the total number of blocks in the page cache.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--aria-pagecache-age-threshold=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>300</code>`
* Range: `<code>100</code>` to `<code>9999900</code>`



#### `<code>aria_pagecache_buffer_size</code>`


* Description: The size of the buffer used for index and data blocks for Aria tables. This can include explicit Aria tables, system tables, and temporary tables. Increase this to get better handling and measure by looking at [aria-status-variables/#aria_pagecache_reads](aria-status-variables.md#aria_pagecache_reads) (should be small) vs [aria-status-variables/#aria_pagecache_read_requests](aria-status-variables.md#aria_pagecache_read_requests).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--aria-pagecache-buffer-size=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value: `<code>134217720</code>` (128MB)
* Range: `<code>131072</code>` (128KB) upwards



#### `<code>aria_pagecache_division_limit</code>`


* Description: The minimum percentage of warm blocks in the key cache.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--aria-pagecache-division-limit=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>100</code>`
* Range: `<code>1</code>` to `<code>100</code>`



#### `<code>aria_pagecache_file_hash_size</code>`


* Description: Number of hash buckets for open and changed files. If you have many Aria files open you should increase this for faster flushing of changes. A good value is probably 1/10th of the number of possible open Aria files.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--aria-pagecache-file-hash-size=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value: `<code>512</code>`
* Range: `<code>128</code>` to `<code>16384</code>`



#### `<code>aria_recover</code>`


* Description: `<code>aria_recover</code>` has been renamed to `<code>aria_recover_options</code>` in [MariaDB 10.2.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1020-release-notes.md). See [aria_recover_options](#aria_recover_options) for the description.



#### `<code>aria_recover_options</code>`


* Description: Specifies how corrupted tables should be automatically repaired. More than one option can be specified, for example `<code>FORCE,BACKUP</code>`.

  * `<code>NORMAL</code>`: Normal automatic repair, the default until [MariaDB 10.2.3](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1023-release-notes.md)
  * `<code>OFF</code>`: Autorecovery is disabled, the equivalent of not using the option
  * `<code>QUICK</code>`: Does not check rows in the table if there are no delete blocks.
  * `<code>FORCE</code>`: Runs the recovery even if it determines that more than one row from the data file will be lost.
  * `<code>BACKUP</code>`: Keeps a backup of the data files.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--aria-recover-options[=#]</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>enumeration</code>`
* Default Value:

  * `<code>BACKUP,QUICK</code>` (>= [MariaDB 10.2.4](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1024-release-notes.md))
  * `<code>NORMAL</code>` (<= [MariaDB 10.2.3](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1023-release-notes.md))
* Valid Values: `<code>NORMAL</code>`, `<code>BACKUP</code>`, `<code>FORCE</code>`, `<code>QUICK</code>`, `<code>OFF</code>`
* Introduced: [MariaDB 10.2.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1020-release-notes.md)



#### `<code>aria_repair_threads</code>`


* Description: Number of threads to use when repairing Aria tables. The value of 1 disables parallel repair. Increasing from the default will usually result in faster repair, but will use more CPU and memory.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--aria-repair-threads=#</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>1</code>`



#### `<code>aria_sort_buffer_size</code>`


* Description: The buffer that is allocated when sorting the index when doing a [REPAIR](../../sql-statements-and-structure/sql-statements/table-statements/repair-table.md) or when creating indexes with [CREATE INDEX](../../sql-statements-and-structure/sql-statements/data-definition/create/create-index.md) or [ALTER TABLE](../../sql-statements-and-structure/sql-statements/data-definition/alter/alter-tablespace.md).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--aria-sort-buffer-size=#</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>268434432</code>`



#### `<code>aria_stats_method</code>`


* Description: Determines how NULLs are treated for Aria index statistics purposes. If set to `<code>nulls_equal</code>`, all NULL index values are treated as a single group. This is usually fine, but if you have large numbers of NULLs the average group size is slanted higher, and the optimizer may miss using the index for ref accesses when it would be useful. If set to `<code>nulls_unequal</code>`, the default, the opposite approach is taken, with each NULL forming its own group of one. Conversely, the average group size is slanted lower, and the optimizer may use the index for ref accesses when not suitable. Setting to `<code>nulls_ignored</code>` ignores NULLs altogether from index group calculations. Statistics need to be recalculated after this method is changed. See also [Index Statistics](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/optimization-and-indexes/index-statistics.md), [myisam_stats_method](../myisam-storage-engine/myisam-system-variables.md) and [innodb_stats_method](../innodb/innodb-system-variables.md).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--aria-stats-method=#</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>nulls_unequal</code>`
* Valid Values: `<code>nulls_equal</code>`, `<code>nulls_unequal</code>`, `<code>nulls_ignored</code>`



#### `<code>aria_sync_log_dir</code>`


* Description: Controls syncing directory after log file growth and new file creation.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--aria-sync-log-dir=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>enumeration</code>`
* Default Value: `<code>NEWFILE</code>`
* Valid Values: `<code>NEWFILE</code>`, `<code>NEVER</code>`, `<code>ALWAYS</code>`



#### `<code>aria_used_for_temp_tables</code>`


* Description: Readonly variable indicating whether the [Aria](../s3-storage-engine/aria_s3_copy.md) storage engine is used for temporary tables. If set to `<code>ON</code>`, the default, the Aria storage engine is used. If set to `<code>OFF</code>`, MariaDB reverts to using [MyISAM](../myisam-storage-engine/myisam-system-variables.md) for on-disk temporary tables. The [MEMORY](../memory-storage-engine.md) storage engine is used for temporary tables regardless of this variable's setting where appropriate. The default can be changed by not using the `<code>--with-aria-tmp-tables</code>` option when building MariaDB.
* Commandline: No
* Scope: Global
* Dynamic: No
* Data Type: `<code>boolean</code>`
* Default Value: `<code>ON</code>`



#### `<code>deadlock_search_depth_long</code>`


* Description: Long search depth for the [two-step deadlock detection](aria-two-step-deadlock-detection.md). Only used by the [Aria](../s3-storage-engine/aria_s3_copy.md) storage engine.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--deadlock-search-depth-long=#</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>15</code>`
* Range: `<code>0</code>` to `<code>33</code>`



#### `<code>deadlock_search_depth_short</code>`


* Description: Short search depth for the [two-step deadlock detection](aria-two-step-deadlock-detection.md). Only used by the [Aria](../s3-storage-engine/aria_s3_copy.md) storage engine.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--deadlock-search-depth-short=#</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>4</code>`
* Range: `<code>0</code>` to `<code>32</code>`



#### `<code>deadlock_timeout_long</code>`


* Description: Long timeout in microseconds for the [two-step deadlock detection](aria-two-step-deadlock-detection.md). Only used by the [Aria](../s3-storage-engine/aria_s3_copy.md) storage engine.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--deadlock-timeout-long=

# </code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>50000000</code>`
* Range: `<code>0</code>` to `<code>4294967295</code>`



#### `<code>deadlock_timeout_short</code>`


* Description: Short timeout in microseconds for the [two-step deadlock detection](aria-two-step-deadlock-detection.md). Only used by the [Aria](../s3-storage-engine/aria_s3_copy.md) storage engine.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--deadlock-timeout-short=

# </code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>10000</code>`
* Range: `<code>0</code>` to `<code>4294967295</code>`


