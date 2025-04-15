
# Spider Table Parameters

When a table uses the [Spider](spider-functions/spider_copy_tables.md) storage engine, the following Spider table parameters can be set in the `<code>COMMENT</code>` clause of the [CREATE TABLE](../../sql-statements-and-structure/vectors/create-table-with-vectors.md) statement. Many Spider table parameters have corresponding system variables, so they can be set for all Spider tables on the node. For additional information, see the [Spider System Variables](spider-system-variables.md) page.


From [MariaDB 11.3](../../../../release-notes/mariadb-community-server/what-is-mariadb-113.md), many table parameters can be set using dedicated Spider table options, see the Table Option Name fields below. From [MariaDB 11.4](../../../../release-notes/mariadb-community-server/what-is-mariadb-114.md), using the `<code>COMMENT</code>` clause is deprecated, as well as table parameters that do not have corresponding table options.



#### `<code>access_balances</code>`


* Description: Connection load balancing integer weight.
* Default Table Value: `<code>0</code>`
* DSN Parameter Name: `<code>abl</code>`
* Deprecated: [MariaDB 11.4.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-4-series/mariadb-11-4-0-release-notes.md)


#### `<code>active_link_count</code>`


* Description: Number of active remote servers, for use in load balancing read connections
* Default Table Value: `<code>all backends</code>`
* DSN Parameter Name: `<code>alc</code>`
* Deprecated: [MariaDB 11.4.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-4-series/mariadb-11-4-0-release-notes.md)


#### `<code>auto_increment_mode</code>`


