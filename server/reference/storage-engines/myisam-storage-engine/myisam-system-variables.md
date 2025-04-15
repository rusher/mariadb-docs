
# MyISAM System Variables

This page documents system variables related to the [MyISAM](myisam-system-variables.md) storage engine. For options, see [MyISAM Options](../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md).


See [Server System Variables](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md) for a complete list of system variables and instructions on setting them.


See also the [Full list of MariaDB options, system and status variables](../../../server-management/variables-and-modes/full-list-of-mariadb-options-system-and-status-variables.md).


#### `<code>key_buffer_size</code>`


* Description: Size of the buffer for the index blocks used by MyISAM tables and shared for all threads. See [Optimizing key_buffer_size](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/optimizing-key_buffer_size.md) for more on selecting the best value.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--key-buffer-size=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>134217728</code>`
* Range: `<code>8</code>` upwards (upper limit determined by operating system per process limit)



#### `<code>key_cache_age_threshold</code>`


* Description: The lower the setting, the more quickly buffers move from the hot key cache sublist to the warm sublist.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--key-cache-age-threshold=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>300</code>`
* Range: `<code>100</code>` to `<code>4294967295</code>`



#### `<code>key_cache_block_size</code>`


* Description: [MyISAM](myisam-system-variables.md) key cache block size in bytes .
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--key-cache-block-size=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>1024</code>`
* Range: `<code>512</code>` to `<code>16384</code>`



#### `<code>key_cache_division_limit</code>`


* Description: Percentage to use for the warm key cache buffer list (the remainder is allocated between the hot and cold caches).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--key-cache-division-limit=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>100</code>`
* Range: `<code>1</code>` to `<code>100</code>`



#### `<code>key_cache_file_hash_size</code>`


* Description: Number of hash buckets for open and changed files. If you have many MyISAM files open you should increase this for faster flushing of changes. A good value is probably 1/10th of the number of possible open MyISAM files.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--key-cache-file-hash-size=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>512</code>`
* Range: `<code>128</code>` to `<code>16384</code>`



#### `<code>key_cache_segments</code>`


* Description: The number of segments in a key cache. See [Segmented Key Cache](../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/benchmarks-and-long-running-tests/benchmarks/segmented-key-cache-performance.md).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--key-cache-segments=#</code>`
* Scope: Global
* Dynamic: Yes
* Type: numeric
* Default Value: `<code class="fixed" style="white-space:pre-wrap">0</code>` (non-segmented)
* Range: `<code>0</code>` to `<code>64</code>`



#### `<code>myisam_block_size</code>`


* Description: Block size to be used for MyISAM index pages.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--myisam-block-size=

# </code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value: `<code>1024</code>`



#### `<code>myisam_data_pointer_size</code>`


* Description: Size in bytes of the default pointer, used in a [MyISAM](myisam-system-variables.md) [CREATE TABLE](../../sql-statements-and-structure/vectors/create-table-with-vectors.md) with no MAX_ROWS option.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--myisam-data-pointer-size=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>6</code>`
* Range: `<code>2</code>` to `<code>7</code>`



#### `<code>myisam_max_extra_sort_file_size</code>`


* Description: Removed in MySQL 5.0.6, was used as a way to force long character keys in large tables to use the key cache method.
* Removed: MySQL 5.0.6



#### `<code>myisam_max_sort_file_size</code>`


* Description: Maximum size in bytes of the temporary file used while recreating a MyISAM index. If the this size is exceeded, the slower process of using the key cache is done instead.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--myisam-max-sort-file-size=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value - 32 bit: `<code>2147483648</code>`
* Default Value - 64 bit: `<code>9223372036854775807</code>`



#### `<code>myisam_mmap_size</code>`


* Description: Maximum memory in bytes that can be used for memory mapping compressed MyISAM files. Too high a value may result in swapping if there are many compressed MyISAM tables.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--myisam-mmap-size=#</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value - 32 bit: `<code>4294967295</code>`
* Default Value - 64 bit: `<code>18446744073709547520</code>`
* Range - 32-bit: `<code>7</code>` to `<code>4294967295</code>`
* Range - 64-bit: `<code>7</code>` to `<code>18446744073709547520</code>`



#### `<code>myisam_recover_options</code>`


* Description: MyISAM recovery mode. Multiple options can be selected, comma-delimited. Using no argument is equivalent to specifying `<code>DEFAULT</code>`, while specifying "" is equivalent to `<code>OFF</code>`. If enabled each time the server opens a MyISAM table, it checks whether it has been marked as crashed, or wasn't closed properly. If so, mysqld will run a check and then attempt to repair the table, writing to the error log beforehand.

  * OFF: No recovery.
  * BACKUP: If the data file is changed while recovering, saves a backup of the .MYD data file. t.MYD will be saved as t.MYD-datetime.BAK.
  * BACKUP_ALL: Same as `<code>BACKUP</code>` but also backs up the .MYI index file. t.MYI will be saved as t.MYI-datetime.BAK.
  * DEFAULT: Recovers without backing up, forcing, or quick checking.
  * FORCE: Runs the recovery even if it determines that more than one row from the data file will be lost.
  * QUICK: Does not check rows in the table if there are no delete blocks.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--myisam-recover-options[=name]</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>enumeration</code>`
