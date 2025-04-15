
# Upgrading from MariaDB 11.3 to MariaDB 11.4


This page includes details for upgrading from [MariaDB 11.3](../../../../release-notes/mariadb-community-server/what-is-mariadb-113.md) to [MariaDB 11.4](../../../../release-notes/mariadb-community-server/what-is-mariadb-114.md). Note that [MariaDB 11.3](../../../../release-notes/mariadb-community-server/what-is-mariadb-113.md) is a [rolling release](https://mariadb.org/about/#maintenance-policy), and [MariaDB 11.4](../../../../release-notes/mariadb-community-server/what-is-mariadb-114.md) is a [long-term maintenance release](https://mariadb.org/about/#maintenance-policy). After [MariaDB 11.4.2](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-4-series/mariadb-11-4-2-release-notes.md), one can continue to the next rolling release, 11.5.2, 11.6.2 and so on, or remain on the long-term series, [MariaDB 11.4.3](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-4-series/mariadb-11-4-3-release-notes.md). [MariaDB 11.4.4](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-4-series/mariadb-11-4-4-release-notes.md) etc.


### How to Upgrade


For Windows, see [Upgrading MariaDB on Windows](upgrading-mariadb-on-windows.md).


For MariaDB Galera Cluster, see [Upgrading from MariaDB 10.6 to MariaDB 10.7 with Galera Cluster](upgrading-from-mariadb-106-to-mariadb-107-with-galera-cluster) instead.


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


### Incompatible Changes Between 11.3 and 11.4


#### Options That Have Been Removed


The following options should be removed if you use them in your [option files](../configuring-mariadb-with-option-files.md):



| Option | Reason |
| --- | --- |
| Option | Reason |
| [debug_no_thread_alarm](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#debug_no_thread_alarm) | Unused code. |



### See Also


* [Features in MariaDB 11.4](../../../../release-notes/mariadb-community-server/what-is-mariadb-114.md)
* [Features in MariaDB 11.3](../../../../release-notes/mariadb-community-server/what-is-mariadb-113.md)



* [Upgrading from MariaDB 10.6 to MariaDB 10.7 with Galera Cluster](upgrading-from-mariadb-106-to-mariadb-107-with-galera-cluster)



* [Upgrading from MariaDB 11.2 to MariaDB 11.3](upgrading-from-mariadb-11-2-to-mariadb-11-3.md)
* [Upgrading from MariaDB 11.1 to MariaDB 11.2](upgrading-from-mariadb-11-1-to-mariadb-11-2.md)
* [Upgrading from MariaDB 10.11 to MariaDB 11.4](upgrading-from-mariadb-10-11-to-mariadb-11-4.md)

