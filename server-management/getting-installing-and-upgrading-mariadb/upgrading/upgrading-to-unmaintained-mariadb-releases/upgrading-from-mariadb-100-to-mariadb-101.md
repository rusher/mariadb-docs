# Upgrading from MariaDB 10.0 to MariaDB 10.1

#

# What You Need to Know

There are no changes in table or index formats between [MariaDB 10.0](/en/what-is-mariadb-100/) and [MariaDB
10.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/what-is-mariadb-1011), so on most servers the upgrade should be painless.

#

## How to Upgrade

For Windows, see [Upgrading MariaDB on Windows](../upgrading-mariadb-on-windows.md) instead.

For MariaDB Galera Cluster, see [Upgrading from MariaDB Galera Cluster 10.0 to MariaDB 10.1 with Galera Cluster](upgrading-galera-cluster-upgrading-from-mariadb-galera-cluster-100-to-maria) instead.

Before you upgrade, it would be best to take a backup of your database. This is always a good idea to do before an upgrade. We would recommend [Percona XtraBackup](/en/backup-restore-and-import-clients-percona-xtrabackup/).

The suggested upgrade procedure is:
1. Modify the repository configuration, so the system's package manager installs [MariaDB 10.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/what-is-mariadb-1011). For example,

 * On Debian, Ubuntu, and other similar Linux distributions, see [Updating the MariaDB APT repository to a New Major Release](../../binary-packages/installing-mariadb-deb-files.md#updating-the-mariadb-apt-repository-to-a-new-major-release) for more information.
 * On RHEL, CentOS, Fedora, and other similar Linux distributions, see [Updating the MariaDB YUM repository to a New Major Release](../../binary-packages/rpm/yum.md#updating-the-mariadb-yum-repository-to-a-new-major-release) for more information.
 * On SLES, OpenSUSE, and other similar Linux distributions, see [Updating the MariaDB ZYpp repository to a New Major Release](../../binary-packages/rpm/installing-mariadb-with-zypper.md#updating-the-mariadb-zypp-repository-to-a-new-major-release) for more information.
1. Set `[innodb_fast_shutdown](/en/xtradbinnodb-server-system-variables/#innodb_fast_shutdown)` to `0`. It can be changed dynamically with `[SET GLOBAL](../../../../server-usage/replication-cluster-multi-master/standard-replication/setting-up-replication.md#global-session)`. For example: 
`SET GLOBAL innodb_fast_shutdown=0;`
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

 1. Ensures that the system tables in the `[mysq](/en/the-mysql-database-tables/)l` database are fully compatible with the new version.
 1. Does a very quick check of all tables and marks them as compatible with the new version of MariaDB .

#

## Incompatible Changes Between 10.0 and 10.1

As mentioned previously, on most servers upgrading from 10.0 should be painless.
However, there are some things that have changed which could affect an upgrade:

#

### Storage Engines

* The [ARCHIVE](/en/archive/) storage engine is no longer enabled by default, and the plugin needs to be specifically enabled.
* The [BLACKHOLE](../../../../reference/storage-engines/blackhole.md) storage engine is no longer enabled by default, and the plugin needs to be specifically enabled.

#

### Replication

* [MariaDB 10.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/what-is-mariadb-1011) introduces new, standards-compliant behavior for dealing with [primary keys over nullable columns](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/optimization-and-indexes/primary-keys-with-nullable-columns.md). In certain edge cases this could cause replication issues when replicating from a [MariaDB 10.0](/en/what-is-mariadb-100/) master to a [MariaDB 10.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/what-is-mariadb-1011) slave using [statement-based replication](../../../server-monitoring-logs/binary-log/binary-log-formats.md#statement-based). See [MDEV-12248](https://jira.mariadb.org/browse/MDEV-12248).

#

### Options That Have Changed Default Values

Most of the following options have increased in value to give better performance.

| Option | Old default value | New default value |
| --- | --- | --- |
| Option | Old default value | New default value |
| [innodb_log_compressed_pages](/en/xtradbinnodb-server-system-variables/#innodb_log_compressed_pages) | ON | OFF |
| [join_buffer_size](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#join_buffer_size) | 128K | 256K |
| [max_allowed_packet](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#max_allowed_packet) | 1M | 4M |
| [query_alloc_block_size](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#query_alloc_block_size) | 8192 | 16384 |
| [query_cache_size](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#query_cache_size) | 0 | 1M |
| [query_cache_type](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#query_cache_type) | ON | OFF |
| [sync_master_info](/en/replication-and-binary-log-server-system-variables/#sync_master_info) | 0 | 10000 |
| [sync_relay_log](/en/replication-and-binary-log-server-system-variables/#sync_relay_log) | 0 | 10000 |
| [sync_relay_log_info](/en/replication-and-binary-log-server-system-variables/#sync_relay_log_info) | 0 | 10000 |
| [query_prealloc_size](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#query_prealloc_size) | 8192 | 24576 |
| [secure_auth](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#secure_auth) | OFF | ON |
| [sql_log_bin](/en/replication-and-binary-log-server-system-variables/#sql_log_bin) | | No longer affects replication of events in a Galera cluster. |
| [sql_mode](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#sql_mode) | empty | NO_AUTO_CREATE_USER, NO_ENGINE_SUBSTITUTION |
| [table_open_cache](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#table_open_cache) | 400 | 2000 |
| [thread_pool_max_threads](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#thread_pool_max_threads) | 500 | 1000 |

#

### Options That Have Been Removed or Renamed

The following options should be removed or renamed if you use them in your config files:

| Option | Reason |
| --- | --- |
| Option | Reason |
| [rpl_recovery_rank](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#rpl_recovery_rank) | Unused in 10.0 |

#

### Other Issues

Note that explicit or implicit casts from MAX(string) to INT, DOUBLE or DECIMAL now produce warnings ([MDEV-8852](https://jira.mariadb.org/browse/MDEV-8852)).

#

## Major New Features To Consider

You might consider using the following major new features in [MariaDB 10.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/what-is-mariadb-1011):

* [Galera Cluster](../../../../server-usage/replication-cluster-multi-master/galera-cluster/galera-use-cases.md) is now included by default.
* [Encryption](../../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/data-at-rest-encryption-overview.md)
* [InnoDB/XtraDB Page Compression](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/optimization-and-tuning-compression/compression-plugins.md)

#

# Notes

#

# See Also

* [The features in MariaDB 10.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/what-is-mariadb-1011)
* [Upgrading from MariaDB Galera Cluster 10.0 to MariaDB 10.1 with Galera Cluster](upgrading-galera-cluster-upgrading-from-mariadb-galera-cluster-100-to-maria)
* [Upgrading from MariaDB 10.1 to MariaDB 10.2](upgrading-from-mariadb-101-to-mariadb-102.md)
* [Upgrading from MariaDB 5.5 to MariaDB 10.0](/en/upgrading-from-mariadb-55-to-mariadb-100/)