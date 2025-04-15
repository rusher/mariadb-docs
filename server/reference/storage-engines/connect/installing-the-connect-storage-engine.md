
# Installing the CONNECT Storage Engine

The `<code>CONNECT</code>` storage engine enables MariaDB to access external local or remote data (MED). This is done by defining tables based on different data types, in particular files in various formats, data extracted from other DBMS or products (such as Excel or MongoDB) via ODBC or JDBC, or data retrieved from the environment (for example DIR, WMI, and MAC tables)


This storage engine supports table partitioning, MariaDB virtual columns and permits defining special columns such as ROWID, FILEID, and SERVID.


The storage engine must be installed before it can be used.



## Installing the Plugin's Package


The `<code>CONNECT</code>` storage engine's shared library is included in MariaDB packages as the `<code>ha_connect.so</code>` or `<code>ha_connect.so</code>` shared library on systems where it can be built.


### Installing on Linux


The `<code>CONNECT</code>` storage engine is included in [binary tarballs](../../../server-management/getting-installing-and-upgrading-mariadb/binary-packages/installing-mariadb-binary-tarballs.md) on Linux.


#### Installing with a Package Manager


The `<code>CONNECT</code>` storage engine can also be installed via a package manager on Linux. In order to do so, your system needs to be configured to install from one of the MariaDB repositories.


You can configure your package manager to install it from MariaDB Corporation's MariaDB Package Repository by using the [MariaDB Package Repository setup script](../../../server-management/getting-installing-and-upgrading-mariadb/binary-packages/mariadb-package-repository-setup-and-usage.md).


You can also configure your package manager to install it from MariaDB Foundation's MariaDB Repository by using the [MariaDB Repository Configuration Tool](https://downloads.mariadb.org/mariadb/repositories/).


##### Installing with yum/dnf


On RHEL, CentOS, Fedora, and other similar Linux distributions, it is highly recommended to install the relevant [RPM package](../../../server-management/getting-installing-and-upgrading-mariadb/binary-packages/rpm/README.md) from MariaDB's
repository using `<code>[yum](../../../server-management/getting-installing-and-upgrading-mariadb/binary-packages/rpm/yum.md)</code>` or `<code>[dnf](https://en.wikipedia.org/wiki/DNF_(software))</code>`. Starting with RHEL 8 and Fedora 22, `<code>yum</code>` has been replaced by `<code>dnf</code>`, which is the next major version of `<code>yum</code>`. However, `<code>yum</code>` commands still work on many systems that use `<code>dnf</code>`. For example:


```
sudo yum install MariaDB-connect-engine
```

##### Installing with apt-get


On Debian, Ubuntu, and other similar Linux distributions, it is highly recommended to install the relevant [DEB package](../../../server-management/getting-installing-and-upgrading-mariadb/binary-packages/automated-mariadb-deployment-and-administration/ansible-and-mariadb/installing-mariadb-deb-files-with-ansible.md) from MariaDB's
repository using `<code>[apt-get](https://wiki.debian.org/apt-get)</code>`. For example:


```
sudo apt-get install mariadb-plugin-connect
```

##### Installing with zypper


On SLES, OpenSUSE, and other similar Linux distributions, it is highly recommended to install the relevant [RPM package](../../../server-management/getting-installing-and-upgrading-mariadb/binary-packages/rpm/README.md) from MariaDB's repository using `<code>[zypper](../../../server-management/getting-installing-and-upgrading-mariadb/binary-packages/rpm/installing-mariadb-with-zypper.md)</code>`. For example:


```
sudo zypper install MariaDB-connect-engine
```

## Installing the Plugin


Once the shared library is in place, the plugin is not actually installed by MariaDB by default. There are two methods that can be used to install the plugin with MariaDB.


The first method can be used to install the plugin without restarting the server. You can install the plugin dynamically by executing `<code>[INSTALL SONAME](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/install-soname.md)</code>` or `<code>[INSTALL PLUGIN](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/install-plugin.md)</code>`. For example:


```
INSTALL SONAME 'ha_connect';
```

The second method can be used to tell the server to load the plugin when it starts up. The plugin can be installed this way by providing the `<code>[--plugin-load](../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md)</code>` or the `<code>[--plugin-load-add](../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md)</code>` options. This can be specified as a command-line argument to `<code>[mysqld](../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md)</code>` or it can be specified in a relevant server [option group](../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md). For example:


```
[mariadb]
...
plugin_load_add = ha_connect
```

## Uninstalling the Plugin


You can uninstall the plugin dynamically by executing `<code>[UNINSTALL SONAME](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-soname.md)</code>` or `<code>[UNINSTALL PLUGIN](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-plugin.md)</code>`. For example:


```
UNINSTALL SONAME 'ha_connect';
```

If you installed the plugin by providing the `<code>[--plugin-load](../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md)</code>` or the `<code>[--plugin-load-add](../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md)</code>` options in a relevant server [option group](../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md), then those options should be removed to prevent the plugin from being loaded the next time the server is restarted.


## Installing Dependencies


The `<code>CONNECT</code>` storage engine has some external dependencies.


### Installing unixODBC


The `<code>CONNECT</code>` storage engine requires an ODBC library. On Unix-like systems, that usually means installing [unixODBC](https://www.unixodbc.org/). On some systems, this is installed as the `<code>unixODBC</code>` package. For example:


```
sudo yum install unixODBC
```

On other systems, this is installed as the `<code>libodbc1</code>` package. For example:


```
sudo apt-get install libodbc1
```

If you do not have the ODBC library installed, then you may get an error about a missing library when you attempt to install the plugin. For example:


```
INSTALL SONAME 'ha_connect';
ERROR 1126 (HY000): Can't open shared library '/home/ian/MariaDB_Downloads/10.1.17/lib/plugin/ha_connect.so' 
  (errno: 2, libodbc.so.1: cannot open shared object file: No such file or directory)
```

## See Also


* [PLUGIN OVERVIEW](../../plugins/plugin-overview.md)

