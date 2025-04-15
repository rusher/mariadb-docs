
# UNINSTALL SONAME

## Syntax


```
UNINSTALL SONAME  [IF EXISTS] 'plugin_library'
```


## Description


This statement is a variant of [UNINSTALL PLUGIN](uninstall-plugin.md) statement, that removes all [plugins](../../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/general-development-information/development-plans/old-plans/plugins-storage-engines-summit-for-mysqlmariadbdrizzle-2011.md) belonging to a specified `<code>plugin_library</code>`. See [UNINSTALL PLUGIN](uninstall-plugin.md) for details.


`<code class="highlight fixed" style="white-space:pre-wrap">plugin_library</code>` is the name of the shared library that
contains the plugin code. The file name extension (for
example, `<code>libmyplugin.so</code>` or `<code>libmyplugin.dll</code>`) can be omitted (which makes the statement look the same on all architectures).


To use `<code class="highlight fixed" style="white-space:pre-wrap">UNINSTALL SONAME</code>`, you must have the
[DELETE privilege](../../account-management-sql-commands/grant.md) for the `<code>mysql.plugin</code>` table.


#### IF EXISTS


If the `<code>IF EXISTS</code>` clause is used, MariaDB will return a note instead of an error if the plugin library does not exist. See [SHOW WARNINGS](../show/show-warnings.md).


## Examples


To uninstall the XtraDB plugin and all of its `<code>information_schema</code>` tables with one statement, use


```
UNINSTALL SONAME 'ha_xtradb';
```

```
UNINSTALL SONAME IF EXISTS 'ha_example';
Query OK, 0 rows affected (0.099 sec)

UNINSTALL SONAME IF EXISTS 'ha_example';
Query OK, 0 rows affected, 1 warning (0.000 sec)

SHOW WARNINGS;
+-------+------+-------------------------------------+
| Level | Code | Message                             |
+-------+------+-------------------------------------+
| Note  | 1305 | SONAME ha_example.so does not exist |
+-------+------+-------------------------------------+
```

## See Also


* [INSTALL SONAME](install-soname.md)
* [SHOW PLUGINS](../show/show-plugins-soname.md)
* [INSTALL PLUGIN](install-plugin.md)
* [UNINSTALL PLUGIN](uninstall-plugin.md)
* [SHOW PLUGINS](../show/show-plugins-soname.md)
* [INFORMATION_SCHEMA.PLUGINS Table](../system-tables/information-schema/information-schema-tables/plugins-table-information-schema.md)
* [mysql_plugin](../../../../../clients-and-utilities/legacy-clients-and-utilities/mysql_plugin.md)
* [List of Plugins](../../../../plugins/information-on-plugins/list-of-plugins.md)

