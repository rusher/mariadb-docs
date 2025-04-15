
# Archive

The `<code>ARCHIVE</code>` storage engine is a storage engine that uses gzip to compress rows. It is mainly used for storing large amounts of data, without indexes, with only a very small footprint.


A table using the `<code>ARCHIVE</code>` storage engine is stored in two files on disk. There's a table definition file with an extension of .frm, and a data file with the extension .ARZ. At times during optimization, a .ARN file will appear.


New rows are inserted into a compression buffer and are flushed to disk when needed. SELECTs cause a flush. Sometimes, rows created by multi-row inserts are not visible until the statement is complete.


`<code>ARCHIVE</code>` allows a maximum of one key. The key must be on an `<code>[AUTO_INCREMENT](../innodb/auto_increment-handling-in-innodb.md)</code>` column, and can be a `<code>PRIMARY KEY</code>` or a non-unique key. However, it has a limitation: it is not possible to insert a value which is lower than the next `<code>AUTO_INCREMENT</code>` value.



## Installing the Plugin


Although the plugin's shared library is distributed with MariaDB by default, the plugin is not actually installed by MariaDB by default. There are two methods that can be used to install the plugin with MariaDB.


The first method can be used to install the plugin without restarting the server. You can install the plugin dynamically by executing `<code>[INSTALL SONAME](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/install-soname.md)</code>` or `<code>[INSTALL PLUGIN](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/install-plugin.md)</code>`. For example:


```
INSTALL SONAME 'ha_archive';
```

The second method can be used to tell the server to load the plugin when it starts up. The plugin can be installed this way by providing the `<code>[--plugin-load](../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md)</code>` or the `<code>[--plugin-load-add](../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md)</code>` options. This can be specified as a command-line argument to `<code>[mysqld](../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md)</code>` or it can be specified in a relevant server [option group](../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md). For example:


```
[mariadb]
...
plugin_load_add = ha_archive
```

## Uninstalling the Plugin


You can uninstall the plugin dynamically by executing `<code>[UNINSTALL SONAME](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-soname.md)</code>` or `<code>[UNINSTALL PLUGIN](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-plugin.md)</code>`. For example:


```
UNINSTALL SONAME 'ha_archive';
```

If you installed the plugin by providing the `<code>[--plugin-load](../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md)</code>` or the `<code>[--plugin-load-add](../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md)</code>` options in a relevant server [option group](../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md), then those options should be removed to prevent the plugin from being loaded the next time the server is restarted.


## Characteristics


* Supports [INSERT](../../sql-statements-and-structure/sql-statements/built-in-functions/string-functions/insert-function.md) and [SELECT](../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/benchmarks-and-long-running-tests/benchmark-results/select-random-ranges-and-select-random-point.md), but not [DELETE](../../sql-statements-and-structure/sql-statements/data-manipulation/changing-deleting-data/delete.md), [UPDATE](../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/tools/buildbot/buildbot-setup/buildbot-setup-for-virtual-machines/buildbot-setup-for-virtual-machines-additional-steps/update-debian-4-mirrors-for-buildbot-vms.md) or [REPLACE](../../sql-statements-and-structure/sql-statements/built-in-functions/string-functions/replace-function.md).
* Data is compressed with zlib as it is inserted, making it very small.
* Data is slow the select, as it needs to be uncompressed, and, besides the [query cache](../../plugins/other-plugins/query-cache-information-plugin.md), there is no cache.
* Supports AUTO_INCREMENT (since MariaDB/MySQL 5.1.6), which can be a unique or a non-unique index.
* Since MariaDB/MySQL 5.1.6, selects scan past BLOB columns unless they are specifically requested, making these queries much more efficient.
* Does not support [spatial](../../sql-statements-and-structure/geographic-geometric-features/spatial-index.md) data types.
* Does not support [transactions](../../../../connectors/mariadb-connector-cpp/transactions-with-mariadb-connector-cpp.md).
* Does not support foreign keys.
* Does not support [virtual columns](../../sql-statements-and-structure/sql-statements/data-definition/create/generated-columns.md).
* No storage limit.
* Supports row locking.
* Supports [table discovery](../storage-engines-storage-engine-development/table-discovery.md), and the server can access ARCHIVE tables even if the corresponding `<code>.frm</code>` file is missing.
* [OPTIMIZE TABLE](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/optimizing-tables/optimize-table.md) and [REPAIR TABLE](../../sql-statements-and-structure/sql-statements/table-statements/repair-table.md) can be used to compress the table in its entirety, resulting in slightly better compression.
* With MariaDB, it is possible to upgrade from the MySQL 5.0 format without having to dump the tables.
* [INSERT DELAYED](../../sql-statements-and-structure/sql-statements/data-manipulation/inserting-loading-data/insert-delayed.md) is supported.
* Running many SELECTs during the insertions can deteriorate the compression, unless only multi-rows INSERTs and INSERT DELAYED are used.

