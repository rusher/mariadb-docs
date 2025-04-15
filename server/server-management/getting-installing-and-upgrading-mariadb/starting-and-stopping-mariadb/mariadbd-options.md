
# mariadbd Options

This page lists all of the options for `<code>mariadbd</code>` (called mysqld before [MariaDB 10.5](../../../../release-notes/mariadb-community-server/what-is-mariadb-105.md)), ordered by topic. For a full alphabetical list of all mariadbd options, as well as server and status variables, see [Full list of MariaDB options, system and status variables](../../variables-and-modes/full-list-of-mariadb-options-system-and-status-variables.md).


In many cases, the entry here is a summary, and links to the full description.


By convention, [server variables](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md) have usually been specified with an underscore in the configuration files, and a dash on the command line. You can however specify underscores as dashes - they are interchangeable.


See [Configuring MariaDB with Option Files](../configuring-mariadb-with-option-files.md) for which files and groups mariadbd reads for it's default options.


Prior to [MariaDB 10.5](../../../../release-notes/mariadb-community-server/what-is-mariadb-105.md), the client used to be called `<code>mysqld</code>`, and can still be accessed under this name, via a symlink in Linux, or an alternate binary in Windows.


## Option Prefixes


#### `<code>--autoset-*</code>`


* Description: Sets the option value automatically. Only supported for certain options.


#### `<code>--disable-*</code>`


* Description: For all boolean options, disables the setting (equivalent to setting it to `<code>0</code>`). Same as `<code>--skip</code>`.


#### `<code>--enable-*</code>`


* Description: For all boolean options, enables the setting (equivalent to setting it to `<code>1</code>`).


#### `<code>--loose-*</code>`


* Description: Don't produce an error if the option doesn't exist.


#### `<code>--maximum-*</code>`


* Description: Sets the maximum value for the option.


#### `<code>--skip-*</code>`


* Description: For all boolean options, disables the setting (equivalent to setting it to `<code>0</code>`). Same as `<code>--disable</code>`.


## Option File Options


#### `<code>--defaults-extra-file</code>`


* Commandline: `<code class="fixed" style="white-space:pre-wrap">--defaults-extra-file=name</code>`
* Description: Read this extra option file after all other option files are read.

  * See [Configuring MariaDB with Option Files](../configuring-mariadb-with-option-files.md).



#### `<code>--defaults-file</code>`


* Commandline: `<code class="fixed" style="white-space:pre-wrap">--defaults-file=name</code>`
* Description: Only read options from the given option file.

  * See [Configuring MariaDB with Option Files](../configuring-mariadb-with-option-files.md).



#### `<code>--defaults-group-suffix</code>`


* Commandline: `<code class="fixed" style="white-space:pre-wrap">--defaults-group-suffix=name</code>`
* Description: In addition to the default option groups, also read option groups with the given suffix.

  * See [Configuring MariaDB with Option Files](../configuring-mariadb-with-option-files.md).



#### `<code>--no-defaults</code>`


* Commandline: `<code class="fixed" style="white-space:pre-wrap">--no-defaults</code>`
* Description: Don't read options from any option file.

  * See [Configuring MariaDB with Option Files](../configuring-mariadb-with-option-files.md).



#### `<code>--print-defaults</code>`


* Commandline: `<code class="fixed" style="white-space:pre-wrap">--print-defaults</code>`
* Description: Read options from option files, print all option values, and then exit the program.

  * See [Configuring MariaDB with Option Files](../configuring-mariadb-with-option-files.md).



## Compatibility Options


The following options have been added to MariaDB to make it more compliant with
other MariaDB and MySQL versions. Options that are also system variables are listed after:


#### `<code>-a, --ansi</code>`


* Description: Use ANSI SQL syntax instead of MariaDB syntax. This mode will also set [transaction isolation level](../../../reference/sql-statements-and-structure/sql-statements/transactions/set-transaction.md) [serializable](../../../reference/sql-statements-and-structure/sql-statements/transactions/set-transaction.md).



#### `<code>--new</code>`


* Description: Use new functionality that will exist in next version of MariaDB. This function exists to make it easier to prepare for an upgrade.



#### `<code>--old-style-user-limits</code>`


* Description: Enable old-style user limits (before MySQL 5.0.3, user resources were counted per each user+host vs. per account).



#### `<code>--safe-mode</code>`


