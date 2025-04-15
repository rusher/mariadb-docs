# WSREP_INFO Plugin

The `WSREP_INFO` plugin library contains the following plugins:

* `WSREP_MEMBERSHIP`
* `WSREP_STATUS`

The `WSREP_MEMBERSHIP` plugin creates the [WSREP_MEMBERSHIP](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-wsrep_membership-table.md) table in the [INFORMATION_SCHEMA](../../../server-usage/programming-customizing-mariadb/views/information-schema-views-table.md) database. The plugin also adds the [SHOW WSREP_MEMBERSHIP](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-wsrep_membership.md) statement.

The `WSREP_STATUS` plugin creates the [WSREP_STATUS](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-wsrep_status-table.md) table in the [INFORMATION_SCHEMA](../../../server-usage/programming-customizing-mariadb/views/information-schema-views-table.md) database. The plugin also adds the [SHOW WSREP_STATUS](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-wsrep_status.md) statement.

These tables and statements provide information about [Galera](../../../server-usage/replication-cluster-multi-master/galera-cluster/galera-use-cases.md). Only users with the [SUPER](../../sql-statements-and-structure/sql-statements/account-management-sql-commands/grant.md#global-privileges) privilege can access this information.

#

# Installing the Plugin

Although the plugin's shared library is distributed with MariaDB by default, the plugin is not actually installed by MariaDB by default. There are two methods that can be used to install the plugin with MariaDB.

The first method can be used to install the plugin without restarting the server. You can install the plugin dynamically by executing [INSTALL SONAME](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/install-soname.md) or [INSTALL PLUGIN](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/install-plugin.md). For example:

```
INSTALL SONAME 'wsrep_info';
```

The second method can be used to tell the server to load the plugin when it starts up. The plugin can be installed this way by providing the [--plugin-load](/en/mysqld-options/#-plugin-load) or the [--plugin-load-add](/en/mysqld-options/#-plugin-load-add) options. This can be specified as a command-line argument to [mysqld](/en/mysqld-options/) or it can be specified in a relevant server [option group](../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md). For example:

```
[mariadb]
...
plugin_load_add = wsrep_info
```

#

# Uninstalling the Plugin

You can uninstall the plugin dynamically by executing [UNINSTALL SONAME](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-soname.md) or [UNINSTALL PLUGIN](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-plugin.md). For example:

```
UNINSTALL SONAME 'wsrep_info';
```

If you installed the plugin by providing the [--plugin-load](/en/mysqld-options/#-plugin-load) or the [--plugin-load-add](/en/mysqld-options/#-plugin-load-add) options in a relevant server [option group](../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md), then those options should be removed to prevent the plugin from being loaded the next time the server is restarted.

#

# Example

```
SHOW TABLES FROM information_schema LIKE 'WSREP%';
+---------------------------------------+
| Tables_in_information_schema (WSREP%) |
+---------------------------------------+
| WSREP_STATUS |
| WSREP_MEMBERSHIP |
+---------------------------------------+
```

#

# Versions

| Version | Status | Introduced |
| --- | --- | --- |
| Version | Status | Introduced |
| 1.0 | Stable | [MariaDB 10.1.18](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/release-notes-mariadb-101-series/mariadb-10118-release-notes) |
| 1.0 | Gamma | [MariaDB 10.1.13](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/release-notes-mariadb-101-series/mariadb-10113-release-notes) |
| 1.0 | Alpha | [MariaDB 10.1.2](/en/mariadb-1012-release-notes/) |

#

# Options

#

## `wsrep_membership`

* Description: Controls how the server should treat the plugin when the server starts up.

 * Valid values are:

 * `OFF` - Disables the plugin without removing it from the [mysql.plugins](/en/mysqlplugin-table/) table.
 * `ON` - Enables the plugin. If the plugin cannot be initialized, then the server will still continue starting up, but the plugin will be disabled.
 * `FORCE` - Enables the plugin. If the plugin cannot be initialized, then the server will fail to start with an error.
 * `FORCE_PLUS_PERMANENT` - Enables the plugin. If the plugin cannot be initialized, then the server will fail to start with an error. In addition, the plugin cannot be uninstalled with [UNINSTALL SONAME](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-soname.md) or [UNINSTALL PLUGIN](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-plugin.md) while the server is running.
 * See [Plugin Overview: Configuring Plugin Activation at Server Startup](../plugin-overview.md#configuring-plugin-activation-at-server-startup) for more information.
* Commandline: `--wsrep-membership=value`
* Data Type: `enumerated`
* Default Value: `ON`
* Valid Values: `OFF`, `ON`, `FORCE`, `FORCE_PLUS_PERMANENT`

#

## `wsrep_status`

* Description: Controls how the server should treat the plugin when the server starts up.

 * Valid values are:

 * `OFF` - Disables the plugin without removing it from the [mysql.plugins](/en/mysqlplugin-table/) table.
 * `ON` - Enables the plugin. If the plugin cannot be initialized, then the server will still continue starting up, but the plugin will be disabled.
 * `FORCE` - Enables the plugin. If the plugin cannot be initialized, then the server will fail to start with an error.
 * `FORCE_PLUS_PERMANENT` - Enables the plugin. If the plugin cannot be initialized, then the server will fail to start with an error. In addition, the plugin cannot be uninstalled with [UNINSTALL SONAME](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-soname.md) or [UNINSTALL PLUGIN](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-plugin.md) while the server is running.
 * See [Plugin Overview: Configuring Plugin Activation at Server Startup](../plugin-overview.md#configuring-plugin-activation-at-server-startup) for more information.
* Commandline: `--wsrep-status=value`
* Data Type: `enumerated`
* Default Value: `ON`
* Valid Values: `OFF`, `ON`, `FORCE`, `FORCE_PLUS_PERMANENT`