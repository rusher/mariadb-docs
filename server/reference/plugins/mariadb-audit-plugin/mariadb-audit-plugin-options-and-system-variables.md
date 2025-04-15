
# MariaDB Audit Plugin Options and System Variables


There are a several options and system variables related to the [MariaDB Audit Plugin](release-notes-mariadb-audit-plugin/mariadb-audit-plugin-113-release-notes.md), once it has been [installed](mariadb-audit-plugin-installation.md). System variables can be displayed using the [SHOW VARIABLES](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-variables.md) statement like so:


```
SHOW GLOBAL VARIABLES LIKE '%server_audit%';

+-------------------------------+-----------------------+
| Variable_name                 | Value                 |
+-------------------------------+-----------------------+
| server_audit_events           | CONNECT,QUERY,TABLE   |
| server_audit_excl_users       |                       |
| server_audit_file_path        | server_audit.log      |
| server_audit_file_rotate_now  | OFF                   |
| server_audit_file_rotate_size | 1000000               |
| server_audit_file_rotations   | 9                     |
| server_audit_incl_users       |                       |
| server_audit_logging          | ON                    |
| server_audit_mode             | 0                     |
| server_audit_output_type      | file                  |
| server_audit_query_log_limit  | 1024                  |
| server_audit_syslog_facility  | LOG_USER              |
| server_audit_syslog_ident     | mysql-server_auditing |
| server_audit_syslog_info      |                       |
| server_audit_syslog_priority  | LOG_INFO              |
+-------------------------------+-----------------------+
```

To change the value of one of these variables, you can use the `<code>SET</code>` statement, or set them at the command-line when starting MariaDB. It's recommended that you set them in the MariaDB configuration for the server like so:


```
[mariadb]
...
server_audit_excl_users='bob,ted'
...
```

### System Variables


Below is a list of all system variables related to the Audit Plugin. See [Server System Variables](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md) for a complete list of system variables and instructions on setting them. See also the [full list of MariaDB options, system and status variables](../../../server-management/variables-and-modes/full-list-of-mariadb-options-system-and-status-variables.md).


#### `<code>server_audit_events</code>`


* Description: If set, then this restricts audit logging to certain event types. If not set, then every event type is logged to the audit log. For example: SET GLOBAL server_audit_events='connect, query'
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--server-audit-events=value</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>string</code>`
* Default Value: Empty string
* Valid Values:

  * `<code>CONNECT</code>`, `<code>QUERY</code>`, `<code>TABLE</code>` (MariaDB Audit Plugin < 1.2.0)
  * `<code>CONNECT</code>`, `<code>QUERY</code>`, `<code>TABLE</code>`, `<code>QUERY_DDL</code>`, `<code>QUERY_DML</code>` (MariaDB Audit Plugin >= 1.2.0)
  * `<code>CONNECT</code>`, `<code>QUERY</code>`, `<code>TABLE</code>`, `<code>QUERY_DDL</code>`, `<code>QUERY_DML</code>`, `<code>QUERY_DCL</code>` (MariaDB Audit Plugin >=1.3.0)
  * `<code>CONNECT</code>`, `<code>QUERY</code>`, `<code>TABLE</code>`, `<code>QUERY_DDL</code>`, `<code>QUERY_DML</code>`, `<code>QUERY_DCL</code>`, `<code>QUERY_DML_NO_SELECT</code>` (MariaDB Audit Plugin >= 1.4.4)
  * See [MariaDB Audit Plugin - Versions](mariadb-audit-plugin-versions.md) to determine which MariaDB releases contain each MariaDB Audit Plugin versions.



#### `<code>server_audit_excl_users</code>`


* Description: If not empty, it contains the list of users whose activity will NOT be logged.	For example: `<code>SET GLOBAL server_audit_excl_users='user_foo, user_bar'</code>`. CONNECT records aren't affected by this variable - they are always logged. The user is still logged if it's specified in [server_audit_incl_users](#server_audit_incl_users).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--server-audit-excl-users=value</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>string</code>`
* Default Value: Empty string
* Size limit: 1024 characters