* Default Value:

  * `<code>BACKUP,QUICK</code>` (>= [MariaDB 10.2.4](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1024-release-notes.md))
  * `<code>DEFAULT</code>` (<= [MariaDB 10.2.3](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1023-release-notes.md))
  * `<code>OFF</code>`
* Valid Values: `<code>OFF</code>`, `<code>DEFAULT</code>`, `<code>BACKUP</code>`, `<code>BACKUP_ALL</code>`, `<code>FORCE</code>` or `<code>QUICK</code>`



#### `<code>myisam_repair_threads</code>`


* Description: If set to more than `<code>1</code>`, the default, MyISAM table indexes each have their own thread during repair and sorting. Increasing from the default will usually result in faster repair, but will use more CPU and memory.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--myisam-repair-threads=#</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>1</code>`
* Range - 32-bit: `<code>1</code>` to `<code>4294967295</code>`
* Range - 64-bit: `<code>1</code>` to `<code>18446744073709547520</code>`



#### `<code>myisam_sort_buffer_size</code>`


* Description: Size in bytes of the buffer allocated when creating or sorting indexes on a MyISAM table. Increase for better [myisamchk -r, --recover](../../../clients-and-utilities/myisam-clients-and-utilities/myisamchk-table-information.md#repairing-tables) performance.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--myisam-sort-buffer-size=#</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>134217720</code>` (128MB)
* Range: `<code>4096</code>` to `<code>18446744073709547520</code>`



#### `<code>myisam_stats_method</code>`


* Description: Determines how NULLs are treated for [MyISAM](myisam-system-variables.md) index statistics purposes. If set to `<code>nulls_equal</code>`, the default, all NULL index values are treated as a single group. This is usually fine, but if you have large numbers of NULLs the average group size is slanted higher, and the optimizer may miss using the index for ref accesses when it would be useful. If set to `<code>nulls_unequal</code>`, the opposite approach is taken, with each NULL forming its own group of one. Conversely, the average group size is slanted lower, and the optimizer may use the index for ref accesses when not suitable. Setting to `<code>nulls_ignored</code>` ignores NULLs altogether from index group calculations. See also [Index Statistics](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/optimization-and-indexes/index-statistics.md), [aria_stats_method](../aria/aria-system-variables.md), [innodb_stats_method](../innodb/innodb-system-variables.md).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--myisam-stats-method=name</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>enumeration</code>`
* Default Value: `<code>nulls_equal</code>`
* Valid Values: `<code>nulls_equal</code>`, `<code>nulls_unequal</code>`, `<code>nulls_ignored</code>`



#### `<code>myisam_use_mmap</code>`


* Description: If set to `<code>1</code>` (0 is default), memory mapping will be used to reading and writing MyISAM tables.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--myisam-use-mmap</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`


