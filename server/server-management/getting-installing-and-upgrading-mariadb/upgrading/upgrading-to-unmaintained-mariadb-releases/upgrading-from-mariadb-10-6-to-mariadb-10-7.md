
# Upgrading from MariaDB 10.6 to MariaDB 10.7


Note that [MariaDB 10.7](../../../../../release-notes/mariadb-community-server/what-is-mariadb-107.md) is [only maintained for one year](https://mariadb.org/about/#maintenance-policy). [MariaDB 10.6](../../../../../release-notes/mariadb-community-server/what-is-mariadb-106.md) is currently the latest long-term maintenance release.


### How to Upgrade


For Windows, see [Upgrading MariaDB on Windows](../upgrading-mariadb-on-windows.md).


For MariaDB Galera Cluster, see [Upgrading from MariaDB 10.6 to MariaDB 10.7 with Galera Cluster](upgrading-from-mariadb-106-to-mariadb-107-with-galera-cluster) instead.


Before you upgrade, it would be best to take a backup of your database. This is always a good idea to do before an upgrade. We would recommend [Mariabackup](../../../backing-up-and-restoring-databases/mariabackup/mariabackup-and-backup-stage-commands.md).



The suggested upgrade procedure is:


1. Modify the repository configuration, so the system's package manager installs [MariaDB 10.7](../../../../../release-notes/mariadb-community-server/what-is-mariadb-107.md). For example,

  * On Debian, Ubuntu, and other similar Linux distributions, see [Updating the MariaDB APT repository to a New Major Release](../../binary-packages/automated-mariadb-deployment-and-administration/ansible-and-mariadb/installing-mariadb-deb-files-with-ansible.md#updating-the-mariadb-apt-repository-to-a-new-major-release) for more information.
  * On RHEL, CentOS, Fedora, and other similar Linux distributions, see [Updating the MariaDB YUM repository to a New Major Release](../../binary-packages/rpm/yum.md#updating-the-mariadb-yum-repository-to-a-new-major-release) for more information.
  * On SLES, OpenSUSE, and other similar Linux distributions, see [Updating the MariaDB ZYpp repository to a New Major Release](../../binary-packages/rpm/installing-mariadb-with-zypper.md#updating-the-mariadb-zypp-repository-to-a-new-major-release) for more information.
1. [Stop MariaDB](../../starting-and-stopping-mariadb/starting-and-stopping-mariadb-automatically.md).
1. Uninstall the old version of MariaDB.

  * On Debian, Ubuntu, and other similar Linux distributions, execute the following: 
`sudo apt-get remove mariadb-server`
  * On RHEL, CentOS, Fedora, and other similar Linux distributions, execute the following: 
`sudo yum remove MariaDB-server`
  * On SLES, OpenSUSE, and other similar Linux distributions, execute the following: 
`sudo zypper remove MariaDB-server`
1. Install the new version of MariaDB.

  * On Debian, Ubuntu, and other similar Linux distributions, see [Installing MariaDB Packages with APT](../../binary-packages/automated-mariadb-deployment-and-administration/ansible-and-mariadb/installing-mariadb-deb-files-with-ansible.md#installing-mariadb-packages-with-apt) for more information.
  * On RHEL, CentOS, Fedora, and other similar Linux distributions, see [Installing MariaDB Packages with YUM](../../binary-packages/rpm/yum.md#installing-mariadb-packages-with-yum) for more information.
  * On SLES, OpenSUSE, and other similar Linux distributions, see [Installing MariaDB Packages with ZYpp](../../binary-packages/rpm/installing-mariadb-with-zypper.md#installing-mariadb-packages-with-zypp) for more information.
1. Make any desired changes to configuration options in [option files](../../configuring-mariadb-with-option-files.md), such as `my.cnf`. This includes removing any options that are no longer supported.
1. [Start MariaDB](../../starting-and-stopping-mariadb/starting-and-stopping-mariadb-automatically.md).
1. Run [mariadb-upgrade](../../../../clients-and-utilities/mariadb-upgrade.md).

  * `mariadb-upgrade` does two things:

    1. Ensures that the system tables in the [mysql](../../../../ref/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/the-mysql-database-tables/README.md) database are fully compatible with the new version.
    1. Does a very quick check of all tables and marks them as compatible with the new version of MariaDB .


### Incompatible Changes Between 10.6 and 10.7


On most servers upgrading from 10.6 should be painless. However, there are some things that have changed which could affect an upgrade:


#### Reserved Words


* ROW_NUMBER is now a [reserved word](../../../../ref/sql-statements-and-structure/sql-language-structure/reserved-words.md).


#### Compression


If a non-zlib compression algorithm was used in [InnoDB](../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/innodb-upgrade-tests/README.md) or [Mroonga](../../../../ref/storage-engines/mroonga/mroonga-user-defined-functions/mroonga_snippet_html.md) before upgrading to 10.7, those tables will be unreadable until the appropriate compression library is installed. See [Compression Plugins#Upgrading](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/optimization-and-tuning-compression/compression-plugins.md#upgrading).


#### Options That Have Changed Default Values



| Option | Old default | New default |
| --- | --- | --- |
| Option | Old default | New default |
| [spider_auto_increment_mode](../../../../ref/storage-engines/spider/spider-system-variables.md) | -1 | 0 |
| [spider_bgs_first_read](../../../../ref/storage-engines/spider/spider-system-variables.md) | -1 | 2 |
| [spider_bgs_mode](../../../../ref/storage-engines/spider/spider-system-variables.md) | -1 | 0 |
| [spider_bgs_second_read](../../../../ref/storage-engines/spider/spider-system-variables.md) | -1 | 100 |
| [spider_bka_mode](../../../../ref/storage-engines/spider/spider-system-variables.md) | -1 | 1 |
| [spider_bka_table_name_type](../../../../ref/storage-engines/spider/spider-system-variables.md) | -1 | 1 |
| [spider_buffer_size](../../../../ref/storage-engines/spider/spider-system-variables.md) | -1 | 16000 |
| [spider_bulk_size](../../../../ref/storage-engines/spider/spider-system-variables.md) | -1 | 16000 |
| [spider_bulk_update_mode](../../../../ref/storage-engines/spider/spider-system-variables.md) | -1 | 0 |
| [spider_bulk_update_size](../../../../ref/storage-engines/spider/spider-system-variables.md) | -1 | 16000 |
| [spider_casual_read](../../../../ref/storage-engines/spider/spider-system-variables.md) | -1 | 0 |
| [spider_connect_timeout](../../../../ref/storage-engines/spider/spider-system-variables.md) | -1 | 6 |
| [spider_crd_bg_mode](../../../../ref/storage-engines/spider/spider-system-variables.md) | -1 | 2 |
| [spider_crd_interval](../../../../ref/storage-engines/spider/spider-system-variables.md) | -1 | 51 |
| [spider_crd_mode](../../../../ref/storage-engines/spider/spider-system-variables.md) | -1 | 1 |
| [spider_crd_sync](../../../../ref/storage-engines/spider/spider-system-variables.md) | -1 | 0 |
| [spider_crd_type](../../../../ref/storage-engines/spider/spider-system-variables.md) | -1 | 2 |
| [spider_crd_weight](../../../../ref/storage-engines/spider/spider-system-variables.md) | -1 | 2 |
| [spider_delete_all_rows_type](../../../../ref/storage-engines/spider/spider-system-variables.md) | -1 | 1 |
| [spider_direct_dup_insert](../../../../ref/storage-engines/spider/spider-system-variables.md) | -1 | 0 |
| [spider_direct_order_limit](../../../../ref/storage-engines/spider/spider-system-variables.md) | -1 | 9223372036854775807 |
| [spider_error_read_mode](../../../../ref/storage-engines/spider/spider-system-variables.md) | -1 | 0 |
| [spider_error_write_mode](../../../../ref/storage-engines/spider/spider-system-variables.md) | -1 | 0 |
| [spider_first_read](../../../../ref/storage-engines/spider/spider-system-variables.md) | -1 | 0 |
| [spider_init_sql_alloc_size](../../../../ref/storage-engines/spider/spider-system-variables.md) | -1 | 1024 |
| [spider_internal_limit](../../../../ref/storage-engines/spider/spider-system-variables.md) | -1 | 9223372036854775807 |
| [spider_internal_offset](../../../../ref/storage-engines/spider/spider-system-variables.md) | -1 | 0 |
| [spider_internal_optimize](../../../../ref/storage-engines/spider/spider-system-variables.md) | -1 | 0 |
| [spider_internal_optimize_local](../../../../ref/storage-engines/spider/spider-system-variables.md) | -1 | 0 |
| [spider_load_crd_at_startup](../../../../ref/storage-engines/spider/spider-system-variables.md) | -1 | 1 |
| [spider_load_sts_at_startup](../../../../ref/storage-engines/spider/spider-system-variables.md) | -1 | 1 |
| [spider_low_mem_read](../../../../ref/storage-engines/spider/spider-system-variables.md) | -1 | 1 |
| [spider_max_order](../../../../ref/storage-engines/spider/spider-system-variables.md) | -1 | 32767 |
| [spider_multi_split_read](../../../../ref/storage-engines/spider/spider-system-variables.md) | -1 | 100 |
| [spider_net_read_timeout](../../../../ref/storage-engines/spider/spider-system-variables.md) | -1 | 600 |
| [spider_net_write_timeout](../../../../ref/storage-engines/spider/spider-system-variables.md) | -1 | 600 |
| [spider_quick_mode](../../../../ref/storage-engines/spider/spider-system-variables.md) | -1 | 3 |
| [spider_quick_page_byte](../../../../ref/storage-engines/spider/spider-system-variables.md) | -1 | 10485760 |
| [spider_quick_page_size](../../../../ref/storage-engines/spider/spider-system-variables.md) | -1 | 1024 |
| [spider_read_only_mode](../../../../ref/storage-engines/spider/spider-system-variables.md) | -1 | 0 |
| [spider_reset_sql_alloc](../../../../ref/storage-engines/spider/spider-system-variables.md) | -1 | 1 |
| [spider_second_read](../../../../ref/storage-engines/spider/spider-system-variables.md) | -1 | 0 |
| [spider_selupd_lock_mode](../../../../ref/storage-engines/spider/spider-system-variables.md) | -1 | 1 |
| [spider_semi_split_read](../../../../ref/storage-engines/spider/spider-system-variables.md) | -1 | 2 |
| [spider_semi_split_read_limit](../../../../ref/storage-engines/spider/spider-system-variables.md) | -1 | 1 |
| [spider_semi_table_lock_connection](../../../../ref/storage-engines/spider/spider-system-variables.md) | -1 | 1 |
| [spider_reset_sql_alloc](../../../../ref/storage-engines/spider/spider-system-variables.md) | -1 | 1 |



#### Options That Have Been Removed or Renamed


The following options should be removed or renamed if you use them in your [option files](../../configuring-mariadb-with-option-files.md):



| Option | Reason |
| --- | --- |
| Option | Reason |
| [wsrep_replicate_myisam](../../../../server-usage/replication-cluster-multi-master/galera-cluster/galera-cluster-system-variables.md#wsrep_replicate_myisam) | Use [wsrep_mode](../../../../server-usage/replication-cluster-multi-master/galera-cluster/galera-cluster-system-variables.md#wsrep_mode) instead. |
| [wsrep_strict_ddl](../../../../server-usage/replication-cluster-multi-master/galera-cluster/galera-cluster-system-variables.md#wsrep_strict_ddl) | Use [wsrep_mode](../../../../server-usage/replication-cluster-multi-master/galera-cluster/galera-cluster-system-variables.md#wsrep_mode) instead. |



### See Also


* [The features in MariaDB 10.7](../../../../../release-notes/mariadb-community-server/what-is-mariadb-107.md)



* [Upgrading from MariaDB 10.6 to MariaDB 10.7 with Galera Cluster](upgrading-from-mariadb-106-to-mariadb-107-with-galera-cluster)



* [Upgrading from MariaDB 10.5 to MariaDB 10.6](../upgrading-from-mariadb-10-5-to-mariadb-10-6.md)
* [Upgrading from MariaDB 10.4 to MariaDB 10.5](../upgrading-from-mariadb-10-4-to-mariadb-10-5.md)
* [Upgrading from MariaDB 10.3 to MariaDB 10.4](upgrading-from-mariadb-103-to-mariadb-104.md)

