
# Replication and Binary Log System Variables

The terms *master* and *slave* have historically been used in replication, and MariaDB has begun the process of adding *primary* and *replica* synonyms. The old terms will continue to be used to maintain backward compatibility - see [MDEV-18777](https://jira.mariadb.org/browse/MDEV-18777) to follow progress on this effort.



This page lists system variables that are related to [binary logging](../../../reference/storage-engines/innodb/binary-log-group-commit-and-innodb-flushing-performance.md) and [replication](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/README.md).


See [Server System Variables](../optimization-and-tuning/system-variables/server-system-variables.md) for a complete list of system variables and instructions on setting them, as well as [System variables for global transaction ID](gtid.md#system-variables-for-global-transaction-id).


Also see [mariadbd replication options](../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md#replication-and-binary-logging-options) for related options that are not system variables (such as [binlog_do_db](../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md#-binlog-do-db) and [binlog_ignore_db](../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md#-binlog-ignore-db)).


See also the [Full list of MariaDB options, system and status variables](../../../server-management/variables-and-modes/full-list-of-mariadb-options-system-and-status-variables.md).


#### `<code>auto_increment_increment</code>`


* Description: The increment for all [AUTO_INCREMENT](../../../reference/storage-engines/innodb/auto_increment-handling-in-innodb.md) values on the server, by default `<code>1</code>`. Intended for use in primary-to-primary [replication](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/README.md).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--auto-increment-increment[=#]</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>1</code>`
* Range: `<code>1</code>` to `<code>65535</code>`



#### `<code>auto_increment_offset</code>`


* Description: The offset for all [AUTO_INCREMENT](../../../reference/storage-engines/innodb/auto_increment-handling-in-innodb.md) values on the server, by default `<code>1</code>`. Intended for use in primary-to-primary [replication](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/README.md). Should be not be larger than [auto_increment_increment](#auto_increment_increment). See [AUTO_INCREMENT#Replication](../../../reference/storage-engines/innodb/auto_increment-handling-in-innodb.md#replication).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--auto-increment-offset[=#]</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>1</code>`
* Range: `<code>1</code>` to `<code>65535</code>`



#### `<code>binlog_alter_two_phase</code>`


* Description: When set, split ALTER at binary logging into two statements: START ALTER and COMMIT/ROLLBACK ALTER. The ON setting is recommended for long-running ALTER-table so
it could start on replica before its actual execution on primary.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--binlog-alter-two-phase[={0|1}]</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`
* Introduced: [MariaDB 10.8.1](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-8-series/mariadb-1081-release-notes.md)



#### `<code>binlog_annotate_row_events</code>`


* Description: This option tells the primary to write [annotate_rows_events](../../../clients-and-utilities/mariadb-binlog/annotate_rows_log_event.md) to the binary log.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--binlog-annotate-row-events[={0|1}]</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: boolean
* Default Value:

  * `<code>ON</code>` (>= [MariaDB 10.2.4](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1024-release-notes.md))
  * `<code>OFF</code>` (<= [MariaDB 10.2.3](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1023-release-notes.md))


#### `<code>binlog_cache_size</code>`


* Description: If the [binary log](../../../reference/storage-engines/innodb/binary-log-group-commit-and-innodb-flushing-performance.md) is active, this variable determines the size in bytes, per-connection, of the cache holding a record of binary log changes during a transaction. A separate variable, [binlog_stmt_cache_size](#binlog_stmt_cache_size), sets the upper limit for the statement cache. The [binlog_cache_disk_use](../optimization-and-tuning/system-variables/server-status-variables.md#binlog_cache_disk_use) and [binlog_cache_use](../optimization-and-tuning/system-variables/server-status-variables.md#binlog_cache_use) [server status variables](../optimization-and-tuning/system-variables/server-status-variables.md) will indicate whether this variable needs to be increased (you want a low ratio of binlog_cache_disk_use to binlog_cache_use).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--binlog-cache-size=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>32768</code>`
* Range - 32 bit: `<code>4096</code>` to `<code>4294967295</code>`
* Range - 64 bit: `<code>4096</code>` to `<code>18446744073709547520</code>`



#### `<code>binlog_checksum</code>`


* Description: Specifies the type of BINLOG_CHECKSUM_ALG for log events in the [binary log](../../../reference/storage-engines/innodb/binary-log-group-commit-and-innodb-flushing-performance.md).
* Commandline: 

  * `<code class="fixed" style="white-space:pre-wrap">--binlog-checksum=name</code>`
  * `<code class="fixed" style="white-space:pre-wrap">--binlog-checksum=[0|1]</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>string</code>`
* Default Value:

  * `<code>CRC32</code>` (>= [MariaDB 10.2.1](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1021-release-notes.md))
  * `<code>NONE</code>` (<= [MariaDB 10.2.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1020-release-notes.md))
* Valid Values: `<code>NONE</code>` (`<code>0</code>`), `<code>CRC32</code>` (`<code>1</code>`)



#### `<code>binlog_commit_wait_count</code>`


* Description: Configures the behavior of [group commit for the binary log](../../../server-management/server-monitoring-logs/binary-log/group-commit-for-the-binary-log.md), which can help increase transaction throughput and is used to enable [conservative mode of in-order parallel replication](parallel-replication.md#conservative-mode-of-in-order-parallel-replication).
With [group commit for the binary log](../../../server-management/server-monitoring-logs/binary-log/group-commit-for-the-binary-log.md), the server can delay flushing a committed transaction into [binary log](../../../reference/storage-engines/innodb/binary-log-group-commit-and-innodb-flushing-performance.md) until the given number of transactions are ready to be flushed as a group. The delay will however not be longer
than the value set by [binlog_commit_wait_usec](#binlog_commit_wait_usec).
The default value of 0 means that no delay is introduced.
Setting this value can reduce I/O on the binary log and give an increased opportunity for parallel apply on the replica when [conservative mode of in-order parallel replication](parallel-replication.md#conservative-mode-of-in-order-parallel-replication) is enabled, but too high a value will decrease the transaction throughput. By monitoring the status variable [binlog_group_commit_trigger_count](replication-and-binary-log-status-variables.md#binlog_group_commit_trigger_count) (>=[MariaDB 10.1.5](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-5-release-notes.md)) it is possible to see how often this is occurring.
* Starting with [MariaDB 10.0.18](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-10018-release-notes.md) and [MariaDB 10.1.4](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-4-release-notes.md):
If the server detects that one of the committing transactions T1 holds an
[InnoDB](../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/innodb-upgrade-tests/README.md) row lock that another transaction T2 is waiting for, then the
commit will complete immediately without further delay. This helps avoid
losing throughput when many transactions need conflicting locks. This often
makes it safe to use this option without losing
throughput on a replica with [conservative mode of in-order parallel replication](parallel-replication.md#conservative-mode-of-in-order-parallel-replication), provided the value of
[slave_parallel_threads](#slave_parallel_threads) is sufficiently high.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--binlog-commit-wait-count=#]</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>0</code>`
* Range: `<code>0</code>` to `<code>18446744073709551615</code>`



#### `<code>binlog_commit_wait_usec</code>`


* Description: Configures the behavior of [group commit for the binary log](../../../server-management/server-monitoring-logs/binary-log/group-commit-for-the-binary-log.md), which can help increase transaction throughput and is used to enable [conservative mode of in-order parallel replication](parallel-replication.md#conservative-mode-of-in-order-parallel-replication).
With [group commit for the binary log](../../../server-management/server-monitoring-logs/binary-log/group-commit-for-the-binary-log.md), the server can delay flushing a committed transaction into [binary log](../../../reference/storage-engines/innodb/binary-log-group-commit-and-innodb-flushing-performance.md) until the transaction has waited the configured number of microseconds. By monitoring the status variable [binlog_group_commit_trigger_timeout](replication-and-binary-log-status-variables.md#binlog_group_commit_trigger_timeout) (>=[MariaDB 10.1.5](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-5-release-notes.md)) it is possible to see how often group commits are made due to `<code>binlog_commit_wait_usec</code>`. As soon as the number of pending commits reaches [binlog_commit_wait_count](#binlog_commit_wait_count), the wait will be terminated, though. Thus, this setting only takes effect if `<code>binlog_commit_wait_count</code>` is non-zero.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--binlog-commit-wait-usec#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>100000</code>`
* Range: `<code>0</code>` to `<code>18446744073709551615</code>`



#### `<code>binlog_direct_non_transactional_updates</code>`


* Description: [Replication](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/README.md) inconsistencies can occur due when a transaction updates both transactional and non-transactional tables and the updates to the non-transactional tables are visible before being written to the binary log. This is because, to preserve causality, the non-transactional statements are written to the transaction cache, which is only flushed on commit. Setting binlog_direct_non_transactional_updates to 1 (0 is default) will cause non-transactional tables to be written straight to the binary log, rather than the transaction cache. This setting has no effect when row-based binary logging is used, as it requires statement-based logging. See [binlog_format](#binlog_format). Use with care, and only in situations where no dependencies exist between the non-transactional and transactional tables, for example INSERTing into a non-transactional table based upon the results of a SELECT from a transactional table.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--binlog-direct-non-transactional-updates[=value]</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF (0)</code>`



#### `<code>binlog_do_db</code>`


* Description: This option allows you to configure a [replication primary](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/README.md) to write statements and transactions affecting databases that match a specified name into its [binary log](../../../reference/storage-engines/innodb/binary-log-group-commit-and-innodb-flushing-performance.md). Since the filtered statements or transactions will not be present in the [binary log](../../../reference/storage-engines/innodb/binary-log-group-commit-and-innodb-flushing-performance.md), its replicas will not be able to replicate them.

  * This option will not work with cross-database updates with [statement-based logging](../../../server-management/server-monitoring-logs/binary-log/binary-log-formats.md#statement-based-logging). See the [Statement-Based Logging](replication-filters.md#statement-based-logging) section for more information.
  * Until [MariaDB 11.2.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-2-series/mariadb-11-2-0-release-notes.md), only available as an option, not a system variable. This option can not be set dynamically.
  * When setting it on the command-line or in a server [option group](../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md), the option does not accept a comma-separated list. If you would like to specify multiple filters, then you need to specify the option multiple times.
  * See [Replication Filters](replication-filters.md) for more information.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--binlog-do-db=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>string</code>`
* Default Value: NULL
* Introduced: [MariaDB 11.2.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-2-series/mariadb-11-2-0-release-notes.md) (as a system variable)



#### `<code>binlog_expire_logs_seconds</code>`


* Description: If non-zero, binary logs will be purged after `<code>binlog_expire_logs_seconds</code>` seconds. Possible purges happen at startup and at binary log rotation. From [MariaDB 10.6.1](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-1061-release-notes.md), `<code>binlog_expire_logs_seconds</code>` and [expire_logs_days](#expire_logs_days) are forms of aliases, such that changes to one automatically reflect in the other.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--binlog-expire-logs-seconds=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>0</code>`
* Range: `<code>0</code>` to `<code>8553600</code>`
* Introduced: [MariaDB 10.6.1](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-1061-release-notes.md)



#### `<code>binlog_file_cache_size</code>`


* Description: Size of in-memory cache that is allocated when reading [binary log](../../../reference/storage-engines/innodb/binary-log-group-commit-and-innodb-flushing-performance.md) and [relay log](../../../server-management/server-monitoring-logs/binary-log/relay-log.md) files.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--binlog-file-cache-size=#</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>16384</code>`
* Range: `<code>8192</code>` to `<code>18446744073709551615</code>`
* Introduced: [MariaDB 10.3.3](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1033-release-notes.md)



#### `<code>binlog_format</code>`


* Description: Determines whether [replication](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/README.md) is row-based, statement-based or mixed. Statement-based was the default until [MariaDB 10.2.3](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1023-release-notes.md). Be careful of changing the binary log format when a replication environment is already running. See [Binary Log Formats](../../../server-management/server-monitoring-logs/binary-log/binary-log-formats.md). Starting from [MariaDB 10.0.22](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-10022-release-notes.md) a replica will apply any events it gets from the primary, regardless of the binary log format. `<code>binlog_format</code>` only applies to normal (not replicated) updates.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--binlog-format=format</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>enumeration</code>`
* Default Value:

  * `<code>MIXED</code>` (>= [MariaDB 10.2.4](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1024-release-notes.md))
  * `<code>STATEMENT</code>` (<= [MariaDB 10.2.3](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1023-release-notes.md))
* Valid Values: `<code>ROW</code>`, `<code>STATEMENT</code>` or `<code>MIXED</code>`



#### `<code>binlog_gtid_index</code>`


* Description: Enable the creation of a GTID index for every binlog file, and the use of such index for speeding up GTID lookup in the binlog. See [Binlog indexing](gtid.md#binlog-indexing).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--binlog-gtid-index{=0|1}</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>ON</code>`
* Introduced: [MariaDB 11.4](../../../../release-notes/mariadb-community-server/what-is-mariadb-114.md)



#### `<code>binlog_gtid_index_page_size</code>`


* Description: Page size to use for the binlog GTID index. See [Binlog indexing](gtid.md#binlog-indexing).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--binlog-gtid-index-page-size=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>4096</code>`
* Range: `<code>64</code>` to `<code>16777216</code>`
* Introduced: [MariaDB 11.4](../../../../release-notes/mariadb-community-server/what-is-mariadb-114.md)



#### `<code>binlog_gtid_index_span_min</code>`


* Description: Control sparseness of the binlog GTID index. If set to N, at most one index record will be added for every N bytes of binlog file written, to reduce the size of the index. Normally does not need tuning. See [Binlog indexing](gtid.md#binlog-indexing).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--binlog-gtid-index-span-min=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>65536</code>`
* Range: `<code>1</code>` to `<code>1073741824</code>`
* Introduced: [MariaDB 11.4](../../../../release-notes/mariadb-community-server/what-is-mariadb-114.md)



#### `<code>binlog_ignore_db</code>`


* Description: This option allows you to configure a [replication primary](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/README.md) to not write statements and transactions affecting databases that match a specified name into its [binary log](../../../reference/storage-engines/innodb/binary-log-group-commit-and-innodb-flushing-performance.md). Since the filtered statements or transactions will not be present in the [binary log](../../../reference/storage-engines/innodb/binary-log-group-commit-and-innodb-flushing-performance.md), its replicas will not be able to replicate them.

  * This option will not work with cross-database updates with [statement-based logging](../../../server-management/server-monitoring-logs/binary-log/binary-log-formats.md#statement-based-logging). See the [Statement-Based Logging](replication-filters.md#statement-based-logging) section for more information.
  * Until [MariaDB 11.2.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-2-series/mariadb-11-2-0-release-notes.md), only available as an option, not a system variable. This option can not be set dynamically.
  * When setting it on the command-line or in a server [option group](../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md), the option does not accept a comma-separated list. If you would like to specify multiple filters, then you need to specify the option multiple times.
  * See [Replication Filters](replication-filters.md) for more information.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--binlog-ignore-db=name</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>string</code>`
* Default Value: NULL
* Introduced: [MariaDB 11.2.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-2-series/mariadb-11-2-0-release-notes.md)



#### `<code>binlog_large_commit_threshold</code>`


* Description: Increases transaction concurrency for large transactions (i.e. those with sizes larger than this value) by using the large transaction's cache file as a new binary log, and rotating the active binary log to the large transaction's cache file at commit time. This avoids the default commit logic that copies the transaction cache data to the end of the active binary log file while holding a lock that prevents other transactions from binlogging.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--binlog-large-commit-threshold=val</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>bigint unsigned</code>`
* Default Value: `<code>134217728</code>`
* Range: `<code>10485760</code>` to `<code>18446744073709551615</code>`
* Introduced: [MariaDB 11.7](../../../../release-notes/mariadb-community-server/what-is-mariadb-117.md)



#### `<code>binlog_legacy_event_pos</code>`


* Description: Fill in the end_log_pos field of _all_ events in the binlog, even when doing so costs performance. Can be used in case some old application needs it for backwards compatibility. Setting this option can hurt binlog scalability.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--binlog-legacy-event-pos{=0|1}</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`
* Introduced: [MariaDB 11.4](../../../../release-notes/mariadb-community-server/what-is-mariadb-114.md)



#### `<code>binlog_optimize_thread_scheduling</code>`


* Description: Run fast part of group commit in a single thread, to optimize kernel thread scheduling. On by default. Disable to run each transaction in group commit in its own thread, which can be slower at very high concurrency. This option is mostly for testing one algorithm versus another, and it should not normally be necessary to change it. Deprecated in [MariaDB 11.7](../../../../release-notes/mariadb-community-server/what-is-mariadb-117.md), as the option was initially added to provide a safe alternative for the newly added binlog group commit logic, such that when 0, it would disable a leader thread
from performing the binlog write for all transactions that are a part of the group commit. Problems related to the binlog group commit optimization are expected to be addressed by now, so the option has been deprecated and will be removed in future.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--binlog-optimize-thread-scheduling</code>` or `<code class="fixed" style="white-space:pre-wrap">--skip-binlog-optimize-thread-scheduling</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>boolean</code>`
* Default Value: `<code>ON</code>`
* Deprecated: [MariaDB 11.7](../../../../release-notes/mariadb-community-server/what-is-mariadb-117.md)



#### `<code>binlog_row_event_max_size</code>`


* Description: The maximum size of a row-based [binary log](../../../reference/storage-engines/innodb/binary-log-group-commit-and-innodb-flushing-performance.md) event in bytes. Rows will be grouped into events smaller than this size if possible. The value has to be a multiple of 256. Until [MariaDB 11.2.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-2-series/mariadb-11-2-0-release-notes.md), only available as an option, not a system variable.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--binlog-row-event-max-size=val</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>8192</code>`
* Range: `<code>256</code>` to `<code>4294967040</code>` (in multiples of 256)
* Introduced: [MariaDB 11.2.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-2-series/mariadb-11-2-0-release-notes.md)



#### `<code>binlog_row_image</code>`


* Description: Controls the logging format in [row-based](../../../server-management/server-monitoring-logs/binary-log/binary-log-formats.md#row-based) [replication](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/README.md). In row-based replication (the variable has no effect with [statement-based replication](../../../server-management/server-monitoring-logs/binary-log/binary-log-formats.md#statement-based)), each row change event contains an image for matching against when choosing the row to be updated, and another image containing the changes. Before the introduction of this variable, all columns were logged for both of these images. In certain circumstances, this is not necessary, and memory, disk and network resources can be saved by partial logging. Note that to safely change this setting from the default, the table being replicated to must contain identical primary key definitions, and columns must be present, in the same order, and use the same data types as the original table. If these conditions are not met, matches may not be correctly determined and updates and deletes may diverge on the replica, with no warnings or errors returned.

  * `<code>FULL</code>`: All columns in the before and after image are logged. This is the default, and the only behavior in earlier versions.
  * `<code>NOBLOB</code>`: mariadbd avoids logging blob and text columns whenever possible (eg, blob column was not changed or is not part of primary key).
  * `<code>MINIMAL</code>`: A PK equivalent (PK columns or full row if there is no PK in the table) is logged in the before image, and only changed columns are logged in the after image.
  * `<code>FULL_NODUP</code>`: All columns are logged in the before image, but only changed columns or all columns of inserted record are logged in the after image. This is essentially the same as `<code>FULL</code>`, but takes less space. From [MariaDB 11.4](../../../../release-notes/mariadb-community-server/what-is-mariadb-114.md).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--binlog-row-image=value</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>enum</code>`
* Default Value: `<code>FULL</code>`
* Valid Values:

  * <= [MariaDB 11.3](../../../../release-notes/mariadb-community-server/what-is-mariadb-113.md): `<code>FULL</code>`, `<code>NOBLOB</code>` or `<code>MINIMAL</code>`
  * >= [MariaDB 11.4](../../../../release-notes/mariadb-community-server/what-is-mariadb-114.md): `<code>FULL</code>`, `<code>NOBLOB</code>`, `<code>MINIMAL</code>` or `<code>FULL_NODUP</code>`



#### `<code>binlog_row_metadata</code>`


* Description: Controls the format used for binlog metadata logging.

  * `<code>NO_LOG</code>`: No metadata is logged (default).
  * `<code>MINIMAL</code>`: Only metadata required by a replica is logged.
  * `<code>FULL</code>`: All metadata is logged.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--binlog-row-metadata=value</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>enum</code>`
* Default Value: `<code>NO_LOG</code>`
* Valid Values: `<code>NO_LOG</code>`, `<code>MINIMAL</code>`, `<code>FULL</code>`
* Introduced: [MariaDB 10.5.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1050-release-notes.md)



#### `<code>binlog_space_limit</code>`


* Description: Alias for [max_binlog_total_size](replication-and-binary-log-system-variables.md#max_binlog_total_size).
* Introduced: [MariaDB 11.4](../../../../release-notes/mariadb-community-server/what-is-mariadb-114.md)



#### `<code>binlog_stmt_cache_size</code>`


* Description: If the [binary log](../../../reference/storage-engines/innodb/binary-log-group-commit-and-innodb-flushing-performance.md) is active, this variable determines the size in bytes of the cache holding a record of binary log changes outside of a transaction. The variable [binlog_cache_size](#binlog_cache_size), determines the cache size for binary log statements inside a transaction. The [binlog_stmt_cache_disk_use](../optimization-and-tuning/system-variables/server-status-variables.md#binlog_stmt_cache_disk_use) and [binlog_stmt_cache_use](../optimization-and-tuning/system-variables/server-status-variables.md#binlog_stmt_cache_use) [server status variables](../optimization-and-tuning/system-variables/server-status-variables.md) will indicate whether this variable needs to be increased (you want a low ratio of binlog_stmt_cache_disk_use to binlog_stmt_cache_use).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--binlog-stmt-cache-size=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>32768</code>`
* Range - 32 bit: `<code>4096</code>` to `<code>4294967295</code>`
* Range - 64 bit: `<code>4096</code>` to `<code>18446744073709547520</code>`



#### `<code>default_master_connection</code>`


* Description: In [multi-source replication](multi-source-replication.md), specifies which connection will be used for commands and variables if you don't specify a connection.
* Commandline: None
* Scope: Session
* Dynamic: Yes
* Data Type: `<code>string</code>`
* Default Value: `<code>''</code>` (empty string)



#### `<code>encrypt_binlog</code>`


* Description: Encrypt [binary logs](../../../reference/storage-engines/innodb/binary-log-group-commit-and-innodb-flushing-performance.md) (including [relay logs](../../../server-management/server-monitoring-logs/binary-log/relay-log.md)). See [Data at Rest Encryption](../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/data-at-rest-encryption-overview.md) and [Encrypting Binary Logs](../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/encrypting-binary-logs.md).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--encrypt-binlog[={0|1}]</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`



#### `<code>expire_logs_days</code>`


* Description: Number of days after which the [binary log](../../../reference/storage-engines/innodb/binary-log-group-commit-and-innodb-flushing-performance.md) can be automatically removed. By default 0, or no automatic removal. When using [replication](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/README.md), should always be set higher than the maximum lag by any replica. Removals take place when the server starts up, when the binary log is flushed, when the next binary log is created after the previous one reaches the maximum size, or when running [PURGE BINARY LOGS](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/purge-binary-logs.md). Units are whole days (integer) until [MariaDB 10.6.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-1060-release-notes.md), or 1/1000000 precision (double) from [MariaDB 10.6.1](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-1061-release-notes.md).Starting from [MariaDB 10.6.1](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-1061-release-notes.md), `<code>expire_logs_days</code>` and [binlog_expire_logs_seconds](#binlog_expire_logs_seconds) are forms of aliases, such that changes to one automatically reflect in the other.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--expire-logs-days=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>0.000000</code>` (>= [MariaDB 10.6.1](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-1061-release-notes.md)), `<code>0</code>` (<= [MariaDB 10.6.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-1060-release-notes.md))
* Range: `<code>0</code>` to `<code>99</code>`



#### `<code>init_slave</code>`


* Description: Similar to [init_connect](../optimization-and-tuning/system-variables/server-system-variables.md#init_connect), but the string contains one or more SQL statements, separated by semicolons, that will be executed by a replica server each time the SQL thread starts. These statements are only executed after the acknowledgement is sent to the replica and [START SLAVE](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/start-replica.md) completes.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--init-slave=name</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>string</code>`
* Related variables: `<code> [init_connect](../optimization-and-tuning/system-variables/server-system-variables.md#init_connect)</code>`



#### `<code>log_bin</code>`


* Description: Whether [binary logging](../../../reference/storage-engines/innodb/binary-log-group-commit-and-innodb-flushing-performance.md) is enabled or not. If the --log-bin [option](../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md) is used, log_bin will be set to ON, otherwise it will be OFF. If no `<code>name</code>` option is given for `<code>--log-bin</code>`, `<code>datadir/'log-basename'-bin</code>` or `<code>'datadir'/mysql-bin</code>` will be used (the latter if [--log-basename](../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md#-log-basename) is not specified). We strongly recommend you use either `<code class="fixed" style="white-space:pre-wrap">--log-basename</code>` or specify a filename to ensure that [replication](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/README.md) doesn't stop if the real hostname of the computer changes. The name option can optionally include an absolute path. If no path is specified, the log will be written to the [data directory](../optimization-and-tuning/system-variables/server-system-variables.md#datadir). The name can optionally include the file extension; it will be stripped and only the file basename will be used.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--log-bin[=name]</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`
* Related variables: `<code>[sql_log_bin](replication-and-binary-log-system-variables.md#sql_log_bin)</code>`



#### `<code>log_bin_basename</code>`


* Description: The full path of the binary log file names, excluding the extension. Its value is derived from the rules specified in `<code>log_bin</code>` system variable. This is a read-only variable only, there is no corresponding configuration file setting or command line option by the same name, use `<code>log_bin</code>` to set the basename path instead.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">No commandline option</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>string</code>`
* Default Value: None
* Dynamic: `<code>No</code>`



#### `<code>log_bin_compress</code>`


* Description: Whether or not the binary log can be compressed. `<code>0</code>` (the default) means no compression. See [Compressing Events to Reduce Size of the Binary Log](../../../server-management/server-monitoring-logs/binary-log/compressing-events-to-reduce-size-of-the-binary-log.md).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--log-bin-compress</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`



#### `<code>log_bin_compress_min_len</code>`


* Description: Minimum length of sql statement (in statement mode) or record (in row mode) that can be compressed. See [Compressing Events to Reduce Size of the Binary Log](../../../server-management/server-monitoring-logs/binary-log/compressing-events-to-reduce-size-of-the-binary-log.md).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--log-bin-compress-min-len</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>256</code>`
* Range: `<code>10</code>` to `<code>1024</code>`



#### `<code>log_bin_index</code>`


* Description: File that holds the names for last binlog files. If [--log-basename](../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md#-log-basename) is also set, `<code>log_bin_index</code>` should be placed after in the config files. Later settings override earlier settings, so `<code>log-basename</code>` will override any earlier log file name settings.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--log-bin-index=name</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>string</code>`
* Default Value: None



#### `<code>log_bin_trust_function_creators</code>`


* Description: Functions and triggers can be dangerous when used with [replication](README.md). Certain types of functions and triggers may have unintended consequences when the statements are applied on a replica. For that reason, there are some restrictions on the creation of functions and triggers when the [binary log](../../../reference/storage-engines/innodb/binary-log-group-commit-and-innodb-flushing-performance.md) is enabled by default, such as:

  * When `<code>log_bin_trust_function_creators</code>` is `<code>OFF</code>` and `<code>[log_bin](#log_bin)</code>` is `<code>ON</code>`, `<code>[CREATE FUNCTION](../../../reference/sql-statements-and-structure/sql-statements/data-definition/create/create-function.md)</code>` and `<code>[ALTER FUNCTION](../../../reference/sql-statements-and-structure/sql-statements/data-definition/alter/alter-function.md)</code>` statements will trigger an error if the function is defined with any of the `<code>NOT DETERMINISTIC</code>`, `<code>CONTAINS SQL</code>` or `<code>MODIFIES SQL DATA</code>` characteristics.
  * This means that when `<code>log_bin_trust_function_creators</code>` is `<code>OFF</code>` and `<code>[log_bin](#log_bin)</code>` is `<code>ON</code>`, `<code>[CREATE FUNCTION](../../../reference/sql-statements-and-structure/sql-statements/data-definition/create/create-function.md)</code>` and `<code>[ALTER FUNCTION](../../../reference/sql-statements-and-structure/sql-statements/data-definition/alter/alter-function.md)</code>` statements will only succeed if the function is defined with any of the `<code>DETERMINISTIC</code>`, `<code>NO SQL</code>`, or `<code>READS SQL DATA</code>` characteristics.
  * When `<code>log_bin_trust_function_creators</code>` is `<code>OFF</code>` and `<code>[log_bin](#log_bin)</code>` is `<code>ON</code>`, the `<code>[SUPER](../../../reference/sql-statements-and-structure/sql-statements/account-management-sql-commands/grant.md#global-privileges)</code>` privilege is also required to execute the following statements:

    * `<code>[CREATE FUNCTION](../../../reference/sql-statements-and-structure/sql-statements/data-definition/create/create-function.md)</code>`
    * `<code>[CREATE TRIGGER](../../programming-customizing-mariadb/triggers-events/triggers/create-trigger.md)</code>`
    * `<code>[DROP TRIGGER](../../../reference/sql-statements-and-structure/sql-statements/data-definition/drop/drop-trigger.md)</code>`
  * Setting `<code>log_bin_trust_function_creators</code>` to `<code>ON</code>` removes these requirements around functions characteristics and the `<code>[SUPER](../../../reference/sql-statements-and-structure/sql-statements/account-management-sql-commands/grant.md#global-privileges)</code>` privileges.
  * See [Binary Logging of Stored Routines](../../programming-customizing-mariadb/stored-routines/binary-logging-of-stored-routines.md) for more information.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--log-bin-trust-function-creators[={0|1}]</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`



#### `<code>log_slow_slave_statements</code>`


* Description: Log slow statements executed by replica thread to the [slow log](../../../server-management/server-monitoring-logs/slow-query-log/slow-query-log-overview.md) if it is open. Before [MariaDB 10.1.13](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10113-release-notes.md), this was only available as a mariadbd option, not a server variable.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--log-slow-slave-statements</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value:

  * `<code>ON </code>` (>= [MariaDB 10.2.4](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1024-release-notes.md))
  * `<code>OFF</code>` (<= [MariaDB 10.2.3](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1023-release-notes.md))



#### `<code>log_slave_updates</code>`


* Description: If set to `<code>0</code>`, the default, updates on a replica received from a primary during [replication](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/README.md) are not logged in the replica's binary log. If set to `<code>1</code>`, they are. The replica's binary log needs to be enabled for this to have an effect. Set to `<code>1</code>` if you want to daisy-chain the replicas.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--log-slave-updates</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`



#### `<code>master_verify_checksum</code>`


* Description: Verify [binlog checksums](binlog-event-checksums.md) when reading events from the binlog on the primary.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--master-verify-checksum=[0|1]</code>`
* Scope: Global
* Access Type: Can be changed dynamically
* Data Type: `<code>bool</code>`
* Default Value: `<code>OFF (0)</code>`



#### `<code>max_binlog_cache_size</code>`


* Description: Restricts the size in bytes used to cache a multi-transactional query. If more bytes are required, a `<code>Multi-statement transaction required more than 'max_binlog_cache_size' bytes of storage</code>` error is generated. If the value is changed, current sessions are unaffected, only sessions started subsequently. See [max_binlog_stmt_cache_size](#max_binlog_stmt_cache_size) and [binlog_cache_size](#binlog_cache_size).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--max-binlog-cache-size=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>18446744073709547520</code>`
* Range: `<code>4096</code>` to `<code>18446744073709547520</code>`



#### `<code>max_binlog_size</code>`


* Description: If the [binary log](../../../reference/storage-engines/innodb/binary-log-group-commit-and-innodb-flushing-performance.md) exceeds this size in bytes after a write, the server rotates it by closing it and opening a new binary log. Single transactions will always be stored in the same binary log, so the server will wait for open transactions to complete before rotating. This figure also applies to the size of [relay logs](../../../server-management/server-monitoring-logs/binary-log/relay-log.md) if [max_relay_log_size](#max_relay_log_size) is set to zero.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--max-binlog-size=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>1073741824</code>` (1GB)
* Range: `<code>4096</code>` to `<code>1073741824</code>` (4KB to 1GB)



#### `<code>max_binlog_stmt_cache_size</code>`


* Description: Restricts the size used to cache non-transactional statements. See [max_binlog_cache_size](#max_binlog_cache_size) and [binlog_stmt_cache_size](#binlog_stmt_cache_size).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--max-binlog-stmt-cache-size=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>18446744073709547520</code>` (64 bit), `<code>4294963200</code>` (32 bit)
* Range: `<code>4096</code>` to `<code>18446744073709547520</code>`



#### `<code>max_binlog_total_size</code>`


* Description: Maximum space in bytes to use for all [binary logs](../../../reference/storage-engines/innodb/binary-log-group-commit-and-innodb-flushing-performance.md). Extra logs are deleted on server start, log rotation, FLUSH LOGS or when writing to binlog. Default is 0, which means no size restrictions. See also [slave_connections_needed_for_purge](#slave_connections_needed_for_purge).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--max-binlog-size=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>0</code>`
* Range: `<code>0</code>` to `<code>18446744073709551615</code>`
* Introduced: [MariaDB 11.4](../../../../release-notes/mariadb-community-server/what-is-mariadb-114.md)



#### `<code>max_relay_log_size</code>`


* Description: Replica will rotate its [relay log](../../../server-management/server-monitoring-logs/binary-log/relay-log.md) if it exceeds this size after a write. If set to 0, the [max_binlog_size](#max_binlog_size) setting is used instead. Previously global only, since the implementation of [multi-source replication](multi-source-replication.md), it can be set per session as well.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--max-relay-log-size=#</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>0</code>`
* Range: `<code>0</code>`, or `<code>4096 to 1073741824</code>` (4KB to 1GB)



#### `<code>read_binlog_speed_limit</code>`


* Description: Used to restrict the speed at which a [replica](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/README.md) can read the binlog from the primary. This can be used to reduce the load on a primary if many replicas need to download large amounts of old binlog files at the same time. The network traffic will be restricted to the specified number of kilobytes per second.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--read-binlog-speed-limit=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>0</code>` (no limit)
* Range: `<code>0</code>` to `<code>18446744073709551615</code>`



#### `<code>relay_log</code>`


* Description: [Relay log](../../../server-management/server-monitoring-logs/binary-log/relay-log.md) basename. If not set, the basename of the files will be `<code>hostname-relay-bin</code>`, or derived from [--log-basename](../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md#-log-basename). If [--log-basename](../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md#-log-basename) is also set, `<code>relay_log</code>` should be placed after in the config files. Later settings override earlier settings, so `<code>log-basename</code>` will override any earlier log file name settings.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--relay-log=file_name</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>filename</code>`
* Default Value: `<code>''</code>` (none)



#### `<code>relay_log_basename</code>`


* Description: The full path of the relay log file names, excluding the extension. Its value is derived from the [relay-log](#relay_log) variable value.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">No commandline option</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>string</code>`
* Default Value: None
* Dynamic: `<code>No</code>`



#### `<code>relay_log_index</code>`


* Description: Name and location of the [relay log](../../../server-management/server-monitoring-logs/binary-log/relay-log.md) index file, the file that keeps a list of the last relay logs. Defaults to hostname-relay-bin.index, or derived from [--log-basename](../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md#-log-basename). If [--log-basename](../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md#-log-basename) is also set, `<code>relay_log_index</code>` should be placed after in the config files. Later settings override earlier settings, so `<code>log-basename</code>` will override any earlier log file name settings.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--relay-log-index=name</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>string</code>`
* Default Value: None



#### `<code>relay_log_info_file</code>`


* Description: Name and location of the file where the `<code>RELAY_LOG_FILE</code>` and `<code>RELAY_LOG_POS</code>` options (i.e. the [relay log](../../../server-management/server-monitoring-logs/binary-log/relay-log.md) position) for the [CHANGE MASTER](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md) statement are written. The [replica's SQL thread](replication-threads.md#slave-sql-thread) keeps this [relay log](../../../server-management/server-monitoring-logs/binary-log/relay-log.md) position updated as it applies events.

  * See [CHANGE MASTER TO: Option Persistence](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md#option-persistence) for more information.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--relay-log-info-file=file_name</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>string</code>`
* Default Value: `<code>relay-log.info</code>`



#### `<code>relay_log_purge</code>`


* Description: If set to `<code>1</code>` (the default), [relay logs](../../../server-management/server-monitoring-logs/binary-log/relay-log.md) will be purged as soon as they are no longer necessary.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--relay-log-purge={0|1}</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>ON</code>`
* Note: In MySQL and in MariaDB before version 10.0.8 this variable was silently changed if you did [CHANGE MASTER](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md).



#### `<code>relay_log_recovery</code>`


* Description: If set to `<code>1</code>` (`<code>0</code>` is default), on startup the replica will drop all [relay logs](../../../server-management/server-monitoring-logs/binary-log/relay-log.md) that haven't yet been processed, and retrieve relay logs from the primary. Can be useful after the replica has crashed to prevent the processing of corrupt relay logs. relay_log_recovery should always be set together with [relay_log_purge](#relay_log_purge). Setting `<code class="fixed" style="white-space:pre-wrap">relay-log-recovery=1</code>` with `<code class="fixed" style="white-space:pre-wrap">relay-log-purge=0</code>` can cause the relay log to be read from files that were not purged, leading to data inconsistencies.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--relay-log-recovery</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`



#### `<code>relay_log_space_limit</code>`


* Description: Specifies the maximum space to be used for the [relay logs](../../../server-management/server-monitoring-logs/binary-log/relay-log.md). The IO thread will stop until the SQL thread has cleared the backlog. By default `<code>0</code>`, or no limit.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--relay-log-space-limit=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value: `<code>0</code>`
* Range - 32 bit: `<code>0</code>` to `<code>4294967295</code>`
* Range - 64 bit: `<code>0</code>` to `<code>18446744073709547520</code>`



#### `<code>replicate_annotate_row_events</code>`


* Description: Tells the replica to reproduce [annotate_rows_events](../../../clients-and-utilities/mariadb-binlog/annotate_rows_log_event.md) received from the primary in its own binary log. This option is sensible only when used in tandem with the [log_slave_updates](#log_slave_updates) option.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--replicate-annotate-row-events</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>boolean</code>`
* Default Value:

  * `<code>ON</code>` (>= [MariaDB 10.2.4](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1024-release-notes.md))
  * `<code>OFF</code>` (<= [MariaDB 10.2.3](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1023-release-notes.md))



#### `<code>replicate_do_db</code>`


* Description: This system variable allows you to configure a [replica](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/README.md) to apply statements and transactions affecting databases that match a specified name.

  * This system variable will not work with cross-database updates with [statement-based logging](../../../server-management/server-monitoring-logs/binary-log/binary-log-formats.md#statement-based-logging). See the [Statement-Based Logging](replication-filters.md#statement-based-logging) section for more information.
  * When setting it dynamically with `<code>[SET GLOBAL](../../../../connectors/mariadb-connector-cpp/setup-for-connector-cpp-examples.md#global-session)</code>`, the system variable accepts a comma-separated list of filters.
  * When setting it on the command-line or in a server [option group](../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md), the system variable does not accept a comma-separated list. If you would like to specify multiple filters, then you need to specify the system variable multiple times.
  * See [Replication Filters](replication-filters.md) for more information.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--replicate-do-db=name</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>string</code>`
* Default Value: `<code>''</code>` (empty)



#### `<code>replicate_do_table</code>`


* Description: This system variable allows you to configure a [replica](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/README.md) to apply statements and transactions that affect tables that match a specified name. The table name is specified in the format: `<code>dbname.tablename</code>`.

  * This system variable will not work with cross-database updates with [statement-based logging](../../../server-management/server-monitoring-logs/binary-log/binary-log-formats.md#statement-based-logging). See the [Statement-Based Logging](replication-filters.md#statement-based-logging) section for more information.
  * When setting it dynamically with `<code>[SET GLOBAL](../../../../connectors/mariadb-connector-cpp/setup-for-connector-cpp-examples.md#global-session)</code>`, the system variable accepts a comma-separated list of filters.
  * When setting it on the command-line or in a server [option group](../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md), the system variable does not accept a comma-separated list. If you would like to specify multiple filters, then you need to specify the system variable multiple times.
  * See [Replication Filters](replication-filters.md) for more information.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--replicate-do-table=name</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>string</code>`
* Default Value: `<code>''</code>` (empty)



#### `<code>replicate_events_marked_for_skip</code>`


* Description: Tells the replica whether to [replicate](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/README.md) events that are marked with the `<code>@@skip_replication</code>` flag. See [Selectively skipping replication of binlog events](selectively-skipping-replication-of-binlog-events.md) for more information.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--replicate-events-marked-for-skip</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>enumeration</code>`
* Default Value: `<code>replicate</code>`
* Valid Values: `<code>REPLICATE</code>`, `<code>FILTER_ON_SLAVE</code>`, `<code>FILTER_ON_MASTER</code>`



#### `<code>replicate_ignore_db</code>`


* Description: This system variable allows you to configure a [replica](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/README.md) to ignore statements and transactions affecting databases that match a specified name.

  * This system variable will not work with cross-database updates with [statement-based logging](../../../server-management/server-monitoring-logs/binary-log/binary-log-formats.md#statement-based-logging). See the [Statement-Based Logging](replication-filters.md#statement-based-logging) section for more information.
  * When setting it dynamically with `<code>[SET GLOBAL](../../../../connectors/mariadb-connector-cpp/setup-for-connector-cpp-examples.md#global-session)</code>`, the system variable accepts a comma-separated list of filters.
  * When setting it on the command-line or in a server [option group](../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md), the system variable does not accept a comma-separated list. If you would like to specify multiple filters, then you need to specify the system variable multiple times.
  * See [Replication Filters](replication-filters.md) for more information.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--replicate-ignore-db=name</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>string</code>`
* Default Value: `<code>''</code>` (empty)



#### `<code>replicate_ignore_table</code>`


* Description: This system variable allows you to configure a [replica](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/README.md) to ignore statements and transactions that affect tables that match a specified name. The table name is specified in the format: `<code>dbname.tablename</code>`.

  * This system variable will not work with cross-database updates with [statement-based logging](../../../server-management/server-monitoring-logs/binary-log/binary-log-formats.md#statement-based-logging). See the [Statement-Based Logging](replication-filters.md#statement-based-logging) section for more information.
  * When setting it dynamically with `<code>[SET GLOBAL](../../../../connectors/mariadb-connector-cpp/setup-for-connector-cpp-examples.md#global-session)</code>`, the system variable accepts a comma-separated list of filters.
  * When setting it on the command-line or in a server [option group](../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md), the system variable does not accept a comma-separated list. If you would like to specify multiple filters, then you need to specify the system variable multiple times.
  * See [Replication Filters](replication-filters.md) for more information.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--replicate-ignore-table=name</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>string</code>`
* Default Value: `<code>''</code>` (empty)



#### `<code>replicate_rewrite_db</code>`


* Description: This option allows you to configure a [replica](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/README.md) to rewrite database names. It uses the format `<code>primary_database->replica_database</code>`. If a replica encounters a [binary log](../../../reference/storage-engines/innodb/binary-log-group-commit-and-innodb-flushing-performance.md) event in which the default database (i.e. the one selected by the `<code>[USE](../../../../general-resources/learning-and-training/training-and-tutorials/beginner-mariadb-articles/useful-mariadb-queries.md)</code>` statement) is `<code>primary_database</code>`, then the replica will apply the event in `<code>replica_database</code>` instead.

  * This option will not work with cross-database updates with [statement-based logging](../../../server-management/server-monitoring-logs/binary-log/binary-log-formats.md#statement-based-logging). See the [Statement-Based Logging](replication-filters.md#statement-based-logging) section for more information.
  * This option only affects statements that involve tables. This option does not affect statements involving the database itself, such as [CREATE DATABASE](../../../reference/sql-statements-and-structure/sql-statements/data-definition/create/create-database.md), [ALTER DATABASE](../../../reference/sql-statements-and-structure/sql-statements/data-definition/alter/alter-database.md), and [DROP DATABASE](../../../reference/sql-statements-and-structure/sql-statements/data-definition/drop/drop-database.md).
  * When setting it on the command-line or in a server [option group](../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md), the option does not accept a comma-separated list. If you would like to specify multiple filters, then you need to specify the option multiple times.
  * See [Replication Filters](replication-filters.md) for more information.
  * Before [MariaDB 10.11](../../../../release-notes/mariadb-community-server/what-is-mariadb-1011.md), `<code>replicate_rewrite_db</code>` was not available as a system variable, only as a mariadbd option, and could not be set dynamically. From [MariaDB 10.11](../../../../release-notes/mariadb-community-server/what-is-mariadb-1011.md) it is available as a dynamic system variable
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--replicate-rewrite-db=primary_database->replica_database</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>string</code>`
* Default Value: `<code>''</code>` (empty)
* Introduced: [MariaDB 10.11.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-11-series/mariadb-10-11-0-release-notes.md)



#### `<code>replicate_wild_do_table</code>`


* Description: This system variable allows you to configure a [replica](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/README.md) to apply statements and transactions that affect tables that match a specified wildcard pattern. The wildcard pattern uses the same semantics as the `<code>[LIKE](../../../reference/sql-statements-and-structure/sql-statements/built-in-functions/string-functions/like.md)</code>` operator.

  * This system variable will work with cross-database updates with [statement-based logging](../../../server-management/server-monitoring-logs/binary-log/binary-log-formats.md#statement-based-logging). See the [Statement-Based Logging](replication-filters.md#statement-based-logging) section for more information.
  * When setting it dynamically with `<code>[SET GLOBAL](../../../../connectors/mariadb-connector-cpp/setup-for-connector-cpp-examples.md#global-session)</code>`, the system variable accepts a comma-separated list of filters.
  * When setting it on the command-line or in a server [option group](../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md), the system variable does not accept a comma-separated list. If you would like to specify multiple filters, then you need to specify the system variable multiple times.
  * See [Replication Filters](replication-filters.md) for more information.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--replicate-wild-do-table=name</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>string</code>`
* Default Value: `<code>''</code>` (empty)



#### `<code>replicate_wild_ignore_table</code>`


* Description: This system variable allows you to configure a [replica](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/README.md) to ignore statements and transactions that affect tables that match a specified wildcard pattern. The wildcard pattern uses the same semantics as the [LIKE](../../../reference/sql-statements-and-structure/sql-statements/built-in-functions/string-functions/like.md) operator. 

  * This system variable will work with cross-database updates with [statement-based logging](../../../server-management/server-monitoring-logs/binary-log/binary-log-formats.md#statement-based-logging). See the [Statement-Based Logging](replication-filters.md#statement-based-logging) section for more information.
  * When setting it dynamically with [SET GLOBAL](../../../../connectors/mariadb-connector-cpp/setup-for-connector-cpp-examples.md#global-session), the system variable accepts a comma-separated list of filters.
  * When setting it on the command-line or in a server [option group](../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md), the system variable does not accept a comma-separated list. If you would like to specify multiple filters, then you need to specify the system variable multiple times.
  * See [Replication Filters](replication-filters.md) for more information.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--replicate-wild-ignore-table=name</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>string</code>`
* Default Value: `<code>''</code>` (empty)



#### `<code>report_host</code>`


* Description: The host name or IP address the replica reports to the primary when it registers. If left unset, the replica will not register itself. Reported by [SHOW SLAVE HOSTS](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-replica-hosts.md). Note that it is not sufficient for the primary to simply read the IP of the replica from the socket once the replica connects. Due to NAT and other routing issues, that IP may not be valid for connecting to the replica from the primary or other hosts.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--report-host=host_name</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>string</code>`



#### `<code>report_password</code>`


* Description: Replica password reported to the primary when it registers. Reported by [SHOW SLAVE HOSTS](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-replica-hosts.md) if `<code>--show-slave-auth-info</code>` is set. This password has no connection with user privileges or with the [replication](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/README.md) user account password.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--report-password=password</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>string</code>`



#### `<code>report_port</code>`


* Description: The commandline option sets the TCP/IP port for connecting to the replica that will be reported to the [replicating](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/README.md) primary during the replica's registration. Viewing the variable will show this value.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--report-port=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value: `<code>0</code>`
* Range: `<code>0</code>` to `<code>65535</code>`



#### `<code>report_user</code>`


* Description: Replica's account user name reported to the primary when it registers. Reported by [SHOW SLAVE HOSTS](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-replica-hosts.md) if `<code>--show-slave-auth-info</code>` is set. This username has no connection with user privileges or with the [replication](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/README.md) user account.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--report-user=name</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>string</code>`



#### `<code>server_id</code>`


* Description: This system variable is used with [MariaDB replication](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/README.md) to identify unique primary and replica servers in a topology. This system variable is also used with the [binary log](../../../reference/storage-engines/innodb/binary-log-group-commit-and-innodb-flushing-performance.md) to determine which server a specific transaction originated on.

  * When [MariaDB replication](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/README.md) is used with standalone MariaDB Server, each server in the replication topology must have a unique `<code>server_id</code>` value.
  * When [MariaDB replication](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/README.md) is used with [MariaDB Galera Cluster](../../../reference/sql-statements-and-structure/sql-statements/built-in-functions/special-functions/galera-functions/README.md), see [Using MariaDB Replication with MariaDB Galera Cluster: Setting server_id on Cluster Nodes](../galera-cluster/using-mariadb-replication-with-mariadb-galera-cluster/using-mariadb-replication-with-mariadb-galera-cluster-using-mariadb-replica.md#setting-server_id-on-cluster-nodes) for more information on how to set the `<code>server_id</code>` values.
  * In [MariaDB 10.2.1](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1021-release-notes.md) and below, the default `<code>server_id</code>` value is `<code>0</code>`. If a replica's `<code>server_id</code>` value is `<code>0</code>`, then all primary's will refuse its connection attempts. If a primary's `<code>server_id</code>` value is `<code>0</code>`, then it will refuse all replica connection attempts.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--server-id =#</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>1</code>`
* Range: `<code>1</code>` to `<code>4294967295</code>`



#### `<code>skip_parallel_replication</code>`


* Description: If set when a transaction is written to the binlog, parallel apply of that transaction will be avoided on a replica where [slave_parallel_mode](#slave_parallel_mode) is not `<code>aggressive</code>`. Can be used to avoid unnecessary rollback and retry for transactions that are likely to cause a conflict if replicated in parallel. See [parallel replication](parallel-replication.md).
* Commandline: None
* Scope: Session
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`



#### `<code>skip_replication</code>`


* Description: Changes are logged into the [binary log](../../../reference/storage-engines/innodb/binary-log-group-commit-and-innodb-flushing-performance.md) with the @@skip_replication flag set. Such events will not be [replicated](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/README.md) by replica that run with `<code class="fixed" style="white-space:pre-wrap">--replicate-events-marked-for-skip</code>` set different from its default of `<code>REPLICATE</code>`. See [Selectively skipping replication of binlog events](selectively-skipping-replication-of-binlog-events.md) for more information.
* Commandline: None
* Scope: Session
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`



#### `<code>slave_abort_blocking_timeout</code>`


* Description: Maximum time a replica DDL will wait for a blocking SELECT or other user query until that query will be aborted. The argument will be treated as a decimal value with nanosecond precision. The variable is intended to solve a problem where a long-running SELECT on a replica causes DDL to wait for that SELECT to complete, potentially causing massive replica lag.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--slave-abort-blocking-timeout=num</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>double</code>`
* Default Value: `<code>31536000.000000</code>`
* Range: `<code>0</code>` to `<code>31536000</code>`
* Introduced: [MariaDB 11.7](../../../../release-notes/mariadb-community-server/what-is-mariadb-117.md)



#### `<code>slave_compressed_protocol</code>`


* Description: If set to 1 (0 is the default), will use compression for the replica/primary protocol if both primary and replica support this.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--slave-compressed-protocol</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>0</code>`



#### `<code>slave_connections_needed_for_purge</code>`


* Description: Minimum number of connected replicas required for automatic [binary log](../../../reference/storage-engines/innodb/binary-log-group-commit-and-innodb-flushing-performance.md) purge with [max_binlog_total_size](#max_binlog_total_size), [binlog_expire_logs_seconds](#binlog_expire_logs_seconds) or [expire_logs_days](#expire_logs_days).
Change of the value triggers an attempt to purging, though without binlog rotation, with the purged set of
files satisfying the above two parameters and the value that is set itself.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--slave-connections-needed-for-purge=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>1</code>`
* Range: `<code>0</code>` to `<code>18446744073709551615</code>`
* Introduced: [MariaDB 11.4](../../../../release-notes/mariadb-community-server/what-is-mariadb-114.md)



#### `<code>slave_ddl_exec_mode</code>`


* Description: Modes for how [replication](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/README.md) of DDL events should be executed. Legal values are `<code class="highlight fixed" style="white-space:pre-wrap">STRICT</code>` and `<code class="highlight fixed" style="white-space:pre-wrap">IDEMPOTENT</code>` (default). In `<code class="highlight fixed" style="white-space:pre-wrap">IDEMPOTENT</code>` mode, the replica will not stop for failed DDL operations that would not cause a difference between the primary and the replica. In particular [CREATE TABLE](../../../reference/sql-statements-and-structure/vectors/create-table-with-vectors.md) is treated as [CREATE OR REPLACE TABLE](../../../reference/sql-statements-and-structure/vectors/create-table-with-vectors.md#create-or-replace) and [DROP TABLE](../../../reference/sql-statements-and-structure/sql-statements/data-definition/drop/drop-tablespace.md) is treated as `<code class="highlight fixed" style="white-space:pre-wrap">DROP TABLE IF EXISTS</code>`.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--slave-ddl-exec-mode=name</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>enumeration</code>`
* Default Value: `<code>IDEMPOTENT</code>`
* Valid Values: `<code>IDEMPOTENT</code>`, `<code>STRICT</code>`



#### `<code>slave_domain_parallel_threads</code>`


* Description: When set to a non-zero value, each [replication](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/README.md) domain in one primary connection can reserve at most that many worker threads at any one time, leaving the rest (up to the value of
[slave_parallel_threads](#slave_parallel_threads)) free for other primary connections
or replication domains to use in parallel. See [Parallel Replication](parallel-replication.md#configuration-variable-slave_domain_parallel_threads) for details.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--slave-domain-parallel-threads=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>0</code>`
* Valid Values: `<code>0</code>` to `<code>16383</code>`



#### `<code>slave_exec_mode</code>`


* Description: Determines the mode used for [replication](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/README.md) error checking and conflict resolution. STRICT mode is the default, and catches all errors and conflicts. IDEMPOTENT mode suppresses duplicate key or no key errors, which can be useful in certain replication scenarios, such as when there are multiple primaries, or circular replication.
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>enumeration</code>`
* Default Value: `<code>IDEMPOTENT</code>` (NDB), `<code>STRICT</code>` (All)
* Valid Values: `<code>IDEMPOTENT</code>`, `<code>STRICT</code>`



#### `<code>slave_load_tmpdir</code>`


* Description: Directory where the replica stores temporary files for [replicating](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/README.md) [LOAD DATA INFILE](../../../reference/sql-statements-and-structure/sql-statements/data-manipulation/inserting-loading-data/load-data-into-tables-or-index/load-data-infile.md) statements. If not set, the replica will use [tmpdir](../optimization-and-tuning/system-variables/server-system-variables.md#tmpdir). Should be set to a disk-based directory that will survive restarts, or else replication may fail.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--slave-load-tmpdir=path</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>file name</code>`
* Default Value: `<code>/tmp</code>`



#### `<code>slave_max_allowed_packet</code>`


* Description: Maximum packet size in bytes for replica SQL and I/O threads. This value overrides [max_allowed_packet](#max_allowed_packet) for [replication](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/README.md) purposes. Set in multiples of 1024 (the minimum) up to 1GB
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--slave-max-allowed-packet=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>1073741824</code>`
* Range: `<code>1024</code>` to `<code>1073741824</code>`



#### `<code>slave_max_statement_time</code>`


* Description: A query that has taken more than this in seconds to run on the replica will be aborted. The argument will be treated as a decimal value with microsecond precision. A value of 0 (default) means no timeout.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--slave-max-statement-time=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>0.000000</code>`
* Range: `<code>0</code>` to `<code>31536000</code>`
* Introduced: [MariaDB 10.10](../../../../release-notes/mariadb-community-server/what-is-mariadb-1010.md)



#### `<code>slave_net_timeout</code>`


* Description: Time in seconds for the replica to wait for more data from the primary before considering the connection broken, after which it will abort the read and attempt to reconnect. The retry interval is determined by the MASTER_CONNECT_RETRY open for the [CHANGE MASTER](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md) statement, while the maximum number of reconnection attempts is set by the [master-retry-count](../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md#-master-retry-count) option. The first reconnect attempt takes place immediately.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--slave-net-timeout=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value:

  * `<code>60 (1 minute)</code>`
* Range: `<code>1</code>` to `<code>31536000</code>`



#### `<code>slave_parallel_max_queued</code>`


* Description: When [parallel_replication](parallel-replication.md) is used, the [SQL thread](replication-threads.md#slave-sql-thread) will read ahead in the relay logs, queueing events in memory while looking for opportunities for executing events in parallel. This system variable sets a
limit for how much memory it will use for this.

  * The configured value of this system variable is actually allocated for each [worker thread](replication-threads.md#worker-threads), so the total allocation is actually equivalent to the following:

    * `<code>[slave_parallel_max_queued](replication-and-binary-log-system-variables.md)</code>` * `<code>[slave_parallel_threads](replication-and-binary-log-system-variables.md)</code>`
  * This system variable is only meaningful when parallel
replication is configured (i.e. when `<code>[slave_parallel_threads](replication-and-binary-log-system-variables.md)</code>` > `<code>0</code>`).
  * See [Parallel Replication: Configuring the Maximum Size of the Parallel Slave Queue](parallel-replication.md#configuring-the-maximum-size-of-the-parallel-slave-queue) for more information.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--slave-parallel-max-queued=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>131072</code>`
* Range: `<code>0</code>` to `<code>2147483647</code>`



#### `<code>slave_parallel_mode</code>`


* Description: Controls what transactions are applied in parallel when using [parallel replication](parallel-replication.md). 

  * `<code>optimistic</code>`: tries to apply most transactional DML in parallel, and handles any conflicts with rollback and retry. See [optimistic mode](parallel-replication.md#optimistic-mode-of-in-order-parallel-replication).
  * `<code>conservative</code>`: limits parallelism in an effort to avoid any conflicts. See [conservative mode](parallel-replication.md#conservative-mode-of-in-order-parallel-replication).
  * `<code>aggressive</code>`: tries to maximize the parallelism, possibly at the cost of increased conflict rate.
  * `<code>minimal</code>`: only parallelizes the commit steps of transactions.
  * `<code>none</code>` disables parallel apply completely.
* Commandline: None
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>enum</code>`
* Default Value: `<code>optimistic</code>` (>= [MariaDB 10.5.1](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1051-release-notes.md)), `<code>conservative</code>` (<= [MariaDB 10.5.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1050-release-notes.md))
* Valid Values: `<code>conservative</code>`, `<code>optimistic</code>`, `<code>none</code>`, `<code>aggressive</code>` and `<code>minimal</code>`



#### `<code>slave_parallel_threads</code>`


* Description: This system variable is used to configure [parallel replication](parallel-replication.md).

  * If this system variable is set to a value greater than `<code>0</code>`, then its value will determine how many replica [worker threads](replication-threads.md#worker-threads) will be created to apply [binary log](../../../reference/storage-engines/innodb/binary-log-group-commit-and-innodb-flushing-performance.md) events in parallel.
  * If this system variable is set to `<code>0</code>` (which is the default value), then no replica [worker threads](replication-threads.md#worker-threads) will be created. Instead, when replication is enabled, [binary log](../../../reference/storage-engines/innodb/binary-log-group-commit-and-innodb-flushing-performance.md) events are applied by the replica's [SQL thread](replication-threads.md#slave-sql-thread).
  * The [replica threads](replication-threads.md#threads-on-the-slave) must be [stopped](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/stop-replica.md) in order to change this option's value dynamically.
  * Events that were logged with [GTIDs](gtid.md) with different `<code>[gtid_domain_id](gtid.md#gtid_domain_id)</code>` values can be applied in parallel in an [out-of-order](parallel-replication.md#out-of-order-parallel-replication) manner. Each `<code>[gtid_domain_id](gtid.md#gtid_domain_id)</code>` can use the number of threads configured by `<code>[slave_domain_parallel_threads](#slave_domain_parallel_threads)</code>`.
  * Events that were [group-committed](../../../server-management/server-monitoring-logs/binary-log/group-commit-for-the-binary-log.md) on the primary can be applied in parallel in an [in-order](parallel-replication.md#what-can-be-run-in-parallel) manner, and the specific behavior can be configured by setting `<code>[slave_parallel_mode](#slave_parallel_mode)</code>`.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--slave-parallel-threads=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>0</code>`
* Range: `<code>0</code>` to `<code>16383</code>`



#### `<code>slave_parallel_workers</code>`


* Description: Alias for [slave_parallel_threads](#slave_parallel_threads).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--slave-parallel-workers=#</code>`



#### `<code>slave_run_triggers_for_rbr</code>`


* Description: See [Running triggers on the slave for Row-based events](running-triggers-on-the-replica-for-row-based-events.md) for a description and use-case for this setting.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--slave-run-triggers-for-rbr=value</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>enum</code>`
* Default Value: `<code>NO</code>`
* Valid Values: `<code>NO</code>`, `<code>YES</code>`, `<code>LOGGING</code>`, or `<code>ENFORCE</code>` (>= [MariaDB 10.5.2](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1052-release-notes.md))



#### `<code>slave_skip_errors</code>`


* Description: When an error occurs on the replica, [replication](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/README.md) usually halts. This option permits a list of [error codes](../../../reference/mariadb-internals/using-mariadb-with-your-programs-api/error-codes/mariadb-error-codes-4000-to-4099/README.md) to ignore, and for which replication will continue. This option should never be needed in normal use, and careless use could lead to replica that are out of sync with primary's. Error codes are in the format of the number from the replica error log. Using `<code>all</code>` as an option permits the replica the keep replicating no matter what error it encounters, an option you would never normally need in production and which could rapidly lead to data inconsistencies. A count of these is kept in [slave_skipped_errors](replication-and-binary-log-status-variables.md#slave_skipped_errors).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--slave-skip-errors=[error_code1,error_code2,...|all|ddl_exist_errors]</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>string</code>`
* Default Value: `<code>OFF</code>`
* Valid Values: `<code>[list of error codes]</code>`, `<code>ALL</code>`, `<code>OFF</code>`



#### `<code>slave_sql_verify_checksum</code>`


* Description: Verify [binlog checksums](binlog-event-checksums.md) when the replica SQL thread reads events from the [relay log](../../../server-management/server-monitoring-logs/binary-log/relay-log.md).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--slave-sql-verify-checksum=[0|1]</code>`
* Scope: Global
* Access Type: Can be changed dynamically
* Data Type: `<code>bool</code>`
* Default Value: `<code>ON (1)</code>`



#### `<code>slave_transaction_retries</code>`


* Description: Number of times a [replication](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/README.md) replica retries to execute an SQL thread after it fails due to InnDB deadlock or by exceeding the transaction execution time limit. If after this number of tries the SQL thread has still failed to execute, the replica will stop with an error. See also the [innodb_lock_wait_timeout](../../../reference/storage-engines/innodb/innodb-system-variables.md) system variable.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--slave-transaction-retries=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>10</code>`
* Range - 32 bit: `<code>0</code>` to `<code>4294967295</code>`
* Range - 64 bit: `<code>0</code>` to `<code>18446744073709547520</code>`



#### `<code>slave_transaction_retry_errors</code>`


* Description: When an error occurs during a transaction on the replica, [replication](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/README.md) usually halts. By default, transactions that caused a deadlock or elapsed lock wait timeout will be retried. One can add other errors to the the list of errors that should be retried by adding a comma-separated list of [error numbers](../../../reference/mariadb-internals/using-mariadb-with-your-programs-api/error-codes/mariadb-error-codes-4000-to-4099/README.md) to this variable. This is particularly useful in some [Spider](../../../reference/storage-engines/spider/spider-functions/spider_copy_tables.md) setups. Some recommended errors to retry for Spider are 1020, 1158, 1159, 1160, 1161, 1429, 2013, 12701 (these are in the default value in recent versions).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--slave-transaction_retry-errors=[error_code1,error_code2,...]</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>string</code>`
* Default Value:

  * `<code>1158,1159,1160,1161,1205,1213,1020,1429,2013,12701</code>` (>= [MariaDB 10.6.18](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-10-6-18-release-notes.md), [MariaDB 10.11.8](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-11-series/mariadb-10-11-8-release-notes.md), [MariaDB 11.0.6](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-0-series/mariadb-11-0-6-release-notes.md), [MariaDB 11.1.5](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-1-series/mariadb-11-1-5-release-notes.md), [MariaDB 11.2.4](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-2-series/mariadb-11-2-4-release-notes.md), [MariaDB 11.4.2](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-4-series/mariadb-11-4-2-release-notes.md))
  * `<code>1158,1159,1160,1161,1205,1213,1429,2013,12701</code>` (>= [MariaDB 10.4.5](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-4-series/mariadb-1045-release-notes.md))
* Valid Values: `<code>comma-separated list of error codes</code>`
* Introduced: [MariaDB 10.3.3](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1033-release-notes.md)



#### `<code>slave_transaction_retry_interval</code>`


* Description: Interval in seconds for the replica SQL thread to retry a failed transaction due to a deadlock, elapsed lock wait timeout or an error listed in [slave_transaction_retry_errors](#slave_transaction_retry_errors). The interval is calculated as `<code>max(slave_transaction_retry_interval, min(retry_count, 5))</code>`.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--slave-transaction-retry-interval=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>0</code>`
* Range: `<code>0</code>` to `<code>3600</code>`
* Introduced: [MariaDB 10.3.3](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1033-release-notes.md)



#### `<code>slave_type_conversions</code>`


* Description: Determines the type conversion mode on the replica when using [row-based](../../../server-management/server-monitoring-logs/binary-log/binary-log-formats.md#row-based) [replication](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/README.md), including replications in MariaDB Galera cluster. Multiple options can be set, delimited by commas. If left empty, the default, type conversions are disallowed. The variable is dynamic and a change in its value takes effect immediately. This variable tells the server what to do if the table definition is different between the primary and replica (for example a column is 'int' on the primary and 'bigint' on the replica). 

  * `<code>ALL_NON_LOSSY</code>` means that all safe conversions (no data loss) are allowed.
  * `<code>ALL_LOSSY</code>` means that all lossy conversions are allowed (for example 'bigint' to 'int'). This, however, does not imply that safe conversions (non-lossy) are allowed as well. In order to allow all conversions, one needs to allow both lossy as well as non-lossy conversions by setting this variable to ALL_NON_LOSSY,ALL_LOSSY.
  * Empty (default) means that the server should give an error and replication should stop if the table definition is different between the primary and replica.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--slave-type-conversions=set</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>set</code>`
* Default Value: `<code>Empty variable</code>`
* Valid Values: `<code>ALL_LOSSY</code>`, `<code>ALL_NON_LOSSY</code>`, empty



#### `<code>sql_log_bin</code>`


* Description: If set to 0 (1 is the default), no logging to the [binary log](../../../reference/storage-engines/innodb/binary-log-group-commit-and-innodb-flushing-performance.md) is done for the client. Only clients with the SUPER privilege can update this variable. Does not affect the replication of events in a Galera cluster. Note that `<code>sql_log_bin</code>` has no effect if `<code>[log_bin](replication-and-binary-log-system-variables.md#log_bin)</code>` is not set.
* Scope: Session
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>1</code>`
* Related variables: `<code>[log_bin](replication-and-binary-log-system-variables.md#log_bin)</code>`



#### `<code>sql_slave_skip_counter</code>`


* Description: Number of events that a replica skips from the primary. If this would cause the replica to begin in the middle of an event group, the replica will instead begin from the beginning of the next event group. See [SET GLOBAL sql_slave_skip_counter](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/set-global-sql_slave_skip_counter.md).
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>0</code>`



#### `<code>sync_binlog</code>`


* Description: MariaDB will synchronize its binary log file to disk after this many events. The default is 0, in which case the operating system handles flushing the file to disk. 1 is the safest, but slowest, choice, since the file is flushed after each write. If autocommit is enabled, there is one write per statement, otherwise there's one write per transaction. If the disk has cache backed by battery, synchronization will be fast and a more conservative number can be chosen.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--sync-binlog=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>0</code>`
* Range: `<code>0</code>` to `<code>4294967295</code>`



#### `<code>sync_master_info</code>`


* Description: A [replication](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/README.md) replica will synchronize its master.info file to disk after this many events. If set to 0, the operating system handles flushing the file to disk.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--sync-master-info=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>10000</code>`



#### `<code>sync_relay_log</code>`


* Description: The MariaDB server will synchronize its [relay log](../../../server-management/server-monitoring-logs/binary-log/relay-log.md) to disk after this many writes to the log. The default until [MariaDB 10.1.7](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-7-release-notes.md) was 0, in which case the operating system handles flushing the file to disk. 1 is the safest, but slowest, choice, since the file is flushed after each write. If autocommit is enabled, there is one write per statement, otherwise there's one write per transaction. If the disk has cache backed by battery, synchronization will be fast and a more conservative number can be chosen.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--sync-relay-log=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>10000</code>`



#### `<code>sync_relay_log_info</code>`


* Description: A [replication](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/README.md) replica will synchronize its relay-log.info file to disk after this many transactions. The default until [MariaDB 10.1.7](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-7-release-notes.md) was 0, in which case the operating system handles flushing the file to disk. 1 is the most secure choice, because at most one event could be lost in the event of a crash, but it's also the slowest.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--sync-relay-log-info=#</code>`
* Scope: Global,
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>10000</code>`
* Range: `<code>0</code>` to `<code>4294967295</code>`


