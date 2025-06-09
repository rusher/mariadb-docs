# BLACKHOLE

The `BLACKHOLE` storage engine accepts data but does not store it and always returns an empty result.

A table using the `BLACKHOLE` storage engine consists of a single .frm table format file, but no associated data or index files.

This storage engine can be useful, for example, if you want to run complex filtering rules on a slave without incurring any overhead on a master. The master can run a `BLACKHOLE` storage engine, with the data replicated to the slave for processing.

## Installing the Plugin

Although the plugin's shared library is distributed with MariaDB by default, the plugin is not actually installed by MariaDB by default. There are two methods that can be used to install the plugin with MariaDB.

The first method can be used to install the plugin without restarting the server. You can install the plugin dynamically by executing [INSTALL SONAME](../sql-statements/administrative-sql-statements/plugin-sql-statements/install-soname.md) or [INSTALL PLUGIN](../sql-statements/administrative-sql-statements/plugin-sql-statements/install-plugin.md). For example:

```sql
INSTALL SONAME 'ha_blackhole';
```

The second method can be used to tell the server to load the plugin when it starts up. The plugin can be installed this way by providing the [--plugin-load](../../server-management/starting-and-stopping-mariadb/mariadbd-options.md) or the [--plugin-load-add](../../server-management/starting-and-stopping-mariadb/mariadbd-options.md) options. This can be specified as a command-line argument to [mysqld](../../server-management/starting-and-stopping-mariadb/mariadbd-options.md) or it can be specified in a relevant server [option group](../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md). For example:

```
[mariadb]
...
plugin_load_add = ha_blackhole
```

## Uninstalling the Plugin

You can uninstall the plugin dynamically by executing [UNINSTALL SONAME](../sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-soname.md) or [UNINSTALL PLUGIN](../sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-plugin.md). For example:

```sql
UNINSTALL SONAME 'ha_blackhole';
```

If you installed the plugin by providing the [--plugin-load](../../server-management/starting-and-stopping-mariadb/mariadbd-options.md) or the [--plugin-load-add](../../server-management/starting-and-stopping-mariadb/mariadbd-options.md) options in a relevant server [option group](../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md), then those options should be removed to prevent the plugin from being loaded the next time the server is restarted.

## Using the BLACKHOLE Storage Engine

### Using with DML

[INSERT](../sql-statements/data-manipulation/inserting-loading-data/insert.md), [UPDATE](../sql-statements/data-manipulation/changing-deleting-data/update.md), and [DELETE](../sql-statements/data-manipulation/changing-deleting-data/delete.md) statements all work with the `BLACKHOLE` storage engine. However, no data changes are actually applied.

### Using with Replication

If the binary log is enabled, all SQL statements will be logged as usual, and replicated to any slave servers. However, since rows are not stored, it is important to use statement-based rather than the row or mixed format, as [UPDATE](../sql-statements/data-manipulation/changing-deleting-data/update.md) and [DELETE](../sql-statements/data-manipulation/changing-deleting-data/delete.md) statements are neither logged nor replicated. See [Binary Log Formats](../../server-management/server-monitoring-logs/binary-log/binary-log-formats.md).

### Using with Triggers

Some [triggers](../../server-usage/triggers-events/triggers/) work with the `BLACKHOLE` storage engine.

`BEFORE` [triggers](../../server-usage/triggers-events/triggers/) for [INSERT](../sql-statements/data-manipulation/inserting-loading-data/insert.md) statements are still activated.

[Triggers](../../server-usage/triggers-events/triggers/) for [UPDATE](../sql-statements/data-manipulation/changing-deleting-data/update.md) and [DELETE](../sql-statements/data-manipulation/changing-deleting-data/delete.md) statements are **not** activated.

[Triggers](../../server-usage/triggers-events/triggers/) with the `FOR EACH ROW` clause do not apply, since the tables have no rows.

### Using with Foreign Keys

Foreign keys are not supported. If you convert an [InnoDB](innodb/) table to `BLACKHOLE`, then the foreign keys will disappear. If you convert the same table back to InnoDB, then you will have to recreate them.

### Using with Virtual Columns

If you convert an [InnoDB](innodb/) table which contains [virtual columns](../sql-statements/data-definition/create/generated-columns.md) to `BLACKHOLE`, then it produces an error.

### Using with AUTO\_INCREMENT

Because a BLACKHOLE table does not store data, it will not maintain the [AUTO\_INCREMENT](../data-types/auto_increment.md) value. If you are replicating to a table that can handle `AUTO_INCREMENT` columns, and are not explicitly setting the primary key auto-increment value in the [INSERT](../sql-statements/data-manipulation/inserting-loading-data/insert.md) query, or using the [SET](../sql-statements/administrative-sql-statements/set-commands/set.md) [INSERT\_ID](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#insert_id) statement, inserts will fail on the slave due to duplicate keys.

## Limits

The maximum key size is:

* 3500 bytes (>= [MariaDB 10.1.48](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-1-series/mariadb-10148-release-notes), [MariaDB 10.2.35](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-10235-release-notes), [MariaDB 10.3.26](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-10326-release-notes), [MariaDB 10.4.16](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/mariadb-10416-release-notes) and [MariaDB 10.5.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/mariadb-1057-release-notes))
* 1000 bytes (<= [MariaDB 10.1.47](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-1-series/mariadb-10147-release-notes), [MariaDB 10.2.34](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-10234-release-notes), [MariaDB 10.3.25](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-10325-release-notes), [MariaDB 10.4.15](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/mariadb-10415-release-notes) and [MariaDB 10.5.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/mariadb-1056-release-notes)).

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

CC BY-SA / Gnu FDL

{% @marketo/form formId="4316" %}
