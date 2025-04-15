
# Server System Variables




## About the Server System Variables


MariaDB has many system variables that can be changed to suit your needs.


The full list of server variables are listed in the contents on this page, and most are described on this page, but some are described elsewhere:


* [Aria System Variables](../../../../reference/storage-engines/aria/aria-system-variables.md)
* [CONNECT System Variables](../../../../reference/storage-engines/connect/connect-system-variables.md)
* [Galera System Variables](../../galera-cluster/galera-cluster-system-variables.md)
* [Global Transaction ID System Variables](../../standard-replication/gtid.md#system-variables-for-global-transaction-id)
* [HandlerSocket Plugin System Variables](../../../../reference/sql-statements-and-structure/nosql/handlersocket/handlersocket-configuration-options.md)
* [InnoDB System Variables](../../../../reference/storage-engines/innodb/innodb-system-variables.md)
* [Mroonga System Variables](../../../../reference/storage-engines/mroonga/mroonga-system-variables.md)
* [MyRocks System Variables](../../../../reference/storage-engines/myrocks/myrocks-system-variables.md)
* [MyISAM System Variables](../../../../reference/storage-engines/myisam-storage-engine/myisam-system-variables.md)
* [Performance Schema System Variables](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/performance-schema/performance-schema-system-variables.md)
* [Replication and Binary Log System Variables](../../standard-replication/replication-and-binary-log-system-variables.md)
* [S3 Storage Engine System Variables](../../../../reference/storage-engines/s3-storage-engine/s3-storage-engine-system-variables.md)
* [Server_Audit System Variables](../../../../reference/plugins/mariadb-audit-plugin/mariadb-audit-plugin-options-and-system-variables.md)
* [Spider System Variables](../../../../reference/storage-engines/spider/spider-system-variables.md)
* [SQL_ERROR_LOG Plugin System Variables](sql-error-log-system-variables-and-options.md)
* [SSL System Variables](../../../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/ssltls-system-variables.md)
* [Threadpool System Variables](../buffers-caches-and-threads/thread-pool/thread-pool-system-status-variables.md)
* [TokuDB System Variables](../../../../reference/storage-engines/tokudb/tokudb-system-variables.md)
* [Vector System Variables](../../../../reference/sql-statements-and-structure/vectors/vector-system-variables.md)


See also the [Full list of MariaDB options, system and status variables](../../../../server-management/variables-and-modes/full-list-of-mariadb-options-system-and-status-variables.md).


Most of these can be set with [command line options](../../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md) and many of them can be changed at runtime.
Variables that can be changed at runtime (and therefore are not read-only) are described as "Dynamic" below, and elsewhere in the documentation.


There are a few ways to see the full list of server system variables:


* While in the mariadb client, run:


```
SHOW VARIABLES;
```

* See [SHOW VARIABLES](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-variables.md) for instructions on using this command.


* From your shell, run mariadbd like so:


```
mariadbd --verbose --help
```

* View the Information Schema [GLOBAL_VARIABLES](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-global_variables-and-session_variables-tables.md), [SESSION_VARIABLES](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-global_variables-and-session_variables-tables.md), and [SYSTEM_VARIABLES](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-system_variables-table.md) tables.


## Setting Server System Variables


There are several ways to set server system variables:


* Specify them on the command line:


```
shell> ./mariadbd-safe --aria_group_commit="hard"
```

* Specify them in your my.cnf file (see [Configuring MariaDB with my.cnf](../../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md) for more information):


```
aria_group_commit = "hard"
```

* Set them from the mariadb client using the [SET](../../../../../connectors/mariadb-connector-cpp/setup-for-connector-cpp-examples.md) command. Only variables that are dynamic can be set at runtime in this way. Note that variables set in this way will not persist after a restart.


```
SET GLOBAL aria_group_commit="hard";
```

By convention, server variables have usually been specified with an underscore in the configuration files, and a dash on the command line. You can however specify underscores as dashes - they are interchangeable.


Variables that take a numeric size can either be specified in full, or with a suffix for easier readability. Valid suffixes are:



| Suffix | Description | Value |
| --- | --- | --- |
| Suffix | Description | Value |
| K | kilobytes | 1024 |
| M | megabytes | 10242 |
| G | gigabytes | 10243 |
| T | terabytes | 10244 (from [MariaDB 10.3.3](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1033-release-notes.md)) |
| P | petabytes | 10245 (from [MariaDB 10.3.3](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1033-release-notes.md)) |
| E | exabytes | 10246 (from [MariaDB 10.3.3](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1033-release-notes.md)) |



The suffix can be upper or lower-case.


## List of Server System Variables


#### `<code>allow_suspicious_udfs</code>`


* Description: Allows use of [user-defined functions](../../../programming-customizing-mariadb/user-defined-functions/user-defined-functions-security.md) consisting of only one symbol `<code>x()</code>` without corresponding `<code>x_init()</code>` or `<code>x_deinit()</code>`. That also means that one can load any function from any library, for example `<code>exit()</code>` from `<code>libc.so</code>`. Not recommended unless you require old UDFs with one symbol that cannot be recompiled. Before [MariaDB 10.10](../../../../../release-notes/mariadb-community-server/what-is-mariadb-1010.md), available as an [option only](../../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md#-allow-suspicious-udfs).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--allow-suspicious-udfs</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`
* Introduced: [MariaDB 10.10](../../../../../release-notes/mariadb-community-server/what-is-mariadb-1010.md)



#### `<code>alter_algorithm</code>`


* Description: The implied `<code>ALGORITHM</code>` for [ALTER TABLE](../../../../reference/sql-statements-and-structure/sql-statements/data-definition/alter/alter-tablespace.md) if no `<code>ALGORITHM</code>` clause is specified. The deprecated variable [old_alter_table](#old_alter_table) is an alias for this. The feature was removed in [MariaDB 11.5](../../../../../release-notes/mariadb-community-server/what-is-mariadb-115.md). See [ALGORITHM=DEFAULT](../../../../reference/sql-statements-and-structure/sql-statements/data-definition/alter/alter-tablespace.md#algorithmdefault).

  * `<code>COPY</code>` corresponds to the pre-MySQL 5.1 approach of creating an intermediate table, copying data one row at a time, and renaming and dropping tables.
  * `<code>INPLACE</code>` requests that the operation be refused if it cannot be done natively inside a the storage engine.
  * `<code>DEFAULT</code>` (the default) chooses `<code>INPLACE</code>` if available, and falls back to `<code>COPY</code>`.
  * `<code>NOCOPY</code>` refuses to copy a table.
  * `<code>INSTANT</code>` refuses an operation that would involve any other than metadata changes.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--alter-algorithm=default</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>enumerated</code>`
* Default Value: `<code>DEFAULT</code>`
* Valid Values: `<code>DEFAULT</code>`, `<code>COPY</code>`, `<code>INPLACE</code>`, `<code>NOCOPY</code>`, `<code>INSTANT</code>`
* Introduced: [MariaDB 10.3.7](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1037-release-notes.md)
* Deprecated: [MariaDB 11.5](../../../../../release-notes/mariadb-community-server/what-is-mariadb-115.md)


#### `<code>analyze_sample_percentage</code>`


* Description: Percentage of rows from the table [ANALYZE TABLE](../../../../reference/sql-statements-and-structure/sql-statements/table-statements/analyze-table.md) will sample to collect table statistics. Set to 0 to let MariaDB decide what percentage of rows to sample.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--analyze-sample-percentage=#</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>100.000000</code>`
* Range: `<code>0</code>` to `<code>100</code>`
* Introduced: [MariaDB 10.4.3](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-4-series/mariadb-1043-release-notes.md)


#### `<code>autocommit</code>`


* Description: If set to 1, the default, all queries are committed immediately. The [LOCK IN SHARE MODE](../../../../reference/sql-statements-and-structure/sql-statements/data-manipulation/selecting-data/lock-in-share-mode.md) and [FOR UPDATE](../../../../reference/sql-statements-and-structure/sql-statements/data-manipulation/selecting-data/for-update.md) clauses therefore have no effect. If set to 0, they are only committed upon a [COMMIT](../../../../reference/sql-statements-and-structure/sql-statements/transactions/commit.md) statement, or rolled back with a [ROLLBACK](https://mariadb.com/kb/en/) statement. If autocommit is set to 0, and then changed to 1, all open transactions are immediately committed.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--autocommit[=#]</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>1</code>`



#### `<code>automatic_sp_privileges</code>`


* Description: When set to 1, the default, when a stored routine is created, the creator is automatically granted permission to [ALTER](../../../programming-customizing-mariadb/stored-routines/stored-procedures/alter-procedure.md) (which includes dropping) and to EXECUTE the routine. If set to 0, the creator is not automatically granted these privileges.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--automatic-sp-privileges</code>`, `<code class="fixed" style="white-space:pre-wrap">--skip-automatic-sp-privileges</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>1</code>`



#### `<code>back_log</code>`


* Description: Connections take a small amount of time to start, and this setting determines the number of outstanding connection requests MariaDB can have, or the size of the listen queue for incoming TCP/IP requests. Requests beyond this will be refused. Increase if you expect short bursts of connections. Cannot be set higher than the operating system limit (see the Unix listen() man page). If not set, set to `<code>0</code>`, or the `<code>--autoset-back-log</code>` option is used, will be autoset to the lower of `<code>900</code>` and (50 + [max_connections](#max_connections)/5).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--back-log=#</code>`
* Scope: Global
* Dynamic: No
* Type: number
* Default Value:

  * The lower of `<code>900</code>` and (50 + [max_connections](#max_connections)/5)



#### `<code>basedir</code>`


* Description: Path to the MariaDB installation directory. Other paths are usually resolved relative to this base directory.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--basedir=path</code>` or `<code class="fixed" style="white-space:pre-wrap">-b path</code>`
* Scope: Global
* Dynamic: No
* Type: directory name



#### `<code>big_tables</code>`


* Description: If this system variable is set to 1, then temporary tables will be saved to disk intead of memory.

  * This system variable's original intention was to allow result sets that were too big for memory-based temporary tables and to avoid the resulting 'table full' errors.
  * This system variable is no longer needed, because the server can automatically convert large memory-based temporary tables into disk-based temporary tables when they exceed the value of the `<code>[tmp_memory_table_size](#tmp_memory_table_size)</code>` system variable.
  * To prevent memory-based temporary tables from being used at all, set the `<code>[tmp_memory_table_size](#tmp_memory_table_size)</code>` system variable to `<code>0</code>`.
  * In [MariaDB 5.5](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5.md) and earlier, `<code>[sql_big_tables](#sql_big_tables)</code>` is a synonym.
  * In [MariaDB 10.5](../../../../../release-notes/mariadb-community-server/what-is-mariadb-105.md), this system variable is deprecated.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--big-tables</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>0</code>`
* Deprecated: [MariaDB 10.5.0](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1050-release-notes.md)



#### `<code>bind_address</code>`


* Description: By default, the MariaDB server listens for TCP/IP connections on all addresses. You can specify an alternative when the server starts using this option; either a host name, an IPv4 or an IPv6 address, "::" or "*" (all addresses). In some systems, such as Debian and Ubuntu, the bind_address is set to 127.0.0.1, which binds the server to listen on localhost only. `<code>bind_address</code>` has always been available as a [mariadbd option](../../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md); from [MariaDB 10.3.3](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1033-release-notes.md) its also available as a system variable. Before [MariaDB 10.6.0](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-1060-release-notes.md) "::" implied listening additionally on IPv4 addresses like "*". From 10.6.0 onwards it refers to IPv6 stictly. Starting with [MariaDB 10.11](../../../../../release-notes/mariadb-community-server/what-is-mariadb-1011.md), a comma-separated list of addresses to bind to can be given. See also [Configuring MariaDB for Remote Client Access](../../../../../general-resources/learning-and-training/training-and-tutorials/basic-mariadb-articles/configuring-mariadb-for-remote-client-access.md).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--bind-address=addr</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>string</code>`
* Default Value: (Empty string)
* Valid Values: Host name, IPv4, IPv6, ::, *
* Introduced: [MariaDB 10.3.3](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1033-release-notes.md) (as a system variable)



#### `<code>block_encryption_mode</code>`


* Description: Default block encryption mode for [AES_ENCRYPT()](../../../../reference/sql-statements-and-structure/sql-statements/built-in-functions/secondary-functions/encryption-hashing-and-compression-functions/aes_encrypt.md) and [AES_DECRYPT()](../../../../reference/sql-statements-and-structure/sql-statements/built-in-functions/secondary-functions/encryption-hashing-and-compression-functions/aes_decrypt.md) functions.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--block-encryption-mode=val</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>aes-128-ecb</code>`
* Valid values: `<code>aes-128-ecb</code>`, `<code>aes-192-ecb</code>`, `<code>aes-256-ecb</code>`, `<code>aes-128-cbc</code>`, `<code>aes-192-cbc</code>`, `<code>aes-256-cbc</code>`, `<code>aes-128-ctr</code>`, `<code>aes-192-ctr</code>`, `<code>aes-256-ctr</code>`
* Introduced: [MariaDB 11.2.0](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-2-series/mariadb-11-2-0-release-notes.md)



#### `<code>bulk_insert_buffer_size</code>`


* Description: Size in bytes of the per-thread cache tree used to speed up bulk inserts into [MyISAM](../../../../reference/storage-engines/myisam-storage-engine/myisam-system-variables.md) and [Aria](../../../../reference/storage-engines/s3-storage-engine/aria_s3_copy.md) tables. A value of 0 disables the cache tree.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--bulk-insert-buffer-size=#</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>8388608</code>`
* Range - 32 bit: `<code>0</code>` to `<code>4294967295</code>`
* Range - 64 bit: `<code>0</code>` to `<code>18446744073709547520</code>`



#### `<code>character_set_client</code>`


* Description: Determines the [character set](../../../../reference/data-types/string-data-types/character-sets/README.md) for queries arriving from the client. It can be set per session by the client, although the server can be configured to ignore client requests with the `<code>--skip-character-set-client-handshake</code>` option. If the client does not request a character set, or requests a character set that the server does not support, the global value will be used. utf16, utf16le, utf32 and ucs2 cannot be used as client character sets. From [MariaDB 10.6](../../../../../release-notes/mariadb-community-server/what-is-mariadb-106.md), the `<code>utf8</code>` [character set](../../../../reference/data-types/string-data-types/character-sets/README.md) (and related collations) is by default an alias for `<code>utf8mb3</code>` rather than the other way around. It can be set to imply `<code>utf8mb4</code>` by changing the value of the [old_mode](server-system-variables.md#old_mode) system variable.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>string</code>`
* Default Value: `<code>utf8mb3</code>` (>= [MariaDB 10.6](../../../../../release-notes/mariadb-community-server/what-is-mariadb-106.md)), `<code>utf8</code>` (<= [MariaDB 10.5](../../../../../release-notes/mariadb-community-server/what-is-mariadb-105.md))



#### `<code>character_set_collations</code>`


* Description: Overrides for character set default collations. Takes a comma-delimited list of character set and collation settings, for example `<code>SET @@character_set_collations = 'utf8mb4=uca1400_ai_ci, latin2=latin2_hungarian_ci';</code>` The new variable will take effect in all cases where a character set is explicitly or implicitly specified without an explicit COLLATE clause, including but not limited to:

  * Column collation
  * Table collation
  * Database collation
  * CHAR(expr USING csname)
  * CONVERT(expr USING csname)
  * CAST(expr AS CHAR CHARACTER SET csname)
  * '' - character string literal
  * _utf8mb3'text' - a character string literal with an introducer
  * _utf8mb3 X'61' - a character string literal with an introducer with hex notation
  * _utf8mb3 0x61 - a character string literal with an introducer with hex hybrid notation
  * @@collation_connection after a SET NAMES without COLLATE
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>string</code>`
* Default Value:

  * `<code>utf8mb3=utf8mb3_uca1400_ai_ci, ucs2=ucs2_uca1400_ai_ci, utf8mb4=utf8mb4_uca1400_ai_ci, utf16=utf16_uca1400_ai_ci, utf32=utf32_uca1400_ai_ci</code>` (>= [MariaDB 11.5](../../../../../release-notes/mariadb-community-server/what-is-mariadb-115.md))
  * Empty (<= [MariaDB 11.4](../../../../../release-notes/mariadb-community-server/what-is-mariadb-114.md))
* Introduced: [MariaDB 11.2](../../../../../release-notes/mariadb-community-server/what-is-mariadb-112.md)



#### `<code>character_set_connection</code>`


* Description: [Character set](../../../../reference/data-types/string-data-types/character-sets/README.md) used for number to string conversion, as well as for literals that don't have a character set introducer. From [MariaDB 10.6](../../../../../release-notes/mariadb-community-server/what-is-mariadb-106.md), the `<code>utf8</code>` [character set](../../../../reference/data-types/string-data-types/character-sets/README.md) (and related collations) is by default an alias for `<code>utf8mb3</code>` rather than the other way around. It can be set to imply `<code>utf8mb4</code>` by changing the value of the [old_mode](server-system-variables.md#old_mode) system variable.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>string</code>`
* Default Value: `<code>utf8mb3</code>` (>= [MariaDB 10.6](../../../../../release-notes/mariadb-community-server/what-is-mariadb-106.md)), `<code>utf8</code>` (<= [MariaDB 10.5](../../../../../release-notes/mariadb-community-server/what-is-mariadb-105.md))



#### `<code>character_set_database</code>`


* Description: [Character set](../../../../reference/data-types/string-data-types/character-sets/README.md) used by the default database, and set by the server whenever the default database is changed. If there's no default database, character_set_database contains the same value as [character_set_server](#character_set_server). This variable is dynamic, but should not be set manually, only by the server.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>string</code>`
* Default Value: `<code>utf8mb4</code>` (>= [MariaDB 11.6.0](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-6-rolling-releases/mariadb-11-6-0-release-notes.md)), `<code>latin1</code>` (<= [MariaDB 11.5](../../../../../release-notes/mariadb-community-server/what-is-mariadb-115.md))



#### `<code>character_set_filesystem</code>`


* Description: The [character set](../../../../reference/data-types/string-data-types/character-sets/README.md) for the filesystem. Used for converting file names specified as a string literal from [character_set_client](#character_set_client) to character_set_filesystem before opening the file. By default set to `<code>binary</code>`, so no conversion takes place. This could be useful for statements such as [LOAD_FILE()](../../../../reference/sql-statements-and-structure/sql-statements/built-in-functions/string-functions/load_file.md) or [LOAD DATA INFILE](../../../../reference/sql-statements-and-structure/sql-statements/data-manipulation/inserting-loading-data/load-data-into-tables-or-index/load-data-infile.md) on system where multi-byte file names are use.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--character-set-filesystem=name</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>string</code>`
* Default Value: `<code>binary</code>`



#### `<code>character_set_results</code>`


* Description: [Character set](../../../../reference/data-types/string-data-types/character-sets/README.md) used for results and error messages returned to the client. From [MariaDB 10.6](../../../../../release-notes/mariadb-community-server/what-is-mariadb-106.md), the `<code>utf8</code>` [character set](../../../../reference/data-types/string-data-types/character-sets/README.md) (and related collations) is by default an alias for `<code>utf8mb3</code>` rather than the other way around. It can be set to imply `<code>utf8mb4</code>` by changing the value of the [old_mode](server-system-variables.md#old_mode) system variable.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>string</code>`
* Default Value: `<code>utf8mb3</code>` (>= [MariaDB 10.6](../../../../../release-notes/mariadb-community-server/what-is-mariadb-106.md)), `<code>utf8</code>` (<= [MariaDB 10.5](../../../../../release-notes/mariadb-community-server/what-is-mariadb-105.md))



#### `<code>character_set_server</code>`


* Description: Default [character set](../../../../reference/data-types/string-data-types/character-sets/README.md) used by the server. See [character_set_database](#character_set_database) for character sets used by the default database. Defaults may be different on some systems, see for example [Differences in MariaDB in Debian](../../../../server-management/getting-installing-and-upgrading-mariadb/troubleshooting-installation-issues/installation-issues-on-debian-and-ubuntu/differences-in-mariadb-in-debian-and-ubuntu.md).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--character-set-server</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>string</code>`
* Default Value: `<code>utf8mb4</code>` (>= [MariaDB 11.6.0](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-6-rolling-releases/mariadb-11-6-0-release-notes.md)), `<code>latin1</code>` (<= [MariaDB 11.5](../../../../../release-notes/mariadb-community-server/what-is-mariadb-115.md))



#### `<code>character_set_system</code>`


* Description: [Character set](../../../../reference/data-types/string-data-types/character-sets/README.md) used by the server to store identifiers, always set to utf8, or its synonym utf8mb3 starting with [MariaDB 10.6](../../../../../release-notes/mariadb-community-server/what-is-mariadb-106.md). From [MariaDB 10.6](../../../../../release-notes/mariadb-community-server/what-is-mariadb-106.md), the `<code>utf8</code>` [character set](../../../../reference/data-types/string-data-types/character-sets/README.md) (and related collations) is by default an alias for `<code>utf8mb3</code>` rather than the other way around. It can be set to imply `<code>utf8mb4</code>` by changing the value of the [old_mode](server-system-variables.md#old_mode) system variable.
* Scope: Global
* Dynamic: No
* Data Type: `<code>string</code>`
* Default Value: `<code>utf8mb3</code>` (>= [MariaDB 10.6](../../../../../release-notes/mariadb-community-server/what-is-mariadb-106.md)), `<code>utf8</code>` (<= [MariaDB 10.5](../../../../../release-notes/mariadb-community-server/what-is-mariadb-105.md))



#### `<code>character_sets_dir</code>`


* Description: Directory where the [character sets](../../../../reference/data-types/string-data-types/character-sets/README.md) are installed.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--character-sets-dir=path</code>`
* Scope: Global
* Dynamic: No
* Type: directory name



#### `<code>check_constraint_checks</code>`


* Description: If set to `<code>0</code>`, will disable [constraint checks](../../../../reference/sql-statements-and-structure/sql-statements/data-definition/constraint.md), for example when loading a table that violates some constraints that you plan to fix later.
* Scope: Global, Session
* Dynamic: Yes
* Type: boolean
* Default: ON



#### `<code>collation_connection</code>`


* Description: Collation used for the connection [character set](../../../../reference/data-types/string-data-types/character-sets/README.md).
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>string</code>`



#### `<code>collation_database</code>`


* Description: [Collation used](../../../../reference/data-types/string-data-types/character-sets/README.md) for the default database. Set by the server if the default database changes, if there is no default database the value from the `<code>collation_server</code>` variable is used. This variable is dynamic, but should not be set manually, only by the server.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>string</code>`



#### `<code>collation_server</code>`


* Description: Default [collation](../../../../reference/data-types/string-data-types/character-sets/README.md) used by the server. This is set to the default collation for a given character set automatically when [character_set_server](#character_set_server) is changed, but it can also be set manually. Defaults may be different on some systems, see for example [Differences in MariaDB in Debian](../../../../server-management/getting-installing-and-upgrading-mariadb/troubleshooting-installation-issues/installation-issues-on-debian-and-ubuntu/differences-in-mariadb-in-debian-and-ubuntu.md).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--collation-server=name</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>string</code>`
* Default Value: `<code>latin1_swedish_ci</code>`



#### `<code>completion_type</code>`


* Description: The transaction completion type. If set to `<code>NO_CHAIN</code>` or `<code>0</code>` (the default), there is no effect on commits and rollbacks. If set to `<code>CHAIN</code>` or `<code>1</code>`, a [COMMIT](../../../../reference/sql-statements-and-structure/sql-statements/transactions/commit.md) statement is equivalent to COMMIT AND CHAIN, while a [ROLLBACK](https://mariadb.com/kb/en/) is equivalent to ROLLBACK AND CHAIN, so a new transaction starts straight away with the same isolation level as transaction that's just finished. If set to `<code>RELEASE</code>` or `<code>2</code>`, a [COMMIT](../../../../reference/sql-statements-and-structure/sql-statements/transactions/commit.md) statement is equivalent to COMMIT RELEASE, while a [ROLLBACK](https://mariadb.com/kb/en/) is equivalent to ROLLBACK RELEASE, so the server will disconnect after the transaction completes. Note that the transaction completion type only applies to explicit commits, not implicit commits.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--completion-type=name</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>enumerated</code>`
* Default Value: `<code>NO_CHAIN</code>`
* Valid Values: `<code>0</code>`, `<code>1</code>`, `<code>2</code>`, `<code>NO_CHAIN</code>`, `<code>CHAIN</code>`, `<code>RELEASE</code>`



#### `<code>concurrent_insert</code>`


* Description: If set to `<code>AUTO</code>` or `<code>1</code>`, the default, MariaDB allows [concurrent INSERTs](../../../../reference/sql-statements-and-structure/sql-statements/data-manipulation/inserting-loading-data/concurrent-inserts.md) and SELECTs for [MyISAM](../../../../reference/storage-engines/myisam-storage-engine/myisam-system-variables.md) tables with no free blocks in the data (deleted rows in the middle). If set to `<code>NEVER</code>` or `<code>0</code>`, concurrent inserts are disabled. If set to `<code>ALWAYS</code>` or `<code>2</code>`, concurrent inserts are permitted for all MyISAM tables, even those with holes, in which case new rows are added at the end of a table if the table is being used by another thread. If the [--skip-new](../../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md#-skip-new) option is used when starting the server, concurrent_insert is set to `<code>NEVER</code>`. Changing the variable only affects new opened tables. Use [FLUSH TABLES](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/flush-commands/flush-tables-for-export.md) If you want it to also affect cached tables. See [Concurrent Inserts](../../../../reference/sql-statements-and-structure/sql-statements/data-manipulation/inserting-loading-data/concurrent-inserts.md) for more.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--concurrent-insert[=value]</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>enumerated</code>`
* Default Value: `<code>AUTO</code>`
* Valid Values: `<code>0</code>`, `<code>1</code>`, `<code>2</code>`, `<code>AUTO</code>`, `<code>NEVER</code>`, `<code>ALWAYS</code>`



#### `<code>connect_timeout</code>`


* Description: Time in seconds that the server waits for a connect packet before returning a 'Bad handshake'. Increasing may help if clients regularly encounter 'Lost connection to MySQL server at 'X', system error: error_number' type-errors.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--connect-timeout=#</code>`
* Scope: Global
* Dynamic: Yes
* Type: numeric
* Default Value: `<code>10</code>`
* Range: `<code>2</code>` to `<code>31536000</code>`



#### `<code>core_file</code>`


* Description: Write a core-file on crashes. The file name and location are system dependent. On Linux it is usually called `<code>core.${PID}</code>`, and it is usually written to the data directory. However, this can be changed.

  * See [Enabling Core Dumps](../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/debugging-mariadb/enabling-core-dumps.md) for more information.
  * Previously this system variable existed only as an [option](../../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md), but it was also made into a read-only system variable starting with [MariaDB 10.3.9](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1039-release-notes.md), [MariaDB 10.2.17](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-10217-release-notes.md) and [MariaDB 10.1.35](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10135-release-notes.md).
  * On Windows >= [MariaDB 10.4.3](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-4-series/mariadb-1043-release-notes.md), this option is set by default.
  * Note that the option accepts no arguments; specifying `<code>--core-file</code>` sets the value to `<code>ON</code>`. It cannot be disabled in the case of Windows >= [MariaDB 10.4.3](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-4-series/mariadb-1043-release-notes.md).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--core-file</code>`
* Scope: Global
* Dynamic: No
* Type: boolean
* Default Value:

  * Windows >= [MariaDB 10.4.3](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-4-series/mariadb-1043-release-notes.md): `<code>ON</code>`
  * All other systems: `<code>OFF</code>`



#### `<code>datadir</code>`


* Description: Directory where the data is stored.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--datadir=path</code>` or `<code class="fixed" style="white-space:pre-wrap">-h path</code>`
* Scope: Global
* Dynamic: No
* Type: directory name



#### `<code>date_format</code>`


* Description: Unused.
* Removed: [MariaDB 11.3.0](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-0-release-notes.md)



#### `<code>datetime_format</code>`


* Description: Unused.
* Removed: [MariaDB 11.3.0](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-0-release-notes.md)



#### `<code>debug/debug_dbug</code>`


* Description: Available in debug builds only (built with -DWITH_DEBUG=1). Used in debugging through the DBUG library to write to a trace file. Just using `<code class="fixed" style="white-space:pre-wrap">--debug</code>` will write a trace of what mariadbd is doing to the default trace file.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">-#</code>`, `<code class="fixed" style="white-space:pre-wrap">--debug[=debug_options]</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>string</code>`
* Default Value:

  * >= [MariaDB 10.5](../../../../../release-notes/mariadb-community-server/what-is-mariadb-105.md): `<code>d:t:i:o,/tmp/mariadbd.trace</code>` (Unix) or `<code>d:t:i:O,\mariadbd.trace</code>` (Windows)
* Debug Options: See the option flags on the [mysql_debug](../../../../../connectors/mariadb-connector-c/mariadb-connectorc-api-functions/mysql_debug.md) page



#### `<code>debug_no_thread_alarm</code>`


* Description: Disable system thread alarm calls. Disabling it may be useful in debugging or testing, never do it in production.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--debug-no-thead-alarm=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`
* Removed: [MariaDB 11.4](../../../../../release-notes/mariadb-community-server/what-is-mariadb-114.md)



#### `<code>debug_sync</code>`


* Description: Used in debugging to show the interface to the [Debug Sync facility](../../../../clients-and-utilities/mariadb-test/the-debug-sync-facility.md). MariaDB needs to be configured with -DENABLE_DEBUG_SYNC=1 for this variable to be available.
* Scope: Session
* Dynamic: Yes
* Data Type: `<code>string</code>`
* Default Value: `<code>OFF</code>` or `<code>ON - current signal <em>signal name</em></code>`



#### `<code>default_password_lifetime</code>`


* Description: This defines the global [password expiration policy](../../../../security/user-account-management/user-password-expiry.md). 0 means automatic password expiration is disabled. If the value is a positive integer N, the passwords must be changed every N days. This behavior can be overridden using the password expiration options in [ALTER USER](../../../../reference/sql-statements-and-structure/sql-statements/account-management-sql-commands/alter-user.md).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--default-password-lifetime=#</code>`
* Scope: Global
* Dynamic: Yes
* Type: numeric
* Default Value: `<code>0</code>`
* Range: `<code>0</code>` to `<code>4294967295</code>`



#### `<code>default_regex_flags</code>`


* Description: Introduced to address remaining incompatibilities between [PCRE](../../../../reference/sql-statements-and-structure/sql-statements/built-in-functions/string-functions/regular-expressions-functions/pcre.md) and the old regex library. Accepts a comma-separated list of zero or more of the following values:



|   |   |   |
| --- | --- | --- |
| Value | Pattern equivalent | Meaning |
| DOTALL | (?s) | . matches anything including NL |
| DUPNAMES | (?J) | Allow duplicate names for subpatterns |
| EXTENDED | (?x) | Ignore white space and 

# comments |
| EXTRA | (?X) | extra features (e.g. error on unknown escape character) |
| MULTILINE | (?m) | ^ and $ match newlines within data |
| UNGREEDY | (?U) | Invert greediness of quantifiers |



* Commandline: `<code class="fixed" style="white-space:pre-wrap">--default-regex-flags=value</code>`
* Scope: Global, Session
* Dynamic: Yes
* Type: enumeration
* Default Value: empty
* Valid Values: `<code>DOTALL</code>`, `<code>DUPNAMES</code>`, `<code>EXTENDED</code>`, `<code>EXTRA</code>`, `<code>MULTILINE</code>`, `<code>UNGREEDY</code>`



#### `<code>default_storage_engine</code>`


* Description: The default [storage engine](../../../../../general-resources/learning-and-training/video-presentations-and-screencasts/storage-engines-and-plugins-videos.md). The default storage engine must be enabled at server startup or the server won't start.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--default-storage-engine=name</code>`
* Scope: Global, Session
* Dynamic: Yes
* Type: enumeration
* Default Value: `<code>InnoDB</code>`



#### `<code>default_table_type</code>`


* Description: A synonym for [default_storage_engine](#default_storage_engine). Removed in [MariaDB 5.5](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5.md).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--default-table-type=name</code>`
* Scope: Global, Session
* Dynamic: Yes
* Removed: [MariaDB 5.5](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5.md)



#### `<code>default_tmp_storage_engine</code>`


* Description: Default storage engine that will be used for tables created with [CREATE TEMPORARY TABLE](../../../../reference/sql-statements-and-structure/vectors/create-table-with-vectors.md) where no engine is specified. For internal temporary tables see [aria_used_for_temp_tables](../../../../reference/storage-engines/aria/aria-system-variables.md#aria_used_for_temp_tables)). The storage engine used must be active or the server will not start. See [default_storage_engine](#default_storage_engine) for the default for non-temporary tables. Defaults to NULL, in which case the value from [default_storage_engine](#default_storage_engine) is used. [ROCKSDB](../../../../reference/storage-engines/myrocks/myrocks-in-mariadb-102-vs-mariadb-103.md) temporary tables cannot be created. Before [MariaDB 10.7](../../../../../release-notes/mariadb-community-server/what-is-mariadb-107.md), attempting to do so would silently fail, and a MyISAM table would instead be created. From [MariaDB 10.7](../../../../../release-notes/mariadb-community-server/what-is-mariadb-107.md), an error is returned.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--default-tmp-storage-engine=name</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>enumeration</code>`
* Default Value: NULL



#### `<code>default_week_format</code>`


* Description: Default mode for the [WEEK()](../../../../reference/sql-statements-and-structure/sql-statements/built-in-functions/date-time-functions/weekofyear.md) function. See that page for details on the different modes
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--default-week-format=#</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>0</code>`
* Range: `<code>0</code>` to `<code>7</code>`



#### `<code>delay_key_write</code>`


* Description: Specifies how MyISAM tables handles [CREATE TABLE](../../../../reference/sql-statements-and-structure/vectors/create-table-with-vectors.md) DELAY_KEY_WRITE. If set to `<code>ON</code>`, the default, any DELAY KEY WRITEs are honored. The key buffer is then flushed only when the table closes, speeding up writes. MyISAM tables should be automatically checked upon startup in this case, and --external locking should not be used, as it can lead to index corruption. If set to `<code>OFF</code>`, DELAY KEY WRITEs are ignored, while if set to `<code>ALL</code>`, all new opened tables are treated as if created with DELAY KEY WRITEs enabled.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--delay-key-write[=name]</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>enumeration</code>`
* Default Value: `<code>ON</code>`
* Valid Values: `<code>ON</code>`, `<code>OFF</code>`, `<code>ALL</code>`



#### `<code>delayed_insert_limit</code>`


* Description: After this many rows have been inserted with [INSERT DELAYED](../../../../reference/sql-statements-and-structure/sql-statements/data-manipulation/inserting-loading-data/insert-delayed.md), the handler will check for and execute any waiting [SELECT](../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/benchmarks-and-long-running-tests/benchmark-results/select-random-ranges-and-select-random-point.md) statements.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--delayed-insert-limit=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>100</code>`
* Range: `<code>1</code>` to `<code>4294967295</code>`



#### `<code>delayed_insert_timeout</code>`


* Description: Time in seconds that the [INSERT DELAYED](../../../../reference/sql-statements-and-structure/sql-statements/data-manipulation/inserting-loading-data/insert-delayed.md) handler will wait for INSERTs before terminating.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--delayed-insert-timeout=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>300</code>`



#### `<code>delayed_queue_size</code>`


* Description: Number of rows, per table, that can be queued when performing [INSERT DELAYED](../../../../reference/sql-statements-and-structure/sql-statements/data-manipulation/inserting-loading-data/insert-delayed.md) statements. If the queue becomes full, clients attempting to perform INSERT DELAYED's will wait until the queue has room available again.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--delayed-queue-size=#</code>`
* Scope: Global
* Dynamic: Yes
* Type: numeric
* Default Value: `<code>1000</code>`
* Range: `<code>1 to 4294967295</code>`



#### `<code>disconnect_on_expired_password</code>`


* Description: When a user password has expired (see [User Password Expiry](../../../../security/user-account-management/user-password-expiry.md)), this variable controls how the server handles clients that are not aware of the sandbox mode. If enabled, the client is not permitted to connect, otherwise the server puts the client in a sandbox mode.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--disconnect-on-expired-password[={0|1}]</code>`
* Scope: Global
* Dynamic: Yes
* Type: boolean
* Default Value: `<code>OFF</code>`



#### `<code>div_precision_increment</code>`


* Description: The precision of the result of the decimal division will be the larger than the precision of the dividend by that number. By default it's `<code>4</code>`, so `<code>SELECT 2/15</code>` would return 0.1333 and `<code>SELECT 2.0/15</code>` would return 0.13333. After setting div_precision_increment to `<code>6</code>`, for example, the same operation would return 0.133333 and 0.1333333 respectively.


From [MariaDB 10.1.46](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10146-release-notes.md), [MariaDB 10.2.33](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-10233-release-notes.md), [MariaDB 10.3.24](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-10324-release-notes.md), [MariaDB 10.4.14](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-4-series/mariadb-10414-release-notes.md) and [MariaDB 10.5.5](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1055-release-notes.md), `<code>div_precision_increment</code>` is taken into account in intermediate calculations. Previous versions did not, and the results were dependent on the optimizer, and therefore unpredictable.



 In [MariaDB 10.1.46](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10146-release-notes.md), [MariaDB 10.1.47](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10147-release-notes.md), [MariaDB 10.2.33](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-10233-release-notes.md), [MariaDB 10.2.34](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-10234-release-notes.md), [MariaDB 10.2.35](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-10235-release-notes.md), [MariaDB 10.3.24](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-10324-release-notes.md), [MariaDB 10.3.25](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-10325-release-notes.md), [MariaDB 10.4.14](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-4-series/mariadb-10414-release-notes.md), [MariaDB 10.4.15](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-4-series/mariadb-10415-release-notes.md), [MariaDB 10.5.5](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1055-release-notes.md) and [MariaDB 10.5.6](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1056-release-notes.md) only, the fix truncated decimal values after every division, resulting in lower precision in some cases for those versions only.



 From [MariaDB 10.1.48](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10148-release-notes.md), [MariaDB 10.2.35](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-10235-release-notes.md), [MariaDB 10.3.26](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-10326-release-notes.md), [MariaDB 10.4.16](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-4-series/mariadb-10416-release-notes.md) and [MariaDB 10.5.7](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1057-release-notes.md), a different fix was implemented. Instead of truncating decimal values after every division, they are instead truncated for comparison purposes only.



 For example



 Versions other than [MariaDB 10.1.46](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10146-release-notes.md), [MariaDB 10.1.47](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10147-release-notes.md), [MariaDB 10.2.33](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-10233-release-notes.md), [MariaDB 10.2.34](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-10234-release-notes.md), [MariaDB 10.2.35](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-10235-release-notes.md), [MariaDB 10.3.24](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-10324-release-notes.md), [MariaDB 10.3.25](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-10325-release-notes.md), [MariaDB 10.4.14](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-4-series/mariadb-10414-release-notes.md), [MariaDB 10.4.15](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-4-series/mariadb-10415-release-notes.md), [MariaDB 10.5.5](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1055-release-notes.md) and [MariaDB 10.5.6](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1056-release-notes.md):



```
SELECT (55/23244*1000);
+-----------------+
| (55/23244*1000) |
+-----------------+
|          2.3662 |
+-----------------
```

 [MariaDB 10.1.46](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10146-release-notes.md), [MariaDB 10.1.47](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10147-release-notes.md), [MariaDB 10.2.33](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-10233-release-notes.md), [MariaDB 10.2.34](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-10234-release-notes.md), [MariaDB 10.2.35](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-10235-release-notes.md), [MariaDB 10.3.24](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-10324-release-notes.md), [MariaDB 10.3.25](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-10325-release-notes.md), [MariaDB 10.4.14](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-4-series/mariadb-10414-release-notes.md), [MariaDB 10.4.15](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-4-series/mariadb-10415-release-notes.md), [MariaDB 10.5.5](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1055-release-notes.md) and [MariaDB 10.5.6](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1056-release-notes.md) only:



```
SELECT (55/23244*1000);
+-----------------+
| (55/23244*1000) |
+-----------------+
|          2.4000 |
+-----------------+
```

 This is because the intermediate result, `<code>SELECT 55/23244</code>` takes into account `<code>div_precision_increment</code>` and results were truncated after every division in those versions only.



* Commandline: `<code class="fixed" style="white-space:pre-wrap">--div-precision-increment=#</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>4</code>`
* Range: `<code>0</code>` to `<code>30</code>`



#### `<code>encrypt_tmp_disk_tables</code>`


* Description: Enables automatic encryption of all internal on-disk temporary tables that are created during query execution if `<code>[aria_used_for_temp_tables=ON](../../../../reference/storage-engines/aria/aria-system-variables.md#aria_used_for_temp_tables)</code>` is set. See [Data at Rest Encryption](../../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/data-at-rest-encryption-overview.md) and [Enabling Encryption for Internal On-disk Temporary Tables](../../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/aria-encryption/aria-encryption-overview.md).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--encrypt-tmp-disk-tables[={0|1}]</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`



#### `<code>encrypt_tmp_files</code>`


* Description: Enables automatic encryption of temporary files, such as those created for filesort operations, binary log file caches, etc. See [Data at Rest Encryption](../../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/data-at-rest-encryption-overview.md).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--encrypt-tmp-files[={0|1}]</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`



#### `<code>encryption_algorithm</code>`


* Description: Which encryption algorithm to use for table encryption. `<code>aes_cbc</code>` is the recommended one. See [Table and Tablespace Encryption](../../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/data-at-rest-encryption-overview.md).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--encryption-algorithm=value</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>enum</code>`
* Default Value: `<code>none</code>`
* Valid Values: `<code>none</code>`, `<code>aes_ecb</code>`, `<code>aes_cbc</code>`, `<code>aes_ctr</code>`
* Introduced: [MariaDB 10.1.3](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-3-release-notes.md)
* Removed: [MariaDB 10.1.4](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-4-release-notes.md)



#### `<code>enforce_storage_engine</code>`


* Description: Force the use of a particular storage engine for new tables. Used to avoid unwanted creation of tables using another engine. For example, setting to [InnoDB](../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/innodb-upgrade-tests/README.md) will prevent any [MyISAM](../../../../reference/storage-engines/myisam-storage-engine/myisam-system-variables.md) tables from being created. If another engine is specified in a [CREATE TABLE](../../../../reference/sql-statements-and-structure/vectors/create-table-with-vectors.md) statement, the outcome depends on whether the `<code>NO_ENGINE_SUBSTITUTION</code>` [SQL_MODE](../../../../server-management/variables-and-modes/sql-mode.md) has been set or not. If set, the query will fail, while if not set, a warning will be returned and the table created according to the engine specified by this variable. The variable has a session scope, but is only modifiable by a user with the SUPER privilege.
* Commandline: None
* Scope: Session
* Dynamic: Yes
* Data Type: `<code>string</code>`
* Default Value: `<code>none</code>`



#### `<code>engine_condition_pushdown</code>`


* Description: Deprecated in [MariaDB 5.5](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5.md) and removed and replaced by the [optimizer_switch](#optimizer_switch) `<code>engine_condition_pushdown={on|off}</code>` flag in [MariaDB 10.0](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md).. Specifies whether the engine condition pushdown optimization is enabled. Since [MariaDB 10.1.1](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-1-release-notes.md), engine condition pushdown is enabled for all engines that support it.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--engine-condition-pushdown</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`
* Deprecated: [MariaDB 5.5](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5.md)
* Removed: [MariaDB 10.0](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md)



#### `<code>eq_range_index_dive_limit</code>`


* Description: Limit used for speeding up queries listed by long nested INs. The optimizer will use existing index statistics instead of doing index dives for equality ranges if the number of equality ranges for the index is larger than or equal to this number. If set to `<code>0</code>` (unlimited), index dives are always used.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--eq-range-index-dive-limit=#</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>200</code>`
* Range: `<code>0</code>` to `<code>4294967295</code>`



#### `<code>error_count</code>`


* Description: Read-only variable denoting the number of errors from the most recent statement in the current session that generated errors. See [SHOW_ERRORS()](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-errors.md).
* Scope: Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`



#### `<code>event_scheduler</code>`


* Description: Status of the [Event](../../../programming-customizing-mariadb/triggers-events/event-scheduler/events.md) Scheduler. Can be set to `<code>ON</code>` or `<code>OFF</code>`, while `<code>DISABLED</code>` means it cannot be set at runtime. Setting the variable will cause a load of events if they were not loaded at startup.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--event-scheduler[=value]</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>enumeration</code>`
* Default Value: `<code>OFF</code>`
* Valid Values: `<code>ON</code>` (or `<code>1</code>`), `<code>OFF</code>` (or `<code>0</code>`), `<code>DISABLED</code>`



#### `<code>expensive_subquery_limit</code>`


* Description: Number of rows to be examined for a query to be considered expensive, that is, maximum number of rows a subquery may examine in order to be executed during optimization and used for constant optimization.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--expensive-subquery-limit=#</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>100</code>`
* Range: `<code>0</code>` upwards



#### `<code>explicit_defaults_for_timestamp</code>`


* Description: This option causes [CREATE TABLE](../../../../reference/sql-statements-and-structure/vectors/create-table-with-vectors.md) to create all [TIMESTAMP](../../../../reference/sql-statements-and-structure/sql-statements/built-in-functions/date-time-functions/timestamp-function.md) columns as [NULL](../../../../reference/data-types/null-values.md) with the DEFAULT NULL attribute, Without this option, TIMESTAMP columns are NOT NULL and have implicit DEFAULT clauses.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--explicit-defaults-for-timestamp=[={0|1}]</code>`
* Scope:

  * Global, Session (>= [MariaDB 10.8.4](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-8-series/mariadb-1084-release-notes.md), [MariaDB 10.7.5](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-7-series/mariadb-1075-release-notes.md), [MariaDB 10.6.9](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-1069-release-notes.md), [MariaDB 10.5.17](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-10517-release-notes.md))
  * Global (<= [MariaDB 10.8.3](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-8-series/mariadb-1083-release-notes.md), [MariaDB 10.7.4](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-7-series/mariadb-1074-release-notes.md), [MariaDB 10.6.8](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-1068-release-notes.md), [MariaDB 10.5.16](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-10516-release-notes.md))
* Dynamic:

  * Yes (>= [MariaDB 10.8.4](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-8-series/mariadb-1084-release-notes.md), [MariaDB 10.7.5](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-7-series/mariadb-1075-release-notes.md), [MariaDB 10.6.9](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-1069-release-notes.md), [MariaDB 10.5.17](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-10517-release-notes.md))
  * No (<= [MariaDB 10.8.3](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-8-series/mariadb-1083-release-notes.md), [MariaDB 10.7.4](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-7-series/mariadb-1074-release-notes.md), [MariaDB 10.6.8](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-1068-release-notes.md), [MariaDB 10.5.16](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-10516-release-notes.md))
* Data Type: `<code>boolean</code>`
* Default Value:`<code>ON</code>` (>= [MariaDB 10.10](../../../../../release-notes/mariadb-community-server/what-is-mariadb-1010.md)), `<code>OFF</code>` (<= [MariaDB 10.9](../../../../../release-notes/mariadb-community-server/what-is-mariadb-109.md))



#### `<code>external_user</code>`


* Description: External user name set by the plugin used to authenticate the client. `<code>NULL</code>` if native MariaDB authentication is used. For example, from [MariaDB 11.6](../../../../../release-notes/mariadb-community-server/what-is-mariadb-116.md), the [Unix socket authentication plugin](../../../../reference/plugins/authentication-plugins/authentication-plugin-unix-socket.md) permits an authentication string, so that the OS and MariaDB user will be different. `<code>external_user</code>` then contains the external OS user. See [Authentication Plugin - Unix Socket: Creating Users](../../../../reference/plugins/authentication-plugins/authentication-plugin-unix-socket.md#creating-users)
* Scope: Session
* Dynamic: No
* Data Type: `<code>string</code>`
* Default Value: `<code>NULL</code>`



#### `<code>flush</code>`


* Description: Usually, MariaDB writes changes to disk after each SQL statement, and the operating system handles synchronizing (flushing) it to disk. If set to `<code>ON</code>`, the server will synchronize all changes to disk after each statement.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--flush</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`



#### `<code>flush_time</code>`


* Description: Interval in seconds that tables are closed to synchronize (flush) data to disk and free up resources. If set to 0, the default, there is no automatic synchronizing tables and closing of tables. This option should not be necessary on systems with sufficient resources.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--flush_time=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>0</code>`



#### `<code>foreign_key_checks</code>`


* Description: If set to 1 (the default) [foreign key constraints](../optimization-and-indexes/foreign-keys.md) (including ON UPDATE and ON DELETE behavior) [InnoDB](../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/innodb-upgrade-tests/README.md) tables are checked, while if set to 0, they are not checked. `<code>0</code>` is not recommended for normal use, though it can be useful in situations where you know the data is consistent, but want to reload data in a different order from that that specified by parent/child relationships. Setting this variable to 1 does not retrospectively check for inconsistencies introduced while set to 0.
* Commandline: None
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>1</code>`



#### `<code>ft_boolean_syntax</code>`


* Description: List of operators supported by an IN BOOLEAN MODE [full-text search](../optimization-and-indexes/full-text-indexes/README.md). If you wish to change, note that each character must be ASCII and non-alphanumeric, the full string must be 14 characters and the first or second character must be a space (marking the behavior by default). Positions 10, 13 and 14 are reserved for future extensions. Also, no duplicates are permitted except for the phrase quoting characters in positions 11 and 12, which may be the same.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--ft-boolean-syntax=name</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>string</code>`
* Default Value: `<code>+ -><()*:""&|</code>`



#### `<code>ft_max_word_len</code>`


* Description: Maximum length for a word to be included in the [MyISAM](../../../../reference/storage-engines/myisam-storage-engine/myisam-system-variables.md) [full-text index](../optimization-and-indexes/full-text-indexes/README.md). If this variable is changed, the full-text index must be rebuilt in order for the new value to take effect. The quickest way to do this is by issuing a `<code class="fixed" style="white-space:pre-wrap">REPAIR TABLE table_name QUICK</code>` statement. See [innodb_ft_max_token_size](../../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_ft_max_token_size) for the [InnoDB](../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/innodb-upgrade-tests/README.md) equivalent.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--ft-max-word-len=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value: `<code>84</code>`
* Minimum Value: `<code>10</code>`



#### `<code>ft_min_word_len</code>`


* Description: Minimum length for a word to be included in the [MyISAM](../../../../reference/storage-engines/myisam-storage-engine/myisam-system-variables.md) [full-text index](../optimization-and-indexes/full-text-indexes/README.md). If this variable is changed, the full-text index must be rebuilt in order for the new value to take effect. The quickest way to do this is by issuing a `<code class="fixed" style="white-space:pre-wrap">REPAIR TABLE table_name QUICK</code>` statement. See [innodb_ft_min_token_size](../../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_ft_min_token_size) for the [InnoDB](../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/innodb-upgrade-tests/README.md) equivalent.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--ft-min-word-len=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value: `<code>4</code>`
* Minimum Value: `<code>1</code>`



#### `<code>ft_query_expansion_limit</code>`


* Description: For [full-text searches](../optimization-and-indexes/full-text-indexes/README.md), denotes the numer of top matches when using WITH QUERY EXPANSION.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--ft-query-expansion-limit=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value: `<code>20</code>`
* Range: `<code>0</code>` to `<code>1000</code>`



#### `<code>ft_stopword_file</code>`


* Description: File containing a list of [stopwords](../optimization-and-indexes/full-text-indexes/full-text-index-stopwords.md) for use in [MyISAM](../../../../reference/storage-engines/myisam-storage-engine/myisam-system-variables.md) [full-text searches](../optimization-and-indexes/full-text-indexes/README.md). Unless an absolute path is specified the file will be looked for in the data directory. The file is not parsed for comments, so all words found become stopwords. By default, a built-in list of words (built from `<code>storage/myisam/ft_static.c file</code>`) is used. Stopwords can be disabled by setting this variable to `<code>''</code>` (an empty string). If this variable is changed, the full-text index must be rebuilt. The quickest way to do this is by issuing a `<code class="fixed" style="white-space:pre-wrap">REPAIR TABLE table_name QUICK</code>` statement. See [innodb_ft_server_stopword_table](../../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_ft_server_stopword_table) for the [InnoDB](../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/innodb-upgrade-tests/README.md) equivalent.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--ft-stopword-file=file_name</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>file name</code>`
* Default Value: `<code>(built-in)</code>`



#### `<code>general_log</code>`


* Description: If set to 0, the default unless the --general-log option is used, the [general query log](../../../../server-management/server-monitoring-logs/general-query-log.md) is disabled, while if set to 1, the general query log is enabled. See [log_output](#log_output) for how log files are written. If that variable is set to `<code>NONE</code>`, no logs will be written even if general_query_log is set to `<code>1</code>`.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--general-log</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>0</code>`



#### `<code>general_log_file</code>`


* Description: Name of the [general query log](../../../../server-management/server-monitoring-logs/general-query-log.md) file. If this is not specified, the name is taken from the [log-basename](../../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md#-log-basename) setting or from your system hostname with `<code class="highlight fixed" style="white-space:pre-wrap">.log</code>` as a suffix. If [--log-basename](../../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md#-log-basename) is also set, `<code>general_log_file</code>` should be placed after in the config files. Later settings override earlier settings, so `<code>log-basename</code>` will override any earlier log file name settings.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--general-log-file=file_name</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>file name</code>`
* Default Value: `<code><em>host_name</em>.log</code>`



#### `<code>group_concat_max_len</code>`


* Description: Maximum length in bytes of the returned result for the functions [GROUP_CONCAT()](../../../../reference/sql-statements-and-structure/sql-statements/built-in-functions/aggregate-functions/group_concat.md), [JSON_OBJECTAGG](../../../../reference/sql-statements-and-structure/sql-statements/built-in-functions/special-functions/json-functions/json_objectagg.md) and [JSON_ARRAYAGG](../../../../reference/sql-statements-and-structure/sql-statements/built-in-functions/special-functions/json-functions/json_arrayagg.md).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--group-concat-max-len=#</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value:

  * `<code>1048576</code>` (1M)
* Range: `<code>4</code>` to `<code>4294967295</code>`



.


#### `<code>have_compress</code>`


* Description: If the zlib compression library is accessible to the server, this will be set to `<code>YES</code>`, otherwise it will be `<code>NO</code>`. The [COMPRESS()](../../../../reference/sql-statements-and-structure/sql-statements/built-in-functions/secondary-functions/encryption-hashing-and-compression-functions/compress.md) and [UNCOMPRESS()](../../../../reference/sql-statements-and-structure/sql-statements/built-in-functions/secondary-functions/encryption-hashing-and-compression-functions/uncompress.md) functions will only be available if set to `<code>YES</code>`.
* Scope: Global
* Dynamic: No



#### `<code>have_crypt</code>`


* Description: If the crypt() system call is available this variable will be set to `<code>YES</code>`, otherwise it will be set to `<code>NO</code>`. If set to `<code>NO</code>`, the [ENCRYPT()](../../../../reference/mariadb-internals/encryption-plugin-api.md) function cannot be used.
* Scope: Global
* Dynamic: No



#### `<code>have_csv</code>`


* Description: If the server supports [CSV tables](../../../../reference/storage-engines/csv/csv-overview.md), will be set to `<code>YES</code>`, otherwise will be set to `<code>NO</code>`. Removed in [MariaDB 10.0](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md), use the [Information Schema PLUGINS](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/plugins-table-information-schema.md) table or [SHOW ENGINES](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-engines.md) instead.
* Scope: Global
* Dynamic: No
* Removed: [MariaDB 10.0](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md)



#### `<code>have_dynamic_loading</code>`


* Description: If the server supports dynamic loading of [plugins](../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/general-development-information/development-plans/old-plans/plugins-storage-engines-summit-for-mysqlmariadbdrizzle-2011.md), will be set to `<code>YES</code>`, otherwise will be set to `<code>NO</code>`.
* Scope: Global
* Dynamic: No



#### `<code>have_geometry</code>`


* Description: If the server supports spatial data types, will be set to `<code>YES</code>`, otherwise will be set to `<code>NO</code>`.
* Scope: Global
* Dynamic: No



#### `<code>have_ndbcluster</code>`


* Description: If the server supports NDBCluster ([disabled in MariaDB](ndb-disabled-in-mariadb)).
* Scope: Global
* Dynamic: No
* Removed: [MariaDB 10.0](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md)



#### `<code>have_partitioning</code>`


* Description: If the server supports partitioning, will be set to `<code>YES</code>`, unless the `<code>--skip-partition</code>` option is used, in which case will be set to `<code>DISABLED</code>`. Will be set to `<code>NO</code>` otherwise. Removed in [MariaDB 10.0](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md) - [SHOW PLUGINS](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-plugins-soname.md) should be used instead.
* Scope: Global
* Dynamic: No
* Removed: [MariaDB 10.0](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md)



#### `<code>have_profiling</code>`


* Description: If statement profiling is available, will be set to `<code>YES</code>`, otherwise will be set to `<code>NO</code>`. See [SHOW PROFILES()](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-profiles.md) and [SHOW PROFILE()](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-profile.md).
* Scope: Global
* Dynamic: No



#### `<code>have_query_cache</code>`


* Description: If the server supports the [query cache](../../../../reference/plugins/other-plugins/query-cache-information-plugin.md), will be set to `<code>YES</code>`, otherwise will be set to `<code>NO</code>`.
* Scope: Global
* Dynamic: No



#### `<code>have_rtree_keys</code>`


* Description: If RTREE indexes (used for [spatial indexes](../../../../reference/sql-statements-and-structure/geographic-geometric-features/spatial-index.md)) are available, will be set to `<code>YES</code>`, otherwise will be set to `<code>NO</code>`.
* Scope: Global
* Dynamic: No



#### `<code>have_symlink</code>`


* Description: This system variable can be used to determine whether the server supports symbolic links (note that it has no meaning on Windows).

  * If symbolic links are supported, then the value will be `<code>YES</code>`.
  * If symbolic links are not supported, then the value will be `<code>NO</code>`.
  * If symbolic links are disabled with the [--symbolic-links](../../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md#-symbolic-links) option and the `<code>skip</code>` [option prefix](../../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md#option-prefixes) (i.e. --skip-symbolic-links), then the value will be `<code>DISABLED</code>`.
  * Symbolic link support is required for the [INDEX DIRECTORY](../../../../reference/sql-statements-and-structure/vectors/create-table-with-vectors.md#data-directoryindex-directory) and [DATA DIRECTORY](../../../../reference/sql-statements-and-structure/vectors/create-table-with-vectors.md#data-directoryindex-directory) table options.
* Scope: Global
* Dynamic: No



#### `<code>histogram_size</code>`


* Description: Number of bytes used for a [histogram](../query-optimizations/statistics-for-optimizing-queries/histogram-based-statistics.md), or, from [MariaDB 10.7](../../../../../release-notes/mariadb-community-server/what-is-mariadb-107.md) when [histogram_type](#histogram_type) is set to `<code>JSON_HB</code>`, number of buckets. If set to 0, no histograms are created by [ANALYZE](../../../../reference/sql-statements-and-structure/sql-statements/table-statements/analyze-table.md).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--histogram-size=#</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>254</code>`
* Range: `<code>0</code>` to `<code>255</code>`



#### `<code>histogram_type</code>`


* Description: Specifies the type of [histograms](../query-optimizations/statistics-for-optimizing-queries/histogram-based-statistics.md) created by [ANALYZE](../../../../reference/sql-statements-and-structure/sql-statements/table-statements/analyze-table.md)..

  * `<code>SINGLE_PREC_HB</code>` - single precision height-balanced.
  * `<code>DOUBLE_PREC_HB</code>` - double precision height-balanced.
  * `<code>JSON_HB</code>` - JSON height-balanced histograms (from [MariaDB 10.8](../../../../../release-notes/mariadb-community-server/what-is-mariadb-108.md))
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--histogram-type=value</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>enumeration</code>`
* Default Value:

  * `<code>JSON_HB</code>` (>= [MariaDB 11.0](../../../../../release-notes/mariadb-community-server/what-is-mariadb-110.md))
  * `<code>DOUBLE_PREC_HB</code>` (<= [MariaDB 10.11](../../../../../release-notes/mariadb-community-server/what-is-mariadb-1011.md), >= [MariaDB 10.4.3](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-4-series/mariadb-1043-release-notes.md))
* Valid Values:

  * `<code>SINGLE_PREC_HB</code>`, `<code>DOUBLE_PREC_HB</code>` (<= [MariaDB 10.6](../../../../../release-notes/mariadb-community-server/what-is-mariadb-106.md))
  * `<code>SINGLE_PREC_HB</code>`, `<code>DOUBLE_PREC_HB</code>`, `<code>JSON_HB</code>` (>= [MariaDB 10.8](../../../../../release-notes/mariadb-community-server/what-is-mariadb-108.md))



#### `<code>host_cache_size</code>`


* Description: Number of host names that will be cached to avoid resolving. Setting to `<code>0</code>` disables the cache. Changing the value while the server is running causes an implicit [FLUSH HOSTS](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/flush-commands/flush-tables-for-export.md), clearing the host cache and truncating the [performance_schema.host_cache](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/performance-schema/performance-schema-tables/performance-schema-host_cache-table.md) table. If you are connecting from a lot of different machines you should consider increasing.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--host-cache-size=#</code>`.
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>128</code>`
* Range: `<code>0</code>` to `<code>65536</code>`



#### `<code>hostname</code>`


* Description: When the server starts, this variable is set to the server host name.
* Scope: Global
* Dynamic: No
* Data Type: `<code>string</code>`



#### `<code>identity</code>`


* Description: A synonym for [last_insert_id](#last_insert_id) variable.



#### `<code>idle_readonly_transaction_timeout</code>`


* Description: Time in seconds that the server waits for idle read-only transactions before killing the connection. If set to `<code>0</code>`, the default, connections are never killed. See also [idle_transaction_timeout](#idle_transaction_timeout), [idle_write_transaction_timeout](#idle_write_transaction_timeout) and [Transaction Timeouts](../../../../reference/sql-statements-and-structure/sql-statements/transactions/transaction-timeouts.md).
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>0</code>`
* Range: `<code>0</code>` to `<code>31536000</code>`



#### `<code>idle_transaction_timeout</code>`


* Description: Time in seconds that the server waits for idle transactions before killing the connection. If set to `<code>0</code>`, the default, connections are never killed. See also [idle_readonly_transaction_timeout](#idle_readonly_transaction_timeout), [idle_write_transaction_timeout](#idle_write_transaction_timeout) and [Transaction Timeouts](../../../../reference/sql-statements-and-structure/sql-statements/transactions/transaction-timeouts.md).
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>0</code>`
* Range: `<code>0</code>` to `<code>31536000</code>`



#### `<code>idle_write_transaction_timeout</code>`


* Description: Time in seconds that the server waits for idle read-write transactions before killing the connection. If set to `<code>0</code>`, the default, connections are never killed. See also [idle_transaction_timeout](#idle_transaction_timeout), [idle_readonly_transaction_timeout](#idle_readonly_transaction_timeout) and [Transaction Timeouts](../../../../reference/sql-statements-and-structure/sql-statements/transactions/transaction-timeouts.md). Called `<code>idle_readwrite_transaction_timeout</code>` until [MariaDB 10.3.2](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1032-release-notes.md).
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>0</code>`
* Range: `<code>0</code>` to `<code>31536000</code>`



#### `<code>ignore_db_dirs</code>`


* Description: Tells the server that this directory can never be a database. That means two things - firstly it is ignored by the [SHOW DATABASES](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-databases.md) command and [INFORMATION_SCHEMA](../../../../reference/mariadb-internals/information-schema-plugins-show-and-flush-statements.md) tables. And secondly, USE, CREATE DATABASE and SELECT statements will return an error if the database from the ignored list specified. Use this option several times if you need to ignore more than one directory. To make the list empty set the void value to the option as --ignore-db-dir=. If the option or configuration is specified multiple times, viewing this value will list the ignore directories separated by commas.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--ignore-db-dirs=dir</code>`.
* Scope: Global
* Dynamic: No
* Data Type: `<code>string</code>`



#### `<code>in_predicate_conversion_threshold</code>`


* Description: The minimum number of scalar elements in the value list of an IN predicate that triggers its conversion to an IN subquery. Set to 0 to disable the conversion. See [Conversion of Big IN Predicates Into Subqueries](../query-optimizations/subquery-optimizations/conversion-of-big-in-predicates-into-subqueries.md).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--in-predicate-conversion-threshold=#</code>`
* Scope: Global, Session
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value: `<code>1000</code>`
* Range: `<code>0</code>` to `<code>4294967295</code>`



#### `<code>in_transaction</code>`


* Description: Session-only and read-only variable that is set to `<code>1</code>` if a transaction is in progress, `<code>0</code>` if not.
* Commandline: No
* Scope: Session
* Dynamic: No
* Data Type: `<code>boolean</code>`
* Default Value: `<code>0</code>`



#### `<code>init_connect</code>`


* Description: String containing one or more SQL statements, separated by semicolons, that will be executed by the server for each client connecting. If there's a syntax error in the one of the statements, the client will fail to connect. For this reason, the statements are not executed for users with the [SUPER](../../../../reference/sql-statements-and-structure/sql-statements/account-management-sql-commands/grant.md#super) privilege or, from [MariaDB 10.5.2](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1052-release-notes.md), the [CONNECTION ADMIN](../../../../reference/sql-statements-and-structure/sql-statements/account-management-sql-commands/grant.md#connection-admin) privilege, who can then still connect and correct the error. See also [init_file](#init_file).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--init-connect=name</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>string</code>`



#### `<code>init_file</code>`


* Description: Name of a file containing SQL statements that will be executed by the server on startup. Each statement should be on a new line, and end with a semicolon. See also [init_connect](#init_connect).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">init-file=file_name</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>file name</code>`



#### `<code>insert_id</code>`


* Description: Value to be used for the next statement inserting a new [AUTO_INCREMENT](../../../../reference/storage-engines/innodb/auto_increment-handling-in-innodb.md) value.
* Scope: Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`



#### `<code>interactive_timeout</code>`


* Description: Time in seconds that the server waits for an interactive connection (one that connects with the mysql_real_connect() CLIENT_INTERACTIVE option) to become active before closing it. See also [wait_timeout](#wait_timeout).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--interactive-timeout=#</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>28800</code>`
* Range: (Windows): `<code>1</code>` to `<code>2147483</code>`
* Range: (Other): `<code>1</code>` to `<code>31536000</code>`



#### `<code>join_buffer_size</code>`


* Description: Minimum size in bytes of the buffer used for queries that cannot use an index, and instead perform a full table scan. Increase to get faster full joins when adding indexes is not possible, although be aware of memory issues, since joins will always allocate the minimum size. Best left low globally and set high in sessions that require large full joins. In 64-bit platforms, Windows truncates values above 4GB to 4GB with a warning. See also [Block-Based Join Algorithms - Size of Join Buffers](../../../../reference/mariadb-internals/mariadb-internals-documentation-query-optimizer/block-based-join-algorithms.md#size-of-join-buffers).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--join-buffer-size=#</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>262144</code>` (256kB)
* Range (non-Windows): `<code>128</code>` to `<code>18446744073709547520</code>`
* Range (Windows): `<code>8228</code>` to `<code>18446744073709547520</code>`



#### `<code>join_buffer_space_limit</code>`


* Description: Maximum size in bytes of the query buffer, By default 1024*128*10. See [Block-based join algorithms](../../../../reference/mariadb-internals/mariadb-internals-documentation-query-optimizer/block-based-join-algorithms.md#size-of-join-buffers).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--join-buffer-space-limit=#</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>2097152</code>`
* Range: `<code>2048</code>` to `<code>18446744073709551615</code>`



#### `<code>join_cache_level</code>`


* Description: Controls which of the eight block-based algorithms can be used for join operations. See [Block-based join algorithms](../../../../reference/mariadb-internals/mariadb-internals-documentation-query-optimizer/block-based-join-algorithms.md) for more information.

  * 1 – flat (Block Nested Loop) BNL
  * 2 – incremental BNL
  * 3 – flat Block Nested Loop Hash (BNLH)
  * 4 – incremental BNLH
  * 5 – flat Batch Key Access (BKA)
  * 6 – incremental BKA
  * 7 – flat Batch Key Access Hash (BKAH)
  * 8 – incremental BKAH
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--join-cache-level=#</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>2</code>`
* Range: `<code>0</code>` to `<code>8</code>`



#### `<code>keep_files_on_create</code>`


* Description: If a [MyISAM](../../../../reference/storage-engines/myisam-storage-engine/myisam-system-variables.md) table is created with no DATA DIRECTORY option, the .MYD file is stored in the database directory. When set to `<code>0</code>`, the default, if MariaDB finds another .MYD file in the database directory it will overwrite it. Setting this variable to `<code>1</code>` means that MariaDB will return an error instead, just as it usually does in the same situation outside of the database directory. The same applies for .MYI files and no INDEX DIRECTORY option. Deprecated in [MariaDB 10.8.0](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-8-series/mariadb-10-8-0-release-notes.md).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--keep-files-on-create=#</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`
* Deprecated: [MariaDB 10.8.0](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-8-series/mariadb-10-8-0-release-notes.md)



#### `<code>large_files_support</code>`


* Description: ON if the server if was compiled with large file support or not, else OFF
* Scope: Global
* Dynamic: No



#### `<code>large_page_size</code>`


* Description: Indicates the size of memory page if large page support (Linux only) is enabled. The page size is determined from the Hugepagesize setting in `<code>/proc/meminfo</code>`. See [large_pages](#large_pages). Deprecated and unused in [MariaDB 10.5.3](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1053-release-notes.md) since multiple page size support was added.
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value: Autosized (see description)
* Deprecated: [MariaDB 10.5.3](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1053-release-notes.md)



#### `<code>large_pages</code>`


* Description: Indicates whether large page support (prior to [MariaDB 10.5](../../../../../release-notes/mariadb-community-server/what-is-mariadb-105.md), Linux only, by now supported Windows and BSD distros, also called huge pages) is used. This is set with `<code>--large-pages</code>` or disabled with `<code>--skip-large-pages</code>`. Large pages are used for the [innodb buffer pool](../../../../reference/storage-engines/innodb/innodb-buffer-pool.md) and for online DDL (of size 3* [innodb_sort_buffer_size](../../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_sort_buffer_size) (or 6 when encryption is used)). To use large pages, the Linux `<code>sysctl</code>` variable `<code>kernel.shmmax</code>` must be large than the llocation. Also the `<code>sysctl</code>` variable `<code>vm.nr_hugepages</code>` multipled by [large-page](#large_page_size)) must be larger than the usage. The ulimit for locked memory must be sufficient to cover the amount used (`<code>ulimit -l</code>` and equalivent in /etc/security/limits.conf / or in systemd [LimitMEMLOCK](../../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/systemd.md)). If these operating system controls or insufficient free huge pages are available, the allocation of large pages will fall back to conventional memory allocation and a warning will appear in the logs. Only allocations of the default `<code>Hugepagesize</code>` currently occur (see `<code>/proc/meminfo</code>`).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--large-pages</code>`, `<code class="fixed" style="white-space:pre-wrap">--skip-large-pages</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`



#### `<code>last_insert_id</code>`


* Description: Contains the same value as that returned by [LAST_INSERT_ID()](../../../../reference/sql-statements-and-structure/sql-statements/built-in-functions/secondary-functions/information-functions/last_insert_id.md). Note that setting this variable doen't update the value returned by the underlying function.
* Scope: Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`



#### `<code>lc_messages</code>`


* Description: This system variable can be specified as a [locale](../../../../reference/data-types/string-data-types/character-sets/internationalization-and-localization/server-locale.md) name. The language of the associated [locale](../../../../reference/data-types/string-data-types/character-sets/internationalization-and-localization/server-locale.md) will be used for error messages. See [Server Locales](../../../../reference/data-types/string-data-types/character-sets/internationalization-and-localization/server-locale.md) for a list of supported locales and their associated languages.

  * This system variable is set to `<code>en_US</code>` by default, which means that error messages are in English by default.
  * If this system variable is set to a valid [locale](../../../../reference/data-types/string-data-types/character-sets/internationalization-and-localization/server-locale.md) name, but the server can't find an [error message file](../../../../server-management/server-monitoring-logs/error-log.md#error-messages-file) for the language associated with the [locale](../../../../reference/data-types/string-data-types/character-sets/internationalization-and-localization/server-locale.md), then the default language will be used instead.
  * This system variable is used along with the `<code>[lc_messages_dir](#lc_messages_dir)</code>` system variable to construct the path to the [error messages file](../../../../server-management/server-monitoring-logs/error-log.md#error-messages-file).
  * See [Setting the Language for Error Messages](../../../../reference/data-types/string-data-types/character-sets/internationalization-and-localization/setting-the-language-for-error-messages.md) for more information.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--lc-messages=name</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>string</code>`
* Default Value: `<code>en_us</code>`



#### `<code>lc_messages_dir</code>`


* Description: This system variable can be specified either as the path to the directory storing the server's [error message files](../../../../server-management/server-monitoring-logs/error-log.md#error-messages-file) or as the path to the directory storing the specific language's [error message file](../../../../server-management/server-monitoring-logs/error-log.md#error-messages-file). See [Server Locales](../../../../reference/data-types/string-data-types/character-sets/internationalization-and-localization/server-locale.md) for a list of available locales and their related languages.

  * The server initially tries to interpret the value of this system variable as a path to the directory storing the server's [error message files](../../../../server-management/server-monitoring-logs/error-log.md#error-messages-file). Therefore, it constructs the path to the language's [error message file](../../../../server-management/server-monitoring-logs/error-log.md#error-messages-file) by concatenating the value of this system variable with the language name of the [locale](../../../../reference/data-types/string-data-types/character-sets/internationalization-and-localization/server-locale.md) specified by the `<code>[lc_messages](server-system-variables.md#lc_messages)</code>` system variable .
  * If the server does not find the [error message file](../../../../server-management/server-monitoring-logs/error-log.md#error-messages-file) for the language, then it tries to interpret the value of this system variable as a direct path to the directory storing the specific language's [error message file](../../../../server-management/server-monitoring-logs/error-log.md#error-messages-file).
  * See [Setting the Language for Error Messages](../../../../reference/data-types/string-data-types/character-sets/internationalization-and-localization/setting-the-language-for-error-messages.md) for more information.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--lc-messages-dir=path</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>directory name</code>`



#### `<code>lc_time_names</code>`


* Description: The locale that determines the language used for the date and time functions [DAYNAME()](../../../../reference/sql-statements-and-structure/sql-statements/built-in-functions/date-time-functions/dayname.md), [MONTHNAME()](../../../../reference/sql-statements-and-structure/sql-statements/built-in-functions/date-time-functions/monthname.md) and [DATE_FORMAT()](https://mariadb.com/kb/en/date-format). Locale names are language and region subtags, for example 'en_ZA' (English - South Africa) or 'es_US: Spanish - United States'. The default is always 'en-US' regardless of the system's locale setting. See [server locale](../../../../reference/data-types/string-data-types/character-sets/internationalization-and-localization/server-locale.md) for a full list of supported locales.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--lc-time-names=name</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>string</code>`
* Default Value: `<code>en_US</code>`



#### `<code>legacy_xa_rollback_at_disconnect</code>`


* Description: If a user session disconnects after putting a transaction into the `<code>XA PREPARE</code>` state, roll back the transaction. Can be used for backwards compatibility to enable this pre-10.5 behavior for applications that expect it. Note that this violates the XA Specification and should not be used for new code.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Introduced: [MariaDB 10.5.27](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-10-5-27-release-notes.md), [MariaDB 10.6.20](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-10-6-20-release-notes.md), [MariaDB 10.11.10](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-11-series/mariadb-10-11-10-release-notes.md), [MariaDB 11.4.4](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-4-series/mariadb-11-4-4-release-notes.md), [MariaDB 11.7.1](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-7-rolling-releases/mariadb-11-7-1-release-notes.md)



#### `<code>license</code>`


* Description: Server license, for example `<code>GPL</code>`.
* Scope: Global
* Dynamic: No
* Data Type: `<code>string</code>`



#### `<code>local_infile</code>`


* Description: If set to `<code>1</code>`, LOCAL is supported for [LOAD DATA INFILE](../../../../reference/sql-statements-and-structure/sql-statements/data-manipulation/inserting-loading-data/load-data-into-tables-or-index/load-data-infile.md) statements. If set to `<code>0</code>`, usually for security reasons, attempts to perform a LOAD DATA LOCAL will fail with an error message.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--local-infile=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>ON</code>`



#### `<code>lock_wait_timeout</code>`


* Description: Timeout in seconds for attempts to acquire [metadata locks](../../../../reference/sql-statements-and-structure/sql-statements/transactions/metadata-locking.md). Statements using metadata locks include [FLUSH TABLES WITH READ LOCK](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/flush-commands/flush-tables-for-export.md), [LOCK TABLES](../../../../reference/sql-statements-and-structure/sql-statements/transactions/lock-tables.md), HANDLER and DML and DDL operations on tables, [stored procedures](../../../programming-customizing-mariadb/stored-routines/stored-procedures/README.md) and [functions](../../../programming-customizing-mariadb/stored-routines/stored-functions/README.md), and [views](../../../programming-customizing-mariadb/views/README.md). The timeout is separate for each attempt, of which there may be multiple in a single statement. `<code>0</code>` means no wait. See [WAIT and NOWAIT](../../../../reference/sql-statements-and-structure/sql-statements/transactions/wait-and-nowait.md).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--lock-wait-timeout=#</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value:

  * `<code>86400</code>` (1 day)
* Range:

  * `<code>0</code>` to `<code>31536000</code>`



#### `<code>locked_in_memory</code>`


* Description: Indicates whether --memlock was used to lock mariadbd in memory.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--memlock</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`



#### `<code>log</code>`


* Description: Deprecated and removed in [MariaDB 10.0](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md), use [general_log](#general_log) instead.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">-l [filename]</code>` or `<code class="fixed" style="white-space:pre-wrap">--log[=filename]</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>string</code>`
* Default Value: `<code>OFF</code>`
* Removed: [MariaDB 10.0](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md)



#### `<code>log_disabled_statements</code>`


* Description: If set, the specified type of statements (slave and/or stored procedure statements) will not be logged to the [general log](../../../../server-management/server-monitoring-logs/general-query-log.md). Multiple values are comma-separated, without spaces.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--log-disabled_statements=value</code>`
* Scope: Global, Session
* Dynamic: No
* Data Type: `<code>set</code>`
* Default Value: `<code>sp</code>`
* Valid Values: `<code>slave</code>` and/or `<code>sp</code>`, or empty string for none



#### `<code>log_error</code>`


* Description: Specifies the name of the [error log](../../../../server-management/server-monitoring-logs/error-log.md). If [--console](../../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md#-console) is specified later in the configuration (Windows only) or this option isn't specified, errors will be logged to stderr. If no name is provided, errors will still be logged to `<code>hostname.err</code>` in the `<code>datadir</code>` directory by default. If a configuration file sets `<code>--log-error</code>`, one can reset it with `<code>--skip-log-error</code>` (useful to override a system wide configuration file). MariaDB always writes its error log, but the destination is configurable. See [error log](../../../../server-management/server-monitoring-logs/error-log.md) for details. Note that if [--log-basename](../../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md#-log-basename) is also set, `<code>log_error</code>` should be placed after in the config files. Later settings override earlier settings, so `<code>log-basename</code>` will override any earlier log file name settings.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--log-error[=name]</code>`, `<code class="fixed" style="white-space:pre-wrap">--skip-log-error</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>file name</code>`
* Default Value: (empty string)



#### `<code>log_output</code>`


* Description: How the output for the [general query log](../../../../server-management/server-monitoring-logs/general-query-log.md) and the [slow query log](../../../../server-management/server-monitoring-logs/slow-query-log/slow-query-log-overview.md) is stored. By default written to file (`<code>FILE</code>`), it can also be stored in the [general_log](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/the-mysql-database-tables/mysqlgeneral_log-table.md) and [slow_log](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/the-mysql-database-tables/mysql-slow_log-table.md) tables in the mysql database (`<code>TABLE</code>`), or not stored at all (`<code>NONE</code>`). More than one option can be chosen at the same time, with `<code>NONE</code>` taking precedence if present. Logs will not be written if logging is not enabled. See [Writing logs into tables](../../../../server-management/server-monitoring-logs/writing-logs-into-tables.md), and the [slow_query_log](#slow_query_log) and [general_log](#general_log) server system variables.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--log-output=name</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>set</code>`
* Default Value: `<code>FILE</code>`
* Valid Values: `<code>TABLE</code>`, `<code>FILE</code>` or `<code>NONE</code>`



#### `<code>log_queries_not_using_indexes</code>`


* Description: Queries that don't use an index, or that perform a full index scan where the index doesn't limit the number of rows, will be logged to the [slow query log](../../../../server-management/server-monitoring-logs/slow-query-log/slow-query-log-overview.md) (regardless of time taken). The slow query log needs to be enabled for this to have an effect. Mapped to `<code>log_slow_filter='not_using_index'</code>` from [MariaDB 10.3.1](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1031-release-notes.md).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--log-queries-not-using-indexes</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`



#### `<code>log_slow_admin_statements</code>`


* Description: Log slow [OPTIMIZE](../optimizing-tables/optimize-table.md), [ANALYZE](../../../../reference/sql-statements-and-structure/sql-statements/table-statements/analyze-table.md), [ALTER](../../../../../general-resources/learning-and-training/training-and-tutorials/beginner-mariadb-articles/altering-tables-in-mariadb.md) and other [administrative](../../../../server-management/server-monitoring-logs/slow-query-log/slow-query-log-overview.md#logging-slow-administrative-statements) statements to the [slow log](../../../../server-management/server-monitoring-logs/slow-query-log/slow-query-log-overview.md) if it is open. See also [log_slow_disabled_statements](#log_slow_disabled_statements) and [log_slow_filter](#log_slow_filter). Deprecated, use [log_slow_filter](#log_slow_filter) without `<code>admin</code>`.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--log-slow-admin-statements</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value:

  * `<code>ON </code>`
* Deprecated: [MariaDB 11.0.1](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-0-series/mariadb-11-0-1-release-notes.md)



#### `<code>log_slow_disabled_statements</code>`


* Description: If set, the specified type of statements will not be logged to the [slow query log](../../../../server-management/server-monitoring-logs/slow-query-log/slow-query-log-overview.md). See also [log_slow_admin_statements](#log_slow_admin_statements) and [log_slow_filter](#log_slow_filter).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--log-slow-disabled_statements=value</code>`
* Scope: Global, Session
* Dynamic: No
* Data Type: `<code>set</code>`
* Default Value: `<code>sp</code>`
* Valid Vales: `<code>admin</code>`, `<code>call</code>`, `<code>slave</code>` and/or `<code>sp</code>`



#### `<code>log_slow_filter</code>`


* Description: Comma-delimited string (without spaces) containing one or more settings for filtering what is logged to the [slow query log](../../../../server-management/server-monitoring-logs/slow-query-log/slow-query-log-overview.md). If a query matches one of the types listed in the filter, and takes longer than [long_query_time](#long_query_time), it will be logged(except for 'not_using_index' which is always logged if enabled, regardless of the time). Sets [log-slow-admin-statements](#log_slow_admin_statements) to ON. See also [log_slow_disabled_statements](#log_slow_disabled_statements).

  * `<code>admin</code>` log [administrative](../../../../server-management/server-monitoring-logs/slow-query-log/slow-query-log-overview.md#logging-slow-administrative-statements) queries (create, optimize, drop etc...)
  * `<code>filesort</code>` logs queries that use a filesort.
  * `<code>filesort_on_disk</code>` logs queries that perform a a filesort on disk.
  * `<code>filesort_priority_queue</code>`
  * `<code>full_join</code>` logs queries that perform a join without indexes.
  * `<code>full_scan</code>` logs queries that perform full table scans.
  * `<code>not_using_index</code>` logs queries that don't use an index, or that perform a full index scan where the index doesn't limit the number of rows. Disregards [long_query_time](#long_query_time), unlike other options. [log_queries_not_using_indexes](#log_queries_not_using_indexes) maps to this option. From [MariaDB 10.3.1](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1031-release-notes.md).
  * `<code>query_cache</code>` log queries that are resolved by the query cache.
  * `<code>query_cache_miss</code>` logs queries that are not found in the [query cache](../../../../reference/plugins/other-plugins/query-cache-information-plugin.md).
  * `<code>tmp_table</code>` logs queries that create an implicit temporary table.
  * `<code>tmp_table_on_disk</code>` logs queries that create a temporary table on disk.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">log-slow-filter=value1[,value2...]</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>enumeration</code>`
* Default Value:

  * `<code>admin</code>`, `<code>filesort</code>`, `<code>filesort_on_disk</code>`, `<code>filesort_priority_queue</code>`, `<code>full_join</code>`, `<code>full_scan</code>`, `<code>query_cache</code>`, `<code>query_cache_miss</code>`, `<code>tmp_table</code>`, `<code>tmp_table_on_disk</code>`
* Valid Values:

  * `<code>admin</code>`, `<code>filesort</code>`, `<code>filesort_on_disk</code>`, `<code>filesort_priority_queue</code>`, `<code>full_join</code>`, `<code>full_scan</code>`, `<code>not_using_index</code>`, `<code>query_cache</code>`, `<code>query_cache_miss</code>`, `<code>tmp_table</code>`, `<code>tmp_table_on_disk</code>`



#### `<code>log_slow_max_warnings</code>`


* Description: Max numbers of warnings printed to slow query log per statement
* Commandline: `<code class="fixed" style="white-space:pre-wrap">log-slow-max-warnings=#</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>10</code>`
* Range: `<code>0</code>` to `<code>1000</code>`
* Introduced: [MariaDB 10.6.16](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-10-6-16-release-notes.md), [MariaDB 10.10.7](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-10-series/mariadb-10-10-7-release-notes.md), [MariaDB 10.11.6](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-11-series/mariadb-10-11-6-release-notes.md), [MariaDB 11.0.4](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-0-series/mariadb-11-0-4-release-notes.md), [MariaDB 11.1.3](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-1-series/mariadb-11-1-3-release-notes.md)



#### `<code>log_slow_min_examined_row_limit</code>`


* Description: Don't write queries to [slow query log](../../../../server-management/server-monitoring-logs/slow-query-log/slow-query-log-overview.md) that examine fewer rows than the set value. If set to `<code>0</code>`, the default, no row limit is used. `<code>min_examined_row_limit</code>` is an alias. From [MariaDB 11.7](../../../../../release-notes/mariadb-community-server/what-is-mariadb-117.md), queries slower than [log_slow_always_query_time](../../../../server-management/server-monitoring-logs/slow-query-log/log_slow_always_query_time-system-variable.md) will always be logged.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--log-slow-min-examined-row-limit=#</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>0</code>`
* Range: `<code>0-4294967295</code>`
* Introduced: [MariaDB 10.11](../../../../../release-notes/mariadb-community-server/what-is-mariadb-1011.md)



#### `<code>log_slow_queries</code>`


* Description: Deprecated and removed in [MariaDB 10.0](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md), use [slow_query_log](#slow_query_log) instead.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--log-slow-queries[=name]</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`
* Removed: [MariaDB 10.0](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md)



#### `<code>log_slow_query</code>`


* Description: If set to 0, the default unless the --slow-query-log option is used, the [slow query log](../../../../server-management/server-monitoring-logs/slow-query-log/slow-query-log-overview.md) is disabled, while if set to 1 (both global and session variables), the slow query log is enabled. Named [slow_query_log](#slow_query_log) before [MariaDB 10.11.0](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-11-series/mariadb-10-11-0-release-notes.md), which is now an alias.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--slow-query-log</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>0</code>`
* Introduced: [MariaDB 10.11.0](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-11-series/mariadb-10-11-0-release-notes.md)
* See also: See [log_output](#log_output) to see how log files are written. If that variable is set to `<code>NONE</code>`, no logs will be written even if log_slow_query is set to `<code>1</code>`.



#### `<code>log_slow_query_file</code>`


* Description: Name of the [slow query log](../../../../server-management/server-monitoring-logs/slow-query-log/slow-query-log-overview.md) file. Before [MariaDB 10.11](../../../../../release-notes/mariadb-community-server/what-is-mariadb-1011.md), was named [slow_query_log_file](#slow_query_log_file). This was named `<code>log_slow_query_file_name</code>` in the [MariaDB 10.11.0](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-11-series/mariadb-10-11-0-release-notes.md) preview release. If [--log-basename](../../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md#-log-basename) is also set, `<code>log_slow_query_file</code>` should be placed after in the config files. Later settings override earlier settings, so `<code>log-basename</code>` will override any earlier log file name settings.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--log-slow-query-file=file_name</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>file name</code>`
* Default Value: `<code><em>host_name</em>-slow.log</code>`
* Introduced: [MariaDB 10.11.0](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-11-series/mariadb-10-11-0-release-notes.md)



#### `<code>log_slow_query_time</code>`


* Description: If a query takes longer than this many seconds to execute (microseconds can be specified too), the [Slow_queries](server-status-variables.md#slow_queries) status variable is incremented and, if enabled, the query is logged to the [slow query log](../../../../server-management/server-monitoring-logs/slow-query-log/slow-query-log-overview.md). Before [MariaDB 10.11](../../../../../release-notes/mariadb-community-server/what-is-mariadb-1011.md), was named [long_query_time](#long_query_time). Affected by [log_slow_rate_limit](#log_slow_rate_limit) and [log_slow_min_examined_row_limit](#log_slow_min_examined_row_limit).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--log-slow-query-time=#</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>10.000000</code>`
* Range: `<code>0</code>` to `<code>31536000</code>`
* Introduced: [MariaDB 10.11.0](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-11-series/mariadb-10-11-0-release-notes.md)



#### `<code>log_slow_rate_limit</code>`


* Description: The [slow query log](../../../../server-management/server-monitoring-logs/slow-query-log/slow-query-log-overview.md) will log every this many queries. The default is `<code>1</code>`, or every query, while setting it to `<code>20</code>` would log every 20 queries, or five percent. Aims to reduce I/O usage and excessively large slow query logs. See also [Slow Query Log Extended Statistics](../query-optimizations/statistics-for-optimizing-queries/slow-query-log-extended-statistics.md). From [MariaDB 11.7](../../../../../release-notes/mariadb-community-server/what-is-mariadb-117.md), queries slower than [log_slow_always_query_time](../../../../server-management/server-monitoring-logs/slow-query-log/log_slow_always_query_time-system-variable.md) will always be logged.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">log-slow-rate-limit=#</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>1</code>`
* Range: `<code>1</code>` upwards



#### `<code>log_slow_verbosity</code>`


* Description: Controls information to be added to the [slow query log](../../../../server-management/server-monitoring-logs/slow-query-log/slow-query-log-overview.md). Options are added in a comma-delimited string. See also [Slow Query Log Extended Statistics](../query-optimizations/statistics-for-optimizing-queries/slow-query-log-extended-statistics.md). log_slow_verbosity is not supported when log_output='TABLE'.

  * `<code>query_plan</code>` logs query execution plan information
  * `<code>innodb</code>` Alias to `<code>engine</code>` (from [MariaDB 10.6.15](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-10-6-15-release-notes.md) and [MariaDB 10.11.5](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-11-series/mariadb-10-11-5-release-notes.md)), previously ignored.
  * `<code>explain</code>` prints EXPLAIN output in the [slow query log](../../../../server-management/server-monitoring-logs/slow-query-log/slow-query-log-overview.md). See [EXPLAIN in the Slow Query Log](../../../../server-management/server-monitoring-logs/slow-query-log/explain-in-the-slow-query-log.md).
  * `<code>engine</code>` Logs engine statistics (from [MariaDB 10.6.15](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-10-6-15-release-notes.md) and [MariaDB 10.11.5](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-11-series/mariadb-10-11-5-release-notes.md)).
  * `<code>warnings</code>` Print all errors, warnings and notes for the statement to the slow query log. (from [MariaDB 10.6.16](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-10-6-16-release-notes.md)).
  * `<code>all</code>` Enables all above options (From [MariaDB 10.6.16](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-10-6-16-release-notes.md))
  * `<code>full</code>` Enables all above options.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">log-slow-verbosity=value1[,value2...]</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>enumeration</code>`
* Default Value: (Empty)
* Valid Values:

  * >= [MariaDB 10.6.16](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-10-6-16-release-notes.md), [MariaDB 10.11.6](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-11-series/mariadb-10-11-6-release-notes.md): (Empty), `<code>query_plan</code>`, `<code>innodb</code>`, `<code>explain</code>`, `<code>engine</code>`, `<code>warnings</code>`, `<code>all</code>`, `<code>full</code>`
  * >= [MariaDB 10.6.15](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-10-6-15-release-notes.md), [MariaDB 10.11.5](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-11-series/mariadb-10-11-5-release-notes.md): (Empty), `<code>query_plan</code>`, `<code>innodb</code>`, `<code>explain</code>`, `<code>engine</code>`, `<code>full</code>`
  * <= [MariaDB 10.6.14](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-10-6-14-release-notes.md), [MariaDB 10.11.4](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-11-series/mariadb-10-11-4-release-notes.md): (Empty), `<code>query_plan</code>`, `<code>innodb</code>`, `<code>explain</code>`



#### `<code>log_tc_size</code>`


* Description: Defines the size in bytes of the memory-mapped file-based transaction coordinator log, which is only used if the [binary log](../../../../reference/storage-engines/innodb/binary-log-group-commit-and-innodb-flushing-performance.md) is disabled. If you have two or more XA-capable storage engines enabled, then a transaction coordinator log must be available. This size is defined in multiples of 4096. See [Transaction Coordinator Log](../../../../server-management/server-monitoring-logs/transaction-coordinator-log/transaction-coordinator-log-overview.md) for more information. Also see the `<code>[--log-tc](../../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md#-log-tc)</code>` server option and the `<code>[--tc-heuristic-recover](#-tc-heuristic-recover)</code>` option.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">log-tc-size=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value: `<code>24576</code>`
* Range: `<code>12288</code>` to `<code>18446744073709551615</code>`



#### `<code>log_warnings</code>`


* Description: Determines which additional warnings are logged. Setting to `<code>0</code>` disables additional warning logging. Note that this does not prevent all warnings, there is a core set of warnings that will always be written to the error log. The additional warnings are as follows:

  * log_warnings >= 1

    * [Event scheduler](../../../programming-customizing-mariadb/triggers-events/event-scheduler/README.md) information.
    * System signals
    * Wrong usage of `<code class="fixed" style="white-space:pre-wrap">--user</code>`
    * Failed setrlimit() and mlockall()
    * Changed limits
    * Wrong values of lower_case_table_names and stack_size
    * Wrong values for command line options
    * Start log position and some master information when starting slaves
    * Slave reconnects
    * Killed slaves
    * Error reading relay logs
    * [Unsafe statements for statement-based replication](../../standard-replication/unsafe-statements-for-statement-based-replication.md). If this warning occurs frequently, it is throttled to prevent flooding the log.
    * Disabled [plugins](../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/general-development-information/development-plans/old-plans/plugins-storage-engines-summit-for-mysqlmariadbdrizzle-2011.md) that one tried to enable or use.
    * UDF files that didn't include the required init functions.
    * DNS lookup failures.
  * log_warnings >= 2

    * Access denied errors.
    * Connections aborted or closed due to errors or timeouts.
    * Table handler errors
    * Messages related to the files used to [persist replication state](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md#option-persistence):

      * Either the default `<code>master.info</code>` file or the file that is configured by the `<code>[master_info_file](../../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md#-master-info-file)</code>` option.
      * Either the default `<code>relay-log.info</code>` file or the file that is configured by the `<code>[relay_log_info_file](../../standard-replication/replication-and-binary-log-system-variables.md#relay_log_info_file)</code>` system variable.
    * Information about a master's [binary log dump thread](../../standard-replication/replication-threads.md#binary-log-dump-thread).
  * log_warnings >= 3

    * All errors and warnings during [MyISAM](../../../../reference/storage-engines/myisam-storage-engine/myisam-system-variables.md) repair and auto recover.
    * Information about old-style language options.
    * Information about [progress of InnoDB online DDL](https://mariadb.org/monitoring-progress-and-temporal-memory-usage-of-online-ddl-in-innodb/).
  * log_warnings >=4

    * Connections aborted due to "Too many connections" errors.
    * Connections closed normally without authentication.
    * Connections aborted due to `<code>[KILL](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/kill.md)</code>`.
    * Connections closed due to released connections, such as when `<code>[completion_type](#completion_type)</code>` is set to `<code>RELEASE</code>`.
    * Could not read packet: (a lot more information)
    * All read/write errors for a connection are logged to the error log.
  * log_warnings >=9

    * Information about initializing plugins.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">-W [level]</code>` or `<code class="fixed" style="white-space:pre-wrap">--log-warnings[=level]</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value:

  * `<code>2</code>`
* Range: `<code>0</code>` to `<code>4294967295</code>`



#### `<code>long_query_time</code>`


* Description: If a query takes longer than this many seconds to execute (microseconds can be specified too), the [Slow_queries](server-status-variables.md#slow_queries) status variable is incremented and, if enabled, the query is logged to the [slow query log](../../../../server-management/server-monitoring-logs/slow-query-log/slow-query-log-overview.md). From [MariaDB 10.11.0](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-11-series/mariadb-10-11-0-release-notes.md), this is an alias for [log_slow_query_time](#log_slow_query_time).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--long-query-time=#</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>10.000000</code>`
* Range: `<code>0</code>` upwards



#### `<code>low_priority_updates</code>`


* Description: If set to 1 (0 is the default), for [storage engines](../../../../../general-resources/learning-and-training/video-presentations-and-screencasts/storage-engines-and-plugins-videos.md) that use only table-level locking ([Aria](../../../../reference/storage-engines/s3-storage-engine/aria_s3_copy.md), [MyISAM](../../../../reference/storage-engines/myisam-storage-engine/myisam-system-variables.md), [MEMORY](../../../../reference/storage-engines/memory-storage-engine.md) and [MERGE](../../../../reference/storage-engines/merge.md)), all INSERTs, UPDATEs, DELETEs and LOCK TABLE WRITEs will wait until there are no more SELECTs or LOCK TABLE READs pending on the relevant tables. Set this to 1 if reads are prioritized over writes. 

  * In [MariaDB 5.5](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5.md) and earlier, `<code>[sql_low_priority_updates](#sql_low_priority_updates)</code>` is a synonym.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--low-priority-updates</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>0</code>`



#### `<code>lower_case_file_system</code>`


* Description: Read-only variable describing whether the file system is case-sensitive. If set to `<code>OFF</code>`, file names are case-sensitive. If set to `<code>ON</code>`, they are not case-sensitive.
* Scope: Global
* Dynamic: No
* Data Type: `<code>boolean</code>`
* Default Value: `<code>##</code>`



#### `<code>lower_case_table_names</code>`


* Description: If set to `<code>0</code>` (the default on Unix-based systems), table names and aliases and database names are compared in a case-sensitive manner. If set to `<code>1</code>` (the default on Windows), names are stored in lowercase and not compared in a case-sensitive manner. If set to `<code>2</code>` (the default on Mac OS X), names are stored as declared, but compared in lowercase.
This system variable's value cannot be changed after the datadir has been initialized. lower_case_table_names is set when a MariaDB instance starts, and it remains constant afterwards.


* Commandline: `<code class="fixed" style="white-space:pre-wrap">--lower-case-table-names[=#]</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value: `<code>0</code>` (Unix), `<code>1</code>` (Windows), `<code>2</code>` (Mac OS X)
* Range: `<code>0</code>` to `<code>2</code>`



#### `<code>max_allowed_packet</code>`


* Description: Maximum size in bytes of a packet or a generated/intermediate string. The packet message buffer is initialized with the value from [net_buffer_length](#net_buffer_length), but can grow up to max_allowed_packet bytes. Set as large as the largest BLOB, in multiples of 1024. If this value is changed, it should be changed on the client side as well. See [slave_max_allowed_packet](../../standard-replication/replication-and-binary-log-system-variables.md) for a specific limit for replication purposes.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--max-allowed-packet=#</code>`
* Scope: Global, Session
* Dynamic: Yes (Global), No (Session)
* Data Type: `<code>numeric</code>`
* Default Value:

  * `<code>16777216</code>` (16M)
  * `<code>1073741824</code>` (1GB) (client-side)
* Range: `<code>1024</code>` to `<code>1073741824</code>`



#### `<code>max_connect_errors</code>`


* Description: Limit to the number of successive failed connects from a host before the host is blocked from making further connections. The count for a host is reset to zero if they successfully connect. To unblock, flush the host cache with a [FLUSH HOSTS](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/flush-commands/flush-tables-for-export.md) statement or [mariadb-admin flush-hosts](../../../../clients-and-utilities/mariadb-admin.md). The [performance_schema.host_cache](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/performance-schema/performance-schema-tables/performance-schema-host_cache-table.md) table contains the status of the current hosts.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--max-connect-errors=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>100</code>`
* Range: `<code>1</code>` to `<code>4294967295</code>`



#### `<code>max_connections</code>`


* Description: The maximum number of simultaneous client connections. See also [Handling Too Many Connections](handling-too-many-connections.md). Note that this value affects the number of file descriptors required on the operating system. Minimum was changed from `<code>1</code>` to `<code>10</code>` to avoid possible unexpected results for the user ([MDEV-18252](https://jira.mariadb.org/browse/MDEV-18252)). Note that MariaDB always has one reserved connection for a `<code>SUPER</code>` (or `<code>CONNECTION ADMIN</code>` user). Additionally it can listen on a separate port, so will be available even when the max_connections limit is reached.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--max-connections=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>151</code>`
* Range: `<code>10</code>` to `<code>100000</code>`



#### `<code>max_delayed_threads</code>`


* Description: Limits to the number of [INSERT DELAYED](../../../../reference/sql-statements-and-structure/sql-statements/data-manipulation/inserting-loading-data/insert-delayed.md) threads. Once this limit is reached, the insert is handled as if there was no DELAYED attribute. If set to `<code>0</code>`, DELAYED is ignored entirely. The session value can only be set to `<code>0</code>` or to the same as the global value.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--max-delayed-threads=#</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>20</code>`
* Range: `<code>0</code>` to `<code>16384</code>`



#### `<code>max_digest_length</code>`


* Description: Maximum length considered for computing a statement digest, such as used by the [Performance Schema](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/performance-schema/performance-schema-tables/performance-schema-table_handles-table.md) and query rewrite plugins. Statements that differ after this many bytes produce the same digest, and are aggregated for statistics purposes. The variable is allocated per session. Increasing will allow longer statements to be distinguished from each other, but increase memory use, while decreasing will reduce memory use, but more statements may become indistinguishable.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--max-digest-length=#</code>`
* Scope: Global,
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value: `<code>1024</code>`
* Range: `<code>0</code>` to `<code>1048576</code>`



#### `<code>max_error_count</code>`


* Description: Specifies the maximum number of messages stored for display by [SHOW ERRORS](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-errors.md) and [SHOW WARNINGS](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-warnings.md) statements.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--max-error-count=#</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>64</code>`
* Range: `<code>0</code>` to `<code>65535</code>`



#### `<code>max_heap_table_size</code>`


* Description: Maximum size in bytes for user-created [MEMORY](../../../../reference/storage-engines/memory-storage-engine.md) tables. Setting the variable while the server is active has no effect on existing tables unless they are recreated or altered. The smaller of max_heap_table_size and [tmp_table_size](#tmp_table_size) also limits internal in-memory tables. When the maximum size is reached, any further attempts to insert data will receive a "table ... is full" error. Temporary tables created with [CREATE TEMPORARY](../../../../reference/sql-statements-and-structure/vectors/create-table-with-vectors.md) will not be converted to Aria, as occurs with internal temporary tables, but will also receive a table full error.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--max-heap-table-size=#</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>16777216</code>`
* Range : `<code>16384</code>` to `<code>4294966272</code>`



#### `<code>max_insert_delayed_threads</code>`


* Description: Synonym for [max_delayed_threads](#max_delayed_threads).



#### `<code>max_join_size</code>`


* Description: Statements will not be performed if they are likely to need to examine more than this number of rows, row combinations or do more disk seeks. Can prevent poorly-formatted queries from taking server resources. Changing this value to anything other the default will reset [sql_big_selects](#sql_big_selects) to 0. If sql_big_selects is set again, max_join_size will be ignored. This limit is also ignored if the query result is sitting in the [query cache](../../../../reference/plugins/other-plugins/query-cache-information-plugin.md). Previously named [sql_max_join_size](#sql_max_join_size), which is still a synonym.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--max-join-size=#</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>18446744073709551615</code>`
* Range: `<code>1</code>` to `<code>18446744073709551615</code>`



#### `<code>max_length_for_sort_data</code>`


* Description: Used to decide which algorithm to choose when sorting rows. If the total size of the column data, not including columns that are part of the sort, is less than `<code>max_length_for_sort_data</code>`, then we add these to the sort key. This can speed up the sort as we don't have to re-read the same row again later. Setting the value too high can slow things down as there will be a higher disk activity for doing the sort.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--max-length-for-sort-data=#</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>1024</code>`
* Range: `<code>4</code>` to `<code>8388608</code>`



#### `<code>max_long_data_size</code>`


* Description: Maximum size for parameter values sent with mysql_stmt_send_long_data(). If not set, will default to the value of [max_allowed_packet](#max_allowed_packet). Deprecated in [MariaDB 5.5](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5.md) and removed in [MariaDB 10.5.0](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1050-release-notes.md); use [max_allowed_packet](#max_allowed_packet) instead.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--max-long-data-size=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value:

  * `<code>16777216</code>` (16M)
* Range: `<code>1024</code>` to `<code>4294967295</code>`
* Deprecated: [MariaDB 5.5](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5.md)
* Removed: [MariaDB 10.5.0](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1050-release-notes.md)



#### `<code>max_password_errors</code>`


* Description: The maximum permitted number of failed connection attempts due to an invalid password before a user is blocked from further connections. [FLUSH_PRIVILEGES](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/flush-commands/flush-tables-for-export.md) will permit the user to connect again. This limit is not applicable for users with the [SUPER](../../../../reference/sql-statements-and-structure/sql-statements/account-management-sql-commands/grant.md#super) privilege or, from [MariaDB 10.5.2](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1052-release-notes.md), the [CONNECTION ADMIN](../../../../reference/sql-statements-and-structure/sql-statements/account-management-sql-commands/grant.md#connection-admin) privilege, with a hostname of localhost, 127.0.0.1 or ::1. See also the [Information Schema USERS table](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-users-table.md).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--max-password-errors=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>4294967295</code>`
* Range: `<code>1</code>` to `<code>4294967295</code>`



#### `<code>max_prepared_stmt_count</code>`


* Description: Maximum number of prepared statements on the server. Can help prevent certain forms of denial-of-service attacks. If set to `<code>0</code>`, no prepared statements are permitted on the server.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--max-prepared-stmt-count=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>16382</code>`
* Range: `<code>0</code>` to `<code>4294967295</code>`



#### `<code>max_recursive_iterations</code>`


* Description: Maximum number of iterations when executing recursive queries, used to prevent infinite loops in [recursive CTEs](../../../../reference/sql-statements-and-structure/sql-statements/data-manipulation/selecting-data/common-table-expressions/recursive-common-table-expressions-overview.md).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--max-recursive-iterations=#</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>1000</code>` (>= [MariaDB 10.6.0](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-1060-release-notes.md)), `<code>4294967295</code>` (<= [MariaDB 10.5](../../../../../release-notes/mariadb-community-server/what-is-mariadb-105.md))
* Range: `<code>0</code>` to `<code>4294967295</code>`



#### `<code>max_rowid_filter_size</code>`


* Description: The maximum size of the container of a rowid filter.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--max-rowid-filter-size=#</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>131072</code>`
* Range: `<code>1024</code>` to `<code>18446744073709551615</code>`



#### `<code>max_seeks_for_key</code>`


* Description: The optimizer assumes that the number specified here is the most key seeks required when searching with an index, regardless of the actual index cardinality. If this value is set lower than its default and maximum, indexes will tend to be preferred over table scans.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--max-seeks-for-key=#</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>4294967295</code>`
* Range: `<code>1</code>` to `<code>4294967295</code>`



#### `<code>max_session_mem_used</code>`


* Description: Amount of memory a single user session is allowed to allocate. This limits the value of the session variable [Memory_used](server-status-variables.md#memory_used).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--max-session-mem-used=#</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>9223372036854775807</code>` (8192 PB)
* Range: `<code>8192</code>` to `<code>18446744073709551615</code>`



#### `<code>max_sort_length</code>`


* Description: Maximum size in bytes used for sorting data values - anything exceeding this is ignored. The server uses only the first `<code>max_sort_length</code>` bytes of each value and ignores the rest. Increasing this may require [sort_buffer_size](#sort_buffer_size) to be increased (especially if ER_OUT_OF_SORTMEMORY errors start appearing). From [MariaDB 11.7](../../../../../release-notes/mariadb-community-server/what-is-mariadb-117.md), a warning is generated when max_sort_length is exceeded.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--max-sort-length=#</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>1024</code>`
* Range:

  * `<code>4</code>` to `<code>8388608</code>` (<= [MariaDB 10.4.13](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-4-series/mariadb-10413-release-notes.md), [MariaDB 10.5.3](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1053-release-notes.md))
  * `<code>8</code>` to `<code>8388608</code>` (>= [MariaDB 10.4.14](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-4-series/mariadb-10414-release-notes.md), [MariaDB 10.5.4](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1054-release-notes.md))



#### `<code>max_sp_recursion_depth</code>`


* Description: Permitted number of recursive calls for a [stored procedure](../../../programming-customizing-mariadb/stored-routines/stored-procedures/README.md). `<code>0</code>`, the default, no recursion is permitted. Increasing this value increases the thread stack requirements, so you may need to increase [thread_stack](#thread_stack) as well. This limit doesn't apply to [stored functions](../../../programming-customizing-mariadb/stored-routines/stored-functions/README.md).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--max-sp-recursion-depth[=#]</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>0</code>`
* Range: `<code>0</code>` to `<code>255</code>`



#### `<code>max_statement_time</code>`


* Description: Maximum time in seconds that a query can execute before being aborted. This includes all queries, not just [SELECT](../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/benchmarks-and-long-running-tests/benchmark-results/select-random-ranges-and-select-random-point.md) statements, but excludes statements in stored procedures. If set to 0, no limit is applied. See [Aborting statements that take longer than a certain time to execute](../query-optimizations/aborting-statements.md) for details and limitations. Useful when combined with [SET STATEMENT](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/set-commands/set-statement.md) for limiting the execution times of individual queries. Replicas are not affected by this variable, however, from [MariaDB 10.10](../../../../../release-notes/mariadb-community-server/what-is-mariadb-1010.md), there's [slave_max_statement_time](../../standard-replication/replication-and-binary-log-system-variables.md#slave_max_statement_time) that sets the limit to abort queries on a replica.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--max-statement-time[=#]</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>0.000000</code>`
* Range: `<code>0</code>` to `<code>31536000</code>`



#### `<code>max_tmp_tables</code>`


* Description: Unused.
* Removed: [MariaDB 11.3.0](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-0-release-notes.md)



#### `<code>max_user_connections</code>`


* Description: 
Maximum simultaneous connections permitted for each user account. When set to `<code>0</code>`, there is no per user limit. Setting it to `<code>-1</code>` stops users without the [SUPER](../../../../reference/sql-statements-and-structure/sql-statements/account-management-sql-commands/grant.md#super) privilege or, from [MariaDB 10.5.2](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1052-release-notes.md), the [CONNECTION ADMIN](../../../../reference/sql-statements-and-structure/sql-statements/account-management-sql-commands/grant.md#connection-admin) privilege, from connecting to the server. The session variable is always read-only and only privileged users can modify user limits. The session variable defaults to the global `<code>max_user_connections</code>` variable, unless the user's specific `<code>[MAX_USER_CONNECTIONS](../../../../reference/sql-statements-and-structure/sql-statements/account-management-sql-commands/create-user.md#max_user_connections)</code>` resource option is non-zero. When both global variable and the user resource option are set, the user's [MAX_USER_CONNECTIONS](../../../../reference/sql-statements-and-structure/sql-statements/account-management-sql-commands/create-user.md#max_user_connections) is used. Note: This variable does not affect users with the [SUPER](../../../../reference/sql-statements-and-structure/sql-statements/account-management-sql-commands/grant.md#super) privilege or, from [MariaDB 10.5.2](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1052-release-notes.md), the [CONNECTION ADMIN](../../../../reference/sql-statements-and-structure/sql-statements/account-management-sql-commands/grant.md#connection-admin) privilege.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--max-user-connections=#</code>`
* Scope: Global, Session
* Dynamic: Yes, (except when globally set to `<code>0</code>` or `<code>-1</code>`)
* Data Type: `<code>numeric</code>`
* Default Value: `<code>0</code>`
* Range: `<code>-1</code>` to `<code>4294967295</code>`



#### `<code>max_write_lock_count</code>`


* Description: Read lock requests will be permitted for processing after this many write locks. Applies only to storage engines that use table level locks (thr_lock), so no effect with [InnoDB](../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/innodb-upgrade-tests/README.md) or [Archive](../../../../reference/storage-engines/archive/README.md).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--max-write-lock-count=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value: `<code>4294967295</code>`
* Range: `<code>1</code>` to `<code>4294967295</code>`



#### `<code>metadata_locks_cache_size</code>`


* Description: Unused since 10.1.4
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--metadata-locks-cache-size=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value: `<code>1024</code>`
* Range: `<code>1</code>` to `<code>1048576</code>`



#### `<code>metadata_locks_hash_instances</code>`


* Description: Unused since 10.1.4
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--metadata-locks-hash-instances=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value: `<code>8</code>`
* Range: `<code>1</code>` to `<code>1024</code>`



#### `<code>min_examined_row_limit</code>`


* Description: Don't write queries to [slow query log](../../../../server-management/server-monitoring-logs/slow-query-log/slow-query-log-overview.md) that examine fewer rows than the set value. If set to `<code>0</code>`, the default, no row limit is used. From [MariaDB 10.11.0](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-11-series/mariadb-10-11-0-release-notes.md), this is an alias for [log_slow_min_examined_row_limit](#log_slow_min_examined_row_limit).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--min-examined-row-limit=#</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>0</code>`
* Range: `<code>0-4294967295</code>`



#### `<code>mrr_buffer_size</code>`


* Description: Size of buffer to use when using multi-range read with range access. See [Multi Range Read optimization](../mariadb-internal-optimizations/multi-range-read-optimization.md#range-access) for more information.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--mrr-buffer-size=#</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>262144</code>`
* Range `<code>8192</code>` to `<code>2147483647</code>`



#### `<code>multi_range_count</code>`


* Description: Ignored. Use [mrr_buffer_size](#mrr_buffer_size) instead.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--multi-range-count=#</code>`
* Default Value: `<code>256</code>`
* Removed: [MariaDB 10.5.1](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1051-release-notes.md)



#### `<code>mysql56_temporal_format</code>`


* Description: If set (the default), MariaDB uses the MySQL 5.6 low level formats for [TIME](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/information-schema/time_ms-column-in-information_schemaprocesslist.md), [DATETIME](../../../../reference/data-types/date-and-time-data-types/datetime.md) and [TIMESTAMP](../../../../reference/sql-statements-and-structure/sql-statements/built-in-functions/date-time-functions/timestamp-function.md) instead of the [MariaDB 5.3](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-3-series/changes-improvements-in-mariadb-5-3.md) version. The version MySQL introduced in 5.6 requires more storage, but potentially allows negative dates and has some advantages in replication. There should be no reason to revert to the old [MariaDB 5.3](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-3-series/changes-improvements-in-mariadb-5-3.md) microsecond format. See also [MDEV-10723](https://jira.mariadb.org/browse/MDEV-10723).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--mysql56-temporal-format</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>ON</code>`



#### `<code>named_pipe</code>`


* Description: On Windows systems, determines whether connections over named pipes are permitted.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--named-pipe</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`



#### `<code>net_buffer_length</code>`


* Description: The starting size, in bytes, for the connection and thread buffers for each client thread. The size can grow to [max_allowed_packet](#max_allowed_packet). This variable's session value is read-only. Can be set to the expected length of client statements if memory is a limitation.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--net-buffer-length=#</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>16384</code>`
* Range: `<code>1024</code>` to `<code>1048576</code>`



#### `<code>net_read_timeout</code>`


* Description: Time in seconds the server will wait for a client connection to send more data before aborting the read. See also [net_write_timeout](#net_write_timeout) and [slave_net_timeout](../../standard-replication/replication-and-binary-log-system-variables.md)
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--net-read-timeout=#</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>30</code>`
* Range: `<code>1</code>` to `<code>31536000</code>`



#### `<code>net_retry_count</code>`


* Description: Permit this many retries before aborting when attempting to read or write on a communication port. On FreeBSD systems should be set higher as threads are sent internal interrupts..
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--net-retry-count=#</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>10</code>`
* Range: `<code>1</code>` to `<code>4294967295</code>`



#### `<code>net_write_timeout</code>`


* Description: Time in seconds to wait on writing a block to a connection before aborting the write. See also [net_read_timeout](#net_read_timeout) and [slave_net_timeout](../../standard-replication/replication-and-binary-log-system-variables.md).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--net-write-timeout=#</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>60</code>`
* Range: `<code>1</code>` upwards



#### `<code>note_verbosity</code>`


* Description: Verbosity level for note-warnings given to the user. Options are added in a comma-delimited string, except for `<code>all</code>`, which sets all options. See also [Notes when an index cannot be used](../../../../reference/mariadb-internals/mariadb-internals-documentation-query-optimizer/notes-when-an-index-cannot-be-used.md). Be aware that if the old [sql_notes](#sql_notes) variable is 0, one will not get any notes. Setting `<code>note_verbosity</code>` to "" is the recommended way to disable notes.

  * `<code>basic</code>` All old notes.
  * `<code>unusable_keys</code>` Give warnings for unusable keys for SELECT, DELETE and UPDATE.
  * `<code>explain</code>` Give warnings for unusable keys for EXPLAIN.
  * `<code>all</code>` Enables all above options. This has to be given alone.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">note-verbosity=value1[,value2...]</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>enumeration</code>`
* Default Value: `<code>basic,explain</code>`
* Valid Values: `<code>basic,explain,unusable_keys</code>` or `<code>all</code>`.
* Introduced: [MariaDB 10.6.16](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-10-6-16-release-notes.md)


#### `<code>old</code>`


* Description: Disabled by default, enabling it reverts index hints to those used before MySQL 5.1.17. Enabling may lead to replication errors. Deprecated and replaced by [old_mode](#old_mode) from [MariaDB 10.9](../../../../../release-notes/mariadb-community-server/what-is-mariadb-109.md).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--old</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`
* Deprecated: [MariaDB 10.9](../../../../../release-notes/mariadb-community-server/what-is-mariadb-109.md)



#### `<code>old_alter_table</code>`


* Description: From [MariaDB 10.3.7](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1037-release-notes.md), an alias for [alter_algorithm](#alter_algorithm). Prior to that, if set to `<code>1</code>` (`<code>0</code>` is default), MariaDB reverts to the non-optimized, pre-MySQL 5.1, method of processing [ALTER TABLE](../../../../reference/sql-statements-and-structure/sql-statements/data-definition/alter/alter-tablespace.md) statements. A temporary table is created, the data is copied over, and then the temporary table is renamed to the original.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--old-alter-table</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>enumerated</code>` (>=[MariaDB 10.3.7](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1037-release-notes.md))
* Default Value: See [alter_algorithm](#alter_algorithm)
* Valid Values: See [alter_algorithm](#alter_algorithm) for the full list.
* Deprecated: [MariaDB 10.3.7](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1037-release-notes.md) (superceded by [alter_algorithm](#alter_algorithm))
* Removed: [MariaDB 11.2.0](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-2-series/mariadb-11-2-0-release-notes.md)



#### `<code>old_mode</code>`


* Description: Used for getting MariaDB to emulate behavior from an old version of MySQL or MariaDB. See [OLD Mode](../../../../server-management/variables-and-modes/old-mode.md). Fully replaces the [old](#old) variable from [MariaDB 10.9](../../../../../release-notes/mariadb-community-server/what-is-mariadb-109.md). Non-default OLD_MODE options are by design deprecated and will eventually be removed.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--old-mode</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>string</code>`
* Default Value: `<code>UTF8_IS_UTF8MB3</code>` (>= [MariaDB 10.6](../../../../../release-notes/mariadb-community-server/what-is-mariadb-106.md)) `<code>(empty string)</code>` (<= [MariaDB 10.5](../../../../../release-notes/mariadb-community-server/what-is-mariadb-105.md))
* Valid Values: See [OLD Mode](../../../../server-management/variables-and-modes/old-mode.md) for the full list.



#### `<code>old_passwords</code>`


* Description: If set to `<code>1</code>` (`<code>0</code>` is default), MariaDB reverts to using the `<code>[mysql_old_password](../../../../reference/plugins/authentication-plugins/authentication-plugin-mysql_old_password.md)</code>` authentication plugin by default for newly created users and passwords, instead of the `<code>[mysql_native_password](../../../../reference/plugins/authentication-plugins/authentication-plugin-mysql_native_password.md)</code>` authentication plugin.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`



#### `<code>open_files_limit</code>`


* Description: The number of file descriptors available to MariaDB. If you are getting the `<code>Too many open files</code>` error, then you should increase this limit. If set to 0, then MariaDB will calculate a limit based on the following: 

MAX([max_connections](#max_connections)*5, [max_connections](#max_connections) +[table_open_cache](#table_open_cache)*2) 

MariaDB sets the limit with `<code>[setrlimit](https://linux.die.net/man/2/setrlimit)</code>`. MariaDB cannot set this to exceed the hard limit imposed by the operating system. Therefore, you may also need to change the hard limit. There are a few ways to do so. 

  * If you are using `<code>[mariadbd_safe](../../../../clients-and-utilities/legacy-clients-and-utilities/mariadbd_safe.md)</code>` to start `<code>mariadbd</code>`, then see the instructions at [mariadbd_safe: Configuring the Open Files Limit](../../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-safe.md#configuring-the-open-files-limit).
  * If you are using `<code>[systemd](../../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/systemd.md)</code>` to start `<code>mariadbd</code>`, then see the instructions at [systemd: Configuring the Open Files Limit](../../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/systemd.md#configuring-the-open-files-limit).
  * Otherwise, you can change the hard limit for the `<code>mysql</code>` user account by modifying `<code>[/etc/security/limits.conf](https://linux.die.net/man/5/limits.conf)</code>`. See [Configuring Linux for MariaDB: Configuring the Open Files Limit](../../../../server-management/getting-installing-and-upgrading-mariadb/mariadb-performance-advanced-configurations/configuring-linux-for-mariadb.md#configuring-the-open-files-limit) for more details.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--open-files-limit=count</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value: Autosized (see description)
* Range: `<code>0</code>` to `<code>4294967295</code>`



#### `<code>optimizer_extra_pruning_depth</code>`


* Description:If the optimizer needs to enumerate a join prefix of this size or larger, then it will try aggressively prune away the search space.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--optimizer-extra-pruning-depth[=#]</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>8</code>`
* Range: `<code>0</code>` to `<code>62</code>`
* Introduced: [MariaDB 10.10.1](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-10-series/mariadb-10101-release-notes.md)



#### optimizer_join_limit_pref_ratio


* Description:Controls the [optimizer_join_limit_pref_ratio optimization](../query-optimizations/optimizer_join_limit_pref_ratio-optimization.md).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--optimizer-join-limit-pref-ratio[=#]</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>0</code>` (Disable)
* Range: `<code>0</code>` to `<code>4294967295</code>`
* Introduced: [MariaDB 10.6.20](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-10-6-20-release-notes.md), [MariaDB 10.11.10](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-11-series/mariadb-10-11-10-release-notes.md), [MariaDB 11.2.6](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-2-series/mariadb-11-2-6-release-notes.md), [MariaDB 11.4.4](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-4-series/mariadb-11-4-4-release-notes.md), [MariaDB 11.6.2](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-6-rolling-releases/mariadb-11-6-2-release-notes.md)



#### `<code>optimizer_max_sel_arg_weight</code>`


* Description: This is an actively enforced maximum effective SEL_ARG tree weight limit. A SEL_ARG weight is the number of effective "ranges" hanging off this root (that is, merged tree elements are "unmerged" to count the weight). During range analysis, looking for possible index merges, SEL_ARG graphs related to key ranges in query conditions are being processed. Graphs exceeding this limit will stop keys being 'and'ed and 'or'ed together to form a new larger SEL_ARG graph. After each 'and' or 'or' process, this maximum weight limit is enforced. It enforces this limit by pruning the key part being used. This key part pruning can be used to limit/disable index merge SEL_ARG graph construction on overly long query conditions.
See [optimizer_max_sel_arg_weight](../../../../reference/mariadb-internals/mariadb-internals-documentation-query-optimizer/optimizer_max_sel_arg_weight.md) for details.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--optimizer-max-sel-arg-weight=#</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>32000</code>`
* Range: `<code>0</code>` to `<code>18446744073709551615</code>`
* Introduced: [MariaDB 10.5.9](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1059-release-notes.md)



#### `<code>optimizer_max_sel_args</code>`


* Description: The maximum number of SEL_ARG objects created when optimizing a range. If more objects would be needed, range scans will not be used by the optimizer.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--optimizer-max-sel-args=#</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>16000</code>`
* Range: `<code>0</code>` to `<code>4294967295</code>`
* Introduced: [MariaDB 10.6.16](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-10-6-16-release-notes.md), [MariaDB 10.10.7](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-10-series/mariadb-10-10-7-release-notes.md), [MariaDB 10.11.6](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-11-series/mariadb-10-11-6-release-notes.md), [MariaDB 11.0.4](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-0-series/mariadb-11-0-4-release-notes.md), [MariaDB 11.1.3](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-1-series/mariadb-11-1-3-release-notes.md)



#### `<code>optimizer_prune_level</code>`


* Description:Controls the heuristic(s) applied during query optimization to prune less-promising partial plans from the optimizer search space.

  * `<code>0</code>`: heuristics are disabled and an exhaustive search is performed
  * `<code>1</code>`: the optimizer will use heuristics to prune less-promising partial plans from the optimizer search space
  * `<code>2</code>`: tables using EQ_REF will be joined together as 'one entity' and the different combinations of these tables will not be considered (from [MariaDB 10.10](../../../../../release-notes/mariadb-community-server/what-is-mariadb-1010.md))
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--optimizer-prune-level[=#]</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>2</code>` (>= [MariaDB 10.10](../../../../../release-notes/mariadb-community-server/what-is-mariadb-1010.md)), `<code>1</code>` (<= [MariaDB 10.9](../../../../../release-notes/mariadb-community-server/what-is-mariadb-109.md))



#### `<code>optimizer_search_depth</code>`


* Description: Maximum search depth by the query optimizer. Smaller values lead to less time spent on execution plans, but potentially less optimal results. If set to `<code>0</code>`, MariaDB will automatically choose a reasonable value. Since the better results from more optimal planning usually offset the longer time spent on planning, this is set as high as possible by default. `<code>63</code>` is a valid value, but its effects (switching to the original find_best search) are deprecated.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--optimizer-search-depth[=#]</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>62</code>`
* Range: `<code>0</code>` to `<code>63</code>`



#### `<code>optimizer_selectivity_sampling_limit</code>`


* Description: Controls number of record samples to check condition selectivity. Only used if `<code>[optimizer_use_condition_selectivity](server-system-variables.md#optimizer_use_condition_selectivity) > 4.</code>`
* Commandline: `<code class="fixed" style="white-space:pre-wrap">optimizer-selectivity-sampling-limit[=#]</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>100</code>`
* Range: `<code>10</code>` upwards



#### `<code>optimizer_switch</code>`


* Description: A series of flags for controlling the query optimizer. See [Optimizer Switch](../query-optimizations/optimizer-switch.md) for defaults, and a comparison to MySQL.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--optimizer-switch=value</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>string</code>`
* Valid Values:

  * `<code>condition_pushdown_for_derived={on|off}</code>`
  * `<code>condition_pushdown_for_subquery={on|off}</code>`
  * `<code>condition_pushdown_from_having={on|off}</code>`
  * `<code>cset_narrowing={on|off}</code>` - see [Charset Narrowing Optimization](../query-optimizations/charset-narrowing-optimization.md) (>= [MariaDB 10.6.16](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-10-6-16-release-notes.md), [MariaDB 10.11.6](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-11-series/mariadb-10-11-6-release-notes.md), [MariaDB 11.0.4](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-0-series/mariadb-11-0-4-release-notes.md), [MariaDB 11.1.3](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-1-series/mariadb-11-1-3-release-notes.md) and [MariaDB 11.2.2](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-2-series/mariadb-11-2-2-release-notes.md))
  * `<code>default</code>` - set all optimizations to their default values.
  * `<code>derived_merge={on|off}</code>` - see [Derived table merge optimization](../query-optimizations/optimizations-for-derived-tables/derived-table-merge-optimization.md)
  * `<code>derived_with_keys={on|off}</code>` - see [Derived table with key optimization](../query-optimizations/optimizations-for-derived-tables/derived-table-with-key-optimization.md)
  * `<code>duplicateweedout={on|off}</code>`. From [MariaDB 11.8](../../../../../release-notes/mariadb-community-server/what-is-mariadb-118.md).
  * `<code>engine_condition_pushdown={on|off}</code>`. Deprecated in [MariaDB 10.1.1](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-1-release-notes.md) as engine condition pushdown is now automatically enabled for all engines that support it.
  * `<code>exists_to_in={on|off}</code>` - see [EXISTS-to-IN optimization](../query-optimizations/subquery-optimizations/exists-to-in-optimization.md)
  * `<code>extended_keys={on|off}</code>` - see [Extended Keys](../../../../reference/mariadb-internals/mariadb-internals-documentation-query-optimizer/extended-keys.md)
  * `<code>firstmatch={on|off}</code>` - see [First Match Strategy](../query-optimizations/optimization-strategies/firstmatch-strategy.md)
  * `<code>hash_join_cardinality={on|off}</code>` - see [hash_join_cardinality-optimizer_switch-flag](../query-optimizations/hash_join_cardinality-optimizer_switch-flag.md) (>= [MariaDB 11.0.2](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-0-series/mariadb-11-0-2-release-notes.md), [MariaDB 10.11.3](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-11-series/mariadb-10-11-3-release-notes.md), [MariaDB 10.6.13](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-10-6-13-release-notes.md))
  * `<code>index_condition_pushdown={on|off}</code>` - see [Index Condition Pushdown](../query-optimizations/index-condition-pushdown.md)
  * `<code>index_merge={on|off}</code>`
  * `<code>index_merge_intersection={on|off}</code>`
  * `<code>index_merge_sort_intersection={on|off}</code>` - [more details](../query-optimizations/index_merge-sort_intersection.md)
  * `<code>index_merge_sort_union={on|off}</code>`
  * `<code>index_merge_union={on|off}</code>`
  * `<code>in_to_exists={on|off}</code>` - see [IN-TO-EXISTS transformation](../query-optimizations/subquery-optimizations/non-semi-join-subquery-optimizations.md#the-in-to-exists-transformation)
  * `<code>join_cache_bka={on|off}</code>` - see [Block-Based Join Algorithms](../../../../reference/mariadb-internals/mariadb-internals-documentation-query-optimizer/block-based-join-algorithms.md)
  * `<code>join_cache_hashed={on|off}</code>` - see [Block-Based Join Algorithms](../../../../reference/mariadb-internals/mariadb-internals-documentation-query-optimizer/block-based-join-algorithms.md)
  * `<code>join_cache_incremental={on|off}</code>` - see [Block-Based Join Algorithms](../../../../reference/mariadb-internals/mariadb-internals-documentation-query-optimizer/block-based-join-algorithms.md)
  * `<code>loosescan={on|off}</code>` - see [LooseScan strategy](../query-optimizations/optimization-strategies/loosescan-strategy.md)
  * `<code>materialization={on|off}</code>` - [Semi-join](../query-optimizations/optimization-strategies/semi-join-materialization-strategy.md) and [non semi-join](../query-optimizations/subquery-optimizations/non-semi-join-subquery-optimizations.md#materialization-for-non-correlated-in-subqueries) materialization.
  * `<code>mrr={on|off}</code>` - see [Multi Range Read optimization](../mariadb-internal-optimizations/multi-range-read-optimization.md)
  * `<code>mrr_cost_based={on|off}</code>` - see [Multi Range Read optimization](../mariadb-internal-optimizations/multi-range-read-optimization.md)
  * `<code>mrr_sort_keys={on|off}</code>` - see [Multi Range Read optimization](../mariadb-internal-optimizations/multi-range-read-optimization.md)
  * `<code>not_null_range_scan={on|off}</code>` - see [not_null_range_scan optimization](../query-optimizations/not_null_range_scan-optimization.md) ( >= [MariaDB 10.5.0](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1050-release-notes.md))
  * `<code>optimize_join_buffer_size={on|off}</code>` - see [Block-Based Join Algorithms](../../../../reference/mariadb-internals/mariadb-internals-documentation-query-optimizer/block-based-join-algorithms.md)
  * `<code>orderby_uses_equalities={on|off}</code>` - if not set, the optimizer ignores equality propagation. See [MDEV-8989](https://jira.mariadb.org/browse/MDEV-8989).
  * `<code>outer_join_with_cache={on|off}</code>` - see [Block-Based Join Algorithms](../../../../reference/mariadb-internals/mariadb-internals-documentation-query-optimizer/block-based-join-algorithms.md)
  * `<code>partial_match_rowid_merge={on|off}</code>` - see [Non-semi-join subquery optimizations](../query-optimizations/subquery-optimizations/non-semi-join-subquery-optimizations.md)
  * `<code>partial_match_table_scan={on|off}</code>` - see [Non-semi-join subquery optimizations](../query-optimizations/subquery-optimizations/non-semi-join-subquery-optimizations.md)
  * `<code>rowid_filter={on|off}</code>` - see [Rowid Filtering Optimization](../query-optimizations/rowid-filtering-optimization.md)
  * `<code>sargable_casefold={on|off}</code>` (>= [MariaDB 11.3.0](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-0-release-notes.md))
  * `<code>semijoin={on|off}</code>` - see [Semi-join subquery optimizations](../query-optimizations/subquery-optimizations/semi-join-subquery-optimizations.md)
  * `<code>semijoin_with_cache={on|off}</code>` - see [Block-Based Join Algorithms](../../../../reference/mariadb-internals/mariadb-internals-documentation-query-optimizer/block-based-join-algorithms.md)
  * `<code>split_materialized={on|off}</code>`
  * `<code>subquery_cache={on|off}</code>` - see [subquery cache](../query-optimizations/subquery-optimizations/subquery-cache.md).
  * `<code>table_elimination={on|off}</code>` - see [Table Elimination User Interface](../query-optimizations/table-elimination/table-elimination-user-interface.md)



#### `<code>optimizer_trace</code>`


* Description: Controls [tracing of the optimizer](../../../../reference/mariadb-internals/mariadb-internals-documentation-query-optimizer/mariadb-internals-documentation-optimizer-trace/optimizer-trace-for-developers.md): optimizer_trace=option=val[,option=val...], where option is one of {enabled} and val is one of {on, off, default}
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--optimizer-trace=value</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>enum</code>`
* Default Value: `<code>enabled=off</code>`
* Valid Values: `<code>enabled={on|off|default}</code>`



#### `<code>optimizer_trace_max_mem_size</code>`


* Description: Limits the memory used while tracing a query by specifying the maximum allowed cumulated size, in bytes, of stored [optimizer traces](../../../../reference/mariadb-internals/mariadb-internals-documentation-query-optimizer/mariadb-internals-documentation-optimizer-trace/optimizer-trace-for-developers.md).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--optimizer-trace-max-mem-size=#</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>1048576</code>`
* Range: `<code>1</code>` to `<code>18446744073709551615</code>`



#### `<code>optimizer_use_condition_selectivity</code>`


* Description: Controls which statistics can be used by the optimizer when looking for
the best query execution plan. In most cases, the default value, `<code>4</code>` will be suitable. However, if you are hitting some of the rare cases where this does not work well (see [MDEV-23707](https://jira.mariadb.org/browse/MDEV-23707)), you can usually work around this by setting this variable to `<code>1</code>`.

  * `<code>1</code>` Use selectivity of predicates as in [MariaDB 5.5](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5.md).
  * `<code>2</code>` Use selectivity of all range predicates supported by indexes.
  * `<code>3</code>` Use selectivity of all range predicates estimated without [histogram](../query-optimizations/statistics-for-optimizing-queries/histogram-based-statistics.md).
  * `<code>4</code>` Use selectivity of all range predicates estimated with [histogram](../query-optimizations/statistics-for-optimizing-queries/histogram-based-statistics.md).
  * `<code>5</code>` Additionally use selectivity of certain non-range predicates calculated on record sample.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--optimizer-use-condition-selectivity=#</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>4</code>`
* Range: `<code>1</code>` to `<code>5</code>`



#### `<code>pid_file</code>`


* Description: Full path of the process ID file. If [--log-basename](../../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md#-log-basename) is also set, `<code>pid_file</code>` should be placed after in the config files. Later settings override earlier settings, so `<code>log-basename</code>` will override any earlier log file name settings.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--pid-file=file_name</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>file name</code>`



#### `<code>plugin_dir</code>`


* Description: Path to the [plugin](../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/general-development-information/development-plans/old-plans/plugins-storage-engines-summit-for-mysqlmariadbdrizzle-2011.md) directory. For security reasons, either make sure this directory can only be read by the server, or set [secure_file_priv](#secure_file_priv).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--plugin-dir=path</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>directory name</code>`
* Default Value: `<code>BASEDIR/lib/plugin</code>`



#### `<code>plugin_maturity</code>`


* Description: The lowest acceptable [plugin](../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/general-development-information/development-plans/old-plans/plugins-storage-engines-summit-for-mysqlmariadbdrizzle-2011.md) maturity. MariaDB will not load plugins less mature than the specified level.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--plugin-maturity=level</code>`
* Scope: Global
* Dynamic: No
* Type: enum
* Default Value: One less than the server maturity
* Valid Values: `<code class="fixed" style="white-space:pre-wrap">unknown</code>`, `<code class="fixed" style="white-space:pre-wrap">experimental</code>`, `<code class="fixed" style="white-space:pre-wrap">alpha</code>`, `<code class="fixed" style="white-space:pre-wrap">beta</code>`, `<code class="fixed" style="white-space:pre-wrap">gamma</code>`, `<code class="fixed" style="white-space:pre-wrap">stable</code>`



#### `<code>port</code>`


* Description: Port to listen for TCP/IP connections. If set to `<code>0</code>`, will default to, in order of preference, my.cnf, the MYSQL_TCP_PORT [environment variable](../../../../server-management/getting-installing-and-upgrading-mariadb/mariadb-environment-variables.md), /etc/services, built-in default (3306).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--port=#</code>`, `<code class="fixed" style="white-space:pre-wrap">-P</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value: `<code>3306</code>`
* Range: `<code>0</code>` to `<code>65535</code>`



#### `<code>preload_buffer_size</code>`


* Description: Size in bytes of the buffer allocated when indexes are preloaded.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--preload-buffer-size=#</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>32768</code>`
* Range: `<code>1024</code>` to `<code>1073741824</code>`



#### `<code>profiling</code>`


* Description: If set to `<code>1</code>` (`<code>0</code>` is default), statement profiling will be enabled. See [SHOW PROFILES()](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-profiles.md) and [SHOW PROFILE()](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-profile.md).
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`



#### `<code>profiling_history_size</code>`


* Description: Number of statements about which profiling information is maintained. If set to `<code>0</code>`, no profiles are stored. See [SHOW PROFILES](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-profiles.md).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--profiling-history-size=

# </code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>15</code>`
* Range: `<code>0</code>` to `<code>100</code>`



#### `<code>progress_report_time</code>`


* Description: Time in seconds between sending [progress reports](../../../../reference/mariadb-internals/using-mariadb-with-your-programs-api/progress-reporting.md) to the client for time-consuming statements. If set to `<code>0</code>`, progress reporting will be disabled.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--progress-report-time=#</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>5</code>`
* Range: `<code>0</code>` to `<code>4294967295</code>`



#### `<code>protocol_version</code>`


* Description: The version of the client/server protocol used by the MariaDB server.
* Commandline: None
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value: `<code>10</code>`
* Range: `<code>0</code>` to `<code>4294967295</code>`



#### `<code>proxy_protocol_networks</code>`


* Description: Enable [proxy protocol](../../../../clients-and-utilities/server-client-software/client-libraries/proxy-protocol-support.md) for these source networks. The syntax is a comma separated list of IPv4 and IPv6 networks. If the network doesn't contain a mask, it is considered to be a single host. "*" represents all networks and must be the only directive on the line. String "localhost" represents non-TCP local connections (Unix domain socket, Windows named pipe or shared memory). See [Proxy Protocol Support](../../../../clients-and-utilities/server-client-software/client-libraries/proxy-protocol-support.md).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--proxy-protocol-networks=value</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>string</code>`
* Default Value: (empty)



#### `<code>proxy_user</code>`


* Description: Set to the proxy user account name if the current client is a proxy, else `<code>NULL</code>`.
* Scope: Session
* Dynamic: No
* Data Type: `<code>string</code>`



#### `<code>pseudo_slave_mode</code>`


* Description: For internal use by the server.
* Scope: Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>OFF</code>`



#### `<code>pseudo_thread_id</code>`


* Description: For internal use only.
* Scope: Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`



#### `<code>query_alloc_block_size</code>`


* Description: Size in bytes of the extra blocks allocated during query parsing and execution (after [query_prealloc_size](#query_prealloc_size) is used up).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--query-alloc-block-size=#</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>16384</code>`
* Range - 32 bit: `<code>1024</code>` to `<code>4294967295</code>`
* Range - 64 bit: `<code>1024</code>` to `<code>18446744073709547520</code>`



#### `<code>query_cache_limit</code>`


* Description: Size in bytes for which results larger than this are not stored in the [query cache](../../../../reference/plugins/other-plugins/query-cache-information-plugin.md).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--query-cache-limit=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>1048576</code>` (1MB)
* Range: `<code>0</code>` to `<code>4294967295</code>`



#### `<code>query_cache_min_res_unit</code>`


* Description: Minimum size in bytes of the blocks allocated for [query cache](../../../../reference/plugins/other-plugins/query-cache-information-plugin.md) results.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--query-cache-min-res-unit=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>4096</code>` (4KB)
* Range - 32 bit: `<code>1024</code>` to `<code>4294967295</code>`
* Range - 64 bit: `<code>1024</code>` to `<code>18446744073709547520</code>`



#### `<code>query_cache_size</code>`


* Description: Size in bytes available to the [query cache](../../../../reference/plugins/other-plugins/query-cache-information-plugin.md). About 40KB is needed for query cache structures, so setting a size lower than this will result in a warning. `<code>0</code>`, the default before [MariaDB 10.1.7](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-7-release-notes.md), effectively disables the query cache.


**Warning:** Starting from [MariaDB 10.1.7](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-7-release-notes.md), [query_cache_type](#query_cache_type) is automatically set to ON if the server is started with the query_cache_size set to a non-zero (and non-default) value. This will happen even if [query_cache_type](#query_cache_type) is explicitly set to OFF in the configuration.


* Commandline: `<code class="fixed" style="white-space:pre-wrap">--query-cache-size=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>1M</code>` (although frequently given a default value in some setups)
* Valid Values: `<code>0</code>` upwards in units of 1024.



#### `<code>query_cache_strip_comments</code>`


* Description: If set to `<code>1</code>` (`<code>0</code>` is default), the server will strip any comments from the query before searching to see if it exists in the [query cache](../../../../reference/plugins/other-plugins/query-cache-information-plugin.md). Multiple space, line feeds, tab and other white space characters will also be removed.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">query-cache-strip-comments</code>`
* Scope: Session, Global
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`



#### `<code>query_cache_type</code>`


* Description: If set to `<code>0</code>`, the [query cache](../../../../reference/plugins/other-plugins/query-cache-information-plugin.md) is disabled (although a buffer of [query_cache_size](#query_cache_size) bytes is still allocated). If set to `<code>1</code>` all SELECT queries will be cached unless SQL_NO_CACHE is specified. If set to `<code>2</code>` (or `<code>DEMAND</code>`), only queries with the SQL CACHE clause will be cached. Note that if the server is started with the query cache disabled, it cannot be enabled at runtime.


**Warning:** Starting from [MariaDB 10.1.7](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-7-release-notes.md), query_cache_type is automatically set to ON if the server is started with the [query_cache_size](#query_cache_size) set to a non-zero (and non-default) value. This will happen even if [query_cache_type](#query_cache_type) is explicitly set to OFF in the configuration.


* Commandline: `<code class="fixed" style="white-space:pre-wrap">--query-cache-type=#</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>enumeration</code>`
* Default Value: `<code>OFF</code>`
* Valid Values: `<code>0</code>` or `<code>OFF</code>`, `<code>1</code>` or `<code>ON</code>`, `<code>2</code>` or `<code>DEMAND</code>`



#### `<code>query_cache_wlock_invalidate</code>`


* Description: If set to `<code>0</code>`, the default, results present in the [query cache](../../../../reference/plugins/other-plugins/query-cache-information-plugin.md) will be returned even if there's a write lock on the table. If set to `<code>1</code>`, the client will first have to wait for the lock to be released.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--query-cache-wlock-invalidate</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`



#### `<code>query_prealloc_size</code>`


* Description: Size in bytes of the persistent buffer for query parsing and execution, allocated on connect and freed on disconnect. Increasing may be useful if complex queries are being run, as this will reduce the need for more memory allocations during query operation. See also [query_alloc_block_size](#query_alloc_block_size).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--query-prealloc-size=#</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>24576</code>`
* Range: `<code>1024</code>` to `<code>4294967295</code>`



#### `<code>rand_seed1</code>`


* Description: `<code>rand_seed1</code>` and `<code>rand_seed2</code>` facilitate replication of the [RAND()](../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/random-query-generator-tests.md) function. The master passes the value of these to the slaves so that the random number generator is seeded in the same way, and generates the same value, on the slave as on the master. Until [MariaDB 10.1.4](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-4-release-notes.md), the variable value could not be viewed, with the [SHOW VARIABLES](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-variables.md) output always displaying zero.
* Commandline: None
* Scope: Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: Varies
* Range: `<code>0</code>` to `<code>18446744073709551615</code>`



#### `<code>rand_seed2</code>`


* Description: See [rand_seed1](#rand_seed1).



#### `<code>range_alloc_block_size</code>`


* Description: Size in bytes of blocks allocated during range optimization. The unit size in 1024.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--range-alloc-block-size=#</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>4096</code>`
* Range - 32 bit: `<code>4096</code>` to `<code>4294967295</code>`
* Range - 64 bit: `<code>4096</code>` to `<code>18446744073709547520</code>`



#### `<code>read_buffer_size</code>`


* Description: Each thread performing a sequential scan (for MyISAM, Aria and MERGE tables) allocates a buffer of this size in bytes for each table scanned. Increase if you perform many sequential scans. If not in a multiple of 4KB, will be rounded down to the nearest multiple. Also used in ORDER BY's for caching indexes in a temporary file (not temporary table), for caching results of nested queries, for bulk inserts into partitions, and to determine the memory block size of [MEMORY](../../../../reference/storage-engines/memory-storage-engine.md) tables.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--read-buffer-size=#</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>131072</code>`
* Range: `<code>8192</code>` to `<code>2147479552</code>`



#### `<code>read_only</code>`


* Description: When set to `<code>1</code>` (`<code>0</code>` is default), no updates are permitted except from users with the [SUPER](../../../../reference/sql-statements-and-structure/sql-statements/account-management-sql-commands/grant.md#super) privilege or, from [MariaDB 10.5.2](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1052-release-notes.md), the [READ ONLY ADMIN](../../../../reference/sql-statements-and-structure/sql-statements/account-management-sql-commands/grant.md#read_only-admin) privilege, or replica servers updating from a primary. The `<code>read_only</code>` variable is useful for replica servers to ensure no updates are accidentally made outside of what are performed on the primary. Inserting rows to log tables, updates to temporary tables and [OPTIMIZE TABLE](../optimizing-tables/optimize-table.md) or [ANALYZE TABLE](../../../../reference/sql-statements-and-structure/sql-statements/table-statements/analyze-table.md) statements are excluded from this limitation. If `<code>read_only</code>` is set to `<code>1</code>`, then the [SET PASSWORD](../../../../reference/sql-statements-and-structure/sql-statements/account-management-sql-commands/set-password.md) statement is limited only to users with the [SUPER](../../../../reference/sql-statements-and-structure/sql-statements/account-management-sql-commands/grant.md#super) privilege (<= [MariaDB 10.5.1](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1051-release-notes.md)) or [READ ONLY ADMIN](../../../../reference/sql-statements-and-structure/sql-statements/account-management-sql-commands/grant.md#read_only-admin) privilege (>= [MariaDB 10.5.2](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1052-release-notes.md)). Attempting to set this variable to `<code>1</code>` will fail if the current session has table locks or transactions pending, while if other sessions hold table locks, the statement will wait until these locks are released before completing. While the attempt to set `<code>read_only</code>` is waiting, other requests for table locks or transactions will also wait until `<code>read_only</code>` has been set. See [Read-Only Replicas](../../standard-replication/read-only-replicas.md) for more. From [MariaDB 10.5.2](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1052-release-notes.md), the [READ_ONLY ADMIN](../../../../reference/sql-statements-and-structure/sql-statements/account-management-sql-commands/grant.md#read_only-admin) privilege will allow users granted that privilege to perform writes, even if the `<code>read_only</code>` variable is set. In earlier versions, and until [MariaDB 10.11.0](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-11-series/mariadb-10-11-0-release-notes.md), users with the [SUPER](../../../../reference/sql-statements-and-structure/sql-statements/account-management-sql-commands/grant.md#super) can perform writes while this variable is set.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--read-only</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`



#### `<code>read_rnd_buffer_size</code>`


* Description: Size in bytes of the buffer used when reading rows from a [MyISAM](../../../../reference/storage-engines/myisam-storage-engine/myisam-system-variables.md) table in sorted order after a key sort. Larger values improve ORDER BY performance, although rather increase the size by SESSION where the need arises to avoid excessive memory use.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--read-rnd-buffer-size=#</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>262144</code>`
* Range: `<code>8200</code>` to `<code>2147483647</code>`



#### `<code>redirect_url</code>`


* Description: URL of another server to redirect clients to. Format should be `<code class="fixed" style="white-space:pre-wrap">{mysql,mariadb}://host[:port]</code>`. Empty string means no redirection. For example `<code class="fixed" style="white-space:pre-wrap">set global redirect_url="mysql://mariadb.org:12345"</code>`. See [Connection Redirection Mechanism in the MariaDB Client/Server Protocol](../../connection-redirection-mechanism-in-the-mariadb-clientserver-protocol.md).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--redirect_url=val</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>string</code>`
* Default Value: Empty
* Introduced: [MariaDB 11.3.0](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-0-release-notes.md)



-


-


#### `<code>require_secure_transport</code>`


* Description: When this option is enabled, connections attempted using insecure transport will be rejected. Secure transports are SSL/TLS, Unix sockets or named pipes. Note that [per-account requirements](../../../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/securing-connections-for-client-and-server.md#requiring-tls) take precedence.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--require-secure-transport[={0|1}]</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`
* Introduced: [MariaDB 10.5.2](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1052-release-notes.md)



#### `<code>rowid_merge_buff_size</code>`


* Description: The maximum size in bytes of the memory available to the Rowid-merge strategy. See [Non-semi-join subquery optimizations](../query-optimizations/subquery-optimizations/non-semi-join-subquery-optimizations.md#optimizer-control) for more information.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--rowid-merge-buff-size=#</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>8388608</code>`
* Range: `<code>0</code>` to `<code>2147483647</code>`



#### `<code>rpl_recovery_rank</code>`


* Description: Unused.
* Removed: [MariaDB 10.1.2](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-2-release-notes.md)



#### `<code>safe_show_database</code>`


* Description: This variable was removed in [MariaDB 5.5](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5.md), and has been replaced by the more flexible [SHOW DATABASES](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-databases.md) privilege.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--safe-show-database</code>` (until MySQL 4.1.1)
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Removed: [MariaDB 5.5](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5.md)



#### `<code>secure_auth</code>`


* Description: Connections will be blocked if they use the the `<code>[mysql_old_password](../../../../reference/plugins/authentication-plugins/authentication-plugin-mysql_old_password.md)</code>` authentication plugin. The server will also fail to start if the privilege tables are in the old, pre-MySQL 4.1 format. `<code>secure_auth=0</code>` was deprecated in [MariaDB 10.6.17](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-10-6-17-release-notes.md), [MariaDB 10.11.7](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-11-series/mariadb-10-11-7-release-notes.md), [MariaDB 11.0.5](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-0-series/mariadb-11-0-5-release-notes.md), [MariaDB 11.1.4](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-1-series/mariadb-11-1-4-release-notes.md), [MariaDB 11.2.3](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-2-series/mariadb-11-2-3-release-notes.md).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--secure-auth</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>ON</code>`



#### `<code>secure_file_priv</code>`


* Description: [LOAD DATA](../../../../reference/sql-statements-and-structure/sql-statements/data-manipulation/inserting-loading-data/load-data-into-tables-or-index/load-data-infile.md), [SELECT ... INTO](../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/benchmarks-and-long-running-tests/benchmark-results/select-random-ranges-and-select-random-point.md#into) and [LOAD FILE()](../../../../reference/sql-statements-and-structure/sql-statements/built-in-functions/string-functions/load_file.md) will only work with files in the specified path. If not set, the default, or set to empty string, the statements will work with any files that can be accessed.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--secure-file-priv=path</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>path name</code>`
* Default Value: None



#### `<code>secure_timestamp</code>`


* Description: Restricts direct setting of a session timestamp. Possible levels are: 

  * YES - timestamp cannot deviate from the system clock. Intended to prevent tampering with [system versioning](../../../../reference/sql-statements-and-structure/temporal-tables/system-versioned-tables.md) history. Should not be used on replicas, as when a value based on the timestamp is inserted in [statement mode](../../../../server-management/server-monitoring-logs/binary-log/binary-log-formats.md#statement-based-logging), discrepancies can occur.
  * REPLICATION - replication thread can adjust timestamp to match the primary's
  * SUPER - a user with this privilege and a replication thread can adjust timestamp
  * NO - historical behavior, anyone can modify session timestamp
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--secure-timestamp=value</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>enum</code>`
* Default Value: `<code>NO</code>`



#### `<code>server_uid</code>`


* Description: Automatically calculated server unique id hash. Added to the [error log](../../../../server-management/server-monitoring-logs/error-log.md) to allow one to verify if error reports are from the same server. UID is a base64-encoded SHA1 hash of the MAC address of one of the interfaces, and the tcp port that the server is listening on.
* Commandline: None
* Scope: Global
* Dynamic: No
* Data Type: `<code>varchar</code>`
* Default Value: None
* Introduced: [MariaDB 10.5.26](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-10-5-26-release-notes.md), [MariaDB 10.6.19](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-10-6-19-release-notes.md), [MariaDB 10.11.9](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-11-series/mariadb-10-11-9-release-notes.md), [MariaDB 11.1.6](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-1-series/mariadb-11-1-6-release-notes.md), [MariaDB 11.2.5](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-2-series/mariadb-11-2-5-release-notes.md), [MariaDB 11.4.3](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-4-series/mariadb-11-4-3-release-notes.md), [MariaDB 11.5.2](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-5-rolling-releases/mariadb-11-5-2-release-notes.md), [MariaDB 11.6.1](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-6-rolling-releases/mariadb-11-6-1-release-notes.md)



#### `<code>session_track_schema</code>`


* Description: Whether to track changes to the default schema within the current session.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--session-track-schema={0|1}</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>ON</code>`



#### `<code>session_track_state_change</code>`


* Description: Whether to track changes to the session state.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--session-track-state-change={0|1}</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`



#### `<code>session_track_system_variables</code>`


* Description: Comma-separated list of session system variables for which to track changes. For compatibility with MySQL defaults, this variable should be set to "autocommit, character_set_client, character_set_connection, character_set_results, time_zone". The `<code>*</code>` character tracks all session variables.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--session-track-system-variables=value</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>string</code>`
* Default Value:

  * >= [MariaDB 11.3](../../../../../release-notes/mariadb-community-server/what-is-mariadb-113.md): `<code>autocommit,character_set_client,character_set_connection,character_set_results,redirect_url,time_zone</code>`
  * <= [MariaDB 11.2](../../../../../release-notes/mariadb-community-server/what-is-mariadb-112.md): `<code>autocommit, character_set_client, character_set_connection, character_set_results, time_zone</code>`



#### `<code>session_track_transaction_info</code>`


* Description: Track changes to the transaction attributes. OFF to disable; STATE to track just transaction state (Is there an active transaction? Does it have any data? etc.); CHARACTERISTICS to track transaction state and report all statements needed to start a transaction with the same characteristics (isolation level, read only/read write,snapshot - but not any work done / data modified within the transaction).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--session-track-transaction-info=value</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>enum</code>`
* Default Value: `<code>OFF</code>`
* Valid Values: `<code>OFF</code>`, `<code>STATE</code>`, `<code>CHARACTERISTICS</code>`



#### `<code>shared_memory</code>`


* Description: Windows only, determines whether the server permits shared memory connections. See also [shared_memory_base_name](#shared_memory_base_name).
* Scope: Global
* Dynamic: No



#### `<code>shared_memory_base_name</code>`


* Description: Windows only, specifies the name of the shared memory to use for shared memory connection. Mainly used when running more than one instance on the same physical machine. By default the name is `<code>MYSQL</code>` and is case sensitive. See also [shared_memory](#shared_memory).
* Scope: Global
* Dynamic: No
* Data Type: `<code>string</code>`
* Default Value: `<code>MYSQL</code>`



#### `<code>skip_external_locking</code>`


* Description: If this system variable is set, then some kinds of external table locks will be disabled for some [storage engines](../../../../../general-resources/learning-and-training/video-presentations-and-screencasts/storage-engines-and-plugins-videos.md).

  * If this system variable is set, then the [MyISAM](../../../../reference/storage-engines/myisam-storage-engine/README.md) storage engine will not use file-based locks. Otherwise, it will use the `<code>[fcntl()](https://linux.die.net/man/2/fcntl)</code>` function with the `<code>F_SETLK</code>` option to get file-based locks on Unix, and it will use the `<code>[LockFileEx()](https://docs.microsoft.com/en-us/windows/desktop/api/fileapi/nf-fileapi-lockfileex)</code>` function to get file-based locks on Windows.
  * If this system variable is set, then the [Aria](../../../../reference/storage-engines/s3-storage-engine/aria_s3_copy.md) storage engine will not lock a table when it decrements the table's in-file counter that keeps track of how many connections currently have the table open. See [MDEV-19393](https://jira.mariadb.org/browse/MDEV-19393) for more information.
  * Note that command line option name is the opposite of the variable name, and the value is the opposite too. `<code>--external-locking=1</code>` means `<code>@@skip_external_locking=0</code>`, and vice versa.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--external-locking</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>boolean</code>`
* Default Value: `<code>1</code>` (for the variable, that is `<code>0</code>` for the command line option)



#### `<code>skip_grant_tables</code>`


* Description: Start without grant tables. This gives all users FULL ACCESS to all tables. Before [MariaDB 10.10](../../../../../release-notes/mariadb-community-server/what-is-mariadb-1010.md), available as an [option only](../../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md). Use [mariadb-admin flush-privileges](../../../../clients-and-utilities/legacy-clients-and-utilities/mysqladmin.md), [mariadb-admin reload](../../../../clients-and-utilities/legacy-clients-and-utilities/mysqladmin.md) or [FLUSH PRIVILEGES](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/flush-commands/flush-tables-for-export.md) to resume using the grant tables.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--skip-grant-tables</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`
* Introduced: [MariaDB 10.10](../../../../../release-notes/mariadb-community-server/what-is-mariadb-1010.md)



#### `<code>skip_name_resolve</code>`


* Description: If set to 1 (0 is the default), only IP addresses are used for connections. Host names are not resolved. All host values in the GRANT tables must be IP addresses (or localhost).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--skip-name-resolve</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>boolean</code>`
* Default Value: `<code>0</code>`



#### `<code>skip_networking</code>`


* Description: If set to 1, (0 is the default), the server does not listen for TCP/IP connections. All interaction with the server will be through socket files (Unix) or named pipes or shared memory (Windows). It's recommended to use this option if only local clients are permitted to connect to the server.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--skip-networking</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>boolean</code>`
* Default Value: `<code>0</code>`



#### `<code>skip_show_database</code>`


* Description: If set to 1, (0 is the default), only users with the [SHOW DATABASES](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-databases.md) privilege can use the SHOW DATABASES statement to see all database names.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--skip-show-database</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>boolean</code>`
* Default Value: `<code>0</code>`



#### `<code>slow_launch_time</code>`


* Description: Time in seconds. If a thread takes longer than this to launch, the `<code>slow_launch_threads</code>` [server status variable](server-status-variables.md) is incremented.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--slow-launch-time=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>2</code>`



#### `<code>slow_query_log</code>`


* Description: If set to 0, the default unless the --slow-query-log option is used, the [slow query log](../../../../server-management/server-monitoring-logs/slow-query-log/slow-query-log-overview.md) is disabled, while if set to 1 (both global and session variables), the slow query log is enabled. From [MariaDB 10.11.0](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-11-series/mariadb-10-11-0-release-notes.md), an alias for [log_slow_query](#log_slow_query).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--slow-query-log</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Data Type: `<code>boolean</code>`
* Default Value: `<code>0</code>`
* See also: See [log_output](#log_output) to see how log files are written. If that variable is set to `<code>NONE</code>`, no logs will be written even if slow_query_log is set to `<code>1</code>`.



#### `<code>slow_query_log_file</code>`


* Description: Name of the [slow query log](../../../../server-management/server-monitoring-logs/slow-query-log/slow-query-log-overview.md) file. From [MariaDB 10.11](../../../../../release-notes/mariadb-community-server/what-is-mariadb-1011.md), an alias for [log_slow_query_file](#log_slow_query_file). If [--log-basename](../../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md#-log-basename) is also set, `<code>slow_query_log_file</code>` should be placed after in the config files. Later settings override earlier settings, so `<code>log-basename</code>` will override any earlier log file name settings.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--slow-query-log-file=file_name</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>file name</code>`
* Default Value: `<code><em>host_name</em>-slow.log</code>`



#### `<code>socket</code>`


* Description: On Unix-like systems, this is the name of the socket file used for local client connections, by default `<code>/tmp/mysql.sock</code>`, often changed by the distribution, for example `<code>/var/lib/mysql/mysql.sock</code>`. On Windows, this is the name of the named pipe used for local client connections, by default `<code>MySQL</code>`. On Windows, this is not case-sensitive.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--socket=name</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>file name</code>`
* Default Value: `<code>/tmp/mysql.sock</code>` (Unix), `<code>MySQL</code>` (Windows)



#### `<code>sort_buffer_size</code>`


* Description: Each session performing a sort allocates a buffer with this amount of memory. Not specific to any storage engine. If the status variable [sort_merge_passes](server-status-variables.md#sort_merge_passes) is too high, you may need to look at improving your query indexes, or increasing this. Consider reducing where there are many small sorts, such as OLTP, and increasing where needed by session. 16k is a suggested minimum.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--sort-buffer-size=#</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>number</code>`
* Default Value: `<code>2M (2097152)</code>` (some distributions increase the default)



#### `<code>sql_auto_is_null</code>`


* Description: If set to 1, the query `<code class="fixed" style="white-space:pre-wrap">SELECT * FROM table_name WHERE auto_increment_column IS NULL</code>` will return an auto-increment that has just been successfully inserted, the same as the LAST_INSERT_ID() function. Some ODBC programs make use of this IS NULL comparison.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>0</code>`



#### `<code>sql_big_selects</code>`


* Description: If set to 0, MariaDB will not perform large SELECTs. See [max_join_size](#max_join_size) for details. If max_join_size is set to anything but DEFAULT, sql_big_selects is automatically set to 0. If sql_big_selects is again set, max_join_size will be ignored.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>1</code>`



#### `<code>sql_big_tables</code>`


* Description: Old variable, which if set to 1, allows large result sets by saving all temporary sets to disk, avoiding 'table full' errors. No longer needed, as the server now handles this automatically.

  * This is a synonym for `<code>[big_tables](#big_tables)</code>`.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--sql-big-tables</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>0</code>`
* Removed: [MariaDB 10.0](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md)



#### `<code>sql_buffer_result</code>`


* Description: If set to 1 (0 is default), results from SELECT statements are always placed into temporary tables. This can help the server when it takes a long time to send the results to the client by allowing the table locks to be freed early.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>0</code>`



#### `<code>sql_if_exists</code>`


* Description: If set to 1, adds an implicit IF EXISTS to ALTER, RENAME and DROP of TABLES, VIEWS, FUNCTIONS and PACKAGES. This variable is mainly used in replication to tag DDLs that can be ignored on the slave if the target table doesn't exist.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--sql-if-exists[={0|1}]</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`
* Introduced: [MariaDB 10.5.2](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1052-release-notes.md)



#### `<code>sql_log_off</code>`


* Description: If set to 1 (0 is the default), no logging to the [general query log](../../../../server-management/server-monitoring-logs/general-query-log.md) is done for the client. Only clients with the [SUPER](../../../../reference/sql-statements-and-structure/sql-statements/account-management-sql-commands/grant.md#super) privilege can update this variable.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>0</code>`



#### `<code>sql_log_update</code>`


* Description: Removed. Use [sql_log_bin](#sql_log_bin) instead.
* Removed: MariaDB/MySQL 5.5



#### `<code>sql_low_priority_updates</code>`


* Description: If set to 1 (0 is the default), for [storage engines](../../../../../general-resources/learning-and-training/video-presentations-and-screencasts/storage-engines-and-plugins-videos.md) that use only table-level locking ([Aria](../../../../reference/storage-engines/s3-storage-engine/aria_s3_copy.md), [MyISAM](../../../../reference/storage-engines/myisam-storage-engine/myisam-system-variables.md), [MEMORY](../../../../reference/storage-engines/memory-storage-engine.md) and [MERGE](../../../../reference/storage-engines/merge.md)), all INSERTs, UPDATEs, DELETEs and LOCK TABLE WRITEs will wait until there are no more SELECTs or LOCK TABLE READs pending on the relevant tables. Set this to 1 if reads are prioritized over writes.

  * This is a synonym for `<code>[low_priority_updates](#low_priority_updates)</code>`.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--sql-low-priority-updates</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>0</code>`
* Removed: [MariaDB 10.0](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md)



#### `<code>sql_max_join_size</code>`


* Description: Synonym for [max_join_size](#max_join_size), the preferred name.
* Deprecated: [MariaDB 5.5](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5.md)
* Removed: [MariaDB 10.0](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md)



#### `<code>sql_mode</code>`


* Description: Sets the [SQL Mode](../../../../server-management/variables-and-modes/sql-mode.md). Multiple modes can be set, separated by a comma.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--sql-mode=value[,value[,value...]]</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>string</code>`
* Default Value:

  * `<code>STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION</code>`
* Valid Values: See [SQL Mode](../../../../server-management/variables-and-modes/sql-mode.md) for the full list.



#### `<code>sql_notes</code>`


* Description: If set to 1, the default, [warning_count](#warning_count) is incremented each time a Note warning is encountered. If set to 0, Note warnings are not recorded. [mariadb-dump](../../../../clients-and-utilities/backup-restore-and-import-clients/mariadb-dump.md) has outputs to set this variable to 0 so that no unnecessary increments occur when data is reloaded. See also [note_verbosity](#note_verbosity), which defines which notes should be given. The recommended way, as of [MariaDB 10.6.16](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-10-6-16-release-notes.md), to disable notes is to set `<code>note_verbosity</code>` to "".
* Commandline: None
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>1</code>`



#### `<code>sql_quote_show_create</code>`


* Description: If set to 1, the default, the server will quote identifiers for [SHOW CREATE DATABASE](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-create-database.md), [SHOW CREATE TABLE](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-create-table.md) and [SHOW CREATE VIEW](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-create-view.md) statements. Quoting is disabled if set to 0. Enable to ensure replication works when identifiers require quoting.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>1</code>`



#### `<code>sql_safe_updates</code>`


* Description: If set to 1, UPDATEs and DELETEs must be executed by using an index (simply mentioning an indexed column in a WHERE clause is not enough, optimizer must actually use it) or they must mention an indexed column and specify a LIMIT clause. Otherwise a statement will be aborted. Prevents the common mistake of accidentally deleting or updating every row in a table. Until [MariaDB 10.3.11](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-10311-release-notes.md), could not be set as a command-line option or in my.cnf.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--sql-safe-updates[={0|1}]</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`



#### `<code>sql_select_limit</code>`


* Description: Maximum number of rows that can be returned from a SELECT query. Default is the maximum number of rows permitted per table by the server, usually 232-1 or 264-1. Can be restored to the default value after being changed by assigning it a value of DEFAULT. If a SELECT has a LIMIT clause, the LIMIT takes precedence over the value of the variable.
* Commandline: None
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>18446744073709551615</code>`



#### `<code>sql_warnings</code>`


* Description: If set to 1, single-row INSERTs will produce a string containing warning information if a warning occurs.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF (0)</code>`



#### `<code>storage_engine</code>`


* Description: See [default_storage_engine](#default_storage_engine).
* Deprecated: [MariaDB 5.5](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5.md)



#### `<code>standard_compliant_cte</code>`


* Description: Allow only standard-compliant [common table expressions](../../../../reference/sql-statements-and-structure/sql-statements/data-manipulation/selecting-data/common-table-expressions/README.md). Prior to [MariaDB 10.2.4](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1024-release-notes.md), this variable was named `<code>standards_compliant_cte</code>`.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--standard-compliant-cte={0|1}</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>ON</code>`



#### `<code>stored_program_cache</code>`


* Description: Limit to the number of [stored routines](../../../programming-customizing-mariadb/stored-routines/README.md) held in the stored procedures and stored functions caches. Each time a stored routine is executed, this limit is first checked, and if the number held in the cache exceeds this, that cache is flushed and memory freed.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--stored-program-cache=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>256</code>`
* Range: `<code>256</code>` to `<code>524288</code>`



#### `<code>strict_password_validation</code>`


* Description: When [password validation](../../../../reference/plugins/password-validation-plugins/README.md) plugins are enabled, reject passwords that cannot be validated (passwords specified as a hash). This excludes direct updates to the privilege tables.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--strict-password-validation</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>ON</code>`



#### `<code>sync_frm</code>`


* Description: If set to 1, the default, each time a non-temporary table is created, its .frm definition file is synced to disk. Fractionally slower, but safer in case of a crash.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--sync-frm</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>TRUE</code>`



#### `<code>system_time_zone</code>`


* Description: The system time zone is determined when the server starts. The system [time zone](../../../../reference/data-types/string-data-types/character-sets/internationalization-and-localization/time-zones.md) is usually read from the operating system's environment but can be overridden by setting the 'TZ' environment variable before starting the server. See [Time Zones: System Time Zone](../../../../reference/data-types/string-data-types/character-sets/internationalization-and-localization/time-zones.md#system-time-zone) for the various ways to change the system time zone. This variable is not the same as the [time_zone](#time_zone) system variable, which is the variable that actually controls a session's active time zone. The system time zone is used for a session when `<code>time_zone</code>` is set to the special value `<code>SYSTEM</code>`.
* Scope: Global
* Dynamic: No
* Data Type: `<code>string</code>`



#### `<code>table_definition_cache</code>`


* Description: Number of table definitions that can be cached. Table definitions are taken from the .frm files, and if there are a large number of tables increasing the cache size can speed up table opening. Unlike the [table_open_cache](#table_open_cache), as the table_definition_cache doesn't use file descriptors, and is much smaller.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--table-definition-cache=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>400</code>`
* Range: `<code>400</code>` to `<code>2097152</code>`



#### `<code>table_lock_wait_timeout</code>`


* Description: Unused, and removed.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--table-lock-wait-timeout=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>50</code>`
* Range: `<code>1</code>` to `<code>1073741824</code>`
* Removed: [MariaDB 5.5](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5.md)



#### `<code>table_open_cache</code>`


* Description: Maximum number of open tables cached in one table cache instance. See [Optimizing table_open_cache](optimizing-table_open_cache.md) for suggestions on optimizing. Increasing table_open_cache increases the number of file descriptors required.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--table-open-cache=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>2000</code>`
* Range:

  * `<code>1</code>` to `<code>1048576</code>` (1024K)



#### `<code>table_open_cache_instances</code>`


* Description: This system variable specifies the maximum number of table cache instances. MariaDB Server initially creates just a single instance. However, whenever it detects contention on the existing instances, it will automatically create a new instance. When the number of instances has been increased due to contention, it does not decrease again. The default value of this system variable is `<code>8</code>`, which is expected to handle up to 100 CPU cores. If your system is larger than this, then you may benefit from increasing the value of this system variable.

  * Depending on the ratio of actual available file handles, and `<code>[table_open_cache](server-system-variables.md#table_open_cache)</code>` size, the max. instance count may be auto adjusted to a lower value on server startup.
  * The implementation and behavior of this feature is different than the same feature in MySQL 5.6.
  * See [Optimizing table_open_cache: Automatic Creation of New Table Open Cache Instances](optimizing-table_open_cache.md#automatic-creation-of-new-table-open-cache-instances) for more information.
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value: `<code>8</code>` (>= [MariaDB 10.2.2](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1022-release-notes.md))
* Range: `<code>1</code>` to `<code>64</code>`



#### `<code>table_type</code>`


* Description: Removed and replaced by [storage_engine](#storage_engine). Use [default_storage_engine](#default_storage_engine) instead.



#### `<code>tcp_keepalive_interval</code>`


* Description: The interval, in seconds, between when successive keep-alive packets are sent if no acknowledgement is received. If set to 0, the system dependent default is used.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--tcp-keepalive-interval=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>0</code>`
* Range: `<code>0</code>` to `<code>2147483</code>`



#### `<code>tcp_keepalive_probes</code>`


* Description: The number of unacknowledged probes to send before considering the connection dead and notifying the application layer. If set to 0, a system dependent default is used.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--tcp-keepalive-probes=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>0</code>`
* Range: `<code>0</code>` to `<code>2147483</code>`



#### `<code>tcp_keepalive_time</code>`


* Description: Timeout, in seconds, with no activity until the first TCP keep-alive packet is sent. If set to 0, a system dependent default is used.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--tcp-keepalive-time=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>0</code>`
* Range: `<code>0</code>` to `<code>2147483</code>`



#### `<code>tcp_nodelay</code>`


* Description: Set the TCP_NODELAY option (disable Nagle's algorithm) on socket.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--tcp-nodelay={0|1}</code>`
* Scope: Session
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>1</code>`



#### `<code>thread_cache_size</code>`


* Description: Number of threads server caches for re-use. If this limit hasn't been reached, when a client disconnects, its threads are put into the cache, and re-used where possible. In [MariaDB 10.2.0](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1020-release-notes.md) and newer the threads are freed after 5 minutes of idle time. Normally this setting has little effect, as the other aspects of the thread implementation are more important, but increasing it can help servers with high volumes of connections per second so that most can use a cached, rather than a new, thread. The cache miss rate can be calculated as the [server status variables](server-status-variables.md) threads_created/connections. If the [thread pool](../buffers-caches-and-threads/thread-pool/thread-pool-in-mariadb-51-53.md) is active, `<code>thread_cache_size</code>` is ignored. If `<code>thread_cache_size</code>` is set to greater than the value of [max_connections](#max_connections), `<code>thread_cache_size</code>` will be set to the [max_connections](#max_connections) value.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--thread-cache-size=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>256</code>` (adjusted if thread pool is active)
* Range: `<code>0</code>` to `<code>16384</code>`



#### `<code>thread_concurrency</code>`


* Description: Allows applications to give the system a hint about the desired number of threads. Specific to Solaris only, invokes thr_setconcurrency(). Deprecated and has no effect from [MariaDB 5.5](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5.md).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--thread-concurrency=

# </code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value: `<code>10</code>`
* Range: `<code>1</code>` to `<code>512</code>`
* Deprecated: [MariaDB 5.5](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5.md)
* Removed: [MariaDB 10.5.1](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1051-release-notes.md)



#### `<code>thread_stack</code>`


* Description: Stack size for each thread. If set too small, limits recursion depth of stored procedures and complexity of SQL statements the server can handle in memory. Also affects limits in the crash-me test.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--thread-stack=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value:

  * `<code>299008</code>`
* Range: `<code>131072</code>` to `<code>18446744073709551615</code>`



#### `<code>time_format</code>`


* Description: Unused.
* Removed: [MariaDB 11.3.0](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-0-release-notes.md)



#### `<code>time_zone</code>`


* Description: The global value determines the default [time zone](../../../../reference/data-types/string-data-types/character-sets/internationalization-and-localization/time-zones.md) for sessions that connect. The session value determines the session's active [time zone](../../../../reference/data-types/string-data-types/character-sets/internationalization-and-localization/time-zones.md). When it is set to `<code>SYSTEM</code>`, the session's time zone is determined by the `<code>[system_time_zone](#system_time_zone)</code>` system variable.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--default-time-zone=string</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>string</code>`
* Default Value: `<code>SYSTEM</code>`



#### `<code>timed_mutexes</code>`


* Description: Determines whether [InnoDB](../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/innodb-upgrade-tests/README.md) mutexes are timed. `<code>OFF</code>`, the default, disables mutex timing, while `<code>ON</code>` enables it. See also [SHOW ENGINE](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-engine-innodb-status.md) for more on mutex statistics. Deprecated and has no effect.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--timed-mutexes</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`
* Deprecated: [MariaDB 5.5.39](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/mariadb-5539-release-notes.md)
* Removed: [MariaDB 10.5.1](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1051-release-notes.md)



#### `<code>timestamp</code>`


* Description: Sets the time for the client. This will affect the result returned by the [NOW()](../../../../reference/sql-statements-and-structure/sql-statements/built-in-functions/date-time-functions/now.md) function, not the [SYSDATE()](../../../../reference/sql-statements-and-structure/sql-statements/built-in-functions/date-time-functions/sysdate.md) function, unless the server is started with the [--sysdate-is-now](../../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md) option, in which case SYSDATE becomes an alias of NOW, and will also be affected. Also used to get the original timestamp when restoring rows from the [binary log](../../../../reference/storage-engines/innodb/binary-log-group-commit-and-innodb-flushing-performance.md).
* Scope: Session
* Dynamic: Yes
* Valid Values: `<code>timestamp_value</code>` (Unix epoch timestamp, not MariaDB timestamp), `<code>DEFAULT</code>`



#### `<code>tmp_disk_table_size</code>`


* Description: Max size for data for an internal temporary on-disk [MyISAM](../../../../reference/storage-engines/myisam-storage-engine/myisam-system-variables.md) or [Aria](../../../../reference/storage-engines/s3-storage-engine/aria_s3_copy.md) table. These tables are created as part of complex queries when the result doesn't fit into the memory engine. You can set this variable if you want to limit the size of temporary tables created in your temporary directory [tmpdir](#tmpdir).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--tmp-disk-table-size=#</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>18446744073709551615</code>` (max unsigned integer, no limit)
* Range: `<code>1024</code>` to `<code>18446744073709551615</code>`



#### `<code>tmp_memory_table_size</code>`


* Description: An alias for [tmp_table_size](#tmp_table_size).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--tmp-memory-table-size=#</code>`



#### `<code>tmp_table_size</code>`


* Description: The largest size for temporary tables in memory (not [MEMORY](../../../../reference/storage-engines/memory-storage-engine.md) tables) although if [max_heap_table_size](#max_heap_table_size) is smaller the lower limit will apply. You can see if it's necessary to increase by comparing the [status variables](server-status-variables.md) `<code>Created_tmp_disk_tables</code>` and `<code>Created_tmp_tables</code>` to see how many temporary tables out of the total created needed to be converted to disk. Often complex GROUP BY queries are responsible for exceeding the limit. Defaults may be different on some systems, see for example [Differences in MariaDB in Debian](../../../../server-management/getting-installing-and-upgrading-mariadb/troubleshooting-installation-issues/installation-issues-on-debian-and-ubuntu/differences-in-mariadb-in-debian-and-ubuntu.md). From [MariaDB 10.2.7](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1027-release-notes.md), [tmp_memory_table_size](#tmp_memory_table_size) is an alias.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--tmp-table-size=#</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>16777216</code>` (16MB)
* Range:

  * `<code>1024</code>` to `<code>4294967295</code>` (< [MariaDB 10.5](../../../../../release-notes/mariadb-community-server/what-is-mariadb-105.md))
  * `<code>0</code>` to `<code>4294967295</code>` (>= [MariaDB 10.5.0](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1050-release-notes.md))



#### `<code>tmpdir</code>`


* Description: Directory for storing temporary tables and files. Can specify a list (separated by semicolons in Windows, and colons in Unix) that will then be used in round-robin fashion. This can be used for load balancing across several disks. Note that if the server is a [replication](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/README.md) replica, and [slave_load_tmpdir](../../standard-replication/replication-and-binary-log-system-variables.md#slave_load_tmpdir), which overrides `<code>tmpdir</code>` for replicas, is not set, you should not set `<code>tmpdir</code>` to a directory that is cleared when the machine restarts, or else replication may fail.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--tmpdir=path</code>` or `<code class="fixed" style="white-space:pre-wrap">-t path</code>`
* Scope: Global
* Dynamic: No
* Type: directory name/s
* Default:

  * `<code>$TMPDIR</code>` (environment variable) if set
  * otherwise `<code>$TEMP</code>` if set and on Windows
  * otherwise `<code>$TMP</code>` if set and on Windows
  * otherwise `<code>P_tmpdir</code>` (`<code>"/tmp"</code>`) or `<code>C:\TEMP</code>` (unless overridden during buid time)



#### `<code>transaction_alloc_block_size</code>`


* Description: Size in bytes to increase the memory pool available to each transaction when the available pool is not large enough. See [transaction_prealloc_size](#transaction_prealloc_size).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--transaction-alloc-block-size=#</code>`
* Scope: Global, Session
* Dynamic: Yes
* Type: numeric
* Default Value: `<code>8192</code>`
* Range: `<code>1024</code>` to `<code>134217728</code>` (128M)
* Block Size: `<code>1024</code>`



#### `<code>transaction_isolation</code>`


* Description: The transaction isolation level. See also [SET TRANSACTION ISOLATION LEVEL](../../../../reference/sql-statements-and-structure/sql-statements/transactions/set-transaction.md). Introduced in [MariaDB 11.1.1](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-1-series/mariadb-11-1-1-release-notes.md) to replace the [tx_isolation](#tx_isolation) system variable and align the option and the system variable name.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--transaction-isolation=name</code>`
* Scope: Global, Session
* Dynamic: Yes
* Type: enumeration
* Default Value: `<code>REPEATABLE-READ</code>`
* Valid Values: `<code>READ-UNCOMMITTED</code>`, `<code>READ-COMMITTED</code>`, `<code>REPEATABLE-READ</code>`, `<code>SERIALIZABLE</code>`
* Introduced: [MariaDB 11.1.1](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-1-series/mariadb-11-1-1-release-notes.md)



#### `<code>transaction_prealloc_size</code>`


* Description: Initial size of a memory pool available to each transaction for various memory allocations. If the memory pool is not large enough for an allocation, it is increased by [transaction_alloc_block_size](#transaction_alloc_block_size) bytes, and truncated back to transaction_prealloc_size bytes when the transaction is completed. If set large enough to contain all statements in a transaction, extra malloc() calls are avoided.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--transaction-prealloc-size=#</code>`
* Scope: Global, Session
* Dynamic: Yes
* Type: numeric
* Default Value: `<code>4096</code>`
* Range: `<code>1024</code>` to `<code>134217728</code>` (128M)
* Block Size: `<code>1024</code>`



#### `<code>transaction_read_only</code>`


* Description: Default transaction access mode. If set to `<code>OFF</code>`, the default, access is read/write. If set to `<code>ON</code>`, access is read-only. The `<code>SET TRANSACTION</code>` statement can also change the value of this variable. See [SET TRANSACTION](../../../../reference/sql-statements-and-structure/sql-statements/transactions/set-transaction.md) and [START TRANSACTION](../../../../reference/sql-statements-and-structure/sql-statements/transactions/start-transaction.md).
* Commandline: None
* Scope: Global, Session
* Dynamic: Yes
* Type: boolean
* Default Value: `<code>OFF</code>`
* Introduced: [MariaDB 11.1](../../../../../release-notes/mariadb-community-server/what-is-mariadb-111.md)



#### `<code>tx_isolation</code>`


* Description: The transaction isolation level. Setting this session variable via `<code>set @@tx_isolation=</code>` will take effect for only the subsequent transaction in the current session, much like [SET TRANSACTION ISOLATION LEVEL](../../../../reference/sql-statements-and-structure/sql-statements/transactions/set-transaction.md). To set for a session, use `<code>SET SESSION tx_isolation</code>` or `<code>SET @@session.tx_isolation</code>`. See [MDEV-31751](https://jira.mariadb.org/browse/MDEV-31751). See also [SET TRANSACTION ISOLATION LEVEL](../../../../reference/sql-statements-and-structure/sql-statements/transactions/set-transaction.md). In [MariaDB 11.1](../../../../../release-notes/mariadb-community-server/what-is-mariadb-111.md), this system variable is deprecated and replaced by [transaction_isolation](#transaction_isolation).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--transaction-isolation=name</code>`
* Scope: Global, Session
* Dynamic: Yes
* Type: enumeration
* Default Value: `<code>REPEATABLE-READ</code>`
* Valid Values: `<code>READ-UNCOMMITTED</code>`, `<code>READ-COMMITTED</code>`, `<code>REPEATABLE-READ</code>`, `<code>SERIALIZABLE</code>`
* Deprecated: [MariaDB 11.1](../../../../../release-notes/mariadb-community-server/what-is-mariadb-111.md)



#### `<code>tx_read_only</code>`


* Description: Default transaction access mode. If set to `<code>OFF</code>`, the default, access is read/write. If set to `<code>ON</code>`, access is read-only. The `<code>SET TRANSACTION</code>` statement can also change the value of this variable. See [SET TRANSACTION](../../../../reference/sql-statements-and-structure/sql-statements/transactions/set-transaction.md) and [START TRANSACTION](../../../../reference/sql-statements-and-structure/sql-statements/transactions/start-transaction.md). In [MariaDB 11.1](../../../../../release-notes/mariadb-community-server/what-is-mariadb-111.md), this system variable is deprecated and replaced by [transaction_read_only](#transaction_read_only).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--transaction-read-only=#</code>`
* Scope: Global, Session
* Dynamic: Yes
* Type: boolean
* Default Value: `<code>OFF</code>`
* Deprecated: [MariaDB 11.1](../../../../../release-notes/mariadb-community-server/what-is-mariadb-111.md)



#### `<code>unique_checks</code>`


* Description: If set to 0, storage engines can (but are not required to) assume that duplicate keys are not present in input data. If set to 0, inserting duplicates into a `<code>UNIQUE</code>` index can succeed, causing the table to become corrupted. Set to 0 to speed up imports of large tables to InnoDB.
* Scope: Global, Session
* Dynamic: Yes
* Type: boolean
* Default Value: `<code>1</code>`



#### `<code>updatable_views_with_limit</code>`


* Description: Determines whether view updates can be made with an UPDATE or DELETE statement with a LIMIT clause if the view does not contain all primary or not null unique key columns from the underlying table. `<code>0</code>` prohibits this, while `<code>1</code>` permits it while issuing a warning (the default).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--updatable-views-with-limit=#</code>`
* Scope: Global, Session
* Dynamic: Yes
* Type: boolean
* Default Value: `<code>1</code>`



#### `<code>use_stat_tables</code>`


* Description: Controls the use of [engine-independent table statistics](../query-optimizations/statistics-for-optimizing-queries/engine-independent-table-statistics.md). 

  * `<code>never</code>`: The optimizer will not use data from statistics tables.
  * `<code>complementary</code>`: The optimizer uses data from statistics tables if the same kind of data is not provided by the storage engine.
  * `<code>preferably</code>`: Prefer the data from statistics tables, if it's not available there, use the data from the storage engine.
  * `<code>complementary_for_queries</code>`: Same as `<code>complementary</code>`, but for queries only (to avoid needlessly collecting for [ANALYZE TABLE](../../../../reference/sql-statements-and-structure/sql-statements/table-statements/analyze-table.md)).
  * `<code>preferably_for_queries</code>`: Same as `<code>preferably</code>`, but for queries only (to avoid needlessly collecting for [ANALYZE TABLE](../../../../reference/sql-statements-and-structure/sql-statements/table-statements/analyze-table.md)).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--use-stat-tables=mode</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>enum</code>`
* Default Value: `<code>preferably_for_queries</code>`



#### `<code>version</code>`


* Description: Server version number. It may also include a suffix with configuration or build information. `<code>-debug</code>` indicates debugging support was enabled on the server, and `<code>-log</code>` indicates at least one of the binary log, general log or [slow query log](../../../../server-management/server-monitoring-logs/slow-query-log/slow-query-log-overview.md) are enabled, for example `<code>10.0.1-MariaDB-mariadb1precise-log</code>`. Can be set at startup in order to fake the server version.
* Commandline: `<code class="fixed" style="white-space:pre-wrap"> -V</code>`, `<code class="fixed" style="white-space:pre-wrap">--version[=name]</code>`
* Scope: Global
* Dynamic: No
* Type: string



#### `<code>version_comment</code>`


* Description: Value of the COMPILATION_COMMENT option specified by CMake when building MariaDB, for example `<code>mariadb.org binary distribution</code>`.
* Scope: Global
* Dynamic: No
* Type: string



#### `<code>version_compile_machine</code>`


* Description: The machine type or architecture MariaDB was built on, for example `<code>i686</code>`.
* Scope: Global
* Dynamic: No
* Type: string



#### `<code>version_compile_os</code>`


* Description: Operating system that MariaDB was built on, for example `<code>debian-linux-gnu</code>`.
* Scope: Global
* Dynamic: No
* Type: string



#### `<code>version_malloc_library</code>`


* Description: Version of the used malloc library.
* Commandline: None
* Scope: Global
* Dynamic: No
* Type: string



#### `<code>version_source_revision</code>`


* Description: Source control revision id for MariaDB source code, enabling one to see exactly which version of the source was used for a build.
* Commandline: None
* Scope: Global
* Dynamic: No
* Type: string



#### `<code>wait_timeout</code>`


* Description: Time in seconds that the server waits for a connection to become active before closing it. The session value is initialized when a thread starts up from either the global value, if the connection is non-interactive, or from the [interactive_timeout](#interactive_timeout) value, if the connection is interactive.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--wait-timeout=#</code>`
* Scope: Global, Session
* Dynamic: Yes
* Type: numeric
* Default Value: `<code>28800</code>`
* Range: (Windows): `<code>1</code>` to `<code>2147483</code>`
* Range: (Other): `<code>1</code>` to `<code>31536000</code>`



#### `<code>warning_count</code>`


* Description: Read-only variable indicating the number of warnings, errors and notes resulting from the most recent statement that generated messages. See [SHOW WARNINGS](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-warnings.md) for more. Note warnings will only be recorded if [sql_notes](#sql_notes) is true (the default).
* Scope: Session
* Dynamic: No
* Type: numeric


