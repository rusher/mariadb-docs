
# Upgrading from MariaDB 10.1 to MariaDB 10.2


### How to Upgrade


For Windows, see [Upgrading MariaDB on Windows](../upgrading-mariadb-on-windows.md) instead.


For MariaDB Galera Cluster, see [Upgrading from MariaDB 10.1 to MariaDB 10.2 with Galera Cluster](https://mariadb.com/kb/en/upgrading-from-mariadb-101-to-mariadb-102-with-galera-cluster) instead.


Before you upgrade, it would be best to take a backup of your database. This is always a good idea to do before an upgrade. We would recommend [Mariabackup](../../../backing-up-and-restoring-databases/mariabackup/README.md).



The suggested upgrade procedure is:


1. Modify the repository configuration, so the system's package manager installs [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/old-releases/release-notes-mariadb-10-2-series/what-is-mariadb-102). For example,

  * On Debian, Ubuntu, and other similar Linux distributions, see [Updating the MariaDB APT repository to a New Major Release](../../binary-packages/installing-mariadb-deb-files.md#updating-the-mariadb-apt-repository-to-a-new-major-release) for more information.
  * On RHEL, CentOS, Fedora, and other similar Linux distributions, see [Updating the MariaDB YUM repository to a New Major Release](../../binary-packages/rpm/yum.md#updating-the-mariadb-yum-repository-to-a-new-major-release) for more information.
  * On SLES, OpenSUSE, and other similar Linux distributions, see [Updating the MariaDB ZYpp repository to a New Major Release](../../binary-packages/rpm/installing-mariadb-with-zypper.md#updating-the-mariadb-zypp-repository-to-a-new-major-release) for more information.
1. Set `[innodb_fast_shutdown](../../../../reference/storage-engines/innodb/innodb-system-variables.md)` to `0`. It can be changed dynamically with `[SET GLOBAL](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/set-commands/set.md#global-session)`. For example: 
`SET GLOBAL innodb_fast_shutdown=0;`

  * This step is not necessary when upgrading to [MariaDB 10.2.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/old-releases/release-notes-mariadb-10-2-series/mariadb-1025-release-notes) or later. Omitting it can make the upgrade process far faster. See [MDEV-12289](https://jira.mariadb.org/browse/MDEV-12289) for more information.
1. [Stop MariaDB](../../starting-and-stopping-mariadb/starting-and-stopping-mariadb-automatically.md).
1. Uninstall the old version of MariaDB.

  * On Debian, Ubuntu, and other similar Linux distributions, execute the following: 
`sudo apt-get remove mariadb-server`
  * On RHEL, CentOS, Fedora, and other similar Linux distributions, execute the following: 
`sudo yum remove MariaDB-server`
  * On SLES, OpenSUSE, and other similar Linux distributions, execute the following: 
`sudo zypper remove MariaDB-server`
1. Install the new version of MariaDB.

  * On Debian, Ubuntu, and other similar Linux distributions, see [Installing MariaDB Packages with APT](../../binary-packages/installing-mariadb-deb-files.md#installing-mariadb-packages-with-apt) for more information.
  * On RHEL, CentOS, Fedora, and other similar Linux distributions, see [Installing MariaDB Packages with YUM](../../binary-packages/rpm/yum.md#installing-mariadb-packages-with-yum) for more information.
  * On SLES, OpenSUSE, and other similar Linux distributions, see [Installing MariaDB Packages with ZYpp](../../binary-packages/rpm/installing-mariadb-with-zypper.md#installing-mariadb-packages-with-zypp) for more information.
1. Make any desired changes to configuration options in [option files](../../configuring-mariadb-with-option-files.md), such as `my.cnf`. This includes removing any options that are no longer supported.
1. [Start MariaDB](../../starting-and-stopping-mariadb/starting-and-stopping-mariadb-automatically.md).
1. Run `[mysql_upgrade](../../../../clients-and-utilities/legacy-clients-and-utilities/mysql_upgrade.md)`.

  * `mysql_upgrade` does two things:

    1. Ensures that the system tables in the `[mysq](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/the-mysql-database-tables/README.md)l` database are fully compatible with the new version.
    1. Does a very quick check of all tables and marks them as compatible with the new version of MariaDB .


### Incompatible Changes Between 10.1 and 10.2


On most servers upgrading from 10.1 should be painless. However, there are some things that have changed which could affect an upgrade:


#### InnoDB Instead of XtraDB


[MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/old-releases/release-notes-mariadb-10-2-series/what-is-mariadb-102) uses [InnoDB](../../../../reference/storage-engines/innodb/README.md) as the default storage engine, rather than XtraDB, used in [MariaDB 10.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/changes-improvements-in-mariadb-10-1) and before. See [Why does MariaDB 10.2 use InnoDB instead of XtraDB?](/kb/en/why-does-mariadb-102-use-innodb-instead-of-xtradb/) In most cases this should have minimal effect as the latest InnoDB has incorporated most of the improvements made in earlier versions of XtraDB. Note that certain [XtraDB system variables](../../../../reference/storage-engines/innodb/innodb-system-variables.md) are now ignored (although they still exist so as to permit easy upgrading).


#### Options That Have Changed Default Values


In particular, take note of the changes to [innodb_strict_mode](../../../../reference/storage-engines/innodb/innodb-system-variables.md), [sql_mode](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#sql_mode), [binlog_format](../../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md), [binlog_checksum](../../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md) and [innodb_checksum_algorithm](../../../../reference/storage-engines/innodb/innodb-system-variables.md).



| Option | Old default value | New default value |
| --- | --- | --- |
| Option | Old default value | New default value |
| [aria_recover(_options)](../../../../reference/storage-engines/aria/aria-system-variables.md#aria_recover_options) | NORMAL | BACKUP, QUICK |
| [binlog_annotate_row_events](../../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md) | OFF | ON |
| [binlog_checksum](../../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md) | NONE | CRC32 |
| [binlog_format](../../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md) | STATEMENT | MIXED |
| [group_concat_max_len](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#group_concat_max_len) | 1024 | 1048576 |
| [innodb_autoinc_lock_mode](../../../../reference/storage-engines/innodb/innodb-system-variables.md) | 1 | 2 |
| [innodb_buffer_pool_dump_at_shutdown](../../../../reference/storage-engines/innodb/innodb-system-variables.md) | OFF | ON |
| [innodb_buffer_pool_dump_pct](../../../../reference/storage-engines/innodb/innodb-system-variables.md) | 100 | 25 |
| [innodb_buffer_pool_instances](../../../../reference/storage-engines/innodb/innodb-system-variables.md) | 8 | Varies |
| [innodb_buffer_pool_load_at_startup](../../../../reference/storage-engines/innodb/innodb-system-variables.md) | OFF | ON |
| [innodb_checksum_algorithm](../../../../reference/storage-engines/innodb/innodb-system-variables.md) | innodb | crc32 |
| [innodb_file_format](../../../../reference/storage-engines/innodb/innodb-system-variables.md) | Antelope | Barracuda |
| [innodb_large_prefix](../../../../reference/storage-engines/innodb/innodb-system-variables.md) | OFF | ON |
| [innodb_lock_schedule_algorithm](../../../../reference/storage-engines/innodb/innodb-system-variables.md) | VATS | FCFS |
| [innodb_log_compressed_pages](../../../../reference/storage-engines/innodb/innodb-system-variables.md) | OFF | ON |
| [innodb_max_dirty_pages_pct_lwm](../../../../reference/storage-engines/innodb/innodb-system-variables.md) | 0.001000 | 0 |
| [innodb_max_undo_log_size](../../../../reference/storage-engines/innodb/innodb-system-variables.md) | 1073741824 | 10485760 |
| [innodb_purge_threads](../../../../reference/storage-engines/innodb/innodb-system-variables.md) | 1 | 4 |
| [innodb_strict_mode](../../../../reference/storage-engines/innodb/innodb-system-variables.md) | OFF | ON |
| [innodb_undo_directory](../../../../reference/storage-engines/innodb/innodb-system-variables.md) | . | NULL |
| [innodb_use_atomic_writes](../../../../reference/storage-engines/innodb/innodb-system-variables.md) | OFF | ON |
| [innodb_use_trim](../../../../reference/storage-engines/innodb/innodb-system-variables.md) | OFF | ON |
| [lock_wait_timeout](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#lock_wait_timeout) | 31536000 | 86400 |
| [log_slow_admin_statements](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#log_slow_admin_statements) | OFF | ON |
| [log_slow_slave_statements](../../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md) | OFF | ON |
| [log_warnings](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#log_warnings) | 1 | 2 |
| [max_allowed_packet](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#max_allowed_packet) | 4M | 16M |
| [max_long_data_size](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#max_long_data_size) | 4M | 16M |
| [myisam_recover_options](../../../../reference/storage-engines/myisam-storage-engine/myisam-system-variables.md#myisam_recover_options) | NORMAL | BACKUP, QUICK |
| [optimizer_switch](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#optimizer_switch) | See [Optimizer Switch](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/query-optimizations/optimizer-switch.md) for details. |
| [replicate_annotate_row_events](../../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md) | OFF | ON |
| [server_id](../../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md) | 0 | 1 |
| [slave_net_timeout](../../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md) | 3600 | 60 |
| [sql_mode](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#sql_mode) | NO_AUTO_CREATE_USER, NO_ENGINE_SUBSTITUTION | STRICT_TRANS_TABLES, ERROR_FOR_DIVISION_BY_ZERO, NO_AUTO_CREATE_USER, NO_ENGINE_SUBSTITUTION |
| [thread_cache_size](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#thread_cache_size) | 0 | Auto |
| [thread_pool_max_threads](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/buffers-caches-and-threads/thread-pool/thread-pool-system-status-variables.md) | 1000 | 65536 |
| [thread_stack](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#thread_stack) | 295936 | 299008 |



#### Options That Have Been Removed or Renamed


The following options should be removed or renamed if you use them in your [option files](../../configuring-mariadb-with-option-files.md):



| Option | Reason |
| --- | --- |
| Option | Reason |
| aria_recover | Renamed to [aria_recover_options](../../../../reference/storage-engines/aria/aria-system-variables.md#aria_recover_options) to match [myisam_recover_options](../../../../reference/storage-engines/myisam-storage-engine/myisam-system-variables.md#myisam_recover_options). |
| [innodb_additional_mem_pool_size](../../../../reference/storage-engines/innodb/innodb-system-variables.md) | Deprecated in [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0). |
| [innodb_api_bk_commit_interval](../../../../reference/storage-engines/innodb/innodb-system-variables.md) | Memcache never implemented in MariaDB. |
| [innodb_api_disable_rowlock](../../../../reference/storage-engines/innodb/innodb-system-variables.md) | Memcache never implemented in MariaDB. |
| [innodb_api_enable_binlog](../../../../reference/storage-engines/innodb/innodb-system-variables.md) | Memcache never implemented in MariaDB. |
| [innodb_api_enable_mdl](../../../../reference/storage-engines/innodb/innodb-system-variables.md) | Memcache never implemented in MariaDB. |
| [|innodb_api_trx_level](../../../../reference/storage-engines/innodb/innodb-system-variables.md) | Memcache never implemented in MariaDB. |
| [innodb_use_sys_malloc](../../../../reference/storage-engines/innodb/innodb-system-variables.md) | Deprecated in [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0). |



#### Reserved Words


New [reserved words](../../../../reference/sql-statements-and-structure/sql-language-structure/reserved-words.md): OVER, RECURSIVE and ROWS. These can no longer be used as [identifiers](../../../../reference/sql-statements-and-structure/sql-language-structure/identifier-names.md) without being quoted.


#### TokuDB


[TokuDB](../../../../reference/storage-engines/tokudb/README.md) has been split into a separate package, mariadb-plugin-tokudb.


#### Replication


[Replication](../../../../server-usage/replication-cluster-multi-master/standard-replication/README.md) from legacy MySQL servers may require setting [binlog_checksum](../../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md) to NONE.


#### SQL Mode


[SQL_MODE](../../../variables-and-modes/sql-mode.md) has been changed; in particular, NOT NULL fields with no default will no longer fall back to a dummy value for inserts which do not specify a value for that field.


#### Auto_increment


[Auto_increment](../../../../reference/data-types/auto_increment.md) columns are no longer permitted in [CHECK constraints](../../../../reference/sql-statements-and-structure/sql-statements/data-definition/constraint.md), [DEFAULT value expressions](../../../../reference/sql-statements-and-structure/sql-statements/data-definition/create/create-table.md#default) and [virtual columns](../../../../reference/sql-statements-and-structure/sql-statements/data-definition/create/generated-columns.md). They were permitted in earlier versions, but did not work correctly.


#### TLS


Starting with [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/old-releases/release-notes-mariadb-10-2-series/what-is-mariadb-102), when the user specifies the `--ssl` option with a [client or utility](/kb/en/clients-utilities/), the [client or utility](/kb/en/clients-utilities/) will not [verify the server certificate](../../../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/secure-connections-overview.md#server-certificate-verification) by default. In order to verify the server certificate, the user must specify the `--ssl-verify-server-cert` option to the [client or utility](/kb/en/clients-utilities/). For more information, see the [list of options](../../../../clients-and-utilities/mariadb-client/mysql-command-line-client.md#options) for the `[mysql](../../../../clients-and-utilities/mariadb-client/mysql-command-line-client.md)` client.


### Major New Features To Consider


You might consider using the following major new features in [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/old-releases/release-notes-mariadb-10-2-series/what-is-mariadb-102):


* [Window Functions](../../../../reference/sql-statements-and-structure/sql-statements/built-in-functions/special-functions/window-functions/README.md)
* [mysqlbinlog](../../../../clients-and-utilities/mariadb-binlog/README.md) now supports continuous binary log backups
* [Recursive Common Table Expressions](../../../../reference/sql-statements-and-structure/sql-statements/data-manipulation/selecting-data/common-table-expressions/recursive-common-table-expressions-overview.md)
* [JSON functions](../../../../reference/sql-statements-and-structure/sql-statements/built-in-functions/special-functions/json-functions/README.md)
* See also [System Variables Added in MariaDB 10.2](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/system-and-status-variables-added-by-major-release/system-and-status-variables-added-by-major-unmaintained-release/system-variables-added-in-mariadb-102.md).


### See Also


* [The features in MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/old-releases/release-notes-mariadb-10-2-series/what-is-mariadb-102)
* [Upgrading from MariaDB 10.1 to MariaDB 10.2 with Galera Cluster](upgrading-from-mariadb-101-to-mariadb-102-with-galera-cluster)
* [Upgrading from MariaDB 10.0 to MariaDB 10.1](upgrading-from-mariadb-100-to-mariadb-101.md)
* [Upgrading from MariaDB 5.5 to MariaDB 10.0](../upgrading-from-mariadb-10-4-to-mariadb-10-5.md)

