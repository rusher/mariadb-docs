
# Upgrading from MariaDB 10.11 to MariaDB 11.4


This page includes details for upgrading from [MariaDB 10.11](../../../../release-notes/mariadb-community-server/what-is-mariadb-1011.md) to the subsequent long-term maintenance version, [MariaDB 11.4](../../../../release-notes/mariadb-community-server/what-is-mariadb-114.md).


### How to Upgrade


For Windows, see [Upgrading MariaDB on Windows](upgrading-mariadb-on-windows.md).


For MariaDB Galera Cluster, see [Upgrading from MariaDB 11.4 to MariaDB 11.4 with Galera Cluster](https://mariadb.com/kb/en/upgrading-from-mariadb-10-11-to-mariadb-11-4-with-galeracluster/).


Before you upgrade, it would be best to take a backup of your database. This is always a good idea to do before an upgrade. We would recommend [Mariabackup](../../backing-up-and-restoring-databases/mariabackup/mariabackup-and-backup-stage-commands.md).



The suggested upgrade procedure is:


1. Modify the repository configuration, so the system's package manager installs [MariaDB 11.4](../../../../release-notes/mariadb-community-server/what-is-mariadb-114.md). For example,

  * On Debian, Ubuntu, and other similar Linux distributions, see [Updating the MariaDB APT repository to a New Major Release](../binary-packages/automated-mariadb-deployment-and-administration/ansible-and-mariadb/installing-mariadb-deb-files-with-ansible.md#updating-the-mariadb-apt-repository-to-a-new-major-release) for more information.
  * On RHEL, CentOS, Fedora, and other similar Linux distributions, see [Updating the MariaDB YUM repository to a New Major Release](../binary-packages/rpm/yum.md#updating-the-mariadb-yum-repository-to-a-new-major-release) for more information.
  * On SLES, OpenSUSE, and other similar Linux distributions, see [Updating the MariaDB ZYpp repository to a New Major Release](../binary-packages/rpm/installing-mariadb-with-zypper.md#updating-the-mariadb-zypp-repository-to-a-new-major-release) for more information.
1. [Stop MariaDB](../starting-and-stopping-mariadb/starting-and-stopping-mariadb-automatically.md).
1. Uninstall the old version of MariaDB.

  * On Debian, Ubuntu, and other similar Linux distributions, execute the following: 
`<code class="fixed" style="white-space:pre-wrap">sudo apt-get remove mariadb-server</code>`
  * On RHEL, CentOS, Fedora, and other similar Linux distributions, execute the following: 
`<code class="fixed" style="white-space:pre-wrap">sudo yum remove MariaDB-server</code>`
  * On SLES, OpenSUSE, and other similar Linux distributions, execute the following: 
`<code class="fixed" style="white-space:pre-wrap">sudo zypper remove MariaDB-server</code>`
1. Install the new version of MariaDB.

  * On Debian, Ubuntu, and other similar Linux distributions, see [Installing MariaDB Packages with APT](../binary-packages/automated-mariadb-deployment-and-administration/ansible-and-mariadb/installing-mariadb-deb-files-with-ansible.md#installing-mariadb-packages-with-apt) for more information.
  * On RHEL, CentOS, Fedora, and other similar Linux distributions, see [Installing MariaDB Packages with YUM](../binary-packages/rpm/yum.md#installing-mariadb-packages-with-yum) for more information.
  * On SLES, OpenSUSE, and other similar Linux distributions, see [Installing MariaDB Packages with ZYpp](../binary-packages/rpm/installing-mariadb-with-zypper.md#installing-mariadb-packages-with-zypp) for more information.
1. Make any desired changes to configuration options in [option files](../configuring-mariadb-with-option-files.md), such as `<code>my.cnf</code>`. This includes removing any options that are no longer supported.
1. [Start MariaDB](../starting-and-stopping-mariadb/starting-and-stopping-mariadb-automatically.md).
1. Run [mariadb-upgrade](../../../clients-and-utilities/mariadb-upgrade.md).

  * `<code>mariadb-upgrade</code>` does two things:

    1. Ensures that the system tables in the [mysql](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/the-mysql-database-tables/README.md) database are fully compatible with the new version.
    1. Does a very quick check of all tables and marks them as compatible with the new version of MariaDB .


### Incompatible Changes Between 10.11 and 11.4


On most servers upgrading from 10.11 should be painless. However, there are some things that have changed which could affect an upgrade:


#### Options That Have Been Removed or Renamed


The following options should be removed or renamed if you use them in your [option files](../configuring-mariadb-with-option-files.md):



| Option | Reason |
| --- | --- |
| Option | Reason |
| [debug_no_thread_alarm](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#debug_no_thread_alarm) | Unused code. |
| [innodb_defragment](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_defragment) | [Defragmenting InnoDB Tablespaces](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/optimizing-tables/defragmenting-innodb-tablespaces.md) in this manner no longer supported. |
| [innodb_defragment_fill_factor](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_defragment_fill_factor) | [Defragmenting InnoDB Tablespaces](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/optimizing-tables/defragmenting-innodb-tablespaces.md) in this manner no longer supported. |
| [innodb_defragment_fill_factor_n_recs](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_defragment_fill_factor_n_recs) | [Defragmenting InnoDB Tablespaces](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/optimizing-tables/defragmenting-innodb-tablespaces.md) in this manner no longer supported. |
| [innodb_defragment_frequency](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_defragment_frequency) | [Defragmenting InnoDB Tablespaces](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/optimizing-tables/defragmenting-innodb-tablespaces.md) in this manner no longer supported. |
| [innodb_defragment_n_pages](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_defragment_n_pages) | [Defragmenting InnoDB Tablespaces](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/optimizing-tables/defragmenting-innodb-tablespaces.md) in this manner no longer supported. |
| [innodb_defragment_stats_accuracy](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_defragment_stats_accuracy) | [Defragmenting InnoDB Tablespaces](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/optimizing-tables/defragmenting-innodb-tablespaces.md) in this manner no longer supported. |



#### Options That Have Changed Default Values



| Option | Old default | New default |
| --- | --- | --- |
| Option | Old default | New default |
| [optimizer_switch](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#optimizer_switch) |  | See [optimizer-switch](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/query-optimizations/optimizer-switch.md). |
| [innodb_purge_batch_size](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_purge_batch_size) | 300 | 1000 |



#### Options That Have Been Removed or Renamed


The following options should be removed or renamed if you use them in your [option files](../configuring-mariadb-with-option-files.md):



| Option | Reason |
| --- | --- |
| Option | Reason |
| [old_alter_table](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#old_alter_table) | Superceded by [alter_algorithm](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#alter_algorithm). |



#### Deprecated Options


The following options have been deprecated. They have not yet been removed, but will be in a future version, and should ideally no longer be used.



| Option | Reason |
| --- | --- |
| Option | Reason |
| [innodb_purge_rseg_truncate_frequency](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_purge_rseg_truncate_frequency) | The motivation for introducing this in MySQL seems to have been to avoid stalls due to freeing undo log pages or truncating undo log tablespaces. In MariaDB, [innodb_undo_log_truncate=ON](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_undo_log_truncate) should be a much lighter operation because it will not involve any log checkpoint, hence this is deprecated and ignored |
| [tx_isolation](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#tx_isolation) | Replaced with [transaction_isolation](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#transaction_isolation) to align the option and system variable. |
| [tx_read_only](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#tx_read_only) | Replaced with [transaction_read_only](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#transaction_read_only) to align the option and system variable. |



### See Also


* [Features in MariaDB 11.4](../../../../release-notes/mariadb-community-server/what-is-mariadb-114.md)
* [Features in MariaDB 11.3](../../../../release-notes/mariadb-community-server/what-is-mariadb-113.md)
* [Features in MariaDB 11.2](../../../../release-notes/mariadb-community-server/what-is-mariadb-112.md)
* [Features in MariaDB 11.1](../../../../release-notes/mariadb-community-server/what-is-mariadb-111.md)
* [Features in MariaDB 11.0](../../../../release-notes/mariadb-community-server/what-is-mariadb-110.md)



* [Upgrading from MariaDB 10.6 to MariaDB 10.7 with Galera Cluster](upgrading-from-mariadb-106-to-mariadb-107-with-galera-cluster)



* [Upgrading from MariaDB 10.6 to MariaDB 10.11](upgrading-from-mariadb-10-6-to-mariadb-10-11.md)
* [Upgrading from MariaDB 10.5 to MariaDB 10.6](upgrading-from-mariadb-10-5-to-mariadb-10-6.md)

