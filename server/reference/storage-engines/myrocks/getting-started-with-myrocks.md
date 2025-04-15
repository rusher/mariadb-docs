
# Getting Started with MyRocks

MyRocks is a storage engine that adds the RocksDB database to MariaDB. RocksDB is an LSM database with a great compression ratio that is optimized for flash storage.


The storage engine must be installed before it can be used.



## Installing the Plugin's Package


The MyRocks storage engine's shared library is included in MariaDB packages as the `<code>ha_rocksdb.so</code>` or `<code>ha_rocksdb.dll</code>` shared library on systems where it can be built.


### Installing on Linux


The MyRocks storage engine is included in [binary tarballs](../../../server-management/getting-installing-and-upgrading-mariadb/binary-packages/installing-mariadb-binary-tarballs.md) on Linux.


#### Installing with a Package Manager


The MyRocks storage engine can also be installed via a package manager on Linux. In order to do so, your system needs to be configured to install from one of the MariaDB repositories.


You can configure your package manager to install it from MariaDB Corporation's MariaDB Package Repository by using the [MariaDB Package Repository setup script](../../../server-management/getting-installing-and-upgrading-mariadb/binary-packages/mariadb-package-repository-setup-and-usage.md).


You can also configure your package manager to install it from MariaDB Foundation's MariaDB Repository by using the [MariaDB Repository Configuration Tool](https://downloads.mariadb.org/mariadb/repositories/).


##### Installing with yum/dnf


On RHEL, CentOS, Fedora, and other similar Linux distributions, it is highly recommended to install the relevant [RPM package](../../../server-management/getting-installing-and-upgrading-mariadb/binary-packages/rpm/README.md) from MariaDB's
repository using `<code>[yum](../../../server-management/getting-installing-and-upgrading-mariadb/binary-packages/rpm/yum.md)</code>` or `<code>[dnf](https://en.wikipedia.org/wiki/DNF_(software))</code>`. Starting with RHEL 8 and Fedora 22, `<code>yum</code>` has been replaced by `<code>dnf</code>`, which is the next major version of `<code>yum</code>`. However, `<code>yum</code>` commands still work on many systems that use `<code>dnf</code>`. For example:


```
sudo yum install MariaDB-rocksdb-engine
```

##### Installing with apt-get


On Debian, Ubuntu, and other similar Linux distributions, it is highly recommended to install the relevant [DEB package](../../../server-management/getting-installing-and-upgrading-mariadb/binary-packages/automated-mariadb-deployment-and-administration/ansible-and-mariadb/installing-mariadb-deb-files-with-ansible.md) from MariaDB's
repository using `<code>[apt-get](https://wiki.debian.org/apt-get)</code>`. For example:


```
sudo apt-get install mariadb-plugin-rocksdb
```

##### Installing with zypper


On SLES, OpenSUSE, and other similar Linux distributions, it is highly recommended to install the relevant [RPM package](../../../server-management/getting-installing-and-upgrading-mariadb/binary-packages/rpm/README.md) from MariaDB's repository using `<code>[zypper](../../../server-management/getting-installing-and-upgrading-mariadb/binary-packages/rpm/installing-mariadb-with-zypper.md)</code>`. For example:


```
sudo zypper install MariaDB-rocksdb-engine
```

### Installing on Windows


The MyRocks storage engine is included in [MSI](../../../server-management/getting-installing-and-upgrading-mariadb/binary-packages/installing-mariadb-msi-packages-on-windows.md) and [ZIP](../../../server-management/getting-installing-and-upgrading-mariadb/binary-packages/installing-mariadb-windows-zip-packages.md) packages on Windows.


## Installing the Plugin


Once the shared library is in place, the plugin is not actually installed by MariaDB by default. There are two methods that can be used to install the plugin with MariaDB.


The first method can be used to install the plugin without restarting the server. You can install the plugin dynamically by executing `<code>[INSTALL SONAME](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/install-soname.md)</code>` or `<code>[INSTALL PLUGIN](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/install-plugin.md)</code>`. For example:


```
INSTALL SONAME 'ha_rocksdb';
```