#### `<code>server_audit_file_path</code>`


* Description: When [server_audit_output_type=file](#server_audit_output_type), sets the path and the filename to the log file. If the specified path exists as a directory, then the log will be created inside that directory with the name 'server_audit.log'. Otherwise the value is treated as a filename. The default value is 'server_audit.log', which means this file will be created in the database directory.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--server-audit-file-path=value</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>string</code>`
* Default Value: `<code>server_audit.log</code>`



#### `<code>server_audit_file_rotate_now</code>`


* Description: When [server_audit_output_type=file](#server_audit_output_type), the user can force the log file rotation by setting this variable to ON or 1.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--server-audit-rotate-now[={0|1}]</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`



#### `<code>server_audit_file_rotate_size</code>`


* Description: When [server_audit_output_type=file](#server_audit_output_type), it limits the size of the log file to the given amount of bytes. Reaching that limit turns on the rotation - the current log file is renamed as 'file_path.1'. The empty log file is created as 'file_path' to log into it. The default value is 1000000.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--server-audit-rotate-size=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>1000000</code>`
* Range: `<code>100</code>` to `<code>9223372036854775807</code>`



#### `<code>server_audit_file_rotations</code>`


* Description: When [server_audit_output_type=file](#server_audit_output_type)', this specifies the number of rotations to save. If set to 0 then the log never rotates. The default value is 9.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--server-audit-rotations=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>9</code>`
* Range: `<code>0</code>` to `<code>999</code>`



#### `<code>server_audit_incl_users</code>`


* Description: If not empty, it contains a comma-delimited list of users whose activity will be logged. For example: `<code>SET GLOBAL server_audit_incl_users='user_foo, user_bar'</code>`. CONNECT records aren't affected by this variable - they are always logged. This setting has higher priority than [server_audit_excl_users](#server_audit_excl_users). So if the same user is specified both in incl_ and excl_ lists, they will still be logged.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--server-audit-incl-users=value</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>string</code>`
* Default Value: Empty string
* Size limit: 1024 characters



#### `<code>server_audit_loc_info</code>`


* Description: Used by plugin internals. It has no useful meaning to users.

  * In earlier versions, users see it as a read-only variable.
  * In later versions, it is hidden from the user.
* Commandline: N/A
* Scope: Global
* Dynamic: No
* Data Type: `<code>string</code>`
* Default Value: Empty string
* Introduced: [MariaDB 10.1.12](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10112-release-notes.md), [MariaDB 10.0.24](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-10024-release-notes.md), [MariaDB 5.5.48](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/mariadb-5548-release-notes.md)
* Hidden: [MariaDB 10.1.18](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10118-release-notes.md), [MariaDB 10.0.28](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-10028-release-notes.md), [MariaDB 5.5.53](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/mariadb-5553-release-notes.md)



#### `<code>server_audit_logging</code>`


* Description: Enables/disables the logging. Expected values are ON/OFF. For example: `<code>SET GLOBAL server_audit_logging=on</code>` If the server_audit_output_type is FILE, this will actually create/open the logfile so the [server_audit_file_path](#server_audit_file_path) should be properly specified beforehand. Same about the SYSLOG-related parameters. The logging is turned off by default.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--server-audit-logging[={0|1}]</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`



#### `<code>server_audit_mode</code>`


* Description: This variable doesn't have any distinctive meaning for a user. Its value mostly reflects the server version with which the plugin was started and is intended to be used by developers for testing.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--server-audit-mode[=#]</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>0</code>`
* Range: `<code>0</code>` to `<code>1</code>`



#### `<code>server_audit_output_type</code>`


* Description: Specifies the desired output type. Can be SYSLOG, FILE or null as no output. For example: `<code>SET GLOBAL server_audit_output_type=file</code>` file: log records will be saved into the rotating log file. The name of the file set by [server_audit_file_path](#server_audit_file_path) variable. syslog: log records will be sent to the local syslogd daemon with the standard <syslog.h> API. The default value is 'file'.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--server-audit-output-type=value</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>enum</code>`
* Default Value: `<code>file</code>`
* Valid Values: `<code>SYSLOG</code>`, `<code>FILE</code>`



#### `<code>server_audit_query_log_limit</code>`


* Description: Limit on the length of the query string in a record.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--server-audit-query-log-limit=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>1024</code>`
* Range: `<code>0</code>` to `<code>2147483647</code>`



#### `<code>server_audit_syslog_facility</code>`


* Description: SYSLOG-mode variable. It defines the 'facility' of the records that will be sent to the syslog. Later the log can be filtered by this parameter.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--server-audit-syslog-facility=value</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>enum</code>`
* Default Value: `<code>LOG_USER</code>`
* Valid Values: `<code>LOG_USER</code>`, `<code>LOG_MAIL</code>`, `<code>LOG_DAEMON</code>`, `<code>LOG_AUTH</code>`, `<code>LOG_SYSLOG</code>`, `<code>LOG_LPR</code>`, `<code>LOG_NEWS</code>`, `<code>LOG_UUCP</code>`, `<code>LOG_CRON</code>`, `<code>LOG_AUTHPRIV</code>`, `<code>LOG_FTP</code>`, and `<code>LOG_LOCAL0</code>`–`<code>LOG_LOCAL7</code>`.



#### `<code>server_audit_syslog_ident</code>`


* Description: SYSLOG-mode variable. String value for the 'ident' part of each syslog record. Default value is 'mysql-server_auditing'. New value becomes effective only after restarting the logging.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--server-audit-syslog-ident=value</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>string</code>`
* Default Value: `<code>mysql-server_auditing</code>`



#### `<code>server_audit_syslog_info</code>`


* Description: SYSLOG-mode variable. The 'info' string to be added to the syslog records. Can be changed any time.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--server-audit-syslog-info=value</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>string</code>`
* Default Value: Empty string



#### `<code>server_audit_syslog_priority</code>`


* Description: SYSLOG-mode variable. Defines the priority of the log records for the syslogd.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--server-audit-syslog-priority=value</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>enum</code>`
* Default Value: `<code>LOG_INFO</code>`
* Valid Values:`<code>LOG_EMERG</code>`, `<code>LOG_ALERT</code>`, `<code>LOG_CRIT</code>`, `<code>LOG_ERR</code>`, `<code>LOG_WARNING</code>`, `<code>LOG_NOTICE</code>`, `<code>LOG_INFO</code>`, `<code>LOG_DEBUG</code>`



### Options


#### `<code>server_audit</code>`


* Description: Controls how the server should treat the plugin when the server starts up.

  * Valid values are:

    * `<code>OFF</code>` - Disables the plugin without removing it from the `<code>[mysql.plugins](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/the-mysql-database-tables/mysql-plugin-table.md)</code>` table.
    * `<code>ON</code>` - Enables the plugin. If the plugin cannot be initialized, then the server will still continue starting up, but the plugin will be disabled.
    * `<code>FORCE</code>` - Enables the plugin. If the plugin cannot be initialized, then the server will fail to start with an error.
    * `<code>FORCE_PLUS_PERMANENT</code>` - Enables the plugin. If the plugin cannot be initialized, then the server will fail to start with an error. In addition, the plugin cannot be uninstalled with `<code>[UNINSTALL SONAME](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-soname.md)</code>` or `<code>[UNINSTALL PLUGIN](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-plugin.md)</code>` while the server is running.
  * See [MariaDB Audit Plugin - Installation: Prohibiting Uninstallation](mariadb-audit-plugin-installation.md#prohibiting-uninstallation) for more information on one use case.
  * See [Plugin Overview: Configuring Plugin Activation at Server Startup](../plugin-overview.md#configuring-plugin-activation-at-server-startup) for more information.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--server-audit=val</code>`
* Data Type: `<code>enumerated</code>`
* Default Value: `<code>ON</code>`
* Valid Values: `<code>OFF</code>`, `<code>ON</code>`, `<code>FORCE</code>`, `<code>FORCE_PLUS_PERMANENT</code>`


