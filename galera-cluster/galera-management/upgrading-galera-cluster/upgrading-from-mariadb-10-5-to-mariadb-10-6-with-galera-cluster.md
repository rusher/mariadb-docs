# Upgrading from MariaDB 10.5 to MariaDB 10.6 with Galera Cluster

[Galera Cluster](../../../en/what-is-mariadb-galera-cluster/) ships with the MariaDB Server. Upgrading a Galera Cluster node is very similar to upgrading a server from [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-5-series/what-is-mariadb-105) to [MariaDB 10.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-6-series/what-is-mariadb-106). For more information on that process as well as incompatibilities between versions, see the [Upgrade Guide](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/getting-installing-and-upgrading-mariadb/upgrading/upgrading-from-mariadb-10-5-to-mariadb-10-6).

## Performing a Rolling Upgrade

The following steps can be used to perform a rolling upgrade from [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-5-series/what-is-mariadb-105) to [MariaDB 10.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-6-series/what-is-mariadb-106) when using Galera Cluster. In a rolling upgrade, each node is upgraded individually, so the cluster is always operational. There is no downtime from the application's perspective.

First, before you get started:

1. First, take a look at [Upgrading from MariaDB 10.5 to MariaDB 10.6](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/getting-installing-and-upgrading-mariadb/upgrading/upgrading-from-mariadb-10-5-to-mariadb-10-6) to see what has changed between the major versions.
2. Check whether any system variables or options have been changed or removed. Make sure that your server's configuration is compatible with the new MariaDB version before upgrading.
3. Check whether replication has changed in the new MariaDB version in any way that could cause issues while the cluster contains upgraded and non-upgraded nodes.
4. Check whether any new features have been added to the new MariaDB version. If a new feature in the new MariaDB version cannot be replicated to the old MariaDB version, then do not use that feature until all cluster nodes have been upgrades to the new MariaDB version.
5. Next, make sure that the Galera version numbers are compatible.
6. If you are upgrading from the most recent [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-5-series/what-is-mariadb-105) release to [MariaDB 10.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-6-series/what-is-mariadb-106), then the versions will be compatible.
7. See [What is MariaDB Galera Cluster?: Galera wsrep provider Versions](../../../en/what-is-mariadb-galera-cluster/#galera-wsrep-provider-versions) for information on which MariaDB releases uses which Galera wsrep provider versions.
8. You want to have a large enough gcache to avoid a [State Snapshot Transfer (SST)](../state-snapshot-transfers-ssts-in-galera-cluster/introduction-to-state-snapshot-transfers-ssts.md) during the rolling upgrade. The gcache size can be configured by setting `[gcache.size](../../reference/wsrep_provider_options.md#gcachesize)` For example:`wsrep_provider_options="gcache.size=2G"`

Before you upgrade, it would be best to take a backup of your database. This is always a good idea to do before an upgrade. We would recommend [Mariabackup](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/backing-up-and-restoring-databases/mariabackup).

Then, for each node, perform the following steps:

1. Modify the repository configuration, so the system's package manager installs [MariaDB 10.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-6-series/what-is-mariadb-106). For example,

* On Debian, Ubuntu, and other similar Linux distributions, see [Updating the MariaDB APT repository to a New Major Release](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/getting-installing-and-upgrading-mariadb/binary-packages/installing-mariadb-deb-files#updating-the-mariadb-apt-repository-to-a-new-major-release) for more information.
* On RHEL, CentOS, Fedora, and other similar Linux distributions, see [Updating the MariaDB YUM repository to a New Major Release](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/getting-installing-and-upgrading-mariadb/binary-packages/rpm/yum#updating-the-mariadb-yum-repository-to-a-new-major-release) for more information.
* On SLES, OpenSUSE, and other similar Linux distributions, see [Updating the MariaDB ZYpp repository to a New Major Release](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/getting-installing-and-upgrading-mariadb/binary-packages/rpm/installing-mariadb-with-zypper#updating-the-mariadb-zypp-repository-to-a-new-major-release) for more information.

1. If you use a load balancing proxy such as MaxScale or HAProxy, make sure to drain the server from the pool so it does not receive any new connections.
2. [Stop MariaDB](https://mariadb.com/kb/en/).
3. Uninstall the old version of MariaDB and the Galera wsrep provider.

* On Debian, Ubuntu, and other similar Linux distributions, execute the following:`sudo apt-get remove mariadb-server galera-4`
* On RHEL, CentOS, Fedora, and other similar Linux distributions, execute the following:`sudo yum remove MariaDB-server galera-4`
* On SLES, OpenSUSE, and other similar Linux distributions, execute the following:`sudo zypper remove MariaDB-server galera-4`

1. Install the new version of MariaDB and the Galera wsrep provider.

* On Debian, Ubuntu, and other similar Linux distributions, see [Installing MariaDB Packages with APT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/getting-installing-and-upgrading-mariadb/binary-packages/installing-mariadb-deb-files#installing-mariadb-packages-with-apt) for more information.
* On RHEL, CentOS, Fedora, and other similar Linux distributions, see [Installing MariaDB Packages with YUM](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/getting-installing-and-upgrading-mariadb/binary-packages/rpm/yum#installing-mariadb-packages-with-yum) for more information.
* On SLES, OpenSUSE, and other similar Linux distributions, see [Installing MariaDB Packages with ZYpp](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/getting-installing-and-upgrading-mariadb/binary-packages/rpm/installing-mariadb-with-zypper#installing-mariadb-packages-with-zypp) for more information.

1. Make any desired changes to configuration options in [option files](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files), such as `my.cnf`. This includes removing any system variables or options that are no longer supported.
2. On Linux distributions that use `systemd` you may need to increase the service startup timeout as the default timeout of 90 seconds may not be sufficient. See [Systemd: Configuring the Systemd Service Timeout](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/systemd#configuring-the-systemd-service-timeout) for more information.
3. [Start MariaDB](https://mariadb.com/kb/en/).
4. Run `[mariadb-upgrade](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/mariadb-upgrade)` with the `--skip-write-binlog` option.

* `mariadb-upgrade` does two things:
  1. Ensures that the system tables in the `[mysql](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/the-mysql-database-tables/)` database are fully compatible with the new version.
  2. Does a very quick check of all tables and marks them as compatible with the new version of MariaDB .

When this process is done for one node, move onto the next node.

Note that when upgrading the Galera wsrep provider, sometimes the Galera protocol version can change. The Galera wsrep provider should not start using the new protocol version until all cluster nodes have been upgraded to the new version, so this is not generally an issue during a rolling upgrade. However, this can cause issues if you restart a non-upgraded node in a cluster where the rest of the nodes have been upgraded.

CC BY-SA / Gnu FDL