The second method can be used to tell the server to load the plugin when it starts up. The plugin can be installed this way by providing the `<code>[--plugin-load](../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md)</code>` or the `<code>[--plugin-load-add](../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md)</code>` options. This can be specified as a command-line argument to `<code>[mysqld](../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md)</code>` or it can be specified in a relevant server [option group](../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md). For example:


```
[mariadb]
...
plugin_load_add = ha_rocksdb
```

Note: When installed with a package manager, an option file that contains the `<code>[--plugin-load-add](../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md)</code>` option may also be installed. The RPM package installs it as `<code>/etc/my.cnf.d/rocksdb.cnf</code>`, and the DEB package installs it as `<code>/etc/mysql/mariadb.conf.d/rocksdb.cnf</code>`


## Uninstalling the Plugin


You can uninstall the plugin dynamically by executing `<code>[UNINSTALL SONAME](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-soname.md)</code>` or `<code>[UNINSTALL PLUGIN](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-plugin.md)</code>`. For example:


```
UNINSTALL SONAME 'ha_rocksdb';
```

If you installed the plugin by providing the `<code>[--plugin-load](../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md)</code>` or the `<code>[--plugin-load-add](../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md)</code>` options in a relevant server [option group](../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md), then those options should be removed to prevent the plugin from being loaded the next time the server is restarted.


## Verifying the Installation


After installing MyRocks you will see RocksDB in the list of plugins:


```
SHOW PLUGINS;
+-------------------------------+----------+--------------------+---------------+---------+
| Name                          | Status   | Type               | Library       | License |
+-------------------------------+----------+--------------------+---------------+---------+
...
| ROCKSDB                       | ACTIVE   | STORAGE ENGINE     | ha_rocksdb.so | GPL     |
| ROCKSDB_CFSTATS               | ACTIVE   | INFORMATION SCHEMA | ha_rocksdb.so | GPL     |
| ROCKSDB_DBSTATS               | ACTIVE   | INFORMATION SCHEMA | ha_rocksdb.so | GPL     |
| ROCKSDB_PERF_CONTEXT          | ACTIVE   | INFORMATION SCHEMA | ha_rocksdb.so | GPL     |
| ROCKSDB_PERF_CONTEXT_GLOBAL   | ACTIVE   | INFORMATION SCHEMA | ha_rocksdb.so | GPL     |
| ROCKSDB_CF_OPTIONS            | ACTIVE   | INFORMATION SCHEMA | ha_rocksdb.so | GPL     |
| ROCKSDB_COMPACTION_STATS      | ACTIVE   | INFORMATION SCHEMA | ha_rocksdb.so | GPL     |
| ROCKSDB_GLOBAL_INFO           | ACTIVE   | INFORMATION SCHEMA | ha_rocksdb.so | GPL     |
| ROCKSDB_DDL                   | ACTIVE   | INFORMATION SCHEMA | ha_rocksdb.so | GPL     |
| ROCKSDB_INDEX_FILE_MAP        | ACTIVE   | INFORMATION SCHEMA | ha_rocksdb.so | GPL     |
| ROCKSDB_LOCKS                 | ACTIVE   | INFORMATION SCHEMA | ha_rocksdb.so | GPL     |
| ROCKSDB_TRX                   | ACTIVE   | INFORMATION SCHEMA | ha_rocksdb.so | GPL     |
...
+-------------------------------+----------+--------------------+---------------+---------+
```

## Compression


Supported compression types are listed in the [rocksdb_supported_compression_types](myrocks-system-variables.md#rocksdb_supported_compression_types) variable. For example:


```
SHOW VARIABLES LIKE 'rocksdb_supported_compression_types';
+-------------------------------------+-------------+
| Variable_name                       | Value       |
+-------------------------------------+-------------+
| rocksdb_supported_compression_types | Snappy,Zlib |
+-------------------------------------+-------------+
```

See [MyRocks and Data Compression](myrocks-and-data-compression.md) for more.


## System and Status Variables


All MyRocks [system variables](myrocks-system-variables.md) and [status variables](myrocks-status-variables.md) are prefaced with "rocksdb", so you can query them with, for example:


```
SHOW VARIABLES LIKE 'rocksdb%';
SHOW STATUS LIKE 'rocksdb%';
```
