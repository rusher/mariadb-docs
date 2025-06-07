# METADATA\_LOCK\_INFO Plugin

The `METADATA_LOCK_INFO` plugin creates the [METADATA\_LOCK\_INFO](../../sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-metadata_lock_info-table.md) table in the [INFORMATION\_SCHEMA](../../sql-statements/administrative-sql-statements/system-tables/information-schema/) database. This table shows active [metadata locks](../../sql-statements/transactions/metadata-locking.md). The table will be empty if there are no active metadata locks.

## Installing the Plugin

Although the plugin's shared library is distributed with MariaDB by default, the plugin is not actually installed by MariaDB by default. There are two methods that can be used to install the plugin with MariaDB.

The first method can be used to install the plugin without restarting the server. You can install the plugin dynamically by executing [INSTALL SONAME](../../sql-statements/administrative-sql-statements/plugin-sql-statements/install-soname.md) or [INSTALL PLUGIN](../../sql-statements/administrative-sql-statements/plugin-sql-statements/install-plugin.md). For example:

```
INSTALL SONAME 'metadata_lock_info';
```

The second method can be used to tell the server to load the plugin when it starts up. The plugin can be installed this way by providing the [--plugin-load](../../../server-management/install-and-upgrade-mariadb/starting-and-stopping-mariadb/mariadbd-options.md) or the [--plugin-load-add](../../../server-management/install-and-upgrade-mariadb/starting-and-stopping-mariadb/mariadbd-options.md) options. This can be specified as a command-line argument to [mysqld](../../../server-management/install-and-upgrade-mariadb/starting-and-stopping-mariadb/mariadbd-options.md) or it can be specified in a relevant server [option group](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md). For example:

```
[mariadb]
...
plugin_load_add = metadata_lock_info
```

## Uninstalling the Plugin

You can uninstall the plugin dynamically by executing [UNINSTALL SONAME](../../sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-soname.md) or [UNINSTALL PLUGIN](../../sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-plugin.md). For example:

```
UNINSTALL SONAME 'metadata_lock_info';
```

If you installed the plugin by providing the [--plugin-load](../../../server-management/install-and-upgrade-mariadb/starting-and-stopping-mariadb/mariadbd-options.md) or the [--plugin-load-add](../../../server-management/install-and-upgrade-mariadb/starting-and-stopping-mariadb/mariadbd-options.md) options in a relevant server [option group](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md), then those options should be removed to prevent the plugin from being loaded the next time the server is restarted.

## Examples

### Viewing all Metadata Locks

```
SELECT * FROM information_schema.metadata_lock_info;  
+-----------+--------------------------+---------------+----------------------+-----------------+-------------+
| THREAD_ID | LOCK_MODE                | LOCK_DURATION | LOCK_TYPE            | TABLE_SCHEMA    | TABLE_NAME  |  
+-----------+--------------------------+---------------+----------------------+-----------------+-------------+
|        31 | MDL_INTENTION_EXCLUSIVE  | MDL_EXPLICIT  | Global read lock     |                 |             |  
|        31 | MDL_INTENTION_EXCLUSIVE  | MDL_EXPLICIT  | Commit lock          |                 |             |
|        31 | MDL_INTENTION_EXCLUSIVE  | MDL_EXPLICIT  | Schema metadata lock | dbname          |             |
|        31 | MDL_SHARED_NO_READ_WRITE | MDL_EXPLICIT  | Table metadata lock  | dbname          | exotics     |
+-----------+--------------------------+---------------+----------------------+-----------------+-------------+
4 rows in set (0.00 sec)
```

### Matching Metadata Locks with Threads and Queries

```
SELECT 
CONCAT('Thread ',P.ID,' executing "',P.INFO,'" IS LOCKED BY Thread ',
M.THREAD_ID) WhoLocksWho 
FROM INFORMATION_SCHEMA.PROCESSLIST P,
INFORMATION_SCHEMA.METADATA_LOCK_INFO M 
WHERE LOCATE(lcase(LOCK_TYPE), lcase(STATE))>0;
+-----------------------------------------------------------------------------------+
| WhoLocksWho                                                                       |
+-----------------------------------------------------------------------------------+
| Thread 3 executing "INSERT INTO foo ( b ) VALUES ( 'FOO' )" IS LOCKED BY Thread 2 |
+-----------------------------------------------------------------------------------+
1 row in set (0.00 sec)

SHOW PROCESSLIST;
+----+------+-----------+------+---------+------+------------------------------+----------------------------------------+----------+
| Id | User | Host      | db   | Command | Time | State                        | Info                                   | Progress |
+----+------+-----------+------+---------+------+------------------------------+----------------------------------------+----------+
|  2 | root | localhost | test | Sleep   |  123 |                              | NULL                                   |    0.000 |
|  3 | root | localhost | test | Query   |  103 | Waiting for global read lock | INSERT INTO foo ( b ) VALUES ( 'FOO' ) |    0.000 |
|  4 | root | localhost | test | Query   |    0 | init                         | SHOW PROCESSLIST                       |    0.000 |
+----+------+-----------+------+---------+------+------------------------------+----------------------------------------+----------+
3 rows in set (0.00 sec)
```

## Versions

| Version | Status | Introduced                                                                                                                                                                          |
| ------- | ------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Version | Status | Introduced                                                                                                                                                                          |
| 0.1     | Stable | [MariaDB 10.1.13](broken-reference)                                                                                                                                                 |
| 0.1     | Beta   | [MariaDB 10.0.10](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/mariadb-10010-release-notes) |
| 0.1     | Alpha  | [MariaDB 10.0.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/mariadb-1007-release-notes)   |

## Options

### `metadata_lock_info`

* Description: Controls how the server should treat the plugin when the server starts up.
  * Valid values are:
    * `OFF` - Disables the plugin without removing it from the [mysql.plugins](../../sql-statements/administrative-sql-statements/system-tables/the-mysql-database-tables/mysql-plugin-table.md) table.
    * `ON` - Enables the plugin. If the plugin cannot be initialized, then the server will still continue starting up, but the plugin will be disabled.
    * `FORCE` - Enables the plugin. If the plugin cannot be initialized, then the server will fail to start with an error.
    * `FORCE_PLUS_PERMANENT` - Enables the plugin. If the plugin cannot be initialized, then the server will fail to start with an error. In addition, the plugin cannot be uninstalled with [UNINSTALL SONAME](../../sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-soname.md) or [UNINSTALL PLUGIN](../../sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-plugin.md) while the server is running.
  * See [Plugin Overview: Configuring Plugin Activation at Server Startup](../plugin-overview.md#configuring-plugin-activation-at-server-startup) for more information.
* Commandline: `--metadata-lock-info=value`
* Data Type: `enumerated`
* Default Value: `ON`
* Valid Values: `OFF`, `ON`, `FORCE`, `FORCE_PLUS_PERMANENT`

CC BY-SA / Gnu FDL
