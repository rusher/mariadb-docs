
# Upgrading from MariaDB 10.3 to MariaDB 10.4


### How to Upgrade


For Windows, see [Upgrading MariaDB on Windows](../upgrading-mariadb-on-windows.md) instead.


For MariaDB Galera Cluster, see [Upgrading from MariaDB 10.3 to MariaDB 10.4 with Galera Cluster](../../../../server-usage/replication-cluster-multi-master/galera-cluster/upgrading-galera-cluster/upgrading-from-mariadb-10-3-to-mariadb-10-4-with-galera-cluster.md) instead.


Before you upgrade, it would be best to take a backup of your database. This is always a good idea to do before an upgrade. We would recommend [Mariabackup](../../../backing-up-and-restoring-databases/mariabackup/mariabackup-and-backup-stage-commands.md).



The suggested upgrade procedure is:


1. Modify the repository configuration, so the system's package manager installs [MariaDB 10.4](../../../../../release-notes/mariadb-community-server/what-is-mariadb-104.md). For example,

  * On Debian, Ubuntu, and other similar Linux distributions, see [Updating the MariaDB APT repository to a New Major Release](../../binary-packages/automated-mariadb-deployment-and-administration/ansible-and-mariadb/installing-mariadb-deb-files-with-ansible.md#updating-the-mariadb-apt-repository-to-a-new-major-release) for more information.
  * On RHEL, CentOS, Fedora, and other similar Linux distributions, see [Updating the MariaDB YUM repository to a New Major Release](../../binary-packages/rpm/yum.md#updating-the-mariadb-yum-repository-to-a-new-major-release) for more information.
  * On SLES, OpenSUSE, and other similar Linux distributions, see [Updating the MariaDB ZYpp repository to a New Major Release](../../binary-packages/rpm/installing-mariadb-with-zypper.md#updating-the-mariadb-zypp-repository-to-a-new-major-release) for more information.
1. [Stop MariaDB](../../starting-and-stopping-mariadb/starting-and-stopping-mariadb-automatically.md).
1. Uninstall the old version of MariaDB.

  * On Debian, Ubuntu, and other similar Linux distributions, execute the following: 
`<code class="fixed" style="white-space:pre-wrap">sudo apt-get remove mariadb-server</code>`
  * On RHEL, CentOS, Fedora, and other similar Linux distributions, execute the following: 
`<code class="fixed" style="white-space:pre-wrap">sudo yum remove MariaDB-server</code>`
  * On SLES, OpenSUSE, and other similar Linux distributions, execute the following: 
`<code class="fixed" style="white-space:pre-wrap">sudo zypper remove MariaDB-server</code>`
1. Install the new version of MariaDB.

  * On Debian, Ubuntu, and other similar Linux distributions, see [Installing MariaDB Packages with APT](../../binary-packages/automated-mariadb-deployment-and-administration/ansible-and-mariadb/installing-mariadb-deb-files-with-ansible.md#installing-mariadb-packages-with-apt) for more information.
  * On RHEL, CentOS, Fedora, and other similar Linux distributions, see [Installing MariaDB Packages with YUM](../../binary-packages/rpm/yum.md#installing-mariadb-packages-with-yum) for more information.
  * On SLES, OpenSUSE, and other similar Linux distributions, see [Installing MariaDB Packages with ZYpp](../../binary-packages/rpm/installing-mariadb-with-zypper.md#installing-mariadb-packages-with-zypp) for more information.
1. Make any desired changes to configuration options in [option files](../../configuring-mariadb-with-option-files.md), such as `<code>my.cnf</code>`. This includes removing any options that are no longer supported.
1. [Start MariaDB](../../starting-and-stopping-mariadb/starting-and-stopping-mariadb-automatically.md).
1. Run `<code>[mysql_upgrade](../../../../clients-and-utilities/legacy-clients-and-utilities/mysql_upgrade.md)</code>`.

  * `<code>mysql_upgrade</code>` does two things:

    1. Ensures that the system tables in the `<code>[mysq](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/the-mysql-database-tables/README.md)l</code>` database are fully compatible with the new version.
    1. Does a very quick check of all tables and marks them as compatible with the new version of MariaDB .


### Incompatible Changes Between 10.3 and 10.4


On most servers upgrading from 10.3 should be painless. However, there are some things that have changed which could affect an upgrade:


#### Options That Have Changed Default Values



| Option | Old default value | New default value |
| --- | --- | --- |
| Option | Old default value | New default value |
| [slave_transaction_retry_errors](../../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md#slave_transaction_retry_errors) | 1213,1205 | 1158,1159,1160,1161,1205,1213,1429,2013,12701 |
| [wsrep_debug](../../../../server-usage/replication-cluster-multi-master/galera-cluster/galera-cluster-system-variables.md#wsrep_debug) | OFF | NONE |
| [wsrep_load_data_splitting](../../../../server-usage/replication-cluster-multi-master/galera-cluster/galera-cluster-system-variables.md#wsrep_load_data_splitting) | ON | OFF |



#### Options That Have Been Removed or Renamed


The following options should be removed or renamed if you use them in your [option files](../../configuring-mariadb-with-option-files.md):



| Option | Reason |
| --- | --- |
| Option | Reason |



#### Authentication and TLS


* See [Authentication from MariaDB 10.4](../../../../security/user-account-management/authentication-from-mariadb-10-4.md) for an overview of the changes.
* The [unix_socket authentication plugin](../../../../reference/plugins/authentication-plugins/authentication-plugin-unix-socket.md) is now default on Unix-like systems.
* TLSv1.0 is disabled by default in [MariaDB 10.4](../../../../../release-notes/mariadb-community-server/what-is-mariadb-104.md). See [tls_version](../../../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/ssltls-system-variables.md#tls_version) and [TLS Protocol Versions](../../../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/secure-connections-overview.md#tls-protocol-versions).


### Major New Features To Consider


You might consider using the following major new features in [MariaDB 10.4](../../../../../release-notes/mariadb-community-server/what-is-mariadb-104.md):


* [Galera](../../../../server-usage/replication-cluster-multi-master/galera-cluster/galera-cluster-status-variables.md) has been upgraded from [Galera](../../../../server-usage/replication-cluster-multi-master/galera-cluster/galera-cluster-status-variables.md) 3 to [Galera](../../../../server-usage/replication-cluster-multi-master/galera-cluster/galera-cluster-status-variables.md) 4.
* [System-versioning](../../../../reference/sql-statements-and-structure/temporal-tables/system-versioned-tables.md) extended with support for [application-time periods](../../../../reference/sql-statements-and-structure/temporal-tables/system-versioned-tables.md).
* [User password expiry](../../../../security/user-account-management/user-password-expiry.md)
* [Account Locking](../../../../security/user-account-management/account-locking.md)
* See also [System Variables Added in MariaDB 10.4](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/system-and-status-variables-added-by-major-release/system-and-status-variables-added-by-major-unmaintained-release/system-variables-added-in-mariadb-10-4.md).


### See Also


* [The features in MariaDB 10.4](../../../../../release-notes/mariadb-community-server/what-is-mariadb-104.md)
* [Upgrading from MariaDB 10.3 to MariaDB 10.4 with Galera Cluster](../../../../server-usage/replication-cluster-multi-master/galera-cluster/upgrading-galera-cluster/upgrading-from-mariadb-10-3-to-mariadb-10-4-with-galera-cluster.md)
* [Upgrading from MariaDB 10.2 to MariaDB 10.3](upgrading-from-mariadb-102-to-mariadb-103.md)
* [Upgrading from MariaDB 10.1 to MariaDB 10.2](upgrading-from-mariadb-101-to-mariadb-102.md)
* [Upgrading from MariaDB 10.0 to MariaDB 10.1](upgrading-from-mariadb-100-to-mariadb-101.md)

