
# Performance Schema System Variables




The following variables are used with MariaDB's [Performance Schema](README.md). See [Performance Schema Options](../../../../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md) for Performance Schema options that are not system variables. See [Server System Variables](../../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md) for a complete list of system variables and instructions on setting them.


See also the [Full list of MariaDB options, system and status variables](../../../../../../server-management/variables-and-modes/full-list-of-mariadb-options-system-and-status-variables.md).


#### `performance_schema`


* Description: If set to `1` (`0` is default), enables the Performance Schema
* Commandline: `--performance-schema=#`
* Scope: Global
* Dynamic: No
* Data Type: `boolean`
* Default Value: `OFF`



#### `performance_schema_accounts_size`


* Description: Maximum number of rows in the [performance_schema.accounts](performance-schema-tables/performance-schema-accounts-table.md) table. If set to 0, the [Performance Schema](README.md) will not store statistics in the accounts table. Use `-1` (the default) for automated sizing.
* Commandline: `--performance-schema-accounts-size=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `-1`
* Range: `-1` to `1048576`



#### `performance_schema_digests_size`


* Description: Maximum number of rows that can be stored in the [events_statements_summary_by_digest](performance-schema-tables/performance-schema-events_statements_summary_by_digest-table.md) table. `0` for disabling, `-1` (the default) for automated sizing.
* Commandline: `--performance-schema-digests-size=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `-1`
* Range: `-1` to `1048576`



#### `performance_schema_events_stages_history_long_size`


* Description: Number of rows in the [events_stages_history_long](performance-schema-tables/performance-schema-events_stages_history_long-table.md) table. `0` for disabling, `-1` (the default) for automated sizing.
* Commandline: `--performance-schema-events-stages-history-long-size=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `-1`
* Range: `-1` to `1048576`



#### `performance_schema_events_stages_history_size`


* Description: Number of rows per thread in the [events_stages_history](performance-schema-tables/performance-schema-events_stages_history-table.md) table. `0` for disabling, `-1` (the default) for automated sizing.
* Commandline: `--performance-schema-events-stages-history-size=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `-1`
* Range: `-1` to `1024`



#### `performance_schema_events_statements_history_long_size`


* Description: Number of rows in the [events_statements_history_long](performance-schema-tables/performance-schema-events_statements_history_long-table.md) table. `0` for disabling, `-1` (the default) for automated sizing.
* Commandline: `--performance-schema-events-statements-history-long-size=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `-1`
* Range: `-1` to `1048576`



#### `performance_schema_events_statements_history_size`


* Description: Number of rows per thread in the [events_statements_history](performance-schema-tables/performance-schema-events_statements_history-table.md) table. `0` for disabling, `-1` (the default) for automated sizing.
* Commandline: `--performance-schema-events-statements-history-size=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `-1`
* Range: `-1` to `1024`



#### `performance_schema_events_transactions_history_long_size`


* Description: Number of rows in [events_transactions_history_long](performance-schema-tables/performance-schema-events_transactions_history_long-table.md) table. Use `0` to disable, `-1` for automated sizing.
* Commandline: `--performance-schema-events-transactions-history-long-size=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `-1`
* Range: `-1` to `1048576`
* Introduced: [MariaDB 10.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-5-series/mariadb-1052-release-notes)



#### `performance_schema_events_transactions_history_size`


* Description:Number of rows per thread in [events_transactions_history](performance-schema-tables/performance-schema-events_transactions_history-table.md). Use 0 to disable, -1 for automated sizing.
* Commandline: `--performance-schema-events-transactions-history-size=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `-1`
* Range: `-1` to `1024`
* Introduced: [MariaDB 10.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-5-series/mariadb-1052-release-notes)



#### `performance_schema_events_waits_history_long_size`


* Description: Number of rows contained in the [events_waits_history_long](performance-schema-tables/performance-schema-events_waits_history_long-table.md) table. `0` for disabling, `-1` (the default) for automated sizing.
* Commandline: `--performance-schema-events-waits-history-long-size=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `-1`
* Range: `-1` to `1048576`



#### `performance_schema_events_waits_history_size`


* Description: Number of rows per thread contained in the [events_waits_history](performance-schema-tables/performance-schema-events_waits_history-table.md) table. `0` for disabling, `-1` (the default) for automated sizing.
* Commandline: `--performance-schema-events-waits-history-size=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `-1`
* Range: `-1` to `1024`



#### `performance_schema_hosts_size`


* Description: Number of rows stored in the [hosts](performance-schema-tables/performance-schema-hosts-table.md) table. If set to zero, no connection statistics are kept for the hosts table. `-1` (the default) for automated sizing.
* Commandline: `--performance-schema-hosts-size=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `-1`
* Range: `-1` to `1048576`



#### `performance_schema_max_cond_classes`


* Description: Specifies the maximum number of condition instruments.
* Commandline: `--performance-schema-max-cond-classes=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `90` (>= [MariaDB 10.5.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-5-series/mariadb-1051-release-notes)), `80` (<= [MariaDB 10.5.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-5-series/mariadb-1050-release-notes))
* Range: `0` to `256`



