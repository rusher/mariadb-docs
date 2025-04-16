
# Upgrading from MariaDB 10.11 to MariaDB 11.0


This page includes details for upgrading from [MariaDB 10.11](../../../../../release-notes/mariadb-community-server/what-is-mariadb-1011.md) to [MariaDB 11.0](../../../../../release-notes/mariadb-community-server/what-is-mariadb-110.md). It is currently incomplete. Note that [MariaDB 10.11](../../../../../release-notes/mariadb-community-server/what-is-mariadb-1011.md) is [maintained for five years](https://mariadb.org/about/#maintenance-policy), while [MariaDB 11.0](../../../../../release-notes/mariadb-community-server/what-is-mariadb-110.md) is a short-term maintenance release, only maintained for one year.


### How to Upgrade


For Windows, see [Upgrading MariaDB on Windows](../upgrading-mariadb-on-windows.md).


For MariaDB Galera Cluster, see [Upgrading from MariaDB 10.6 to MariaDB 10.7 with Galera Cluster](upgrading-from-mariadb-106-to-mariadb-107-with-galera-cluster) instead.


Before you upgrade, it would be best to take a backup of your database. This is always a good idea to do before an upgrade. We would recommend [Mariabackup](../../../backing-up-and-restoring-databases/mariabackup/mariabackup-and-backup-stage-commands.md).



The suggested upgrade procedure is:


1. Modify the repository configuration, so the system's package manager installs [MariaDB 11.0](../../../../../release-notes/mariadb-community-server/what-is-mariadb-110.md). For example,

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


### Incompatible Changes Between 10.11 and 11.0


On most servers upgrading from 10.11 should be painless. However, there are some things that have changed which could affect an upgrade:


#### Options That Have Changed Default Values



| Option | Old default | New default |
| --- | --- | --- |
| Option | Old default | New default |
| [innodb_undo_tablespaces](../../../../ref/storage-engines/innodb/innodb-system-variables.md#innodb_undo_tablespaces) | 0 | 3 |
| [histogram_type](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#histogram_type) | DOUBLE_PREC_HB | JSON_HB |



#### Options That Have Been Removed or Renamed


The following options should be removed or renamed if you use them in your [option files](../../configuring-mariadb-with-option-files.md):



| Option | Reason |
| --- | --- |
| Option | Reason |
| [innodb_change_buffer_max_size](../../../../ref/storage-engines/innodb/innodb-system-variables.md#innodb_change_buffer_max_size) | [InnoDB Change Buffer removed](../../../../ref/storage-engines/innodb/innodb-change-buffering.md) |
| [innodb_change_buffering](../../../../ref/storage-engines/innodb/innodb-system-variables.md#innodb_change_buffering) | [InnoDB Change Buffer removed](../../../../ref/storage-engines/innodb/innodb-change-buffering.md) |



#### Deprecated Options


The following options have been deprecated. They have not yet been removed, but will be in a future version, and should ideally no longer be used.



| Option | Reason |
| --- | --- |
| Option | Reason |
| [innodb_defragment](../../../../ref/storage-engines/innodb/innodb-system-variables.md#innodb_defragment) | [InnoDB Defragmentation](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/optimizing-tables/defragmenting-innodb-tablespaces.md#innodb-defragmentation) is not particularly useful and causes a maintenance burden. |
| [innodb_defragment_n_pages](../../../../ref/storage-engines/innodb/innodb-system-variables.md#innodb_defragment_n_pages) |  |
| [innodb_defragment_stats_accuracy](../../../../ref/storage-engines/innodb/innodb-system-variables.md#innodb_defragment_stats_accuracy) |  |
| [innodb_defragment_fill_factor_n_recs](../../../../ref/storage-engines/innodb/innodb-system-variables.md#innodb_defragment_fill_factor_n_recs) |  |
| [innodb_defragment_fill_factor](../../../../ref/storage-engines/innodb/innodb-system-variables.md#innodb_defragment_fill_factor) |  |
| [innodb_defragment_frequency](../../../../ref/storage-engines/innodb/innodb-system-variables.md#innodb_defragment_frequency) |  |
| [innodb_file_per_table](../../../../ref/storage-engines/innodb/innodb-system-variables.md#innodb_file_per_table) |  |
| [innodb_flush_method](../../../../ref/storage-engines/innodb/innodb-system-variables.md#innodb_flush_method) |  |
| [innodb_file_per_table](../../../../ref/storage-engines/innodb/innodb-system-variables.md#innodb_file_per_table) | Has been set for many releases. Unsetting (the original InnoDB default) is no longer useful |
| [innodb_flush_method](../../../../ref/storage-engines/innodb/innodb-system-variables.md#innodb_flush_method) | Mapped it to 4 new boolean parameters that can be changed while the server is running |
| [log_slow_admin_statements](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#log_slow_admin_statements) | Use [log_slow_filter](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#log_slow_filter) without admin |



### See Also


* [Features in MariaDB 11.0](/en/what-is-mariadb-11-0/)
* [Features in MariaDB 10.11](../../../../../release-notes/mariadb-community-server/what-is-mariadb-1011.md)



* [Upgrading from MariaDB 10.6 to MariaDB 10.7 with Galera Cluster](upgrading-from-mariadb-106-to-mariadb-107-with-galera-cluster)



* [Upgrading from MariaDB 10.6 to MariaDB 10.11](../upgrading-from-mariadb-10-6-to-mariadb-10-11.md)
* [Upgrading from MariaDB 10.7 to MariaDB 10.8](upgrading-from-mariadb-10-7-to-mariadb-10-8.md)
* [Upgrading from MariaDB 10.6 to MariaDB 10.7](upgrading-from-mariadb-10-6-to-mariadb-10-7.md)

