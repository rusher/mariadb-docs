
# Spider System Variables

The following variables are available when the [Spider](spider-functions/spider_copy_tables.md) storage engine has been installed.


See [Server System Variables](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md) for a complete list of system variables and instructions on setting them.


See also the [Full list of MariaDB options, system and status variables](../../../server-management/variables-and-modes/full-list-of-mariadb-options-system-and-status-variables.md).



##### MariaDB starting with [10.5.22](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-10-5-22-release-notes.md)
Starting from [MariaDB 10.5.22](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-10-5-22-release-notes.md), [MariaDB 10.6.15](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-10-6-15-release-notes.md), [MariaDB 10.9.8](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-9-series/mariadb-10-9-8-release-notes.md), [MariaDB 10.10.6](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-10-series/mariadb-10-10-6-release-notes.md), [MariaDB 10.11.5](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-11-series/mariadb-10-11-5-release-notes.md), [MariaDB 11.0.3](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-0-series/mariadb-11-0-3-release-notes.md), all spider system variables with the value -1 for deferring to table parameter values follow the correct overriding mechanism: table parameter (if set) overrides system variables (if not -1) overrides actual variable default. As a side effect, all such system variables in all versions have the same default value as the table param default value.
Before this change, a non-minus-one system variable value would override the table parameter value. That is, if both the system variable value and the table parameter value were set to be non-minus-one, the system variable value would prevail. For [MariaDB 10.7](../../../../release-notes/mariadb-community-server/what-is-mariadb-107.md)+ where the system variable default values were the same as table param default instead of -1, this means that if the system variable were not set, but a table param is set to a non-default value, the default would override the non-default value.



#### `<code>spider_auto_increment_mode</code>`


