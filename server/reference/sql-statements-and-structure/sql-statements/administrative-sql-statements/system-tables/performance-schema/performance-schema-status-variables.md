
# Performance Schema Status Variables




This page documents status variables related to the [Performance Schema](performance-schema-tables/performance-schema-table_handles-table.md). See [Server Status Variables](../../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-status-variables.md) for a complete list of status variables that can be viewed with [SHOW STATUS](../../show/show-status.md).


See also the [Full list of MariaDB options, system and status variables](../../../../../../server-management/variables-and-modes/full-list-of-mariadb-options-system-and-status-variables.md).


#### `<code>Performance_schema_accounts_lost</code>`


* Description: Number of times a row could not be added to the performance schema accounts table due to it being full. The global value can be flushed by [FLUSH STATUS](../../flush-commands/flush-tables-for-export.md).
* Scope: Global, Session
* Data Type: `<code>numeric</code>`



#### `<code>Performance_schema_cond_classes_lost</code>`


* Description: Number of condition instruments that could not be loaded.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`



#### `<code>Performance_schema_cond_instances_lost</code>`


* Description: Number of instances a condition object could not be created. The global value can be flushed by [FLUSH STATUS](../../flush-commands/flush-tables-for-export.md).
* Scope: Global, Session
* Data Type: `<code>numeric</code>`



#### `<code>Performance_schema_digest_lost</code>`


* Description: The global value can be flushed by [FLUSH STATUS](../../flush-commands/flush-tables-for-export.md).
* Scope: Global, Session
* Data Type: `<code>numeric</code>`



#### `<code>Performance_schema_file_classes_lost</code>`


* Description: Number of file instruments that could not be loaded.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`



#### `<code>Performance_schema_file_handles_lost</code>`


* Description: Number of instances a file object could not be opened. The global value can be flushed by [FLUSH STATUS](../../flush-commands/flush-tables-for-export.md).
* Scope: Global, Session
* Data Type: `<code>numeric</code>`



#### `<code>Performance_schema_file_instances_lost</code>`


* Description: Number of instances a file object could not be created. The global value can be flushed by [FLUSH STATUS](../../flush-commands/flush-tables-for-export.md).
* Scope: Global, Session
* Data Type: `<code>numeric</code>`



#### `<code>Performance_schema_hosts_lost</code>`


* Description: Number of times a row could not be added to the performance schema hosts table due to it being full. The global value can be flushed by [FLUSH STATUS](../../flush-commands/flush-tables-for-export.md).
* Scope: Global, Session
* Data Type: `<code>numeric</code>`



#### `<code>Performance_schema_index_stat_lost</code>`


* Description:
* Scope: Global, Session
* Data Type: `<code>numeric</code>`
* Introduced: [MariaDB 10.5.2](../../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1052-release-notes.md)



#### `<code>Performance_schema_locker_lost</code>`


* Description: Number of events not recorded, due to either being recursive, or having a deeper nested events stack than the implementation limit. The global value can be flushed by [FLUSH STATUS](../../flush-commands/flush-tables-for-export.md).
* Scope: Global, Session
* Data Type: `<code>numeric</code>`



#### `<code>Performance_schema_memory_classes_lost</code>`


* Description:
* Scope: Global, Session
* Data Type: `<code>numeric</code>`
* Introduced: [MariaDB 10.5.2](../../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1052-release-notes.md)



#### `<code>Performance_schema_metadata_lock_lost</code>`


* Description:
* Scope: Global, Session
* Data Type: `<code>numeric</code>`
* Introduced: [MariaDB 10.5.2](../../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1052-release-notes.md)



#### `<code>Performance_schema_mutex_classes_lost</code>`


