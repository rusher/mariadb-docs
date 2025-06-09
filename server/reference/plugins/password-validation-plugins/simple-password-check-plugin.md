# Simple Password Check Plugin

`simple_password_check` is a [password validation](broken-reference) plugin. It can check whether a password contains at least a certain number of characters of a specific type. When first installed, a password is required to be at least eight characters, and requires at least one digit, one uppercase character, one lowercase character, and one character that is neither a digit nor a letter.

Note that passwords can be directly set as a hash, bypassing the password validation, if the [strict\_password\_validation](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#strict_password_validation) variable is `OFF` (it is `ON` by default).

## Installing the Plugin

Although the plugin's shared library is distributed with MariaDB by default, the plugin is not actually installed by MariaDB by default. There are two methods that can be used to install the plugin with MariaDB.

The first method can be used to install the plugin without restarting the server. You can install the plugin dynamically by executing `[INSTALL SONAME](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/install-soname.md)` or `[INSTALL PLUGIN](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/install-plugin.md)`. For example:

```
INSTALL SONAME 'simple_password_check';
```

The second method can be used to tell the server to load the plugin when it starts up. The plugin can be installed this way by providing the `[--plugin-load](../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md)` or the `[--plugin-load-add](../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md)` options. This can be specified as a command-line argument to `[mysqld](../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md)` or it can be specified in a relevant server [option group](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md). For example:

```
[mariadb]
...
plugin_load_add = simple_password_check
```

## Uninstalling the Plugin

You can uninstall the plugin dynamically by executing `[UNINSTALL SONAME](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-soname.md)` or `[UNINSTALL PLUGIN](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-plugin.md)`. For example:

```
UNINSTALL SONAME 'simple_password_check';
```

If you installed the plugin by providing the `[--plugin-load](../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md)` or the `[--plugin-load-add](../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md)` options in a relevant server [option group](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md), then those options should be removed to prevent the plugin from being loaded the next time the server is restarted.

## Example

When creating a new password, if the criteria are not met, the following error is returned:

```
SET PASSWORD FOR 'bob'@'%.loc.gov' = PASSWORD('abc');
ERROR 1819 (HY000): Your password does not satisfy the current policy requirements
```

## Known Issues

### Issues with PAM Authentication Plugin

Prior to [MariaDB 10.4.0](broken-reference), all [password validation plugins](./) are incompatible with the `[pam](../authentication-plugins/authentication-with-pluggable-authentication-modules-pam/authentication-plugin-pam.md)` authentication plugin. See [Authentication Plugin - PAM: Conflicts with Password Validation](../authentication-plugins/authentication-with-pluggable-authentication-modules-pam/authentication-plugin-pam.md#conflicts-with-password-validation) for more information.

## Versions

| Version | Status | Introduced                                                                                                                                                                          |
| ------- | ------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Version | Status | Introduced                                                                                                                                                                          |
| 1.0     | Stable | [MariaDB 10.1.18](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-1-series/mariadb-10118-release-notes) |
| 1.0     | Gamma  | [MariaDB 10.1.13](broken-reference)                                                                                                                                                 |
| 1.0     | Beta   | [MariaDB 10.1.11](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-1-series/mariadb-10111-release-notes) |
| 1.0     | Alpha  | [MariaDB 10.1.2](broken-reference)                                                                                                                                                  |

## System Variables

#### `simple_password_check_digits`

* Description: A password must contain at least this many digits.
* Commandline: `--simple-password-check-digits=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `1`
* Range: `0` to `1000`

#### `simple_password_check_letters_same_case`

* Description: A password must contain at least this many upper-case and this many lower-case letters.
* Commandline: `--simple-password-check-letters-same-case=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `1`
* Range: `0` to `1000`

#### `simple_password_check_minimal_length`

* Description: A password must contain at least this many characters.
* Commandline: `--simple-password-check-minimal-length=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `8`
* Range: `0` to `1000`

#### `simple_password_check_other_characters`

* Description: A password must contain at least this many characters that are neither digits nor letters.
* Commandline: `--simple-password-check-other-characters=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `1`
* Range: `0` to `1000`

## Options

#### `simple_password_check`

* Description: Controls how the server should treat the plugin when the server starts up.
  * Valid values are:
    * `OFF` - Disables the plugin without removing it from the `[mysql.plugins](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/the-mysql-database-tables/mysql-plugin-table.md)` table.
    * `ON` - Enables the plugin. If the plugin cannot be initialized, then the server will still continue starting up, but the plugin will be disabled.
    * `FORCE` - Enables the plugin. If the plugin cannot be initialized, then the server will fail to start with an error.
    * `FORCE_PLUS_PERMANENT` - Enables the plugin. If the plugin cannot be initialized, then the server will fail to start with an error. In addition, the plugin cannot be uninstalled with `[UNINSTALL SONAME](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-soname.md)` or `[UNINSTALL PLUGIN](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-plugin.md)` while the server is running.
  * See [Plugin Overview: Configuring Plugin Activation at Server Startup](../plugin-overview.md#configuring-plugin-activation-at-server-startup) for more information.
* Commandline: `--simple-password-check=value`
* Data Type: `enumerated`
* Default Value: `ON`
* Valid Values: `OFF`, `ON`, `FORCE`, `FORCE_PLUS_PERMANENT`

## See Also

* [Password Validation](broken-reference)
* [cracklib\_password\_check plugin](cracklib-password-check-plugin.md) - use the Cracklib password-strength checking library

CC BY-SA / Gnu FDL

{% @marketo/form formId="4316" %}