#### `performance_schema_max_cond_instances`


* Description: Specifies the maximum number of instrumented condition objects. `0` for disabling, `-1` (the default) for automated sizing.
* Commandline: `--performance-schema-max-cond-instances=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `-1`
* Range: `-1` to `1048576`



#### `performance_schema_max_digest_length`


* Description: Maximum length considered for digest text, when stored in performance_schema tables.
* Commandline: `--performance-schema-max-digest-length=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `1024`
* Range: `0` to `1048576`



#### `performance_schema_max_file_classes`


* Description: Specifies the maximum number of file instruments.
* Commandline: `--performance-schema-max-file-classes=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value:`80` (>= [MariaDB 10.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-5-series/mariadb-1052-release-notes)), `50` (<= [MariaDB 10.5.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-5-series/mariadb-1051-release-notes))
* Range: `0` to `256`



#### `performance_schema_max_file_handles`


* Description: Specifies the maximum number of opened file objects. Should always be higher than [open_files_limit](../../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#open_files_limit).
* Commandline: `--performance-schema-max-file-handles=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `32768`
* Range: `-1` to `32768`



#### `performance_schema_max_file_instances`


* Description: Specifies the maximum number of instrumented file objects. `0` for disabling, `-1` (the default) for automated sizing.
* Commandline: `--performance-schema-max-file-instances=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `-1`
* Range: `-1` to `1048576`



#### `performance_schema_max_index_stat`


* Description: Maximum number of index statistics for instrumented tables. Use 0 to disable, -1 for automated scaling.
* Commandline: `--performance-schema-max-index-stat=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `-1`
* Range: `-1` to `1048576`
* Introduced: [MariaDB 10.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-5-series/mariadb-1052-release-notes)



#### `performance_schema_max_memory_classes`


* Description: Maximum number of memory pool instruments.
* Commandline: `--performance-schema-max-memory-classes=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `320`
* Range: `0` to `1024`
* Introduced: [MariaDB 10.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-5-series/mariadb-1052-release-notes)



#### `performance_schema_max_metadata_locks`


* Description: Maximum number of [Performance Schema metadata locks](performance-schema-tables/performance-schema-metadata_locks-table.md). Use 0 to disable, -1 for automated scaling.
* Commandline: `--performance-schema-max-metadata-locks=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `-1`
* Range: `-1` to `104857600`
* Introduced: [MariaDB 10.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-5-series/mariadb-1052-release-notes)



#### `performance_schema_max_mutex_classes`


* Description: Specifies the maximum number of mutex instruments.
* Commandline: `--performance-schema-max-mutex-classes=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `210` (>= [MariaDB 10.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-5-series/mariadb-1052-release-notes)), `200` (<= [MariaDB 10.5.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-5-series/mariadb-1051-release-notes))
* Range: `0` to `256`



#### `performance_schema_max_mutex_instances`


* Description: Specifies the maximum number of instrumented mutex instances. `0` for disabling, `-1` (the default) for automated sizing.
* Commandline: `--performance-schema-max-mutex-instances=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value:`-1`
* Range: `-1` to `104857600`



#### `performance_schema_max_prepared_statement_instances`


* Description: Maximum number of instrumented prepared statements. Use 0 to disable, -1 for automated scaling.
* Commandline: `--performance-schema-max-prepared-statement-instances=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `-1`
* Range: `-1` to `1048576`
* Introduced: [MariaDB 10.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-5-series/mariadb-1052-release-notes)



#### `performance_schema_max_program_instances`


* Description: Maximum number of instrumented programs. Use 0 to disable, -1 for automated scaling.
* Commandline: `--performance-schema-max-program-instances=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `-1`
* Range: `-1` to `1048576`
* Introduced: [MariaDB 10.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-5-series/mariadb-1052-release-notes)



#### `performance_schema_max_rwlock_classes`


* Description: Specifies the maximum number of rwlock instruments.
* Commandline: `--performance-schema-max-rwlock-classes=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `50` (>= [MariaDB 10.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-5-series/mariadb-1052-release-notes)), `40` (<= [MariaDB 10.5.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-5-series/mariadb-1051-release-notes))
* Range: `0` to `256`



#### `performance_schema_max_rwlock_instances`


* Description: Specifies the maximum number of instrumented rwlock objects. `0` for disabling, `-1` (the default) for automated sizing.
* Commandline: `--performance-schema-max-rwlock-instances=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value:`-1`
* Range: `-1` to `104857600`



#### `performance_schema_max_socket_classes`


* Description: Specifies the maximum number of socket instruments.
* Commandline: `--performance-schema-max-socket-classes=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `10`
* Range: `0` to `256`



#### `performance_schema_max_socket_instances`


* Description: Specifies the maximum number of instrumented socket objects. `0` for disabling, `-1` (the default) for automated sizing.
* Commandline: `--performance-schema-max-socket-instances=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value:`-1`
* Range: `-1` to `1048576`



#### `performance_schema_max_sql_text_length`


