
# Upgrading from MariaDB 11.4 to MariaDB 11.8


This page includes details for upgrading from [MariaDB 11.4](../../../../release-notes/mariadb-community-server/what-is-mariadb-114.md) to the subsequent long-term maintenance version, [MariaDB 11.8](../../../../release-notes/mariadb-community-server/what-is-mariadb-118.md).


### How to Upgrade


For Windows, see [Upgrading MariaDB on Windows](upgrading-mariadb-on-windows.md).


For MariaDB Galera Cluster, see [Upgrading from MariaDB 11.4 to MariaDB 11.8 with Galera Cluster](https://mariadb.com/kb/en/upgrading-from-mariadb-11-4-to-mariadb-11-8-with-galeracluster/).


Before you upgrade, it would be best to take a backup of your database. This is always a good idea to do before an upgrade. We would recommend [Mariabackup](../../backing-up-and-restoring-databases/mariabackup/mariabackup-and-backup-stage-commands.md).



The suggested upgrade procedure is:


1. Modify the repository configuration, so the system's package manager installs [MariaDB 11.8](../../../../release-notes/mariadb-community-server/what-is-mariadb-118.md). For example,

  * On Debian, Ubuntu, and other similar Linux distributions, see [Updating the MariaDB APT repository to a New Major Release](../binary-packages/automated-mariadb-deployment-and-administration/ansible-and-mariadb/installing-mariadb-deb-files-with-ansible.md#updating-the-mariadb-apt-repository-to-a-new-major-release) for more information.
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

  * On Debian, Ubuntu, and other similar Linux distributions, see [Installing MariaDB Packages with APT](../binary-packages/automated-mariadb-deployment-and-administration/ansible-and-mariadb/installing-mariadb-deb-files-with-ansible.md#installing-mariadb-packages-with-apt) for more information.
  * On RHEL, CentOS, Fedora, and other similar Linux distributions, see [Installing MariaDB Packages with YUM](../binary-packages/rpm/yum.md#installing-mariadb-packages-with-yum) for more information.
  * On SLES, OpenSUSE, and other similar Linux distributions, see [Installing MariaDB Packages with ZYpp](../binary-packages/rpm/installing-mariadb-with-zypper.md#installing-mariadb-packages-with-zypp) for more information.
1. Make any desired changes to configuration options in [option files](../configuring-mariadb-with-option-files.md), such as `my.cnf`. This includes removing any options that are no longer supported.
1. [Start MariaDB](../starting-and-stopping-mariadb/starting-and-stopping-mariadb-automatically.md).
1. Run [mariadb-upgrade](../../../clients-and-utilities/mariadb-upgrade.md).

  * `mariadb-upgrade` does two things:

    1. Ensures that the system tables in the [mysql](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/the-mysql-database-tables/README.md) database are fully compatible with the new version.
    1. Does a very quick check of all tables and marks them as compatible with the new version of MariaDB .


### Incompatible Changes Between 11.4 and 11.8


On most servers upgrading from 11.4 should be painless. However, there are some things that have changed which could affect an upgrade:


#### Options That Have Been Removed or Renamed


The following options should be removed or renamed if you use them in your [option files](../configuring-mariadb-with-option-files.md):



| Option | Reason |
| --- | --- |
| Option | Reason |
| [wsrep_load_data_splitting](../../../server-usage/replication-cluster-multi-master/galera-cluster/galera-cluster-system-variables.md#wsrep_load_data_splitting) | Deprecated in [MariaDB 10.4](../../../../release-notes/mariadb-community-server/what-is-mariadb-104.md), defaults to OFF. |



#### Options That Have Changed Default Values



| Option | Old default | New default |
| --- | --- | --- |
| Option | Old default | New default |



#### Deprecated Options


The following options have been deprecated. They have not yet been removed, but will be in a future version, and should ideally no longer be used.



| Option | Reason |
| --- | --- |
| Option | Reason |



### See Also


* [Features in MariaDB 11.8](../../../../release-notes/mariadb-community-server/what-is-mariadb-118.md)
* [Features in MariaDB 11.4](../../../../release-notes/mariadb-community-server/what-is-mariadb-114.md)



* [Upgrading from MariaDB 10.6 to MariaDB 10.7 with Galera Cluster](upgrading-from-mariadb-106-to-mariadb-107-with-galera-cluster)



* [Upgrading from MariaDB 10.11 to MariaDB 11.4](upgrading-from-mariadb-10-11-to-mariadb-11-4.md)
* [Upgrading from MariaDB 10.6 to MariaDB 10.11](upgrading-from-mariadb-10-6-to-mariadb-10-11.md)
* [Upgrading from MariaDB 10.5 to MariaDB 10.6](upgrading-from-mariadb-10-5-to-mariadb-10-6.md)

