# Eperi Key Management Encryption Plugin

Eperi's Key Management Plugin Package no longer appears to be available.

MariaDB's [data-at-rest encryption](../data-at-rest-encryption-overview.md) requires the use of a [key management and encryption plugin](encryption-key-management.md). These plugins are responsible both for the management of encryption keys and for the actual encryption and decryption of data.

MariaDB supports the use of [multiple encryption keys](encryption-key-management.md#using-multiple-encryption-keys). Each encryption key uses a 32-bit integer as a key identifier. If the specific plugin supports [key rotation](encryption-key-management.md#rotating-keys), then encryption keys can also be rotated, which creates a new version of the encryption key.

The Eperi Key Management plugin is a [key management and encryption plugin](encryption-key-management.md) that integrates with [eperi Gateway for Databases](https://eperi.com/database-encryption/).

## Overview

The Eperi Key Management plugin is one of the [key management and encryption plugins](encryption-key-management.md) that can be set up for users who want to use [data-at-rest encryption](../data-at-rest-encryption-overview.md). Some of the plugin's primary features are:

* It reads encryption keys from [eperi Gateway for Databases](https://eperi.com/database-encryption/).
* It supports multiple encryption keys.
* It supports key rotation.
* It supports two different algorithms for encrypting data.

The [eperi Gateway for Databases](https://eperi.com/database-encryption/) stores encryption keys on the key server outside of the database server itself, which provides an extra level of security. The [eperi Gateway for Databases](https://eperi.com/database-encryption/) also supports performing all data encryption operations on the key server as well, but this is optional.

It also provides the following benefits:

* Key management outside the database
* No keys on database server hard disk
* Graphical user interface for configuration
* Encryption and decryption outside the database, supporting HSM's for maximum security.

Support for MariaDB is provided in [eperi Gateway for Databases 3.4](https://eperi.com/eperi-gateway-for-databases-version-3-4-offers-native-mariadb-support/).

## Installing the Eperi Key Management Plugin's Package

For information on how to install the package, see Eperi's documentation at the [Eperi Customer Portal](https://customer.eperi.de/index.jsp).

## Installing the Plugin

Even after the package that contains the plugin's shared library is installed on the operating system, the plugin is not actually installed by MariaDB by default. The plugin can be installed by providing the `[--plugin-load](../../../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md)` or the `[--plugin-load-add](../../../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md)` options. This can be specified as a command-line argument to `[mysqld](../../../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md)` or it can be specified in a relevant server [option group](../../../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md). For example:

```
[mariadb]
...
plugin_load_add = eperi_key_management_plugin
```

## Uninstalling the Plugin

Before you uninstall the plugin, you should ensure that [data-at-rest encryption](../data-at-rest-encryption-overview.md) is completely disabled, and that MariaDB no longer needs the plugin to decrypt tables or other files.

You can uninstall the plugin dynamically by executing `[UNINSTALL SONAME](../../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-soname.md)` or `[UNINSTALL PLUGIN](../../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-plugin.md)`. For example:

```sql
UNINSTALL SONAME 'eperi_key_management_plugin';
```

If you installed the plugin by providing the `[--plugin-load](../../../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md)` or the `[--plugin-load-add](../../../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md)` options in a relevant server [option group](../../../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md), then those options should be removed to prevent the plugin from being loaded the next time the server is restarted.

## Configuring the Eperi Key Management Plugin

For information on how to configure the plugin, see Eperi's documentation at the [Eperi Customer Portal](https://customer.eperi.de/index.jsp).

## Using the Eperi Key Management Plugin

Once the Eperi Key Management Plugin is enabled, you can use it by creating an encrypted table:

```sql
CREATE TABLE t (i int) ENGINE=InnoDB ENCRYPTED=YES
```

Now, table `t` will be encrypted using the encryption key from the key server.

For more information on how to use encryption, see [Data at Rest Encryption](../data-at-rest-encryption-overview.md).

## Using Multiple Encryption Keys

The Eperi Key Management Plugin supports [using multiple encryption keys](encryption-key-management.md#using-multiple-encryption-keys). Each encryption key can be defined with a different 32-bit integer as a key identifier.

When [encrypting InnoDB tables](../innodb-encryption/), the key that is used to encrypt tables [can be changed](../innodb-encryption/innodb-encryption-keys.md).

When [encrypting Aria tables](../aria-encryption/), the key that is used to encrypt tables [cannot currently be changed](../aria-encryption/aria-encryption-keys.md).

## Key Rotation

The Eperi Key Management plugin supports [key rotation](encryption-key-management.md#key-rotation).

## Versions

| Version | Status  | Introduced                                                                  |
| ------- | ------- | --------------------------------------------------------------------------- |
| Version | Status  | Introduced                                                                  |
| 1.0     | Unknown | [eperi Gateway for Databases](https://eperi.com/database-encryption/) 3.4.0 |

## System Variables

### `eperi_key_management_plugin_databaseId`

* Description: Determines the database ID which is processed in the eperi Gateway.
* Commandline: `--eperi-key-management-plugin-databaseid=value`
* Scope: Global
* Dynamic: No
* Data Type: `integer`
* Default Value: `1`

### `eperi_key_management_plugin_encryption_algorithm`

* Description: This system variable is used to determine which algorithm the plugin will use to encrypt data.
  * The recommended algorithm is `AES_CTR`, but this algorithm is only available when MariaDB is built with recent versions of [OpenSSL](https://www.openssl.org/). If the server is built with [wolfSSL](https://www.wolfssl.com/products/wolfssl/) or [yaSSL](https://www.wolfssl.com/products/yassl/), then this algorithm is not available. See [TLS and Cryptography Libraries Used by MariaDB](../../tls-and-cryptography-libraries-used-by-mariadb.md) for more information about which libraries are used on which platforms.
* Commandline: `--eperi-key-management-plugin-encryption-algorithm=value`
* Scope: Global
* Dynamic: No
* Data Type: `enumerated`
* Default Value: `AES_CBC`
* Valid Values: `AES_CBC`, `AES_CTR`

### `eperi_key_management_plugin_encryption_mode`

* Description: Encryption mode.
* Commandline: `--eperi-key-management-plugin-encryption-mode=value`
* Scope: Global
* Dynamic: No
* Data Type: `enumerated`
* Default Value: `database`
* Valid Values: `database`, `gateway`

### `eperi_key_management_plugin_osslmt`

* Description: Determines, whether the plugin should register callback functions for OpenSSL thread support.
* Commandline: `--eperi-key-management-plugin-osslmt=value`
* Scope: Global
* Dynamic: No
* Data Type: `boolean`
* Default Value: `0` (Linux), `1` (Windows)

### `eperi_key_management_plugin_port`

* Description: Listener port for plugin.
* Commandline: `--eperi-key-management-plugin-port=value`
* Scope: Global
* Dynamic: No
* Data Type: `integer`
* Default Value: `14332`

### `eperi_key_management_plugin_url`

* Description: URL to key server. The expected format of the URL is :. The port number is optional, and the port number defaults to 14333 if it is not specified.
* Commandline: `--eperi-key-management-plugin-url=value`
* Scope: Global
* Dynamic: No
* Data Type: `string`
* Default Value: `NULL`

### `eperi_key_management_plugin_url_check_disabled`

* Description: Determines, whether the connection between plugin and eperi Gateway is tested at server startup.
* Commandline: `--eperi-key-management-plugin-url-check-disabled=value`
* Scope: Global
* Dynamic: No
* Data Type: `boolean`
* Default Value: `1`

## Options

### `eperi_key_management_plugin`

* Description: Controls how the server should treat the plugin when the server starts up.
  * Valid values are:
    * `OFF` - Disables the plugin without removing it from the `[mysql.plugins](../../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/the-mysql-database-tables/mysql-plugin-table.md)` table.
    * `ON` - Enables the plugin. If the plugin cannot be initialized, then the server will still continue starting up, but the plugin will be disabled.
    * `FORCE` - Enables the plugin. If the plugin cannot be initialized, then the server will fail to start with an error.
    * `FORCE_PLUS_PERMANENT` - Enables the plugin. If the plugin cannot be initialized, then the server will fail to start with an error. In addition, the plugin cannot be uninstalled with `[UNINSTALL SONAME](../../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-soname.md)` or `[UNINSTALL PLUGIN](../../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-plugin.md)` while the server is running.
  * See [Plugin Overview: Configuring Plugin Activation at Server Startup](../../../../../reference/plugins/plugin-overview.md#configuring-plugin-activation-at-server-startup) for more information.
* Commandline: `--eperi-key-management-plugin=value`
* Data Type: `enumerated`
* Default Value: `ON`
* Valid Values: `OFF`, `ON`, `FORCE`, `FORCE_PLUS_PERMANENT`

## See Also

* [Database Encryption - eperi](https://eperi.com/database-encryption/)
* [eperi Gateway for Databases version 3.4 offers native MariaDB support](https://eperi.com/eperi-gateway-for-databases-version-3-4-offers-native-mariadb-support/)
* [eperi Customer Portal](https://customer.eperi.de/index.jsp)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