* Description: Number of mutual exclusion instruments that could not be loaded.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`



#### `<code>Performance_schema_mutex_instances_lost</code>`


* Description: Number of instances a mutual exclusion object could not be created. The global value can be flushed by [FLUSH STATUS](../../flush-commands/flush-tables-for-export.md).
* Scope: Global, Session
* Data Type: `<code>numeric</code>`



#### `<code>Performance_schema_nested_statement_lost</code>`


* Description:
* Scope: Global, Session
* Data Type: `<code>numeric</code>`
* Introduced: [MariaDB 10.5.2](../../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1052-release-notes.md)



#### `<code>Performance_schema_prepared_statements_lost</code>`


* Description:
* Scope: Global, Session
* Data Type: `<code>numeric</code>`
* Introduced: [MariaDB 10.5.2](../../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1052-release-notes.md)



#### `<code>Performance_schema_program_lost</code>`


* Description:
* Scope: Global, Session
* Data Type: `<code>numeric</code>`
* Introduced: [MariaDB 10.5.2](../../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1052-release-notes.md)



#### `<code>Performance_schema_rwlock_classes_lost</code>`


* Description: Number of read/write lock instruments that could not be loaded.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`



#### `<code>Performance_schema_rwlock_instances_lost</code>`


* Description: Number of instances a read/write lock object could not be created. The global value can be flushed by [FLUSH STATUS](../../flush-commands/flush-tables-for-export.md).
* Scope: Global, Session
* Data Type: `<code>numeric</code>`



#### `<code>Performance_schema_session_connect_attrs_lost</code>`


* Description: Number of connections for which connection attribute truncation has occurred. The global value can be flushed by [FLUSH STATUS](../../flush-commands/flush-tables-for-export.md).
* Scope: Global, Session
* Data Type: `<code>numeric</code>`



#### `<code>Performance_schema_socket_classes_lost</code>`


* Description:
* Scope: Global, Session
* Data Type: `<code>numeric</code>`



#### `<code>Performance_schema_socket_instances_lost</code>`


* Description: Number of instances a socket object could not be created. The global value can be flushed by [FLUSH STATUS](../../flush-commands/flush-tables-for-export.md).
* Scope: Global, Session
* Data Type: `<code>numeric</code>`



#### `<code>Performance_schema_stage_classes_lost</code>`


* Description: Number of stage event instruments that could not be loaded. The global value can be flushed by [FLUSH STATUS](../../flush-commands/flush-tables-for-export.md).
* Scope: Global, Session
* Data Type: `<code>numeric</code>`



#### `<code>Performance_schema_statement_classes_lost</code>`


* Description: Number of statement instruments that could not be loaded. The global value can be flushed by [FLUSH STATUS](../../flush-commands/flush-tables-for-export.md).
* Scope: Global, Session
* Data Type: `<code>numeric</code>`



#### `<code>Performance_schema_table_handles_lost</code>`


* Description: Number of instances a table object could not be opened. The global value can be flushed by [FLUSH STATUS](../../flush-commands/flush-tables-for-export.md).
* Scope: Global, Session
* Data Type: `<code>numeric</code>`



#### `<code>Performance_schema_table_instances_lost</code>`


* Description: Number of instances a table object could not be created. The global value can be flushed by [FLUSH STATUS](../../flush-commands/flush-tables-for-export.md).
* Scope: Global, Session
* Data Type: `<code>numeric</code>`



#### `<code>Performance_schema_table_lock_stat_lost</code>`


* Description:
* Scope: Global, Session
* Data Type: `<code>numeric</code>`
* Introduced: [MariaDB 10.5.2](../../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1052-release-notes.md)



#### `<code>Performance_schema_thread_classes_lost</code>`


* Description: Number of thread instruments that could not be loaded.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`



#### `<code>Performance_schema_thread_instances_lost</code>`


* Description: Number of instances thread object could not be created. The global value can be flushed by [FLUSH STATUS](../../flush-commands/flush-tables-for-export.md).
* Scope: Global, Session
* Data Type: `<code>numeric</code>`



#### `<code>Performance_schema_users_lost</code>`


* Description: Number of times a row could not be added to the performance schema users table due to it being full. The global value can be flushed by [FLUSH STATUS](../../flush-commands/flush-tables-for-export.md).
* Scope: Global, Session
* Data Type: `<code>numeric</code>`


