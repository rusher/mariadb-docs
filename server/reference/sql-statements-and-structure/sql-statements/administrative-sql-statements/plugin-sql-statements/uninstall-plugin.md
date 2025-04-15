
# UNINSTALL PLUGIN

## Syntax


```
UNINSTALL PLUGIN [IF EXISTS] plugin_name
```


## Description


This statement removes a single installed [plugin](../../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/general-development-information/development-plans/old-plans/plugins-storage-engines-summit-for-mysqlmariadbdrizzle-2011.md). To uninstall the whole library which contains the plugin, use [UNINSTALL SONAME](uninstall-soname.md). You cannot uninstall a plugin if any table that uses it is open.


`<code class="highlight fixed" style="white-space:pre-wrap">plugin_name</code>` must be the name of some plugin that is listed
in the [mysql.plugin](../system-tables/the-mysql-database-tables/mysql-plugin-table.md) table. The server executes the plugin's deinitialization
function and removes the row for the plugin from the `<code>mysql.plugin</code>`
table, so that subsequent server restarts will not load and initialize
the plugin. `<code class="highlight fixed" style="white-space:pre-wrap">UNINSTALL PLUGIN</code>` does not remove the plugin's
shared library file.


To use `<code class="highlight fixed" style="white-space:pre-wrap">UNINSTALL PLUGIN</code>`, you must have the
[DELETE](../../account-management-sql-commands/grant.md) privilege for the [mysql.plugin](../system-tables/the-mysql-database-tables/mysql-plugin-table.md) table.


#### IF EXISTS


If the `<code>IF EXISTS</code>` clause is used, MariaDB will return a note instead of an error if the plugin does not exist. See [SHOW WARNINGS](../show/show-warnings.md).


## Examples


```
UNINSTALL PLUGIN example;
```

```
UNINSTALL PLUGIN IF EXISTS example;
Query OK, 0 rows affected (0.099 sec)

UNINSTALL PLUGIN IF EXISTS example;
Query OK, 0 rows affected, 1 warning (0.000 sec)

SHOW WARNINGS;
+-------+------+-------------------------------+
| Level | Code | Message                       |
+-------+------+-------------------------------+
| Note  | 1305 | PLUGIN example does not exist |
+-------+------+-------------------------------+
```

## See Also


* [Plugin Overview](../../../../plugins/plugin-overview.md)
* [mysql_plugin](../../../../../clients-and-utilities/legacy-clients-and-utilities/mysql_plugin.md)
* [INSTALL PLUGIN](install-plugin.md)
* [List of Plugins](../../../../plugins/information-on-plugins/list-of-plugins.md)

