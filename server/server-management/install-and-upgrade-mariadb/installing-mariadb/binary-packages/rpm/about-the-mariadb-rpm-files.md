# About the MariaDB RPM Files

## Available RPM Packages

The available RPM packages depend on the specific MariaDB release series.

### Available RPM Packages in MariaDB

The following RPMs are available in current versions of MariaDB:

| Package Name                     | Description                                                                                                                                                                                                                                                            |
| -------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Package Name                     | Description                                                                                                                                                                                                                                                            |
| galera-4                         | The WSREP provider for [Galera](https://github.com/mariadb-corporation/docs-server/blob/test/kb/en/galera/README.md) 4.                                                                                                                                                |
| MariaDB-backup                   | [Mariabackup](../../../../../server-usage/backing-up-and-restoring-databases/mariabackup/)                                                                                                                                                                             |
| MariaDB-backup-debuginfo         | Debuginfo for [Mariabackup](../../../../../server-usage/backing-up-and-restoring-databases/mariabackup/)                                                                                                                                                               |
| MariaDB-client                   | Client tools like [mariadb CLI](../../../../../clients-and-utilities/mariadb-client/), [mariadb-dump](../../../../../clients-and-utilities/backup-restore-and-import-clients/mariadb-dump.md), and others.                                                             |
| MariaDB-client-debuginfo         | Debuginfo for client tools like mariadb CLI, mariadb-dump, and others.                                                                                                                                                                                                 |
| MariaDB-common                   | Character set files and /etc/my.cnf                                                                                                                                                                                                                                    |
| MariaDB-common-debuginfo         | Debuginfo for character set files and /etc/my.cnf                                                                                                                                                                                                                      |
| MariaDB-compat                   | Old shared client libraries, may be needed by old MariaDB or MySQL clients                                                                                                                                                                                             |
| MariaDB-connect-engine           | The [CONNECT](../../../../../server-usage/storage-engines/connect/) storage engine.                                                                                                                                                                                    |
| MariaDB-connect-engine-debuginfo | Debuginfo for the [CONNECT](../../../../../server-usage/storage-engines/connect/) storage engine.                                                                                                                                                                      |
| MariaDB-cracklib-password-check  | The [cracklib\_password\_check](../../../../../reference/plugins/password-validation-plugins/cracklib-password-check-plugin.md) password validation plugin.                                                                                                            |
| MariaDB-cracklib-password-check  | Debuginfo for the [cracklib\_password\_check](../../../../../reference/plugins/password-validation-plugins/cracklib-password-check-plugin.md) password validation plugin.                                                                                              |
| MariaDB-devel                    | Development headers and static libraries.                                                                                                                                                                                                                              |
| MariaDB-devel-debuginfo          | Debuginfo for development headers and static libraries.                                                                                                                                                                                                                |
| MariaDB-gssapi-server            | The [gssapi](../../../../../reference/plugins/authentication-plugins/authentication-plugin-gssapi.md) authentication plugin.                                                                                                                                           |
| MariaDB-gssapi-server-debuginfo  | Debuginfo for the [gssapi](../../../../../reference/plugins/authentication-plugins/authentication-plugin-gssapi.md) authentication plugin.                                                                                                                             |
| MariaDB-rocksdb-engine           | The [MyRocks](../../../../../server-usage/storage-engines/myrocks/) storage engine.                                                                                                                                                                                    |
| MariaDB-rocksdb-engine-debuginfo | Debuginfo for the [MyRocks](../../../../../server-usage/storage-engines/myrocks/) storage engine.                                                                                                                                                                      |
| MariaDB-server                   | The server and server tools, like [myisamchk](../../../../../clients-and-utilities/myisam-clients-and-utilities/myisamchk.md) and [mariadb-hotcopy](../../../../../clients-and-utilities/backup-restore-and-import-clients/mariadb-hotcopy.md) are here.               |
| MariaDB-server-compat            | Symbolic links from old MySQL tool names to MariaDB, like mysqladmin -> mariadb-admin or mysql -> mariadb. Good to have if you are using MySQL tool names in your scripts.                                                                                             |
| MariaDB-server-debuginfo         | Debuginfo for the server and server tools, like [myisamchk](../../../../../clients-and-utilities/myisam-clients-and-utilities/myisamchk.md) and [mariadb-hotcopy](../../../../../clients-and-utilities/backup-restore-and-import-clients/mariadb-hotcopy.md) are here. |
| MariaDB-shared                   | Dynamic client libraries.                                                                                                                                                                                                                                              |
| MariaDB-shared-debuginfo         | Debuginfo for dynamic client libraries.                                                                                                                                                                                                                                |
| MariaDB-test                     | mysql-client-test executable, and mysql-test framework with the tests.                                                                                                                                                                                                 |
| MariaDB-test-debuginfo           | Debuginfo for mysql-client-test executable, and mysql-test framework with the tests.                                                                                                                                                                                   |
| MariaDB-tokudb-engine            | The [TokuDB](../../../../../server-usage/storage-engines/tokudb/) storage engine.                                                                                                                                                                                      |
| MariaDB-tokudb-engine-debuginfo  | Debuginfo for the [TokuDB](../../../../../server-usage/storage-engines/tokudb/) storage engine.                                                                                                                                                                        |

## Installing RPM Packages

Preferably, you should install MariaDB RPM packages using the package manager\
of your Linux distribution, for example **`yum`** o&#x72;**`zypper`**. But you can also use the lower-leve&#x6C;**`rpm`** tool.

## Actions Performed by RPM Packages

### Users and Groups Created

When the `MariaDB-server` RPM package is installed, it will create a user and group named `mysql`, if it does not already exist.

## See Also

* [Installing MariaDB with yum](yum.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
