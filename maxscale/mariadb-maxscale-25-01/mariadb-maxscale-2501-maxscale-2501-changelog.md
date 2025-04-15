
# MaxScale 25.01 Changelog

# Changelog


## MariaDB MaxScale 25.01


* The functionality that was enabled by the `<code>reuse_prepared_statements</code>`
 parameter in readwritesplit has been moved into the
 [PsReuse](mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-psreuse.md) filter module. The `<code>reuse_prepared_statements</code>`
 parameter has been removed from readwritesplit.
* The functionality that was enabled by the `<code>optimistic_trx</code>` parameter in
 readwritesplit has been moved into the
 [OptimisticTrx](mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-optimistic-transaction-execution-filter.md) filter module. The
 `<code>optimistic_trx</code>` parameter has been removed from readwritesplit.
* Added a safe-option to MariaDB Monitor auto-failover. safe does not
 perform failover if data loss is certain. Equivalent manual command added.
 See [monitor documentation](mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)
 for more information.
* MariaDB Monitor can perform a write test on the primary server.
 See [monitor documentation](mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)
 for more information.
* MariaDB Monitor switchover can be called with key-value arguments. This form
 also supports leaving the old primary in maintenance mode instead of
 redirecting it. See [monitor documentation](mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)
 for more information.
* Allowed REST-API TLS ciphers can be tuned with the global setting
 [admin_ssl_cipher](mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md).
* The `<code>transaction_replay_safe_commit</code>` parameter in readwritesplit now
 also disables the replaying of all writes done when autocommit is
 enabled. This means that transaction replay will never replay a
 statement that may commit a transaction.
