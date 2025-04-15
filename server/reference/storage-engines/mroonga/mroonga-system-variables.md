
# Mroonga System Variables

This page documents system variables related to the [Mroonga storage engine](mroonga-user-defined-functions/mroonga_snippet_html.md). See [Server System Variables](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md) for a complete list of system variables and instructions on setting them.


See also the [Full list of MariaDB options, system and status variables](../../../server-management/variables-and-modes/full-list-of-mariadb-options-system-and-status-variables.md).


#### `<code>mroonga_action_on_fulltext_query_error</code>`


* Description: Action to take when encountering a Mroonga fulltext error.

  * `<code>ERROR</code>`: Report an error without logging.
  * `<code>ERROR_AND_LOG</code>`: Report an error with logging (the default)
  * `<code>IGNORE</code>`: No logging or reporting - the error is ignored.
  * `<code>IGNORE_AND_LOG</code>`: Log the error without reporting it.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--mroonga-action-on-fulltext-query-error=value</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>enum</code>`
* Default Value: `<code>ERROR_AND_LOG</code>`



#### `<code>mroonga_boolean_mode_syntax_flags</code>`


* Description: Flags to customize syntax in BOOLEAN MODE searches. Available flags: 

  * `<code>DEFAULT</code>`: (=SYNTAX_QUERY,ALLOW_LEADING_NOT)
  * `<code>ALLOW_COLUMN</code>`: Allows `<code>COLUMN:...</code>` syntax in query syntax, an incompatible change to the regular BOOLEAN MODE syntax. Permits multiple indexes in one `<code>MATCH () AGAINST ()</code>`. Can be used in other operations besides full-text search, such as equal, and prefix search. See [Groonga query syntax](https://groonga.org/docs/reference/grn_expr/query_syntax.html) for more details.
  * `<code>ALLOW_LEADING_NOT</code>` Permits using the `<code>NOT_INCLUDED_KEYWORD</code>` syntax in the query syntax.
  * `<code>ALLOW_UPDATE</code>`: Permits updating values with the `<code>COLUMN:=NEW_VALUE</code>` syntax in the query syntax.
  * `<code>SYNTAX_QUERY</code>`: Mroonga will use Groonga's query syntax, compatible with MariaDB's BOOLEAN MODE syntax. Unless `<code>SYNTAX_SCRIPT</code>` is specified, this mode is always in use.
  * `<code>SYNTAX_SCRIPT</code>`: Mroonga will use Groonga's script syntax, a JavaScript-like syntax. If both `<code>SYNTAX_QUERY</code>` and `<code>SYNTAX_SCRIPT</code>` are specified, `<code>SYNTAX_SCRIPT</code>` will take precedence..
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--mroonga-boolean-mode-syntax-flags=value</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>enum</code>`
* Default Value: `<code>DEFAULT</code>`



#### `<code>mroonga_database_path_prefix</code>`


* Description: The database path prefix.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--mroonga-database-path-prefix=value</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>string</code>`
* Default Value: (Empty)



#### `<code>mroonga_default_parser</code>`


* Description: The fulltext default parser, for example `<code>TokenBigramSplitSymbolAlphaDigit</code>` or `<code>TokenBigram</code>` (the default). See the list of options at [Mroonga Overview:Parser](mroonga-overview.md#parser). Deprecated since Mroonga 5.04, use [mroonga_default_tokenizer](#mroonga_default_tokenizer) instead.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--mroonga-default-parser=value</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>string</code>`
* Default Value: `<code>TokenBigram</code>`
* Deprecated: [MariaDB 10.1.6](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-6-release-notes.md), Mroonga 5.0.4



#### `<code>mroonga_default_tokenizer</code>`