* Description: Maximum length of displayed sql text.
* Commandline: `--performance-schema-max-sql-text-length=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `1024`
* Range: `0` to `1048576`
* Introduced: [MariaDB 10.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-5-series/mariadb-1052-release-notes)



#### `performance_schema_max_stage_classes`


* Description: Specifies the maximum number of stage instruments.
* Commandline: `--performance-schema-max-stage-classes=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `160`
* Range: `0` to `256`



#### `performance_schema_max_statement_classes`


* Description: Specifies the maximum number of statement instruments. Automatically calculated at server build based on the number of available statements. Should be left as either autosized or disabled, as changing to any positive value has no benefit and will most likely allocate unnecessary memory. Setting to zero disables all statement instrumentation, and no memory will be allocated for this purpose.
* Commandline: `--performance-schema-max-statement-classes=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: Autosized (see description)
* Range: `0` to `256`



#### `performance_schema_max_statement_stack`


* Description: Number of rows per thread in EVENTS_STATEMENTS_CURRENT.
* Commandline: `--performance-schema-max-statement-stack=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `10`
* Range: `1` to `256`
* Introduced: [MariaDB 10.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-5-series/mariadb-1052-release-notes)



#### `performance_schema_max_table_handles`


* Description: Specifies the maximum number of opened table objects. `0` for disabling, `-1` (the default) for automated sizing. See also the [Performance Schema table_handles table](performance-schema-tables/performance-schema-table_handles-table.md).
* Commandline: `--performance-schema-max-table-handles=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `-1`
* Range: `-1` to `1048576`



#### `performance_schema_max_table_instances`


* Description: Specifies the maximum number of instrumented table objects. `0` for disabling, `-1` (the default) for automated sizing.
* Commandline: `--performance-schema-max-table-instances=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value:`-1`
* Range: `-1` to `1048576`



#### `performance_schema_max_table_lock_stat`


* Description: Maximum number of lock statistics for instrumented tables. Use 0 to disable, -1 for automated scaling.
* Commandline: `--performance-schema-max-table-lock-stat=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `-1`
* Range: `-1` to `1048576`
* Introduced: [MariaDB 10.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-5-series/mariadb-1052-release-notes)



#### `performance_schema_max_thread_classes`


* Description: Specifies the maximum number of thread instruments.
* Commandline: `--performance-schema-max-thread-classes=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `50`
* Range: `0` to `256`



#### `performance_schema_max_thread_instances`


* Description: Specifies how many of the running server threads (see [max_connections](../../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#max_connections) and [max_delayed_threads](../../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#max_delayed_threads)) can be instrumented. Should be greater than the sum of max_connections and max_delayed_threads. `0` for disabling, `-1` (the default) for automated sizing.
* Commandline: `--performance-schema-max-thread-instances=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value:`-1`
* Range: `-1` to `1048576`



#### `performance_schema_session_connect_attrs_size`


* Description: Per thread preallocated memory for holding connection attribute strings. Incremented if the strings are larger than the reserved space. `0` for disabling, `-1` (the default) for automated sizing.
* Commandline: `--performance-schema-session-connect-attrs-size=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `-1`
* Range: `-1` to `1048576`



#### `performance_schema_setup_actors_size`


* Description: The maximum number of rows to store in the performance schema [setup_actors](performance-schema-tables/performance-schema-setup_actors-table.md) table. `-1` (from [MariaDB 10.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-5-series/mariadb-1052-release-notes)) denotes automated sizing.
* Commandline: `--performance-schema-setup-actors-size=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `-1` (>= [MariaDB 10.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-5-series/mariadb-1052-release-notes)), `100` (<= [MariaDB 10.5.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-5-series/mariadb-1051-release-notes))
* Range: `-1` to `1024` (>= [MariaDB 10.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-5-series/mariadb-1052-release-notes)), `0` to `1024` (<= [MariaDB 10.5.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-5-series/mariadb-1051-release-notes))



#### `performance_schema_setup_objects_size`


* Description: The maximum number of rows that can be stored in the performance schema [setup_objects](performance-schema-tables/performance-schema-setup_objects-table.md) table. `-1` (from [MariaDB 10.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-5-series/mariadb-1052-release-notes)) denotes automated sizing.
* Commandline: `--performance-schema-setup-objects-size=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `-1` (>= [MariaDB 10.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-5-series/mariadb-1052-release-notes)), `100` (<= [MariaDB 10.5.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-5-series/mariadb-1051-release-notes))
* Range: `-1` to `1048576` (>= [MariaDB 10.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-5-series/mariadb-1052-release-notes)), `0` to `1048576` (<= [MariaDB 10.5.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-5-series/mariadb-1051-release-notes))



#### `performance_schema_users_size`


* Description: Number of rows in the [performance_schema.users](performance-schema-tables/performance-schema-users-table.md) table. If set to 0, the [Performance Schema](README.md) will not store connection statistics in the users table. `-1` (the default) for automated sizing.
* Commandline: `--performance-schema-users-size=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `-1`
* Range: `-1` to `1048576`


