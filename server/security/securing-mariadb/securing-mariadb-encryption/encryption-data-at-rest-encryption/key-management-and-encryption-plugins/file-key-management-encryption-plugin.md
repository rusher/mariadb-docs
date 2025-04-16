
# File Key Management Encryption Plugin


MariaDB's [data-at-rest encryption](../data-at-rest-encryption-overview.md) requires the use of a [key management and encryption plugin](encryption-key-management.md). These plugins are responsible both for the management of encryption keys and for the actual encryption and decryption of data.


MariaDB supports the use of [multiple encryption keys](encryption-key-management.md#using-multiple-encryption-keys). Each encryption key uses a 32-bit integer as a key identifier. If the specific plugin supports [key rotation](encryption-key-management.md#key-rotation), then encryption keys can also be rotated, which creates a new version of the encryption key.


The File Key Management plugin that ships with MariaDB is a [key management and encryption plugin](encryption-key-management.md) that reads encryption keys from a plain-text file.


## Overview


The File Key Management plugin is the easiest [key management and encryption plugin](encryption-key-management.md) to set up for users who want to use [data-at-rest encryption](../data-at-rest-encryption-overview.md). Some of the plugin's primary features are:


* It reads encryption keys from a plain-text key file.
* As an extra protection mechanism, the plain-text key file can be encrypted.
* It supports multiple encryption keys.
* It does not support key rotation.
* It supports two different algorithms for encrypting data.


It can also serve as an example and as a starting point when developing a key management and encryption plugin with the [encryption plugin API](../../../../../reference/mariadb-internals/encryption-plugin-api.md).


## Installing the File Key Management Plugin's Package


The File Key Management plugin is included in MariaDB packages as the `file_key_management.so` or `file_key_management.dll` shared library. The shared library is in the main server package, so no additional package installations are necessary. The plug-in must be installed into MariaDB however as follows.


## Installing the Plugin


Although the plugin's shared library is distributed with MariaDB by default, the plugin is not actually installed by MariaDB by default. The plugin can be installed by providing the `[--plugin-load](../../../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md)` or the `[--plugin-load-add](../../../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md)` options. This can be specified as a command-line argument to `[mysqld](../../../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md)` or it can be specified in a relevant server [option group](../../../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md). For example:


```
[mariadb]
...
plugin_load_add = file_key_management
```

## Uninstalling the Plugin


Before you uninstall the plugin, you should ensure that [data-at-rest encryption](../data-at-rest-encryption-overview.md) is completely disabled, and that MariaDB no longer needs the plugin to decrypt tables or other files.


You can uninstall the plugin dynamically by executing `[UNINSTALL SONAME](../../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-soname.md)` or `[UNINSTALL PLUGIN](../../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-plugin.md)`. For example:


```
UNINSTALL SONAME 'file_key_management';
```

If you installed the plugin by providing the `[--plugin-load](../../../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md)` or the `[--plugin-load-add](../../../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md)` options in a relevant server [option group](../../../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md), then those options should be removed to prevent the plugin from being loaded the next time the server is restarted.


## Creating the Key File


In order to encrypt your tables with encryption keys using the File Key Management plugin, you first need to create the file that contains the encryption keys. The file needs to contain two pieces of information for each encryption key. First, each encryption key needs to be identified with a 32-bit integer as the key identifier. Second, the encryption key itself needs to be provided in hex-encoded form. These two pieces of information need to be separated by a semicolon. For example, the file is formatted in the following way:


```
<encryption_key_id1>;<hex-encoded_encryption_key1>
<encryption_key_id2>;<hex-encoded_encryption_key2>
```

You can also optionally encrypt the key file to make it less accessible from the file system. That is explained further in the section below.


The File Key Management plugin uses [Advanced Encryption Standard (AES)](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard) to encrypt data, which supports 128-bit, 192-bit, and 256-bit encryption keys. Therefore, the plugin also supports 128-bit, 192-bit, and 256-bit encryption keys.


You can generate random encryption keys using the `[openssl rand](https://www.openssl.org/docs/man1.1.1/man1/rand.html)` command. For example, to create a random 256-bit (32-byte) encryption key, you would run the following command:


```
$ openssl rand -hex 32
a7addd9adea9978fda19f21e6be987880e68ac92632ca052e5bb42b1a506939a
```

The key file still needs to have a key identifier for each encryption key added to the beginning of each line. Key identifiers do not need to be contiguous.


For example, to append three new encryption keys to a new key file, you could execute the following:


```
$ (echo -n "1;" ; openssl rand -hex 32 ) | sudo tee -a  /etc/mysql/encryption/keyfile
$ (echo -n "2;" ; openssl rand -hex 32 ) | sudo tee -a  /etc/mysql/encryption/keyfile
$ (echo -n "100;" ; openssl rand -hex 32 ) | sudo tee -a  /etc/mysql/encryption/keyfile
```

The new key file would look something like the following after this step:


```
1;a7addd9adea9978fda19f21e6be987880e68ac92632ca052e5bb42b1a506939a
2;49c16acc2dffe616710c9ba9a10b94944a737de1beccb52dc1560abfdd67388b
100;8db1ee74580e7e93ab8cf157f02656d356c2f437d548d5bf16bf2a56932954a3
```

The key identifiers give you a way to reference the encryption keys from MariaDB. In the example above, you could reference these encryption keys using the key identifiers `1`, `2` or `100` with the `[ENCRYPTION_KEY_ID](../../../../../reference/sql-statements-and-structure/vectors/create-table-with-vectors.md#encryption_key_id)` table option or with system variables such as `[innodb_default_encryption_key_id](../../../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_default_encryption_key_id)`. You do not necessarily need multiple encryption keys--the encryption key with the key identifier `1` is the only mandatory encryption key.


### Configuring the Path to an Unencrypted Key File


If the key file is unencrypted, then the File Key Management plugin only requires the `[file_key_management_filename](#file_key_management_filename)` system variable to be configured.


This system variable can be specified as command-line arguments to `[mysqld](../../../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md)` or it can be specified in a relevant server [option group](../../../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md). For example:


```
[mariadb]
...
loose_file_key_management_filename = /etc/mysql/encryption/keyfile
```

Note that the `[loose](../../../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md)` option prefix is specified. This option prefix is used in case the plugin hasn't been installed yet.


## Encrypting the Key File


By enabling the File Key Management plugin and setting the appropriate path on the `[file_key_management_filename](#file_key_management_filename)` system variable, you can begin using the plugin to manage your encryption keys. But, there is a security risk in doing so, given that the keys are stored in plain text on your system. You can reduce this exposure using file permissions, but it's better to encrypt the whole key file to further restrict access.


There are some important details to keep in mind about encrypting the key file, such as:


* The only algorithm that MariaDB currently supports to encrypt the key file is [Cipher Block Chaining (CBC)](https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation#CBC) mode of [Advanced Encryption Standard (AES)](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard).
* The encryption key size can be 128-bits, 192-bits, or 256-bits.
* The encryption key is created from the [SHA-1](https://en.wikipedia.org/wiki/SHA-1) hash of the encryption password.
* The encryption password has a max length of 256 characters.


You can generate a random encryption password using the `[openssl rand](https://www.openssl.org/docs/man1.1.1/man1/rand.html)` command. For example, to create a random 256 character encryption password, you could execute the following:


```
$ sudo openssl rand -hex 128 > /etc/mysql/encryption/keyfile.key
```

You can encrypt the key file using the `[openssl enc](https://www.openssl.org/docs/man1.1.1/man1/enc.html)` command. For example, to encrypt the key file with the encryption password created in the previous step, you could execute the following:


```
$ sudo openssl enc -aes-256-cbc -md sha1 \
   -pass file:/etc/mysql/encryption/keyfile.key \
   -in /etc/mysql/encryption/keyfile \
   -out /etc/mysql/encryption/keyfile.enc
```

**Note:** some more recent `openssl` versions may complain with

```
*** WARNING : deprecated key derivation used.
Using -iter or -pbkdf2 would be better.
```

Keys generated that way won't work with the current implementation of the plugin though. Also as SHA1 is only used to generate the actual AES encryption key, from a long random string, it's not really an issue here. SHA1 deprecation is mostly related to checksum / signing use cases, not to what we are using it here for. 


Running this command reads the unencrypted `keyfile` file created above and creates a new encrypted `keyfile.enc` file, using the encryption password stored in `keyfile.key`. Once you've finished preparing your system, you can delete the unencrypted `keyfile` file, as it's no longer necessary.


### Configuring the Path to an Encrypted Key File


If the key file is encrypted, then the File Key Management plugin requires both the `[file_key_management_filename](#file_key_management_filename)` and the `[file_key_management_filekey](#file_key_management_filekey)` system variables to be configured.


The `[file_key_management_filekey](#file_key_management_filekey)` system variable can be provided in two forms:


* It can be the actual plain-text encryption password. This is not recommended, since the plain-text encryption password would be visible in the output of the `[SHOW VARIABLES](../../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-variables.md)` statement.
* If it is prefixed with `FILE:`, then it can be a path to a file that contains the plain-text encryption password.


These system variables can be specified as command-line arguments to `[mysqld](../../../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md)` or they can be specified in a relevant server [option group](../../../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md). For example:


```
[mariadb]
...
loose_file_key_management_filename = /etc/mysql/encryption/keyfile.enc
loose_file_key_management_filekey = FILE:/etc/mysql/encryption/keyfile.key
```

Note that the `[loose](../../../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md)` option prefix is specified. This option prefix is used in case the plugin hasn't been installed yet.


## Choosing an Encryption Algorithm


The File Key Management plugin currently supports two encryption algorithms for encrypting data: `AES_CBC` and `AES_CTR`. Both of these algorithms use [Advanced Encryption Standard (AES)](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard) in different modes. AES uses 128-bit blocks, and supports 128-bit, 192-bit, and 256-bit keys. The modes are:


* The `AES_CBC` mode uses AES in the [Cipher Block Chaining (CBC)](https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation#Cipher_Block_Chaining_.28CBC.29) mode.
* The `AES_CTR` mode uses AES in two slightly different modes in different contexts. When encrypting tablespace pages (such as pages in InnoDB, XtraDB, and Aria tables), it uses AES in the 
[Counter (CTR)](https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation#Counter_.28CTR.29) mode. When encrypting temporary files (where the cipher text is allowed to be larger than the plain text), it uses AES in the authenticated [Galois/Counter Mode (GCM)](https://en.wikipedia.org/wiki/Galois/Counter_Mode).


The recommended algorithm is `AES_CTR`, but this algorithm is only available when MariaDB is built with recent versions of [OpenSSL](https://www.openssl.org/). If the server is built with [wolfSSL](https://www.wolfssl.com/products/wolfssl/) or [yaSSL](https://www.wolfssl.com/products/yassl/), then this algorithm is not available. See [TLS and Cryptography Libraries Used by MariaDB](../../tls-and-cryptography-libraries-used-by-mariadb.md) for more information about which libraries are used on which platforms.


### Configuring the Encryption Algorithm


The encryption algorithm can be configured by setting the `[file_key_management_encryption_algorithm](#file_key_management_encryption_algorithm)` system variable.


This system variable can be set to one of the following values:



| System Variable Value | Description |
| --- | --- |
| System Variable Value | Description |
| AES_CBC | Data is encrypted using AES in the [Cipher Block Chaining (CBC)](https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation#Cipher_Block_Chaining_.28CBC.29) mode. This is the default value. |
| AES_CTR | Data is encrypted using AES either in the [Counter (CTR)](https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation#Counter_.28CTR.29) mode or in the authenticated [Galois/Counter Mode (GCM)](https://en.wikipedia.org/wiki/Galois/Counter_Mode) mode, depending on context. This is only supported in some builds. See the previous section for more information. |



This system variable can be specified as command-line arguments to `[mysqld](../../../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md)` or it can be specified in a relevant server [option group](../../../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md). For example:


```
[mariadb]
...
loose_file_key_management_encryption_algorithm = AES_CTR
```

Note that the `[loose](../../../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md)` option prefix is specified. This option prefix is used in case the plugin hasn't been installed yet.


Note that this variable does not affect the algorithm that MariaDB uses to decrypt the key file. This variable only affects the encryption algorithm that MariaDB uses to encrypt and decrypt data. The only algorithm that MariaDB currently supports to encrypt the key file is [Cipher Block Chaining (CBC)](https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation#CBC) mode of [Advanced Encryption Standard (AES)](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard).


## Using the File Key Management Plugin


Once the File Key Management Plugin is enabled, you can use it by creating an encrypted table:


```
CREATE TABLE t (i int) ENGINE=InnoDB ENCRYPTED=YES
```

Now, table `t` will be encrypted using the encryption key from the key file.


For more information on how to use encryption, see [Data at Rest Encryption](../data-at-rest-encryption-overview.md).


## Using Multiple Encryption Keys


The File Key Management Plugin supports [using multiple encryption keys](encryption-key-management.md#using-multiple-encryption-keys). Each encryption key can be defined with a different 32-bit integer as a key identifier.


When [encrypting InnoDB tables](../innodb-encryption/innodb-encryption-troubleshooting.md), the key that is used to encrypt tables [can be changed](../innodb-encryption/innodb-encryption-keys.md).


When [encrypting Aria tables](../aria-encryption/aria-encryption-overview.md), the key that is used to encrypt tables [cannot currently be changed](../aria-encryption/aria-encryption-keys.md).


## Key Rotation


The File Key Management plugin does not currently support [key rotation](encryption-key-management.md#key-rotation). See [MDEV-20713](https://jira.mariadb.org/browse/MDEV-20713) for more information.


## Versions



| Version | Status | Introduced |
| --- | --- | --- |
| Version | Status | Introduced |
| 1.0 | Stable | [MariaDB 10.1.18](../../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10118-release-notes.md) |
| 1.0 | Gamma | [MariaDB 10.1.13](../../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10113-release-notes.md) |
| 1.0 | Alpha | [MariaDB 10.1.3](../../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-3-release-notes.md) |



## System Variables


### `file_key_management_encryption_algorithm`


* Description: This system variable is used to determine which algorithm the plugin will use to encrypt data.

  * The recommended algorithm is `AES_CTR`, but this algorithm is only available when MariaDB is built with recent versions of [OpenSSL](https://www.openssl.org/). If the server is built with [wolfSSL](https://www.wolfssl.com/products/wolfssl/) or [yaSSL](https://www.wolfssl.com/products/yassl/), then this algorithm is not available. See [TLS and Cryptography Libraries Used by MariaDB](../../tls-and-cryptography-libraries-used-by-mariadb.md) for more information about which libraries are used on which platforms.
* Commandline: `--file-key-management-encryption-algorithm=value`
* Scope: Global
* Dynamic: No
* Data Type: `enumerated`
* Default Value: `AES_CBC`
* Valid Values: `AES_CBC`, `AES_CTR`



### `file_key_management_filekey`


* Description: This system variable is used to determine the encryption password that is used to decrypt the key file defined by `[file_key_management_filename](#file_key_management_filename)`.

  * If this system variable's value is prefixed with `FILE:`, then it is interpreted as a path to a file that contains the plain-text encryption password.
  * If this system variable's value is not prefixed with `FILE:`, then it is interpreted as the plain-text encryption password. However, this is not recommended.
  * The encryption password has a max length of 256 characters.
  * The only algorithm that MariaDB currently supports when decrypting the key file is [Cipher Block Chaining (CBC)](https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation#CBC) mode of [Advanced Encryption Standard (AES)](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard). The encryption key size can be 128-bits, 192-bits, or 256-bits. The encryption key is calculated by taking a [SHA-1](https://en.wikipedia.org/wiki/SHA-1) hash of the encryption password.
* Commandline: `--file-key-management-filekey=value`
* Scope: Global
* Dynamic: No
* Data Type: `string`
* Default Value: (empty)



### `file_key_management_filename`


* Description: This system variable is used to determine the path to the file that contains the encryption keys. If `[file_key_management_filekey](#file_key_management_filekey)` is set, then this file can be encrypted with [Cipher Block Chaining (CBC)](https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation#CBC) mode of [Advanced Encryption Standard (AES)](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard).
* Commandline: `--file-key-management-filename=value`
* Scope: Global
* Dynamic: No
* Data Type: `string`
* Default Value: (empty)



## Options


### `file_key_management`


* Description: Controls how the server should treat the plugin when the server starts up.

  * Valid values are:

    * `OFF` - Disables the plugin without removing it from the `[mysql.plugins](../../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/the-mysql-database-tables/mysql-plugin-table.md)` table.
    * `ON` - Enables the plugin. If the plugin cannot be initialized, then the server will still continue starting up, but the plugin will be disabled.
    * `FORCE` - Enables the plugin. If the plugin cannot be initialized, then the server will fail to start with an error.
    * `FORCE_PLUS_PERMANENT` - Enables the plugin. If the plugin cannot be initialized, then the server will fail to start with an error. In addition, the plugin cannot be uninstalled with `[UNINSTALL SONAME](../../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-soname.md)` or `[UNINSTALL PLUGIN](../../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-plugin.md)` while the server is running.
  * See [Plugin Overview: Configuring Plugin Activation at Server Startup](../../../../../reference/plugins/plugin-overview.md#configuring-plugin-activation-at-server-startup) for more information.
* Commandline: `--file-key-management=value`
* Data Type: `enumerated`
* Default Value: `ON`
* Valid Values: `OFF`, `ON`, `FORCE`, `FORCE_PLUS_PERMANENT`


