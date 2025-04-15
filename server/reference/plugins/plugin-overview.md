
# Plugin Overview


Plugins are server components that enhance MariaDB in some way. These can be anything from new storage engines, plugins for enhancing full-text parsing, or even small enhancements, such as a plugin to get a timestamp as an integer.


## Querying Plugin Information


There are a number of ways to see which plugins are currently active.


A server almost always has a large number of active plugins, because the server contains a large number of built-in plugins, which are active by default and cannot be uninstalled.


### Querying Plugin Information with `<code>SHOW PLUGINS</code>`


The [SHOW PLUGINS](../sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-plugins-soname.md) statement can be used to query information about all active plugins.


For example:


```
SHOW PLUGINS\G;
********************** 1. row **********************
   Name: binlog
 Status: ACTIVE
   Type: STORAGE ENGINE
Library: NULL
License: GPL
********************** 2. row **********************
   Name: mysql_native_password
 Status: ACTIVE
   Type: AUTHENTICATION
Library: NULL
License: GPL
********************** 3. row **********************
   Name: mysql_old_password
 Status: ACTIVE
   Type: AUTHENTICATION
Library: NULL
License: GPL
...
```

If a plugin's `<code>Library</code>` column has a `<code>NULL</code>` value, then the plugin is built-in, and it cannot be uninstalled.


### Querying Plugin Information with information_schema.PLUGINS


The [information_schema.PLUGINS](../sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/plugins-table-information-schema.md) table can be queried to get more detailed information about plugins.


For example:


```
SELECT * FROM information_schema.PLUGINS\G
...
*************************** 65. row ***************************
           PLUGIN_NAME: user_variables
        PLUGIN_VERSION: 1.0
         PLUGIN_STATUS: ACTIVE
           PLUGIN_TYPE: INFORMATION SCHEMA
   PLUGIN_TYPE_VERSION: 110600.0
        PLUGIN_LIBRARY: NULL
PLUGIN_LIBRARY_VERSION: NULL
         PLUGIN_AUTHOR: Sergey Vojtovich
    PLUGIN_DESCRIPTION: User-defined variables
        PLUGIN_LICENSE: GPL
           LOAD_OPTION: ON
       PLUGIN_MATURITY: Stable
   PLUGIN_AUTH_VERSION: 1.0
*************************** 66. row ***************************
           PLUGIN_NAME: wsrep_provider
        PLUGIN_VERSION: 1.0
         PLUGIN_STATUS: ACTIVE
           PLUGIN_TYPE: REPLICATION
   PLUGIN_TYPE_VERSION: 2.0
        PLUGIN_LIBRARY: NULL
PLUGIN_LIBRARY_VERSION: NULL
         PLUGIN_AUTHOR: Codership Oy
    PLUGIN_DESCRIPTION: Wsrep provider plugin
        PLUGIN_LICENSE: GPL
           LOAD_OPTION: ON
       PLUGIN_MATURITY: Alpha
   PLUGIN_AUTH_VERSION: 1.0
*************************** 67. row ***************************
           PLUGIN_NAME: THREAD_POOL_GROUPS
        PLUGIN_VERSION: 1.0
         PLUGIN_STATUS: ACTIVE
           PLUGIN_TYPE: INFORMATION SCHEMA
   PLUGIN_TYPE_VERSION: 110600.0
        PLUGIN_LIBRARY: NULL
PLUGIN_LIBRARY_VERSION: NULL
         PLUGIN_AUTHOR: Vladislav Vaintroub
    PLUGIN_DESCRIPTION: Provides information about threadpool groups.
        PLUGIN_LICENSE: GPL
           LOAD_OPTION: ON
       PLUGIN_MATURITY: Stable
   PLUGIN_AUTH_VERSION: 1.0
...
```

If a plugin's `<code>PLUGIN_LIBRARY</code>` column has the `<code>NULL</code>` value, then the plugin is built-in, and it cannot be uninstalled.


### Querying Plugin Information with `<code>mysql.plugin</code>`


The [mysql.plugin](../sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/the-mysql-database-tables/mysql-plugin-table.md) table can be queried to get information about installed plugins.


This table only contains information about plugins that have been installed via the following methods:


* The [INSTALL SONAME](../sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/install-soname.md) statement.
* The [INSTALL PLUGIN](../sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/install-plugin.md) statement.
* The [mariadb-plugin](../../clients-and-utilities/mariadb-plugin.md) utility.


This table does not contain information about:


