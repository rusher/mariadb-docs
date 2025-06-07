# Upgrading from MariaDB 10.6 to MariaDB 10.7

Note that [MariaDB 10.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-7-series/what-is-mariadb-107) is [only maintained for one year](https://mariadb.org/about/#maintenance-policy). [MariaDB 10.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-6-series/what-is-mariadb-106) is currently the latest long-term maintenance release.

### How to Upgrade

For Windows, see [Upgrading MariaDB on Windows](../upgrading-mariadb-on-windows.md).

For MariaDB Galera Cluster, see [Upgrading from MariaDB 10.6 to MariaDB 10.7 with Galera Cluster](../../../getting-installing-and-upgrading-mariadb/upgrading/upgrading-to-unmaintained-mariadb-releases/upgrading-from-mariadb-106-to-mariadb-107-with-galera-cluster/) instead.

Before you upgrade, it would be best to take a backup of your database. This is always a good idea to do before an upgrade. We would recommend [Mariabackup](../../../../server-usage/backing-up-and-restoring-databases/mariabackup/).

The suggested upgrade procedure is:

1. Modify the repository configuration, so the system's package manager installs [MariaDB 10.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-7-series/what-is-mariadb-107). For example,

* On Debian, Ubuntu, and other similar Linux distributions, see [Updating the MariaDB APT repository to a New Major Release](../../installing-mariadb/binary-packages/installing-mariadb-deb-files.md#updating-the-mariadb-apt-repository-to-a-new-major-release) for more information.
* On RHEL, CentOS, Fedora, and other similar Linux distributions, see [Updating the MariaDB YUM repository to a New Major Release](../../installing-mariadb/binary-packages/rpm/yum.md#updating-the-mariadb-yum-repository-to-a-new-major-release) for more information.
* On SLES, OpenSUSE, and other similar Linux distributions, see [Updating the MariaDB ZYpp repository to a New Major Release](../../installing-mariadb/binary-packages/rpm/installing-mariadb-with-zypper.md#updating-the-mariadb-zypp-repository-to-a-new-major-release) for more information.

1. [Stop MariaDB](../../../starting-and-stopping-mariadb/starting-and-stopping-mariadb-automatically.md).
2. Uninstall the old version of MariaDB.

* On Debian, Ubuntu, and other similar Linux distributions, execute the following:`sudo apt-get remove mariadb-server`
* On RHEL, CentOS, Fedora, and other similar Linux distributions, execute the following:`sudo yum remove MariaDB-server`
* On SLES, OpenSUSE, and other similar Linux distributions, execute the following:`sudo zypper remove MariaDB-server`

1. Install the new version of MariaDB.

* On Debian, Ubuntu, and other similar Linux distributions, see [Installing MariaDB Packages with APT](../../installing-mariadb/binary-packages/installing-mariadb-deb-files.md#installing-mariadb-packages-with-apt) for more information.
* On RHEL, CentOS, Fedora, and other similar Linux distributions, see [Installing MariaDB Packages with YUM](../../installing-mariadb/binary-packages/rpm/yum.md#installing-mariadb-packages-with-yum) for more information.
* On SLES, OpenSUSE, and other similar Linux distributions, see [Installing MariaDB Packages with ZYpp](../../installing-mariadb/binary-packages/rpm/installing-mariadb-with-zypper.md#installing-mariadb-packages-with-zypp) for more information.

1. Make any desired changes to configuration options in [option files](../../configuring-mariadb/configuring-mariadb-with-option-files.md), such as `my.cnf`. This includes removing any options that are no longer supported.
2. [Start MariaDB](../../../starting-and-stopping-mariadb/starting-and-stopping-mariadb-automatically.md).
3. Run [mariadb-upgrade](../../../../clients-and-utilities/mariadb-upgrade.md).

* `mariadb-upgrade` does two things:
  1. Ensures that the system tables in the [mysql](../../../../reference/sql-statements/administrative-sql-statements/system-tables/the-mysql-database-tables/) database are fully compatible with the new version.
  2. Does a very quick check of all tables and marks them as compatible with the new version of MariaDB .

### Incompatible Changes Between 10.6 and 10.7

On most servers upgrading from 10.6 should be painless. However, there are some things that have changed which could affect an upgrade:

#### Reserved Words

* ROW\_NUMBER is now a [reserved word](../../../../reference/sql-structure/sql-language-structure/reserved-words.md).

#### Compression

If a non-zlib compression algorithm was used in [InnoDB](../../../../reference/storage-engines/innodb/) or [Mroonga](../../../../reference/storage-engines/mroonga/) before upgrading to 10.7, those tables will be unreadable until the appropriate compression library is installed. See [Compression Plugins#Upgrading](../../../../ha-and-performance/optimization-and-tuning/optimization-and-tuning-compression/compression-plugins.md#upgrading).

#### Options That Have Changed Default Values

| Option                                                                                                           | Old default | New default         |
| ---------------------------------------------------------------------------------------------------------------- | ----------- | ------------------- |
| Option                                                                                                           | Old default | New default         |
| [spider\_auto\_increment\_mode](../../../../reference/storage-engines/spider/spider-system-variables.md)         | -1          | 0                   |
| [spider\_bgs\_first\_read](../../../../reference/storage-engines/spider/spider-system-variables.md)              | -1          | 2                   |
| [spider\_bgs\_mode](../../../../reference/storage-engines/spider/spider-system-variables.md)                     | -1          | 0                   |
| [spider\_bgs\_second\_read](../../../../reference/storage-engines/spider/spider-system-variables.md)             | -1          | 100                 |
| [spider\_bka\_mode](../../../../reference/storage-engines/spider/spider-system-variables.md)                     | -1          | 1                   |
| [spider\_bka\_table\_name\_type](../../../../reference/storage-engines/spider/spider-system-variables.md)        | -1          | 1                   |
| [spider\_buffer\_size](../../../../reference/storage-engines/spider/spider-system-variables.md)                  | -1          | 16000               |
| [spider\_bulk\_size](../../../../reference/storage-engines/spider/spider-system-variables.md)                    | -1          | 16000               |
| [spider\_bulk\_update\_mode](../../../../reference/storage-engines/spider/spider-system-variables.md)            | -1          | 0                   |
| [spider\_bulk\_update\_size](../../../../reference/storage-engines/spider/spider-system-variables.md)            | -1          | 16000               |
| [spider\_casual\_read](../../../../reference/storage-engines/spider/spider-system-variables.md)                  | -1          | 0                   |
| [spider\_connect\_timeout](../../../../reference/storage-engines/spider/spider-system-variables.md)              | -1          | 6                   |
| [spider\_crd\_bg\_mode](../../../../reference/storage-engines/spider/spider-system-variables.md)                 | -1          | 2                   |
| [spider\_crd\_interval](../../../../reference/storage-engines/spider/spider-system-variables.md)                 | -1          | 51                  |
| [spider\_crd\_mode](../../../../reference/storage-engines/spider/spider-system-variables.md)                     | -1          | 1                   |
| [spider\_crd\_sync](../../../../reference/storage-engines/spider/spider-system-variables.md)                     | -1          | 0                   |
| [spider\_crd\_type](../../../../reference/storage-engines/spider/spider-system-variables.md)                     | -1          | 2                   |
| [spider\_crd\_weight](../../../../reference/storage-engines/spider/spider-system-variables.md)                   | -1          | 2                   |
| [spider\_delete\_all\_rows\_type](../../../../reference/storage-engines/spider/spider-system-variables.md)       | -1          | 1                   |
| [spider\_direct\_dup\_insert](../../../../reference/storage-engines/spider/spider-system-variables.md)           | -1          | 0                   |
| [spider\_direct\_order\_limit](../../../../reference/storage-engines/spider/spider-system-variables.md)          | -1          | 9223372036854775807 |
| [spider\_error\_read\_mode](../../../../reference/storage-engines/spider/spider-system-variables.md)             | -1          | 0                   |
| [spider\_error\_write\_mode](../../../../reference/storage-engines/spider/spider-system-variables.md)            | -1          | 0                   |
| [spider\_first\_read](../../../../reference/storage-engines/spider/spider-system-variables.md)                   | -1          | 0                   |
| [spider\_init\_sql\_alloc\_size](../../../../reference/storage-engines/spider/spider-system-variables.md)        | -1          | 1024                |
| [spider\_internal\_limit](../../../../reference/storage-engines/spider/spider-system-variables.md)               | -1          | 9223372036854775807 |
| [spider\_internal\_offset](../../../../reference/storage-engines/spider/spider-system-variables.md)              | -1          | 0                   |
| [spider\_internal\_optimize](../../../../reference/storage-engines/spider/spider-system-variables.md)            | -1          | 0                   |
| [spider\_internal\_optimize\_local](../../../../reference/storage-engines/spider/spider-system-variables.md)     | -1          | 0                   |
| [spider\_load\_crd\_at\_startup](../../../../reference/storage-engines/spider/spider-system-variables.md)        | -1          | 1                   |
| [spider\_load\_sts\_at\_startup](../../../../reference/storage-engines/spider/spider-system-variables.md)        | -1          | 1                   |
| [spider\_low\_mem\_read](../../../../reference/storage-engines/spider/spider-system-variables.md)                | -1          | 1                   |
| [spider\_max\_order](../../../../reference/storage-engines/spider/spider-system-variables.md)                    | -1          | 32767               |
| [spider\_multi\_split\_read](../../../../reference/storage-engines/spider/spider-system-variables.md)            | -1          | 100                 |
| [spider\_net\_read\_timeout](../../../../reference/storage-engines/spider/spider-system-variables.md)            | -1          | 600                 |
| [spider\_net\_write\_timeout](../../../../reference/storage-engines/spider/spider-system-variables.md)           | -1          | 600                 |
| [spider\_quick\_mode](../../../../reference/storage-engines/spider/spider-system-variables.md)                   | -1          | 3                   |
| [spider\_quick\_page\_byte](../../../../reference/storage-engines/spider/spider-system-variables.md)             | -1          | 10485760            |
| [spider\_quick\_page\_size](../../../../reference/storage-engines/spider/spider-system-variables.md)             | -1          | 1024                |
| [spider\_read\_only\_mode](../../../../reference/storage-engines/spider/spider-system-variables.md)              | -1          | 0                   |
| [spider\_reset\_sql\_alloc](../../../../reference/storage-engines/spider/spider-system-variables.md)             | -1          | 1                   |
| [spider\_second\_read](../../../../reference/storage-engines/spider/spider-system-variables.md)                  | -1          | 0                   |
| [spider\_selupd\_lock\_mode](../../../../reference/storage-engines/spider/spider-system-variables.md)            | -1          | 1                   |
| [spider\_semi\_split\_read](../../../../reference/storage-engines/spider/spider-system-variables.md)             | -1          | 2                   |
| [spider\_semi\_split\_read\_limit](../../../../reference/storage-engines/spider/spider-system-variables.md)      | -1          | 1                   |
| [spider\_semi\_table\_lock\_connection](../../../../reference/storage-engines/spider/spider-system-variables.md) | -1          | 1                   |
| [spider\_reset\_sql\_alloc](../../../../reference/storage-engines/spider/spider-system-variables.md)             | -1          | 1                   |

#### Options That Have Been Removed or Renamed

The following options should be removed or renamed if you use them in your [option files](../../configuring-mariadb/configuring-mariadb-with-option-files.md):

| Option                                                                                                                                      | Reason                                                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| Option                                                                                                                                      | Reason                                                                                                                          |
| [wsrep\_replicate\_myisam](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_replicate_myisam) | Use [wsrep\_mode](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_mode) instead. |
| [wsrep\_strict\_ddl](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_strict_ddl)             | Use [wsrep\_mode](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_mode) instead. |

### See Also

* [The features in MariaDB 10.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-7-series/what-is-mariadb-107)
* [Upgrading from MariaDB 10.6 to MariaDB 10.7 with Galera Cluster](../../../getting-installing-and-upgrading-mariadb/upgrading/upgrading-to-unmaintained-mariadb-releases/upgrading-from-mariadb-106-to-mariadb-107-with-galera-cluster/)
* [Upgrading from MariaDB 10.5 to MariaDB 10.6](../upgrading-from-to-specific-versions/upgrading-from-mariadb-10-5-to-mariadb-10-6.md)
* [Upgrading from MariaDB 10.4 to MariaDB 10.5](../upgrading-from-to-specific-versions/upgrading-from-mariadb-10-4-to-mariadb-10-5.md)
* [Upgrading from MariaDB 10.3 to MariaDB 10.4](upgrading-from-mariadb-103-to-mariadb-104.md)

CC BY-SA / Gnu FDL
