
# SHOW PLUGINS

## Syntax


```
SHOW PLUGINS;
```


## Description


`<code class="highlight fixed" style="white-space:pre-wrap">SHOW PLUGINS</code>` displays information about installed [plugins](../../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/general-development-information/development-plans/old-plans/plugins-storage-engines-summit-for-mysqlmariadbdrizzle-2011.md). The `<code>Library</code>` column indicates the plugin library - if it is `<code>NULL</code>`, the plugin is built-in and cannot be uninstalled.


The `<code>[PLUGINS](../system-tables/information-schema/information-schema-tables/plugins-table-information-schema.md)</code>` table in the `<code>information_schema</code>` database contains more detailed information.


For specific information about storage engines (a particular type of plugin), see the `<code>[information_schema.ENGINES](../system-tables/information-schema/information-schema-tables/information-schema-engines-table.md)</code>` table and the `<code>[SHOW ENGINES](show-engines.md)</code>` statement.


## Examples


```
SHOW PLUGINS;
+----------------------------+----------+--------------------+-------------+---------+
| Name                       | Status   | Type               | Library     | License |
+----------------------------+----------+--------------------+-------------+---------+
| binlog                     | ACTIVE   | STORAGE ENGINE     | NULL        | GPL     |
| mysql_native_password      | ACTIVE   | AUTHENTICATION     | NULL        | GPL     |
| mysql_old_password         | ACTIVE   | AUTHENTICATION     | NULL        | GPL     |
| MRG_MyISAM                 | ACTIVE   | STORAGE ENGINE     | NULL        | GPL     |
| MyISAM                     | ACTIVE   | STORAGE ENGINE     | NULL        | GPL     |
| CSV                        | ACTIVE   | STORAGE ENGINE     | NULL        | GPL     |
| MEMORY                     | ACTIVE   | STORAGE ENGINE     | NULL        | GPL     |
| FEDERATED                  | ACTIVE   | STORAGE ENGINE     | NULL        | GPL     |
| PERFORMANCE_SCHEMA         | ACTIVE   | STORAGE ENGINE     | NULL        | GPL     |
| Aria                       | ACTIVE   | STORAGE ENGINE     | NULL        | GPL     |
| InnoDB                     | ACTIVE   | STORAGE ENGINE     | NULL        | GPL     |
| INNODB_TRX                 | ACTIVE   | INFORMATION SCHEMA | NULL        | GPL     |
...
| INNODB_SYS_FOREIGN         | ACTIVE   | INFORMATION SCHEMA | NULL        | GPL     |
| INNODB_SYS_FOREIGN_COLS    | ACTIVE   | INFORMATION SCHEMA | NULL        | GPL     |
| SPHINX                     | ACTIVE   | STORAGE ENGINE     | NULL        | GPL     |
| ARCHIVE                    | ACTIVE   | STORAGE ENGINE     | NULL        | GPL     |
| BLACKHOLE                  | ACTIVE   | STORAGE ENGINE     | NULL        | GPL     |
| FEEDBACK                   | DISABLED | INFORMATION SCHEMA | NULL        | GPL     |
| partition                  | ACTIVE   | STORAGE ENGINE     | NULL        | GPL     |
| pam                        | ACTIVE   | AUTHENTICATION     | auth_pam.so | GPL     |
+----------------------------+----------+--------------------+-------------+---------+
```

## See Also


* [List of Plugins](../../../../plugins/information-on-plugins/list-of-plugins.md)
* [Plugin Overview](../../../../plugins/plugin-overview.md)
* [INFORMATION_SCHEMA.PLUGINS Table](../system-tables/information-schema/information-schema-tables/plugins-table-information-schema.md)
* [INSTALL PLUGIN](../plugin-sql-statements/install-plugin.md)
* [INFORMATION_SCHEMA.ALL_PLUGINS Table](../system-tables/information-schema/information-schema-tables/all-plugins-table-information-schema.md) (all plugins, installed or not)
* [INSTALL SONAME](../plugin-sql-statements/install-soname.md)
* [UNINSTALL PLUGIN](../plugin-sql-statements/uninstall-plugin.md)
* [UNINSTALL SONAME](../plugin-sql-statements/uninstall-soname.md)

