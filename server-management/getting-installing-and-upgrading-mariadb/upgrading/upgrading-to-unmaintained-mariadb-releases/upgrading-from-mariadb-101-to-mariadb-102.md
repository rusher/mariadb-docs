# Upgrading from MariaDB 10.1 to MariaDB 10.2

#

## How to Upgrade

For Windows, see [Upgrading MariaDB on Windows](../upgrading-mariadb-on-windows.md) instead.

For MariaDB Galera Cluster, see [Upgrading from MariaDB 10.1 to MariaDB 10.2 with Galera Cluster](upgrading-from-mariadb-101-to-mariadb-102-with-galera-cluster) instead.

Before you upgrade, it would be best to take a backup of your database. This is always a good idea to do before an upgrade. We would recommend [Mariabackup](../../../../server-usage/replication-cluster-multi-master/galera-cluster/state-snapshot-transfers-ssts-in-galera-cluster/mariabackup-sst-method.md).

The suggested upgrade procedure is:
1. Modify the repository configuration, so the system's package manager installs [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/what-is-mariadb-102). For example,

 * On Debian, Ubuntu, and other similar Linux distributions, see [Updating the MariaDB APT repository to a New Major Release](../../binary-packages/installing-mariadb-deb-files.md#updating-the-mariadb-apt-repository-to-a-new-major-release) for more information.
 * On RHEL, CentOS, Fedora, and other similar Linux distributions, see [Updating the MariaDB YUM repository to a New Major Release](../../binary-packages/rpm/yum.md#updating-the-mariadb-yum-repository-to-a-new-major-release) for more information.
 * On SLES, OpenSUSE, and other similar Linux distributions, see [Updating the MariaDB ZYpp repository to a New Major Release](../../binary-packages/rpm/installing-mariadb-with-zypper.md#updating-the-mariadb-zypp-repository-to-a-new-major-release) for more information.
1. Set `[innodb_fast_shutdown](/kb/en/xtradbinnodb-server-system-variables/#innodb_fast_shutdown)` to `0`. It can be changed dynamically with `[SET GLOBAL](../../../../server-usage/replication-cluster-multi-master/standard-replication/setting-up-replication.md#global-session)`. For example: 
`SET GLOBAL innodb_fast_shutdown=0;`

 * This step is not necessary when upgrading to [MariaDB 10.2.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/release-notes-mariadb-102-series/mariadb-1025-release-notes) or later. Omitting it can make the upgrade process far faster. See [MDEV-12289](https://jira.mariadb.org/browse/MDEV-12289) for more information.
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

 1. Ensures that the system tables in the `[mysq](/kb/en/the-mysql-database-tables/)l` database are fully compatible with the new version.
 1. Does a very quick check of all tables and marks them as compatible with the new version of MariaDB .

#

## Incompatible Changes Between 10.1 and 10.2

On most servers upgrading from 10.1 should be painless. However, there are some things that have changed which could affect an upgrade:

#

### InnoDB Instead of XtraDB

[MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/what-is-mariadb-102) uses [InnoDB](../../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/innodb-encryption/innodb-encryption-troubleshooting.md) as the default storage engine, rather than XtraDB, used in [MariaDB 10.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/what-is-mariadb-1011) and before. See [Why does MariaDB 10.2 use InnoDB instead of XtraDB?](/kb/en/why-does-mariadb-102-use-innodb-instead-of-xtradb/) In most cases this should have minimal effect as the latest InnoDB has incorporated most of the improvements made in earlier versions of XtraDB. Note that certain [XtraDB system variables](/kb/en/xtradbinnodb-server-system-variables/) are now ignored (although they still exist so as to permit easy upgrading).

#

### Options That Have Changed Default Values

In particular, take note of the changes to [innodb_strict_mode](/kb/en/xtradbinnodb-server-system-variables/#innodb_strict_mode), [sql_mode](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#sql_mode), [binlog_format](/kb/en/replication-and-binary-log-server-system-variables/#binlog_format), [binlog_checksum](/kb/en/replication-and-binary-log-server-system-variables/#binlog_checksum) and [innodb_checksum_algorithm](/kb/en/xtradbinnodb-server-system-variables/#innodb_checksum_algorithm).

| Option | Old default value | New default value |
| --- | --- | --- |
| Option | Old default value | New default value |
| [aria_recover(_options)](../../../../reference/storage-engines/aria/aria-system-variables.md#aria_recover_options) | NORMAL | BACKUP, QUICK |
| [binlog_annotate_row_events](/kb/en/replication-and-binary-log-server-system-variables/#binlog_annotate_row_events) | OFF | ON |
| [binlog_checksum](/kb/en/replication-and-binary-log-server-system-variables/#binlog_checksum) | NONE | CRC32 |
| [binlog_format](/kb/en/replication-and-binary-log-server-system-variables/#binlog_format) | STATEMENT | MIXED |
| [group_concat_max_len](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#group_concat_max_len) | 1024 | 1048576 |
| [innodb_autoinc_lock_mode](/kb/en/xtradbinnodb-server-system-variables/#innodb_autoinc_lock_mode) | 1 | 2 |
| [innodb_buffer_pool_dump_at_shutdown](/kb/en/xtradbinnodb-server-system-variables/#innodb_buffer_pool_dump_at_shutdown) | OFF | ON |
| [innodb_buffer_pool_dump_pct](/kb/en/xtradbinnodb-server-system-variables/#innodb_buffer_pool_dump_pct) | 100 | 25 |
| [innodb_buffer_pool_instances](/kb/en/xtradbinnodb-server-system-variables/#innodb_buffer_pool_instances) | 8 | Varies |
| [innodb_buffer_pool_load_at_startup](/kb/en/xtradbinnodb-server-system-variables/#innodb_buffer_pool_load_at_startup) | OFF | ON |
| [innodb_checksum_algorithm](/kb/en/xtradbinnodb-server-system-variables/#innodb_checksum_algorithm) | innodb | crc32 |
| [innodb_file_format](/kb/en/xtradbinnodb-server-system-variables/#innodb_file_format) | Antelope | Barracuda |
| [innodb_large_prefix](/kb/en/xtradbinnodb-server-system-variables/#innodb_large_prefix) | OFF | ON |
| [innodb_lock_schedule_algorithm](/kb/en/xtradbinnodb-server-system-variables/#innodb_lock_schedule_algorithm) | VATS | FCFS |
| [innodb_log_compressed_pages](/kb/en/xtradbinnodb-server-system-variables/#innodb_log_compressed_pages) | OFF | ON |
| [innodb_max_dirty_pages_pct_lwm](/kb/en/xtradbinnodb-server-system-variables/#innodb_max_dirty_pages_pct_lwm) | 0.001000 | 0 |
| [innodb_max_undo_log_size](/kb/en/xtradbinnodb-server-system-variables/#innodb_max_undo_log_size) | 1073741824 | 10485760 |
| [innodb_purge_threads](/kb/en/xtradbinnodb-server-system-variables/#innodb_purge_threads) | 1 | 4 |
| [innodb_strict_mode](/kb/en/xtradbinnodb-server-system-variables/#innodb_strict_mode) | OFF | ON |
| [innodb_undo_directory](/kb/en/xtradbinnodb-server-system-variables/#innodb_undo_directory) | . | NULL |
| [innodb_use_atomic_writes](/kb/en/xtradbinnodb-server-system-variables/#innodb_use_atomic_writes) | OFF | ON |
| [innodb_use_trim](/kb/en/xtradbinnodb-server-system-variables/#innodb_use_trim) | OFF | ON |
| [lock_wait_timeout](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#lock_wait_timeout) | 31536000 | 86400 |
| [log_slow_admin_statements](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#log_slow_admin_statements) | OFF | ON |
| [log_slow_slave_statements](/kb/en/replication-and-binary-log-server-system-variables/#log_slow_slave_statements) | OFF | ON |
| [log_warnings](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#log_warnings) | 1 | 2 |
| [max_allowed_packet](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#max_allowed_packet) | 4M | 16M |
| [max_long_data_size](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#max_long_data_size) | 4M | 16M |
| [myisam_recover_options](../../../../reference/storage-engines/myisam-storage-engine/myisam-system-variables.md#myisam_recover_options) | NORMAL | BACKUP, QUICK |
| [optimizer_switch](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#optimizer_switch) | See [Optimizer Switch](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/sys-schema/sys-schema-stored-procedures/optimizer_switch-helper-functions.md) for details. |
| [replicate_annotate_row_events](/kb/en/replication-and-binary-log-server-system-variables/#replicate_annotate_row_events) | OFF | ON |
| [server_id](/kb/en/replication-and-binary-log-server-system-variables/#server_id) | 0 | 1 |
| [slave_net_timeout](/kb/en/replication-and-binary-log-server-system-variables/#slave_net_timeout) | 3600 | 60 |
| [sql_mode](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#sql_mode) | NO_AUTO_CREATE_USER, NO_ENGINE_SUBSTITUTION | STRICT_TRANS_TABLES, ERROR_FOR_DIVISION_BY_ZERO, NO_AUTO_CREATE_USER, NO_ENGINE_SUBSTITUTION |
| [thread_cache_size](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#thread_cache_size) | 0 | Auto |
| [thread_pool_max_threads](/kb/en/thread-pool-system-and-status-variables/) | 1000 | 65536 |
| [thread_stack](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#thread_stack) | 295936 | 299008 |

#

### Options That Have Been Removed or Renamed

The following options should be removed or renamed if you use them in your [option files](../../configuring-mariadb-with-option-files.md):

| Option | Reason |
| --- | --- |
| Option | Reason |
| aria_recover | Renamed to [aria_recover_options](../../../../reference/storage-engines/aria/aria-system-variables.md#aria_recover_options) to match [myisam_recover_options](../../../../reference/storage-engines/myisam-storage-engine/myisam-system-variables.md#myisam_recover_options). |
| [innodb_additional_mem_pool_size](/kb/en/xtradbinnodb-server-system-variables/#innodb_additional_mem_pool_size) | Deprecated in [MariaDB 10.0](/kb/en/what-is-mariadb-100/). |
| [innodb_api_bk_commit_interval](/kb/en/xtradbinnodb-server-system-variables/#innodb_api_bk_commit_interval) | Memcache never implemented in MariaDB. |
| [innodb_api_disable_rowlock](/kb/en/xtradbinnodb-server-system-variables/#innodb_api_disable_rowlock) | Memcache never implemented in MariaDB. |
| [innodb_api_enable_binlog](/kb/en/xtradbinnodb-server-system-variables/#innodb_api_enable_binlog) | Memcache never implemented in MariaDB. |
| [innodb_api_enable_mdl](/kb/en/xtradbinnodb-server-system-variables/#innodb_api_enable_mdl) | Memcache never implemented in MariaDB. |
| [|innodb_api_trx_level](/kb/en/xtradbinnodb-server-system-variables/#innodb_api_trx_level) | Memcache never implemented in MariaDB. |
| [innodb_use_sys_malloc](/kb/en/xtradbinnodb-server-system-variables/#innodb_use_sys_malloc) | Deprecated in [MariaDB 10.0](/kb/en/what-is-mariadb-100/). |

#

### Reserved Words

New [reserved words](../../../../reference/sql-statements-and-structure/sql-language-structure/reserved-words.md): OVER, RECURSIVE and ROWS. These can no longer be used as [identifiers](../../../../reference/sql-statements-and-structure/sql-language-structure/identifier-names.md) without being quoted.

#

### TokuDB

[TokuDB](../../../../reference/storage-engines/tokudb/tokudb-resources.md) has been split into a separate package, mariadb-plugin-tokudb.

#

### Replication

[Replication](/kb/en/standard-replication/) from legacy MySQL servers may require setting [binlog_checksum](/kb/en/replication-and-binary-log-server-system-variables/#binlog_checksum) to NONE.

#

### SQL Mode

[SQL_MODE](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/mariadb-releases/compatibility-differences/sql_modemssql) has been changed; in particular, NOT NULL fields with no default will no longer fall back to a dummy value for inserts which do not specify a value for that field.

#

### Auto_increment

[Auto_increment](../../../../reference/data-types/auto_increment.md) columns are no longer permitted in [CHECK constraints](../../../../reference/sql-statements-and-structure/sql-statements/data-definition/constraint.md), [DEFAULT value expressions](../../../../reference/sql-statements-and-structure/sql-statements/data-definition/create/create-tablespace.md#default) and [virtual columns](/kb/en/virtual-computed-columns/). They were permitted in earlier versions, but did not work correctly.

#

### TLS

Starting with [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/what-is-mariadb-102), when the user specifies the `--ssl` option with a [client or utility](/kb/en/clients-utilities/), the [client or utility](/kb/en/clients-utilities/) will not [verify the server certificate](../../../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/secure-connections-overview.md#server-certificate-verification) by default. In order to verify the server certificate, the user must specify the `--ssl-verify-server-cert` option to the [client or utility](/kb/en/clients-utilities/). For more information, see the [list of options](../../../../clients-and-utilities/mariadb-client/mysql-command-line-client.md#options) for the `[mysql](../../../../clients-and-utilities/mariadb-client/mysql-command-line-client.md)` client.

#

## Major New Features To Consider

You might consider using the following major new features in [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/what-is-mariadb-102):

* [Window Functions](../../../../reference/sql-statements-and-structure/sql-statements/built-in-functions/special-functions/window-functions/window-functions-overview.md)
* [mysqlbinlog](/kb/en/mysqlbinlog/) now supports continuous binary log backups
* [Recursive Common Table Expressions](../../../../reference/sql-statements-and-structure/sql-statements/data-manipulation/selecting-data/common-table-expressions/recursive-common-table-expressions-overview.md)
* [JSON functions](/kb/en/json-functions/)
* See also [System Variables Added in MariaDB 10.2](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/system-and-status-variables-added-by-major-release/system-and-status-variables-added-by-major-unmaintained-release/system-variables-added-in-mariadb-102.md).

#

## See Also

* [The features in MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/what-is-mariadb-102)
* [Upgrading from MariaDB 10.1 to MariaDB 10.2 with Galera Cluster](upgrading-from-mariadb-101-to-mariadb-102-with-galera-cluster)
* [Upgrading from MariaDB 10.0 to MariaDB 10.1](upgrading-from-mariadb-100-to-mariadb-101.md)
* [Upgrading from MariaDB 5.5 to MariaDB 10.0](/kb/en/upgrading-from-mariadb-55-to-mariadb-100/)