* NoSQL protocol has been extended.
* Now supports [MongoDB Compass](https://www.mongodb.com/products/tools/compass)
* Initial support for the command aggregate has been added.
* When running in a container, MaxScale adapts to the amount of resources
 available in the container.
* MaxGUI Query Editor now requires delimiter changes for compound statements such
 as stored procedures, functions, etc. See [delimiters documentation](../../server/clients-and-utilities/mariadb-client/delimiters.md)
 for more information. However, the dedicated SQL editor (opened via "Create Function",
 "Alter Function", "Create Trigger" etc., in the schema tree explorer) does not require
 delimiter changes as it handles SQL as a single statement.
* MaxGUI Query Editor now automatically injects a `<code>LIMIT</code>` clause with a
 default limit of 10000 into every `<code>SELECT</code>` statement.
* The new
 [trace_file_dir](https://mariadb.com/kb/Getting-Started/Configuration-Guide#trace_file_dir) and
 [trace_file_size](https://mariadb.com/kb/Getting-Started/Configuration-Guide#trace_file_size)
 parameters can be used to enable a trace log that writes messages from all log
 levels to a set of rotating log files. If enabled, the symlink
 `<code>/var/log/maxscale/maxscale.trace</code>` will point to the latest trace log
 file. This is a low-overhead alternative to enabling `<code>log_info</code>` and is
 intended to be used for debugging application problems in production where the
 overhead of `<code>log_info</code>` cannot be afforded.
* The [Avro Router](mariadb-maxscale-25-01-tutorials/mariadb-maxscale-2501-maxscale-2501-avrorouter-tutorial.md) and the [CDC Protocol](mariadb-maxscale-25-01-protocols/mariadb-maxscale-2501-maxscale-2501-change-data-capture-cdc-protocol.md)
 have been deprecated and will be removed in the next major release.
 [KafkaCDC](mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkacdc.md) can be used instead.
* The [passive](https://mariadb.com/kb/Getting-Started/Configuration-Guide#passive) configuration
 setting has been deprecated and will be removed in the next series.


For more details, please refer to:


* [MariaDB MaxScale 25.01.2 Release Notes](mariadb-maxscale-25-01-release-notes/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-enterprise-25012-release-notes.md)
* [MariaDB MaxScale 25.01.1 Release Notes](mariadb-maxscale-25-01-release-notes/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-25011-release-notes-2025-01-16.md)


## MariaDB MaxScale 24.02


* The default values of some readwritesplit parameters have been updated. The
 new default values are:


  * `<code>master_reconnection=true</code>`
  * `<code>master_failure_mode=fail_on_write</code>`
  * `<code>strict_tmp_tables=true</code>`
  * `<code>transaction_replay_timeout=30s</code>`
* MariaDB-Monitor now requires MariaDB Server 10.4 or newer for failover/
 switchover. Server 10.3 is end of life.
* Server setting `<code>private_address</code>` added. Used for detecting and setting up
 replication. See
 [MariaDB Monitor documentation](mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)
 for more information.
* MariaDB-Monitor allows customization of some Mariabackup settings. See
 [mariabackup_use_memory](mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)
 and [mariabackup_parallel](mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)
 for more information.
* MariaDB-Monitor setting `<code>servers_no_promotion</code>` now affects primary
 server selection during MaxScale startup or due to replication topology
 changes.
* Pam authentication now always checks account status. Previously, this check
 was not performed if MaxScale was configured for username mapping
 (`<code>authenticator_options=pam_backend_mapping=mariadb</code>`). This means that if
 username mapping is configured in the OS pam service config, the final
 username must be a valid user. This is similar to MariaDB Server behavior.
* Support for the legacy SysV and Upstart system managers has been removed. In
 practice this change will not affect anything as all supported operating
 systems use SystemD as the system manager and MaxScale has long preferred it
 over the legacy systems.
* The output of `<code>maxctrl show service</code>` now includes the statistics for
 the services.
* The `<code>max_sescmd_history_length</code>` and `<code>avg_sescmd_history_length</code>` statistics in
 readwritesplit were moved into the core as service statistics. The session
 command history was moved into the MaxScale core in MaxScale 6 but the
 statistics were not updated to match this.
* Several redundant schemarouter statistics have been either replaced by
 statistics that are found in the general service statistics output or have
 been removed if they were irrelevant.


  * `<code>longest_sescmd_chain</code>` replaced by `<code>max_sescmd_history_length</code>`.
  * `<code>queries</code>` replaced with `<code>routed_packets</code>`.
  * `<code>times_sescmd_limit_exceeded</code>` has been removed.
  * `<code>sescmd_percentage</code>` has been removed.
  * `<code>longest_session</code>` replaced with `<code>max_session_lifetime</code>`.
  * `<code>average_session</code>` replaced with `<code>avg_session_lifetime</code>`.
  * `<code>shortest_session</code>` has been removed.
* `<code>admin_readwrite_hosts</code>` and `<code>admin_readonly_hosts</code>` added. These settings limit
 the allowed source addresses for admin (REST-API) connections. See
 [here](mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
 for more information.
* The `<code>alter</code>` commands in MaxCtrl now allow modifications to the
 `<code>targets</code>`, `<code>servers</code>`, `<code>filters</code>` and `<code>cluster</code>` parameters for monitors
 and services. This makes it easier to define the exact set of servers
 that is to be used by a monitor or a service.
* The [causal_reads](mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-readwritesplit.md) feature no longer
 requires modifying `<code>session_track_system_variables</code>` on
 the server. MaxScale adds `<code>last_gtid</code>` to the variable automatically
 for each session. Clients should not modify it manually.
* The [qlafilter](mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-query-log-all-filter.md) now logs the execution of the
 binary protocol statements as text. This makes it so that for all execution of
 SQL, the `<code>query</code>` value in `<code>log_data</code>` will produce output.
* The functionality that the `<code>auth_all_servers</code>` parameter enabled is
 automatically enabled by the schemarouter whenever it is used.


For more details, please refer to:


* [MariaDB MaxScale 24.02.5 Release Notes](https://mariadb.com/kb/en/Release-Notes/MaxScale-24.02.5-Release-Notes)
* [MariaDB MaxScale 24.02.4 Release Notes](https://mariadb.com/kb/en/maxscale-25-01-mariadb-maxscale-24-02-4-release-notes-2024-12-09/)
* [MariaDB MaxScale 24.02.3 Release Notes](https://mariadb.com/kb/en/maxscale-25-01-mariadb-maxscale-24-02-3-release-notes-2024-09-09/)
* [MariaDB MaxScale 24.02.2 Release Notes](https://mariadb.com/kb/en/maxscale-25-01-mariadb-maxscale-24-02-2-release-notes-2024-06-03/)
* [MariaDB MaxScale 24.02.1 Release Notes](https://mariadb.com/kb/en/maxscale-25-01-mariadb-maxscale-24-02-1-release-notes-2024-04-10/)
* [MariaDB MaxScale 24.02.0 Release Notes](https://mariadb.com/kb/en/maxscale-25-01-mariadb-maxscale-24-02-0-release-notes-2024-02-29/)


## MariaDB MaxScale 23.08


* The global setting `<code>skip_permission_checks</code>` has been deprecated and is
 ignored. Monitors start regardless of monitor user permissions.
* The uppercase versions of the `<code>slave_selection_criteria</code>` parameter in
 readwritesplit have been deprecated. All runtime modifications to the
 parameters are now saved using the lowercase versions.
* By default, readwritesplit will not replay transactions that are about to
 commit when `<code>transaction_replay</code>` is enabled. To retain the old behavior where
 transactions were always replayed, disable `<code>transaction_replay_safe_commit</code>`.
* Readwritesplit will now retry queries with partially returned results if they
 are done inside a transaction and `<code>transaction_replay</code>` is enabled.
* `<code>prune_sescmd_history</code>` now also performs history simplification by removing
 redundant executions of the same statement. This will reduce memory usage in
 the case when history repeats a small cycle of commands. One example of this
 is connection pools that prepare the connection with a small set of commands
 like `<code>SET NAMES</code>` and `<code>SET SQL_MODE</code>`.
* Common configuration settings can now be specified in a separate section,
 to be included by other sections.
* When changing the service password, the previous password will be retained
 and continue to be used if the new does not work.
* Embedded newlines are removed from logged messages.
* Schemarouter database map caches can be cleared with `<code>maxctrl call command
 schemarouter clear <service></code>` where `<code><service></code>` is a service that uses the
 schemarouter.
* Schemarouter now allows stale cache entries to be used while the database map
 cache is being updated. By default the entries are usable for 150 seconds
 after they have gone stale. This limit can be configured with the
 `<code>max_staleness</code>` parameter.
* Added switchover-force command to MariaDB Monitor. This command performs a
 switchover even if primary server is unresponsive.
* Switchover now uses a longer command timeout on the old master. This should
 remove the need for adjusting monitor setting `<code>backend_read_timeout</code>` to get
 switchover to work.
* The NoSQL protocol now provides internal caching.
* Additional metadata is sent in the connection handshake. For more information,
 refer to the
 [parameter](mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
 documentation.
* The `<code>connection_timeout</code>` parameter was renamed to `<code>wait_timeout</code>` to make the
 naming of the parameters the same in MaxScale and MariaDB server. The old
 `<code>connection_timeout</code>` parameter is now an alias to `<code>wait_timeout</code>` and its use
 has been deprecated. If used, a warning will be logged that the parameter is
 deprecated.
* The `<code>strip_db_esc</code>` parameter has been deprecated. The default behavior of
 stripping the escape characters is in all known cases the correct thing to
 do. Only broken legacy versions where the grants would be returned without
 backslash escaping would require this parameter to work.
* The Xpand monitor is now region aware.
* Passthrough authentication mode added to MariaDBAuth-module. See
 [authenticator documentation](mariadb-maxscale-25-01-authenticators/mariadb-maxscale-2501-maxscale-2501-mariadbmysql-authenticator.md) for more
 information.
* Added `<code>pam_mode=suid</code>` option to PamAuth module. This option separates the
 pam system library calls to a separate executable. See
 [authenticator documentation](mariadb-maxscale-25-01-authenticators/mariadb-maxscale-2501-maxscale-2501-pam-authenticator.md)
 for more information. test_pam_login tool updated to support this mode.
* Added `<code>disk_space_ok</code>` option to MariaDB Monitor settings `<code>master_conditions</code>`
 and `<code>slave_conditions</code>`. Enabled by default in `<code>master_conditions</code>`. See
 [monitor documentation](../mariadb-maxscale-21-06/README.md)
 for more information. Only available in MaxScale 23.08.5, 24.02.1 and later.


For more details, please refer to:


* [MariaDB MaxScale 23.08.9 Release Notes](https://mariadb.com/kb/en/Release-Notes/MaxScale-23.08.9-Release-Notes)
* [MariaDB MaxScale 23.08.8 Release Notes](https://mariadb.com/kb/en/Release-Notes/MaxScale-23.08.8-Release-Notes)
* [MariaDB MaxScale 23.08.7 Release Notes](https://mariadb.com/kb/en/Release-Notes/MaxScale-23.08.7-Release-Notes)
* [MariaDB MaxScale 23.08.6 Release Notes](Release-Notes/MaxScale-23.08.6-Release-Notes.md)
* [MariaDB MaxScale 23.08.5 Release Notes](Release-Notes/MaxScale-23.08.5-Release-Notes.md)
* [MariaDB MaxScale 23.08.4 Release Notes](Release-Notes/MaxScale-23.08.4-Release-Notes.md)
* [MariaDB MaxScale 23.08.3 Release Notes](Release-Notes/MaxScale-23.08.3-Release-Notes.md)
* [MariaDB MaxScale 23.08.2 Release Notes](Release-Notes/MaxScale-23.08.2-Release-Notes.md)
* [MariaDB MaxScale 23.08.1 Release Notes](Release-Notes/MaxScale-23.08.1-Release-Notes.md)
* [MariaDB MaxScale 23.08.0 Release Notes](Release-Notes/MaxScale-23.08.0-Release-Notes.md)


## MariaDB MaxScale 23.02


* A transition from the traditional master/slave terminology to the
 primary/replica terminology has been started. In the documentation
 and in the logging the transition has been made, but in configuration
 settings and command output the traditional terminology is still used.
 Conceptually, master/slave and primary/replica are completely
 interchangeable.
* MariaDB Monitor now preserves the MASTER_USE_GTID-setting of a replica when
 redirecting one during switchover and failover. When starting a new
 replication connection on a previous replica, Slave_Pos is used. When starting
 a new replication connection on a previous primary, Current_Pos is used.
* Added `<code>replication_custom_options</code>`-setting to both MariaDB Monitor and server.
 This setting enables e.g. setting SSL certificates for replication
 connections. See [MariaDB Monitor documentation](mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)
 for more information.
* Create-Backup and Restore-From-Backup commands added to MariaDBMonitor.
* The `<code>csmon</code>` and `<code>auroramon</code>` monitors that were deprecated in 22.08.2
 have been removed.
* The obsolete `<code>maxctrl drain</code>` command has been removed. Use `<code>maxctrl set server
 <name> drain</code>` to use the built-in draining mechanism.
* The `<code>maxctrl cluster</code>` commands have been removed. Use the built-in
 [configuration synchronization](mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
 to synchronize the configurations of multiple MaxScale instances.
* The REST-API is now supports ODBC-type connections in the `<code>/sql</code>`
 endpoints. For more information, refer to the SQL resource
 [documentation](mariadb-maxscale-25-01-rest-api/mariadb-maxscale-2501-maxscale-2501-sql-resource.md).
* The REST-API query endpoint now supports asynchronous query execution
 using the `<code>async=true</code>` option.
* The new `<code>/sql/:id/etl</code>` endpoints allow ETL operations to be done from
 ODBC data sources into MariaDB servers. For more information on the
 new API functions, refer to the SQL resource
 [documentation](mariadb-maxscale-25-01-rest-api/mariadb-maxscale-2501-maxscale-2501-sql-resource.md).
* The number of routing threads MaxScale uses can now be changed at runtime.
* The Audit-Log allows all REST-API calls to be logged.
* MaxScale now supports Xpand parallel replication streams that go through
 MaxScale.
* Authentication can now be enabled when Redis is used as the cache storage.
* SSL/TLS can now be used in the communication between MaxScale and Redis
 when Redis is used as the storage for the cache.
* Some Cache configuration parameters, most notable the rules, can now be
 changed at runtime.
* Support for inbound proxy protocol added.
* Ed25519Auth-plugin added. The plugin enables authentication with the
 MariaDB Server ed25519 authentication plugin.
* MaxGUI Query Editor has been renamed to "Workspace," and its internal storage
 key has been modified. As a result, the query history, snippets, and user
 preferences settings are restored to their default values.
* The redundant options for `<code>create server</code>` and `<code>create listener</code>` that were
 deprecated in 22.08 have been removed in MaxScale 23.02. The use of explicit
 options has been superseded by the use of `<code>key=value</code>` parameters in all
 `<code>create</code>` commands.


For more details, please refer to:


* [MariaDB MaxScale 23.02.13 Release Notes](https://mariadb.com/kb/en/Release-Notes/MaxScale-23.02.13-Release-Notes)
* [MariaDB MaxScale 23.02.12 Release Notes](https://mariadb.com/kb/en/Release-Notes/MaxScale-23.02.12-Release-Notes)
* [MariaDB MaxScale 23.02.11 Release Notes](https://mariadb.com/kb/en/Release-Notes/MaxScale-23.02.11-Release-Notes)
* [MariaDB MaxScale 23.02.10 Release Notes](Release-Notes/MaxScale-23.02.10-Release-Notes.md)
* [MariaDB MaxScale 23.02.9 Release Notes](Release-Notes/MaxScale-23.02.9-Release-Notes.md)
* [MariaDB MaxScale 23.02.8 Release Notes](Release-Notes/MaxScale-23.02.8-Release-Notes.md)
* [MariaDB MaxScale 23.02.7 Release Notes](Release-Notes/MaxScale-23.02.7-Release-Notes.md)
* [MariaDB MaxScale 23.02.6 Release Notes](Release-Notes/MaxScale-23.02.6-Release-Notes.md)
* [MariaDB MaxScale 23.02.5 Release Notes](Release-Notes/MaxScale-23.02.5-Release-Notes.md)
* [MariaDB MaxScale 23.02.4 Release Notes](Release-Notes/MaxScale-23.02.4-Release-Notes.md)
* [MariaDB MaxScale 23.02.3 Release Notes](Release-Notes/MaxScale-23.02.3-Release-Notes.md)
* [MariaDB MaxScale 23.02.2 Release Notes](Release-Notes/MaxScale-23.02.2-Release-Notes.md)
* [MariaDB MaxScale 23.02.1 Release Notes](Release-Notes/MaxScale-23.02.1-Release-Notes.md)
* [MariaDB MaxScale 23.02.0 Release Notes](Release-Notes/MaxScale-23.02.0-Release-Notes.md)


## MariaDB MaxScale 22.08


* Sessions can now be restarted so that added server are taken into use.
* Sessions can now be killed using maxctrl.
* MariaDBMonitor can use Mariabackup to clone the contents of a server.
* MariaDBMonitor can issue ColumnStore commands similar to CSMon
* MariaDBMonitor settings `<code>ignore_external_masters</code>`, `<code>detect_replication_lag</code>`
`<code>detect_standalone_master</code>`, `<code>detect_stale_master</code>` and `<code>detect_stale_slave</code>`
 have been removed. The first two were ineffective, the latter three are
 replaced by `<code>master_conditions</code>` and `<code>slave_conditions</code>`.
* A new Query Rewrite filter, using which queries can be rewritten based
 upon a template, has been added.
* MaxScale no longer logs to both the SystemD journal and MaxScale log by
 default: the default value of `<code>syslog</code>` was changed from `<code>true</code>` to `<code>false</code>` to
 reduce the amount of redundant log messages that are logged. To retain the old
 behavior of logging to both MaxScale's own files and to the SystemD journal,
 add `<code>syslog=true</code>` under the `<code>[maxscale]</code>` section.
* The `<code>dbfwfilter</code>` module that was deprecated in version 6 has now been removed.
* MaxGUI Query Editor has changed the type of browser storage from local storage
 to IndexedDB. As the result, query history, favorite, and configuration are reset.
 Apart from that, query favorite was renamed to query snippets allowing to quickly
 insert the query to the editor by typing its prefix. See MaxGUI tutorial
 [Using-MaxGUI-Tutorial](mariadb-maxscale-25-01-tutorials/mariadb-maxscale-2501-maxscale-2501-using-maxgui-tutorial.md)
* The Xpand monitor now handles group change explicitly.
* The `<code>Maintenance|Drain</code>` state of a server is now synchronized between multiple
 MaxScale instances if configuration synchronization is enabled.
* Causal reads now supported in a multi-MaxScale setup.
* The `<code>csmon</code>` and `<code>auroramon</code>` monitors are deprecated in 22.08.2 and will be
 removed in 23.02.0.


For more details, please refer to:


* [MariaDB MaxScale 22.08.16 Release Notes](https://mariadb.com/kb/en/Release-Notes/MaxScale-22.08.16-Release-Notes)
* [MariaDB MaxScale 22.08.15 Release Notes](https://mariadb.com/kb/en/Release-Notes/MaxScale-22.08.15-Release-Notes)
* [MariaDB MaxScale 22.08.14 Release Notes](https://mariadb.com/kb/en/Release-Notes/MaxScale-22.08.14-Release-Notes)
* [MariaDB MaxScale 22.08.13 Release Notes](Release-Notes/MaxScale-22.08.13-Release-Notes.md)
* [MariaDB MaxScale 22.08.12 Release Notes](Release-Notes/MaxScale-22.08.12-Release-Notes.md)
* [MariaDB MaxScale 22.08.11 Release Notes](Release-Notes/MaxScale-22.08.11-Release-Notes.md)
* [MariaDB MaxScale 22.08.10 Release Notes](Release-Notes/MaxScale-22.08.10-Release-Notes.md)
* [MariaDB MaxScale 22.08.9 Release Notes](Release-Notes/MaxScale-22.08.9-Release-Notes.md)
* [MariaDB MaxScale 22.08.8 Release Notes](Release-Notes/MaxScale-22.08.8-Release-Notes.md)
* [MariaDB MaxScale 22.08.7 Release Notes](Release-Notes/MaxScale-22.08.7-Release-Notes.md)
* [MariaDB MaxScale 22.08.6 Release Notes](Release-Notes/MaxScale-22.08.6-Release-Notes.md)
* [MariaDB MaxScale 22.08.5 Release Notes](Release-Notes/MaxScale-22.08.5-Release-Notes.md)
* [MariaDB MaxScale 22.08.4 Release Notes](Release-Notes/MaxScale-22.08.4-Release-Notes.md)
* [MariaDB MaxScale 22.08.3 Release Notes](Release-Notes/MaxScale-22.08.3-Release-Notes.md)
* [MariaDB MaxScale 22.08.2 Release Notes](Release-Notes/MaxScale-22.08.2-Release-Notes.md)
* [MariaDB MaxScale 22.08.1 Release Notes](Release-Notes/MaxScale-22.08.1-Release-Notes.md)
* [MariaDB MaxScale 22.08.0 Release Notes](Release-Notes/MaxScale-22.08.0-Release-Notes.md)


## MariaDB MaxScale 21.06


**NOTE** MaxScale 6.4 was renamed to 21.06 in May 2024. Thus, what would have
been released as 6.4.16 in June, was released as 21.06.16. The purpose of this
change is to make the versioning scheme used by all MaxScale series
identical. 21.06 denotes the year and month when the first 6 release was made.


* Added `<code>multiplex_timeout</code>`. It sets the time a session can wait
 for a backend connection to become available when using connection sharing
 (i.e. `<code>idle_session_pool_time</code>`).
* The `<code>hintrouter</code>` module was removed in MaxScale 21.06.18. The module was non-functional.


For more details, please refer to:


* [MariaDB MaxScale 21.06.19 Release Notes](https://mariadb.com/kb/en/Release-Notes/MaxScale-21.06.19-Release-Notes)
* [MariaDB MaxScale 21.06.18 Release Notes](https://mariadb.com/kb/en/Release-Notes/MaxScale-21.06.18-Release-Notes)
* [MariaDB MaxScale 21.06.17 Release Notes](https://mariadb.com/kb/en/Release-Notes/MaxScale-21.06.17-Release-Notes)
* [MariaDB MaxScale 21.06.16 Release Notes](Release-Notes/MaxScale-21.06.16-Release-Notes.md)
* [MariaDB MaxScale 6.4.15 Release Notes](Release-Notes/MaxScale-6.4.15-Release-Notes.md)
* [MariaDB MaxScale 6.4.14 Release Notes](Release-Notes/MaxScale-6.4.14-Release-Notes.md)
* [MariaDB MaxScale 6.4.13 Release Notes](Release-Notes/MaxScale-6.4.13-Release-Notes.md)
* [MariaDB MaxScale 6.4.12 Release Notes](Release-Notes/MaxScale-6.4.12-Release-Notes.md)
* [MariaDB MaxScale 6.4.11 Release Notes](Release-Notes/MaxScale-6.4.11-Release-Notes.md)
* [MariaDB MaxScale 6.4.10 Release Notes](Release-Notes/MaxScale-6.4.10-Release-Notes.md)
* [MariaDB MaxScale 6.4.9 Release Notes](Release-Notes/MaxScale-6.4.9-Release-Notes.md)
* [MariaDB MaxScale 6.4.8 Release Notes](Release-Notes/MaxScale-6.4.8-Release-Notes.md)
* [MariaDB MaxScale 6.4.7 Release Notes](Release-Notes/MaxScale-6.4.7-Release-Notes.md)
* [MariaDB MaxScale 6.4.6 Release Notes](Release-Notes/MaxScale-6.4.6-Release-Notes.md)
* [MariaDB MaxScale 6.4.5 Release Notes](Release-Notes/MaxScale-6.4.5-Release-Notes.md)
* [MariaDB MaxScale 6.4.4 Release Notes](Release-Notes/MaxScale-6.4.4-Release-Notes.md)
* [MariaDB MaxScale 6.4.3 Release Notes](Release-Notes/MaxScale-6.4.3-Release-Notes.md)
* [MariaDB MaxScale 6.4.2 Release Notes](Release-Notes/MaxScale-6.4.2-Release-Notes.md)
* [MariaDB MaxScale 6.4.1 Release Notes](Release-Notes/MaxScale-6.4.1-Release-Notes.md)
* [MariaDB MaxScale 6.4.0 Release Notes](Release-Notes/MaxScale-6.4.0-Release-Notes.md)


## MariaDB MaxScale 6.3


* Nosqlprotocol now supports both SSL and authentication.
* A large number of client connections can now share a smaller number of
 backend connections.
* MaxGUI now shows which MaxScale node is in control when cooperative monitoring
 is enabled.
* Filtering can now be used in the KafkaCDC router.
* The user is now informed if runtime changes are made to configuration objects
 that are defined in static configuration files.


For more details, please refer to:


* [MariaDB MaxScale 6.3.1 Release Notes](Release-Notes/MaxScale-6.3.1-Release-Notes.md)
* [MariaDB MaxScale 6.3.0 Release Notes](Release-Notes/MaxScale-6.3.0-Release-Notes.md)


## MariaDB MaxScale 6.2


* Significant improvements and feature additions to MaxGUI
* Significant improvements to nosqlprotocol
* Transaction Performance Monitoring Filter functionality moved to Qlafilter
* Most filters can now be reconfigured at runtime
* Synchronous mode for the Tee filter
* New `<code>list queries</code>` command for MaxCtrl that lists all active queries
* MaxScale can read client user accounts from a file and map them to backend
 users. See service setting
 [user_accounts_file](mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
 and listener setting
 [user_mapping_file](mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
 for more information.


For more details, please refer to:


* [MariaDB MaxScale 6.2.4 Release Notes](Release-Notes/MaxScale-6.2.4-Release-Notes.md)
* [MariaDB MaxScale 6.2.3 Release Notes](Release-Notes/MaxScale-6.2.3-Release-Notes.md)
* [MariaDB MaxScale 6.2.2 Release Notes](Release-Notes/MaxScale-6.2.2-Release-Notes.md)
* [MariaDB MaxScale 6.2.1 Release Notes](Release-Notes/MaxScale-6.2.1-Release-Notes.md)
* [MariaDB MaxScale 6.2.0 Release Notes](Release-Notes/MaxScale-6.2.0-Release-Notes.md)


## MariaDB MaxScale 6.1


* The versioning scheme has changed; earlier this would have been version 2.6.
* A `<code>nosqlprotocol</code>` protocol module that implements the MongoDB® wire protocol
 has been introduced.
* The Columnstore monitor is now exclusively intended for Columnstore version 1.5.
* The Columnstore monitor can now automatically adapt to changes in the cluster
 configuration.
* The Database Firewall filter has been deprecated.
* If extra_port is defined for a server, it's used by default for monitor and
user account manager connections. Normal port is used if the extra-port
connection fails due to too low extra_max_connections-setting on the backend.
* The deprecated `<code>required</code>` and `<code>disabled</code>` values for the `<code>ssl</code>` parameter have been removed.
* Backend connection multiplexing added. See
[idle_session_pool_time](mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
for more information.
* Defaults for `<code>maxctrl</code>` can now be specified in the file `<code>~/maxctrl.cnf</code>`
* PAM Authenticator can map PAM users to MariaDB users.
* MariaDB-Monitor can launch monitor script when slave server exceeds replication
lag limit (`<code>script_max_replication_lag</code>`).
* MariaDB-Monitor can disable read_only on master server
(`<code>enforce_writable_master</code>`).
* A graphical user interface SQL queries tool for writing, running SQL queries and visualizing
the results has been introduced.


For more details, please refer to:


* [MariaDB MaxScale 6.1.4 Release Notes](Release-Notes/MaxScale-6.1.4-Release-Notes.md)
* [MariaDB MaxScale 6.1.3 Release Notes](Release-Notes/MaxScale-6.1.3-Release-Notes.md)
* [MariaDB MaxScale 6.1.2 Release Notes](Release-Notes/MaxScale-6.1.2-Release-Notes.md)
* [MariaDB MaxScale 6.1.1 Release Notes](Release-Notes/MaxScale-6.1.1-Release-Notes.md)
* [MariaDB MaxScale 6.1.0 Release Notes](Release-Notes/MaxScale-6.1.0-Release-Notes.md)
* [MariaDB MaxScale 6.0.0 Release Notes](Release-Notes/MaxScale-6.0.0-Release-Notes.md)


## MariaDB MaxScale 2.5


* MaxAdmin has been removed.
* MaxGUI, a new browser based tool for configuring and managing
 MaxScale is introduced.
* MaxInfo-router and the related httpd-protocol have been removed.
* Server weights have been removed.
* Services can now directly route to other services with the help of the
 [target](mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md) parameter.
* Server parameters protocol and authenticator have been deprecated. Any
 definitions are ignored.
* Listeners support multiple authenticators.
* The replication lag of a slave server must now be less than
 [max_slave_replication_lag](mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-readwritesplit.md)
 whereas in older versions the replication lag had to be less than or
 equal to the configured limit.
* The global settings auth_read_timeout and auth_write_timeout have been
 deprecated. Any definitions are ignored.
* The Columnstore monitor is now capable of monitoring Columnstore 1.5 in
 addition to 1.0 and 1.2.
* MariaDB-Monitor supports cooperative monitoring. See
 [cooperative monitoring](mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)
 for more information.
* The MaxScale cache can now be shared between two MaxScale instances,
 in which case either memcached or Redis can be used as cache storage.
 Further, the cache can now also perform table level invalidations
 and be specific to a particular user.
* A completely new binlog router implementation.
* New routers, [mirror](mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-mirror.md) and [kafkacdc](mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkacdc.md).
* Service-to-service routing is now possible with the `<code>targets</code>` parameter.
* TLS CRL and peer host verification support.
* Multiple modes of operation for `<code>causal_reads</code>`.


For more details, please refer to:


* [MariaDB MaxScale 2.5.29 Release Notes](Release-Notes/MaxScale-2.5.29-Release-Notes.md)
* [MariaDB MaxScale 2.5.28 Release Notes](Release-Notes/MaxScale-2.5.28-Release-Notes.md)
* [MariaDB MaxScale 2.5.27 Release Notes](Release-Notes/MaxScale-2.5.27-Release-Notes.md)
* [MariaDB MaxScale 2.5.26 Release Notes](Release-Notes/MaxScale-2.5.26-Release-Notes.md)
* [MariaDB MaxScale 2.5.25 Release Notes](Release-Notes/MaxScale-2.5.25-Release-Notes.md)
* [MariaDB MaxScale 2.5.24 Release Notes](Release-Notes/MaxScale-2.5.24-Release-Notes.md)
* [MariaDB MaxScale 2.5.23 Release Notes](Release-Notes/MaxScale-2.5.23-Release-Notes.md)
* [MariaDB MaxScale 2.5.22 Release Notes](Release-Notes/MaxScale-2.5.22-Release-Notes.md)
* [MariaDB MaxScale 2.5.21 Release Notes](Release-Notes/MaxScale-2.5.21-Release-Notes.md)
* [MariaDB MaxScale 2.5.20 Release Notes](Release-Notes/MaxScale-2.5.20-Release-Notes.md)
* [MariaDB MaxScale 2.5.19 Release Notes](Release-Notes/MaxScale-2.5.19-Release-Notes.md)
* [MariaDB MaxScale 2.5.18 Release Notes](Release-Notes/MaxScale-2.5.18-Release-Notes.md)
* [MariaDB MaxScale 2.5.17 Release Notes](Release-Notes/MaxScale-2.5.17-Release-Notes.md)
* [MariaDB MaxScale 2.5.16 Release Notes](Release-Notes/MaxScale-2.5.16-Release-Notes.md)
* [MariaDB MaxScale 2.5.15 Release Notes](Release-Notes/MaxScale-2.5.15-Release-Notes.md)
* [MariaDB MaxScale 2.5.14 Release Notes](Release-Notes/MaxScale-2.5.14-Release-Notes.md)
* [MariaDB MaxScale 2.5.13 Release Notes](Release-Notes/MaxScale-2.5.13-Release-Notes.md)
* [MariaDB MaxScale 2.5.12 Release Notes](Release-Notes/MaxScale-2.5.12-Release-Notes.md)
* [MariaDB MaxScale 2.5.11 Release Notes](Release-Notes/MaxScale-2.5.11-Release-Notes.md)
* [MariaDB MaxScale 2.5.10 Release Notes](Release-Notes/MaxScale-2.5.10-Release-Notes.md)
* [MariaDB MaxScale 2.5.9 Release Notes](Release-Notes/MaxScale-2.5.9-Release-Notes.md)
* [MariaDB MaxScale 2.5.8 Release Notes](Release-Notes/MaxScale-2.5.8-Release-Notes.md)
* [MariaDB MaxScale 2.5.7 Release Notes](Release-Notes/MaxScale-2.5.7-Release-Notes.md)
* [MariaDB MaxScale 2.5.6 Release Notes](Release-Notes/MaxScale-2.5.6-Release-Notes.md)
* [MariaDB MaxScale 2.5.5 Release Notes](Release-Notes/MaxScale-2.5.5-Release-Notes.md)
* [MariaDB MaxScale 2.5.4 Release Notes](Release-Notes/MaxScale-2.5.4-Release-Notes.md)
* [MariaDB MaxScale 2.5.3 Release Notes](Release-Notes/MaxScale-2.5.3-Release-Notes.md)
* [MariaDB MaxScale 2.5.2 Release Notes](Release-Notes/MaxScale-2.5.2-Release-Notes.md)
* [MariaDB MaxScale 2.5.1 Release Notes](Release-Notes/MaxScale-2.5.1-Release-Notes.md)
* [MariaDB MaxScale 2.5.0 Release Notes](Release-Notes/MaxScale-2.5.0-Release-Notes.md)


## MariaDB MaxScale 2.4


* A Clustrix specific monitor has been added.
* A new router, Smart Router, capable of routing a query to different
 backends depending on the characteristics of the query has been added.
* Transaction replaying is now performed also in conjunction with server
 initiated transaction rollbacks.
* Names starting with `<code>@@</code>` are reserved for use by MaxScale.
* Names can no longer contain whitespace.
* Servers can now be drained.
* The servers of a service can now be defined using a monitor.
* Durations can now be specified as hours, minutes, seconds or milliseconds.
* MaxCtrl commands `<code>list sessions</code>`, `<code>show sessions</code>` and `<code>show session <id></code>`
 support reverse DNS lookup of client addresses. The conversion is activated
 by adding the `<code>--rdns</code>`-option to the command.
* The following MariaDB-Monitor settings have been removed and cause a startup error
 if defined: `<code>mysql51_replication</code>`, `<code>multimaster</code>` and `<code>allow_cluster_recovery</code>`. The
 setting `<code>detect_replication_lag</code>` is deprecated and ignored.
* `<code>enforce_simple_topology</code>`-setting added to MariaDB-Monitor.
* The mqfilter has been deprecated.


For more details, please refer to:


* [MariaDB MaxScale 2.4.19 Release Notes](Release-Notes/MaxScale-2.4.19-Release-Notes.md)
* [MariaDB MaxScale 2.4.18 Release Notes](Release-Notes/MaxScale-2.4.18-Release-Notes.md)
* [MariaDB MaxScale 2.4.17 Release Notes](Release-Notes/MaxScale-2.4.17-Release-Notes.md)
* [MariaDB MaxScale 2.4.16 Release Notes](Release-Notes/MaxScale-2.4.16-Release-Notes.md)
* [MariaDB MaxScale 2.4.15 Release Notes](Release-Notes/MaxScale-2.4.15-Release-Notes.md)
* [MariaDB MaxScale 2.4.14 Release Notes](Release-Notes/MaxScale-2.4.14-Release-Notes.md)
* [MariaDB MaxScale 2.4.13 Release Notes](Release-Notes/MaxScale-2.4.13-Release-Notes.md)
* [MariaDB MaxScale 2.4.12 Release Notes](Release-Notes/MaxScale-2.4.12-Release-Notes.md)
* [MariaDB MaxScale 2.4.11 Release Notes](Release-Notes/MaxScale-2.4.11-Release-Notes.md)
* [MariaDB MaxScale 2.4.10 Release Notes](Release-Notes/MaxScale-2.4.10-Release-Notes.md)
* [MariaDB MaxScale 2.4.9 Release Notes](Release-Notes/MaxScale-2.4.9-Release-Notes.md)
* [MariaDB MaxScale 2.4.8 Release Notes](Release-Notes/MaxScale-2.4.8-Release-Notes.md)
* [MariaDB MaxScale 2.4.7 Release Notes](Release-Notes/MaxScale-2.4.7-Release-Notes.md)
* [MariaDB MaxScale 2.4.6 Release Notes](Release-Notes/MaxScale-2.4.6-Release-Notes.md)
* [MariaDB MaxScale 2.4.5 Release Notes](Release-Notes/MaxScale-2.4.5-Release-Notes.md)
* [MariaDB MaxScale 2.4.4 Release Notes](Release-Notes/MaxScale-2.4.4-Release-Notes.md)
* [MariaDB MaxScale 2.4.3 Release Notes](Release-Notes/MaxScale-2.4.3-Release-Notes.md)
* [MariaDB MaxScale 2.4.2 Release Notes](Release-Notes/MaxScale-2.4.2-Release-Notes.md)
* [MariaDB MaxScale 2.4.1 Release Notes](Release-Notes/MaxScale-2.4.1-Release-Notes.md)
* [MariaDB MaxScale 2.4.0 Release Notes](Release-Notes/MaxScale-2.4.0-Release-Notes.md)


## MariaDB MaxScale 2.3


* Runtime Configuration of the Cache
* User Specified Syslog Facility and Level for Authentication Errors
* `<code>config reload</code>` removed from MaxAdmin (was deprecated in 2.2)
* MariaDBMonitor features added, modified and removed
* A Comment filter has been added.
* Services and filters can be created at runtime via the REST API
* Runtime router reconfiguration is now possible
* New Throttle filter that replaces and extends on the limit_queries functionality
* MaxCtrl
* The `<code>create monitor</code>` command now accepts a list of key-value parameters
* The new `<code>drain server</code>` drains the server of connections
* A new interactive input mode was added
* Readwritesplit
* Automatic transaction replay allows transactions to be migrated between servers
* Master connections can now be re-opened
* Writes with autocommit enabled can be automatically retried
* Consistent reads on slaves via MASTER_GTID_WAIT
* Transaction load balancing for normal transactions
* Support for runtime router reconfiguration
* A new load balancing method: ADAPTIVE_ROUTING
* Experimental resultset concatenation router, `<code>cat</code>`
* The schema router is now capable of table family sharding.
* The binlog router can now automatically switch to secondary masters
 when replicating from a Galera cluster in case the primary master
 goes down.
* MaxScale now has a systemd compatible watchdog.
* Server setting `<code>authenticator_options</code>` is no longer used and any value is
 ignored.


For more details, please refer to:


* [MariaDB MaxScale 2.3.20 Release Notes](Release-Notes/MaxScale-2.3.20-Release-Notes.md)
* [MariaDB MaxScale 2.3.19 Release Notes](Release-Notes/MaxScale-2.3.19-Release-Notes.md)
* [MariaDB MaxScale 2.3.18 Release Notes](Release-Notes/MaxScale-2.3.18-Release-Notes.md)
* [MariaDB MaxScale 2.3.17 Release Notes](Release-Notes/MaxScale-2.3.17-Release-Notes.md)
* [MariaDB MaxScale 2.3.16 Release Notes](Release-Notes/MaxScale-2.3.16-Release-Notes.md)
* [MariaDB MaxScale 2.3.15 Release Notes](Release-Notes/MaxScale-2.3.15-Release-Notes.md)
* [MariaDB MaxScale 2.3.14 Release Notes](Release-Notes/MaxScale-2.3.14-Release-Notes.md)
* [MariaDB MaxScale 2.3.13 Release Notes](Release-Notes/MaxScale-2.3.13-Release-Notes.md)
* [MariaDB MaxScale 2.3.12 Release Notes](Release-Notes/MaxScale-2.3.12-Release-Notes.md)
* [MariaDB MaxScale 2.3.11 Release Notes](Release-Notes/MaxScale-2.3.11-Release-Notes.md)
* [MariaDB MaxScale 2.3.10 Release Notes](Release-Notes/MaxScale-2.3.10-Release-Notes.md)
* [MariaDB MaxScale 2.3.9 Release Notes](Release-Notes/MaxScale-2.3.9-Release-Notes.md)
* [MariaDB MaxScale 2.3.8 Release Notes](Release-Notes/MaxScale-2.3.8-Release-Notes.md)
* [MariaDB MaxScale 2.3.7 Release Notes](Release-Notes/MaxScale-2.3.7-Release-Notes.md)
* [MariaDB MaxScale 2.3.6 Release Notes](Release-Notes/MaxScale-2.3.6-Release-Notes.md)
* [MariaDB MaxScale 2.3.5 Release Notes](Release-Notes/MaxScale-2.3.5-Release-Notes.md)
* [MariaDB MaxScale 2.3.4 Release Notes](Release-Notes/MaxScale-2.3.4-Release-Notes.md)
* [MariaDB MaxScale 2.3.3 Release Notes](Release-Notes/MaxScale-2.3.3-Release-Notes.md)
* [MariaDB MaxScale 2.3.2 Release Notes](Release-Notes/MaxScale-2.3.2-Release-Notes.md)
* [MariaDB MaxScale 2.3.1 Release Notes](Release-Notes/MaxScale-2.3.1-Release-Notes.md)
* [MariaDB MaxScale 2.3.0 Release Notes](Release-Notes/MaxScale-2.3.0-Release-Notes.md)


## MariaDB MaxScale 2.2


* Limited support from Pluggable Authentication Modules (PAM).
* Proxy protocol support for backend connections.
* REST-API for obtaining information about and for manipulating the
 resources of MaxScale.
* MaxCtrl, a new command line client for administering MaxScale
 implemented in terms of the REST-API.
* Firewall can now prevent the use of functions in conjunction with
 certain columns.
* Parser of MaxScale extended to support window functions and CTEs.
* Parser of MaxScale extended to support PL/SQL compatibility features
 of upcoming 10.3 release.
* Prepared statements are now parsed and the execution of read only
 ones will be routed to slaves.
* Server states are persisted, so in case of crash and restart MaxScale
 has the correct server state quicker.
* Monitor scripts are executed synchronously, so they can safely perform
 actions that change the server states.
* The Masking filter can now both obfuscate and partially mask columns.
* Binlog router supports MariaDB 10 GTID at both ends.
* KILL CONNECTION can now be used through MaxScale.
* Environment variables can now be used in the MaxScale configuration file.
* By default, MaxScale can no longer be run as root.
* The MySQL Monitor is now capable of performing failover and switchover of
 the master. There is also limited capability for rejoining nodes.


For more details, please refer to:


* [MariaDB MaxScale 2.2.21 Release Notes](Release-Notes/MaxScale-2.2.21-Release-Notes.md)
* [MariaDB MaxScale 2.2.20 Release Notes](Release-Notes/MaxScale-2.2.20-Release-Notes.md)
* [MariaDB MaxScale 2.2.19 Release Notes](Release-Notes/MaxScale-2.2.19-Release-Notes.md)
* [MariaDB MaxScale 2.2.18 Release Notes](Release-Notes/MaxScale-2.2.18-Release-Notes.md)
* [MariaDB MaxScale 2.2.17 Release Notes](Release-Notes/MaxScale-2.2.17-Release-Notes.md)
* [MariaDB MaxScale 2.2.16 Release Notes](Release-Notes/MaxScale-2.2.16-Release-Notes.md)
* [MariaDB MaxScale 2.2.15 Release Notes](Release-Notes/MaxScale-2.2.15-Release-Notes.md)
* [MariaDB MaxScale 2.2.14 Release Notes](Release-Notes/MaxScale-2.2.14-Release-Notes.md)
* [MariaDB MaxScale 2.2.13 Release Notes](Release-Notes/MaxScale-2.2.13-Release-Notes.md)
* [MariaDB MaxScale 2.2.12 Release Notes](Release-Notes/MaxScale-2.2.12-Release-Notes.md)
* [MariaDB MaxScale 2.2.11 Release Notes](Release-Notes/MaxScale-2.2.11-Release-Notes.md)
* [MariaDB MaxScale 2.2.10 Release Notes](Release-Notes/MaxScale-2.2.10-Release-Notes.md)
* [MariaDB MaxScale 2.2.9 Release Notes](Release-Notes/MaxScale-2.2.9-Release-Notes.md)
* [MariaDB MaxScale 2.2.8 Release Notes](Release-Notes/MaxScale-2.2.8-Release-Notes.md)
* [MariaDB MaxScale 2.2.7 Release Notes](Release-Notes/MaxScale-2.2.7-Release-Notes.md)
* [MariaDB MaxScale 2.2.6 Release Notes](Release-Notes/MaxScale-2.2.6-Release-Notes.md)
* [MariaDB MaxScale 2.2.5 Release Notes](Release-Notes/MaxScale-2.2.5-Release-Notes.md)
* [MariaDB MaxScale 2.2.4 Release Notes](Release-Notes/MaxScale-2.2.4-Release-Notes.md)
* [MariaDB MaxScale 2.2.3 Release Notes](Release-Notes/MaxScale-2.2.3-Release-Notes.md)
* [MariaDB MaxScale 2.2.2 Release Notes](Release-Notes/MaxScale-2.2.2-Release-Notes.md)
* [MariaDB MaxScale 2.2.1 Release Notes](Release-Notes/MaxScale-2.2.1-Release-Notes.md)
* [MariaDB MaxScale 2.2.0 Release Notes](Release-Notes/MaxScale-2.2.0-Release-Notes.md)


## MariaDB MaxScale 2.1


* MariaDB MaxScale is licensed under MariaDB BSL 1.1.
* Hierarchical configuration files are now supported.
* Logging is now performed in a way compatible with logrotate(8).
* Persistent connections are reset upon reuse.
* Galera monitor now consistently chooses the same node as master.
* Galera Monitor can set the preferred donor nodes list.
* The configuration can now be altered dynamically and the changes are persisted.
* There is now a monitor for Amazon Aurora clusters.
* MySQL Monitor now has a multi-master mode.
* MySQL Monitor now has a failover mode.
* Named Server Filter now supports wildcards for source option.
* Binlog Server can now be configured to encrypt binlog files.
* New filters, cache, ccrfilter, insertstream, masking, and maxrows are introduced.
* GSSAPI based authentication can be used
* Prepared statements are now in the database firewall filtered exactly like non-prepared
 statements.
* The firewall filter can now filter based on function usage.
* MaxScale now supports IPv6


For more details, please refer to:


* [MariaDB MaxScale 2.1.17 Release Notes](Release-Notes/MaxScale-2.1.17-Release-Notes.md)
* [MariaDB MaxScale 2.1.16 Release Notes](Release-Notes/MaxScale-2.1.16-Release-Notes.md)
* [MariaDB MaxScale 2.1.15 Release Notes](Release-Notes/MaxScale-2.1.15-Release-Notes.md)
* [MariaDB MaxScale 2.1.14 Release Notes](Release-Notes/MaxScale-2.1.14-Release-Notes.md)
* [MariaDB MaxScale 2.1.13 Release Notes](Release-Notes/MaxScale-2.1.13-Release-Notes.md)
* [MariaDB MaxScale 2.1.12 Release Notes](Release-Notes/MaxScale-2.1.12-Release-Notes.md)
* [MariaDB MaxScale 2.1.11 Release Notes](Release-Notes/MaxScale-2.1.11-Release-Notes.md)
* [MariaDB MaxScale 2.1.10 Release Notes](Release-Notes/MaxScale-2.1.10-Release-Notes.md)
* [MariaDB MaxScale 2.1.9 Release Notes](Release-Notes/MaxScale-2.1.9-Release-Notes.md)
* [MariaDB MaxScale 2.1.8 Release Notes](Release-Notes/MaxScale-2.1.8-Release-Notes.md)
* [MariaDB MaxScale 2.1.7 Release Notes](Release-Notes/MaxScale-2.1.7-Release-Notes.md)
* [MariaDB MaxScale 2.1.6 Release Notes](Release-Notes/MaxScale-2.1.6-Release-Notes.md)
* [MariaDB MaxScale 2.1.5 Release Notes](Release-Notes/MaxScale-2.1.5-Release-Notes.md)
* [MariaDB MaxScale 2.1.4 Release Notes](Release-Notes/MaxScale-2.1.4-Release-Notes.md)
* [MariaDB MaxScale 2.1.3 Release Notes](Release-Notes/MaxScale-2.1.3-Release-Notes.md)
* [MariaDB MaxScale 2.1.2 Release Notes](Release-Notes/MaxScale-2.1.2-Release-Notes.md)
* [MariaDB MaxScale 2.1.1 Release Notes](Release-Notes/MaxScale-2.1.1-Release-Notes.md)
* [MariaDB MaxScale 2.1.0 Release Notes](Release-Notes/MaxScale-2.1.0-Release-Notes.md)


## MariaDB MaxScale 2.0


* MariaDB MaxScale is licensed under MariaDB BSL.
* SSL can be used in the communication between MariaDB MaxScale and the backend servers.
* The number of allowed connections can explicitly be throttled.
* MariaDB MaxScale can continue serving read request even if the master has gone down.
* The security of MaxAdmin has been improved; Unix domain sockets can be used in the
 communication with MariaDB MaxScale and the Linux identity can be used for authorization.
* MariaDB MaxScale can in real time make binlog events available as raw AVRO or
 as JSON objects (beta level functionality).


For more details, please refer to:


* [MariaDB MaxScale 2.0.6 Release Notes](Release-Notes/MaxScale-2.0.6-Release-Notes.md)
* [MariaDB MaxScale 2.0.5 Release Notes](Release-Notes/MaxScale-2.0.5-Release-Notes.md)
* [MariaDB MaxScale 2.0.4 Release Notes](Release-Notes/MaxScale-2.0.4-Release-Notes.md)
* [MariaDB MaxScale 2.0.3 Release Notes](Release-Notes/MaxScale-2.0.3-Release-Notes.md)
* [MariaDB MaxScale 2.0.2 Release Notes](Release-Notes/MaxScale-2.0.2-Release-Notes.md)
* [MariaDB MaxScale 2.0.1 Release Notes](Release-Notes/MaxScale-2.0.1-Release-Notes.md)
* [MariaDB MaxScale 2.0.0 Release Notes](Release-Notes/MaxScale-2.0.0-Release-Notes.md)


## MariaDB MaxScale 1.4


* Authentication now allows table level resolution of grants. MaxScale service
 users will now need SELECT privileges on `<code>mysql.tables_priv</code>` to be able to
 authenticate users at the database and table level.
* Firewall filter allows whitelisting.
* Client side SSL works.


For more details, please refer to


* [MariaDB MaxScale 1.4.3 Release Notes](Release-Notes/MaxScale-1.4.3-Release-Notes.md)
* [MariaDB MaxScale 1.4.2 Release Notes](Release-Notes/MaxScale-1.4.2-Release-Notes.md)
* [MariaDB MaxScale 1.4.1 Release Notes](Release-Notes/MaxScale-1.4.1-Release-Notes.md)
* [MariaDB MaxScale 1.4.0 Release Notes](Release-Notes/MaxScale-1.4.0-Release-Notes.md).


## MariaDB MaxScale 1.3


* Added support for persistent backend connections
* The binlog server is now an integral component of MariaDB MaxScale.
* The logging has been changed; instead of different log files there is one log file and different message priorities.


For more details, please refer to [MariaDB MaxScale 1.3 Release Notes](Release-Notes/MaxScale-1.3.0-Release-Notes.md)


## MariaDB MaxScale 1.2


* Logfiles have been renamed. The log names are now named error.log, messages.log, trace.log and debug.log.


## MariaDB MaxScale 1.1.1


* Schemarouter now also allows for an upper limit to session commands.
* Schemarouter correctly handles SHOW DATABASES responses that span multiple buffers.
* Readwritesplit and Schemarouter now allow disabling of the session command history.


## MariaDB MaxScale 1.1


**NOTE:** MariaDB MaxScale default installation directory has changed to `<code>/usr/local/mariadb-maxscale</code>` and the default password for MaxAdmin is now ´mariadb´.


* New modules added

  * Binlog router
  * Firewall filter
  * Multi-Master monitor
  * RabbitMQ logging filter
  * Schema Sharding router
* Added option to use high precision timestamps in logging.
* Readwritesplit router now returns the master server's response.
* New readwritesplit router option added. It is now possible to control the amount of memory readwritesplit sessions will consume by limiting the amount of session modifying statements they can execute.
* Minimum required CMake version is now 2.8.12 for package building.
* Session idle timeout added for services. More details can be found in the configuration guide.
* Monitor API is updated to 2.0.0. Monitors with earlier versions of the API no longer work with this version of MariaDB MaxScale.
* MariaDB MaxScale now requires libcurl and libcurl development headers.
* Nagios plugins added.
* Notification service added.
* Readconnrouter has a new "running" router_option. This allows it to use any running server as a valid backend server.
* Database names can be stripped of escape characters with the `<code>strip_db_esc</code>` service parameter.
