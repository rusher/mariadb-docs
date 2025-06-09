# UNINSTALL SONAME

## Syntax

```
UNINSTALL SONAME  [IF EXISTS] 'plugin_library'
```

## Description

This statement is a variant of [UNINSTALL PLUGIN](uninstall-plugin.md) statement, that removes all [plugins](../../../plugins/) belonging to a specified `plugin_library`. See [UNINSTALL PLUGIN](uninstall-plugin.md) for details.

`plugin_library` is the name of the shared library that\
contains the plugin code. The file name extension (for\
example, `libmyplugin.so` or `libmyplugin.dll`) can be omitted (which makes the statement look the same on all architectures).

To use `UNINSTALL SONAME`, you must have the[DELETE privilege](../../account-management-sql-statements/grant.md) for the `mysql.plugin` table.

#### IF EXISTS

If the `IF EXISTS` clause is used, MariaDB will return a note instead of an error if the plugin library does not exist. See [SHOW WARNINGS](../show/show-warnings.md).

## Examples

To uninstall the XtraDB plugin and all of its `information_schema` tables with one statement, use

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
* [SHOW PLUGINS](../show/show-plugins.md)
* [INSTALL PLUGIN](install-plugin.md)
* [UNINSTALL PLUGIN](uninstall-plugin.md)
* [SHOW PLUGINS](../show/show-plugins.md)
* [INFORMATION\_SCHEMA.PLUGINS Table](../system-tables/information-schema/information-schema-tables/plugins-table-information-schema.md)
* [mysql\_plugin](../../../../clients-and-utilities/legacy-clients-and-utilities/mysql_plugin.md)
* [List of Plugins](../../../plugins/information-on-plugins/list-of-plugins.md)

CC BY-SA / Gnu FDL

{% @marketo/form formId="4316" %}
