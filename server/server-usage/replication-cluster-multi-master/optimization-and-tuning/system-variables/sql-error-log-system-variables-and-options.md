
# SQL Error Log System Variables and Options

This page documents system variables and options related to the [SQL_Error_Log Plugin](../../../../server-management/server-monitoring-logs/sql-error-log-plugin.md). See [Server System Variables](server-system-variables.md) for a complete list of system variables and instructions on setting them.


See also the [Full list of MariaDB options, system and status variables](../../../../server-management/variables-and-modes/full-list-of-mariadb-options-system-and-status-variables.md).


## Options


#### `<code>sql_error_log</code>`


* Description: Controls how the server should treat the plugin when the server starts up.

  * Valid values are:

    * `<code>OFF</code>` - Disables the plugin without removing it from the [mysql.plugins](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/the-mysql-database-tables/mysql-plugin-table.md) table.
    * `<code>ON</code>` - Enables the plugin. If the plugin cannot be initialized, then the server will still continue starting up, but the plugin will be disabled.
    * `<code>FORCE</code>` - Enables the plugin. If the plugin cannot be initialized, then the server will fail to start with an error.
    * `<code>FORCE_PLUS_PERMANENT</code>` - Enables the plugin. If the plugin cannot be initialized, then the server will fail to start with an error. In addition, the plugin cannot be uninstalled with [UNINSTALL SONAME](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-soname.md) or [UNINSTALL PLUGIN](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-plugin.md) while the server is running.
  * See [Plugin Overview: Configuring Plugin Activation at Server Startup](../../../../reference/plugins/plugin-overview.md#configuring-plugin-activation-at-server-startup) for more information.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--sql-error-log=value</code>`
* Data Type: `<code>enumerated</code>`
* Default Value: `<code>ON</code>`
* Valid Values: `<code>OFF</code>`, `<code>ON</code>`, `<code>FORCE</code>`, `<code>FORCE_PLUS_PERMANENT</code>`



## System Variables


#### `<code>sql_error_log_filename</code>`


* Description: The name (and optionally path) of the logfile containing the errors. Rotation will use a naming convention such as `<code>sql_error_log_filename.001</code>`. If no path is specified, the log file will be written to the [data directory](server-system-variables.md#datadir).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--sql-error-log-filename=value</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>string</code>`
* Default Value: `<code>sql_errors.log</code>`



#### `<code>sql_error_log_rate</code>`


* Description: The logging sampling rate. Setting to `<code>10</code>`, for example, means that one in ten errors will be logged. If set to zero, logging is disabled. The default, `<code>1</code>`, logs every error.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--sql-error-log-rate=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>1</code>`



#### `<code>sql_error_log_rotate</code>`


* Description: Setting to #1`<code> forces log rotation.</code>`
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--sql-error-log-rate[={0|1}]</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`



#### `<code>sql_error_log_rotations</code>`


* Description: Number of rotations before the log is removed. When rotated, the current log file is stored and a new, empty, log is created. Any rotations older than this setting are removed.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--sql-error-log-rotations=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>9</code>`
* Range: `<code>1</code>` to `<code>999</code>`



#### `<code>sql_error_log_size_limit</code>`


* Description: The log file size limit in bytes. After reaching this size, the log file is rotated.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--sql-error-log-size-limit=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>numeric</code>`
* Default Value: `<code>1000000</code>`
* Range: `<code>100</code>` to `<code>9223372036854775807</code>`



#### `<code>sql_error_log_warnings</code>`


* Description: If set, log warnings in addition to errors.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--sql-error-log-warnings={0,1}</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`
* Introduced: [MariaDB 10.11.5](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-11-series/mariadb-10-11-5-release-notes.md)



#### `<code>sql_error_log_with_db_and_thread_info</code>`


* Description: If enabled, it prints the database name and the thread ID in the log in addition to already existing columns.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--sql-error-log-with-db-and-thread-info=value</code>`
* Scope: Global
* Dynamic: No
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`
* Introduced: [MariaDB 10.6.17](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-10-6-17-release-notes.md), [MariaDB 10.11.7](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-11-series/mariadb-10-11-7-release-notes.md), [MariaDB 11.0.5](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-0-series/mariadb-11-0-5-release-notes.md), [MariaDB 11.1.4](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-1-series/mariadb-11-1-4-release-notes.md), [MariaDB 11.2.3](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-2-series/mariadb-11-2-3-release-notes.md)


