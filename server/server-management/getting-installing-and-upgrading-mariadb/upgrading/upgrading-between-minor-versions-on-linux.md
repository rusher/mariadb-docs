# Upgrading Between Minor Versions on Linux

For Windows, see [Upgrading MariaDB on Windows](upgrading-mariadb-on-windows.md) instead.

For MariaDB Galera Cluster, see [Upgrading Between Minor Versions with Galera Cluster](/kb/en/upgrading-between-minor-versions-with-galera-cluster/) instead.

Before you upgrade, it would be best to take a backup of your database. This is always a good idea to do before an upgrade. We would recommend [Mariabackup](../../../server-usage/replication-cluster-multi-master/galera-cluster/state-snapshot-transfers-ssts-in-galera-cluster/mariabackup-sst-method.md).

To upgrade between minor versions of MariaDB on Linux/Unix (for example from [MariaDB 10.11.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/release-notes-mariadb-1011-series/mariadb-10-11-4-release-notes) to [MariaDB 10.11.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/release-notes-mariadb-1011-series/mariadb-10-11-5-release-notes)), the following procedure is suggested:
1. [Stop MariaDB](/kb/en/starting-and-stopping-mariadb-starting-and-stopping-mariadb/).
1. Uninstall the old version of MariaDB.
1. Install the new version of MariaDB.

 * On Debian, Ubuntu, and other similar Linux distributions, see [Installing MariaDB Packages with APT](../binary-packages/installing-mariadb-deb-files.md#installing-mariadb-packages-with-apt) for more information.
 * On RHEL, CentOS, Fedora, and other similar Linux distributions, see [Installing MariaDB Packages with YUM](../binary-packages/rpm/yum.md#installing-mariadb-packages-with-yum) for more information.
 * On SLES, OpenSUSE, and other similar Linux distributions, see [Installing MariaDB Packages with ZYpp](../binary-packages/rpm/installing-mariadb-with-zypper.md#installing-mariadb-packages-with-zypp) for more information.
1. Make any desired changes to configuration options in [option files](../configuring-mariadb-with-option-files.md), such as `my.cnf`.
1. [Start MariaDB](/kb/en/starting-and-stopping-mariadb-starting-and-stopping-mariadb/).

To upgrade between major versions, see the following:

* [Upgrading Between Major MariaDB Versions](upgrading-between-major-mariadb-versions.md)
* [Upgrading from MariaDB 11.1 to MariaDB 11.2](upgrading-from-mariadb-11-1-to-mariadb-11-2.md)
* [Upgrading from MariaDB 11.0 to MariaDB 11.1](upgrading-to-unmaintained-mariadb-releases/upgrading-from-mariadb-11-0-to-mariadb-11-1.md)
* [Upgrading from MariaDB 10.11 to MariaDB 11.0](upgrading-to-unmaintained-mariadb-releases/upgrading-from-mariadb-10-11-to-mariadb-11-0.md)
* [Upgrading from MariaDB 10.6 to MariaDB 10.11](../../../server-usage/replication-cluster-multi-master/galera-cluster/upgrading-galera-cluster/upgrading-from-mariadb-10-6-to-mariadb-10-11-with-galeracluster.md)
* [Upgrading from MariaDB 10.5 to MariaDB 10.6](../../../server-usage/replication-cluster-multi-master/galera-cluster/upgrading-galera-cluster/upgrading-from-mariadb-10-5-to-mariadb-10-6-with-galera-cluster.md)
* [Upgrading from MariaDB 10.4 to MariaDB 10.5](/kb/en/upgrading-from-mariadb-104-to-mariadb-105/)
* [Upgrading from MariaDB 10.3 to MariaDB 10.4](upgrading-to-unmaintained-mariadb-releases/upgrading-from-mariadb-103-to-mariadb-104.md)