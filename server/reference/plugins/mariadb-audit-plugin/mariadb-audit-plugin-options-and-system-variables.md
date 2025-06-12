# MariaDB Audit Plugin Options and System Variables

There are a several options and system variables related to the [MariaDB Audit Plugin](./), once it has been [installed](mariadb-audit-plugin-installation.md). System variables can be displayed using the [SHOW VARIABLES](../../sql-statements/administrative-sql-statements/show/show-variables.md) statement like so:

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

To change the value of one of these variables, you can use the `SET` statement, or set them at the command-line when starting MariaDB. It's recommended that you set them in the MariaDB configuration for the server like so:

```
[mariadb]
...
server_audit_excl_users='bob,ted'
...
```

### System Variables

Below is a list of all system variables related to the Audit Plugin. See [Server System Variables](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md) for a complete list of system variables and instructions on setting them. See also the [full list of MariaDB options, system and status variables](../../full-list-of-mariadb-options-system-and-status-variables.md).

#### `server_audit_events`

* Description: If set, then this restricts audit logging to certain event types. If not set, then every event type is logged to the audit log. For example: SET GLOBAL server\_audit\_events='connect, query'
* Commandline: `--server-audit-events=value`
* Scope: Global
* Dynamic: Yes
* Data Type: `string`
* Default Value: Empty string
* Valid Values:
  * `CONNECT`, `QUERY`, `TABLE` (MariaDB Audit Plugin < 1.2.0)
  * `CONNECT`, `QUERY`, `TABLE`, `QUERY_DDL`, `QUERY_DML` (MariaDB Audit Plugin >= 1.2.0)
  * `CONNECT`, `QUERY`, `TABLE`, `QUERY_DDL`, `QUERY_DML`, `QUERY_DCL` (MariaDB Audit Plugin >=1.3.0)
  * `CONNECT`, `QUERY`, `TABLE`, `QUERY_DDL`, `QUERY_DML`, `QUERY_DCL`, `QUERY_DML_NO_SELECT` (MariaDB Audit Plugin >= 1.4.4)
  * See [MariaDB Audit Plugin - Versions](mariadb-audit-plugin-versions.md) to determine which MariaDB releases contain each MariaDB Audit Plugin versions.

#### `server_audit_excl_users`

