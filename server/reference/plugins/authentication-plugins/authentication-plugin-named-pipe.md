
# Authentication Plugin - Named Pipe

The `named_pipe` authentication plugin allows the user to use operating system credentials when connecting to MariaDB via named pipe on Windows. Named pipe connections are enabled by the `[named_pipe](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#named_pipe)` system variable.


The `named_pipe` authentication plugin works by using [named pipe impersonation](https://msdn.microsoft.com/en-us/library/windows/desktop/aa378618%28v=vs.85%29.aspx) and calling `GetUserName()` to retrieve the user name of the process that is connected to the named pipe. Once it has the user name, it authenticates the connecting user as the MariaDB account that has the same user name.



## Installing the Plugin


Although the plugin's shared library is distributed with MariaDB by default, the plugin is not actually installed by MariaDB by default. There are two methods that can be used to install the plugin with MariaDB.


The first method can be used to install the plugin without restarting the server. You can install the plugin dynamically by executing `[INSTALL SONAME](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/install-soname.md)` or `[INSTALL PLUGIN](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/install-plugin.md)`. For example:


```
INSTALL SONAME 'auth_named_pipe';
```

The second method can be used to tell the server to load the plugin when it starts up. The plugin can be installed this way by providing the `[--plugin-load](../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md)` or the `[--plugin-load-add](../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md)` options. This can be specified as a command-line argument to `[mysqld](../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md)` or it can be specified in a relevant server [option group](../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md). For example:


```
[mariadb]
...
plugin_load_add = auth_named_pipe
```

## Uninstalling the Plugin


You can uninstall the plugin dynamically by executing `[UNINSTALL SONAME](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-soname.md)` or `[UNINSTALL PLUGIN](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-plugin.md)`. For example:


```
UNINSTALL SONAME 'auth_named_pipe';
```

If you installed the plugin by providing the `[--plugin-load](../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md)` or the `[--plugin-load-add](../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md)` options in a relevant server [option group](../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md), then those options should be removed to prevent the plugin from being loaded the next time the server is restarted.


## Creating Users


To create a user account via `[CREATE USER](../../sql-statements-and-structure/sql-statements/account-management-sql-commands/create-user.md)`, specify the name of the plugin in the `[IDENTIFIED VIA](../../sql-statements-and-structure/sql-statements/account-management-sql-commands/create-user.md#identified-viawith-authentication_plugin)` clause. For example:


```
CREATE USER username@hostname IDENTIFIED VIA named_pipe;
```

If `[SQL_MODE](../../../server-management/variables-and-modes/sql-mode.md)` does not have `NO_AUTO_CREATE_USER` set, then you can also create the user account via `[GRANT](../../sql-statements-and-structure/sql-statements/account-management-sql-commands/grant.md)`. For example:


```
GRANT SELECT ON db.* TO username@hostname IDENTIFIED VIA named_pipe;
```

## Client Authentication Plugins


The `named_pipe` authentication plugin does not require any specific client authentication plugins. It should work with all clients.


## Support in Client Libraries


The `named_pipe` authentication plugin does not require any special support in client libraries. It should work with all client libraries.


## Example


```
CREATE USER wlad IDENTIFIED VIA named_pipe;
CREATE USER monty IDENTIFIED VIA named_pipe;
quit

C:\>echo %USERNAME%
wlad

C:\> mysql --user=wlad --protocol=PIPE
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 4
Server version: 10.1.12-MariaDB-debug Source distribution

Copyright (c) 2000, 2015, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> quit
Bye

C:\> mysql --user=monty  --protocol=PIPE
ERROR 1698 (28000): Access denied for user 'monty'@'localhost'
```

In this example, a user `wlad` is already logged into the system. Because he has identified himself to the operating system, he does not need to do it again for the database — MariaDB trusts the operating system credentials. However, he cannot connect to the database as another user.


## Versions



| Version | Status | Introduced |
| --- | --- | --- |
| Version | Status | Introduced |
| 1.0 | Stable | [MariaDB 10.1.11](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10111-release-notes) |



## Options


### `named_pipe`


* Description: Controls how the server should treat the plugin when the server starts up.

  * Valid values are:

    * `OFF` - Disables the plugin without removing it from the `[mysql.plugins](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/the-mysql-database-tables/mysql-plugin-table.md)` table.
    * `ON` - Enables the plugin. If the plugin cannot be initialized, then the server will still continue starting up, but the plugin will be disabled.
    * `FORCE` - Enables the plugin. If the plugin cannot be initialized, then the server will fail to start with an error.
    * `FORCE_PLUS_PERMANENT` - Enables the plugin. If the plugin cannot be initialized, then the server will fail to start with an error. In addition, the plugin cannot be uninstalled with `[UNINSTALL SONAME](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-soname.md)` or `[UNINSTALL PLUGIN](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-plugin.md)` while the server is running.
  * See [Plugin Overview: Configuring Plugin Activation at Server Startup](../plugin-overview.md#configuring-plugin-activation-at-server-startup) for more information.
  * There may be ambiguity between this option and the `[named_pipe](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#named_pipe)` system variable. See [MDEV-19625](https://jira.mariadb.org/browse/MDEV-19625) about that.
* Commandline: `--named-pipe=value`
* Data Type: `enumerated`
* Default Value: `ON`
* Valid Values: `OFF`, `ON`, `FORCE`, `FORCE_PLUS_PERMANENT`
* Introduced: [MariaDB 10.1.11](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10111-release-notes)


