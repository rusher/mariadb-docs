
# Performance Schema System Variables




The following variables are used with MariaDB's [Performance Schema](performance-schema-tables/performance-schema-table_handles-table.md). See [Performance Schema Options](../../../../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md) for Performance Schema options that are not system variables. See [Server System Variables](../../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md) for a complete list of system variables and instructions on setting them.


See also the [Full list of MariaDB options, system and status variables](../../../../../../server-management/variables-and-modes/full-list-of-mariadb-options-system-and-status-variables.md).


#### `<code>performance_schema</code>`


* Description: If set to `<code>1</code>` (`<code>0</code>` is default), enables the Performance Schema
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--performance-schema=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`



#### `<code>performance_schema_accounts_size</code>`


* Description: Maximum number of rows in the [performance_schema.accounts](performance-schema-tables/performance-schema-accounts-table.md) table. If set to 0, the [Performance Schema](performance-schema-tables/performance-schema-table_handles-table.md) will not store statistics in the accounts table. Use `<code>-1</code>` (the default) for automated sizing.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--performance-schema-accounts-size=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value: `<code>-1</code>`
* Range: `<code>-1</code>` to `<code>1048576</code>`



#### `<code>performance_schema_digests_size</code>`


* Description: Maximum number of rows that can be stored in the [events_statements_summary_by_digest](performance-schema-tables/performance-schema-events_statements_summary_by_digest-table.md) table. `<code>0</code>` for disabling, `<code>-1</code>` (the default) for automated sizing.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--performance-schema-digests-size=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value: `<code>-1</code>`
* Range: `<code>-1</code>` to `<code>1048576</code>`



#### `<code>performance_schema_events_stages_history_long_size</code>`


* Description: Number of rows in the [events_stages_history_long](performance-schema-tables/performance-schema-events_stages_history_long-table.md) table. `<code>0</code>` for disabling, `<code>-1</code>` (the default) for automated sizing.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--performance-schema-events-stages-history-long-size=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value: `<code>-1</code>`
* Range: `<code>-1</code>` to `<code>1048576</code>`



#### `<code>performance_schema_events_stages_history_size</code>`


* Description: Number of rows per thread in the [events_stages_history](performance-schema-tables/performance-schema-events_stages_history-table.md) table. `<code>0</code>` for disabling, `<code>-1</code>` (the default) for automated sizing.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--performance-schema-events-stages-history-size=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value: `<code>-1</code>`
* Range: `<code>-1</code>` to `<code>1024</code>`



#### `<code>performance_schema_events_statements_history_long_size</code>`


* Description: Number of rows in the [events_statements_history_long](performance-schema-tables/performance-schema-events_statements_history_long-table.md) table. `<code>0</code>` for disabling, `<code>-1</code>` (the default) for automated sizing.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--performance-schema-events-statements-history-long-size=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value: `<code>-1</code>`
* Range: `<code>-1</code>` to `<code>1048576</code>`



#### `<code>performance_schema_events_statements_history_size</code>`


* Description: Number of rows per thread in the [events_statements_history](performance-schema-tables/performance-schema-events_statements_history-table.md) table. `<code>0</code>` for disabling, `<code>-1</code>` (the default) for automated sizing.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--performance-schema-events-statements-history-size=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value: `<code>-1</code>`
* Range: `<code>-1</code>` to `<code>1024</code>`



#### `<code>performance_schema_events_transactions_history_long_size</code>`


* Description: Number of rows in [events_transactions_history_long](performance-schema-tables/performance-schema-events_transactions_history_long-table.md) table. Use `<code>0</code>` to disable, `<code>-1</code>` for automated sizing.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--performance-schema-events-transactions-history-long-size=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value: `<code>-1</code>`
* Range: `<code>-1</code>` to `<code>1048576</code>`
* Introduced: [MariaDB 10.5.2](../../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1052-release-notes.md)



#### `<code>performance_schema_events_transactions_history_size</code>`


* Description:Number of rows per thread in [events_transactions_history](performance-schema-tables/performance-schema-events_transactions_history-table.md). Use 0 to disable, -1 for automated sizing.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--performance-schema-events-transactions-history-size=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value: `<code>-1</code>`
* Range: `<code>-1</code>` to `<code>1024</code>`
* Introduced: [MariaDB 10.5.2](../../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1052-release-notes.md)



#### `<code>performance_schema_events_waits_history_long_size</code>`


* Description: Number of rows contained in the [events_waits_history_long](performance-schema-tables/performance-schema-events_waits_history_long-table.md) table. `<code>0</code>` for disabling, `<code>-1</code>` (the default) for automated sizing.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--performance-schema-events-waits-history-long-size=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value: `<code>-1</code>`
* Range: `<code>-1</code>` to `<code>1048576</code>`



#### `<code>performance_schema_events_waits_history_size</code>`


* Description: Number of rows per thread contained in the [events_waits_history](performance-schema-tables/performance-schema-events_waits_history-table.md) table. `<code>0</code>` for disabling, `<code>-1</code>` (the default) for automated sizing.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--performance-schema-events-waits-history-size=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value: `<code>-1</code>`
* Range: `<code>-1</code>` to `<code>1024</code>`



#### `<code>performance_schema_hosts_size</code>`


* Description: Number of rows stored in the [hosts](performance-schema-tables/performance-schema-hosts-table.md) table. If set to zero, no connection statistics are kept for the hosts table. `<code>-1</code>` (the default) for automated sizing.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--performance-schema-hosts-size=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value: `<code>-1</code>`
* Range: `<code>-1</code>` to `<code>1048576</code>`



#### `<code>performance_schema_max_cond_classes</code>`


* Description: Specifies the maximum number of condition instruments.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--performance-schema-max-cond-classes=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value: `<code>90</code>` (>= [MariaDB 10.5.1](../../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1051-release-notes.md)), `<code>80</code>` (<= [MariaDB 10.5.0](../../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1050-release-notes.md))
* Range: `<code>0</code>` to `<code>256</code>`



#### `<code>performance_schema_max_cond_instances</code>`


* Description: Specifies the maximum number of instrumented condition objects. `<code>0</code>` for disabling, `<code>-1</code>` (the default) for automated sizing.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--performance-schema-max-cond-instances=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value: `<code>-1</code>`
* Range: `<code>-1</code>` to `<code>1048576</code>`



#### `<code>performance_schema_max_digest_length</code>`


* Description: Maximum length considered for digest text, when stored in performance_schema tables.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--performance-schema-max-digest-length=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value: `<code>1024</code>`
* Range: `<code>0</code>` to `<code>1048576</code>`



#### `<code>performance_schema_max_file_classes</code>`


* Description: Specifies the maximum number of file instruments.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--performance-schema-max-file-classes=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value:`<code>80</code>` (>= [MariaDB 10.5.2](../../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1052-release-notes.md)), `<code>50</code>` (<= [MariaDB 10.5.1](../../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1051-release-notes.md))
* Range: `<code>0</code>` to `<code>256</code>`



#### `<code>performance_schema_max_file_handles</code>`


* Description: Specifies the maximum number of opened file objects. Should always be higher than [open_files_limit](../../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#open_files_limit).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--performance-schema-max-file-handles=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value: `<code>32768</code>`
* Range: `<code>-1</code>` to `<code>32768</code>`



#### `<code>performance_schema_max_file_instances</code>`


* Description: Specifies the maximum number of instrumented file objects. `<code>0</code>` for disabling, `<code>-1</code>` (the default) for automated sizing.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--performance-schema-max-file-instances=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value: `<code>-1</code>`
* Range: `<code>-1</code>` to `<code>1048576</code>`



#### `<code>performance_schema_max_index_stat</code>`


* Description: Maximum number of index statistics for instrumented tables. Use 0 to disable, -1 for automated scaling.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--performance-schema-max-index-stat=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value: `<code>-1</code>`
* Range: `<code>-1</code>` to `<code>1048576</code>`
* Introduced: [MariaDB 10.5.2](../../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1052-release-notes.md)



#### `<code>performance_schema_max_memory_classes</code>`


* Description: Maximum number of memory pool instruments.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--performance-schema-max-memory-classes=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value: `<code>320</code>`
* Range: `<code>0</code>` to `<code>1024</code>`
* Introduced: [MariaDB 10.5.2](../../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1052-release-notes.md)



#### `<code>performance_schema_max_metadata_locks</code>`


* Description: Maximum number of [Performance Schema metadata locks](performance-schema-tables/performance-schema-metadata_locks-table.md). Use 0 to disable, -1 for automated scaling.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--performance-schema-max-metadata-locks=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value: `<code>-1</code>`
* Range: `<code>-1</code>` to `<code>104857600</code>`
* Introduced: [MariaDB 10.5.2](../../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1052-release-notes.md)



#### `<code>performance_schema_max_mutex_classes</code>`


* Description: Specifies the maximum number of mutex instruments.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--performance-schema-max-mutex-classes=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value: `<code>210</code>` (>= [MariaDB 10.5.2](../../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1052-release-notes.md)), `<code>200</code>` (<= [MariaDB 10.5.1](../../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1051-release-notes.md))
* Range: `<code>0</code>` to `<code>256</code>`



#### `<code>performance_schema_max_mutex_instances</code>`


* Description: Specifies the maximum number of instrumented mutex instances. `<code>0</code>` for disabling, `<code>-1</code>` (the default) for automated sizing.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--performance-schema-max-mutex-instances=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value:`<code>-1</code>`
* Range: `<code>-1</code>` to `<code>104857600</code>`



#### `<code>performance_schema_max_prepared_statement_instances</code>`


* Description: Maximum number of instrumented prepared statements. Use 0 to disable, -1 for automated scaling.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--performance-schema-max-prepared-statement-instances=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value: `<code>-1</code>`
* Range: `<code>-1</code>` to `<code>1048576</code>`
* Introduced: [MariaDB 10.5.2](../../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1052-release-notes.md)



#### `<code>performance_schema_max_program_instances</code>`


* Description: Maximum number of instrumented programs. Use 0 to disable, -1 for automated scaling.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--performance-schema-max-program-instances=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value: `<code>-1</code>`
* Range: `<code>-1</code>` to `<code>1048576</code>`
* Introduced: [MariaDB 10.5.2](../../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1052-release-notes.md)



#### `<code>performance_schema_max_rwlock_classes</code>`


* Description: Specifies the maximum number of rwlock instruments.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--performance-schema-max-rwlock-classes=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value: `<code>50</code>` (>= [MariaDB 10.5.2](../../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1052-release-notes.md)), `<code>40</code>` (<= [MariaDB 10.5.1](../../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1051-release-notes.md))
* Range: `<code>0</code>` to `<code>256</code>`



#### `<code>performance_schema_max_rwlock_instances</code>`


* Description: Specifies the maximum number of instrumented rwlock objects. `<code>0</code>` for disabling, `<code>-1</code>` (the default) for automated sizing.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--performance-schema-max-rwlock-instances=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value:`<code>-1</code>`
* Range: `<code>-1</code>` to `<code>104857600</code>`



#### `<code>performance_schema_max_socket_classes</code>`


* Description: Specifies the maximum number of socket instruments.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--performance-schema-max-socket-classes=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value: `<code>10</code>`
* Range: `<code>0</code>` to `<code>256</code>`



#### `<code>performance_schema_max_socket_instances</code>`


* Description: Specifies the maximum number of instrumented socket objects. `<code>0</code>` for disabling, `<code>-1</code>` (the default) for automated sizing.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--performance-schema-max-socket-instances=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value:`<code>-1</code>`
* Range: `<code>-1</code>` to `<code>1048576</code>`



#### `<code>performance_schema_max_sql_text_length</code>`


* Description: Maximum length of displayed sql text.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--performance-schema-max-sql-text-length=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value: `<code>1024</code>`
* Range: `<code>0</code>` to `<code>1048576</code>`
* Introduced: [MariaDB 10.5.2](../../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1052-release-notes.md)



#### `<code>performance_schema_max_stage_classes</code>`


* Description: Specifies the maximum number of stage instruments.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--performance-schema-max-stage-classes=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value: `<code>160</code>`
* Range: `<code>0</code>` to `<code>256</code>`



#### `<code>performance_schema_max_statement_classes</code>`


* Description: Specifies the maximum number of statement instruments. Automatically calculated at server build based on the number of available statements. Should be left as either autosized or disabled, as changing to any positive value has no benefit and will most likely allocate unnecessary memory. Setting to zero disables all statement instrumentation, and no memory will be allocated for this purpose.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--performance-schema-max-statement-classes=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value: Autosized (see description)
* Range: `<code>0</code>` to `<code>256</code>`



#### `<code>performance_schema_max_statement_stack</code>`


* Description: Number of rows per thread in EVENTS_STATEMENTS_CURRENT.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--performance-schema-max-statement-stack=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value: `<code>10</code>`
* Range: `<code>1</code>` to `<code>256</code>`
* Introduced: [MariaDB 10.5.2](../../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1052-release-notes.md)



#### `<code>performance_schema_max_table_handles</code>`


* Description: Specifies the maximum number of opened table objects. `<code>0</code>` for disabling, `<code>-1</code>` (the default) for automated sizing. See also the [Performance Schema table_handles table](performance-schema-tables/performance-schema-table_handles-table.md).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--performance-schema-max-table-handles=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value: `<code>-1</code>`
* Range: `<code>-1</code>` to `<code>1048576</code>`



#### `<code>performance_schema_max_table_instances</code>`


* Description: Specifies the maximum number of instrumented table objects. `<code>0</code>` for disabling, `<code>-1</code>` (the default) for automated sizing.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--performance-schema-max-table-instances=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value:`<code>-1</code>`
* Range: `<code>-1</code>` to `<code>1048576</code>`



#### `<code>performance_schema_max_table_lock_stat</code>`


* Description: Maximum number of lock statistics for instrumented tables. Use 0 to disable, -1 for automated scaling.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--performance-schema-max-table-lock-stat=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value: `<code>-1</code>`
* Range: `<code>-1</code>` to `<code>1048576</code>`
* Introduced: [MariaDB 10.5.2](../../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1052-release-notes.md)



#### `<code>performance_schema_max_thread_classes</code>`


* Description: Specifies the maximum number of thread instruments.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--performance-schema-max-thread-classes=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value: `<code>50</code>`
* Range: `<code>0</code>` to `<code>256</code>`



#### `<code>performance_schema_max_thread_instances</code>`


* Description: Specifies how many of the running server threads (see [max_connections](../../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#max_connections) and [max_delayed_threads](../../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#max_delayed_threads)) can be instrumented. Should be greater than the sum of max_connections and max_delayed_threads. `<code>0</code>` for disabling, `<code>-1</code>` (the default) for automated sizing.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--performance-schema-max-thread-instances=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value:`<code>-1</code>`
* Range: `<code>-1</code>` to `<code>1048576</code>`



#### `<code>performance_schema_session_connect_attrs_size</code>`


* Description: Per thread preallocated memory for holding connection attribute strings. Incremented if the strings are larger than the reserved space. `<code>0</code>` for disabling, `<code>-1</code>` (the default) for automated sizing.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--performance-schema-session-connect-attrs-size=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value: `<code>-1</code>`
* Range: `<code>-1</code>` to `<code>1048576</code>`



#### `<code>performance_schema_setup_actors_size</code>`


* Description: The maximum number of rows to store in the performance schema [setup_actors](performance-schema-tables/performance-schema-setup_actors-table.md) table. `<code>-1</code>` (from [MariaDB 10.5.2](../../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1052-release-notes.md)) denotes automated sizing.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--performance-schema-setup-actors-size=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value: `<code>-1</code>` (>= [MariaDB 10.5.2](../../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1052-release-notes.md)), `<code>100</code>` (<= [MariaDB 10.5.1](../../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1051-release-notes.md))
* Range: `<code>-1</code>` to `<code>1024</code>` (>= [MariaDB 10.5.2](../../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1052-release-notes.md)), `<code>0</code>` to `<code>1024</code>` (<= [MariaDB 10.5.1](../../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1051-release-notes.md))



#### `<code>performance_schema_setup_objects_size</code>`


* Description: The maximum number of rows that can be stored in the performance schema [setup_objects](performance-schema-tables/performance-schema-setup_objects-table.md) table. `<code>-1</code>` (from [MariaDB 10.5.2](../../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1052-release-notes.md)) denotes automated sizing.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--performance-schema-setup-objects-size=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value: `<code>-1</code>` (>= [MariaDB 10.5.2](../../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1052-release-notes.md)), `<code>100</code>` (<= [MariaDB 10.5.1](../../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1051-release-notes.md))
* Range: `<code>-1</code>` to `<code>1048576</code>` (>= [MariaDB 10.5.2](../../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1052-release-notes.md)), `<code>0</code>` to `<code>1048576</code>` (<= [MariaDB 10.5.1](../../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1051-release-notes.md))



#### `<code>performance_schema_users_size</code>`


* Description: Number of rows in the [performance_schema.users](performance-schema-tables/performance-schema-users-table.md) table. If set to 0, the [Performance Schema](performance-schema-tables/performance-schema-table_handles-table.md) will not store connection statistics in the users table. `<code>-1</code>` (the default) for automated sizing.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--performance-schema-users-size=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value: `<code>-1</code>`
* Range: `<code>-1</code>` to `<code>1048576</code>`