* Description: If not empty, it contains the list of users whose activity will NOT be logged. For example: `SET GLOBAL server_audit_excl_users='user_foo, user_bar'`. CONNECT records aren't affected by this variable - they are always logged. The user is still logged if it's specified in [server\_audit\_incl\_users](mariadb-audit-plugin-options-and-system-variables.md#server_audit_incl_users).
* Commandline: `--server-audit-excl-users=value`
* Scope: Global
* Dynamic: Yes
* Data Type: `string`
* Default Value: Empty string
* Size limit: 1024 characters

#### `server_audit_file_path`

* Description: When [server\_audit\_output\_type=file](mariadb-audit-plugin-options-and-system-variables.md#server_audit_output_type), sets the path and the filename to the log file. If the specified path exists as a directory, then the log will be created inside that directory with the name 'server\_audit.log'. Otherwise the value is treated as a filename. The default value is 'server\_audit.log', which means this file will be created in the database directory.
* Commandline: `--server-audit-file-path=value`
* Scope: Global
* Dynamic: Yes
* Data Type: `string`
* Default Value: `server_audit.log`

#### `server_audit_file_rotate_now`

* Description: When [server\_audit\_output\_type=file](mariadb-audit-plugin-options-and-system-variables.md#server_audit_output_type), the user can force the log file rotation by setting this variable to ON or 1.
* Commandline: `--server-audit-rotate-now[={0|1}]`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`

#### `server_audit_file_rotate_size`

* Description: When [server\_audit\_output\_type=file](mariadb-audit-plugin-options-and-system-variables.md#server_audit_output_type), it limits the size of the log file to the given amount of bytes. Reaching that limit turns on the rotation - the current log file is renamed as 'file\_path.1'. The empty log file is created as 'file\_path' to log into it. The default value is 1000000.
* Commandline: `--server-audit-rotate-size=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `1000000`
* Range: `100` to `9223372036854775807`

#### `server_audit_file_rotations`

* Description: When [server\_audit\_output\_type=file](mariadb-audit-plugin-options-and-system-variables.md#server_audit_output_type)', this specifies the number of rotations to save. If set to 0 then the log never rotates. The default value is 9.
* Commandline: `--server-audit-rotations=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `9`
* Range: `0` to `999`

#### `server_audit_incl_users`

* Description: If not empty, it contains a comma-delimited list of users whose activity will be logged. For example: `SET GLOBAL server_audit_incl_users='user_foo, user_bar'`. CONNECT records aren't affected by this variable - they are always logged. This setting has higher priority than [server\_audit\_excl\_users](mariadb-audit-plugin-options-and-system-variables.md#server_audit_excl_users). So if the same user is specified both in incl\_ and excl\_ lists, they will still be logged.
* Commandline: `--server-audit-incl-users=value`
* Scope: Global
* Dynamic: Yes
* Data Type: `string`
* Default Value: Empty string
* Size limit: 1024 characters

#### `server_audit_loc_info`

* Description: Used by plugin internals. It has no useful meaning to users.
  * In earlier versions, users see it as a read-only variable.
  * In later versions, it is hidden from the user.
* Commandline: N/A
* Scope: Global
* Dynamic: No
* Data Type: `string`
* Default Value: Empty string
* Introduced: [MariaDB 10.1.12](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-1-series/mariadb-10112-release-notes), [MariaDB 10.0.24](broken-reference/), [MariaDB 5.5.48](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/mariadb-5548-release-notes)
* Hidden: [MariaDB 10.1.18](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-1-series/mariadb-10118-release-notes), [MariaDB 10.0.28](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/mariadb-10028-release-notes), [MariaDB 5.5.53](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/mariadb-5553-release-notes)

#### `server_audit_logging`

* Description: Enables/disables the logging. Expected values are ON/OFF. For example: `SET GLOBAL server_audit_logging=on` If the server\_audit\_output\_type is FILE, this will actually create/open the logfile so the [server\_audit\_file\_path](mariadb-audit-plugin-options-and-system-variables.md#server_audit_file_path) should be properly specified beforehand. Same about the SYSLOG-related parameters. The logging is turned off by default.
* Commandline: `--server-audit-logging[={0|1}]`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`

#### `server_audit_mode`

* Description: This variable doesn't have any distinctive meaning for a user. Its value mostly reflects the server version with which the plugin was started and is intended to be used by developers for testing.
* Commandline: `--server-audit-mode[=#]`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `0`
* Range: `0` to `1`

#### `server_audit_output_type`

* Description: Specifies the desired output type. Can be SYSLOG, FILE or null as no output. For example: `SET GLOBAL server_audit_output_type=file` file: log records will be saved into the rotating log file. The name of the file set by [server\_audit\_file\_path](mariadb-audit-plugin-options-and-system-variables.md#server_audit_file_path) variable. syslog: log records will be sent to the local syslogd daemon with the standard \<syslog.h> API. The default value is 'file'.
* Commandline: `--server-audit-output-type=value`
* Scope: Global
* Dynamic: Yes
* Data Type: `enum`
* Default Value: `file`
* Valid Values: `SYSLOG`, `FILE`

#### `server_audit_query_log_limit`

* Description: Limit on the length of the query string in a record.
* Commandline: `--server-audit-query-log-limit=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `1024`
* Range: `0` to `2147483647`

#### `server_audit_syslog_facility`

* Description: SYSLOG-mode variable. It defines the 'facility' of the records that will be sent to the syslog. Later the log can be filtered by this parameter.
* Commandline: `--server-audit-syslog-facility=value`
* Scope: Global
* Dynamic: Yes
* Data Type: `enum`
* Default Value: `LOG_USER`
* Valid Values: `LOG_USER`, `LOG_MAIL`, `LOG_DAEMON`, `LOG_AUTH`, `LOG_SYSLOG`, `LOG_LPR`, `LOG_NEWS`, `LOG_UUCP`, `LOG_CRON`, `LOG_AUTHPRIV`, `LOG_FTP`, and `LOG_LOCAL0`–`LOG_LOCAL7`.

#### `server_audit_syslog_ident`

* Description: SYSLOG-mode variable. String value for the 'ident' part of each syslog record. Default value is 'mysql-server\_auditing'. New value becomes effective only after restarting the logging.
* Commandline: `--server-audit-syslog-ident=value`
* Scope: Global
* Dynamic: Yes
* Data Type: `string`
* Default Value: `mysql-server_auditing`

#### `server_audit_syslog_info`

* Description: SYSLOG-mode variable. The 'info' string to be added to the syslog records. Can be changed any time.
* Commandline: `--server-audit-syslog-info=value`
* Scope: Global
* Dynamic: Yes
* Data Type: `string`
* Default Value: Empty string

#### `server_audit_syslog_priority`

* Description: SYSLOG-mode variable. Defines the priority of the log records for the syslogd.
* Commandline: `--server-audit-syslog-priority=value`
* Scope: Global
* Dynamic: Yes
* Data Type: `enum`
* Default Value: `LOG_INFO`
* Valid Values:`LOG_EMERG`, `LOG_ALERT`, `LOG_CRIT`, `LOG_ERR`, `LOG_WARNING`, `LOG_NOTICE`, `LOG_INFO`, `LOG_DEBUG`

### Options

#### `server_audit`

* Description: Controls how the server should treat the plugin when the server starts up.
  * Valid values are:
    * `OFF` - Disables the plugin without removing it from the `[mysql.plugins](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/the-mysql-database-tables/mysql-plugin-table.md)` table.
    * `ON` - Enables the plugin. If the plugin cannot be initialized, then the server will still continue starting up, but the plugin will be disabled.
    * `FORCE` - Enables the plugin. If the plugin cannot be initialized, then the server will fail to start with an error.
    * `FORCE_PLUS_PERMANENT` - Enables the plugin. If the plugin cannot be initialized, then the server will fail to start with an error. In addition, the plugin cannot be uninstalled with `[UNINSTALL SONAME](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-soname.md)` or `[UNINSTALL PLUGIN](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-plugin.md)` while the server is running.
  * See [MariaDB Audit Plugin - Installation: Prohibiting Uninstallation](mariadb-audit-plugin-installation.md#prohibiting-uninstallation) for more information on one use case.
  * See [Plugin Overview: Configuring Plugin Activation at Server Startup](../plugin-overview.md#configuring-plugin-activation-at-server-startup) for more information.
* Commandline: `--server-audit=val`
* Data Type: `enumerated`
* Default Value: `ON`
* Valid Values: `OFF`, `ON`, `FORCE`, `FORCE_PLUS_PERMANENT`

CC BY-SA / Gnu FDL

{% @marketo/form formId="4316" %}
