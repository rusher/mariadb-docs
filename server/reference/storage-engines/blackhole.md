
# BLACKHOLE

The `<code>BLACKHOLE</code>` storage engine accepts data but does not store it and always returns an empty result.


A table using the `<code>BLACKHOLE</code>` storage engine consists of a single .frm table format file, but no associated data or index files.


This storage engine can be useful, for example, if you want to run complex filtering rules on a slave without incurring any overhead on a master. The master can run a `<code>BLACKHOLE</code>` storage engine, with the data replicated to the slave for processing.



## Installing the Plugin


Although the plugin's shared library is distributed with MariaDB by default, the plugin is not actually installed by MariaDB by default. There are two methods that can be used to install the plugin with MariaDB.


The first method can be used to install the plugin without restarting the server. You can install the plugin dynamically by executing [INSTALL SONAME](../sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/install-soname.md) or [INSTALL PLUGIN](../sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/install-plugin.md). For example:


```
INSTALL SONAME 'ha_blackhole';
```

The second method can be used to tell the server to load the plugin when it starts up. The plugin can be installed this way by providing the [--plugin-load](../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md) or the [--plugin-load-add](../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md) options. This can be specified as a command-line argument to [mysqld](../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md) or it can be specified in a relevant server [option group](../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md). For example:


```
[mariadb]
...
plugin_load_add = ha_blackhole
```

## Uninstalling the Plugin


You can uninstall the plugin dynamically by executing [UNINSTALL SONAME](../sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-soname.md) or [UNINSTALL PLUGIN](../sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-plugin.md). For example:


```
UNINSTALL SONAME 'ha_blackhole';
```

If you installed the plugin by providing the [--plugin-load](../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md) or the [--plugin-load-add](../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md) options in a relevant server [option group](../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md), then those options should be removed to prevent the plugin from being loaded the next time the server is restarted.


## Using the BLACKHOLE Storage Engine


### Using with DML


[INSERT](../sql-statements-and-structure/sql-statements/built-in-functions/string-functions/insert-function.md), [UPDATE](../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/tools/buildbot/buildbot-setup/buildbot-setup-for-virtual-machines/buildbot-setup-for-virtual-machines-additional-steps/update-debian-4-mirrors-for-buildbot-vms.md), and [DELETE](../sql-statements-and-structure/sql-statements/data-manipulation/changing-deleting-data/delete.md) statements all work with the `<code>BLACKHOLE</code>` storage engine. However, no data changes are actually applied.


### Using with Replication


If the binary log is enabled, all SQL statements will be logged as usual, and replicated to any slave servers. However, since rows are not stored, it is important to use statement-based rather than the row or mixed format, as [UPDATE](../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/tools/buildbot/buildbot-setup/buildbot-setup-for-virtual-machines/buildbot-setup-for-virtual-machines-additional-steps/update-debian-4-mirrors-for-buildbot-vms.md) and [DELETE](../sql-statements-and-structure/sql-statements/data-manipulation/changing-deleting-data/delete.md) statements are neither logged nor replicated. See [Binary Log Formats](../../server-management/server-monitoring-logs/binary-log/binary-log-formats.md).


### Using with Triggers


Some [triggers](../../server-usage/programming-customizing-mariadb/triggers-events/triggers/triggers-and-implicit-locks.md) work with the `<code>BLACKHOLE</code>` storage engine.


`<code>BEFORE</code>` [triggers](../../server-usage/programming-customizing-mariadb/triggers-events/triggers/triggers-and-implicit-locks.md) for [INSERT](../sql-statements-and-structure/sql-statements/built-in-functions/string-functions/insert-function.md) statements are still activated.


[Triggers](../../server-usage/programming-customizing-mariadb/triggers-events/triggers/triggers-and-implicit-locks.md) for [UPDATE](../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/tools/buildbot/buildbot-setup/buildbot-setup-for-virtual-machines/buildbot-setup-for-virtual-machines-additional-steps/update-debian-4-mirrors-for-buildbot-vms.md) and [DELETE](../sql-statements-and-structure/sql-statements/data-manipulation/changing-deleting-data/delete.md) statements are **not** activated.


[Triggers](../../server-usage/programming-customizing-mariadb/triggers-events/triggers/triggers-and-implicit-locks.md) with the `<code>FOR EACH ROW</code>` clause do not apply, since the tables have no rows.


### Using with Foreign Keys


Foreign keys are not supported. If you convert an [InnoDB](../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/innodb-upgrade-tests/README.md) table to `<code>BLACKHOLE</code>`, then the foreign keys will disappear. If you convert the same table back to InnoDB, then you will have to recreate them.


### Using with Virtual Columns


If you convert an [InnoDB](../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/innodb-upgrade-tests/README.md) table which contains [virtual columns](../sql-statements-and-structure/sql-statements/data-definition/create/generated-columns.md) to `<code>BLACKHOLE</code>`, then it produces an error.


### Using with AUTO_INCREMENT


Because a BLACKHOLE table does not store data, it will not maintain the [AUTO_INCREMENT](innodb/auto_increment-handling-in-innodb.md) value. If you are replicating to a table that can handle `<code>AUTO_INCREMENT</code>` columns, and are not explicitly setting the primary key auto-increment value in the [INSERT](../sql-statements-and-structure/sql-statements/built-in-functions/string-functions/insert-function.md) query, or using the [SET](../../../connectors/mariadb-connector-cpp/setup-for-connector-cpp-examples.md) [INSERT_ID](../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#insert_id) statement, inserts will fail on the slave due to duplicate keys.


## Limits


The maximum key size is:


* 3500 bytes (>= [MariaDB 10.1.48](../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10148-release-notes.md), [MariaDB 10.2.35](../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-10235-release-notes.md), [MariaDB 10.3.26](../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-10326-release-notes.md), [MariaDB 10.4.16](../../../release-notes/mariadb-community-server/release-notes-mariadb-10-4-series/mariadb-10416-release-notes.md) and [MariaDB 10.5.7](../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1057-release-notes.md))
* 1000 bytes (<= [MariaDB 10.1.47](../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10147-release-notes.md), [MariaDB 10.2.34](../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-10234-release-notes.md), [MariaDB 10.3.25](../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-10325-release-notes.md), [MariaDB 10.4.15](../../../release-notes/mariadb-community-server/release-notes-mariadb-10-4-series/mariadb-10415-release-notes.md) and [MariaDB 10.5.6](../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1056-release-notes.md)).


## Examples


```
CREATE TABLE table_name (
   id int unsigned primary key not null,
   v varchar(30)
) ENGINE=BLACKHOLE;

INSERT INTO table_name VALUES (1, 'bob'),(2, 'jane');

SELECT * FROM table_name;
Empty set (0.001 sec)
```
