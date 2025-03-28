# Upgrading from MariaDB 10.6 to MariaDB 10.11

#

## How to Upgrade

For Windows, see [Upgrading MariaDB on Windows](upgrading-mariadb-on-windows.md).

For MariaDB Galera Cluster, see [Upgrading from MariaDB 10.6 to MariaDB 10.11 with Galera Cluster](../../../server-usage/replication-cluster-multi-master/galera-cluster/upgrading-galera-cluster/upgrading-from-mariadb-10-6-to-mariadb-10-11-with-galeracluster.md).

Before you upgrade, it would be best to take a backup of your database. This is always a good idea to do before an upgrade. We would recommend [Mariabackup](../../../server-usage/replication-cluster-multi-master/galera-cluster/state-snapshot-transfers-ssts-in-galera-cluster/mariabackup-sst-method.md).

The suggested upgrade procedure is:
1. Modify the repository configuration, so the system's package manager installs [MariaDB 10.11](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/what-is-mariadb-1011). For example,

 * On Debian, Ubuntu, and other similar Linux distributions, see [Updating the MariaDB APT repository to a New Major Release](../binary-packages/installing-mariadb-deb-files.md#updating-the-mariadb-apt-repository-to-a-new-major-release) for more information.
 * On RHEL, CentOS, Fedora, and other similar Linux distributions, see [Updating the MariaDB YUM repository to a New Major Release](../binary-packages/rpm/yum.md#updating-the-mariadb-yum-repository-to-a-new-major-release) for more information.
 * On SLES, OpenSUSE, and other similar Linux distributions, see [Updating the MariaDB ZYpp repository to a New Major Release](../binary-packages/rpm/installing-mariadb-with-zypper.md#updating-the-mariadb-zypp-repository-to-a-new-major-release) for more information.
1. [Stop MariaDB](../starting-and-stopping-mariadb/starting-and-stopping-mariadb-automatically.md).
1. Uninstall the old version of MariaDB.

 * On Debian, Ubuntu, and other similar Linux distributions, execute the following: 
`sudo apt-get remove mariadb-server`
 * On RHEL, CentOS, Fedora, and other similar Linux distributions, execute the following: 
`sudo yum remove MariaDB-server`
 * On SLES, OpenSUSE, and other similar Linux distributions, execute the following: 
`sudo zypper remove MariaDB-server`
1. Install the new version of MariaDB.

 * On Debian, Ubuntu, and other similar Linux distributions, see [Installing MariaDB Packages with APT](../binary-packages/installing-mariadb-deb-files.md#installing-mariadb-packages-with-apt) for more information.
 * On RHEL, CentOS, Fedora, and other similar Linux distributions, see [Installing MariaDB Packages with YUM](../binary-packages/rpm/yum.md#installing-mariadb-packages-with-yum) for more information.
 * On SLES, OpenSUSE, and other similar Linux distributions, see [Installing MariaDB Packages with ZYpp](../binary-packages/rpm/installing-mariadb-with-zypper.md#installing-mariadb-packages-with-zypp) for more information.
1. Make any desired changes to configuration options in [option files](../configuring-mariadb-with-option-files.md), such as `my.cnf`. This includes removing any options that are no longer supported.
1. [Start MariaDB](../starting-and-stopping-mariadb/starting-and-stopping-mariadb-automatically.md).
1. Run [mariadb-upgrade](../../../clients-and-utilities/mariadb-upgrade.md).

 * `mariadb-upgrade` does two things:

 1. Ensures that the system tables in the [mysql](/kb/en/the-mysql-database-tables/) database are fully compatible with the new version.
 1. Does a very quick check of all tables and marks them as compatible with the new version of MariaDB .

#

## Incompatible Changes Between 10.6 and 10.11

On most servers upgrading from 10.6 should be painless. However, there are some things that have changed which could affect an upgrade:

#

### Compression

If a non-zlib compression algorithm was used in [InnoDB](../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/innodb-encryption/innodb-encryption-troubleshooting.md) or [Mroonga](../../../reference/storage-engines/mroonga/mroonga-status-variables.md) before upgrading to 10.11, those tables will be unreadable until the appropriate compression library is installed. See [Compression Plugins#Upgrading](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/optimization-and-tuning-compression/compression-plugins.md#upgrading).

#

### Options That Have Changed Default Values

| Option | Old default | New default |
| --- | --- | --- |
| Option | Old default | New default |
| [innodb_buffer_pool_chunk_size](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_buffer_pool_chunk_size) | 134217728 | Autosized |
| [spider_auto_increment_mode](/kb/en/spider-server-system-variables/#spider_auto_increment_mode) | -1 | 0 |
| [spider_bgs_first_read](/kb/en/spider-server-system-variables/#spider_bgs_first_read) | -1 | 2 |
| [spider_bgs_mode](/kb/en/spider-server-system-variables/#spider_bgs_mode) | -1 | 0 |
| [spider_bgs_second_read](/kb/en/spider-server-system-variables/#spider_bgs_second_read) | -1 | 100 |
| [spider_bka_mode](/kb/en/spider-server-system-variables/#spider_bka_mode) | -1 | 1 |
| [spider_bka_table_name_type](/kb/en/spider-server-system-variables/#spider_bka_table_name_type) | -1 | 1 |
| [spider_buffer_size](/kb/en/spider-server-system-variables/#spider_buffer_size) | -1 | 16000 |
| [spider_bulk_size](/kb/en/spider-server-system-variables/#spider_bulk_size) | -1 | 16000 |
| [spider_bulk_update_mode](/kb/en/spider-server-system-variables/#spider_bulk_update_mode) | -1 | 0 |
| [spider_bulk_update_size](/kb/en/spider-server-system-variables/#spider_bulk_update_size) | -1 | 16000 |
| [spider_casual_read](/kb/en/spider-server-system-variables/#spider_casual_read) | -1 | 0 |
| [spider_connect_timeout](/kb/en/spider-server-system-variables/#spider_connect_timeout) | -1 | 6 |
| [spider_crd_bg_mode](/kb/en/spider-server-system-variables/#spider_crd_bg_mode) | -1 | 2 |
| [spider_crd_interval](/kb/en/spider-server-system-variables/#spider_crd_interval) | -1 | 51 |
| [spider_crd_mode](/kb/en/spider-server-system-variables/#spider_crd_mode) | -1 | 1 |
| [spider_crd_sync](/kb/en/spider-server-system-variables/#spider_crd_sync) | -1 | 0 |
| [spider_crd_type](/kb/en/spider-server-system-variables/#spider_crd_type) | -1 | 2 |
| [spider_crd_weight](/kb/en/spider-server-system-variables/#spider_crd_weight) | -1 | 2 |
| [spider_delete_all_rows_type](/kb/en/spider-server-system-variables/#spider_delete_all_rows_type) | -1 | 1 |
| [spider_direct_dup_insert](/kb/en/spider-server-system-variables/#spider_direct_dup_insert) | -1 | 0 |
| [spider_direct_order_limit](/kb/en/spider-server-system-variables/#spider_direct_order_limit) | -1 | 9223372036854775807 |
| [spider_error_read_mode](/kb/en/spider-server-system-variables/#spider_error_read_mode) | -1 | 0 |
| [spider_error_write_mode](/kb/en/spider-server-system-variables/#spider_error_write_mode) | -1 | 0 |
| [spider_first_read](/kb/en/spider-server-system-variables/#spider_first_read) | -1 | 0 |
| [spider_init_sql_alloc_size](/kb/en/spider-server-system-variables/#spider_init_sql_alloc_size) | -1 | 1024 |
| [spider_internal_limit](/kb/en/spider-server-system-variables/#spider_internal_limit) | -1 | 9223372036854775807 |
| [spider_internal_offset](/kb/en/spider-server-system-variables/#spider_internal_offset) | -1 | 0 |
| [spider_internal_optimize](/kb/en/spider-server-system-variables/#spider_internal_optimize) | -1 | 0 |
| [spider_internal_optimize_local](/kb/en/spider-server-system-variables/#spider_internal_optimize_local) | -1 | 0 |
| [spider_load_crd_at_startup](/kb/en/spider-server-system-variables/#spider_load_crd_at_startup) | -1 | 1 |
| [spider_load_sts_at_startup](/kb/en/spider-server-system-variables/#spider_load_sts_at_startup) | -1 | 1 |
| [spider_low_mem_read](/kb/en/spider-server-system-variables/#spider_low_mem_read) | -1 | 1 |
| [spider_max_order](/kb/en/spider-server-system-variables/#spider_max_order) | -1 | 32767 |
| [spider_multi_split_read](/kb/en/spider-server-system-variables/#spider_multi_split_read) | -1 | 100 |
| [spider_net_read_timeout](/kb/en/spider-server-system-variables/#spider_net_read_timeout) | -1 | 600 |
| [spider_net_write_timeout](/kb/en/spider-server-system-variables/#spider_net_write_timeout) | -1 | 600 |
| [spider_quick_mode](/kb/en/spider-server-system-variables/#spider_quick_mode) | -1 | 3 |
| [spider_quick_page_byte](/kb/en/spider-server-system-variables/#spider_quick_page_byte) | -1 | 10485760 |
| [spider_quick_page_size](/kb/en/spider-server-system-variables/#spider_quick_page_size) | -1 | 1024 |
| [spider_read_only_mode](/kb/en/spider-server-system-variables/#spider_read_only_mode) | -1 | 0 |
| [spider_reset_sql_alloc](/kb/en/spider-server-system-variables/#spider_reset_sql_alloc) | -1 | 1 |
| [spider_second_read](/kb/en/spider-server-system-variables/#spider_second_read) | -1 | 0 |
| [spider_selupd_lock_mode](/kb/en/spider-server-system-variables/#spider_selupd_lock_mode) | -1 | 1 |
| [spider_semi_split_read](/kb/en/spider-server-system-variables/#spider_semi_split_read) | -1 | 2 |
| [spider_semi_split_read_limit](/kb/en/spider-server-system-variables/#spider_semi_split_read_limit) | -1 | 1 |
| [spider_semi_table_lock_connection](/kb/en/spider-server-system-variables/#spider_semi_table_lock_connection) | -1 | 1 |
| [spider_semi_table_lock](/kb/en/spider-server-system-variables/#spider_semi_table_lock) | 1 | 0 |

#

### Options That Have Been Removed or Renamed

The following options should be removed or renamed if you use them in your [option files](../configuring-mariadb-with-option-files.md):

| Option | Reason |
| --- | --- |
| Option | Reason |
| [innodb_log_write_ahead_size](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_log_write_ahead_size) | On Linux and Windows, the physical block size of the underlying storage is instead detected and used. |
| [innodb_version](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_version) | Redundant |
| [wsrep_replicate_myisam](../../../server-usage/replication-cluster-multi-master/galera-cluster/galera-cluster-system-variables.md#wsrep_replicate_myisam) | Use [wsrep_mode](../../../server-usage/replication-cluster-multi-master/galera-cluster/galera-cluster-system-variables.md#wsrep_mode) instead. |
| [wsrep_strict_ddl](../../../server-usage/replication-cluster-multi-master/galera-cluster/galera-cluster-system-variables.md#wsrep_strict_ddl) | Use [wsrep_mode](../../../server-usage/replication-cluster-multi-master/galera-cluster/galera-cluster-system-variables.md#wsrep_mode) instead. |

#

### Deprecated Options

The following options have been deprecated. They have not yet been removed, but will be in a future version, and should ideally no longer be used.

| Option | Reason |
| --- | --- |
| Option | Reason |
| [keep_files_on_create](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#keep_files_on_create) | MariaDB now deletes orphan files, so this setting should never be necessary. |

#

## See Also

* [Features in MariaDB 10.11](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/what-is-mariadb-1011)
* [Features in MariaDB 10.10](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/what-is-mariadb-1010)
* [Features in MariaDB 10.9](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/what-is-mariadb-109)
* [Features in MariaDB 10.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/what-is-mariadb-108)
* [Features in MariaDB 10.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/what-is-mariadb-107)

* [Upgrading from MariaDB 10.6 to MariaDB 10.7 with Galera Cluster](upgrading-from-mariadb-106-to-mariadb-107-with-galera-cluster)

* [Upgrading from MariaDB 10.7 to MariaDB 10.8](upgrading-to-unmaintained-mariadb-releases/upgrading-from-mariadb-10-7-to-mariadb-10-8.md)
* [Upgrading from MariaDB 10.6 to MariaDB 10.7](/kb/en/upgrading-from-mariadb-106-to-mariadb-107/)
* [Upgrading from MariaDB 10.5 to MariaDB 10.6](/kb/en/upgrading-from-mariadb-105-to-mariadb-106/)