* Description: Disable some potential unsafe optimizations. For 5.2, [INSERT DELAYED](../../../reference/sql-statements-and-structure/sql-statements/data-manipulation/inserting-loading-data/insert-delayed.md) is disabled, [myisam_recover_options](../../../reference/storage-engines/myisam-storage-engine/myisam-system-variables.md#myisam_recover_options) is set to DEFAULT (automatically recover crashed MyISAM files) and the [query cache](../../../reference/plugins/other-plugins/query-cache-information-plugin.md) is disabled. For [Aria](../../../reference/storage-engines/s3-storage-engine/aria_s3_copy.md) tables, disable bulk insert optimization to enable one to use [aria_read_log](../../../clients-and-utilities/aria-clients-and-utilities/aria_read_log.md) to recover tables even if tables are deleted (good for testing recovery).



#### `<code>--skip-new</code>`


* Description: Disables [--new](#-new).



### Compatibility Options and System Variables


* [--old](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#old)
* [--old-alter-table](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#old_alter_table)
* [--old-mode](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#old_mode)
* [--old-passwords](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#old_passwords)
* [--show-old-temporals](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#show_old_temporals)


## Locale Options


Options that are also system variables are listed after:


#### `<code>--character-set-client-handshake</code>`


* Commandline: `<code class="fixed" style="white-space:pre-wrap">--character-set-client-handshake</code>`
* Description: Don't ignore client side character set value sent during handshake. `<code>--skip-character-set-client-handshake</code>` will ignore the client value and use the default server value.



#### `<code>--default-character-set</code>`


* Commandline: `<code class="fixed" style="white-space:pre-wrap">--default-character-set=name</code>`
* Description: Still available as an option for setting the default character set for clients and their connections, it was deprecated and removed in [MariaDB 10.2](../../../../release-notes/mariadb-community-server/what-is-mariadb-102.md) as a server option. Use [character-set-server](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#character_set_server) instead.



#### `<code>--language</code>`


* Description: This option can be used to set the server's language for error messages. This option can be specified either as a language name or as the path to the directory storing the language's [error message file](../../server-monitoring-logs/error-log.md#error-messages-file). See [Server Locales](../../../reference/data-types/string-data-types/character-sets/internationalization-and-localization/server-locale.md) for a list of supported locales and their associated languages.

  * This option is deprecated. Use the `<code>[lc_messages](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#lc_messages)</code>` and `<code>[lc_messages_dir](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#lc_messages_dir)</code>` system variables instead.
  * See [Setting the Language for Error Messages](../../../reference/data-types/string-data-types/character-sets/internationalization-and-localization/setting-the-language-for-error-messages.md) for more information.



### Locale Options and System Variables


* [character-set-filesystem](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#character_set_filesystem)
* [character-set-client](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#character_set_client)
* [character-set-connection](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#character_set_connection)
* [character-set-database](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#character_set_database)
* [character-set-filesystem](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#character_set_filesystem)
* [character-set-results](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#character_set_results)
* [character-set-server](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#character_set_server)
* [character-set-system](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#character_set_system)
* [character-sets-dir](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#character_sets_dir)
* [collation-connection](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#collation_connection)
* [collation-database](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#collation_database)
* [collation-server](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#collation_server)
* [default-week-format](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#default_week_format)
* [default-time-zone](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#time_zone)
* [lc-messages](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#lc_messages)
* [lc-messages-dir](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#lc_messages_dir)
* [lc-time-names](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#lc_time_names)


## Windows Options


Options that are also system variables are listed after:


#### `<code>--console</code>`


* Description: Windows-only option that keeps the console window open and for writing log messages to stderr and stdout. If specified together with [--log-error](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#log_error), the last option will take precedence.



#### `<code>--install</code>`


* Description: Windows-only option that installs the `<code>mariadbd</code>` process as a Windows service.

  * The Windows service created with this option [auto-starts](https://docs.microsoft.com/en-us/windows/desktop/Services/automatically-starting-services). If you want a service that is [started on demand](https://docs.microsoft.com/en-us/windows/desktop/Services/starting-services-on-demand), then use the `<code>[--install-manual](#install-manual)</code>` option.
  * This option takes a service name as an argument. If this option is provided without a service name, then the service name defaults to "MARIADB".
  * This option is deprecated and may be removed in a future version. See [MDEV-19358](https://jira.mariadb.org/browse/MDEV-19358) for more information.



#### `<code>--install-manual</code>`


* Description: Windows-only option that installs the `<code>mariadbd</code>` process as a Windows service.

  * The Windows service created with this option is [started on demand](https://docs.microsoft.com/en-us/windows/desktop/Services/starting-services-on-demand). If you want a service that [auto-starts](https://docs.microsoft.com/en-us/windows/desktop/Services/automatically-starting-services), use the `<code>[--install](#install)</code>` option.
  * This option takes a service name as an argument. If this option is provided without a service name, then the service name defaults to "MARIADB".
  * This option is deprecated and may be removed in a future version. See [MDEV-19358](https://jira.mariadb.org/browse/MDEV-19358) for more information.



#### `<code>--remove</code>`


* Description: Windows-only option that removes the Windows service created by the `<code>[--install](#install)</code>` or `<code>[--install-manual](#install-manual)</code>` options.

  * This option takes a service name as an argument. If this option is provided without a service name, then the service name defaults to "MARIADB".
  * This option is deprecated and may be removed in a future version. See [MDEV-19358](https://jira.mariadb.org/browse/MDEV-19358) for more information.



#### `<code>--slow-start-timeout</code>`


* Description: Windows-only option that defines the maximum number of milliseconds that the service control manager should wait before trying to kill the Windows service during startup. Defaults to `<code>15000</code>`.



#### `<code>--standalone</code>`


* Description: Windows-only option that has no effect. Kept for compatibility reasons.



### Windows Options and System Variables


The following options and system variables are related to using MariaDB on Windows:


* `<code>[--named-pipe](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#named_pipe)</code>`


## Replication and Binary Logging Options


The following options are related to [replication](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/README.md) and the [binary log](../../../reference/storage-engines/innodb/binary-log-group-commit-and-innodb-flushing-performance.md). Options that are also system variables are listed after:


#### `<code>--abort-slave-event-count</code>`


* Commandline: `<code class="fixed" style="white-space:pre-wrap">--abort-slave-event-count=#</code>`
* Description: Option used by mysql-test for debugging and testing of replication.



#### `<code>--binlog-do-db</code>`


* Commandline: `<code class="fixed" style="white-space:pre-wrap">--binlog-do-db=name</code>`
* Description: This option allows you to configure a [replication master](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/README.md) to write statements and transactions affecting databases that match a specified name into its [binary log](../../../reference/storage-engines/innodb/binary-log-group-commit-and-innodb-flushing-performance.md). Since the filtered statements or transactions will not be present in the [binary log](../../../reference/storage-engines/innodb/binary-log-group-commit-and-innodb-flushing-performance.md), its replicas will not be able to replicate them.

  * This option will not work with cross-database updates with [statement-based logging](../../server-monitoring-logs/binary-log/binary-log-formats.md#statement-based-logging). See the [Statement-Based Logging](../../../server-usage/replication-cluster-multi-master/standard-replication/replication-filters.md#statement-based-logging) section for more information.
  * This option can not be set dynamically. Available as a [system variable](../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md#binlog_do_db) from [MariaDB 11.2.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-2-series/mariadb-11-2-0-release-notes.md).
  * When setting it on the command-line or in a server [option group](../configuring-mariadb-with-option-files.md#option-groups) in an [option file](../configuring-mariadb-with-option-files.md), the option does not accept a comma-separated list. If you would like to specify multiple filters, then you need to specify the option multiple times.
  * See [Replication Filters](../../../server-usage/replication-cluster-multi-master/standard-replication/replication-filters.md) for more information.



#### `<code>--binlog-ignore-db</code>`


* Commandline: `<code class="fixed" style="white-space:pre-wrap">--binlog-ignore-db=name</code>`
* Description: This option allows you to configure a [replication master](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/README.md) to not write statements and transactions affecting databases that match a specified name into its [binary log](../../../reference/storage-engines/innodb/binary-log-group-commit-and-innodb-flushing-performance.md). Since the filtered statements or transactions will not be present in the [binary log](../../../reference/storage-engines/innodb/binary-log-group-commit-and-innodb-flushing-performance.md), its replicas will not be able to replicate them.

  * This option will not work with cross-database updates with [statement-based logging](../../server-monitoring-logs/binary-log/binary-log-formats.md#statement-based-logging). See the [Statement-Based Logging](../../../server-usage/replication-cluster-multi-master/standard-replication/replication-filters.md#statement-based-logging) section for more information.
  * This option can not be set dynamically. Available as a [system variable](../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md#binlog_ignore_db) from [MariaDB 11.2.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-2-series/mariadb-11-2-0-release-notes.md).
  * When setting it on the command-line or in a server [option group](../configuring-mariadb-with-option-files.md#option-groups) in an [option file](../configuring-mariadb-with-option-files.md), the option does not accept a comma-separated list. If you would like to specify multiple filters, then you need to specify the option multiple times.
  * See [Replication Filters](../../../server-usage/replication-cluster-multi-master/standard-replication/replication-filters.md) for more information.



#### `<code>--binlog-row-event-max-size</code>`


* Commandline: `<code class="fixed" style="white-space:pre-wrap">--binlog-row-event-max-size=#</code>`
* Description: The maximum size of a row-based [binary log](../../../reference/storage-engines/innodb/binary-log-group-commit-and-innodb-flushing-performance.md) event in bytes. Rows will be grouped into events smaller than this size if possible. The value has to be a multiple of 256. Available as a [system variable](../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md#binlog_row_event_max_size) from [MariaDB 11.2.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-2-series/mariadb-11-2-0-release-notes.md).
* Default value `<code>8192</code>`



#### `<code>--disconnect-slave-event-count</code>`


* Commandline: `<code class="fixed" style="white-space:pre-wrap">--disconnect-slave-event-count=#</code>`
* Description: Option used by mysql-test for debugging and testing of replication.



#### `<code>--flashback</code>`


* Commandline: `<code class="fixed" style="white-space:pre-wrap">--flashback</code>`
* Description: Setup the server to use flashback. This enables the [binary log](../../../reference/storage-engines/innodb/binary-log-group-commit-and-innodb-flushing-performance.md) and sets `<code>binlog_format=ROW</code>`.



#### `<code>--init-rpl-role</code>`


* Commandline: `<code class="fixed" style="white-space:pre-wrap">--init-rpl-role=name</code>`
* Description: Set the replication role. From [MariaDB 10.6.19](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-10-6-19-release-notes.md), [MariaDB 10.11.9](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-11-series/mariadb-10-11-9-release-notes.md), [MariaDB 11.1.6](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-1-series/mariadb-11-1-6-release-notes.md), [MariaDB 11.2.5](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-2-series/mariadb-11-2-5-release-notes.md), [MariaDB 11.4.3](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-4-series/mariadb-11-4-3-release-notes.md) and [MariaDB 11.5.2](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-5-rolling-releases/mariadb-11-5-2-release-notes.md), changes the condition for [semi-sync recovery](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/semisynchronous-replication-plugin-status-variables.md) to truncate the [binlog](../../../reference/storage-engines/innodb/binary-log-group-commit-and-innodb-flushing-performance.md) to instead use this option, when set to SLAVE. This allows for both [rpl_semi_sync_master_enabled](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/semisynchronous-replication-plugin-status-variables.md#rpl_semi_sync_master_enabled) and [rpl_semi_sync_slave_enabled](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/semisynchronous-replication-plugin-status-variables.md#rpl_semi_sync_slave_enabled) to be set for a primary that is restarted, and no transactions will be lost, so long as `<code>--init-rpl-role</code>` is not set to SLAVE. In earlier versions, for servers configured with both [rpl_semi_sync_master_enabled=1](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/semisynchronous-replication-plugin-status-variables.md#rpl_semi_sync_master_enabled) and [rpl_semi_sync_slave_enabled=1](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/semisynchronous-replication-plugin-status-variables.md#rpl_semi_sync_slave_enabled), if a primary is just re-started (i.e. retaining its role as primary), it can truncate its binlog to drop transactions which its replica(s) have already received and executed. If this happens, when the replica reconnects, its [gtid_slave_pos](../../../server-usage/replication-cluster-multi-master/standard-replication/gtid.md) can be ahead of the recovered primary’s [gtid_binlog_pos](../../../server-usage/replication-cluster-multi-master/standard-replication/gtid.md), resulting in an error state where the replica’s state is ahead of the primary’s. See [-init-rpl-role](mariadbd-options.md#-init-rpl-role).
* Valid values: Empty, `<code>MASTER</code>` or `<code>SLAVE</code>`



#### `<code>--log-basename</code>`


* Commandline: `<code class="fixed" style="white-space:pre-wrap">--log-basename=name</code>`
* Description: Basename for all log files and the .pid file. This sets all log file names at once (in 'datadir') and is normally the only option you need for specifying log files. This is especially recommended to be set if you are using [replication](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/README.md) as it ensures that your log file names are not dependent on your host name. Sets names for the [binary log](../../../reference/storage-engines/innodb/binary-log-group-commit-and-innodb-flushing-performance.md), [relay log](../../server-monitoring-logs/binary-log/relay-log.md), [general query log](../../server-monitoring-logs/general-query-log.md), [slow query log](../../server-monitoring-logs/slow-query-log/slow-query-log-overview.md) and [error log](../../server-monitoring-logs/error-log.md). Note that if you explicity set log file names with any of these other options; [log-bin-index](../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md), [relay-log](../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md), [relay-log-index](../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md), [general-log-file](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#general_log_file), [log_slow_query_file](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#log_slow_query_file) ([slow_query_log_file](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#slow_query_log_file)), [log_error](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#log_error), and [pid-file](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#pid_file), these should be placed after `<code>--log-basename</code>` in the config files. Later settings override earlier settings, so `<code>log-basename</code>` will override any earlier log file name settings.



#### `<code>--log-bin-trust-routine-creators</code>`


* Commandline: `<code class="fixed" style="white-space:pre-wrap">--log-bin-trust-routine-creators</code>`
* Description: Deprecated, use [log-bin-trust-function-creators](../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md).



#### `<code>--master-host</code>`


* Commandline: `<code class="fixed" style="white-space:pre-wrap">--master-host=name</code>`
* Description: Primary hostname or IP address for replication. If not set, the replica thread will not be started. Note that the setting of master-host will be ignored if there exists a valid master.info file.



#### `<code>--master-info-file</code>`


* Commandline: `<code class="fixed" style="white-space:pre-wrap">--master-info-file=name</code>`
* Description: Name and location of the file on the replica where the `<code>MASTER_LOG_FILE</code>` and `<code>MASTER_LOG_POS</code>` options (i.e. the [binary log](../../../reference/storage-engines/innodb/binary-log-group-commit-and-innodb-flushing-performance.md) position on the primary) and most other [CHANGE MASTER](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md) options are written. The [replica's I/O thread](../../../server-usage/replication-cluster-multi-master/standard-replication/replication-threads.md#replica-io-thread) keeps this [binary log](../../../reference/storage-engines/innodb/binary-log-group-commit-and-innodb-flushing-performance.md) position updated as it downloads events.

  * See [CHANGE MASTER TO: Option Persistence](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md#option-persistence) for more information.



#### `<code>--master-password</code>`


* Commandline: `<code class="fixed" style="white-space:pre-wrap">--master-password=name</code>`
* Description: The password the replica thread will authenticate with when connecting to the primary. If not set, an empty password is assumed. The value in master.info will take precedence if it can be read.



#### `<code>--master-port</code>`


* Commandline: `<code class="fixed" style="white-space:pre-wrap">--master-port=#</code>`
* Description: The port the master is listening on. If not set, the compiled setting of MYSQL_PORT is assumed. If you have not tinkered with configure options, this should be 3306. The value in master.info will take precedence if it can be read.



#### `<code>--master-retry-count</code>`


* Commandline: `<code class="fixed" style="white-space:pre-wrap">--master-retry-count=#</code>`
* Description: Number of times a replica will attempt to connect to a primary before giving up. The retry interval is determined by the MASTER_CONNECT_RETRY option for the CHANGE MASTER statement. A value of 0 means the replica will not stop attempting to reconnect. Reconnects are triggered when a replica has timed out. See [slave_net_timeout](../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md).
* Default Value: `<code>86400</code>` through 10.5, `<code>100000</code>` as of 10.6
* Range - 32 bit: `<code>0 to 4294967295</code>`
* Range - 64 bit: `<code>0 to 18446744073709551615</code>`



#### `<code>--master-ssl</code>`


* Commandline: `<code class="fixed" style="white-space:pre-wrap">--master-ssl</code>`
* Description: Enable the replica to [connect to the master using TLS](../../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/secure-connections-overview.md).



#### `<code>--master-ssl-ca</code>`


* Commandline: `<code class="fixed" style="white-space:pre-wrap">--master-ssl-ca[=name]</code>`
* Description: Master TLS CA file. Only applies if you have enabled [master-ssl](#-master-ssl).



#### `<code>--master-ssl-capath</code>`


* Commandline: `<code class="fixed" style="white-space:pre-wrap">--master-ssl-capath[=name]</code>`
* Description: Master TLS CA path. Only applies if you have enabled [master-ssl](#-master-ssl).



#### `<code>--master-ssl-cert</code>`


* Commandline: `<code class="fixed" style="white-space:pre-wrap">--master-ssl-cert[=name]</code>`
* Description: Master TLS certificate file name. Only applies if you have enabled [master-ssl](#-master-ssl).



#### `<code>--master-ssl-cipher</code>`


* Commandline: `<code class="fixed" style="white-space:pre-wrap">--master-ssl-cipher[=name]</code>`
* Description: Master TLS cipher. Only applies if you have enabled [master-ssl](#-master-ssl).



#### `<code>--master-ssl-key</code>`


* Commandline: `<code class="fixed" style="white-space:pre-wrap">--master-ssl-key[=name]</code>`
* Description: Master TLS keyfile name. Only applies if you have enabled [master-ssl](#-master-ssl).



#### `<code>--master-user</code>`


* Commandline: `<code class="fixed" style="white-space:pre-wrap">--master-user=name</code>`
* Description: The username the replica thread will use for authentication when connecting to the primary. The user must have FILE privilege. If the primary user is not set, user test is assumed. The value in master.info will take precedence if it can be read.



#### `<code>--max-binlog-dump-events</code>`


* Commandline: `<code class="fixed" style="white-space:pre-wrap">--max-binlog-dump-events=#</code>`
* Description: Option used by mysql-test for debugging and testing of replication.



#### `<code>--replicate-same-server-id</code>`


* Commandline: `<code class="fixed" style="white-space:pre-wrap">--replicate-same-server-id</code>`
* Description: In replication, if set to 1, do not skip events having our server id. Default value is 0 (to break infinite loops in circular replication). Can't be set to 1 if [log-slave-updates](../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md) is used.



#### `<code>--sporadic-binlog-dump-fail</code>`


* Commandline: `<code class="fixed" style="white-space:pre-wrap">--sporadic-binlog-dump-fail</code>`
* Description: Option used by mysql-test for debugging and testing of replication.



#### `<code>--sysdate-is-now</code>`


* Commandline: `<code class="fixed" style="white-space:pre-wrap">--sysdate-is-now</code>`
* Description: Non-default option to alias [SYSDATE()](../../../reference/sql-statements-and-structure/sql-statements/built-in-functions/date-time-functions/sysdate.md) to [NOW()](../../../reference/sql-statements-and-structure/sql-statements/built-in-functions/date-time-functions/now.md) to make it safe for [replication](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/README.md). Since 5.0, SYSDATE() has returned a `dynamic' value different for different invocations, even within the same statement.



### Replication and Binary Logging Options and System Variables


The following options and system variables are related to [replication](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/README.md) and the [binary log](../../../reference/storage-engines/innodb/binary-log-group-commit-and-innodb-flushing-performance.md):


* [auto-increment-increment](../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md)
* [auto-increment-offset](../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md)
* [binlog-alter-two-phase](../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md)
* [binlog-annotate-row-events](../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md)
* [binlog-cache-size](../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md)
* [binlog-checksum](../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md)
* [binlog-commit-wait-count](../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md)
* [binlog-commit-wait-usec](../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md)
* [binlog-direct-non-transactional-updates|](../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md)
* [binlog-expire-logs-seconds](../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md)
* [binlog-file-cache-size](../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md)
* [binlog-format](../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md)
* [binlog-gtid-index](../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md)
* [binlog-gtid-index-page-size](../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md)
* [binlog-gtid-index-span-min](../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md)
* [binlog-large-commit-threshold](../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md)
* [binlog-legacy-event-pos](../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md)
* [binlog-optimize-thread-scheduling](../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md)
* [binlog-row-image](../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md)
* [binlog-row-metadata](../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md)
* [binlog-space-limit](../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md)
* [binlog-stmt-cache-size](../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md)
* [default-master-connection](../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md)
* [gtid-cleanup-batch-size](../../../server-usage/replication-cluster-multi-master/standard-replication/gtid.md)
* [gtid-domain-id](../../../server-usage/replication-cluster-multi-master/standard-replication/gtid.md)
* [gtid-ignore-duplicates](../../../server-usage/replication-cluster-multi-master/standard-replication/gtid.md)
* [gtid-strict-mode](../../../server-usage/replication-cluster-multi-master/standard-replication/gtid.md)
* [init-slave](../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md)
* [log-bin](../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md)
* [log-bin-compress](../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md)
* [log-bin-compress-min-len](../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md)
* [log-bin-index](../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md)
* [log-bin-trust-function-creators](../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md)
* [log-slave-updates](../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md)
* [master-verify-checksum](../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md)
* [max-binlog-cache-size](../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md)
* [max-binlog-size](../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md)
* [max-binlog-stmt-cache-size](../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md)
* [max-binlog-total-size](../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md)
* [max-relay-log-size](../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md)
* [read-binlog-speed-limit](../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md)
* [relay-log](../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md)
* [relay-log-index](../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md)
* [relay-log-info-file](../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md)
* [relay-log-purge](../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md)
* [relay-log-recovery](../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md)
* [relay-log-space-limit](../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md)
* [replicate-annotate-row-events](../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md)
* [replicate-do-db](../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md)
* [replicate-do-table](../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md)
* [replicate-events-marked-for-skip](../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md)
* [replicate-ignore-db](../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md)
* [replicate-ignore-table](../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md)
* [replicate-rewrite-db](../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md)
* [replicate-wild-do-table](../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md)
* [replicate-wild-ignore-table](../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md)
* [report-host](../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md)
* [report-password](../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md)
* [report-port](../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md)
* [report-user](../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md)
* [rpl-recovery-rank](../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md)
* [server-id](../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md)
* [slave-abort-blocking-timeout](../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md#slave_abort_blocking_timeout)
* [slave-compressed-protocol](../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md)
* [slave-connections-needed-for-purge](../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md)
* [slave-ddl-exec-mode](../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md)
* [slave-domain-parallel-threads](../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md)
* [slave-exec-mode](../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md)
* [slave-load-tmpdir](../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md)
* [slave-max-allowed-packet](../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md)
* [slave-max-statement-time](../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md)
* [slave-net-timeout](../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md)
* [slave-parallel-max-queued](../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md)
* [slave-parallel-threads](../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md)
* [slave-run-triggers-for-rbr](../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md)
* [slave-skip-errors](../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md)
* [slave-sql-verify-checksum](../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md)
* [slave-transaction-retries](../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md)
* [slave_transaction_retry_errors](../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md)
* [slave_transaction_retry_interval](../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md)
* [slave-type-conversions](../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md)
* [sync-binlog](../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md)
* [sync-master-info](../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md)
* [sync-relay-log](../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md)
* [sync-relay-log-info](../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md)


### Semisynchronous Replication Options and System Variables


The options and system variables related to [Semisynchronous Replication](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/semisynchronous-replication-plugin-status-variables.md) are described [here](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/semisynchronous-replication-plugin-status-variables.md#system-variables).


## Optimizer Options


Options that are also system variables are listed after:


#### `<code>--record-buffer</code>`


* Commandline: `<code class="fixed" style="white-space:pre-wrap">--record-buffer=#</code>`
* Description: Old alias for [read_buffer_size](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#read_buffer_size).
* Removed: [MariaDB 5.5](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5.md)



#### `<code>--table-cache</code>`


* Commandline: `<code class="fixed" style="white-space:pre-wrap">--table-open-cache=#</code>`
* Description: Removed; use [--table-open-cache](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#table_open_cache) instead.
* Removed: [MariaDB 5.1.3](https://mariadb.com/kb/en/mariadb-513-release-notes/)



### Optimizer Options and System Variables


* [alter-algorithm](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#alter_algorithm)
* [analyze-sample-percentage](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#analyze_sample_percentage)
* [big-tables](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#big_tables)
* [bulk-insert-buffer-size](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#bulk_insert_buffer_size)
* [expensive-subquery-limit](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#expensive_subquery_limit)
* [join-buffer-size](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#join_buffer_size)
* [join-buffer-space-limit](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#join_buffer_space_limit)
* [join-cache-level](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#join_cache_level)
* [max-heap-table-size](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#max_heap_table_size)
* [max-join-size](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#max_join_size)
* [max-seeks-for-key](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#max_seeks_for_key)
* [max-sort-length](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#max_sort_length)
* [mrr-buffer-size](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#mrr_buffer_size)
* [optimizer-adjust-secondary-key-costs](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/query-optimizations/optimizer_adjust_secondary_key_costs.md)
* [optimizer-extra-pruning-depth](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#optimizer_extra_pruning_depth)
* [optimizer-join-limit-pref-ratio](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#optimizer_join_limit_pref_ratio)
* [optimizer-max-sel-arg-weight](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#optimizer_max_sel_arg_weight)
* [optimizer-max-sel-args](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#optimizer_max_sel_args)
* [optimizer-prune-level](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#optimizer_prune_level)
* [optimizer-search-depth](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#optimizer_search_depth)
* [optimizer-selectivity-sampling-limit](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#optimizer_selectivity_sampling_limit)
* [optimizer-switch](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#optimizer_switch)
* [optimizer-trace](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#optimizer_trace)
* [optimizer-trace-max-mem-size](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#optimizer_trace_max_mem_size)
* [optimizer-use-condition-selectivity](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#optimizer_use_condition_selectivity)
* [query-alloc-block-size](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#query_alloc_block_size)
* [query-prealloc-size](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#query_prealloc_size)
* [range-alloc-block-size](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#range_alloc_block_size)
* [read-buffer-size](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#read_buffer_size)
* [rowid-merge-buff-size](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#rowid_merge_buff_size)
* [table-definition-cache](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#table_definition_cache)
* [table-open-cache](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#table_open_cache)
* [table-open-cache-instances](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#table_open_cache_instances)
* [tmp-disk-table-size](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#tmp_disk_table_size)
* [tmp-memory-table-size](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#tmp_memory_table_size)
* [tmp-table-size](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#tmp_table_size)
* [use-stat-tables](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#use_stat_tables)


## Storage Engine Options


#### `<code>--skip-bdb</code>`


* Commandline: `<code class="fixed" style="white-space:pre-wrap">----skip-bdb</code>`
* Description: Deprecated option; Exists only for compatibility with very old my.cnf files.
* Removed: [MariaDB 10.5.1](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1051-release-notes.md)



#### `<code>--external-locking</code>`


* Commandline: `<code class="fixed" style="white-space:pre-wrap">--external-locking</code>`
* Description: Use system (external) locking (disabled by default). With this option enabled you can run [myisamchk](../../../clients-and-utilities/myisam-clients-and-utilities/myisamchk-table-information.md) to test (not repair) tables while the server is running. Disable with [--skip-external-locking](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#skip_external_locking). From [MariaDB 10.2.40](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-10240-release-notes.md), [MariaDB 10.3.31](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-10331-release-notes.md), [MariaDB 10.4.21](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-4-series/mariadb-10421-release-notes.md), [MariaDB 10.5.12](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-10512-release-notes.md), [MariaDB 10.6.4](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-1064-release-notes.md) and all later version, this effects InnoDB and can be used to prevent multiple instances running on the same data.



### MyISAM Storage Engine Options


The options related to the [MyISAM](../../../reference/storage-engines/myisam-storage-engine/README.md) storage engine are described below. Options that are also system variables are listed after:


#### `<code>--log-isam</code>`


* Commandline: `<code class="fixed" style="white-space:pre-wrap">--log-isam[=file_name]</code>`
* Description: Enable the [MyISAM log](../../server-monitoring-logs/myisam-log.md), which logs all MyISAM changes to file. If no filename is provided, the default, myisam.log is used.



#### MyISAM Storage Engine Options and System Variables


Some options and system variables related to the [MyISAM](../../../reference/storage-engines/myisam-storage-engine/README.md) storage engine can be found [here](../../../reference/storage-engines/myisam-storage-engine/myisam-system-variables.md). Direct links to many of them can be found below.


* [concurrent-insert](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#concurrent_insert)
* [delayed-insert-limit](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#delayed_insert_limit)
* [delayed-insert-timeout](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#delayed_insert_timeout)
* [delayed-queue-size](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#delayed_queue_size)
* [keep-files-on-create](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#keep_files_on_create)
* [key-buffer-size](../../../reference/storage-engines/myisam-storage-engine/myisam-system-variables.md#key_buffer_size)
* [key-cache-age-threshold](../../../reference/storage-engines/myisam-storage-engine/myisam-system-variables.md#key_cache_age_threshold)
* [key-cache-block-size](../../../reference/storage-engines/myisam-storage-engine/myisam-system-variables.md#key_cache_block_size)
* [key-cache-division-limit](../../../reference/storage-engines/myisam-storage-engine/myisam-system-variables.md#key_cache_division_limit)
* [key-cache-file-hash-size](../../../reference/storage-engines/myisam-storage-engine/myisam-system-variables.md#key_cache_file_hash_size)
* [key-cache-segments](../../../reference/storage-engines/myisam-storage-engine/myisam-system-variables.md#key_cache_segments)
* [myisam-block-size](../../../reference/storage-engines/myisam-storage-engine/myisam-system-variables.md)
* [myisam-data-pointer-size](../../../reference/storage-engines/myisam-storage-engine/myisam-system-variables.md)
* [myisam-max-sort-file-size](../../../reference/storage-engines/myisam-storage-engine/myisam-system-variables.md)
* [myisam-mmap-size](../../../reference/storage-engines/myisam-storage-engine/myisam-system-variables.md)
* [myisam-recover-options](../../../reference/storage-engines/myisam-storage-engine/myisam-system-variables.md)
* [myisam-repair-threads](../../../reference/storage-engines/myisam-storage-engine/myisam-system-variables.md)
* [myisam-sort-buffer-size](../../../reference/storage-engines/myisam-storage-engine/myisam-system-variables.md)
* [myisam-stats-method](../../../reference/storage-engines/myisam-storage-engine/myisam-system-variables.md)
* [myisam-use-mmap](../../../reference/storage-engines/myisam-storage-engine/myisam-system-variables.md)


### InnoDB Storage Engine Options


The options related to the [InnoDB](../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/innodb-upgrade-tests/README.md) storage engine are described below. Options that are also system variables are listed after:


#### `<code>--innodb</code>`


* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb=value</code>`, `<code class="fixed" style="white-space:pre-wrap">--skip-innodb</code>`
* Description: This variable controls whether or not to load the InnoDB storage engine. Possible values are `<code>ON</code>`, `<code>OFF</code>`, `<code>FORCE</code>` or `<code>FORCE_PLUS_PERMANENT</code>` (from [MariaDB 5.5](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5.md)). If set to `<code>OFF</code>` (the same as --skip-innodb), since InnoDB is the default storage engine, the server will not start unless another storage engine has been chosen with [--default-storage-engine](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#default_storage_engine). `<code>FORCE</code>` means that the storage engine must be successfully loaded, or else the server won't start. `<code>FORCE_PLUS_PERMANENT</code>` enables the plugin, but if plugin cannot initialize, the server will not start. In addition, the plugin cannot be uninstalled while the server is running.



#### `<code>--innodb-cmp</code>`


* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-cmp</code>`
* Description:
* Default: `<code>ON</code>`



#### `<code>--innodb-cmp-reset</code>`


* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-cmp-reset</code>`
* Description:
* Default: `<code>ON</code>`



#### `<code>--innodb-cmpmem</code>`


* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-cmpmem</code>`
* Description:
* Default: `<code>ON</code>`



#### `<code>--innodb-cmpmem-reset</code>`


* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-cmpmem-reset</code>`
* Description:
* Default: `<code>ON</code>`



#### `<code>--innodb-file-io-threads</code>`


* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-file-io-threads</code>`
* Description:
* Default: `<code>4</code>`
* Removed: [MariaDB 10.3.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1030-release-notes.md)



#### `<code>--innodb-index-stats</code>`


* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-index-stats</code>`
* Description:
* Default: `<code>ON</code>`
* Removed: [MariaDB 10.0.0](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-1000-release-notes.md)



#### `<code>--innodb-lock-waits</code>`


* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-lock-waits</code>`
* Description:
* Default: `<code>ON</code>`



#### `<code>--innodb-locks</code>`


* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-locks</code>`
* Description:
* Default: `<code>ON</code>`



#### `<code>--innodb-rseg</code>`


* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-rseg</code>`
* Description:
* Default: `<code>ON</code>`
* Removed: [MariaDB 10.0.0](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-1000-release-notes.md)



#### `<code>--innodb-status-file</code>`


* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-status-file</code>`
* Description:
* Default: `<code>FALSE</code>`



#### `<code>--innodb-sys-indexes</code>`


* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-sys-indexes</code>`
* Description:
* Default: `<code>ON</code>`



#### `<code>--innodb-sys-stats</code>`


* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-sys-stats</code>`
* Description:
* Default: `<code>ON</code>`
* Removed: [MariaDB 10.0.0](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-1000-release-notes.md)



#### `<code>--innodb-sys-tables</code>`


* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-sys-tables</code>`
* Description:
* Default: `<code>ON</code>`



#### `<code>--innodb-table-stats</code>`


* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-table-stats</code>`
* Description:
* Default: `<code>ON</code>`
* Removed: [MariaDB 10.0.0](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-1000-release-notes.md)



#### `<code>--innodb-trx</code>`


* Commandline: `<code class="fixed" style="white-space:pre-wrap">--innodb-trx</code>`
* Description:
* Default: `<code>ON</code>`



#### InnoDB Storage Engine Options and System Variables


Some options and system variables related to the [InnoDB](../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/innodb-upgrade-tests/README.md) storage engine can be found [here](../../../reference/storage-engines/innodb/innodb-system-variables.md). Direct links to many of them can be found below.


* [ignore-builtin-innodb](../../../reference/storage-engines/innodb/innodb-system-variables.md#ignore_builtin_innodb)
* [innodb-adaptive-checkpoint](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_adaptive_checkpoint)
* [innodb-adaptive-flushing](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_adaptive_flushing)
* [innodb-adaptive-flushing-lwm](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_adaptive_flushing_lwm)
* [innodb-adaptive-flushing-method](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_adaptive_flushing_method)
* [innodb-adaptive-hash-index](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_adaptive_hash_index)
* [innodb-adaptive-hash-index-partitions](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_adaptive_hash_index_partitions)
* [innodb-adaptive-hash-index-parts](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_adaptive_hash_index_parts)
* [innodb-adaptive-max-sleep-delay](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_adaptive_max_sleep_delay)
* [innodb-additional-mem-pool-size](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_additional_mem_pool_size)
* [innodb-alter-copy-bulk](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_alter_copy_bulk)
* [innodb-api-bk-commit-interval](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_api_bk_commit_interval)
* [innodb-api-disable-rowlock](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_api_disable_rowlock)
* [innodb-api-enable-binlog](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_api_enable_binlog)
* [innodb-api-enable-mdl](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_api_enable_mdl)
* [innodb-api-trx-level](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_api_trx_level)
* [innodb-auto-lru-dump](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_auto_lru_dump)
* [innodb-autoextend-increment](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_autoextend_increment)
* [innodb-autoinc-lock-mode](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_autoinc_lock_mode)
* [innodb-background-scrub-data-check-interval](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_background_scrub_data_check_interval)
* [innodb-background-scrub-data-compressed](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_background_scrub_data_compressed)
* [innodb-background-scrub-data-interval](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_background_scrub_data_interval)
* [innodb-background-scrub-data-uncompressed](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_background_scrub_data_uncompressed)
* [innodb-blocking-buffer-pool-restore](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_blocking_buffer_pool_restore)
* [innodb-buf-dump-status-frequency](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_buf_dump_status_frequency)
* [innodb-buffer-pool-chunk-size](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_buffer_pool_chunk_size)
* [innodb-buffer-pool-dump-at-shutdown](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_buffer_pool_dump_at_shutdown)
* [innodb-buffer-pool-dump-now](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_buffer_pool_dump_now)
* [innodb-buffer-pool-dump-pct](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_buffer_pool_dump_pct)
* [innodb-buffer-pool-evict](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_buffer_pool_evict)
* [innodb-buffer-pool-filename](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_buffer_pool_filename)
* [innodb-buffer-pool-instances](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_buffer_pool_instances)
* [innodb-buffer-pool-load-abort](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_buffer_pool_load_abort)
* [innodb-buffer-pool-load-at-startup](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_buffer_pool_load_at_startup)
* [innodb-buffer-pool-load-now](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_buffer_pool_load_now)
* [innodb-buffer-pool-load-pages-abort](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_buffer_pool_load_pages_abort)
* [innodb-buffer-pool-populate](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_buffer_pool_populate)
* [innodb-buffer-pool-restore-at-startup](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_buffer_pool_restore_at_startup)
* [innodb-buffer-pool-shm-checksum](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_buffer_pool_shm_checksum)
* [innodb-buffer-pool-shm-key](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_buffer_pool_shm_key)
* [innodb-buffer-pool-size](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_buffer_pool_size)
* [innodb-change-buffer-max-size](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_change_buffer_max_size)
* [innodb-change-buffering](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_change_buffering)
* [innodb-change-buffering-debug](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_change_buffering_debug)
* [innodb-checkpoint-age-target](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_checkpoint_age_target)
* [innodb-checksum-algorithm](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_checksum_algorithm)
* [innodb-checksums](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_checksums)
* [innodb-cleaner-lsn-age-factor](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_cleaner_lsn_age_factor)
* [innodb-cmp-per-index-enabled](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_cmp_per_index_enabled)
* [innodb-commit-concurrency](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_commit_concurrency)
* [innodb-compression-algorithm](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_compression_algorithm)
* [innodb-compression-failure-threshold-pct](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_compression_failure_threshold_pct)
* [innodb-compression-level](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_compression_level)
* [innodb-compression-pad-pct-max](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_compression_pad_pct_max)
* [innodb-concurrency-tickets](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_concurrency_tickets)
* [innodb-corrupt-table-action](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_corrupt_table_action)
* [innodb-data-file-buffering](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_data_file_buffering)
* [innodb-data-file-path](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_data_file_path)
* [innodb-data-file-write-through](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_data_file_write_through)
* [innodb-data-home-dir](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_data_home_dir)
* [innodb-deadlock-detect](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_deadlock_detect)
* [innodb-deadlock-report](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_deadlock_report)
* [innodb-default-encryption-key-id](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_default_encryption_key_id)
* [innodb-default-page-encryption-key](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_default_page_encryption_key)
* [innodb-default-row-format](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_default_row_format)
* [innodb-defragment](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_defragment)
* [innodb-defragment-fill-factor](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_defragment_fill_factor)
* [innodb-defragment-fill-factor-n-recs](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_defragment_fill_factor_n_recs)
* [innodb-defragment-frequency](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_defragment_frequency)
* [innodb-defragment-n-pages](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_defragment_n_pages)
* [innodb-defragment-stats-accuracy](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_defragment_stats_accuracy)
* [innodb-dict-size-limit](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_dict_size_limit)
* [innodb_disable_sort_file_cache](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_disable_sort_file_cache)
* [innodb-doublewrite](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_doublewrite)
* [innodb-doublewrite-file](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_doublewrite_file)
* [innodb-empty-free-list-algorithm](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_empty_free_list_algorithm)
* [innodb-enable-unsafe-group-commit](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_enable_unsafe_group_commit)
* [innodb-encrypt-log](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_encrypt_log)
* [innodb-encrypt-tables](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_encrypt_tables)
* [innodb-encrypt-temporary-tables](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_encrypt_tables)
* [innodb-encryption-rotate-key-age](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_encryption_rotate_key_age)
* [innodb-encryption-rotation_iops](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_encryption_rotation_iops)
* [innodb-encryption-threads](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_encryption_threads)
* [innodb-extra-rsegments](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_extra_rsegments)
* [innodb-extra-undoslots](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_extra_undoslots)
* [innodb-fake-changes](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_fake_changes)
* [innodb-fast-checksum](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_fast_checksum)
* [innodb-fast-shutdown](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_fast_shutdown)
* [innodb-fatal-semaphore-wait-threshold](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_fatal_semaphore_wait_threshold)
* [innodb-file-format](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_file_format)
* [innodb-file-format-check](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_file_format_check)
* [innodb-file-format-max](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_file_format_max)
* [innodb-file-per-table](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_file_per_table)
* [innodb-fill-factor](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_fill_factor)
* [innodb-flush-log-at-trx-commit](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_flush_log_at_trx_commit)
* [innodb-flush-method](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_flush_method)
* [innodb-flush-neighbor-pages](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_flush_neighbor_pages)
* [innodb-flush-neighbors](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_flush_neighbors)
* [innodb-flush-sync](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_flush_sync)
* [innodb-flushing-avg-loops](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_flushing_avg_loops)
* [innodb-force-load-corrupted](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_force_load_corrupted)
* [innodb-force-primary-key](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_force_primary_key)
* [innodb-force-recovery](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_force_recovery)
* [innodb-foreground-preflush](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_foreground_preflush)
* [innodb-ft-aux-table](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_ft_aux_table)
* [innodb-ft-cache-size](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_ft_cache_size)
* [innodb-ft-enable-diag-print](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_ft_enable_diag_print)
* [innodb-ft-enable-stopword](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_ft_enable_stopword)
* [innodb-ft-max-token-size](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_ft_max_token_size)
* [innodb-ft-min-token-size](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_ft_min_token_size)
* [innodb-ft-num-word-optimize](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_ft_num_word_optimize)
* [innodb-ft-result-cache-limit](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_ft_result_cache_limit)
* [innodb-ft-server-stopword-table](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_ft_server_stopword_table)
* [innodb-ft-sort-pll-degree](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_ft_sort_pll_degree)
* [innodb-ft-total-cache-size](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_ft_total_cache_size)
* [innodb-ft-user-stopword-table](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_ft_user_stopword_table)
* [innodb-ibuf-accel-rate](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_ibuf_accel_rate)
* [innodb-ibuf-active-contract](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_ibuf_active_contract)
* [innodb-ibuf-max-size](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_ibuf_max_size)
* [innodb-idle-flush-pct](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_idle_flush_pct)
* [innodb-immediate-scrub-data-uncompressed](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_immediate_scrub_data_uncompressed)
* [innodb-import-table-from-xtrabackup](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_import_table_from_xtrabackup)
* [innodb-instant-alter-column-allowed](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_instant_alter_column_allowed)
* [innodb-instrument-semaphores](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_instrument_semaphores)
* [innodb-io-capacity](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_io_capacity)
* [innodb-io-capacity-max](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_io_capacity_max)
* [innodb-large-prefix](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_large_prefix)
* [innodb-lazy-drop-table](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_lazy_drop_table)
* [innodb-lock-schedule-algorithm](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_lock_schedule_algorithmt)
* [innodb-locking-fake-changes](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_locking_fake_changes)
* [innodb-locks-unsafe-for-binlog](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_locks_unsafe_for_binlog)
* [innodb-log-arch-dir](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_log_arch_dir)
* [innodb-log-arch-expire-sec](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_log_arch_expire_sec)
* [innodb-log-archive](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_log_archive)
* [innodb-log-block-size](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_log_block_size)
* [innodb-log-buffer-size](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_log_buffer_size)
* [innodb-log-checksum-algorithm](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_log_checksum_algorithm)
* [innodb-log-checksums](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_log_checksums)
* [innodb-log-compressed-pages](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_log_compressed_pages)
* [innodb-log-file-buffering](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_log_file_buffering)
* [innodb-log-file-mmap](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_log_file_mmap)
* [innodb-log-file-size](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_log_file_size)
* [innodb-log-file-write-through](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_log_file_write_through)
* [innodb-log-files-in-group](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_log_files_in_group)
* [innodb-log-group-home-dir](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_log_group_home_dir)
* [innodb-log-optimize-ddl](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_log_optimize_ddl)
* [innodb-log-spin-wait-delay](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb-log_spin_wait_delay)
* [innodb-log-write-ahead-size](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_log_write_ahead_size)
* [innodb-lru-flush-size](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_lru_flush_size)
* [innodb-lru-scan-depth](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_lru_scan_depth)
* [innodb-max-bitmap-file-size](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_max_bitmap_file_size)
* [innodb-max-changed-pages](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_max_changed_pages)
* [innodb-max-dirty-pages-pct](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_max_dirty_pages_pct)
* [innodb-max-dirty-pages-pct-lwm](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_max_dirty_pages_pct_lwm)
* [innodb-max-purge-lag](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_max_purge_lag)
* [innodb-max-purge-lag-delay](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_max_purge_lag_delay)
* [innodb-max-purge-lag-wait](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_max_purge_lag_wait)
* [innodb-max-undo-log-size](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_max_undo_log_size)
* [innodb-merge-sort-block-size](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_merge_sort_block_size)
* [innodb-mirrored-log-groups](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_mirrored_log_groups)
* [innodb-monitor-disable](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_monitor_disable)
* [innodb-monitor-enable](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_monitor_enable)
* [innodb-monitor-reset](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_monitor_reset)
* [innodb-monitor-reset-all](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_monitor_reset_all)
* [innodb-mtflush-threads](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_mtflush_threads)
* [innodb-numa-interleave](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_numa_interleave)
* [innodb-old-blocks-pct](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_old_blocks_pct)
* [innodb-old-blocks-time](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_old_blocks_time)
* [innodb-online-alter-log-max-size](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_online_alter_log_max_size)
* [innodb-open-files](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_open_files)
* [innodb-optimize-fulltext-only](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_optimize_fulltext_only)
* [innodb-page-cleaners](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_page_cleaners)
* [innodb-page-size](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_page_size)
* [innodb-pass-corrupt-table](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_pass_corrupt_table)
* [innodb-prefix-index-cluster-optimization](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_prefix_index_cluster_optimization)
* [innodb-print-all-deadlocks](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_print_all_deadlocks)
* [innodb-purge-batch-size](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_purge_batch_size)
* [innodb-purge-rseg-truncate-frequency](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_purge_rseg_truncate_frequency)
* [innodb-purge-threads](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_purge_threads)
* [innodb-random-read-ahead](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_random_read_ahead)
* [innodb-read-ahead](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_read_ahead)
* [innodb-read-ahead-threshold](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_read_ahead_threshold)
* [innodb-read-io-threads](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_read_io_threads)
* [innodb-read-only](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_read_only)
* [innodb-recovery-update-relay-log](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_recovery_update_relay_log)
* [innodb-replication-delay](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_replication_delay)
* [innodb-rollback-on-timeout](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_rollback_on_timeout)
* [innodb-rollback-segments](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_rollback_segments)
* [innodb-safe-truncate](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_safe_truncate)
* [innodb-sched-priority-cleaner](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_sched_priority_cleaner)
* [innodb-scrub-log](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_scrub_log)
* [innodb-scrub-log-interval](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_scrub_log_interval)
* [innodb-scrub-log-speed](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_scrub_log_speed)
* [innodb-show-locks-held](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_show_locks_held)
* [innodb-show-verbose-locks](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_show_verbose_locks)
* [innodb-snapshot-isolation](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_snapshot_isolation)
* [innodb-sort-buffer-size](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_sort_buffer_size)
* [innodb-spin-wait-delay](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_spin_wait_delay)
* [innodb-stats-auto-recalc](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_stats_auto_recalc)
* [innodb-stats-auto-update](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_stats_auto_update)
* [innodb-stats-include-delete-marked](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_stats_include_delete_marked)
* [innodb-stats-method](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_stats_method)
* [innodb-stats-modified-counter](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_stats_modified_counter)
* [innodb-stats-on-metadata](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_stats_on_metadata)
* [innodb-stats-persistent](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_stats_persistent)
* [innodb-stats-persistent-sample-pages](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_stats_persistent_sample_pages)
* [innodb-stats-sample-pages](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_stats_sample_pages)
* [innodb-stats-transient-sample-pages](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_stats_transient_sample_pages)
* [innodb-stats-traditional](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_stats_traditional)
* [innodb-stats-update-need-lock](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_stats_update_need_lock)
* [innodb-status-output](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_status_output)
* [innodb-status-output-locks](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_status_output_locks)
* [innodb-strict-mode](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_strict_mode)
* [innodb-support-xa](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_support_xa)
* [innodb-sync-array-size](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_sync_array_size)
* [innodb-sync-spin-loops](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_sync_spin_loops)
* [innodb-table-locks](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_table_locks)
* [innodb-temp-data-file-path](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_temp_data_file_path)
* [innodb-thread-concurrency](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_thread_concurrency)
* [innodb-thread-concurrency-timer-based](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_thread_concurrency_timer_based)
* [innodb-thread-sleep-delay](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_thread_sleep_delay)
* [innodb-tmpdir](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_tmpdir)
* [innodb-track-changed-pages](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_track_changed_pages)
* [innodb-track-redo-log-now](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_track_redo_log_now)
* [innodb-truncate-temporary-tablespace-now](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_truncate_temporary_tablespace_now)
* [innodb-undo-directory](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_undo_directory)
* [innodb-undo-log-truncate](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_undo_log_truncate)
* [innodb-undo-logs](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_undo_logs)
* [innodb-undo-tablespaces](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_undo_tablespaces)
* [innodb-use-atomic-writes](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_use_atomic_writes)
* [innodb-use-fallocate](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_use_fallocate)
* [innodb-use-global-flush-log-at-trx-commit](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_use_global_flush_log_at_trx_commit)
* [innodb-use-mtflush](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_use_mtflush)
* [innodb-use-native_aio](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_use_native_aio)
* [innodb-use-purge-thread](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_use_purge_thread)
* [innodb-use-stacktrace](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_use_stacktrace)
* [innodb-use-sys-malloc](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_use_sys_malloc)
* [innodb-use-sys-stats-table](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_use_sys_stats_table)
* [innodb-use-trim](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_use_trim)
* [innodb-write-io-threads](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_write_io_threads)
* [skip-innodb](#-innodb)
* [skip-innodb-checksums](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_checksums)
* [skip-innodb-doublewrite](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_doublewrite)


### Aria Storage Engine Options


Options related to the [Aria](../../../reference/storage-engines/s3-storage-engine/aria_s3_copy.md) storage engine are listed below:


#### Aria Storage Engine Options and System Variables


Some options and system variables related to the [Aria](../../../reference/storage-engines/s3-storage-engine/aria_s3_copy.md) storage engine can be found [here](../../../reference/storage-engines/aria/aria-system-variables.md). Direct links to many of them can be found below.


* [aria-block-size](../../../reference/storage-engines/aria/aria-system-variables.md#aria_block_size)
* [aria-checkpoint-interval](../../../reference/storage-engines/aria/aria-system-variables.md#aria_checkpoint_interval)
* [aria-checkpoint-log-activity](../../../reference/storage-engines/aria/aria-system-variables.md#aria_checkpoint_log_activity)
* [aria-encrypt-tables](../../../reference/storage-engines/aria/aria-system-variables.md#aria_encrypt_tables)
* [aria-force-start-after-recovery-failures](../../../reference/storage-engines/aria/aria-system-variables.md#aria_force_start_after_recovery_failures)
* [aria-group-commit](../../../reference/storage-engines/aria/aria-system-variables.md#aria_group_commit)
* [aria-group-commit-interval](../../../reference/storage-engines/aria/aria-system-variables.md#aria_group_commit_interval)
* [aria-log-dir-path](../../../reference/storage-engines/aria/aria-system-variables.md#aria_log_dir_path)
* [aria-log-file-size](../../../reference/storage-engines/aria/aria-system-variables.md#aria_log_file_size)
* [aria-log-purge-type](../../../reference/storage-engines/aria/aria-system-variables.md#aria_log_purge_type)
* [aria-max-sort-file-size](../../../reference/storage-engines/aria/aria-system-variables.md#aria_max_sort_file_size)
* [aria-page-checksum](../../../reference/storage-engines/aria/aria-system-variables.md#aria_page_checksum)
* [aria-pagecache-age-threshold](../../../reference/storage-engines/aria/aria-system-variables.md#aria_pagecache_age_threshold)
* [aria-pagecache-buffer-size](../../../reference/storage-engines/aria/aria-system-variables.md#aria_pagecache_buffer_size)
* [aria-pagecache-division-limit](../../../reference/storage-engines/aria/aria-system-variables.md#aria_pagecache_division_limit)
* [aria-pagecache-file-hash-size](../../../reference/storage-engines/aria/aria-system-variables.md#aria_pagecache_file_hash_size)
* [aria-recover](../../../reference/storage-engines/aria/aria-system-variables.md#aria_recover)
* [aria-recover-options](../../../reference/storage-engines/aria/aria-system-variables.md#aria_recover_options)
* [aria-repair-threads](../../../reference/storage-engines/aria/aria-system-variables.md#aria_repair_threads)
* [aria-sort-buffer-size](../../../reference/storage-engines/aria/aria-system-variables.md#aria_sort_buffer_size)
* [aria-stats-method](../../../reference/storage-engines/aria/aria-system-variables.md#aria_stats_method)
* [aria-sync-log-dir](../../../reference/storage-engines/aria/aria-system-variables.md#aria_sync_log_dir)
* [aria-used-for-temp-tables](../../../reference/storage-engines/aria/aria-system-variables.md#aria_used_for_temp_tables)
* [deadlock-search-depth-long](../../../reference/storage-engines/aria/aria-system-variables.md#deadlock_search_depth_long)
* [deadlock-search-depth-short](../../../reference/storage-engines/aria/aria-system-variables.md#deadlock_search_depth_short)
* [deadlock-timeout-long](../../../reference/storage-engines/aria/aria-system-variables.md#deadlock_timeout_long)
* [deadlock-timeout-short](../../../reference/storage-engines/aria/aria-system-variables.md#deadlock_timeout_short)


### MyRocks Storage Engine Options


The options and system variables related to the [MyRocks](../../../reference/storage-engines/myrocks/myrocks-in-mariadb-102-vs-mariadb-103.md) storage engine can be found [here](../../../reference/storage-engines/myrocks/myrocks-system-variables.md).


### S3 Storage Engine Options


The options and system variables related to the [S3](../../../reference/storage-engines/s3-storage-engine/s3-storage-engine-status-variables.md) storage engine can be found [here](../../../reference/storage-engines/s3-storage-engine/s3-storage-engine-system-variables.md).


### CONNECT Storage Engine Options


The options related to the [CONNECT](../../../../connectors/mariadb-connector-nodejs/connector-nodejs-pipelining.md) storage engine are described below.


#### CONNECT Storage Engine Options and System Variables


Some options and system variables related to the [CONNECT](../../../../connectors/mariadb-connector-nodejs/connector-nodejs-pipelining.md) storage engine can be found [here](../../../reference/storage-engines/connect/connect-system-variables.md). Direct links to many of them can be found below.


* [connect-class-path](../../../reference/storage-engines/connect/connect-system-variables.md#connect_class_path)
* [connect-cond-push](../../../reference/storage-engines/connect/connect-system-variables.md#connect_cond_push)
* [connect-conv-size](../../../reference/storage-engines/connect/connect-system-variables.md#connect_conv_size)
* [connect-default-depth](../../../reference/storage-engines/connect/connect-system-variables.md#connect_default_depth)
* [connect-default-prec](../../../reference/storage-engines/connect/connect-system-variables.md#connect_default_prec)
* [connect-enable-mongo](../../../reference/storage-engines/connect/connect-system-variables.md#connect_enable_mongo)
* [connect-exact-info](../../../reference/storage-engines/connect/connect-system-variables.md#connect_exact_info)
* [connect-force_bson](../../../reference/storage-engines/connect/connect-system-variables.md#connect_force_bson)
* [connect-indx-map](../../../reference/storage-engines/connect/connect-system-variables.md#connect_indx_map)
* [connect-java-wrapper](../../../reference/storage-engines/connect/connect-system-variables.md#connect_java_wrapper)
* [connect-json-all-path](../../../reference/storage-engines/connect/connect-system-variables.md#connect_json_all_path)
* [connect-json-grp-size](../../../reference/storage-engines/connect/connect-system-variables.md#connect_json_grp_size)
* [connect-json-null](../../../reference/storage-engines/connect/connect-system-variables.md#connect_json_null)
* [connect-jvm-path](../../../reference/storage-engines/connect/connect-system-variables.md#connect_jvm_path)
* [connect-type-conv](../../../reference/storage-engines/connect/connect-system-variables.md#connect_type_conv)
* [connect-use-tempfile](../../../reference/storage-engines/connect/connect-system-variables.md#connect_use_tempfile)
* [connect-work-size](../../../reference/storage-engines/connect/connect-system-variables.md#connect_work_size)
* [connect-xtrace](../../../reference/storage-engines/connect/connect-system-variables.md#connect_xtrace)


### Spider Storage Engine Options


The options and system variables related to the [Spider](../../../reference/storage-engines/spider/spider-functions/spider_copy_tables.md) storage engine can be found [here](../../../reference/storage-engines/spider/spider-system-variables.md).


### Mroonga Storage Engine Options


The options and system variables related to the [Mroonga](../../../reference/storage-engines/mroonga/mroonga-user-defined-functions/mroonga_snippet_html.md) storage engine can be found [here](../../../reference/storage-engines/mroonga/mroonga-system-variables.md).


### TokuDB Storage Engine Options


The options and system variables related to the [TokuDB](../../../reference/storage-engines/tokudb/tokudb-resources.md) storage engine can be found [here](../../../reference/storage-engines/tokudb/tokudb-system-variables.md).


### Vector Options


The options and system variables related to [Vectors](../../../reference/sql-statements-and-structure/vectors/README.md) storage engine (beginning with `<code>mhnsw</code>`) can be found [here](../../../reference/sql-statements-and-structure/vectors/vector-system-variables.md).


## Performance Schema Options


The options related to the [Performance Schema](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/performance-schema/performance-schema-tables/performance-schema-table_handles-table.md) are described below. Options that are also system variables are listed after:





#### `<code>--performance-schema-consumer-events-stages-current</code>`


* Commandline: `<code class="fixed" style="white-space:pre-wrap">--performance-schema-consumer-events-stages-current</code>`
* Description: Enable the [events-stages-current](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/performance-schema/performance-schema-tables/performance-schema-events_stages_current-table.md) consumer.
* Default: `<code>OFF</code>`



#### `<code>--performance-schema-consumer-events-stages-history</code>`


* Commandline: `<code class="fixed" style="white-space:pre-wrap">--performance-schema-consumer-events-stages-history</code>`
* Description: Enable the [events-stages-history](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/performance-schema/performance-schema-tables/performance-schema-events_stages_history-table.md) consumer.
* Default: `<code>OFF</code>`



#### `<code>--performance-schema-consumer-events-stages-history-long</code>`


* Commandline: `<code class="fixed" style="white-space:pre-wrap">--performance-schema-consumer-events-stages-history-long</code>`
* Description: Enable the [events-stages-history-long](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/performance-schema/performance-schema-tables/performance-schema-events_stages_history_long-table.md) consumer.
* Default: `<code>OFF</code>`



#### `<code>--performance-schema-consumer-events-statements-current</code>`


* Commandline: `<code class="fixed" style="white-space:pre-wrap">--performance-schema-consumer-events-statements-current</code>`
* Description: Enable the [events-statements-current](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/performance-schema/performance-schema-tables/performance-schema-events_statements_current-table.md) consumer. Use `<code>--skip-performance-schema-consumer-events-statements-current</code>` to disable.
* Default: `<code>ON</code>`



#### `<code>--performance-schema-consumer-events-statements-history</code>`


* Commandline: `<code class="fixed" style="white-space:pre-wrap">--performance-schema-consumer-events-statements-history</code>`
* Description: Enable the [events-statements-history](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/performance-schema/performance-schema-tables/performance-schema-events_statements_history-table.md) consumer.
* Default: `<code>OFF</code>`



#### `<code>--performance-schema-consumer-events-statements-history-long</code>`


* Commandline: `<code class="fixed" style="white-space:pre-wrap">--performance-schema-consumer-events-statements-history-long</code>`
* Description: Enable the [events-statements-history-long](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/performance-schema/performance-schema-tables/performance-schema-events_statements_history_long-table.md) consumer.
* Default: `<code>OFF</code>`



#### `<code>--performance-schema-consumer-events-waits-current</code>`


* Commandline: `<code class="fixed" style="white-space:pre-wrap">--performance-schema-consumer-events-waits-current</code>`
* Description: Enable the [events-waits-current](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/performance-schema/performance-schema-tables/performance-schema-events_waits_current-table.md) consumer.
* Default: `<code>OFF</code>`



#### `<code>--performance-schema-consumer-events-waits-history</code>`


* Commandline: `<code class="fixed" style="white-space:pre-wrap">--performance-schema-consumer-events-waits-history</code>`
* Description: Enable the [events-waits-history](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/performance-schema/performance-schema-tables/performance-schema-events_waits_history-table.md) consumer.
* Default: `<code>OFF</code>`



#### `<code>--performance-schema-consumer-events-waits-history-long</code>`


* Commandline: `<code class="fixed" style="white-space:pre-wrap">--performance-schema-consumer-events-waits-history-long</code>`
* Description: Enable the [events-waits-history-long](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/performance-schema/performance-schema-tables/performance-schema-events_waits_history_long-table.md) consumer.
* Default: `<code>OFF</code>`



#### `<code>--performance-schema-consumer-global-instrumentation</code>`


* Commandline: `<code class="fixed" style="white-space:pre-wrap">--performance-schema-consumer-global-instrumentation</code>`
* Description: Enable the global-instrumentation consumer. Use `<code>--skip-performance-schema-consumer-global-instrumentation</code>` to disable.
* Default: `<code>ON</code>`



#### `<code>--performance-schema-consumer-statements-digest</code>`


* Commandline: `<code class="fixed" style="white-space:pre-wrap">--performance-schema-consumer-statements-digest</code>`
* Description: Enable the statements-digest consumer. Use `<code>--skip-performance-schema-consumer-statements-digest</code>` to disable.
* Default: `<code>ON</code>`



#### `<code>--performance-schema-consumer-thread-instrumentation</code>`


* Commandline: `<code class="fixed" style="white-space:pre-wrap">--performance-schema-consumer-thread-instrumentation</code>`
* Description: Enable the statements-thread-instrumentation. Use `<code>--skip-performance-schema-thread-instrumentation</code>` to disable.
* Default: `<code>ON</code>`























### Performance Schema Options and System Variables


Some options and system variables related to the [Performance Schema](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/performance-schema/performance-schema-tables/performance-schema-table_handles-table.md) can be found [here](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/performance-schema/performance-schema-system-variables.md). Direct links to many of them can be found below.


* [performance-schema](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/performance-schema/performance-schema-system-variables.md#performance_schema)
* [performance-schema-accounts-size](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/performance-schema/performance-schema-system-variables.md#performance_schema_accounts_size)
* [performance-schema-digests-size](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/performance-schema/performance-schema-system-variables.md#performance_schema_digests_size)
* [performance-schema-events-stages-history-long-size](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/performance-schema/performance-schema-system-variables.md#performance_schema_events_stages_history_long_size)
* [performance-schema-events-stages-history-size](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/performance-schema/performance-schema-system-variables.md#performance_schema_events_stages_history_size)
* [performance-schema-events-statements-history-long-size](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/performance-schema/performance-schema-system-variables.md#performance_schema_events_statements_history_long_size)
* [performance-schema-events-statements-history-size](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/performance-schema/performance-schema-system-variables.md#performance_schema_events_statements_history_size)
* [performance-schema-events-waits-history-long-size](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/performance-schema/performance-schema-system-variables.md#performance_schema_events_waits_history_long_size)
* [performance-schema-events-waits-history-size](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/performance-schema/performance-schema-system-variables.md#performance_schema_events_waits_history_size)
* [performance-schema-hosts-size](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/performance-schema/performance-schema-system-variables.md#performance_schema_hosts_size)
* [performance-schema-max-cond-classes](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/performance-schema/performance-schema-system-variables.md#performance_schema_max_cond_classes)
* [performance-schema-max-cond-instances](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/performance-schema/performance-schema-system-variables.md#performance_schema_max_cond_instances)
* [performance-schema-max-digest-length](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/performance-schema/performance-schema-system-variables.md#performance_schema_max_digest_length)
* [performance-schema-max-file-classes](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/performance-schema/performance-schema-system-variables.md#performance_schema_max_file_classes)
* [performance-schema-max-file-handles](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/performance-schema/performance-schema-system-variables.md#performance_schema_max_file_handles)
* [performance-schema-max-file-instances](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/performance-schema/performance-schema-system-variables.md#performance_schema_max_file_instances)
* [performance-schema-max-mutex-classes](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/performance-schema/performance-schema-system-variables.md#performance_schema_max_mutex_classes)
* [performance-schema-max-mutex-instances](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/performance-schema/performance-schema-system-variables.md#performance_schema_max_mutex_instances)
* [performance-schema-max-rwlock-classes](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/performance-schema/performance-schema-system-variables.md#performance_schema_max_rwlock_classes)
* [performance-schema-max-rwlock-instances](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/performance-schema/performance-schema-system-variables.md#performance_schema_max_rwlock_instances)
* [performance-schema-max-socket-classes](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/performance-schema/performance-schema-system-variables.md#performance_schema_max_socket_classes)
* [performance-schema-max-socket-instances](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/performance-schema/performance-schema-system-variables.md#performance_schema_max_socket_instances)
* [performance-schema-max-stage-classes](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/performance-schema/performance-schema-system-variables.md#performance_schema_max_stage_classes)
* [performance-schema-max-statement-classes](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/performance-schema/performance-schema-system-variables.md#performance_schema_max_statement_classes)
* [performance-schema-max-table-handles](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/performance-schema/performance-schema-system-variables.md#performance_schema_max_table_handles)
* [performance-schema-max-table-instances](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/performance-schema/performance-schema-system-variables.md#performance_schema_max_table_instances)
* [performance-schema-max-thread-classes](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/performance-schema/performance-schema-system-variables.md#performance_schema_max_thread_classes)
* [performance-schema-max-thread-instances](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/performance-schema/performance-schema-system-variables.md#performance_schema_max_thread_instances)
* [performance-schema-session-connect-attrs-size](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/performance-schema/performance-schema-system-variables.md#performance_schema_session_connect_attrs_size)
* [performance-schema-setup-actors-size](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/performance-schema/performance-schema-system-variables.md#performance_schema_setup_actors_size)
* [performance-schema-setup-objects-size](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/performance-schema/performance-schema-system-variables.md#performance_schema_setup_objects_size)
* [performance-schema-users-size](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/performance-schema/performance-schema-system-variables.md#performance_schema_users_size)


## Galera Cluster Options


The options related to [Galera Cluster](../../../reference/sql-statements-and-structure/sql-statements/built-in-functions/special-functions/galera-functions/README.md) are described below. Options that are also system variables are listed after:


#### `<code>--wsrep-new-cluster</code>`


* Commandline: `<code class="fixed" style="white-space:pre-wrap">--wsrep-new-cluster</code>`
* Description: Bootstrap a cluster. It works by overriding the current value of wsrep_cluster_address. It is recommended not to add this option to the config file as this will trigger bootstrap on every server start.



### Galera Cluster Options and System Variables


Some options and system variables related to [Galera Cluster](../../../reference/sql-statements-and-structure/sql-statements/built-in-functions/special-functions/galera-functions/README.md) can be found [here](../../../server-usage/replication-cluster-multi-master/galera-cluster/galera-cluster-system-variables.md). Direct links to many of them can be found below.


* [wsrep-allowlist](../../../server-usage/replication-cluster-multi-master/galera-cluster/galera-cluster-system-variables.md#wsrep_allowlist)
* [wsrep-auto-increment-control](../../../server-usage/replication-cluster-multi-master/galera-cluster/galera-cluster-system-variables.md#wsrep_auto_increment_control)
* [wsrep-causal-reads](../../../server-usage/replication-cluster-multi-master/galera-cluster/galera-cluster-system-variables.md#wsrep_causal_reads)
* [wsrep-certify-nonPK](../../../server-usage/replication-cluster-multi-master/galera-cluster/galera-cluster-system-variables.md#wsrep_certify_nonpk)
* [wsrep-cluster-address](../../../server-usage/replication-cluster-multi-master/galera-cluster/galera-cluster-system-variables.md#wsrep_cluster_address)
* [wsrep-cluster-name](../../../server-usage/replication-cluster-multi-master/galera-cluster/galera-cluster-system-variables.md#wsrep_cluster_name)
* [wsrep-convert-LOCK-to-trx](../../../server-usage/replication-cluster-multi-master/galera-cluster/galera-cluster-system-variables.md#wsrep_convert_lock_to_trx)
* [wsrep-data-home-dir](../../../server-usage/replication-cluster-multi-master/galera-cluster/galera-cluster-system-variables.md#wsrep_data_home_dir)
* [wsrep-dbug-option](../../../server-usage/replication-cluster-multi-master/galera-cluster/galera-cluster-system-variables.md#wsrep_dbug_option)
* [wsrep-debug](../../../server-usage/replication-cluster-multi-master/galera-cluster/galera-cluster-system-variables.md#wsrep_debug)
* [wsrep-desync](../../../server-usage/replication-cluster-multi-master/galera-cluster/galera-cluster-system-variables.md#wsrep_desync)
* [wsrep-dirty-reads](../../../server-usage/replication-cluster-multi-master/galera-cluster/galera-cluster-system-variables.md#wsrep_dirty_reads)
* [wsrep-drupal-282555-workaround](../../../server-usage/replication-cluster-multi-master/galera-cluster/galera-cluster-system-variables.md#wsrep_drupal_282555_workaround)
* [wsrep-forced-binlog-format](../../../server-usage/replication-cluster-multi-master/galera-cluster/galera-cluster-system-variables.md#wsrep_forced_binlog_format)
* [wsrep-gtid-domain-id](../../../server-usage/replication-cluster-multi-master/galera-cluster/galera-cluster-system-variables.md#wsrep_gtid_domain_id)
* [wsrep-gtid-mode](../../../server-usage/replication-cluster-multi-master/galera-cluster/galera-cluster-system-variables.md#wsrep_gtid_mode)
* [wsrep-ignore-apply-errors](../../../server-usage/replication-cluster-multi-master/galera-cluster/galera-cluster-system-variables.md#wsrep_ignore_apply_errors)
* [wsrep-load-data-splitting](../../../server-usage/replication-cluster-multi-master/galera-cluster/galera-cluster-system-variables.md#wsrep_load_data_splitting)
* [wsrep-log-conflicts](../../../server-usage/replication-cluster-multi-master/galera-cluster/galera-cluster-system-variables.md#wsrep_log_conflicts)
* [wsrep-max-ws-rows](../../../server-usage/replication-cluster-multi-master/galera-cluster/galera-cluster-system-variables.md#wsrep_max_ws_rows)
* [wsrep-max-ws-size](../../../server-usage/replication-cluster-multi-master/galera-cluster/galera-cluster-system-variables.md#wsrep_max_ws_size)
* [wsrep-mode](../../../server-usage/replication-cluster-multi-master/galera-cluster/galera-cluster-system-variables.md#wsrep_mode)
* [wsrep-mysql-replication-bundle](../../../server-usage/replication-cluster-multi-master/galera-cluster/galera-cluster-system-variables.md#wsrep_mysql_replication_bundle)
* [wsrep-node-address](../../../server-usage/replication-cluster-multi-master/galera-cluster/galera-cluster-system-variables.md#wsrep_node_address)
* [wsrep-node-incoming-address](../../../server-usage/replication-cluster-multi-master/galera-cluster/galera-cluster-system-variables.md#wsrep_node_incoming_address)
* [wsrep-node-name](../../../server-usage/replication-cluster-multi-master/galera-cluster/galera-cluster-system-variables.md#wsrep_node_name)
* [wsrep-notify-cmd](../../../server-usage/replication-cluster-multi-master/galera-cluster/galera-cluster-system-variables.md#wsrep_notify_cmd)
* [wsrep-on](../../../server-usage/replication-cluster-multi-master/galera-cluster/galera-cluster-system-variables.md#wsrep_on)
* [wsrep-OSU-method](../../../server-usage/replication-cluster-multi-master/galera-cluster/galera-cluster-system-variables.md#wsrep_osu_method)
* [wsrep-provider](../../../server-usage/replication-cluster-multi-master/galera-cluster/galera-cluster-system-variables.md#wsrep_provider)
* [wsrep-provider-options](../../../server-usage/replication-cluster-multi-master/galera-cluster/galera-cluster-system-variables.md#wsrep_provider_options)
* [wsrep-recover](../../../server-usage/replication-cluster-multi-master/galera-cluster/galera-cluster-system-variables.md#wsrep_recover)
* [wsrep-reject_queries](../../../server-usage/replication-cluster-multi-master/galera-cluster/galera-cluster-system-variables.md#wsrep_reject_queries)
* [wsrep-retry-autocommit](../../../server-usage/replication-cluster-multi-master/galera-cluster/galera-cluster-system-variables.md#wsrep_retry_autocommit)
* [wsrep-slave-FK-checks](../../../server-usage/replication-cluster-multi-master/galera-cluster/galera-cluster-system-variables.md#wsrep_slave_fk_checks)
* [wsrep-slave-threads](../../../server-usage/replication-cluster-multi-master/galera-cluster/galera-cluster-system-variables.md#wsrep_slave_threads)
* [wsrep-slave-UK-checks](../../../server-usage/replication-cluster-multi-master/galera-cluster/galera-cluster-system-variables.md#wsrep_slave_uk_checks)
* [wsrep-sr-store](../../../server-usage/replication-cluster-multi-master/galera-cluster/galera-cluster-system-variables.md#wsrep_sr_store)
* [wsrep-sst-auth](../../../server-usage/replication-cluster-multi-master/galera-cluster/galera-cluster-system-variables.md#wsrep_sst_auth)
* [wsrep-sst-donor](../../../server-usage/replication-cluster-multi-master/galera-cluster/galera-cluster-system-variables.md#wsrep_sst_donor)
* [wsrep-sst-donor-rejects-queries](../../../server-usage/replication-cluster-multi-master/galera-cluster/galera-cluster-system-variables.md#wsrep_sst_donor_rejects_queries)
* [wsrep-sst-method](../../../server-usage/replication-cluster-multi-master/galera-cluster/galera-cluster-system-variables.md#wsrep_sst_method)
* [wsrep-sst-receive-address](../../../server-usage/replication-cluster-multi-master/galera-cluster/galera-cluster-system-variables.md#wsrep_sst_receive_address)
* [wsrep-start-position](../../../server-usage/replication-cluster-multi-master/galera-cluster/galera-cluster-system-variables.md#wsrep_start_position)
* [wsrep-status-file](../../../server-usage/replication-cluster-multi-master/galera-cluster/galera-cluster-system-variables.md#wsrep_status_file)
* [wsrep-strict-ddl](../../../server-usage/replication-cluster-multi-master/galera-cluster/galera-cluster-system-variables.md#wsrep_strict_ddl)
* [wsrep-sync-wait](../../../server-usage/replication-cluster-multi-master/galera-cluster/galera-cluster-system-variables.md#wsrep_sync_wait)
* [wsrep-trx_fragment_size](../../../server-usage/replication-cluster-multi-master/galera-cluster/galera-cluster-system-variables.md#wsrep_trx_fragment_size)
* [wsrep-trx_fragment_unit](../../../server-usage/replication-cluster-multi-master/galera-cluster/galera-cluster-system-variables.md#wsrep_trx_fragment_unit)


## Options When Debugging mariadbd


#### `<code>--debug-assert-if-crashed-table</code>`


* Description: Do an assert in handler::print_error() if we get a crashed table.



#### `<code>--debug-binlog-fsync-sleep</code>`


* Description: `<code class="fixed" style="white-space:pre-wrap">--debug-binlog-fsync-sleep=#</code>`If not set to zero, sets the number of micro-seconds to sleep after running fsync() on the [binary log](../../../reference/storage-engines/innodb/binary-log-group-commit-and-innodb-flushing-performance.md) to flush transactions to disk. This can thus be used to artificially increase the perceived cost of such an fsync().



#### `<code>--debug-crc-break</code>`


* Description: `<code class="fixed" style="white-space:pre-wrap">--debug-crc-break=#</code>`Call my_debug_put_break_here() if crc matches this number (for debug).



#### `<code>--debug-flush</code>`


* Description: Default debug log with flush after write.



#### `<code>--debug-no-sync</code>`


* Description: `<code class="fixed" style="white-space:pre-wrap">debug-no-sync[=#]</code>`Disables system sync calls. Only for running tests or debugging!



#### `<code>--debug-sync-timeout</code>`


* Description: `<code class="fixed" style="white-space:pre-wrap">debug-sync-timeout[=#]</code>`Enable the debug sync facility and optionally specify a default wait timeout in seconds. A zero value keeps the facility disabled.



#### `<code>--gdb</code>`


* Description: Set up signals usable for debugging.



#### `<code>--silent-startup</code>`


* Description: Don't print Notes to the [error log](../../server-monitoring-logs/error-log.md) during startup.



#### `<code>--sync-sys</code>`


* Description: Enable/disable system sync calls. Syncs should only be turned off (`<code class="fixed" style="white-space:pre-wrap">--disable-sync-sys</code>`) when running tests or debugging! Replaced by [debug-no-sync](#-debug-no-sync) from [MariaDB 5.5](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5.md).
* Removed: [MariaDB 5.5](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5.md)



#### `<code>--thread-alarm</code>`


* Description: Enable/disable system thread alarm calls. Should only be turned off (`<code class="fixed" style="white-space:pre-wrap">--disable-thread-alarm</code>`) when running tests or debugging!



### Debugging Options and System Variables


* [core-file](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#core_file)
* [debug](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#debug)
* [debug-no-thread-alarm](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#debug_no_thread_alarm)


## Other Options


Options that are also system variables are listed after:


#### `<code>--allow-suspicious-udfs</code>`


* Commandline: `<code class="fixed" style="white-space:pre-wrap">--allow-suspicious-udfs</code>`
* Description: Allows use of [user-defined functions](../../../server-usage/programming-customizing-mariadb/user-defined-functions/user-defined-functions-security.md) consisting of only one symbol `<code>x()</code>` without corresponding `<code>x_init()</code>` or `<code>x_deinit()</code>`. That also means that one can load any function from any library, for example `<code>exit()</code>` from `<code>libc.so</code>`. Not recommended unless you require old UDFs with one symbol that cannot be recompiled. From [MariaDB 10.10](../../../../release-notes/mariadb-community-server/what-is-mariadb-1010.md), available as a [system variable](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#allow_suspicious_udfs) as well.



#### `<code>--bootstrap</code>`


* Commandline: `<code class="fixed" style="white-space:pre-wrap">--bootstrap</code>`
* Description: Used by mariadb installation scripts, such as [mariadb-install-db](../mariadb-install-db-exe.md) to execute SQL scripts before any privilege or system tables exist. Do no use while an existing MariaDB instance is running.



#### `<code>--chroot</code>`


* Commandline: `<code class="fixed" style="white-space:pre-wrap">--chroot=name</code>`
* Description: Chroot mariadbd daemon during startup.



#### `<code>--des-key-file</code>`


* Commandline: `<code class="fixed" style="white-space:pre-wrap">--des-key-file=name</code>`
* Description: Load keys for [des_encrypt()](../../../reference/sql-statements-and-structure/sql-statements/built-in-functions/secondary-functions/encryption-hashing-and-compression-functions/des_encrypt.md) and des_encrypt from given file.



#### `<code>--exit-info</code>`


* Commandline: `<code class="fixed" style="white-space:pre-wrap">--exit-info[=#]</code>`
* Description: Used for debugging. Use at your own risk.



#### `<code>--getopt-prefix-matching</code>`


* Commandline: `<code class="fixed" style="white-space:pre-wrap">--getopt-prefix-matching={0|1}</code>`
* Description: Makes it possible to disable historical "unambiguous prefix" matching in the command-line option parsing.
* Default: TRUE
* Introduced: [MariaDB 10.1.3](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-3-release-notes.md)



#### `<code>--help</code>`


* Commandline: `<code class="fixed" style="white-space:pre-wrap">--help</code>`
* Description: Displays help with many commandline options described, and exits. From [MariaDB 11.5](../../../../release-notes/mariadb-community-server/what-is-mariadb-115.md), includes deprecation information.



#### `<code>--log-ddl-recovery</code>`


* Commandline: `<code class="fixed" style="white-space:pre-wrap">--log-ddl-recovery=name</code>`
* Description: Path to file used for recovery of DDL statements after a crash.
* Default Value: `<code>ddl-recover.log</code>`
* Introduced: [MariaDB 10.6.1](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-1061-release-notes.md)


#### `<code>--log-short-format</code>`


* Commandline: `<code class="fixed" style="white-space:pre-wrap">--log-short-format</code>`
* Description: Don't log extra information to update and [slow-query](../../server-monitoring-logs/slow-query-log/slow-query-log-overview.md) logs.



#### `<code>--log-slow-file</code>`


* Commandline: `<code class="fixed" style="white-space:pre-wrap">--log-slow-file=name</code>`
* Description: Log [slow queries](../../server-monitoring-logs/slow-query-log/slow-query-log-overview.md) to given log file. Defaults logging to hostname-slow.log



#### `<code>--log-slow-time</code>`


* Commandline: `<code class="fixed" style="white-space:pre-wrap">--log-slow-time=#</code>`
* Description: Log all queries that have taken more than [long-query-time](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#long_query_time) seconds to execute to the slow query log, if active. The argument will be treated as a decimal value with microsecond precision.



#### `<code>--log-tc</code>`


* Commandline: `<code class="fixed" style="white-space:pre-wrap">--log-tc=name</code>`
* Description: Defines the path to the memory-mapped file-based transaction coordinator log, which is only used if the [binary log](../../../reference/storage-engines/innodb/binary-log-group-commit-and-innodb-flushing-performance.md) is disabled. If you have two or more XA-capable storage engines enabled, then a transaction coordinator log must be available. See [Transaction Coordinator Log](../../server-monitoring-logs/transaction-coordinator-log/transaction-coordinator-log-overview.md) for more information. Also see the the `<code>[log_tc_size](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#log_tc_size)</code>` system variable and the `<code>[--tc-heuristic-recover](#-tc-heuristic-recover)</code>` option.
* Default Value: `<code>tc.log</code>`



#### `<code>--master-connect-retry</code>`


* Commandline: `<code class="fixed" style="white-space:pre-wrap">--master-connect-retry=#</code>`
* Description: Deprecated in 5.1.17 and removed in 5.5. The number of seconds the replica thread will sleep before retrying to connect to the master, in case the master goes down or the connection is lost.



#### `<code>--memlock</code>`


* Commandline: `<code class="fixed" style="white-space:pre-wrap">--memlock</code>`
* Description: Lock mariadbd in memory.



#### `<code>--ndb-use-copying-alter-table</code>`


* Commandline: `<code class="fixed" style="white-space:pre-wrap">--ndb-use-copying-alter-table</code>`
* Description: Force ndbcluster to always copy tables at alter table (should only be used if on-line alter table fails).



#### `<code>--one-thread</code>`


* Commandline: `<code class="fixed" style="white-space:pre-wrap">--one-thread</code>`
* Description: (Deprecated): Only use one thread (for debugging under Linux). Use [thread-handling=no-threads](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/buffers-caches-and-threads/thread-pool/thread-pool-system-status-variables.md) instead.
* Removed: [MariaDB 10.0.4](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-1004-release-notes.md)



#### `<code>--plugin-load</code>`


* Commandline: `<code class="fixed" style="white-space:pre-wrap">--plugin-load=name</code>`
* Description: This option can be used to configure the server to load specific [plugins](../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/general-development-information/development-plans/old-plans/plugins-storage-engines-summit-for-mysqlmariadbdrizzle-2011.md). This option uses the following format:

  * Plugins can be specified in the format `<code>name=library</code>`, where `<code>name</code>` is the plugin name and `<code>library</code>` is the plugin library. This format installs a single plugin from the given plugin library.
  * Plugins can also be specified in the format `<code>library</code>`, where `<code>library</code>` is the plugin library. This format installs all plugins from the given plugin library.
  * Multiple plugins can be specified by separating them with semicolons.
* Special care must be taken when specifying the `<code>[--plugin-load](mariadbd-options.md#-plugin-load)</code>` option multiple times, or when specifying both the `<code>[--plugin-load](mariadbd-options.md#-plugin-load)</code>` option and the `<code>[--plugin-load-add](mariadbd-options.md#-plugin-load-add)</code>` option together. The `<code>[--plugin-load](mariadbd-options.md#-plugin-load)</code>` option resets the plugin load list, and this can cause unexpected problems if you are not aware. The `<code>[--plugin-load-add](mariadbd-options.md#-plugin-load-add)</code>` option does not reset the plugin load list, so it is much safer to use. See [Plugin Overview: Specifying Multiple Plugin Load Options](../../../reference/plugins/plugin-overview.md#specifying-multiple-plugin-load-options) for more information.
* See [Plugin Overview: Installing a Plugin with Plugin Load Options](../../../reference/plugins/plugin-overview.md#installing-a-plugin-with-plugin-load-options) for more information.



#### `<code>--plugin-load-add</code>`


* Commandline: `<code class="fixed" style="white-space:pre-wrap">--plugin-load-add=name</code>`
* Description: This option can be used to configure the server to load specific [plugins](../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/general-development-information/development-plans/old-plans/plugins-storage-engines-summit-for-mysqlmariadbdrizzle-2011.md). This option uses the following format:

  * Plugins can be specified in the format `<code>name=library</code>`, where `<code>name</code>` is the plugin name and `<code>library</code>` is the plugin library. This format installs a single plugin from the given plugin library.
  * Plugins can also be specified in the format `<code>library</code>`, where `<code>library</code>` is the plugin library. This format installs all plugins from the given plugin library.
  * Multiple plugins can be specified by separating them with semicolons.
* Special care must be taken when specifying both the `<code>[--plugin-load](mariadbd-options.md#-plugin-load)</code>` option and the `<code>[--plugin-load-add](mariadbd-options.md#-plugin-load-add)</code>` option together. The `<code>[--plugin-load](mariadbd-options.md#-plugin-load)</code>` option resets the plugin load list, and this can cause unexpected problems if you are not aware. The `<code>[--plugin-load-add](mariadbd-options.md#-plugin-load-add)</code>` option does not reset the plugin load list, so it is much safer to use. See [Plugin Overview: Specifying Multiple Plugin Load Options](../../../reference/plugins/plugin-overview.md#specifying-multiple-plugin-load-options) for more information.
* See [Plugin Overview: Installing a Plugin with Plugin Load Options](../../../reference/plugins/plugin-overview.md#installing-a-plugin-with-plugin-load-options) for more information.



#### `<code>--port-open-timeout</code>`


* Commandline: `<code class="fixed" style="white-space:pre-wrap">--port-open-timeout=#</code>`
* Description: Maximum time in seconds to wait for the port to become free. (Default: No wait).



#### `<code>--safe-user-create</code>`


* Commandline: `<code class="fixed" style="white-space:pre-wrap">--safe-user-create</code>`
* Description: Don't allow new user creation by the user who has no write privileges to the [mysql.user](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/the-mysql-database-tables/mysql-user-table.md) table.



#### `<code>--safemalloc-mem-limit</code>`


* Commandline: `<code class="fixed" style="white-space:pre-wrap">--safemalloc-mem-limit=#</code>`
* Description: Simulate memory shortage when compiled with the `<code><code>--</code>with-debug=full</code>` option.



#### `<code>--show-slave-auth-info</code>`


* Commandline: `<code class="fixed" style="white-space:pre-wrap">--show-slave-auth-info</code>`
* Description: Show user and password in SHOW SLAVE HOSTS on this primary.



#### `<code>--skip-grant-tables</code>`


* Commandline: `<code class="fixed" style="white-space:pre-wrap">--skip-grant-tables</code>`
* Description: Start without grant tables. This gives all users FULL ACCESS to all tables, which is useful in case of a lost root password. Use [mariadb-admin flush-privileges](../../../clients-and-utilities/mariadb-admin.md), [mariadb-admin reload](../../../clients-and-utilities/mariadb-admin.md) or [FLUSH PRIVILEGES](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/flush-commands/flush-tables-for-export.md) to resume using the grant tables. From [MariaDB 10.10](../../../../release-notes/mariadb-community-server/what-is-mariadb-1010.md), available as a [system variable](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#skip_grant_tables) as well.


Because the [Event Scheduler](../../../server-usage/programming-customizing-mariadb/triggers-events/event-scheduler/README.md) also depends on the grant tables for its functionality, it is automatically disabled when running with `<code class="fixed" style="white-space:pre-wrap">--skip-grant-tables</code>`.



#### `<code>--skip-host-cache</code>`


* Commandline: `<code class="fixed" style="white-space:pre-wrap">--skip-host-cache</code>`
* Description: Don't cache host names.



#### `<code>--skip-partition</code>`


* Commandline: `<code class="fixed" style="white-space:pre-wrap">--skip-partition</code>`, `<code class="fixed" style="white-space:pre-wrap">--disable-partition</code>`
* Description: Disables user-defined [partitioning](../../partitioning-tables/README.md). Previously partitioned tables cannot be accessed or modifed. Tables can still be seen with [SHOW TABLES](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-tables.md) or by viewing the [INFORMATION_SCHEMA.TABLES table](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-tables-table.md). Tables can be dropped with [DROP TABLE](../../../reference/sql-statements-and-structure/sql-statements/data-definition/drop/drop-tablespace.md), but this only removes .frm files, not the associated .par files, which will need to be removed manually.



#### `<code>--skip-slave-start</code>`


* Commandline: `<code class="fixed" style="white-space:pre-wrap">--skip-slave-start</code>`
* Description: If set, replica is not autostarted.



#### `<code>--skip-ssl</code>`


* Commandline: `<code class="fixed" style="white-space:pre-wrap">--skip-ssl</code>`
* Description: Disable [TLS connections](../../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/secure-connections-overview.md).



#### `<code>--skip-symlink</code>`


* Commandline: `<code class="fixed" style="white-space:pre-wrap">--skip-symlink</code>`
* Description: Don't allow symlinking of tables. Deprecated and removed in [MariaDB 5.5](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5.md). Use [symbolic-links](#-symbolic-links) with the `<code>skip</code>` [option prefix](#option-prefixes) instead.
* Removed: [MariaDB 5.5](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5.md)



#### `<code>--skip-thread-priority</code>`


* Commandline: `<code class="fixed" style="white-space:pre-wrap">--skip-thread-priority</code>`
* Description: Don't give threads different priorities. Deprecated and removed in [MariaDB 10.0](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md).
* Removed: [MariaDB 10.0](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md)



#### `<code>--sql-bin-update-same</code>`


* Commandline: `<code class="fixed" style="white-space:pre-wrap">--sql-bin-update-same=#</code>`
* Description: The update log was deprecated in version 5.0 and replaced by the [binary log](../../../reference/storage-engines/innodb/binary-log-group-commit-and-innodb-flushing-performance.md), so this option did nothing since then. Deprecated and removed in [MariaDB 5.5](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5.md).
* Removed: [MariaDB 5.5](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5.md)



#### `<code>--ssl</code>`


* Commandline: `<code class="fixed" style="white-space:pre-wrap">--ssl</code>`
* Description: Enable [TLS for connection](../../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/secure-connections-overview.md) (automatically enabled with other flags). Disable with '`<code><code>--</code>skip-ssl</code>`'.



#### `<code>--stack-trace</code>`


* Commandline: `<code class="fixed" style="white-space:pre-wrap">--stack-trace</code>`, `<code class="fixed" style="white-space:pre-wrap">--skip-stack-trace</code>`
* Description: Print a stack trace on failure. Enabled by default, disable with `<code>-skip-stack-trace</code>`.



#### `<code>--symbolic-links</code>`


* Commandline: `<code class="fixed" style="white-space:pre-wrap">--symbolic-links</code>`
* Description: Enables symbolic link support. When set, the [have_symlink](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#have_symlink) system variable shows as `<code>YES</code>`. Silently ignored in Windows. Use `<code>--skip-symbolic-links</code>` to disable.



#### `<code>--tc-heuristic-recover</code>`


* Commandline: `<code class="fixed" style="white-space:pre-wrap">--tc-heuristic-recover=name</code>`
* Description: If [manual heuristic recovery](../../server-monitoring-logs/transaction-coordinator-log/heuristic-recovery-with-the-transaction-coordinator-log.md) is needed, this option defines the decision to use in the heuristic recovery process. Manual heuristic recovery may be needed if the [transaction coordination log](../../server-monitoring-logs/transaction-coordinator-log/transaction-coordinator-log-overview.md) is missing or if it doesn't contain all prepared transactions. This option can be set to `<code>OFF</code>`, `<code>COMMIT</code>`, or `<code>ROLLBACK</code>`. The default is `<code>OFF</code>`. See also the `<code>[--log-tc](mariadbd-options.md#-log-tc)</code>` server option and the `<code>[log_tc_size](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#log_tc_size)</code>` system variable.



#### `<code>--temp-pool</code>`


* Commandline: `<code class="fixed" style="white-space:pre-wrap">--temp-pool</code>`
* Description: Using this option will cause most temporary files created to use a small set of names, rather than a unique name for each new file. This behavior works around a bug in old Linux kernels where the kernel appeared to "leak" memory. In a Docker environment it might look like an unbounded working-set memory growth. 
Defaults to `<code>1</code>` until [MariaDB 10.5.6](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1056-release-notes.md), use `<code>--skip-temp-pool</code>` to disable. Defaults to `<code>0</code>` from [MariaDB 10.5.7](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1057-release-notes.md), as benchmarking shows it causes a heavy mutex contention.



#### `<code>--test-expect-abort</code>`


* Commandline: `<code class="fixed" style="white-space:pre-wrap">--test-expect-abort</code>`
* Description: Expect that server aborts with 'abort'; Don't write out server variables on 'abort'. Useful only for test scripts.



#### `<code>--test-ignore-wrong-options</code>`


* Commandline: `<code class="fixed" style="white-space:pre-wrap">--test-ignore-wrong-options</code>`
* Description: Ignore wrong enums values in command line arguments. Useful only for test scripts.



#### `<code>--user</code>`


* Commandline: `<code class="fixed" style="white-space:pre-wrap">--user=name</code>`
* Description: Run mariadbd daemon as user.



#### `<code>--verbose</code>`


* Commandline: `<code class="fixed" style="white-space:pre-wrap">-v</code>`, `<code class="fixed" style="white-space:pre-wrap">--verbose</code>`
* Description: Used with [help](#help) option for detailed help.



## Other Options and System Variables


* [allow-suspicious-udfs](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#allow-suspicious-udfs)
* [automatic-sp-privileges](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#automatic_sp_privileges)
* [back-log](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#back_log)
* [basedir](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#basedir)
* [check-constraint-checks](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#check_constraint_checks)
* [column-compression-threshold](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/optimization-and-tuning-compression/storage-engine-independent-column-compression.md#column_compression_threshold)
* [column-compression-zlib-level](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/optimization-and-tuning-compression/storage-engine-independent-column-compression.md#column_compression_zlib_level)
* [column-compression-zlib-strategy](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/optimization-and-tuning-compression/storage-engine-independent-column-compression.md#column_compression_zlib_strategy)
* [column-compression-zlib-wrap](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/optimization-and-tuning-compression/storage-engine-independent-column-compression.md#column_compression_zlib_wrap)
* [completion-type](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#completion_type)
* [connect-timeout](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#connect_timeout)
* [datadir](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#datadir)
* [date-format](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#date_format)
* [datetime-format](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#datetime_format)
* [deadlock-search-depth-long](../../../reference/storage-engines/aria/aria-system-variables.md)
* [deadlock-search-depth-short](../../../reference/storage-engines/aria/aria-system-variables.md)
* [deadlock-timeout-long](../../../reference/storage-engines/aria/aria-system-variables.md)
* [deadlock-timeout-short](../../../reference/storage-engines/aria/aria-system-variables.md)
* [default-password-lifetime](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#default_password_lifetime)
* [default-regex-flags](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#default_regex_flags)
* [default-storage-engine](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#default_storage_engine)
* [default-table-type](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#default_table_type)
* [delay-key-write](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#delay_key_write)
* [disconnect-on-expired-password](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#disconnect_on_expired_password)
* [div-precision-increment](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#div_precision_increment)
* [enable-named-pipe](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#named_pipe)
* [encrypt-binlog](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#encrypt_binlog)
* [encrypt-tmp-disk-tables](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#encrypt_tmp_disk_tables)
* [encrypt-tmp-files](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#encrypt_tmp_files)
* [encryption-algorithm](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#encryption_algorithm)
* [engine-condition-pushdown](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#engine_condition_pushdown)
* [eq-range-index-dive-limit](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#eq_range_index_dive_limit)
* [event-scheduler](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#event_scheduler)
* [expire-logs-days](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#expire_logs_days)
* [explicit-defaults-for-timestamp](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#explicit_defaults_for_timestamp)
* [extra-max-connections](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/buffers-caches-and-threads/thread-pool/thread-pool-system-status-variables.md)
* [extra-port](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/buffers-caches-and-threads/thread-pool/thread-pool-system-status-variables.md)
* [flush](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#flush)
* [flush-time](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#flush_time)
* [ft-boolean-syntax](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#ft_boolean_syntax)
* [ft-max-word-len](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#ft_max_word_len)
* [ft-min-word-len](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#ft_min_word_len)
* [ft-query-expansion-limit](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#ft_query_expansion_limit)
* [ft-stopword-file](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#ft_stopword_file)
* [general-log](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#general_log)
* [general-log-file](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#general_log_file)
* [group-concat-max-len](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#group_concat_max_len)
* [histogram-size](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#histogram_size)
* [histogram-type](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#histogram_type)
* [host-cache-size](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#host_cache_size)
* [idle-readonly-transaction-timeout](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#idle_readonly_transaction_timeout)
* [idle-transaction-timeout](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#idle_transaction_timeout)
* [idle-write-transaction-timeout](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#idle_write_transaction_timeout)
* [ignore-db-dirs](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#ignore_db_dirs)
* [in-predicate-conversion-threshold](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#in_predicate_conversion_threshold)
* [init-connect](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#init_connect)
* [init-file](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#init_file)
* [interactive-timeout](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#interactive_timeout)
* [large-pages](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#large_pages)
* [local-infile](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#local_infile)
* [lock-wait-timeout](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#lock_wait_timeout)
* [log](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#log)
* [log-disabled-statements](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#log_disabled_statements)
* [log-error](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#log_error)
* [log-output](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#log_output)
* [log-queries-not-using-indexes](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#log_queries_not_using_indexes)
* [log-slow-admin-statements](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#log_slow_admin_statements)
* [log-slow-always-query-time](../../server-monitoring-logs/slow-query-log/log_slow_always_query_time-system-variable.md)
* [log-slow-disabled-statements](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#log_slow_disabled_statements)
* [log-slow-filter](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#log_slow_filter)
* [log-slow-min-examined-row-limit](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#log_slow_min_examined_row_limit)
* [log-slow-queries](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#log_slow_queries)
* [log-slow-query](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#log_slow_query)
* [log-slow-query-file](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#log_slow_query_file)
* [log-slow-query-time](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#log_slow_query_time)
* [log-slow-rate-limit](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#log_slow_rate_limit)
* [log-slow-slave-statements](../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md#log_slow_slave_statements)
* [log-slow-verbosity](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#log_slow_verbosity)
* [log-tc-size](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#log_tc_size)
* [log-warnings](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#log_warnings)
* [long-query-time](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#long_query_time)
* [low-priority-updates](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#low_priority_updates)
* [lower-case-table-names](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#lower_case_table_names)
* [max-allowed-packet](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#max_allowed_packet)
* [max-connections](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#max_connections)
* [max-connect-errors](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#max_connect_errors)
* [max-delayed-threads](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#max_delayed_threads)
* [max-digest-length](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#max_digest_length%22)
* [max-error-count](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#max_error_count)
* [max-length-for-sort-data](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#max_length_for_sort_data)
* [max-long-data-size](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#max_long_data_size)
* [max-password-errors](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#max_password_errors)
* [max-prepared-stmt-count](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#max_prepared_stmt_count)
* [max-recursive-iterations](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#max_recursive_iterations)
* [max-rowid-filter-size](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#max_rowid_filter_size)
* [max-session-mem-used](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#max_session_mem_used)
* [max-sp-recursion-depth](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#max_sp_recursion_depth)
* [max-statement-time](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#max_statement_time)
* [max-tmp-session-space-usage](../../../security/user-account-management/limiting-size-of-created-disk-temporary-files-and-tables/max_tmp_session_space_usage-system-variable.md)
* [max-tmp-tables](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#max_tmp_tables)
* [max-tmp-total-space-usage](../../../security/user-account-management/limiting-size-of-created-disk-temporary-files-and-tables/max_tmp_total_space_usage-system-variable.md)
* [max-user-connections](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#max_user_connections)
* [max-write-lock-count](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#max_write_lock_count)
* [metadata-locks-cache-size](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#metadata_locks_cache_size)
* [metadata-locks-hash-instances](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#metadata_locks_hash_instances)
* [min-examined-row-limit](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#min_examined_row_limit)
* [mrr-buffer-size](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#mrr_buffer_size)
* [multi-range-count](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#multi_range_count)
* [--mysql56-temporal-format](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#mysql56_temporal_format)
* [net-buffer-length](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#net_buffer_length)
* [net-read-timeout](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#net_read_timeout)
* [net-retry-count](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#net_retry_count)
* [net-write-timeout](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#net_write_timeout)
* [open-files-limit](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#open_files_limit)
* [pid-file](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#pid_file)
* [plugin-dir](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#plugin_dir)
* [plugin-maturity](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#plugin_maturity)
* [port](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#port)
* [preload-buffer-size](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#preload_buffer_size)
* [profiling-history-size](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#profiling_history_size)
* [progress-report-time](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#progress_report_time)
* [proxy-protocol-networks](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#proxy_protocol_networks)
* [query-cache-limit](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#query_cache_limit)
* [query-cache-min-res-unit](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#query_cache_min_res_unit)
* [query-cache-strip-comments](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#query_cache_strip_comments)
* [query-cache-wlock-invalidate](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#query_cache_wlock_invalidate)
* [read-rnd-buffer-size](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#read_rnd_buffer_size)
* [read-only](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#read_only)
* [redirect-url](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#redirect_url)
* [require-secure-transport](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#require_secure_transport)
* [safe-show-database](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#safe_show_database)
* [secure-auth](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#secure_auth)
* [secure-file-priv](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#secure_file_priv)
* [secure-timestamp](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#secure_timestamp)
* [session-track-schema](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#session_track_schema)
* [session-track-state-change](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#session_track_state_change)
* [session-track-system-variables](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#session_track_system_variables)
* [session-track-transaction-info](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#session_track_transaction_info)
* [skip-automatic-sp-privileges](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#automatic_sp_privileges)
* [skip-external-locking](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#skip_external_locking)
* [skip-large-pages](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#large_pages)
* [skip-log-error](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#log_error)
* [skip-name-resolve](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#skip_name_resolve)
* [skip-networking](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#skip_networking)
* [skip-show-database](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#skip_show_database)
* [slow-launch-time](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#slow_launch_time)
* [slow-query-log](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#slow_query_log)
* [slow-query-log-file](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#slow_query_log_file)
* [socket](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#socket)
* [sort-buffer-size](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#sort_buffer_size)
* [sql-if-exists](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#sql_if_exists)
* [sql-mode](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#sql_mode)
* [ssl-ca](../../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/ssltls-system-variables.md)
* [ssl-capath](../../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/ssltls-system-variables.md)
* [ssl-cert](../../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/ssltls-system-variables.md)
* [ssl-cipher](../../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/ssltls-system-variables.md)
* [ssl-crl](../../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/ssltls-system-variables.md)
* [ssl-crlpath](../../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/ssltls-system-variables.md)
* [ssl-key](../../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/ssltls-system-variables.md)
* [standards_compliant_cte](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#standards_compliant_cte)
* [stored-program-cache](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#stored_program_cache)
* [strict_password_validation](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#strict_password_validation)
* [sync-frm](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#sync_frm)
* [system-versioning-alter-history](../../../reference/sql-statements-and-structure/temporal-tables/system-versioned-tables.md#system_versioning_alter_history)
* [system-versioning-asof](../../../reference/sql-statements-and-structure/temporal-tables/system-versioned-tables.md#system_versioning_asof)
* [system-versioning-innodb-algorithm-simple](../../../reference/sql-statements-and-structure/temporal-tables/system-versioned-tables.md#system_versioning_innodb_algorithm_simple)
* [system-versioning-insert-history](../../../reference/sql-statements-and-structure/temporal-tables/system-versioned-tables.md#system_versioning_insert_history)
* [table-lock-wait-timeout](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#table_lock_wait_timeout)
* [tcp-keepalive-interval](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#tcp_keepalive_interval)
* [tcp-keepalive-probes](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#tcp_keepalive_probes)
* [tcp-keepalive-time](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#tcp_keepalive_time)
* [tcp-nodelay](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#tcp_nodelay)
* [thread-cache-size](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#thread_cache_size)
* [thread-concurrency](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#thread_concurrency)
* [thread-handling](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#thread_handling)
* [thread-pool-dedicated-listener](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/buffers-caches-and-threads/thread-pool/thread-pool-system-status-variables.md)
* [thread-pool-exact-stats](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/buffers-caches-and-threads/thread-pool/thread-pool-system-status-variables.md)
* [thread-pool-idle-timeout](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/buffers-caches-and-threads/thread-pool/thread-pool-system-status-variables.md)
* [thread-pool-max-threads](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/buffers-caches-and-threads/thread-pool/thread-pool-system-status-variables.md)
* [thread-pool-min-threads](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/buffers-caches-and-threads/thread-pool/thread-pool-system-status-variables.md)
* [thread-pool-oversubscribe](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/buffers-caches-and-threads/thread-pool/thread-pool-system-status-variables.md)
* [thread-pool-prio-kickup-timer](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/buffers-caches-and-threads/thread-pool/thread-pool-system-status-variables.md)
* [thread-pool-priority](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/buffers-caches-and-threads/thread-pool/thread-pool-system-status-variables.md)
* [thread-pool-size](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/buffers-caches-and-threads/thread-pool/thread-pool-system-status-variables.md)
* [thread-pool-stall-limit](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/buffers-caches-and-threads/thread-pool/thread-pool-system-status-variables.md)
* [thread-stack](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#thread_stack)
* [timed-mutexes](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#timed_mutexes)
* [time-format](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#time_format)
* [tls-version](../../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/ssltls-system-variables.md)
* [tmpdir](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#tmpdir)
* [transaction-isolation](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#tx_isolation)
* [transaction-alloc-block-size](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#transaction_alloc_block_size)
* [transaction-prealloc-size](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#transaction_prealloc_size)
* [transaction-read-only](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#tx_read_only)
* [updatable-views-with-limit](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#updatable_views_with_limit)
* [userstat](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#userstat)
* [version](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#version)
* [wait-timeout](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#wait_timeout)


## Authentication Plugins - Options and System Variables


### Authentication Plugin - `<code>ed25519</code>`


The options related to the `<code>[ed25519](../../../reference/plugins/authentication-plugins/authentication-plugin-ed25519.md)</code>` authentication plugin can be found [here](../../../reference/plugins/authentication-plugins/authentication-plugin-ed25519.md#options).


### Authentication Plugin - `<code>gssapi</code>`


The system variables related to the `<code>[gssapi](../../../reference/plugins/authentication-plugins/authentication-plugin-gssapi.md)</code>` authentication plugin can be found [here](../../../reference/plugins/authentication-plugins/authentication-plugin-gssapi.md#system-variables).


The options related to the `<code>[gssapi](../../../reference/plugins/authentication-plugins/authentication-plugin-gssapi.md)</code>` authentication plugin can be found [here](../../../reference/plugins/authentication-plugins/authentication-plugin-gssapi.md#options).


### Authentication Plugin - `<code>named_pipe</code>`


The options related to the `<code>[named_pipe](../../../reference/plugins/authentication-plugins/authentication-plugin-named-pipe.md)</code>` authentication plugin can be found [here](../../../reference/plugins/authentication-plugins/authentication-plugin-named-pipe.md#options).


### Authentication Plugin - `<code>pam</code>`


The system variables related to the `<code>[pam](../../../reference/plugins/authentication-plugins/authentication-with-pluggable-authentication-modules-pam/authentication-plugin-pam.md)</code>` authentication plugin can be found [here](../../../reference/plugins/authentication-plugins/authentication-with-pluggable-authentication-modules-pam/authentication-plugin-pam.md#system-variables).


The options related to the `<code>[pam](../../../reference/plugins/authentication-plugins/authentication-with-pluggable-authentication-modules-pam/authentication-plugin-pam.md)</code>` authentication plugin can be found [here](../../../reference/plugins/authentication-plugins/authentication-with-pluggable-authentication-modules-pam/authentication-plugin-pam.md#options).


### Authentication Plugin - `<code>unix_socket</code>`


The options related to the `<code>[unix_socket](../../../reference/plugins/authentication-plugins/authentication-plugin-unix-socket.md)</code>` authentication plugin can be found [here](../../../reference/plugins/authentication-plugins/authentication-plugin-unix-socket.md#options).


## Encryption Plugins - Options and System Variables


### Encryption Plugin - `<code>aws_key_management</code>`


The system variables related to the `<code>[aws_key_management](../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/key-management-and-encryption-plugins/aws-key-management-encryption-plugin-setup-guide.md)</code>` encryption plugin can be found [here](../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/key-management-and-encryption-plugins/aws-key-management-encryption-plugin-setup-guide.md#system-variables).


The options elated to the `<code>[aws_key_management](../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/key-management-and-encryption-plugins/aws-key-management-encryption-plugin-setup-guide.md)</code>` encryption plugin can be found [here](../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/key-management-and-encryption-plugins/aws-key-management-encryption-plugin-setup-guide.md#options).


### Encryption Plugin - `<code>file_key_management</code>`


The system variables related to the `<code>[file_key_management](../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/key-management-and-encryption-plugins/file-key-management-encryption-plugin.md)</code>` encryption plugin can be found [here](../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/key-management-and-encryption-plugins/file-key-management-encryption-plugin.md#system-variables).


The options related to the `<code>[file_key_management](../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/key-management-and-encryption-plugins/file-key-management-encryption-plugin.md)</code>` encryption plugin can be found [here](../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/key-management-and-encryption-plugins/file-key-management-encryption-plugin.md#options).


## Password Validation Plugins - Options and System Variables


### Password Validation Plugin - `<code>simple_password_check</code>`


The system variables related to the `<code>[simple_password_check](../../../reference/plugins/password-validation-plugins/simple-password-check-plugin.md)</code>` password validation plugin can be found [here](../../../reference/plugins/password-validation-plugins/simple-password-check-plugin.md).


The options related to the `<code>[simple_password_check](../../../reference/plugins/password-validation-plugins/simple-password-check-plugin.md)</code>` password validation plugin can be found [here](../../../reference/plugins/password-validation-plugins/simple-password-check-plugin.md).


### Password Validation Plugin - `<code>cracklib_password_check</code>`


The system variables related to the `<code>[cracklib_password_check](../../../reference/plugins/password-validation-plugins/cracklib-password-check-plugin.md)</code>` password validation plugin can be found [here](../../../reference/plugins/password-validation-plugins/cracklib-password-check-plugin.md).


The options related to the `<code>[cracklib_password_check](../../../reference/plugins/password-validation-plugins/cracklib-password-check-plugin.md)</code>` password validation plugin can be found [here](../../../reference/plugins/password-validation-plugins/cracklib-password-check-plugin.md).


## Audit Plugins - Options and System Variables


### Audit Plugin - `<code>server_audit</code>`


Options and system variables related to the `<code>[server_audit](../../../reference/plugins/mariadb-audit-plugin/release-notes-mariadb-audit-plugin/mariadb-audit-plugin-113-release-notes.md)</code>` audit plugin can be found [here](../../../reference/plugins/mariadb-audit-plugin/mariadb-audit-plugin-options-and-system-variables.md).


### Audit Plugin - `<code>SQL_ERROR_LOG</code>`


The options and system variables related to the [SQL_ERROR_LOG](../../server-monitoring-logs/sql-error-log-plugin.md) audit plugin can be found [here](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/sql-error-log-system-variables-and-options.md#system-variables).


### Audit Plugin - QUERY_RESPONSE_TIME_AUDIT


The options related to the `<code>[QUERY_RESPONSE_TIME_AUDIT](../../../reference/plugins/other-plugins/query-response-time-plugin.md)</code>` audit plugin can be found [here](../../../reference/plugins/other-plugins/query-response-time-plugin.md#options).


## Daemon Plugins - Options and System Variables


### Daemon Plugin - `<code>handlersocket</code>`


The options for the HandlerSocket plugin are all described on the [HandlerSocket Configuration Option](../../../reference/sql-statements-and-structure/nosql/handlersocket/handlersocket-configuration-options.md) page.


## Information Schema Plugins - Options and System Variables


### Information Schema Plugin - `<code>DISKS</code>`


The options related to the `<code>[DISKS](../../../reference/plugins/other-plugins/disks-plugin.md)</code>` information schema plugin can be found [here](../../../reference/plugins/other-plugins/disks-plugin.md#options).


### Information Schema Plugin - `<code>feedback</code>`


The system variables related to the `<code>[feedback](../../../reference/plugins/other-plugins/feedback-plugin.md)</code>` plugin can be found [here](../../../reference/plugins/other-plugins/feedback-plugin.md#system-variables).


The options related to the `<code>[feedback](../../../reference/plugins/other-plugins/feedback-plugin.md)</code>` plugin can be found [here](../../../reference/plugins/other-plugins/feedback-plugin.md#options).


### Information Schema Plugin - `<code>LOCALES</code>`


The options related to the `<code>[LOCALES](../../../reference/data-types/string-data-types/character-sets/internationalization-and-localization/locales-plugin.md)</code>` information schema plugin can be found [here](../../../reference/data-types/string-data-types/character-sets/internationalization-and-localization/locales-plugin.md#options).


### Information Schema Plugin - `<code>METADATA_LOCK_INFO</code>`


The options related to the `<code>[METADATA_LOCK_INFO](../../../reference/plugins/other-plugins/metadata-lock-info-plugin.md)</code>` information schema plugin can be found [here](../../../reference/plugins/other-plugins/metadata-lock-info-plugin.md).


### Information Schema Plugin - `<code>QUERY_CACHE_INFO</code>`


The options related to the `<code>[QUERY_CACHE_INFO](../../../reference/plugins/other-plugins/query-cache-information-plugin.md)</code>` information schema plugin can be found [here](../../../reference/plugins/other-plugins/query-cache-information-plugin.md#options).


### Information Schema Plugin - `<code>QUERY_RESPONSE_TIME</code>`


The system variables related to the `<code>[QUERY_RESPONSE_TIME](../../../reference/plugins/other-plugins/query-response-time-plugin.md)</code>` information schema plugin can be found [here](../../../reference/plugins/other-plugins/query-response-time-plugin.md#system-variables).


The options related to the `<code>[QUERY_RESPONSE_TIME](../../../reference/plugins/other-plugins/query-response-time-plugin.md)</code>` information schema plugin can be found [here](../../../reference/plugins/other-plugins/query-response-time-plugin.md#options).


### Information Schema Plugin - `<code>user_variables</code>`


The options related to the `<code>[user_variables](../../../reference/plugins/other-plugins/user-variables-plugin.md)</code>` information schema plugin can be found [here](../../../reference/plugins/other-plugins/user-variables-plugin.md#options).


### Information Schema Plugin - `<code>WSREP_MEMBERSHIP</code>`


The options related to the `<code>[WSREP_MEMBERSHIP](../../../reference/plugins/mariadb-replication-cluster-plugins/wsrep_info-plugin.md)</code>` information schema plugin can be found [here](../../../reference/plugins/mariadb-replication-cluster-plugins/wsrep_info-plugin.md#options).


### Information Schema Plugin - `<code>WSREP_STATUS</code>`


The options related to the `<code>[WSREP_STATUS](../../../reference/plugins/mariadb-replication-cluster-plugins/wsrep_info-plugin.md)</code>` information schema plugin can be found [here](../../../reference/plugins/mariadb-replication-cluster-plugins/wsrep_info-plugin.md#options).


## Replication Plugins - Options and System Variables


### Replication Plugin - `<code>rpl_semi_sync_master</code>`


The system variables related to the `<code>[rpl_semi_sync_master](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/semisynchronous-replication-plugin-status-variables.md)</code>` replication plugin can be found [here](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/semisynchronous-replication-plugin-status-variables.md#system-variables).


The options related to the `<code>[rpl_semi_sync_master](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/semisynchronous-replication-plugin-status-variables.md)</code>` replication plugin can be found [here](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/semisynchronous-replication-plugin-status-variables.md#options).


### Replication Plugin - `<code>rpl_semi_sync_slave</code>`


The system variables related to the `<code>[rpl_semi_sync_slave](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/semisynchronous-replication-plugin-status-variables.md)</code>` replication plugin can be found [here](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/semisynchronous-replication-plugin-status-variables.md#system-variables).


The options related to the `<code>[rpl_semi_sync_slave](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/semisynchronous-replication-plugin-status-variables.md)</code>` replication plugin can be found [here](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/semisynchronous-replication-plugin-status-variables.md#options).


## Default Values


You can verify the default values for an option by doing:


```
mariadbd --no-defaults --help --verbose
```
