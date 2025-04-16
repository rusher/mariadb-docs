
# mariadb-plugin

`mariadb-plugin` is a tool for enabling or disabling [plugins](../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/general-development-information/development-plans/old-plans/plugins-storage-engines-summit-for-mysqlmariadbdrizzle-2011.md).


Prior to [MariaDB 10.5](../../release-notes/mariadb-community-server/what-is-mariadb-105.md), the client was called `mysql_plugin`. It can still be accessed under this name, via a symlink in Linux, or an alternate binary in Windows.


It is a commandline alternative to the [INSTALL PLUGIN](../ref/sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/install-plugin.md) and [UNINSTALL PLUGIN](../ref/sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-plugin.md) statements, and the `--plugin-load option` to [mariadbd](../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md).


`mariadb-plugin` must be run while the server is offline, and works by adding or removing rows from the [mysql.plugin](../ref/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/the-mysql-database-tables/mysql-plugin-table.md) table.


`mariadb-plugin` basically has two use cases:


* adding a plugin even before the first real server startup
* removing a plugin that crashes the server on startup


For the install use case, adding a [plugin-load-add](../ref/plugins/plugin-overview.md#installing-a-plugin-with-plugin-load-add) entry to `my.cnf` or in a separate include option file, is probably a better alternative. In case of a plugin loaded via a `mysql.plugin` crashing the server, uninstalling the plugin with the help of `mariadb-plugin` can be the only viable action though.


## Usage


```
mariadb-plugin [options] <plugin> ENABLE|DISABLE
```

`mariadb-plugin` expects to find a configuration file that indicates how to configure the plugins. The configuration file is by default the same name as the plugin, with a `.ini` extension. For example:


```
mariadb-plugin crazyplugins ENABLE
```

Here, `mariadb-plugin` will look for a file called `crazyplugins.ini`


```
crazyplugins
crazyplugin1
crazyplugin2
crazyplugin3
```

The first line should contain the name of the library object file, with no extension. The other lines list the names of the components. Each value should be on a separate line, and the `#` character at the start of the line indicates a comment.


## Options


The following options can be specified on the command line, while some can be specified in the `[mysqld]` group of any option file. For options specified in a `[mysqld]` group, only the `--basedir`, `--datadir`, and `--plugin-dir` options can be used - the rest are ignored.



| Option | Description |
| --- | --- |
| Option | Description |
| -b, --basedir=name | The base directory for the server. |
| -d, --datadir=name | The data directory for the server. |
| -?, --help | Display help and exit. |
| -f, --my-print-defaults=name | Path to my_print_defaults executable. Example: /source/temp11/extra |
| -m, --mysqld=name | Path to mysqld executable. Example: /sbin/temp1/mysql/bin |
| -n, --no-defaults | Do not read values from configuration file. |
| -p, --plugin-dir=name | The plugin directory for the server. |
| -i, --plugin-ini=name | Read plugin information from configuration file specified instead of from <plugin-dir>/<plugin_name>.ini. |
| -P, --print-defaults | Show default values from configuration file. |
| -v, --verbose | More verbose output; you can use this multiple times to get even more verbose output. |
| -V, --version | Output version information and exit. |



## See Also


* [List of Plugins](../ref/plugins/information-on-plugins/list-of-plugins.md)
* [Plugin Overview](../ref/plugins/plugin-overview.md)
* [INFORMATION_SCHEMA.PLUGINS Table](../ref/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/plugins-table-information-schema.md)
* [INSTALL PLUGIN](../ref/sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/install-plugin.md)
* [INSTALL SONAME](../ref/sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/install-soname.md)
* [UNINSTALL PLUGIN](../ref/sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-plugin.md)
* [UNINSTALL SONAME](../ref/sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-soname.md)

