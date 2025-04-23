
# Configuring MariaDB with Option Files


You can configure MariaDB to run the way you want by configuring the server with MariaDB's option files. The default MariaDB option file is called `my.cnf` (or `mariadb.cnf`) on Unix-like operating systems and `my.ini` on Windows. Depending on how you've [installed](README.md) MariaDB, the default option file may be in a number of places, or it may not exist at all.


## Global Options Related to Option Files


The following options relate to how MariaDB handles option files. These options can be used with most of MariaDB's command-line tools, not just [mariadbd](starting-and-stopping-mariadb/mariadbd-options.md). They must be given as the first argument on the command-line:



| Option | Description |
| --- | --- |
| Option | Description |
| [--print-defaults](starting-and-stopping-mariadb/mariadbd-options.md#-print-defaults) | Read options from option files, print all option values, and then exit the program. |
| [--no-defaults](starting-and-stopping-mariadb/mariadbd-options.md#-no-defaults) | Don't read options from any option file. |
| [--defaults-file](starting-and-stopping-mariadb/mariadbd-options.md#-defaults-file) =path | Only read options from the given option file. |
| [--defaults-extra-file](starting-and-stopping-mariadb/mariadbd-options.md#-defaults-extra-file) =path | Read this extra option file after all other option files are read. |
| [--defaults-group-suffix](starting-and-stopping-mariadb/mariadbd-options.md#-defaults-group-suffix) =suffix | In addition to the default option groups, also read option groups with the given suffix. |



## Default Option File Locations


MariaDB reads option files from many different directories by default. See the sections below to find out which directories are checked for which system.


For an exact list of option files read on your system by a specific program, you can execute:


```
$program --help --verbose
```

For example:


```
$ mariadbd --help --verbose
mariadbd  Ver 10.11.2-MariaDB for linux-systemd on x86_64 (MariaDB Server)
Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Starts the MariaDB database server.

Usage: mariadbd [OPTIONS]

Default options are read from the following files in the given order:
/etc/my.cnf ~/.my.cnf
The following groups are read: mysqld server mysqld-10.11 mariadb mariadb-10.11 mariadbd mariadbd-10.11 client-server galera
....
```

The option files are each scanned once, in the order given by `--help --verbose`. The effect of the configuration options are as if they would have been given as command line options in the order they are found.


### Default Option File Locations on Linux, Unix, Mac


On Linux, Unix, or Mac OS X, the default option file is called `my.cnf`. MariaDB looks for the MariaDB option file in the locations and orders listed below.


The locations are dependent on whether the `DEFAULT_SYSCONFDIR` `[cmake](compiling-mariadb-from-source/generic-build-instructions.md#using-cmake)` option was defined when MariaDB was built. This option is usually defined as `/etc` when building [RPM packages](binary-packages/rpm/README.md), but it is usually not defined when building [DEB packages](binary-packages/installing-mariadb-deb-files.md) or [binary tarballs](binary-packages/installing-mariadb-binary-tarballs.md).


* When the `DEFAULT_SYSCONFDIR` `[cmake](compiling-mariadb-from-source/generic-build-instructions.md#using-cmake)` option was not defined, MariaDB looks for the MariaDB option file in the following locations in the following order:



| Location | Scope |
| --- | --- |
| Location | Scope |
| /etc/my.cnf | Global |
| /etc/mysql/my.cnf | Global |
| $MARIADB_HOME/my.cnf | Server |
| $MYSQL_HOME/my.cnf | Server |
| defaults-extra-file | File specified with [--defaults-extra-file](starting-and-stopping-mariadb/mariadbd-options.md#-defaults-extra-file), if any |
| ~/.my.cnf | User |



* When the `DEFAULT_SYSCONFDIR` `[cmake](compiling-mariadb-from-source/generic-build-instructions.md#using-cmake)` option was defined, MariaDB looks for the MariaDB option file in the following locations in the following order:



| Location | Scope |
| --- | --- |
| Location | Scope |
| DEFAULT_SYSCONFDIR/my.cnf | Global |
| $MARIADB_HOME/my.cnf | Server (from [MariaDB 10.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-6-series/what-is-mariadb-106)) |
| $MYSQL_HOME/my.cnf | Server |
| defaults-extra-file | File specified with [--defaults-extra-file](starting-and-stopping-mariadb/mariadbd-options.md#-defaults-extra-file), if any |
| ~/.my.cnf | User |



* `MARIADB_HOME` (from [MariaDB 10.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-6-series/what-is-mariadb-106)) or `MYSQL_HOME` is the [environment variable](mariadb-environment-variables.md) containing the path to the directory holding the server-specific `my.cnf` file. If `MYSQL_HOME` is not set, and the server is started with [mysqld_safe](../../clients-and-utilities/legacy-clients-and-utilities/mariadbd_safe.md), `MYSQL_HOME` is set as follows:

  * If there is a `my.cnf` file in the MariaDB data directory, but not in the MariaDB base directory, `MYSQL_HOME` is set to the MariaDB data directory.
  * Else, `MYSQL_HOME` is set to the MariaDB base directory.
* Note that if `MARIADB_HOME` is set (from [MariaDB 10.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-6-series/what-is-mariadb-106)), `MYSQL_HOME` will not be used, even if set.


### Default Option File Locations on Windows


On Windows, the option file can be called either `my.ini` or `my.cnf`. MariaDB looks for the MariaDB option file in the following locations in the following order:



| Location | Scope |
| --- | --- |
| Location | Scope |
| System Windows Directory\my.ini | Global |
| System Windows Directory\my.cnf | Global |
| Windows Directory\my.ini | Global |
| Windows Directory\my.cnf | Global |
| C:\my.ini | Global |
| C:\my.cnf | Global |
| INSTALLDIR\my.ini | Server |
| INSTALLDIR\my.cnf | Server |
| INSTALLDIR\data\my.ini | Server |
| INSTALLDIR\data\my.cnf | Server |
| %MARIADB_HOME%\my.ini | Server (from [MariaDB 10.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-6-series/what-is-mariadb-106)) |
| %MARIADB_HOME%\my.cnf | Server (from [MariaDB 10.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-6-series/what-is-mariadb-106)) |
| %MYSQL_HOME%\my.ini | Server |
| %MYSQL_HOME%\my.cnf | Server |
| defaults-extra-file | File specified with [--defaults-extra-file](starting-and-stopping-mariadb/mariadbd-options.md#-defaults-extra-file), if any |



* The `System Windows Directory` is the directory returned by the `[GetSystemWindowsDirectory](https://docs.microsoft.com/en-us/windows/desktop/api/sysinfoapi/nf-sysinfoapi-getsystemwindowsdirectorya)` function. The value is usually `C:\Windows`. To find its specific value on your system, open `[cmd.exe](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/cmd)` and execute: 
```
echo %WINDIR%
```
* The `Windows Directory` is the directory returned by the `[GetWindowsDirectory](https://docs.microsoft.com/en-us/windows/desktop/api/sysinfoapi/nf-sysinfoapi-getwindowsdirectorya)` function. The value may be a private `Windows Directory` for the application, or it may be the same as the `System Windows Directory` returned by the `[GetSystemWindowsDirectory](https://docs.microsoft.com/en-us/windows/desktop/api/sysinfoapi/nf-sysinfoapi-getsystemwindowsdirectorya)` function.
* `INSTALLDIR` is the parent directory of the directory where `mysqld.exe` is located. For example, if `mysqld.exe` is in `C:\Program Files\[MariaDB 10.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/what-is-mariadb-103)\bin`, then `INSTALLDIR` would be `C:\Program Files\[MariaDB 10.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/what-is-mariadb-103)`.
* `MARIADB_HOME` (from [MariaDB 10.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-6-series/what-is-mariadb-106)) or `MYSQL_HOME` is the [environment variable](mariadb-environment-variables.md) containing the path to the directory holding the server-specific `my.cnf` file.
* Note that if `MARIADB_HOME` is set (from [MariaDB 10.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-6-series/what-is-mariadb-106)), `MYSQL_HOME` will not be used, even if set.


### Default Option File Hierarchy


MariaDB will look in all of the above locations, in order, even if it has already found an option file, and it's possible for more than one option file to exist. For example, you could have an option file in `/etc/my.cnf` with global settings for all servers, and then you could another option file in `~/.my.cnf` (i.e.your user account's home directory) which will specify additional settings (or override previously specified settings) that are specific only to that user.


Option files are usually optional. However, if the `[--defaults-file](starting-and-stopping-mariadb/mariadbd-options.md#-defaults-file)` option is set, and if the file does not exist, then MariaDB will raise an error. If the `[--defaults-file](starting-and-stopping-mariadb/mariadbd-options.md#-defaults-file)` option is set, then MariaDB will *only* read the option file referred to by this option.


If an option or system variable is not explicitly set, then it will be set to its default value. See [Server System Variables](../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md) for a full list of all server system variables and their default values.


If an option is set multiple times, the later setting will override the earlier setting/s.


If [--log-basename](starting-and-stopping-mariadb/mariadbd-options.md#-log-basename) is set, there are various other log file naming options that, if set, should be placed **after** in the config file hierarchy. Later settings override earlier settings, so `log-basename` will override any earlier log file name settings. See [--log-basename](starting-and-stopping-mariadb/mariadbd-options.md#-log-basename) for details.


## Custom Option File Locations


MariaDB can be configured to read options from custom options files with the following command-line arguments. These command-line arguments can be used with most of MariaDB's command-line tools, not just `[mariadbd](starting-and-stopping-mariadb/mariadbd-options.md)`. They must be given as the first argument on the command-line:



| Option | Description |
| --- | --- |
| Option | Description |
| [--defaults-file](starting-and-stopping-mariadb/mariadbd-options.md#-defaults-file) =path | Only read options from the given option file. |
| [--defaults-extra-file](starting-and-stopping-mariadb/mariadbd-options.md#-defaults-extra-file) =path | Read this extra option file after all other option files are read. |



## Option File Syntax


The syntax of the MariaDB option files are:


* Lines starting with 

# are comments.
* Empty lines are ignored.
* Option groups use the syntax `[group-name]`. See the [Option Groups](#option-groups) section below for more information on available option groups.
* The same option group can appear multiple times.
* The `!include` directive can be used to include other option files. See the [Including Option Files](#including-option-files) section below for more information on this syntax.
* The `!includedir` directive can be used to include all `.cnf` files (and potentially `.ini` files) in a given directory. The option files within the directory are read in alphabetical order. See the [Including Option File Directories](#including-option-file-directories) section below for more information on this syntax.
* Dashes (`-`) and underscores (`_`) in options are interchangeable.
* Double quotes can be used to quote values
* `\n`, `\r`, `\t`, `\b`, `\s`, `\"`, `\'`, and `\\` are recognized as character escapes for new line, carriage return, tab, backspace, space, double quote, single quote, and backslash respectively.
* Certain option prefixes are supported. See the [Option Prefixes](#option-prefixes) section below for information about available option prefixes.
* See the [Options](#options) section below for information about available options.


## Option Groups


A MariaDB program can read options from one or many option groups. For an exact list of option groups read on your system by a specific program, you can execute:


```
$program --help --verbose
```

For example:


```
$ mariadbd --help --verbose
mariadbd  Ver 10.11.2-MariaDB for linux-systemd on x86_64 (MariaDB Server)
Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Starts the MariaDB database server.

Usage: mariadbd [OPTIONS]

Default options are read from the following files in the given order:
/etc/my.cnf ~/.my.cnf
The following groups are read: mysqld server mysqld-10.11 mariadb mariadb-10.11 mariadbd mariadbd-10.11 client-server galera
....
```

### Server Option Groups


MariaDB programs reads server options from the following server option groups:



| Group | Description |
| --- | --- |
| Group | Description |
| [client-server] | Options read by all MariaDB [client programs](/kb/en/clients-utilities/) and the MariaDB Server. This is useful for options like socket and port, which is common between the server and the clients. |
| [server] | Options read by MariaDB Server. |
| [mysqld] | Options read by mysqld, which includes both MariaDB Server and MySQL Server. |
| [mysqld-X.Y] | Options read by a specific version of mysqld, which includes both MariaDB Server and MySQL Server. For example, [mysqld-10.4]. |
| [mariadb] | Options read by MariaDB Server. |
| [mariadb-X.Y] | Options read by a specific version of MariaDB Server. For example, [mariadb-10.4]. |
| [mariadbd] | Options read by MariaDB Server. Available starting with [MariaDB 10.4.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/mariadb-1046-release-notes). |
| [mariadbd-X.Y] | Options read by a specific version of MariaDB Server. For example, [mariadbd-10.4]. Available starting with [MariaDB 10.4.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/mariadb-1046-release-notes). |
| [galera] | Options read by MariaDB Server, but only if it is compiled with [Galera Cluster](../../server-usage/replication-cluster-multi-master/galera-cluster/README.md) support. In [MariaDB 10.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-1-series/changes-improvements-in-mariadb-10-1) and later, all builds on Linux are compiled with [Galera Cluster](../../server-usage/replication-cluster-multi-master/galera-cluster/README.md) support. When using one of these builds, options from this option group are read even if the [Galera Cluster](../../server-usage/replication-cluster-multi-master/galera-cluster/README.md) functionality is not enabled. |



*X.Y* in the examples above refer to the base (major.minor) version of the server. For example, [MariaDB 10.3.10](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-10310-release-notes) would read from `[mariadb-10.3]`. By using the `mariadb-X.Y` syntax, one can create option files that have MariaDB-only options in the MariaDB-specific option groups. That would allow the option file to work for both MariaDB and MySQL.


### Client Option Groups


MariaDB programs reads client options from the following option groups:



| Group | Description |
| --- | --- |
| Group | Description |
| [client] | Options read by all MariaDB and MySQL [client programs](/kb/en/clients-utilities/), which includes both MariaDB and MySQL clients. For example, mariadb-dump. |
| [client-server] | Options read by all MariaDB [client programs](/kb/en/clients-utilities/) and the MariaDB Server. This is useful for options like socket and port, which is common between the server and the clients. |
| [client-mariadb] | Options read by all MariaDB [client programs](/kb/en/clients-utilities/). |



### Tool-Specific Option Groups


Many MariaDB tools reads options from their own option groups as well. Many of them are listed below:



| Group | Description |
| --- | --- |
| Group | Description |
| [mysqld_safe] | Options read by [mysqld_safe](../../clients-and-utilities/legacy-clients-and-utilities/mariadbd_safe.md), which includes both MariaDB Server and MySQL Server. |
| [safe_mysqld] | Options read by [mysqld_safe](../../clients-and-utilities/legacy-clients-and-utilities/mariadbd_safe.md), which includes both MariaDB Server and MySQL Server. |
| [mariadbd-safe] | Options read by [mysqld_safe](../../clients-and-utilities/legacy-clients-and-utilities/mariadbd_safe.md) from MariaDB Server. Available starting with [MariaDB 10.4.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/mariadb-1046-release-notes). |
| [mariadb_safe] | Options read by [mysqld_safe](../../clients-and-utilities/legacy-clients-and-utilities/mariadbd_safe.md) from MariaDB Server. Deprecated, please avoid using this. |
| [mariabackup] | Options read by [Mariabackup](../backing-up-and-restoring-databases/mariabackup/README.md). Available starting with [MariaDB 10.1.31](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-1-series/mariadb-10131-release-notes) and [MariaDB 10.2.13](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-10213-release-notes). |
| [xtrabackup] | Options read by [Mariabackup](../backing-up-and-restoring-databases/mariabackup/README.md) and [Percona XtraBackup](../../clients-and-utilities/legacy-clients-and-utilities/backing-up-and-restoring-databases-percona-xtrabackup/percona-xtrabackup-overview.md). |
| [mysql_upgrade] | Options read by [mysql_upgrade](../../clients-and-utilities/legacy-clients-and-utilities/mysql_upgrade.md), which includes both MariaDB Server and MySQL Server. |
| [mariadb-upgrade] | Options read by [mariadb-upgrade](../../clients-and-utilities/mariadb-upgrade.md). Available starting with [MariaDB 10.4.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/mariadb-1046-release-notes). |
| [sst] | Specific options read by the [mariabackup SST method](../../server-usage/replication-cluster-multi-master/galera-cluster/state-snapshot-transfers-ssts-in-galera-cluster/mariabackup-sst-method.md) and the [xtrabackup-v2 SST method](https://mariadb.com/kb/en/). |
| [mysql] | Options read by [mysql](../../clients-and-utilities/mariadb-client/README.md), which includes both MariaDB Server and MySQL Server. |
| [mariadb-client] | Options read by [mariadb](../../clients-and-utilities/mariadb-client/README.md). Available starting with [MariaDB 10.4.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/mariadb-1046-release-notes). |
| [mysqldump] | Options read by [mysqldump](../../clients-and-utilities/legacy-clients-and-utilities/mysqldump.md), which includes both MariaDB Server and MySQL Server. |
| [mariadb-dump] | Options read by [mariadb-dump](../../clients-and-utilities/backup-restore-and-import-clients/mariadb-dump.md). Available starting with [MariaDB 10.4.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/mariadb-1046-release-notes). |
| [mysqlimport] | Options read by [mysqlimport](../../clients-and-utilities/legacy-clients-and-utilities/mysqlimport.md), which includes both MariaDB Server and MySQL Server. |
| [mariadb-import] | Options read by [mariadb-import](../../clients-and-utilities/backup-restore-and-import-clients/mariadb-import.md). Available starting with [MariaDB 10.4.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/mariadb-1046-release-notes). |
| [mysqlbinlog] | Options read by [mysqlbinlog](../../clients-and-utilities/mariadb-binlog/README.md), which includes both MariaDB Server and MySQL Server. |
| [mariadb-binlog] | Options read by [mariadb-binlog](../../clients-and-utilities/mariadb-binlog/README.md). Available starting with [MariaDB 10.4.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/mariadb-1046-release-notes). |
| [mysqladmin] | Options read by [mysqladmin](../../clients-and-utilities/legacy-clients-and-utilities/mysqladmin.md), which includes both MariaDB Server and MySQL Server. |
| [mariadb-admin] | Options read by [mariadb-admin](../../clients-and-utilities/mariadb-admin.md). Available starting with [MariaDB 10.4.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/mariadb-1046-release-notes). |
| [mysqlshow] | Options read by [mysqlshow](../../clients-and-utilities/legacy-clients-and-utilities/mysqlshow.md), which includes both MariaDB Server and MySQL Server. |
| [mariadb-show] | Options read by [mariadb-show](../../clients-and-utilities/mariadb-show.md). Available starting with [MariaDB 10.4.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/mariadb-1046-release-notes). |
| [mysqlcheck] | Options read by [mariadb-check](../../clients-and-utilities/mariadb-check.md), which includes both MariaDB Server and MySQL Server. |
| [mariadb-check] | Options read by [mariadb-check](../../clients-and-utilities/mariadb-check.md). Available starting with [MariaDB 10.4.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/mariadb-1046-release-notes). |
| [mysqlslap] | Options read by [mysqlslap](../../clients-and-utilities/legacy-clients-and-utilities/mysqlslap.md), which includes both MariaDB Server and MySQL Server. |
| [mariadb-slap] | Options read by [mariadb-slap](../../clients-and-utilities/mariadb-slap.md). Available starting with [MariaDB 10.4.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/mariadb-1046-release-notes). |
| [odbc] | Options read by [MariaDB Connector/ODBC](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-odbc/), but only if the [USE_MYCNF](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-odbc/about-mariadb-connector-odbc#general-connection-parameters) parameter has been set. |



### Custom Option Group Suffixes


MariaDB can be configured to read options from option groups with a custom suffix by providing the following command-line argument. This command-line argument can be used with most of MariaDB's command-line tools, not just `[mariadbd](starting-and-stopping-mariadb/mariadbd-options.md)`. It must be given as the first argument on the command-line:



| Option | Description |
| --- | --- |
| Option | Description |
| [--defaults-group-suffix](starting-and-stopping-mariadb/mariadbd-options.md#-defaults-group-suffix) =suffix | In addition to the default option groups, also read option groups with the given suffix. |



The default group suffix can also be specified via the `MYSQL_GROUP_SUFFIX` [environment variable](mariadb-environment-variables.md).


## Including Option Files


It is possible to include additional option files from another option file. For example, to include `/etc/mysql/dbserver1.cnf`, an option file could contain:


```
[mariadb]
...
!include /etc/mysql/dbserver1.cnf
```

## Including Option File Directories


It is also possible to include all option files in a directory from another option file. For example, to include all option files in `/etc/my.cnf.d/`, an option file could contain:


```
[mariadb]
...
!includedir /etc/my.cnf.d/
```

The option files within the directory are read in alphabetical order.


All option file names must end in `.cnf` on Unix-like operating systems. On Windows, all option file names must end in `.cnf` or `.ini`.


## Checking Program Options


You can check which options a given program is going to use by using the `[--print-defaults](starting-and-stopping-mariadb/mariadbd-options.md#-print-defaults)` command-line argument:



| Option | Description |
| --- | --- |
| Option | Description |
| [--print-defaults](starting-and-stopping-mariadb/mariadbd-options.md#-print-defaults) | Read options from option files, print all option values, and then exit the program. |



This command-line argument can be used with most of MariaDB's command-line tools, not just `[mariadbd](starting-and-stopping-mariadb/mariadbd-options.md)`. It must be given as the first argument on the command-line. For example:


```
$ mariadb-dump --print-defaults
mariadb-dump would have been started with the following arguments:
--ssl_cert=/etc/my.cnf.d/certificates/client-cert.pem --ssl_key=/etc/my.cnf.d/certificates/client-key.pem --ssl_ca=/etc/my.cnf.d/certificates/ca.pem --ssl-verify-server-cert --max_allowed_packet=1GB
```

You can also check which options a given program is going to use by using the `[my_print_defaults](../../clients-and-utilities/my_print_defaults.md)` utility and providing the names of the option groups that the program reads. For example:


```
$ my_print_defaults mariadb-dump client client-server client-mariadb
--ssl_cert=/etc/my.cnf.d/certificates/client-cert.pem
--ssl_key=/etc/my.cnf.d/certificates/client-key.pem
--ssl_ca=/etc/my.cnf.d/certificates/ca.pem
--ssl-verify-server-cert
--max_allowed_packet=1GB
```

The `[my_print_defaults](../../clients-and-utilities/my_print_defaults.md)` utility's `--mariadbd` command-line option provides a shortcut to refer to all of the [server option groups](#server-option-groups):


```
$ my_print_defaults --mysqld
--log_bin=mariadb-bin
--log_slave_updates=ON
--ssl_cert=/etc/my.cnf.d/certificates/server-cert.pem
--ssl_key=/etc/my.cnf.d/certificates/server-key.pem
--ssl_ca=/etc/my.cnf.d/certificates/ca.pem
```

## MySQL 5.6 Obfuscated Authentication Credential Option File


MySQL 5.6 and above support an obfuscated authentication credential option file called `.mylogin.cnf` that is created with `[mysql_config_editor](https://dev.mysql.com/doc/refman/5.6/en/mysql-config-editor.html)`.


MariaDB does not support this. The passwords in MySQL's `.mylogin.cnf` are only obfuscated, rather than encrypted, so the feature does not really add much from a security perspective. It is more likely to give users a false sense of security, rather than to seriously protect them.


## Option Prefixes


MariaDB supports certain prefixes that can be used with options. The supported option prefixes are:



| Option Prefix | Description |
| --- | --- |
| Option Prefix | Description |
| [autoset](starting-and-stopping-mariadb/mariadbd-options.md#-autoset-) | Sets the option value automatically. Only supported for certain options. |
| [disable](starting-and-stopping-mariadb/mariadbd-options.md#-disable-) | For all boolean options, disables the setting (equivalent to setting it to 0). Same as skip. |
| [enable](starting-and-stopping-mariadb/mariadbd-options.md#-enable-) | For all boolean options, enables the setting (equivalent to setting it to 1). |
| [loose](starting-and-stopping-mariadb/mariadbd-options.md#-loose-) | Don't produce an error if the option doesn't exist. |
| [maximum](starting-and-stopping-mariadb/mariadbd-options.md#-maximum-) | Sets the maximum value for the option. |
| [skip](starting-and-stopping-mariadb/mariadbd-options.md#-skip-) | For all boolean options, disables the setting (equivalent to setting it to 0). Same as disable. |



For example:


```
[mariadb]
...
# determine a good value for open_files_limit automatically
autoset_open_files_limit

# disable the unix socket plugin
disable_unix_socket

# enable the slow query log
enable_slow_query_log

# don't produce an error if these options don't exist
loose_file_key_management_filename = /etc/mysql/encryption/keyfile.enc
loose_file_key_management_filekey = FILE:/etc/mysql/encryption/keyfile.key
loose_file_key_management_encryption_algorithm = AES_CTR

# set max_allowed_packet to maximum value
maximum_max_allowed_packet

# disable external locking for MyISAM
skip_external_locking
```

## Options


Dashes (`-`) and underscores (`_`) in options are interchangeable.


If an option is not explicitly set, then the server or client will simply use the default value for that option.


### MariaDB Server Options


MariaDB Server options can be set in [server option groups](#server-option-groups).


For a list of options that can be set for MariaDB Server, see the list of options available for `[mariadbd](starting-and-stopping-mariadb/mariadbd-options.md)`.


Most of the [server system variables](../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md) can also be set in MariaDB's option file.


### MariaDB Client Options


MariaDB client options can be set in [client option groups](#client-option-groups).


See the specific page for each [client program](/kb/en/clients-utilities/) to determine what options are available for that program.


## Example Option Files


Most MariaDB installations include a sample MariaDB option file called `my-default.cnf`. On older releases, you would have also found the following option files:


* `my-small.cnf`
* `my-medium.cnf`
* `my-large.cnf`
* `my-huge.cnf`


However, these option files are now very dated for modern servers, so they were removed in [MariaDB 10.3.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-1031-release-notes).


In source distributions, the sample option files are usually found in the `support-files` directory, and in other distributions, the option files are usually found in the `share/mysql` directory that is relative to the MariaDB base installation directory.


You can copy one of these sample MariaDB option files and use it as the basis for building your server's primary MariaDB option file.


### Example Minimal Option File


The following is a minimal my.cnf file that you can use to test MariaDB.


```
[client-server]
# Uncomment these if you want to use a nonstandard connection to MariaDB
#socket=/tmp/mysql.sock
#port=3306

# This will be passed to all MariaDB clients
[client]
#password=my_password

# The MariaDB server
[mysqld]
# Directory where you want to put your data
data=/usr/local/mysql/var
# Directory for the errmsg.sys file in the language you want to use
language=/usr/local/share/mysql/english

# This is the prefix name to be used for all log, error and replication files
log-basename=mysqld

# Enable logging by default to help find problems
general-log
log-slow-queries
```

### Example Hybrid Option File


The following is an extract of an option file that one can use if one wants to work with both MySQL and MariaDB.


```
# Example mysql config file.

[client-server]
socket=/tmp/mysql-dbug.sock
port=3307

# This will be passed to all mariadb clients
[client]
password=my_password

# Here are entries for some specific programs
# The following values assume you have at least 32M ram

# The MariaDB server
[mysqld]
temp-pool
key_buffer_size=16M
datadir=/my/mysqldata
loose-innodb_file_per_table

[mariadb]
datadir=/my/data
default-storage-engine=aria
loose-mutex-deadlock-detector
max-connections=20

[mariadb-5.5]
language=/my/maria-5.5/sql/share/english/
socket=/tmp/mysql-dbug.sock
port=3307

[mariadb-10.1]
language=/my/maria-10.1/sql/share/english/
socket=/tmp/mysql2-dbug.sock

[mysqldump]
quick
max_allowed_packet=16M

[mysql]
no-auto-rehash
loose-abort-source-on-error
```

## See Also


* [Configuring MariaDB Connector/C with Option Files](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/configuring-mariadb-connectorc-with-option-files)
* [Troubleshooting Connection Issues](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/learning-and-training/training-and-tutorials/basic-mariadb-articles/troubleshooting-connection-issues)
* [Configuring MariaDB for Remote Client Access](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/learning-and-training/training-and-tutorials/basic-mariadb-articles/configuring-mariadb-for-remote-client-access)
* [MySQL 5.6: Security through Complacency?](https://mariadb.com/resources/blog/mysql-5-6-security-through-complacency)

