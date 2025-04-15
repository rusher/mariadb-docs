
# Simple Password Check Plugin

`<code>simple_password_check</code>` is a [password validation](README.md) plugin. It can check whether a password contains at least a certain number of characters of a specific type. When first installed, a password is required to be at least eight characters, and requires at least one digit, one uppercase character, one lowercase character, and one character that is neither a digit nor a letter.


Note that passwords can be directly set as a hash, bypassing the password validation, if the [strict_password_validation](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#strict_password_validation) variable is `<code>OFF</code>` (it is `<code>ON</code>` by default).



## Installing the Plugin


Although the plugin's shared library is distributed with MariaDB by default, the plugin is not actually installed by MariaDB by default. There are two methods that can be used to install the plugin with MariaDB.


The first method can be used to install the plugin without restarting the server. You can install the plugin dynamically by executing `<code>[INSTALL SONAME](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/install-soname.md)</code>` or `<code>[INSTALL PLUGIN](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/install-plugin.md)</code>`. For example:


```
INSTALL SONAME 'simple_password_check';
```

The second method can be used to tell the server to load the plugin when it starts up. The plugin can be installed this way by providing the `<code>[--plugin-load](../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md)</code>` or the `<code>[--plugin-load-add](../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md)</code>` options. This can be specified as a command-line argument to `<code>[mysqld](../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md)</code>` or it can be specified in a relevant server [option group](../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md). For example:


```
[mariadb]
...
plugin_load_add = simple_password_check
```

## Uninstalling the Plugin


You can uninstall the plugin dynamically by executing `<code>[UNINSTALL SONAME](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-soname.md)</code>` or `<code>[UNINSTALL PLUGIN](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-plugin.md)</code>`. For example:


```
UNINSTALL SONAME 'simple_password_check';
```

If you installed the plugin by providing the `<code>[--plugin-load](../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md)</code>` or the `<code>[--plugin-load-add](../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md)</code>` options in a relevant server [option group](../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md), then those options should be removed to prevent the plugin from being loaded the next time the server is restarted.


## Example


When creating a new password, if the criteria are not met, the following error is returned:


```
SET PASSWORD FOR 'bob'@'%.loc.gov' = PASSWORD('abc');
ERROR 1819 (HY000): Your password does not satisfy the current policy requirements
```

## Known Issues


### Issues with PAM Authentication Plugin


Prior to [MariaDB 10.4.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-4-series/mariadb-1040-release-notes.md), all [password validation plugins](README.md) are incompatible with the `<code>[pam](../authentication-plugins/authentication-with-pluggable-authentication-modules-pam/authentication-plugin-pam.md)</code>` authentication plugin. See [Authentication Plugin - PAM: Conflicts with Password Validation](../authentication-plugins/authentication-with-pluggable-authentication-modules-pam/authentication-plugin-pam.md#conflicts-with-password-validation) for more information.


## Versions



| Version | Status | Introduced |
| --- | --- | --- |
| Version | Status | Introduced |
| 1.0 | Stable | [MariaDB 10.1.18](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10118-release-notes.md) |
| 1.0 | Gamma | [MariaDB 10.1.13](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10113-release-notes.md) |
| 1.0 | Beta | [MariaDB 10.1.11](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10111-release-notes.md) |
| 1.0 | Alpha | [MariaDB 10.1.2](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-2-release-notes.md) |



## System Variables


#### `<code>simple_password_check_digits</code>`


* Description: A password must contain at least this many digits.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--simple-password-check-digits=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>1</code>`
* Range: `<code>0</code>` to `<code>1000</code>`



#### `<code>simple_password_check_letters_same_case</code>`


* Description: A password must contain at least this many upper-case and this many lower-case letters.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--simple-password-check-letters-same-case=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>1</code>`
* Range: `<code>0</code>` to `<code>1000</code>`



#### `<code>simple_password_check_minimal_length</code>`


* Description: A password must contain at least this many characters.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--simple-password-check-minimal-length=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>8</code>`
* Range: `<code>0</code>` to `<code>1000</code>`



#### `<code>simple_password_check_other_characters</code>`


* Description: A password must contain at least this many characters that are neither digits nor letters.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--simple-password-check-other-characters=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>1</code>`
* Range: `<code>0</code>` to `<code>1000</code>`



## Options


#### `<code>simple_password_check</code>`


* Description: Controls how the server should treat the plugin when the server starts up.

  * Valid values are:

    * `<code>OFF</code>` - Disables the plugin without removing it from the `<code>[mysql.plugins](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/the-mysql-database-tables/mysql-plugin-table.md)</code>` table.
    * `<code>ON</code>` - Enables the plugin. If the plugin cannot be initialized, then the server will still continue starting up, but the plugin will be disabled.
    * `<code>FORCE</code>` - Enables the plugin. If the plugin cannot be initialized, then the server will fail to start with an error.
    * `<code>FORCE_PLUS_PERMANENT</code>` - Enables the plugin. If the plugin cannot be initialized, then the server will fail to start with an error. In addition, the plugin cannot be uninstalled with `<code>[UNINSTALL SONAME](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-soname.md)</code>` or `<code>[UNINSTALL PLUGIN](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-plugin.md)</code>` while the server is running.
  * See [Plugin Overview: Configuring Plugin Activation at Server Startup](../plugin-overview.md#configuring-plugin-activation-at-server-startup) for more information.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--simple-password-check=value</code>`
* Data Type: `<code>enumerated</code>`
* Default Value: `<code>ON</code>`
* Valid Values: `<code>OFF</code>`, `<code>ON</code>`, `<code>FORCE</code>`, `<code>FORCE_PLUS_PERMANENT</code>`



## See Also


* [Password Validation](README.md)
* [cracklib_password_check plugin](cracklib-password-check-plugin.md) - use the Cracklib password-strength checking library