* Description: The [auto increment](../innodb/auto_increment-handling-in-innodb.md) mode.

  * `<code>-1</code>` Falls back to the default value, if the [table parameter](spider-table-parameters.md) is not set.
  * `<code>0</code>` Normal Mode. Uses a counter that Spider gets from the remote backend server with an exclusive lock for the auto-increment value. This mode is slow. Use Quick Mode (`<code>2</code>`), if you use Spider tables with the table partitioning feature and the auto-increment column is the first column of the index.
  * `<code>1</code>` Quick Mode. Uses an internal Spider counter for the auto-increment value. This mode is fast, but it is possible for duplicates to occur when updating the same table from multiple Spider proxies.
  * `<code>2</code>` Set Zero Mode. The auto-increment value is given by the remote backend. Sets the column to `<code>0</code>`, even if you set the value to the auto-increment column in your statement. If you use the table with the table partitioning feature, it sets to zero after choosing an inserted partition.
  * `<code>3</code>` When the auto-increment column is set to `<code>NULL</code>`, the value is given by the remote backend server. If you set the auto-increment column to `<code>0</code>`,the value is given by the local server. Set [spider_reset_auto_incremnet](#spider_reset_auto_increment) to `<code>2</code>` or `<code>3</code>` if you want to use an auto-increment column on the remote server.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Session Value: `<code>0</code>`
* Default Table Value: `<code>0</code>`
* Range: `<code>-1</code>` to `<code>3</code>`
* DSN Parameter Name: `<code>aim</code>`



#### `<code>spider_bgs_first_read</code>`


* Description: Number of first read records to use when performing a concurrent background search. To start a range scan on the remote backend, the storage engine first needs to send the first record. Fetching a second record in the same query can save a network round trip stopping the plan if the backend has a single record. The first and second reads are used to warm up for background search. When not using [spider_split_read](#spider_split_read) and [spider_semi_split_read](#spider_semi_split_read), the third read fetches the remaining data source in a single fetch.

  * `<code>-1</code>` Falls back to the default value, if the [table parameter](spider-table-parameters.md) is not set.
  * `<code>0</code>` Records are usually retrieved.
  * `<code>1</code>` and greater: Number of records.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Session Value: `<code>2</code>`
* Default Table Value: `<code>2</code>`
* Range: `<code>-1</code>` to `<code>9223372036854775807</code>`
* DSN Parameter Name: `<code>bfr</code>`



#### `<code>spider_bgs_mode</code>`


* Description: Background search mode. This enables the use of a thread per data server connection if the query is not shard-based and must be distributed across shards. The partitioning plugin scans partitions one after the other to optimize memory usage. Because the shards are external, reading all shards can be performed in parallel when the plan prunes multiple partitions. 

  * `<code>-1</code>` Falls back to the default value, if the [table parameter](spider-table-parameters.md) is not set.
  * `<code>0</code>` Disables background search.
  * `<code>1</code>` Uses background search when searching without locks
  * `<code>2</code>` Uses background search when searching without locks or with shared locks.
  * `<code>3</code>` Uses background search regardless of locks.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Session Value: `<code>0</code>`
* Default Table Value: `<code>0</code>`
* Range: `<code>-1</code>` to `<code>3</code>`
* DSN Parameter Name: `<code>bmd</code>`



#### `<code>spider_bgs_second_read</code>`


* Description: Number of second read records on the backend server when using background search. When the first records are found from [spider_bgs_first_read](#spider_bgs_first_read), the engine continues scanning a range adding a `<code>LIMIT</code>` of [spider_bgs_first_read](#spider_bgs_first_read) and [spider_bgs_second_read](#spider_bgs_second_read).

  * `<code>-1</code>` Falls back to the default value, if the [table parameter](spider-table-parameters.md) is not set.
  * `<code>0</code>` Records are usually retrieved.
  * `<code>1</code>` and greater: Number of records.
* Scope: Global, Session
* Dynamic: Yes
* Default Session Value: `<code>100</code>`
* Default Table Value: `<code>100</code>`
* Range: `<code>-1</code>` to `<code>9223372036854775807</code>`
* DSN Parameter Name: `<code>bsr</code>`



#### `<code>spider_bka_engine</code>`


* Description: Storage engine used with temporary tables when the [spider_bka_mode](#spider_bka_mode) system variable is set to `<code>1</code>`. Defaults to the value of the [table parameter](spider-table-parameters.md), which is [MEMORY](../memory-storage-engine.md) by default.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>string</code>`
* Default Session Value: `<code>""</code>`
* Default Table Value: `<code>Memory</code>`
* DSN Parameter Name: `<code>bke</code>`



#### `<code>spider_bka_mode</code>`


* Description: Internal action to perform when multi-split reads are disabled. If the [spider_multi_split_read](#spider_multi_split_read) system variable is set to `<code>0</code>`, Spider uses this variable to determine how to handle statements when the optimizer resolves range retrieval to multiple conditions.

  * `<code> -1</code>` Falls back to the default value, if the [table parameter](spider-table-parameters.md) is not set.
  * `<code>0</code>` Uses "union all".
  * `<code>1</code>` Uses a temporary table, if it is judged acceptable.
  * `<code>2</code>` Uses a temporary table, if it is judged acceptable and avoids replication delay.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Session Value: `<code>1</code>`
* Default Table Value: `<code>1</code>`
* Range: `<code>-1</code>` to `<code>2</code>`
* DSN Parameter Name: `<code>bkm</code>`



#### `<code>spider_bka_table_name_type</code>`


* Description: The type of temporary table name for bka.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Session Value: `<code>1</code>`
* Range: `<code>-1</code>` to `<code>1</code>`



#### `<code>spider_block_size</code>`


* Description: Size of memory block used in MariaDB. Can usually be left unchanged.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Session Value: `<code>16384</code>`
* Range: `<code>0</code>` to `<code>4294967295</code>`
* DSN Parameter Name: `<code>bsz</code>`



#### `<code>spider_buffer_size</code>`


* Description: Buffer size. `<code>-1</code>`, the default, will use the [table parameter](spider-table-parameters.md).
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Session Value: `<code>16000</code>`
* Default Table Value: `<code>16000</code>`
* Range: `<code>-1</code>` to `<code>2147483647</code>`
* Introduced: [MariaDB 10.5.4](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1054-release-notes.md)



#### `<code>spider_bulk_size</code>`


* Description: Size in bytes of the buffer when multiple grouping multiple `<code>INSERT</code>` statements in a batch, (that is, bulk inserts).

  * `<code>-1</code>` The [table parameter](spider-table-parameters.md) is adopted.
  * `<code>0</code>` or greater: Size of the buffer.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Session Value: `<code>16000</code>`
* Default Table Value: `<code>16000</code>`
* Range: `<code>-1</code>` to `<code>2147483647</code>`
* DSN Parameter Name: `<code>bsz</code>`



#### `<code>spider_bulk_update_mode</code>`


* Description: Bulk update and delete mode. Note: If you use a non-default value for the [spider_bgs_mode](#spider_bgs_mode) or [spider_split_read](#spider_split_read) system variables, Spider sets this variable to `<code>2</code>`.

  * `<code>-1</code>` Falls back to the default value, if the [table parameter](spider-table-parameters.md) is not set.
  * `<code>0</code>` Sends `<code>UPDATE</code>` and `<code>DELETE</code>` statements one by one.
  * `<code>1</code>` Collects multiple `<code>UPDATE</code>` and `<code>DELETE</code>` statements, then sends the collected statements one by one.
  * `<code>2</code>` Collects multiple `<code>UPDATE</code>` and `<code>DELETE</code>` statements and sends them together.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Session Value: `<code>0</code>`
* Default Table Value: `<code>0</code>`
* Range: `<code>-1</code>` to `<code>2</code>`
* DSN Parameter Name: `<code>bum</code>`



#### `<code>spider_bulk_update_size</code>`


* Description: Size in bytes for `<code>UPDATE</code>` and `<code>DELETE</code>` queries when generating bulk updates.

  * `<code>-1</code>` The [table parameter](spider-table-parameters.md) is adopted.
  * `<code>0</code>` or greater: Size of buffer.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Session Value: `<code>16000</code>`
* Default Table Value: `<code>16000</code>`
* Range: `<code>-1</code>` to `<code>2147483647</code>`
* DSN Parameter Name: `<code>bus</code>`



#### `<code>spider_casual_read</code>`


* Description: Casual Reads enables all isolation levels, (such as repeatable reads) to work with transactions on multiple backends. With auto-commit queries, you can relax read consistency and run on multiple connections to the backends. This enables parallel queries across partitions, even if multiple shards are stored on the same physical server. Deprecated in [MariaDB 11.5](../../../../release-notes/mariadb-community-server/what-is-mariadb-115.md) due to the complexity of the code for little benefit.

  * `<code>-1</code>` Use [table parameter](spider-table-parameters.md).
  * `<code>0</code>` Use casual read.
  * `<code>1</code>` Choose connection channel automatically.
  * `<code>2</code>` to `<code>63</code>` Number of connection channels.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Session Value: `<code>0</code>`
* Default Table Value: `<code>0</code>`
* Range: `<code>-1</code>` to `<code>63</code>`
* DSN Parameter Name: `<code>##</code>`
* Deprecated: [MariaDB 11.5](../../../../release-notes/mariadb-community-server/what-is-mariadb-115.md)



#### `<code>spider_conn_recycle_mode</code>`


* Description: Connection recycle mode.

  * `<code>0</code>` Disconnect.
  * `<code>1</code>` Recycle by all sessions.
  * `<code>2</code>` Recycle in the same session.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Range: `<code>0</code>` to `<code>2</code>`
* Default Session Value: `<code>0</code>`



#### `<code>spider_conn_recycle_strict</code>`


* Description: Whether to force the creation of new connections.

  * `<code>1</code>` Don't force.
  * `<code>0</code>` Force new connection
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Session Value: `<code>0</code>`
* Range: `<code>0</code>` to `<code>1</code>`



#### `<code>spider_conn_wait_timeout</code>`


* Description: Max waiting time in seconds for Spider to get a remote connection.
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Session Value: `<code>10</code>`
* Range: `<code>0</code>` to `<code>1000</code>`
* Introduced: [MariaDB 10.3.3](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1033-release-notes.md)



#### `<code>spider_connect_error_interval</code>`


* Description: Return same error code until interval passes if connection is failed
* Scope: Global,
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>1</code>`
* Range: `<code>0</code>` to `<code>4294967295</code>`



#### `<code>spider_connect_mutex</code>`


* Description: Whether to serialize remote servers connections (use mutex at connecting). Use this parameter if you get an error or slowdown due to too many connection processes.

  * `<code>0</code>` Not serialized.
  * `<code>1</code>` : Serialized.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Session Value: `<code>0</code>`



#### `<code>spider_connect_retry_count</code>`


* Description: Number of times to retry connections that fail due to too many connection processes.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Session Value: `<code>2</code>` (>= [MariaDB 11.8](../../../../release-notes/mariadb-community-server/what-is-mariadb-118.md)), `<code>1000</code>` (<= [MariaDB 11.7](../../../../release-notes/mariadb-community-server/what-is-mariadb-117.md))
* Range: `<code>0</code>` to `<code>2147483647</code>`



#### `<code>spider_connect_retry_interval</code>`


* Description: Interval in microseconds for connection failure due to too many connection processes.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Session Value: `<code>1000</code>`
* Range: `<code>-1</code>` to `<code>9223372036854775807</code>`



#### `<code>spider_connect_timeout</code>`


* Description: Timeout in seconds to declare remote backend unresponsive when opening a connection. Change for high-latency networks.

  * `<code>-1</code>` The [table parameter](spider-table-parameters.md) is adopted.
  * `<code>0</code>` Less than 1.
  * `<code>1</code>` and greater: Number of seconds.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Session Value: `<code>6</code>`
* Default Table Value: `<code>0</code>`
* Range: `<code>-1</code>` to `<code>2147483647</code>`
* DSN Parameter Name: `<code>cto</code>`



#### `<code>spider_crd_bg_mode</code>`


* Description: Indexes cardinality statistics in the background. Disable when the [spider_crd_mode](#spider_crd_mode) system variable is set to `<code>3</code>` or when the [spider_crd_interval](#spider_crd_interval) variable is set to `<code>0</code>`.

  * `<code>-1</code>` Falls back to the default value, if the [table parameter](spider-table-parameters.md) is not set.
  * `<code>0</code>` Disables background confirmation.
  * `<code>2</code>` Enables background confirmation.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Session Value: `<code>2</code>`
* Default Table Value: `<code>1</code>`
* Range: `<code>-1</code>` to `<code>2</code>`
* DSN Parameter Name: `<code>cbm</code>`



#### `<code>spider_crd_interval</code>`


* Description: Time interval in seconds of index cardinality statistics. Set to `<code>0</code>` to always get the latest information from remote servers. 

  * `<code>-1</code>` The [table parameter](spider-table-parameters.md) is adopted.
  * `<code>1</code>` or more: Interval in seconds table state confirmation.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Session Value: `<code>51</code>`
* Default Table Value: `<code>51</code>`
* Range: `<code>-1</code>` to `<code>2147483647</code>`
* DSN Parameter Name: `<code>civ</code>`



#### `<code>spider_crd_mode</code>`


* Description: Mode for index cardinality statistics. By default, uses `<code>SHOW</code>` at the table-level.

  * `<code>-1,0</code>` Uses the [table parameter](spider-table-parameters.md).
  * `<code>1</code>` Uses the `<code>SHOW</code>` command.
  * `<code>2</code>` Uses the Information Schema.
  * `<code>3</code>` Uses the `<code>EXPLAIN</code>` command.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Session Value: `<code>1</code>`
* Default Table Value: `<code>1</code>`
* Range: `<code>-1</code>` to `<code>3</code>`
* DSN Parameter Name: `<code>cmd</code>`
* Deprecated: [MariaDB 10.7.4](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-7-series/mariadb-1074-release-notes.md), [MariaDB 10.8.3](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-8-series/mariadb-1083-release-notes.md)



#### `<code>spider_crd_sync</code>`


* Description: Synchronize index cardinality statistics in partitioned tables.

  * `<code>-1</code>` Falls back to the default value, if the [table parameter](spider-table-parameters.md) is not set.
  * `<code>0</code>` Disables synchronization.
  * `<code>1</code>` Uses table state synchronization when opening a table, but afterwards performs no synchronization.
  * `<code>2</code>` Enables synchronization.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Session Value: `<code>0</code>`
* Default Table Value: `<code>0</code>`
* Range: `<code>-1</code>` to `<code>2</code>`
* DSN Parameter Name: `<code>csy</code>`



#### `<code>spider_crd_type</code>`


* Description: Type of cardinality calculation. Only effective when the [spider_crd_mode](#spider_crd_mode) system variable is set to use `<code>SHOW</code>` (`<code>1</code>`) or to use the Information Schema (`<code>2</code>`).

  * `<code>-1</code>` Falls back to the default value, if the [table parameter](spider-table-parameters.md) is not set.
  * `<code>0</code>` Uses the value of the [spider_crd_weight](#spider_crd_weight) system variable, as a fixed value.
  * `<code>1</code>` Uses the value of the [spider_crd_weight](#spider_crd_weight) system variable, as an addition value.
  * `<code>2</code>` Uses the value of the [spider_crd_weight](#spider_crd_weight) system variable, as a multiplication value.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Session Value: `<code>2</code>`
* Default Table Value: `<code>2</code>`
* Range: `<code>-1</code>` to `<code>2</code>`
* DSN Parameter Name: `<code>ctp</code>`
* Deprecated: [MariaDB 10.7.4](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-7-series/mariadb-1074-release-notes.md), [MariaDB 10.8.3](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-8-series/mariadb-1083-release-notes.md)



#### `<code>spider_crd_weight</code>`


* Description: Weight coefficient used to calculate effectiveness of index from the cardinality of column. For more information, see the description for the [spider_crd_type](#spider_crd_type) system variable.

  * `<code>-1</code>` Falls back to the default value, if the [table parameter](spider-table-parameters.md) is not set.
  * `<code>0</code>` or greater: Weight.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Session Value: `<code>2</code>`
* Default Table Value: `<code>2</code>`
* Range: `<code>-1</code>` to `<code>2147483647</code>`
* DSN Parameter Name: `<code>cwg</code>`
* Deprecated: [MariaDB 10.7.4](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-7-series/mariadb-1074-release-notes.md), [MariaDB 10.8.3](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-8-series/mariadb-1083-release-notes.md)



#### `<code>spider_delete_all_rows_type</code>`


* Description: The type of delete_all_rows.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Session Value: `<code>1</code>`
* Range: `<code>-1</code>` to `<code>1</code>`



#### `<code>spider_direct_dup_insert</code>`


* Description: Manages duplicate key check for [REPLACE](../../sql-statements-and-structure/sql-statements/built-in-functions/string-functions/replace-function.md), [INSERT IGNORE](../../sql-statements-and-structure/sql-statements/data-manipulation/inserting-loading-data/ignore.md) and [LOAD DATA LOCAL INFILE](../../sql-statements-and-structure/sql-statements/data-manipulation/inserting-loading-data/load-data-into-tables-or-index/load-data-infile.md) to remote servers. This can save on network roundtrips if the key always maps to a single partition. For bulk operations, records are checked for duplicate key errors one by one on the remote server, unless you set it to avoid duplicate checks on local servers (`<code>1</code>`).

  * `<code>-1</code>` Falls back to the default value, if the [table parameter](spider-table-parameters.md) is not set.
  * `<code>0</code>` Performs duplicate checks on the local server.
  * `<code>1</code>` Avoids duplicate checks on the local server.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Session Value: `<code>0</code>`
* Default Table Value: `<code>0</code>`
* Range: `<code>-1</code>` to `<code>1</code>`
* DSN Parameter Name: `<code>ddi</code>`



#### `<code>spider_direct_order_limit</code>`


* Description: Pushes `<code>ORDER BY</code>` and `<code>LIMIT</code>` operations to the remote server.

  * `<code>-1</code>` Falls back to the default value, if the [table parameter](spider-table-parameters.md) is not set.
  * `<code>0</code>` Uses local execution.
  * `<code>1</code>` Uses push down execution.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Session Value: `<code>2</code>`
* Default Table Value: `<code>9223372036854775807</code>`
* Range: `<code>-1</code>` to `<code>9223372036854775807</code>`
* DSN Parameter Name: `<code>dol</code>`



#### `<code>spider_disable_group_by_handler</code>`


* Description: Whether to disable the spider group by handler, which if created takes over the query execution after query optimization is done.

  * `<code>OFF</code>` Does not disable the spider group by handler.
  * `<code>ON</code>` Disables the spider group by handler.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`
* Introduced: [MariaDB 10.10.7](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-10-series/mariadb-10-10-7-release-notes.md)



#### `<code>spider_dry_access</code>`


* Description: Simulates an empty result-set. No queries are sent to the backend. Use for performance tuning.

  * `<code>0</code>` Normal access.
  * `<code>1</code>` All access from Spider to data node is suppressed.
* Scope: Global
* Dynamic: No
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`



#### `<code>spider_error_read_mode</code>`


* Description: Sends an empty result-set when reading a backend server raises an error. Useful with applications that don't implement transaction replays.

  * `<code>-1</code>` Falls back to the default value, if the [table parameter](spider-table-parameters.md) is not set.
  * `<code>0</code>` Returns an error.
  * `<code>1</code>` Returns an empty result.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Session Value: `<code>0</code>`
* Default Table Value: `<code>0</code>`
* Range: `<code>-1</code>` to `<code>1</code>`
* DSN Parameter Name: `<code>erm</code>`



#### `<code>spider_error_write_mode</code>`


* Description: Sends an empty result-set when writing to a backend server raises an error. Useful with applications that don't implement transaction replays.

  * `<code>-1</code>` Falls back to the default value, if the [table parameter](spider-table-parameters.md) is not set.
  * `<code>0</code>` Returns an error.
  * `<code>1</code>` Returns an empty result-set on error.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Session Value: `<code>0</code>`
* Default Table Value: `<code>0</code>`
* Range: `<code>-1</code>` to `<code>1</code>`
* DSN Parameter Name: `<code>ewm</code>`



#### `<code>spider_first_read</code>`


* Description: Number of first read records to start a range scan on the backend server. Spider needs to send the first record. Fetching the second record saves network round-trips, stopping the plan if the backend has a single record. First read and second read are used to warm up for background searches, third reads without using the [spider_split_read](#spider_split_read) and [spider_semi_split_read](#spider_semi_split_read) system variables fetches the remaining data source in a single last fetch.

  * `<code>-1</code>` Use the [table parameter](spider-table-parameters.md).
  * `<code>0</code>` Usually retrieves records.
  * `<code>1</code>` and greater: Sets the number of first read records.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Session Value: `<code>0</code>`
* Default Table Value: `<code>2</code>`
* Range: `<code>-1</code>` to `<code>9223372036854775807</code>`
* DSN Parameter Name: `<code>frd</code>`



#### `<code>spider_force_commit</code>`


* Description: Behavior when error occurs on `<code>XA PREPARE</code>`, `<code>XA COMMIT</code>`, and `<code>XA ROLLBACK</code>` statements.

  * `<code>0</code>` Returns the error.
  * `<code>1</code>` Returns the error when the `<code>xid</code>` doesn't exist, otherwise it continues processing the XA transaction.
  * `<code>2</code>` Continues processing the XA transaction, disregarding all errors.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Session Value: `<code>0</code>`
* Range: `<code>0</code>` to `<code>2</code>`



#### `<code>spider_general_log</code>`


* Description: Whether Spider logs all commands to the General Log. Spider logs error codes according to the [spider_log_result_errors](#spider_log_result_errors) system variable.

  * `<code>OFF</code>` Logs no commands.
  * `<code>ON</code>` Logs commands to the General Log.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Session Value: `<code>OFF</code>`



#### `<code>spider_ignore_comments</code>`


* Description: Whether to unconditionally ignore COMMENT and CONNECTION strings without checking whether table options are specified.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`
* Introduced: [MariaDB 11.3.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-0-release-notes.md)



#### `<code>spider_index_hint_pushdown</code>`


* Description: Whether to use pushdown index hints, like `<code>force_index</code>`.

  * `<code>0</code>` Do not use pushdown hints
  * `<code>1</code>` Use pushdown hints
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Session Value: `<code>OFF</code>`
* Introduced: [MariaDB 10.3.3](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1033-release-notes.md)



#### `<code>spider_init_sql_alloc_size</code>`


* Description: Initial size of the local SQL buffer.

  * `<code>-1</code>` Falls back to the default value, if the [table parameter](spider-table-parameters.md) is not set.
  * `<code>0</code>` or greater: Size of the buffer.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Session Value: `<code>1024</code>`
* Default Table Value: `<code>1024</code>`
* DSN Parameter Name: `<code>isa</code>`
* Range: `<code>-1</code>` to `<code>2147483647</code>`
* Deprecated: [MariaDB 10.7.5](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-7-series/mariadb-1075-release-notes.md), [MariaDB 10.8.4](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-8-series/mariadb-1084-release-notes.md), [MariaDB 10.9.2](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-9-series/mariadb-1092-release-notes.md)



#### `<code>spider_internal_limit</code>`


* Description: Limits the number of records when acquired from a remote server.

  * `<code>-1</code>` The [table parameter](spider-table-parameters.md) is adopted.
  * `<code>0</code>` or greater: Records limit.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Session Value: `<code>9223372036854775807</code>`
* Default Table Value: `<code>9223372036854775807</code>`
* Range: `<code>-1</code>` to `<code>9223372036854775807</code>`
* DSN Parameter Name: `<code>ilm</code>`
* Deprecated: [MariaDB 10.7.4](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-7-series/mariadb-1074-release-notes.md), [MariaDB 10.8.3](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-8-series/mariadb-1083-release-notes.md)



#### `<code>spider_internal_offset</code>`


* Description: Skip records when acquired from the remote server.

  * `<code>-1</code>` Falls back to the default value, if the [table parameter](spider-table-parameters.md) is not set.
  * `<code>0</code>` or more : Number of records to skip.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Session Value: `<code>0</code>`
* Default Table Value: `<code>0</code>`
* Range: `<code>-1</code>` to `<code>9223372036854775807</code>`
* DSN Parameter Name: `<code>ios</code>`
* Deprecated: [MariaDB 10.7.4](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-7-series/mariadb-1074-release-notes.md), [MariaDB 10.8.3](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-8-series/mariadb-1083-release-notes.md)



#### `<code>spider_internal_optimize</code>`


* Description: Whether to perform push down operations for [OPTIMIZE TABLE](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/optimizing-tables/optimize-table.md) statements.

  * `<code>-1</code>` Falls back to the default value, if the [table parameter](spider-table-parameters.md) is not set.
  * `<code>0</code>` Transmitted.
  * `<code>1</code>` Not transmitted.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Session Value: `<code>0</code>`
* Default Table Value: `<code>0</code>`
* Range: `<code>-1</code>` to `<code>1</code>`
* DSN Parameter Name: `<code>iom</code>`



#### `<code>spider_internal_optimize_local</code>`


* Description: Whether to transmit to remote servers when [OPTIMIZE TABLE](https://mariadb.com/kb/en/optimize_table) statements are executed on the local server.

  * `<code>-1</code>` Falls back to the default value, if the [table parameter](spider-table-parameters.md) is not set.
  * `<code>0</code>` Not transmitted.
  * `<code>1</code>` Transmitted.
* Default Session Value: `<code>0</code>`
* Default Table Value: `<code>0</code>`
* Range: `<code>-1</code>` to `<code>1</code>`
* DSN Parameter Name: `<code>iol</code>`



#### `<code>spider_internal_sql_log_off</code>`


* Description: Whether to log SQL statements sent to the remote server in the [General Query Log](../../../server-management/server-monitoring-logs/general-query-log.md). 

  * Explicitly setting this system variable to either `<code>ON</code>` or `<code>OFF</code>` causes the Spider node to send a `<code>SET sql_log_off</code>` statement to each of the data nodes using the `<code>SUPER</code>` privilege.
  * `<code>-1</code>` Don't know or does not matter; don't send 'SET SQL_LOG_OFF' statement
  * `<code>0</code>` Send 'SET SQL_LOG_OFF 0' statement to data nodes (logs SQL statements to the remote server)
  * `<code>1</code>` Send 'SET SQL_LOG_OFF 1' statement to data nodes (doesn't log SQL statements to the remote server)
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>` (previously `<code>boolean</code>`)
* Range: `<code>-1</code>` to `<code>1</code>`
* Default Session Value: `<code>-1</code>` (previously `<code>ON</code>`)



#### `<code>spider_internal_unlock</code>`


* Description: Whether to transmit unlock tables to the connection of the table used with `<code>SELECT</code>` statements.

  * `<code>0</code>` Not transmitted.
  * `<code>1</code>` Transmitted.
* Data Type: `<code>boolean</code>`
* Default Session Value: `<code>0</code>`



#### `<code>spider_internal_xa</code>`


* Description: Whether to implement XA at the server- or storage engine-level. When using the server-level, set different values for the [server_id](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#server_id) system variable on all server instances to generate different `<code>xid</code>` values.

  * `<code>OFF</code>` Uses the storage engine protocol.
  * `<code>ON</code>` Uses the server protocol.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Session Value: `<code>OFF</code>`



#### `<code>spider_internal_xa_id_type</code>`


* Description: The type of internal_xa id.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Session Value: `<code>0</code>`
* Range: `<code>-1</code>` to `<code>1</code>`



#### `<code>spider_internal_xa_snapshot</code>`


* Description: Limitation for reading consistent data on all backend servers when using MariaDB's internal XA implementation and `<code>START TRANSACTION WITH CONSISTENT SNAPSHOT</code>`.

  * `<code>0</code>` Raise error when using a Spider table.
  * `<code>1</code>` Raise error when issued a `<code>START TRANSACTION</code>` statement.
  * `<code>2</code>` Takes a consistent snapshot on each backend, but loses global consistency.
  * `<code>3</code>` Starts transactions with XA, but removes `<code>CONSISTENT SNAPSHOT</code>`.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Range: `<code>0</code>` to `<code>3</code>`
* Default Session Value: `<code>0</code>`



#### `<code>spider_load_crd_at_startup</code>`


* Description: Whether to load CRD from the system table at startup.

  * `<code>-1</code>` Use [table parameter](spider-table-parameters.md)
  * `<code>0</code>` Do not load
  * `<code>1</code>` Load
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Session Value: `<code>1</code>`
* Range: `<code>-1</code>` to `<code>1</code>`
* Introduced: [MariaDB 10.3.3](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1033-release-notes.md)
* Deprecated: [MariaDB 10.7.4](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-7-series/mariadb-1074-release-notes.md), [MariaDB 10.8.3](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-8-series/mariadb-1083-release-notes.md)



#### `<code>spider_load_sts_at_startup</code>`


* Description: Whether to load STS from the system table at startup.

  * `<code>-1</code>` Use [table parameter](spider-table-parameters.md)
  * `<code>0</code>` Do not load
  * `<code>1</code>` Load
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Session Value: `<code>1</code>`
* Range: `<code>-1</code>` to `<code>1</code>`
* Introduced: [MariaDB 10.3.3](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1033-release-notes.md)
* Deprecated: [MariaDB 10.7.4](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-7-series/mariadb-1074-release-notes.md), [MariaDB 10.8.3](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-8-series/mariadb-1083-release-notes.md)



#### `<code>spider_local_lock_table</code>`


* Description: Whether to push [LOCK TABLES](../../sql-statements-and-structure/sql-statements/transactions/lock-tables.md) statements down to the remote server.

  * `<code>0</code>` Transmitted.
  * `<code>1</code>` Not transmitted.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>0</code>`



#### `<code>spider_lock_exchange</code>`


* Description: 
Whether to convert [SELECT... LOCK IN SHARE MODE](../../sql-statements-and-structure/sql-statements/data-manipulation/selecting-data/lock-in-share-mode.md) and [SELECT... FOR UPDATE](../../sql-statements-and-structure/sql-statements/data-manipulation/selecting-data/for-update.md) statements into a [LOCK TABLE](../../sql-statements-and-structure/sql-statements/transactions/lock-tables.md) statement.

  * `<code>0</code>` Not converted.
  * `<code>1</code>` Converted.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>0</code>`



#### `<code>spider_log_result_error_with_sql</code>`


* Description: How to log SQL statements with result errors.

  * `<code>0</code>` No log
  * `<code>1</code>` Log error
  * `<code>2</code>` Log warning summary
  * `<code>3</code>` Log warning
  * `<code>4</code>` Log info (Added in [MariaDB 10.5.4](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1054-release-notes.md))
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>0</code>`
* Range: `<code>0</code>` to `<code>4</code>`



#### `<code>spider_log_result_errors</code>`


* Description: Log results from data nodes to the Spider node in the [Error Log](../../../server-management/server-monitoring-logs/error-log.md). Performs no logging by default.

  * `<code>0</code>` : Logs no errors from data nodes.
  * `<code>1</code>` : Logs errors from data nodes.
  * `<code>2</code>` : Logs errors from data nodes, as well as warning summaries.
  * `<code>3</code>` : Logs errors from data nodes, as well as warning summaries and details.
  * `<code>4</code>` : Logs errors from data nodes, as well as warning summaries and details, and result summaries.
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>0</code>`
* Range: `<code>0</code>` to `<code>4</code>`



#### `<code>spider_low_mem_read</code>`


* Description: Whether to use low memory mode when executing queries issued internally to remote servers that return result-sets.

  * `<code>-1</code>` Falls back to the default value, if the [table parameter](spider-table-parameters.md) is not set.
  * `<code>0</code>` Doesn't use low memory mode.
  * `<code>1</code>` Uses low memory mode.
* Data Type: `<code>numeric</code>`
* Default Session Value: `<code>1</code>`
* Default Table Value: `<code>1</code>`
* Range: `<code>-1</code>` to `<code>1</code>`



#### `<code>spider_max_connections</code>`


* Description: Maximum number of connections from Spider to a remote MariaDB servers. Defaults to `<code>0</code>`, which is no limit.
* Command-line: `<code>--spider-max-connections</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Session Value: `<code>0</code>`
* Range: `<code>0</code>` to `<code>99999</code>`
* Introduced: [MariaDB 10.3.3](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1033-release-notes.md)



#### `<code>spider_max_order</code>`


* Description: Maximum number of columns for `<code>ORDER BY</code>` operations.

  * `<code>-1</code>` The [table parameter](spider-table-parameters.md) is adopted.
  * `<code>0</code>` and greater: Maximum number of columns.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Session Value: `<code>32767</code>`
* Default Table Value: `<code>32767</code>`
* Range: `<code>-1</code>` to `<code>32767</code>`
* DSN Parameter Name: `<code>mod</code>`



#### `<code>spider_multi_split_read</code>`


* Description: 
Whether to divide a statement into multiple SQL statements sent to the remote backend server when the optimizer resolves range retrievals to multiple conditions.

  * `<code>-1</code>` Falls back to the default value, if the [table parameter](spider-table-parameters.md) is not set.
  * `<code>0</code>` Doesn't divide statements.
  * `<code>1</code>` Divides statements.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Session Value: `<code>100</code>`
* Default Table Value: `<code>100</code>`
* Range: `<code>-1</code>` to `<code>2147483647</code>`
* DSN Parameter Name: `<code>msr</code>`



#### `<code>spider_net_read_timeout</code>`


* Description: TCP timeout in seconds to declare remote backend servers unresponsive when reading from a connection. Change for high latency networks.

  * `<code>-1</code>` Falls back to the default value, if the [table parameter](spider-table-parameters.md) is not set.
  * `<code>0</code>` Less than 1 second timeout.
  * `<code>1</code>` and greater: Timeout in seconds.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Session Value: `<code>600</code>`
* Default Table Value: `<code>600</code>`
* Range: `<code>-1</code>` to `<code>2147483647</code>`
* DSN Parameter Name: `<code>nrt</code>`



#### `<code>spider_net_write_timeout</code>`


* Description: TCP timeout in seconds to declare remote backend servers unresponsive when writing to a connection. Change for high latency networks.

  * `<code>-1</code>` The [table parameter](spider-table-parameters.md) is adopted.
  * `<code>0</code>` Less than 1 second timeout.
  * `<code>1</code>` and more: Timeout in seconds.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Session Value: `<code>600</code>`
* Default Table Value: `<code>600</code>`
* Range: `<code>-1</code>` to `<code>2147483647</code>`
* DSN Parameter Name: `<code>nwt</code>`



#### `<code>spider_ping_interval_at_trx_start</code>`


* Description: Resets the connection with keepalive timeout in seconds by sending a ping. 

  * `<code>0</code>` At every transaction.
  * `<code>1</code>` and greater: Number of seconds.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>3600</code>`
* Range: `<code>0</code>` to `<code>2147483647</code>`



#### `<code>spider_quick_mode</code>`


* Description: Sets the backend query buffering to cache on the remote backend server or in the local buffer.

  * `<code>-1</code>` Falls back to the default value, if the [table parameter](spider-table-parameters.md) is not set.
  * `<code>0</code>` Local buffering, it acquires records collectively with `<code>store_result</code>`.
  * `<code>1</code>` Remote buffering, it acquires records one by one. Interrupts don't wait and recovery on context switch back.
  * `<code>2</code>` Remote buffering, it acquires records one by one. Interrupts wait to the end of the acquisition.
  * `<code>3</code>` Local buffering, uses a temporary table on disk when the result-set is greater than the value of the [spider_quick_page_size](#spider_quick_page_size) system variable.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Session Value: `<code>3</code>`
* Default Table Value: `<code>3</code>`
* Range: `<code>-1</code>` to `<code>3</code>`
* DSN Parameter Name: `<code>qmd</code>`



#### `<code>spider_quick_page_byte</code>`


* Description: Memory limit by size in bytes in a page when acquired record by record.

  * `<code>-1</code>` The [table parameter](spider-table-parameters.md) is used. When quick_mode is 1 or 2, Spider stores at least 1 record even if quick_page_byte is smaller than 1 record. When quick_mode is 3, quick_page_byte is used for judging using temporary tables. That is given priority when spider_quick_page_byte is set.
  * `<code>0</code>` or greater: Memory limit.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Session Value: `<code>10485760</code>`
* Range: `<code>-1</code>` to `<code>9223372036854775807</code>`
* Introduced: [MariaDB 10.4.3](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-4-series/mariadb-1043-release-notes.md), [MariaDB 10.3.13](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-10313-release-notes.md)



#### `<code>spider_quick_page_size</code>`


* Description: Number of records in a page when acquired record by record. 

  * `<code>-1</code>` The [table parameter](spider-table-parameters.md) is adopted.
  * `<code>0</code>` or greater: Number of records.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Session Value: `<code>1024</code>` (>=[MariaDB 10.7](../../../../release-notes/mariadb-community-server/what-is-mariadb-107.md)), `<code>-1</code>` (<= [MariaDB 10.6](../../../../release-notes/mariadb-community-server/what-is-mariadb-106.md))
* Default Table Value: `<code>100</code>`
* Range: `<code>-1</code>` to `<code>9223372036854775807</code>`
* DSN Parameter Name: `<code>qps</code>`



#### `<code>spider_read_only_mode</code>`


* Description: Whether to allow writes on Spider tables. 

  * `<code>-1</code>` Falls back to the default value, if the [table parameter](spider-table-parameters.md) is not set.
  * `<code>0</code>` Allows writes to Spider tables.
  * `<code>1</code>` Makes tables read- only.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Session Value: `<code>0</code>` (>=[MariaDB 10.7](../../../../release-notes/mariadb-community-server/what-is-mariadb-107.md)), `<code>-1</code>` (<= [MariaDB 10.6](../../../../release-notes/mariadb-community-server/what-is-mariadb-106.md))
* Default Table Value: `<code>0</code>`
* Range: `<code>-1</code>` to `<code>1</code>`
* DSN Parameter Name: `<code>rom</code>`



#### `<code>spider_remote_access_charset</code>`


* Description: Forces the specified session [character set](../../data-types/string-data-types/character-sets/README.md) when connecting to the backend server. This can improve connection time performance.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>string</code>`
* Default Session Value: `<code>null</code>`



#### `<code>spider_remote_autocommit</code>`


* Description: Sets the auto-commit mode when connecting to backend servers. This can improve connection time performance.

  * `<code>-1</code>` Doesn't change the auto-commit mode.
  * `<code>0</code>` Sets the auto-commit mode to `<code>0</code>`.
  * `<code>1</code>` Sets the auto-commit mode to `<code>1</code>`.
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Session Value: `<code>-1</code>`
* Range: `<code>-1</code>` to `<code>1</code>`



#### `<code>spider_remote_default_database</code>`


* Description: Sets the local default database when connecting to backend servers. This can improve connection time performance.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>string</code>`
* Default Session Value: Empty string



#### `<code>spider_remote_sql_log_off</code>`


* Description: Sets the [sql_log_off](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#sql_log_off) system variable to use when connecting to backend servers.

  * `<code>-1</code>` Doesn't set the value.
  * `<code>0</code>` Doesn't log Spider SQL statements to remote backend servers.
  * `<code>1</code>` Logs SQL statements on remote backend
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Session Value: `<code>-1</code>`
* Range: `<code>-1</code>` to `<code>1</code>`



#### `<code>spider_remote_time_zone</code>`


* Description: Forces the specified [time zone](../../data-types/string-data-types/character-sets/internationalization-and-localization/time-zones.md) setting when connecting to backend servers. 
This can improve connection performance when you know the time zone.
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>string</code>`
* Default Session Value: `<code>null</code>`



#### `<code>spider_remote_trx_isolation</code>`


* Description: Sets the [Transaction Isolation Level](../../sql-statements-and-structure/sql-statements/transactions/set-transaction.md#isolation-levels) when connecting to the backend server. 

  * `<code>-1</code>` Doesn't set the Isolation Level.
  * `<code>0</code>` Sets to the `<code>READ UNCOMMITTED</code>` level.
  * `<code>1</code>` Sets to the `<code>READ COMMITTED</code>` level.
  * `<code>2</code>` Sets to the `<code>REPEATABLE READ</code>` level.
  * `<code>3</code>` Sets to the `<code>SERIALIZABLE</code>` level.
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Session Value: `<code>-1</code>`
* Range: `<code>-1</code>` to `<code>3</code>`



#### `<code>spider_remote_wait_timeout</code>`


* Description: Wait timeout in seconds on remote server. `<code>-1</code>` means not set.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>-1</code>`
* Range: `<code>-1</code>` to `<code>2147483647</code>`
* Introduced: [MariaDB 10.4.5](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-4-series/mariadb-1045-release-notes.md)



#### `<code>spider_reset_sql_alloc</code>`


* Description: Resets the per connection SQL buffer after an SQL statement executes.

  * `<code>-1</code>` Falls back to the default value, if the [table parameter](spider-table-parameters.md) is not set.
  * `<code>0</code>` Doesn't reset.
  * `<code>1</code>` Resets.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Session Value: `<code>1</code>`
* Default Table Value: `<code>1</code>`
* Range: `<code>-1</code>` to `<code>1</code>`
* DSN Parameter Name: `<code>rsa</code>`



#### `<code>spider_same_server_link</code>`


* Description: Enables the linking of a table to the same local instance.

  * `<code>0</code>` Disables linking.
  * `<code>1</code>` Enables linking.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Session Value: `<code>OFF</code>`



#### `<code>spider_second_read</code>`


* Description: Number of second read records on the backend server when the first records are found from the first read. Spider continues scanning a range, adding a `<code>LIMIT</code>` using the [spider_first_read](#spider_first_read) and [spider_second_read](#spider_second_read) variables.

  * `<code>-1</code>` Falls back to the default value, if the [table parameter](spider-table-parameters.md) is not set.
  * `<code>0</code>` Usually retrieves records.
  * `<code>1</code>` and greater: Number of records.
* Scope: Global, Session
* Dynamic: Yes
* Default Session Value: `<code>0</code>`
* Default Table Value: `<code>0</code>`
* Range: `<code>-1</code>` to `<code>9223372036854775807</code>`
* DSN Parameter Name: `<code>srd</code>`



#### `<code>spider_select_column_mode</code>`


* Description: Mode for column retrieval from remote backend server.

  * `<code>-1</code>` Falls back to the default value, if the [table parameter](spider-table-parameters.md) is not set.
  * `<code>0</code>` Uses index columns when the `<code>SELECT</code>` statement can resolve with an index, otherwise uses all columns.
  * `<code>1</code>` Uses all columns judged necessary to resolve the query.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Session Value: `<code>1</code>`
* Default Table Value: `<code>1</code>`
* Range: `<code>-1</code>` to `<code>1</code>`
* DSN Parameter Name: `<code>scm</code>`



#### `<code>spider_selupd_lock_mode</code>`


* Description: Local lock mode on `<code>INSERT SELECT</code>`.

  * `<code>-1</code>` Falls back to the default value, if the [table parameter](spider-table-parameters.md) is not set.
  * `<code>0</code>` Takes no locks.
  * `<code>1</code>` Takes shared locks.
  * `<code>2</code>` Takes exclusive locks.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Session Value: `<code>1</code>`
* Default Table Value: `<code>1</code>`
* Range: `<code>-1</code>` to `<code>2</code>`
* DSN Parameter Name: `<code>slm#</code>`



#### `<code>spider_semi_split_read</code>`


* Description: 
Whether to use chunk retrieval with offset and limit parameters on SQL statements sent to the remote backend server when using the [spider_split_read](#spider_split_read) system variable.

  * `<code>-1</code>` Falls back to the default value, if the [table parameter](spider-table-parameters.md) is not set.
  * `<code>0</code>` Doesn't use chunk retrieval.
  * `<code>1 or more </code>` Uses chunk retrieval.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Session Value: `<code>2</code>`
* Default Table Value: `<code>2</code>`
* Range: `<code>-1</code>` to `<code>2147483647</code>`
* DSN Parameter Name: `<code>ssr#</code>`



#### `<code>spider_semi_split_read_limit</code>`


* Description: Sets the limit value for the [spider_semi_split_read](#spider_semi_split_read) system variable.

  * `<code>-1</code>` Falls back to the default value, if the [table parameter](spider-table-parameters.md) is not set.
  * `<code>0</code>` or more: The limit value.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Session Value: `<code>9223372036854775807</code>`
* Default Table Value: `<code>9223372036854775807</code>`
* Range: `<code>-1</code>` to `<code>9223372036854775807</code>`
* DSN Parameter Name: `<code>ssl#</code>`



#### `<code>spider_semi_table_lock</code>`


* Description: Enables semi-table locking. This adds a [LOCK TABLES](../../sql-statements-and-structure/sql-statements/transactions/lock-tables.md) statement to SQL executions sent to the remote backend server when using non-transactional storage engines to preserve consistency between roundtrips.

  * `<code>0</code>` Disables semi-table locking.
  * `<code>1</code>` Enables semi-table locking.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Session Value: `<code>0</code>` (>=[MariaDB 10.8](../../../../release-notes/mariadb-community-server/what-is-mariadb-108.md)), `<code>1</code>` (<= [MariaDB 10.7](../../../../release-notes/mariadb-community-server/what-is-mariadb-107.md))
* Range: `<code>0</code>` to `<code>1</code>`
* DSN Parameter Name: `<code>stl#</code>`



#### `<code>spider_semi_table_lock_connection</code>`


* Description: Whether to use multiple connections with semi-table locking. To enable semi-table locking, use the [spider_semi_table_lock](#spider_semi_table_lock) system variable.

  * `<code>-1</code>` Falls back to the default value, if the [table parameter](spider-table-parameters.md) is not set.
  * `<code>0</code>` Uses the same connection.
  * `<code>1</code>` Uses different connections.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Session Value: `<code>1</code>`
* Default Table Value: `<code>1</code>`
* Range: `<code>-1</code>` to `<code>1</code>`
* DSN Parameter Name: `<code>stc#</code>`



#### `<code>spider_semi_trx</code>`


* Description: Enables semi-transactions. This controls transaction consistency when an SQL statement is split into multiple statements issued to the backend servers. You can preserve or relax consistency as need. Spider encapsulates auto-committed SQL statements within a transaction on the remote backend server. When using `<code>READ COMMITTED</code>` or `<code>READ UNCOMMITTED</code>` [transaction isolation levels](../../sql-statements-and-structure/sql-statements/transactions/set-transaction.md#isolation-levels) to force consistency, set the [spider_semi_trx_isolation](#spider_semi_trx_isolation) system variable to `<code>2</code>`.

  * `<code>0</code>` Disables semi-transaction consistency.
  * `<code>1</code>` Enables semi-transaction consistency.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Session Value: `<code>ON</code>`



#### `<code>spider_semi_trx_isolation</code>`


* Description: Set consistency during range SQL execution when [spider_sync_trx_isolation](#spider_sync_trx_isolation) is 1

  * `<code>-1</code>` OFF
  * `<code>0</code>` READ UNCOMMITTED
  * `<code>1</code>` READ COMMITTED
  * `<code>2</code>` REPEATABLE READ
  * `<code>3</code>` SERIALIZABLE
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Session Value: `<code>-1</code>`
* Range: `<code>-1</code>` to `<code>3</code>`



#### `<code>spider_skip_default_condition</code>`


* Description: Whether to compute condition push downs.

  * `<code>-1</code>` Falls back to the default value, if the [table parameter](spider-table-parameters.md) is not set.
  * `<code>0</code>` Computes condition push downs.
  * `<code>1</code>` Doesn't compute condition push downs.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Session Value: `<code>0</code>`
* Default Table Value: `<code>0</code>`
* Range: `<code>-1</code>` to `<code>1</code>`
* DSN Parameter Name: `<code>sdc</code>`



#### `<code>spider_skip_parallel_search</code>`


* Description: Whether to skip parallel search by specific conditions.

  * `<code>-1</code>` :use [table parameter](spider-table-parameters.md)
  * `<code>0</code>` :not skip
  * `<code>1</code>` :skip parallel search if query is not SELECT statement
  * `<code>2</code>` :skip parallel search if query has SQL_NO_CACHE
  * `<code>3</code>` :1+2
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--spider-skip-parallel-search=#</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Session Value: `<code>0</code>`
* Range: `<code>-1</code>` to `<code>3</code>`
* Introduced: [MariaDB 10.3.3](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1033-release-notes.md)



#### `<code>spider_slave_trx_isolation</code>`


* Description: Transaction isolation level when Spider table is used by slave SQL thread.

  * `<code>-1</code>` off
  * `<code>0</code>` read uncommitted
  * `<code>1</code>` read committed
  * `<code>2</code>` repeatable read
  * `<code>3</code>` serializable
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--spider-slave-trx-isolation=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Session Value: `<code>-1</code>`
* Range: `<code>-1</code>` to `<code>3</code>`
* Introduced: [MariaDB 10.4.3](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-4-series/mariadb-1043-release-notes.md), [MariaDB 10.3.13](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-10313-release-notes.md)



#### `<code>spider_split_read</code>`


* Description: Number of records in chunk to retry the result when a range query is sent to remote backend servers.

  * `<code>-1</code>` Falls back to the default value, if the [table parameter](spider-table-parameters.md) is not set.
  * `<code>0</code>` or more: Number of records.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Session Value: `<code>9223372036854775807</code>`
* Default Table Value: `<code>9223372036854775807</code>`
* Range: `<code>-1</code>` to `<code>9223372036854775807</code>`
* DSN Parameter Name: `<code>srd</code>`



#### `<code>spider_store_last_crd</code>`


* Description: Whether to store last CRD result in the system table.

  * `<code>-1</code>` Use [table parameter](spider-table-parameters.md).
  * `<code>0</code>` Do not store last CRD result in the system table.
  * `<code>1</code>` Store last CRD result in the system table.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--spider-store-last-crd=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Session Value: `<code>1</code>`
* Range: `<code>-1</code>` to `<code>1</code>`
* Introduced: [MariaDB 10.3.3](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1033-release-notes.md)
* Deprecated: [MariaDB 10.7.4](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-7-series/mariadb-1074-release-notes.md), [MariaDB 10.8.3](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-8-series/mariadb-1083-release-notes.md)



#### `<code>spider_store_last_sts</code>`


* Description: Whether to store last STS result in the system table.

  * `<code>-1</code>` Use [table parameter](spider-table-parameters.md).
  * `<code>0</code>` Do not store last STS result in the system table.
  * `<code>1</code>` Store last STS result in the system table.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--spider-store-last-sts=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Session Value: `<code>1</code>`
* Range: `<code>-1</code>` to `<code>1</code>`
* Introduced: [MariaDB 10.3.3](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1033-release-notes.md)
* Deprecated: [MariaDB 10.7.4](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-7-series/mariadb-1074-release-notes.md), [MariaDB 10.8.3](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-8-series/mariadb-1083-release-notes.md)



#### `<code>spider_strict_group_by</code>`


* Description: 
Whether to use columns in select clause strictly for group by clause

  * `<code>-1</code>` Use the [table parameter](spider-table-parameters.md).
  * `<code>0</code>` Do not strictly use columns in select clause for group by clause
  * `<code>1</code>` Use columns in select clause strictly for group by clause
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Session Value: `<code>1</code>`
* Range: `<code>-1</code>` to `<code>1</code>`
* Introduced: [MariaDB 10.5.4](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1054-release-notes.md)



#### `<code>spider_sts_bg_mode</code>`


* Description: 
Enables background confirmation for table statistics. When background confirmation is enabled, Spider uses one thread per partition to maintain table status. Disable when the [spider_sts_interval](#spider_sts_interval) system variable is set to `<code>0</code>`, which causes Spider to always retrieve the latest information as need. It is effective, when the [spider_sts_interval](#spider_sts_interval) system variable is set to `<code>10</code>`.

  * `<code>-1</code>` Falls back to the default value, if the [table parameter](spider-table-parameters.md) is not set.
  * `<code>0</code>` Disables background confirmation.
  * `<code>1</code>` Enables background confirmation (create thread per table/partition).
  * `<code>2</code>` Enables background confirmation (use static threads). (from MariaDB 10.)
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Session Value: `<code>2</code>`
* Range: `<code>-1</code>` to `<code>2</code>`
* DSN Parameter Name: `<code>sbm</code>`



#### `<code>spider_sts_interval</code>`


* Description: Time interval of table statistics from the remote backend servers.

  * `<code>-1</code>` Falls back to the default value, if the [table parameter](spider-table-parameters.md) is not set.
  * `<code>0</code>` Retrieves the latest table statistics on request.
  * `<code>1</code>` or more: Interval in seconds for table state confirmation.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Session Value: `<code>10</code>`
* Default Table Value: `<code>10</code>`
* Range: `<code>-1</code>` to `<code>2147483647</code>`
* DSN Parameter Name: `<code>siv</code>`



#### `<code>spider_sts_mode</code>`


* Description: Table statistics mode.
Mode for table statistics. The [SHOW](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-procedure-code.md) command is used at the table level default.

  * `<code>-1,0</code>` Uses the [table parameter](spider-table-parameters.md).
  * `<code>1</code>` Uses the `<code>SHOW</code>` command.
  * `<code>2</code>` Uses the Information Schema.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Session Value: `<code>1</code>`
* Default Table Value: `<code>1</code>`
* Range: `<code>-1</code>` to `<code>2</code>`
* DSN Parameter Name: `<code>smd</code>`
* Deprecated: [MariaDB 10.7.4](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-7-series/mariadb-1074-release-notes.md), [MariaDB 10.8.3](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-8-series/mariadb-1083-release-notes.md)



#### `<code>spider_sts_sync</code>`


* Description: Synchronizes table statistics in partitioned tables.

  * `<code>-1</code>` Falls back to the default value, if the [table parameter](spider-table-parameters.md) is not set.
  * `<code>0</code>` Doesn't synchronize table statistics in partitioned tables.
  * `<code>1</code>` Synchronizes table state when opening a table, doesn't synchronize after opening.
  * `<code>2</code>` Synchronizes table statistics.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Session Value: `<code>0</code>`
* Default Table Value: `<code>0</code>`
* Range: `<code>-1</code>` to `<code>2</code>`
* DSN Parameter Name: `<code>ssy</code>`



#### `<code>spider_support_xa</code>`


* Description: XA Protocol for mirroring and for multi-shard transactions.

  * `<code>1</code>` Enables XA Protocol for these Spider operations.
  * `<code>0</code>` Disables XA Protocol for these Spider operations.
* Scope: Global
* Dynamic: No
* Data Type: `<code>boolean</code>`
* Default Table Value: `<code>1</code>`



#### `<code>spider_suppress_comment_ignored_warning</code>`


* Description: Whether to suppress warnings that table COMMENT or CONNECTION strings are ignored due to specified table options.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`
* Introduced: [MariaDB 11.3.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-0-release-notes.md)



#### `<code>spider_sync_autocommit</code>`


* Description: Whether to push down local auto-commits to remote backend servers.

  * `<code>OFF</code>` Pushes down local auto-commits.
  * `<code>ON</code>` Doesn't push down local auto-commits.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Session Value: `<code>ON</code>`



#### `<code>spider_sync_sql_mode</code>`


* Description: Whether to sync [sql_mode](../../../server-management/variables-and-modes/sql-mode.md).

  * `<code>OFF</code>` No sync
  * `<code>ON</code>` Sync
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>ON</code>`
* Introduced: [MariaDB 10.4.7](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-4-series/mariadb-1047-release-notes.md)



#### `<code>spider_sync_time_zone</code>`


* Description: Whether to push the local time zone down to remote backend servers.

  * `<code>OFF</code>` Doesn't synchronize time zones.
  * `<code>ON</code>` Synchronize time zones.
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Session Value: `<code>OFF</code>`
* Removed: [MariaDB 10.3.9](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1039-release-notes.md)



#### `<code>spider_sync_trx_isolation</code>`


* Description: Pushes local transaction isolation levels down to remote backend servers.

  * `<code>OFF</code>` Doesn't push down local isolation levels.
  * `<code>ON</code>` Pushes down local isolation levels.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Session Value: `<code>ON</code>`



#### `<code>spider_table_crd_thread_count</code>`


* Description: Static background thread count of table crd.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--spider-table-crd-thread-count=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value:

  * `<code>1</code>` (>= [MariaDB 10.4.33](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-4-series/mariadb-10-4-33-release-notes.md), [MariaDB 10.5.24](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-10-5-24-release-notes.md), [MariaDB 10.6.17](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-10-6-17-release-notes.md), [MariaDB 10.11.7](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-11-series/mariadb-10-11-7-release-notes.md), [MariaDB 11.0.5](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-0-series/mariadb-11-0-5-release-notes.md), [MariaDB 11.1.4](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-1-series/mariadb-11-1-4-release-notes.md), [MariaDB 11.2.3](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-2-series/mariadb-11-2-3-release-notes.md))
  * `<code>10</code>` (<= [MariaDB 10.4.32](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-4-series/mariadb-10-4-32-release-notes.md), [MariaDB 10.5.23](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-10-5-23-release-notes.md), [MariaDB 10.6.16](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-10-6-16-release-notes.md), [MariaDB 10.11.6](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-11-series/mariadb-10-11-6-release-notes.md), [MariaDB 11.0.4](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-0-series/mariadb-11-0-4-release-notes.md), [MariaDB 11.1.3](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-1-series/mariadb-11-1-3-release-notes.md), [MariaDB 11.2.2](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-2-series/mariadb-11-2-2-release-notes.md))
* Range: `<code>1</code>` to `<code>4294967295</code>`
* Deprecated: [MariaDB 11.7](../../../../release-notes/mariadb-community-server/what-is-mariadb-117.md)



#### `<code>spider_table_init_error_interval</code>`


* Description: Interval in seconds where the same error code is returned if table initialization fails. Use to protect against infinite loops in table links.
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>1</code>`
* Range: `<code>0</code>` to `<code>4294967295</code>`



#### `<code>spider_table_sts_thread_count</code>`


* Description: Static background thread count of table sts.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--spider-table-sts-thread-count=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`

  * `<code>1</code>` (>= [MariaDB 10.4.33](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-4-series/mariadb-10-4-33-release-notes.md), [MariaDB 10.5.24](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-10-5-24-release-notes.md), [MariaDB 10.6.17](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-10-6-17-release-notes.md), [MariaDB 10.11.7](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-11-series/mariadb-10-11-7-release-notes.md), [MariaDB 11.0.5](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-0-series/mariadb-11-0-5-release-notes.md), [MariaDB 11.1.4](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-1-series/mariadb-11-1-4-release-notes.md), [MariaDB 11.2.3](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-2-series/mariadb-11-2-3-release-notes.md))
  * `<code>10</code>` (<= [MariaDB 10.4.32](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-4-series/mariadb-10-4-32-release-notes.md), [MariaDB 10.5.23](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-10-5-23-release-notes.md), [MariaDB 10.6.16](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-10-6-16-release-notes.md), [MariaDB 10.11.6](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-11-series/mariadb-10-11-6-release-notes.md), [MariaDB 11.0.4](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-0-series/mariadb-11-0-4-release-notes.md), [MariaDB 11.1.3](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-1-series/mariadb-11-1-3-release-notes.md), [MariaDB 11.2.2](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-2-series/mariadb-11-2-2-release-notes.md))
* Range: `<code>1</code>` to `<code>4294967295</code>`
* Deprecated: [MariaDB 11.7](../../../../release-notes/mariadb-community-server/what-is-mariadb-117.md)



#### `<code>spider_udf_ct_bulk_insert_interval</code>`


* Description: Interval in milliseconds between bulk inserts at copying. For use with the UDF spider_copy_tables, which copies table data linked to a Spider table from the source server to destination server using bulk insert. If this interval is 0, it may cause higher write traffic.

  * `<code>-1</code>` Uses the UDF parameter.
  * `<code>0</code>` and more: Time in milliseconds.
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>10</code>`
* Default Table Value: `<code>10</code>`
* Range: `<code>-1</code>` to `<code>2147483647</code>`
* Deprecated: [MariaDB 10.7.4](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-7-series/mariadb-1074-release-notes.md), [MariaDB 10.8.3](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-8-series/mariadb-1083-release-notes.md)
* Removed: [MariaDB 10.10](../../../../release-notes/mariadb-community-server/what-is-mariadb-1010.md)



#### `<code>spider_udf_ct_bulk_insert_rows</code>`


* Description: Number of rows to insert at a time when copying during bulk inserts.

  * `<code>-1, 0</code>`: Uses the [table parameter](spider-table-parameters.md).
  * `<code>1</code>` and more: Number of rows
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>100</code>`
* Default Table Value: `<code>100</code>`
* Range: `<code>-1</code>` to `<code>9223372036854775807</code>`
* Deprecated: [MariaDB 10.7.4](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-7-series/mariadb-1074-release-notes.md), [MariaDB 10.8.3](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-8-series/mariadb-1083-release-notes.md)
* Removed: [MariaDB 10.10](../../../../release-notes/mariadb-community-server/what-is-mariadb-1010.md)



#### `<code>spider_udf_ds_bulk_insert_rows</code>`


* Description: Number of rows inserted at a time during bulk inserts when the result-set is stored in a temporary table on executing a UDF.

  * `<code>-1, 0</code>` Uses the UDF parameter.
  * `<code>1</code>` or more: Number of rows
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>3000</code>`
* Default Table Value: `<code>3000</code>`
* Range: `<code>-1</code>` to `<code>9223372036854775807</code>`
* Deprecated: [MariaDB 10.7.4](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-7-series/mariadb-1074-release-notes.md), [MariaDB 10.8.3](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-8-series/mariadb-1083-release-notes.md)
* Removed: [MariaDB 10.10](../../../../release-notes/mariadb-community-server/what-is-mariadb-1010.md)



#### `<code>spider_udf_ds_table_loop_mode</code>`


* Description: Whether to store the result-set in the same temporary table when the temporary table list count for UDF is less than the result-set count on UDF execution.

  * `<code>-1</code>` Falls back to the default value, if the [table parameter](spider-table-parameters.md) is not set.
  * `<code>0</code>` Drops records.
  * `<code>1</code>` Inserts the last table.
  * `<code>2</code>` Inserts the first table and loops again.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>0</code>`
* Range: `<code>-1</code>` to `<code>2</code>`
* Deprecated: [MariaDB 10.7.4](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-7-series/mariadb-1074-release-notes.md), [MariaDB 10.8.3](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-8-series/mariadb-1083-release-notes.md)
* Removed: [MariaDB 10.10](../../../../release-notes/mariadb-community-server/what-is-mariadb-1010.md)



#### `<code>spider_udf_ds_use_real_table</code>`


* Description: Whether to use real table for temporary table list.

  * `<code>-1</code>` Use UDF parameter.
  * `<code>0</code>` Do not use real table.
  * `<code>1</code>` Use real table.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>0</code>`
* Range: `<code>-1</code>` to `<code>1</code>`
* Deprecated: [MariaDB 10.7.4](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-7-series/mariadb-1074-release-notes.md), [MariaDB 10.8.3](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-8-series/mariadb-1083-release-notes.md)
* Removed: [MariaDB 10.10](../../../../release-notes/mariadb-community-server/what-is-mariadb-1010.md)



#### `<code>spider_udf_table_lock_mutex_count</code>`


* Description: Mutex count of table lock for Spider UDFs.
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value: `<code>20</code>`
* Range: `<code>1</code>` to `<code>4294967295</code>`
* Removed: [MariaDB 10.10](../../../../release-notes/mariadb-community-server/what-is-mariadb-1010.md)


#### `<code>spider_udf_table_mon_mutex_count</code>`


* Description: Mutex count of table mon for Spider UDFs.
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value: `<code>20</code>`
* Range: `<code>1</code>` to `<code>4294967295</code>`
* Removed: [MariaDB 10.10](../../../../release-notes/mariadb-community-server/what-is-mariadb-1010.md)



#### `<code>spider_use_all_conns_snapshot</code>`


* Description: Whether to pass `<code>START TRANSACTION WITH SNAPSHOT</code>` statements to all connections.

  * `<code>OFF</code>` Doesn't pass statement to all connections.
  * `<code>ON</code>` Passes statement to all connections.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Session Value: `<code>OFF</code>`



#### `<code>spider_use_cond_other_than_pk_for_update</code>`


* Description: Whether to use all conditions even if condition has a primary key. 

  * `<code>0</code>` Don't use all conditions
  * `<code>1</code>` Use all conditions
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>1</code>`
* Range: `<code>0</code>` to `<code>1</code>`
* Introduced: [MariaDB 10.3.13](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-10313-release-notes.md), [MariaDB 10.4.3](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-4-series/mariadb-1043-release-notes.md)



#### `<code>spider_use_consistent_snapshot</code>`


* Description: 
Whether to push a local `<code>START TRANSACTION WITH CONSISTENT</code>` statement down to remote backend servers.

  * `<code>OFF</code>` Doesn't push the local statement down.
  * `<code>ON</code>` Pushes the local statement down.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`



#### `<code>spider_use_default_database</code>`


* Description: Whether to use the default database.

  * `<code>OFF</code>` Doesn't use the default database.
  * `<code>ON</code>` Uses the default database.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>ON</code>`



#### `<code>spider_use_flash_logs</code>`


* Description: Whether to push [FLUSH LOGS](https://mariadb.com/kb/en/flush-logs) statements down to remote backend servers.

  * `<code>OFF</code>` Doesn't push the statement down.
  * `<code>ON</code>` Pushes the statement down.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`



#### `<code>spider_use_handler</code>`


* Description: Converts [HANDLER](../../sql-statements-and-structure/nosql/handler/handler-commands.md) SQL statements.
When the [spider_sync_trx_isolation](#spider_sync_trx_isolation) system variable is set to `<code>0</code>`, Spider disables [HANDLER](../../sql-statements-and-structure/nosql/handler/handler-commands.md) conversions to prevent use of the statement on the [SERIALIZABLE](../../sql-statements-and-structure/sql-statements/transactions/set-transaction.md#serializable) isolation level.

  * `<code>-1</code>` Falls back to the default value, if the [table parameter](spider-table-parameters.md) is not set.
  * `<code>0</code>` Converts [HANDLER](../../sql-statements-and-structure/nosql/handler/handler-commands.md) statements into [SELECT](../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/benchmarks-and-long-running-tests/benchmark-results/select-random-ranges-and-select-random-point.md) statements.
  * `<code>1</code>` Passes [HANDLER](../../sql-statements-and-structure/nosql/handler/handler-commands.md) to the remote backend server.
  * `<code>2</code>` Converts SQL statements to [HANDLER](../../sql-statements-and-structure/nosql/handler/handler-commands.md) statements.
  * `<code>3</code>` Converts SQL statements to [HANDLER](../../sql-statements-and-structure/nosql/handler/handler-commands.md) statements and [HANDLER](../../sql-statements-and-structure/nosql/handler/handler-commands.md) statements to SQL statements.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>0</code>`
* Default Table Value: `<code>0</code>`
* Range: `<code>-1</code>` to `<code>3</code>`
* DSN Parameter Name: `<code>uhd</code>`
* Deprecated: [MariaDB 10.7.4](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-7-series/mariadb-1074-release-notes.md), [MariaDB 10.8.3](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-8-series/mariadb-1083-release-notes.md)
* Removed: [MariaDB 10.10](../../../../release-notes/mariadb-community-server/what-is-mariadb-1010.md)



#### `<code>spider_use_pushdown_udf</code>`


* Description: 
When using a UDF function in a condition and the [engine_condition_pushdown](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#engine_condition_pushdown) system variable is set to `<code>1</code>`, whether to execute the UDF function locally or push it down.

  * `<code>-1</code>` Falls back to the default value, if the [table parameter](spider-table-parameters.md) is not set.
  * `<code>0</code>` Doesn't transmit the UDF
  * `<code>1</code>` Transmits the UDF.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>-1</code>`
* Default Table Value: `<code>1</code>`
* Range: `<code>-1</code>` to `<code>1</code>`
* DSN Parameter Name: `<code>upu</code>`



#### `<code>spider_use_snapshot_with_flush_tables</code>`


* Description: 
Whether to encapsulate [FLUSH LOGS](flush-logs) and [UNLOCK TABLES](../../sql-statements-and-structure/sql-statements/transactions/lock-tables.md) statements when `<code>START TRANSACTION WITH CONSISTENT</code>` and `<code>FLUSH TABLE WITH READ LOCK</code>` statements are sent to the remote backend servers.

  * `<code>0</code>` : No encapsulation.
  * `<code>1</code>` : Encapsulates, only when the [spider_use_all_conns_snapshot](#spider_use_all_conns_snapshot) system variable i set to `<code>1</code>`.
  * `<code>2</code>` : 
Synchronizes the snapshot using a [LOCK TABLES](../../sql-statements-and-structure/sql-statements/transactions/lock-tables.md) statement and [flush|FLUSH TABLES]] at the XA transaction level. This is only effective when the [spider_use_all_cons_snapshot](#spider_use_all_cons_snapshot) system variable is set to `<code>1</code>`.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>0</code>`
* Range: `<code>0</code>` to `<code>2</code>`



#### `<code>spider_use_table_charset</code>`


* Description: Whether to use the local table [character set](../../data-types/string-data-types/character-sets/README.md) for the remote backend server connections.

  * `<code>-1</code>` Falls back to the default value, if the [table parameter](spider-table-parameters.md) is not set.
  * `<code>0</code>` Use `<code>utf8</code>`.
  * `<code>1</code>` Uses the table character set.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>1</code>`
* Default Table Value: `<code>1</code>`
* Range: `<code>-1</code>` to `<code>1</code>`
* DSN Parameter Name: `<code>utc</code>`



#### `<code>spider_version</code>`


* Description: The current Spider version. Removed in [MariaDB 10.9.2](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-9-series/mariadb-1092-release-notes.md) when the Spider version number was matched with the server version.
* Scope: Global
* Dynamic: No
* Data Type: `<code>string</code>`
* Removed: [MariaDB 10.9.2](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-9-series/mariadb-1092-release-notes.md)



#### `<code>spider_wait_timeout</code>`


* Description: Wait timeout in seconds of setting to remote server. `<code>-1</code>` means not set.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>604800</code>`
* Range: `<code>-1</code>` to `<code>2147483647</code>`
* Introduced: [MariaDB 10.4.5](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-4-series/mariadb-1045-release-notes.md)



#### `<code>spider_xa_register_mode</code>`


* Description: Mode of XA transaction register into system table.

  * `<code>0</code>` Register all XA transactions
  * `<code>1</code>` Register only write XA transactions
* Command-line: `<code class="fixed" style="white-space:pre-wrap">--spider-xa-register-mode=#</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>1</code>`
* Range: `<code>0</code>` to `<code>1</code>`
* Introduced: [MariaDB 10.3.3](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1033-release-notes.md)
* Deprecated: [MariaDB 10.7.4](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-7-series/mariadb-1074-release-notes.md), [MariaDB 10.8.3](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-8-series/mariadb-1083-release-notes.md)

