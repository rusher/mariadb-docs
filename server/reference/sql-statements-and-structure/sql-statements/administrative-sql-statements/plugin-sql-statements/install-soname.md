
# INSTALL SONAME

## Syntax


```
INSTALL SONAME 'plugin_library'
```


## Description


This statement is a variant of [INSTALL PLUGIN](install-plugin.md). It installs **all** [plugins](../../../../plugins/README.md) from a given `plugin_library`. See [INSTALL PLUGIN](install-plugin.md) for details.


`plugin_library` is the name of the shared library that
contains the plugin code. The file name extension (for
example, `libmyplugin.so` or `libmyplugin.dll`) can be omitted (which makes the statement look the same on all architectures).


The shared library must be located in the plugin directory (that is,
the directory named by the [plugin_dir](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#plugin_dir) system variable). The library must be in the plugin directory itself, not in a subdirectory. By
default, `plugin_dir` is plugin directory under the directory named by
the `pkglibdir` configuration variable, but it can be changed by setting
the value of `plugin_dir` at server startup. For example, set
its value in a `my.cnf` file:


```
[mariadbd]
plugin_dir=/path/to/plugin/directory
```

If the value of [plugin_dir](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#plugin_dir) is a relative path name, it is
taken to be relative to the MySQL base directory (the value of the `basedir`
system variable).


`INSTALL SONAME` adds one or more lines to the `mysql.plugin` table that
describes the plugin. This table contains the plugin name and library file
name.


`INSTALL SONAME` causes the server to read
option (`my.cnf`) files just as during server startup. This enables the plugin to
pick up any relevant options from those files. It is possible to add plugin
options to an option file even before loading a plugin (if the loose prefix is
used). It is also possible to uninstall a plugin, edit `my.cnf`, and install the
plugin again. Restarting the plugin this way enables it to the new option
values without a server restart.


`INSTALL SONAME` also loads and initializes the plugin code to
make the plugin available for use. A plugin is initialized by executing its
initialization function, which handles any setup that the plugin must perform
before it can be used.


To use `INSTALL SONAME`, you must have the
[INSERT privilege](../../account-management-sql-commands/grant.md) for the `mysql.plugin` table.


At server startup, the server loads and initializes any plugin that is
listed in the `mysql.plugin` table. This means that a plugin is installed
with `INSTALL SONAME` only once, not every time the server
starts. Plugin loading at startup does not occur if the server is started with
the `--skip-grant-tables` option.


When the server shuts down, it executes the de-initialization function
for each plugin that is loaded so that the plugin has a chance to
perform any final cleanup.


If you need to load plugins for a single server startup when the
`--skip-grant-tables` option is given (which tells the server
not to read system tables), use the 
`--plugin-load` [mariadbd option](../../../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md#-plugin-load).


If you need to install only one plugin from a library, use the [INSTALL PLUGIN](install-plugin.md) statement.


## Examples


To load the [LOCALES plugin](../../../../data-types/string-data-types/character-sets/internationalization-and-localization/locales-plugin.md) and all of its `information_schema` tables with one statement, use


```
INSTALL SONAME 'locales';
```

This statement can be used instead of `INSTALL PLUGIN` even when the library contains only one plugin:


```
INSTALL SONAME 'ha_sequence';
```

## See Also


* [List of Plugins](../../../../plugins/information-on-plugins/list-of-plugins.md)
* [Plugin Overview](../../../../plugins/plugin-overview.md)
* [SHOW PLUGINS](../show/show-plugins.md)
* [INSTALL PLUGIN](install-plugin.md)
* [UNINSTALL PLUGIN](uninstall-plugin.md)
* [UNINSTALL SONAME](uninstall-soname.md)
* [SHOW PLUGINS](../show/show-plugins.md)
* [INFORMATION_SCHEMA.PLUGINS Table](../system-tables/information-schema/information-schema-tables/plugins-table-information-schema.md)
* [mysql_plugin](../../../../../clients-and-utilities/legacy-clients-and-utilities/mysql_plugin.md)