* Built-in plugins.
* Plugins loaded with the [--plugin-load-add](../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md#-plugin-load-add) option.
* Plugins loaded with the [--plugin-load](../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md#-plugin-load) option.


This table only contains enough information to reload the plugin when the server is restarted, which means it only contains the plugin name and the plugin library.


For example:


```
SELECT * FROM mysql.plugin;

+------+------------+
| name | dl         |
+------+------------+
| PBXT | libpbxt.so |
+------+------------+
```

## Installing a Plugin


There are three primary ways to install a plugin:


* A plugin can be installed dynamically with an SQL statement.
* A plugin can be installed with a [mariadbd](../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md) option, but it requires a server restart.
* A plugin can be installed with the [mariadb-plugin](../../clients-and-utilities/mariadb-plugin.md) utility, while the server is completely offline.


When you are installing a plugin, you also have to ensure that:


* The server's plugin directory is properly configured, and the plugin's library is in the plugin directory.
* The server's minimum plugin maturity is properly configured, and the plugin is mature enough to be installed.


### Installing a Plugin Dynamically


A plugin can be installed dynamically by executing either the [INSTALL SONAME](../sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/install-soname.md) or the [INSTALL PLUGIN](../sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/install-plugin.md) statement.


If a plugin is installed with one of these statements, then a record will be added to the [mysql.plugins](../sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/the-mysql-database-tables/mysql-plugin-table.md) table for the plugin. This means that the plugin will automatically be loaded every time the server restarts, unless specifically uninstalled or deactivated.


#### Installing a Plugin with `<code>INSTALL SONAME</code>`


You can install a plugin dynamically by executing the [INSTALL SONAME](../sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/install-soname.md) statement. [INSTALL SONAME](../sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/install-soname.md) installs all plugins from the given plugin library. This could be required for some plugin libraries.


For example, to install all plugins in the `<code>server_audit</code>` plugin library (which is currently only the [server_audit](mariadb-audit-plugin/release-notes-mariadb-audit-plugin/mariadb-audit-plugin-113-release-notes.md) audit plugin), you could execute the following:


```
INSTALL SONAME 'server_audit';
```

#### Installing a Plugin with `<code>INSTALL PLUGIN</code>`


You can install a plugin dynamically by executing the [INSTALL PLUGIN](../sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/install-plugin.md) statement. [INSTALL PLUGIN](../sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/install-plugin.md) installs a single plugin from the given plugin library.


For example, to install the [server_audit](mariadb-audit-plugin/release-notes-mariadb-audit-plugin/mariadb-audit-plugin-113-release-notes.md) audit plugin from the `<code>server_audit</code>` plugin library, you could execute the following:


```
INSTALL PLUGIN server_audit SONAME 'server_audit';
```

### Installing a Plugin with Plugin Load Options


A plugin can be installed with a [mariadbd](../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md) option by providing either the [--plugin-load-add](../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md#-plugin-load-add) or the [--plugin-load](../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md#-plugin-load) option.


If a plugin is installed with one of these options, then a record will **not** be added to the [mysql.plugins](../sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/the-mysql-database-tables/mysql-plugin-table.md) table for the plugin. This means that if the server is restarted without the same option set, then the plugin will **not** automatically be loaded.


#### Installing a Plugin with `<code>--plugin-load-add</code>`


You can install a plugin with the [--plugin-load-add](../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md#-plugin-load-add) option by specifying the option as a command-line argument to [mariadbd](../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md) or by specifying the option in a relevant server [option group](../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md).


The [--plugin-load-add](https://mariadb.com/kb/en/-options/#-plugin-load-add) option uses the following format:


* Plugins can be specified in the format `<code>name=library</code>`, where `<code>name</code>` is the plugin name and `<code>library</code>` is the plugin library. This format installs a single plugin from the given plugin library.
* Plugins can also be specified in the format `<code>library</code>`, where `<code>library</code>` is the plugin library. This format installs all plugins from the given plugin library.
* Multiple plugins can be specified by separating them with semicolons.


For example, to install all plugins in the `<code>server_audit</code>` plugin library (which is currently only the `<code>[server_audit](mariadb-audit-plugin/release-notes-mariadb-audit-plugin/mariadb-audit-plugin-113-release-notes.md)</code>` audit plugin) and also the `<code>[ed25519](authentication-plugins/authentication-plugin-ed25519.md)</code>` authentication plugin from the `<code>auth_ed25519</code>` plugin library, you could set the option to the following values on the command-line:


```
$ mariadbd --user=mysql --plugin-load-add='server_audit' --plugin-load-add='ed25519=auth_ed25519'
```

You could also set the option to the same values in an [option file](../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md):


```
[mariadb]
...
plugin_load_add = server_audit
plugin_load_add = ed25519=auth_ed25519
```

Special care must be taken when specifying both the [--plugin-load](../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md#-plugin-load) option and the [--plugin-load-add](../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md#-plugin-load-add) option together. The [--plugin-load](../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md#-plugin-load) option resets the plugin load list, and this can cause unexpected problems if you are not aware. The [--plugin-load-add](../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md#-plugin-load-add) option does **not** reset the plugin load list, so it is much safer to use. See [Specifying Multiple Plugin Load Options](#specifying-multiple-plugin-load-options) for more information.


#### Installing a Plugin with `<code>--plugin-load</code>`


You can install a plugin with the [--plugin-load](../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md#-plugin-load) option by specifying the option as a command-line argument to [mariadbd](../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md) or by specifying the option in a relevant server [option group](../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md).


The [--plugin-load](../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md#-plugin-load) option uses the following format:


* Plugins can be specified in the format `<code>name=library</code>`, where `<code>name</code>` is the plugin name and `<code>library</code>` is the plugin library. This format installs a single plugin from the given plugin library.
* Plugins can also be specified in the format `<code>library</code>`, where `<code>library</code>` is the plugin library. This format installs all plugins from the given plugin library.
* Multiple plugins can be specified by separating them with semicolons.


For example, to install all plugins in the `<code>server_audit</code>` plugin library (which is currently only the `<code>[server_audit](mariadb-audit-plugin/release-notes-mariadb-audit-plugin/mariadb-audit-plugin-113-release-notes.md)</code>` audit plugin) and also the `<code>[ed25519](authentication-plugins/authentication-plugin-ed25519.md)</code>` authentication plugin from the `<code>auth_ed25519</code>` plugin library, you could set the option to the following values on the command-line:


```
$ mariadbd --user=mysql --plugin-load='server_audit;ed25519=auth_ed25519'
```

You could also set the option to the same values in an [option file](../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md):


```
[mariadb]
...
plugin_load = server_audit;ed25519=auth_ed25519
```

Special care must be taken when specifying the `<code>[--plugin-load](../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md#-plugin-load)</code>` option multiple times, or when specifying both the `<code>[--plugin-load](../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md#-plugin-load)</code>` option and the `<code>[--plugin-load-add](../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md#-plugin-load-add)</code>` option together. The `<code>[--plugin-load](../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md#-plugin-load)</code>` option resets the plugin load list, and this can cause unexpected problems if you are not aware. The `<code>[--plugin-load-add](../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md#-plugin-load-add)</code>` option does **not** reset the plugin load list, so it is much safer to use. See [Specifying Multiple Plugin Load Options](#specifying-multiple-plugin-load-options) for more information.


#### Specifying Multiple Plugin Load Options


Special care must be taken when specifying the `<code>[--plugin-load](../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md#-plugin-load)</code>` option multiple times, or when specifying both the `<code>[--plugin-load](../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md#-plugin-load)</code>` option and the `<code>[--plugin-load-add](../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md#-plugin-load-add)</code>` option. The `<code>[--plugin-load](../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md#-plugin-load)</code>` option resets the plugin load list, and this can cause unexpected problems if you are not aware. The `<code>[--plugin-load-add](../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md#-plugin-load-add)</code>` option does **not** reset the plugin load list, so it is much safer to use.


This can have the following consequences:


* If the `<code>[--plugin-load](../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md#-plugin-load)</code>` option is specified multiple times, then only the last instance will have any effect. For example, in the following case, the first instance of the option is reset:


```
[mariadb]
...
plugin_load = server_audit
plugin_load = ed25519=auth_ed25519
```

* If the `<code>[--plugin-load](../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md#-plugin-load)</code>` option is specified after the `<code>[--plugin-load-add](../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md#-plugin-load-add)</code>` option, then it will also reset the changes made by that option. For example, in the following case, the `<code>[--plugin-load-add](../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md#-plugin-load-add)</code>` option does not do anything, because the subsequent `<code>[--plugin-load](../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md#-plugin-load)</code>` option resets the plugin load list:


```
[mariadb]
...
plugin_load_add = server_audit
plugin_load = ed25519=auth_ed25519
```

* In contrast, if the `<code>[--plugin-load](../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md#-plugin-load)</code>` option is specified before the `<code>[--plugin-load-add](../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md#-plugin-load-add)</code>` option, then it will work fine, because the `<code>[--plugin-load-add](../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md#-plugin-load-add)</code>` option does not reset the plugin load list. For example, in the following case, both plugins are properly loaded:


```
[mariadb]
...
plugin_load = server_audit
plugin_load_add = ed25519=auth_ed25519
```

### Installing a Plugin with mariadb-plugin


A plugin can be installed with the [mariadb-plugin](../../clients-and-utilities/mariadb-plugin.md) utility if the server is completely offline.


The syntax is:


```
mariadb-plugin [options] <plugin> ENABLE|DISABLE
```

For example, to install the [server_audit](mariadb-audit-plugin/release-notes-mariadb-audit-plugin/mariadb-audit-plugin-113-release-notes.md) audit plugin, you could execute the following:


```
mariadb-plugin server_audit ENABLE
```

If a plugin is installed with this utility, then a record will be added to the [mysql.plugins](../sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/the-mysql-database-tables/mysql-plugin-table.md) table for the plugin. This means that the plugin will automatically be loaded every time the server restarts, unless specifically uninstalled or deactivated.


### Configuring the Plugin Directory


When a plugin is being installed, the server looks for the plugin's library in the server's plugin directory. This directory is configured by the `<code>[plugin_dir](../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#plugin_dir)</code>` system variable. This can be specified as a command-line argument to `<code>[mariadbd](../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md)</code>` or it can be specified in a relevant server [option group](../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md). For example:


```
[mariadb]
...
plugin_dir = /usr/lib64/mysql/plugin
```

### Configuring the Minimum Plugin Maturity


When a plugin is being installed, the server compares the plugin's maturity level against the server's minimum allowed plugin maturity. This can help prevent users from using unstable plugins on production servers. This minimum plugin maturity is configured by the `<code>[plugin_maturity](../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#plugin_maturity)</code>` system variable. This can be specified as a command-line argument to `<code>[mariadbd](../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md)</code>` or it can be specified in a relevant server [option group](../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md). For example:


```
[mariadb]
...
plugin_maturity = stable
```

### Configuring Plugin Activation at Server Startup


A plugin will be loaded by default when the server starts if:


* The plugin was installed with the [INSTALL SONAME](../sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/install-soname.md) statement.
* The plugin was installed with the [INSTALL PLUGIN](../sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/install-plugin.md) statement.
* The plugin was installed with the [mariadb-plugin](../../clients-and-utilities/mariadb-plugin.md) utility.
* The server is configured to load the plugin with the [--plugin-load-add](../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md#-plugin-load-add) option.
* The server is configured to load the plugin with the [--plugin-load](../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md#-plugin-load) option.


This behavior can be changed with special options that take the form `<code>--plugin-name</code>`. For example, for the `<code>[server_audit](mariadb-audit-plugin/release-notes-mariadb-audit-plugin/mariadb-audit-plugin-113-release-notes.md)</code>` audit plugin, the special option is called [--server-audit](mariadb-audit-plugin/mariadb-audit-plugin-options-and-system-variables.md).


The possible values for these special options are:



| Option Value | Description |
| --- | --- |
| Option Value | Description |
| OFF | Disables the plugin without removing it from the [mysql.plugins](../sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/the-mysql-database-tables/mysql-plugin-table.md) table. |
| ON | Enables the plugin. If the plugin cannot be initialized, then the server will still continue starting up, but the plugin will be disabled. |
| FORCE | Enables the plugin. If the plugin cannot be initialized, then the server will fail to start with an error. |
| FORCE_PLUS_PERMANENT | Enables the plugin. If the plugin cannot be initialized, then the server will fail to start with an error. In addition, the plugin cannot be uninstalled with [UNINSTALL SONAME](../sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-soname.md) or [UNINSTALL PLUGIN](../sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-plugin.md) while the server is running. |



A plugin's status can be found by looking at the `<code>PLUGIN_STATUS</code>` column of the [information_schema.PLUGINS](../sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/plugins-table-information-schema.md) table.


## Uninstalling Plugins


Plugins that are found in the mysql.plugin table, that is those that were installed with [INSTALL SONAME](../sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/install-soname.md), [INSTALL PLUGIN](../sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/install-plugin.md) or [mariadb-plugin](../../clients-and-utilities/mariadb-plugin.md) can be uninstalled in one of two ways:


* The [UNINSTALL SONAME](../sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-soname.md) or the [UNINSTALL PLUGIN](../sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-plugin.md) statement while the server is running
* With [mariadb-plugin](../../clients-and-utilities/mariadb-plugin.md) while the server is offline.


Plugins that were enabled as a `<code>--plugin-load</code>` option do not need to be uninstalled. If `<code>--plugin-load</code>` is omitted the next time the server starts, or the plugin is not listed as one of the `<code>--plugin-load</code>` entries, the plugin will not be loaded.


[UNINSTALL PLUGIN](../sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-plugin.md) uninstalls a single installed plugin, while [UNINSTALL SONAME](../sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-soname.md) uninstalls all plugins belonging to a given library.


## See Also


* [List of Plugins](information-on-plugins/list-of-plugins.md)
* [INSTALL PLUGIN](../sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/install-plugin.md)
* [INSTALL SONAME](../sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/install-soname.md)
* [UNINSTALL PLUGIN](../sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-plugin.md)
* [UNINSTALL SONAME](../sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-soname.md)
* [SHOW PLUGINS](../sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-plugins-soname.md)
* [INFORMATION_SCHEMA.PLUGINS Table](../sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/plugins-table-information-schema.md)
* [mariadb-plugin](../../clients-and-utilities/mariadb-plugin.md)

