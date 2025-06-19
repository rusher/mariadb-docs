
# SHOW PLUGINS SONAME

## Syntax


```
SHOW PLUGINS SONAME { library | LIKE 'pattern' | WHERE expr };
```

## Description


`SHOW PLUGINS SONAME` displays information about compiled-in and all server plugins in the [plugin_dir](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#plugin_dir) directory, including plugins that haven't been installed.


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

There is also a corresponding [information_schema](../system-tables/information-schema/README.md) table, called [ALL_PLUGINS](../system-tables/information-schema/information-schema-tables/all-plugins-table-information-schema.md), which contains more complete information.


<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>


{% @marketo/form formId="4316" %}
