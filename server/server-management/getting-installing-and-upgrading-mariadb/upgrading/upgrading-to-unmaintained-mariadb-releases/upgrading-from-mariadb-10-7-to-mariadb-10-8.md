
# Upgrading from MariaDB 10.7 to MariaDB 10.8


### How to Upgrade


For Windows, see [Upgrading MariaDB on Windows](../upgrading-mariadb-on-windows.md).


For MariaDB Galera Cluster, see [Upgrading from MariaDB 10.7 to MariaDB 10.8 with Galera Cluster](https://mariadb.com/kb/en/upgrading-from-mariadb-107-to-mariadb-108-with-galera-cluster) instead.


Before you upgrade, it would be best to take a backup of your database. This is always a good idea to do before an upgrade. We would recommend [Mariabackup](../../../backing-up-and-restoring-databases/mariabackup/mariabackup-and-backup-stage-commands.md).



The suggested upgrade procedure is:


1. Modify the repository configuration, so the system's package manager installs [MariaDB 10.8](../../../../../release-notes/mariadb-community-server/what-is-mariadb-108.md). For example,

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

    1. Ensures that the system tables in the [mysql](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/the-mysql-database-tables/README.md) database are fully compatible with the new version.
    1. Does a very quick check of all tables and marks them as compatible with the new version of MariaDB .


### Incompatible Changes Between 10.7 and 10.8


On most servers upgrading from 10.7 should be painless. However, there are some things that have changed which could affect an upgrade:


#### Options That Have Changed Default Values



| Option | Old default value | New default value |
| --- | --- | --- |
| Option | Old default value | New default value |
| [innodb_buffer_pool_chunk_size](../../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_buffer_pool_chunk_size) | 134217728 | Autosized |
| [spider_semi_table_lock](../../../../reference/storage-engines/spider/spider-system-variables.md) | 1 | 0 |



#### Options That Have Been Removed or Renamed


The following options should be removed or renamed if you use them in your [option files](../../configuring-mariadb-with-option-files.md):



| Option | Reason |
| --- | --- |
| Option | Reason |
| [innodb_log_write_ahead_size](../../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_log_write_ahead_size) | On Linux and Windows, the physical block size of the underlying storage is instead detected and used. |



#### Deprecated Options


The following options have been deprecated. They have not yet been removed, but will be in a future version, and should ideally no longer be used.



| Option | Reason |
| --- | --- |
| Option | Reason |
| [keep_files_on_create](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#keep_files_on_create) | MariaDB now deletes orphan files, so this setting should never be necessary. |



### Major New Features To Consider


You might consider using the following major new features in [MariaDB 10.8](../../../../../release-notes/mariadb-community-server/what-is-mariadb-108.md):


* Stored procedures already have support for the [IN, OUT and INOUT](../../../../server-usage/programming-customizing-mariadb/stored-routines/stored-procedures/create-procedure.md#inoutinout) parameter qualifiers. Added as well for [stored functions](../../../../reference/sql-statements-and-structure/sql-statements/data-definition/create/create-function.md#in-out-inout-in-out) and (IN only) [cursors](../../../../server-usage/programming-customizing-mariadb/programmatic-compound-statements/programmatic-compound-statements-cursors/declare-cursor.md#in) ([MDEV-10654](https://jira.mariadb.org/browse/MDEV-10654)).
* Individual columns in the [index](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/optimization-and-indexes/README.md) can now be explicitly sorted in the ascending or descending order. This can be useful for optimizing certain [ORDER BY](../../../../reference/sql-statements-and-structure/sql-statements/data-manipulation/selecting-data/order-by.md) cases ([MDEV-13756](https://jira.mariadb.org/browse/MDEV-13756), [MDEV-26938](https://jira.mariadb.org/browse/MDEV-26938), [MDEV-26939](https://jira.mariadb.org/browse/MDEV-26939), [MDEV-26996](https://jira.mariadb.org/browse/MDEV-26996)).
* See also [System Variables Added in MariaDB 10.8](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/system-and-status-variables-added-by-major-release/system-and-status-variables-added-by-major-unmaintained-release/system-variables-added-in-mariadb-10-8.md).


### See Also


* [The features in MariaDB 10.8](../../../../../release-notes/mariadb-community-server/what-is-mariadb-108.md)



* [Upgrading from MariaDB 10.7 to MariaDB 10.7 with Galera Cluster](upgrading-from-mariadb-107-to-mariadb-108-with-galera-cluster)



* [Upgrading from MariaDB 10.6 to MariaDB 10.7](upgrading-from-mariadb-10-6-to-mariadb-10-7.md)
* [Upgrading from MariaDB 10.5 to MariaDB 10.6](../upgrading-from-mariadb-10-5-to-mariadb-10-6.md)
* [Upgrading from MariaDB 10.4 to MariaDB 10.5](../upgrading-from-mariadb-10-4-to-mariadb-10-5.md)