* Description: The fulltext default parser, for example `<code>TokenBigramSplitSymbolAlphaDigit</code>` or `<code>TokenBigram</code>` (the default). See the list of options at [Mroonga Overview:Parser](mroonga-overview.md#parser).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--mroonga-default-tokenizer=value</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>string</code>`
* Default Value: `<code>TokenBigram</code>`
* Introduced: [MariaDB 10.1.6](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-6-release-notes.md), Mroonga 5.0.4



#### `<code>mroonga_default_wrapper_engine</code>`


* Description: The default engine for wrapper mode.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--mroonga-default-wrapper-engine=value</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>string</code>`
* Default Value: (Empty)



#### `<code>mroonga_dry_write</code>`


* Description: If set to `<code>on</code>`, (`<code>off</code>` is default), data is not actually written to the Groonga database. Only really useful to change for benchmarking.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--mroonga-dry-write[={0|1}]</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>off</code>`



#### `<code>mroonga_enable_operations_recording</code>`


* Description: Whether recording operations for recovery to the Groonga database is enabled (default) or not. Requires reopening the database with [FLUSH TABLES](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/flush-commands/flush-tables-for-export.md) after changing the variable.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--mroonga-enable-operations-recording={0|1}</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>ON</code>`
* Introduced: [MariaDB 10.2.11](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-10211-release-notes.md), [MariaDB 10.1.29](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10129-release-notes.md)



#### `<code>mroonga_enable_optimization</code>`


* Description: If set to `<code>on</code>` (the default), optimization is enabled. Only really useful to change for benchmarking.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--mroonga-enable-optimization={0|1}</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>on</code>`



#### `<code>mroonga_libgroonga_embedded</code>`


* Description: Whether libgroonga is embedded or not.
* Commandline: None
* Scope: Global
* Dynamic: No
* Data Type: `<code>boolean</code>`
* Default Value: `<code>ON</code>`
* Introduced: [MariaDB 10.1.6](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-6-release-notes.md)



#### `<code>mroonga_libgroonga_support_lz4</code>`


* Description: Whether libgroonga supports lz4 or not.
* Commandline: None
* Scope: Global
* Dynamic: No
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`



#### `<code>mroonga_libgroonga_support_zlib</code>`


* Description: Whether libgroonga supports zlib or not.
* Commandline: None
* Scope: Global
* Dynamic: No
* Data Type: `<code>boolean</code>`
* Default Value: `<code>ON</code>`



#### `<code>mroonga_libgroonga_support_zstd</code>`


* Description: Whether libgroonga supports Zstandard or not.
* Commandline: None
* Scope: Global
* Dynamic: No
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`
* Introduced: [MariaDB 10.2.11](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-10211-release-notes.md), [MariaDB 10.1.29](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10129-release-notes.md)



#### `<code>mroonga_libgroonga_version</code>`


* Description: Groonga library version.
* Commandline: None
* Scope: Global
* Dynamic: No
* Data Type: `<code>string</code>`



#### `<code>mroonga_lock_timeout</code>`


* Description: Lock timeout used in Groonga.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--mroonga-lock-timeout=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>900000</code>`
* Range: `<code>-1</code>` to `<code>2147483647</code>`



#### `<code>mroonga_log_file</code>`


* Description: Name and path of the Mroonga log file.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--mroonga-log-file=value</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>string</code>`
* Default Value: `<code>groonga.log</code>`



#### `<code>mroonga_log_level</code>`


* Description: Mroonga log file output level, which determines what is logged. Valid levels include:

  * `<code>NONE</code>` 	No output.
  * `<code>EMERG</code>`: Only emergency error messages, such as database corruption.
  * `<code>ALERT</code>`: Alert messages, such as internal errors.
  * `<code>CRIT </code>`: Critical error messages, such as deadlocks.
  * `<code>ERROR </code>`: Errors, such as API errors.
  * `<code>WARNING</code>`: Warnings, such as invalid arguments.
  * `<code>NOTICE</code>`: Notices, such as a change in configuration or a status change.
  * `<code>INFO</code>`: Information messages, such as file system operations.
  * `<code>DEBUG</code>`: Debug messages, suggested for developers or testers.
  * `<code>DUMP</code>`: Dump messages.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--mroonga-log-level=value</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>enum</code>`
* Default Value: `<code>NOTICE</code>`



#### `<code>mroonga_match_escalation_threshold</code>`


* Description: The threshold to determine whether the match method is escalated. `<code>-1</code>` means never escalate.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--mroonga-match-escalation-threshold=#</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>0</code>`
* Range: `<code>-1</code>` to `<code>9223372036854775807</code>`



#### `<code>mroonga_max_n_records_for_estimate</code>`


* Description: The max number of records to estimate the number of matched records
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--mroonga-max-n-records-for-estimate=#</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>1000</code>`
* Range: `<code>-1</code>` to `<code>2147483647</code>`



#### `<code>mroonga_query_log_file</code>`


* Description: Query log file for Mroonga.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--mroonga-query-log-file=filename</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>string</code>`
* Default Value: (Empty string)
* Introduced: [MariaDB 10.2.11](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-10211-release-notes.md)



#### `<code>mroonga_vector_column_delimiter</code>`


* Description: Delimiter to use when outputting a vector column. The default is a white space.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--mroonga-vector-column-delimiter=value</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>string</code>`
* Default Value: `<code> </code>` (white space)



#### `<code>mroonga_version</code>`


* Description: Mroonga version
* Commandline: None
* Scope: Global
* Dynamic: No
* Data Type: `<code>string</code>`