* Description: The table level value of [spider_auto_increment_mode](spider-system-variables.md#spider_auto_increment_mode)
* Table Option Name: `<code>AUTO_INCREMENT_MODE</code>`
* Table Option Introduced: [MariaDB 11.3.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-0-release-notes.md)


#### `<code>bgs_mode</code>`


* Description: The table level value of [spider_bgs_mode](spider-system-variables.md#spider_bgs_mode).
* Table Option Name: `<code>BGS_MODE</code>`
* Table Option Introduced: [MariaDB 11.3.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-0-release-notes.md)


#### `<code>bulk_size</code>`


* Description: The table level value of [spider_bulk_size](spider-system-variables.md#spider_bulk_size).
* Table Option Name: `<code>BULK_SIZE</code>`
* Table Option Introduced: [MariaDB 11.3.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-0-release-notes.md)


#### `<code>bulk_update_size</code>`


* Description: The table level value of [spider_bulk_update_size](spider-system-variables.md#spider_bulk_update_size).
* Table Option Name: `<code>BULK_UPDATE_SIZE</code>`
* Table Option Introduced: [MariaDB 11.3.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-0-release-notes.md)


#### `<code>casual_read</code>`


* Description:
* Default Table Value:
* DSN Parameter Name:
* Introduced: Spider 3.2
* Deprecated: [MariaDB 11.4.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-4-series/mariadb-11-4-0-release-notes.md)


#### `<code>connect_timeout</code>`


* Description: The table level value of [spider_connect_timeout](spider-system-variables.md#spider_connect_timeout).
* Table Option Name: `<code>CONNECT_TIMEOUT</code>`
* Table Option Introduced: [MariaDB 11.3.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-0-release-notes.md)


#### `<code>database</code>`


* Description: Database name for reference table that exists on remote backend server.
* Default Table Value: `<code>local table database</code>`
* DSN Parameter Name: `<code>database</code>`
* Table Option Name: `<code>REMOTE_DATABASE</code>`
* Table Option Introduced: [MariaDB 10.8.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-8-series/mariadb-10-8-0-release-notes.md)


#### `<code>default_file</code>`


* Description: Configuration file used when connecting to remote servers. When the `<code>[default_group](#default_group)</code>` table variable is set, this variable defaults to the values of the `<code>--defaults-extra-file</code>` or `<code>--defaults-file</code>` options. When the `<code>[default_group](#default_group)</code>` table variable is not set, it defaults to `<code>none</code>`.
* Default Table Value: `<code>none</code>`
* DSN Parameter Name: `<code>dff</code>`
* Table Option Name: `<code>DEFAULT_FILE</code>`
* Table Option Introduced: [MariaDB 11.3.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-0-release-notes.md)


#### `<code>default_group</code>`


* Description: Group name in configuration file used when connecting to remote servers.
* Default Table Value: `<code>none</code>`
* DSN Parameter Name: `<code>dfg</code>`
* Table Option Name: `<code>DEFAULT_GROUP</code>`
* Table Option Introduced: [MariaDB 11.3.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-0-release-notes.md)


#### `<code>delete_all_rows_type</code>`


* Description: The table level value of [spider_delete_all_rows_type](spider-system-variables.md#spider_delete_all_rows_type).
* Introduced: Spider 3.2
* Table Option Name: `<code>DELETE_ALL_ROWS_TYPE</code>`
* Table Option Introduced: [MariaDB 11.3.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-0-release-notes.md)


#### `<code>force_bulk_delete</code>`


* Description:
* Introduced: [MariaDB 10.0.5](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-1005-release-notes.md)
* Table Option Name: `<code>FORCE_BULK_DELETE</code>`
* Table Option Introduced: [MariaDB 11.3.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-0-release-notes.md)


#### `<code>force_bulk_update</code>`


* Description:
* Introduced: [MariaDB 10.0.5](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-1005-release-notes.md)
* Table Option Name: `<code>FORCE_BULK_UPDATE</code>`
* Table Option Introduced: [MariaDB 11.3.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-0-release-notes.md)


#### `<code>host</code>`


* Description: Host name of remote server.
* Default Table Value: `<code>localhost</code>`
* DSN Parameter Name: `<code>host</code>`
* Table Option Name: `<code>REMOTE_HOST</code>`
* Table Option Introduced: [MariaDB 11.3.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-0-release-notes.md)


#### `<code>idx000</code>`


* Description: When using an index on Spider tables for searching, Spider uses this hint to search the remote table. The remote table index is related to the Spider table index by this hint. The number represented by `<code>000</code>` is the index ID, which is the number of the index shown by the `<code>[SHOW CREATE TABLE](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-create-table.md)</code>` statement. `<code>000</code>` is the Primary Key. For instance, `<code>idx000 "force index(PRIMARY)"</code>` (in abbreviated format `<code>idx000 "f PRIMARY"</code>`).

  * `<code>f</code>` force index
  * `<code>u</code>` use index
  * `<code>ig</code>` ignore index
* Default Table Value: `<code>none</code>`
* Table Option Name: `<code>IDX</code>`
* Table Option Introduced: [MariaDB 11.3.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-0-release-notes.md)


#### `<code>link_status</code>`


* Description: Change status of the remote backend server link.

  * `<code>0</code>` Doesn't change status.
  * `<code>1</code>` Changes status to `<code>OK</code>`.
  * `<code>2</code>` Changes status to `<code>RECOVERY</code>`.
  * `<code>3</code>` Changes status to no more in group communication.
* Default Table Value: `<code>0</code>`
* DSN Parameter Name: `<code>lst</code>`
* Deprecated: [MariaDB 11.4.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-4-series/mariadb-11-4-0-release-notes.md)


#### `<code>monitoring_bg_interval</code>`


* Description: Interval of background monitoring in microseconds.
* Default Table Value: `<code>10000000</code>`
* DSN Parameter Name: `<code>mbi</code>`
* Deprecated: [MariaDB 11.4.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-4-series/mariadb-11-4-0-release-notes.md)


#### `<code>monitoring_bg_kind</code>`


* Description: Kind of background monitoring to use.

  * `<code>0</code>` Disables background monitoring.
  * `<code>1</code>` Monitors connection state.
  * `<code>2</code>` Monitors state of table without `<code>WHERE</code>` clause.
  * `<code>3</code>` Monitors state of table with `<code>WHERE</code>` clause (currently unsupported).
* Default Table Value: `<code>0</code>`
* DSN Parameter Name: `<code>mbk</code>`
* Deprecated: [MariaDB 11.4.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-4-series/mariadb-11-4-0-release-notes.md)


#### `<code>monitoring_kind</code>`


* Description: Kind of monitoring.

  * `<code>0</code>` Disables monitoring
  * `<code>1</code>` Monitors connection state.
  * `<code>2</code>` Monitors state of table without `<code>WHERE</code>` clause.
  * `<code>3</code>` Monitors state of table with `<code>WHERE</code>` clause (currently unsupported).
* Default Table Value: `<code>0</code>`
* DSN Parameter Name: `<code>mkd</code>`
* Deprecated: [MariaDB 11.4.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-4-series/mariadb-11-4-0-release-notes.md)


#### `<code>monitoring_limit</code>`


* Description: Limits the number of records in the monitoring table. This is only effective when Spider monitors the state of a table, which occurs when the `<code>[monitoring_kind](#monitoring_kind)</code>` table variable is set to a value greater than `<code>1</code>`.
* Default Table Value: `<code>1</code>`
* Range: `<code>0</code>` upwards
* DSN Parameter Name: `<code>mlt</code>`
* Deprecated: [MariaDB 11.4.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-4-series/mariadb-11-4-0-release-notes.md)


#### `<code>monitoring_server_id</code>`


* Description: Preferred monitoring `<code>@@server_id</code>` for each backend failure. You can use this to geo-localize backend servers and set the first Spider monitoring node to contact for failover. In the event that this monitor fails, other monitoring nodes are contacted. For multiple copy backends, you can set a lazy configuration with a single MSI instead of one per backend.
* Default Table Value: `<code>server_id</code>`
* DSN Parameter Name: `<code>msi</code>`
* Deprecated: [MariaDB 11.4.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-4-series/mariadb-11-4-0-release-notes.md)


#### `<code>multi_split_read</code>`


* Description: The table level value of [spider_multi_split_read](spider-system-variables.md#spider_multi_split_read).
* Table Option Name: `<code>MULTI_SPLIT_READ</code>`
* Table Option Introduced: [MariaDB 11.3.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-0-release-notes.md)


#### `<code>net_read_timeout</code>`


* Description: The table level value of [spider_net_read_timeout](spider-system-variables.md#spider_net_read_timeout).
* Table Option Name: `<code>NET_READ_TIMEOUT</code>`
* Table Option Introduced: [MariaDB 11.3.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-0-release-notes.md)


#### `<code>net_write_timeout</code>`


* Description: The table level value of [spider_net_write_timeout](spider-system-variables.md#spider_net_write_timeout).
* Table Option Name: `<code>NET_WRITE_TIMEOUT</code>`
* Table Option Introduced: [MariaDB 11.3.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-0-release-notes.md)


#### `<code>password</code>`


* Description: Remote server password.
* Default Table Value: `<code>none</code>`
* DSN Parameter Name: `<code>password</code>`
* Table Option Name: `<code>REMOTE_PASSWORD</code>`
* Table Option Introduced: [MariaDB 11.3.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-0-release-notes.md)


#### `<code>port</code>`


* Description: Remote server port.
* Default Table Value: `<code>3306</code>`
* DSN Parameter Name: `<code>port</code>`
* Table Option Name: `<code>REMOTE_PORT</code>`
* Table Option Introduced: [MariaDB 11.3.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-0-release-notes.md)


#### `<code>priority</code>`


* Description: Priority. Used to define the order of execution. For instance, Spider uses priority when deciding the order in which to lock tables on a remote server.
* Default Table Value: `<code>1000000</code>`
* DSN Parameter Name: `<code>prt</code>`
* Table Option Name: `<code>PRIORITY</code>`
* Table Option Introduced: [MariaDB 11.3.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-0-release-notes.md)


#### `<code>query_cache</code>`


* Description: Uses the option for the [Query Cache](../../plugins/other-plugins/query-cache-information-plugin.md) when issuing `<code>[SELECT](../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/benchmarks-and-long-running-tests/benchmark-results/select-random-ranges-and-select-random-point.md)</code>` statements to the remote server.

  * `<code>0</code>` No option used.
  * `<code>1</code>` Uses the `<code>[SQL_CACHE](../../sql-statements-and-structure/sql-statements/data-manipulation/selecting-data/optimizer-hints.md#sql_cache-sql_no_cache)</code>` option.
  * `<code>2</code>` Uses the `<code>[SQL_NO_CACHE](../../sql-statements-and-structure/sql-statements/data-manipulation/selecting-data/optimizer-hints.md#sql_cache-sql_no_cache)</code>` option.
* Default Table Value: `<code>0</code>`
* DSN Parameter Name: `<code>qch</code>`
* Table Option Name: `<code>QUERY_CACHE</code>`
* Table Option Introduced: [MariaDB 11.3.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-0-release-notes.md)


#### `<code>query_cache_sync</code>`


* Description: A two-bit bitmap. Whether to pass the option for the [Query Cache](../../plugins/other-plugins/query-cache-information-plugin.md) (if any) when issuing `<code>[SELECT](../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/benchmarks-and-long-running-tests/benchmark-results/select-random-ranges-and-select-random-point.md)</code>` statements to the remote server.

  * `<code>0</code>` No option passed.
  * `<code>1</code>` Passes the `<code>[SQL_CACHE](../../sql-statements-and-structure/sql-statements/data-manipulation/selecting-data/optimizer-hints.md#sql_cache-sql_no_cache)</code>` option, if specified in the query to the spider table.
  * `<code>2</code>` Passes the `<code>[SQL_NO_CACHE](../../sql-statements-and-structure/sql-statements/data-manipulation/selecting-data/optimizer-hints.md#sql_cache-sql_no_cache)</code>` option, if specified in the query to the spider table.
  * `<code>3</code>` Passes both the `<code>[SQL_CACHE](../../sql-statements-and-structure/sql-statements/data-manipulation/selecting-data/optimizer-hints.md#sql_cache-sql_no_cache)</code>` option and the `<code>[SQL_NO_CACHE](../../sql-statements-and-structure/sql-statements/data-manipulation/selecting-data/optimizer-hints.md#sql_cache-sql_no_cache)</code>` option, if specified in the query to the spider table.
* Default Table Value: `<code>3</code>`
* Table Option Name: `<code>QUERY_CACHE_SYNC</code>`
* Table Option Introduced: [MariaDB 11.3.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-0-release-notes.md)


#### `<code>read_rate</code>`


* Description: Rate used to calculate the amount of time Spider requires when executing index scans.
* Default Table Value: `<code>0.0002</code>`
* DSN Parameter Name: `<code>rrt</code>`
* Deprecated: [MariaDB 11.4.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-4-series/mariadb-11-4-0-release-notes.md)


#### `<code>scan_rate</code>`


* Description: Rate used to calculate the amount of time Spider requires when scanning tables.
* Default Table Value: `<code> 0.0001</code>`
* DSN Parameter Name: `<code>srt</code>`
* Deprecated: [MariaDB 11.4.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-4-series/mariadb-11-4-0-release-notes.md)


#### `<code>server</code>`


* Description: Server name. Used when generating connection information with `<code>[CREATE SERVER](../../sql-statements-and-structure/sql-statements/data-definition/create/create-server.md)</code>` statements.
* Default Table Value: `<code>none</code>`
* DSN Parameter Name: `<code>srv</code>`
* Table Option Name: `<code>REMOTE_SERVER</code>`
* Table Option Introduced: [MariaDB 10.8.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-8-series/mariadb-10-8-0-release-notes.md)


#### `<code>skip_parallel_search</code>`


* Description: The table level value of [spider_skip_parallel_search](spider-system-variables.md#spider_skip_parallel_search).
* Table Option Name: `<code>SKIP_PARALLEL_SEARCH</code>`
* Table Option Introduced: [MariaDB 11.3.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-0-release-notes.md)


#### `<code>socket</code>`


* Description: Remote server socket.
* Default Table Value: `<code>none</code>`
* DSN Parameter Name: `<code>socket</code>`
* Table Option Name: `<code>REMOTE_SOCKET</code>`
* Table Option Introduced: [MariaDB 11.3.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-0-release-notes.md)


#### `<code>ssl_ca</code>`


* Description: Path to the Certificate Authority file.
* Default Table Value: `<code>none</code>`
* DSN Parameter Name: `<code>sca</code>`
* Table Option Name: `<code>SSL_CA</code>`
* Table Option Introduced: [MariaDB 11.3.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-0-release-notes.md)


#### `<code>ssl_capath</code>`


* Description: Path to directory containing trusted TLS CA certificates in PEM format.
* Default Table Value: `<code>none</code>`
* DSN Parameter Name: `<code>scp</code>`
* Table Option Name: `<code>SSL_CAPATH</code>`
* Table Option Introduced: [MariaDB 11.3.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-0-release-notes.md)


#### `<code>ssl_cert</code>`


* Description: Path to the certificate file.
* Default Table Value: `<code>none</code>`
* DSN Parameter Name: `<code>scr</code>`
* Table Option Name: `<code>SSL_CERT</code>`
* Table Option Introduced: [MariaDB 11.3.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-0-release-notes.md)


#### `<code>ssl_cipher</code>`


* Description: List of allowed ciphers to use with [TLS encryption](../../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/secure-connections-overview.md).
* Default Table Value: `<code>none</code>`
* DSN Parameter Name: `<code>sch</code>`
* Table Option Name: `<code>SSL_CIPHER</code>`
* Table Option Introduced: [MariaDB 11.3.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-0-release-notes.md)


#### `<code>ssl_key</code>`


* Description: Path to the key file.
* Default Table Value: `<code>none</code>`
* DSN Parameter Name: `<code>sky</code>`
* Table Option Name: `<code>SSL_KEY</code>`
* Table Option Introduced: [MariaDB 11.3.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-0-release-notes.md)


#### `<code>ssl_verify_server_cert</code>`


* Description: Enables verification of the server's Common Name value in the certificate against the host name used when connecting to the server.

  * `<code>0</code>` Disables verification.
  * `<code>1</code>` Enables verification.
* Default Table Value: `<code>0</code>`
* DSN Parameter Name: `<code>svc</code>`
* Table Option Name: `<code>SSL_VSC</code>`
* Table Option Introduced: [MariaDB 11.3.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-0-release-notes.md)


#### `<code>table</code>`


* Description: Destination table name.
* Default Table Value: `<code>Same table name</code>`
* DSN Parameter Name: `<code>tbl</code>`
* Table Option Name: `<code>REMOTE_TABLE</code>`
* Table Option Introduced: [MariaDB 10.8.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-8-series/mariadb-10-8-0-release-notes.md)


#### `<code>table_count_mode</code>`


* Description: for setting table flags HA_STATS_RECORDS_IS_EXACT and HA_HAS_RECORDS.
* Default Table Value: `<code>0</code>`
* Table Option Name: `<code>TABLE_COUNT_MODE</code>`
* Table Option Introduced: [MariaDB 11.3.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-0-release-notes.md)


#### `<code>username</code>`


* Description: user name for the data node.
* Default Table Value: `<code>Same user name</code>`
* Table Option Name: `<code>REMOTE_USERNAME</code>`
* Table Option Introduced: [MariaDB 11.3.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-0-release-notes.md)


#### `<code>use_pushdown_udf</code>`


* Description: The table level value of [spider_use_pushdown_udf](spider-system-variables.md#spider_use_pushdown_udf).
* Table Option Name: `<code>USE_PUSHDOWN_UDF</code>`
* Table Option Introduced: [MariaDB 11.3.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-0-release-notes.md)


#### `<code>wrapper</code>`


* Description: wrapper for the data node.
* Table Option Name: `<code>WRAPPER</code>`
* Table Option Introduced: [MariaDB 11.3.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-0-release-notes.md)

