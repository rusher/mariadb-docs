# About the MariaDB RPM Files

## Available RPM Packages

The available RPM packages depend on the specific MariaDB release series.

### Available RPM Packages in MariaDB

The following RPMs are available in current versions of MariaDB:

| Package Name                       | Description                                                                                                                                                                                                  |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `galera-4`                         | The WSREP provider for Galera 4.                                                                                                                                                                             |
| `mariadb-backup`                   | `mariadb-backup` is a command-line utility for creating consistent and reliable backups of MariaDB databases, supporting full and incremental backup options.                                                |
| `mariadb-backup-debuginfo`         | Debuginfo for `mariadb-backup`                                                                                                                                                                               |
| `mariadb-client`                   | Client tools like mariadb CLI, `mariadb-dump`, and others.                                                                                                                                                   |
| `mariadb-client-compat`            | Symbolic links from old MySQL tool names to MariaDB, like `mysqladmin` -> `mariadb-admin` or `mysql` -> `mariadb`. Good to have if you are using MySQL tool names in your scripts.                           |
| `mariadb-client-debuginfo`         | Debuginfo for client tools like mariadb CLI, `mariadb-dump`, and others.                                                                                                                                     |
| `mariadb-common`                   | Character set files and `/etc/my.cnf`                                                                                                                                                                        |
| `mariadb-common-debuginfo`         | Debuginfo for character set files and `/etc/my.cnf`                                                                                                                                                          |
| `mariadb-compat`                   | Old shared client libraries, may be needed by old mariadb or mysql clients                                                                                                                                   |
| `mariadb-connect-engine`           | The CONNECT storage engine.                                                                                                                                                                                  |
| `mariadb-connect-engine-debuginfo` | Debuginfo for the CONNECT storage engine.                                                                                                                                                                    |
| `mariadb-cracklib-password-check`  | The `cracklib_password_check` password validation plugin.                                                                                                                                                    |
| `mariadb-cracklib-password-check`  | Debuginfo for the `cracklib_password_check` password validation plugin.                                                                                                                                      |
| `mariadb-devel`                    | Development headers and static libraries.                                                                                                                                                                    |
| `mariadb-devel-debuginfo`          | Debuginfo for development headers and static libraries.                                                                                                                                                      |
| `mariadb-gssapi-server`            | The gssapi authentication plugin.                                                                                                                                                                            |
| `mariadb-gssapi-server-debuginfo`  | Debuginfo for the gssapi authentication plugin.                                                                                                                                                              |
| `mariadb-rocksdb-engine`           | The MyRocks storage engine.                                                                                                                                                                                  |
| `mariadb-rocksdb-engine-debuginfo` | Debuginfo for the MyRocks storage engine.                                                                                                                                                                    |
| `mariadb-server`                   | The server and server tools, like `myisamchk` and `mariadb-hotcopy` are here.                                                                                                                                |
| `mariadb-server-compat`            | Symbolic links from old MySQL server executable names to MariaDB, like `mysqld` -> `mariadbd` or `mysql_install_db` -> `mariadb-install-db`. Good to have if you are using MySQL tool names in your scripts. |
| `mariadb-server-debuginfo`         | Debuginfo for the server and server tools, like `myisamchk` and `mariadb-hotcopy` are here.                                                                                                                  |
| `mariadb-shared`                   | Dynamic client libraries.                                                                                                                                                                                    |
| `mariadb-shared-debuginfo`         | Debuginfo for dynamic client libraries.                                                                                                                                                                      |
| `mariadb-test`                     | `mysql-client-test` executable, and mysql-test framework with the tests.                                                                                                                                     |
| `mariadb-test-debuginfo`           | Debuginfo for `mysql-client-test` executable, and `mysql-test` framework with the tests.                                                                                                                     |
| `mariadb-tokudb-engine`            | The TokuDB storage engine.                                                                                                                                                                                   |
| `mariadb-tokudb-engine-debuginfo`  | Debuginfo for the TokuDB storage engine.                                                                                                                                                                     |

## Installing RPM Packages

Preferably, you should install MariaDB RPM packages using the package manager\
of your Linux distribution, for example `yum` or`zypper`. But you can also use the lower-level `rpm` tool.

## Actions Performed by RPM Packages

### Users and Groups Created

When the `mariadb-server` RPM package is installed, it will create a user and group named `mysql`, if it does not already exist.

## See Also

* [Installing MariaDB with yum](yum.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
