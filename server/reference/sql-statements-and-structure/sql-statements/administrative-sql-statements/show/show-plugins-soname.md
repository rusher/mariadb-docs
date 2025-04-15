
# SHOW PLUGINS SONAME

## Syntax


```
SHOW PLUGINS SONAME { library | LIKE 'pattern' | WHERE expr };
```

## Description


`<code class="highlight fixed" style="white-space:pre-wrap">SHOW PLUGINS SONAME</code>` displays information about compiled-in and all server plugins in the `<code>[plugin_dir](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#plugin_dir)</code>` directory, including plugins that haven't been installed.


## Examples


```
SHOW PLUGINS SONAME 'ha_example.so';
+----------+---------------+----------------+---------------+---------+
| Name     | Status        | Type           | Library       | License |
+----------+---------------+----------------+---------------+---------+
| EXAMPLE  | NOT INSTALLED | STORAGE ENGINE | ha_example.so | GPL     |
| UNUSABLE | NOT INSTALLED | DAEMON         | ha_example.so | GPL     |
+----------+---------------+----------------+---------------+---------+
```

There is also a corresponding `<code>[information_schema](../../../../mariadb-internals/information-schema-plugins-show-and-flush-statements.md)</code>` table, called `<code>[ALL_PLUGINS](../system-tables/information-schema/information-schema-tables/all-plugins-table-information-schema.md)</code>`, which contains more complete information.

