# Installing System Tables (mariadb-install-db)

`mariadb-install-db` initializes the MariaDB data directory and creates the
[system tables](/kb/en/system-tables/) in the [mysql](/kb/en/the-mysql-database-tables/) database, if they do not exist. MariaDB uses these tables to manage [privileges](../../reference/sql-statements-and-structure/sql-statements/account-management-sql-commands/grant.md#privilege-levels), [roles](../../security/user-account-management/roles/roles_overview.md), and [plugins](../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/plugins-table-information-schema.md). It also uses them to provide the data for the [help](../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/help-command.md) command in the [mariadb](../../clients-and-utilities/mariadb-client/mariadb-command-line-client.md) client.

[mariadb-install-db](../../clients-and-utilities/mariadb-install-db.md) works by starting MariaDB Server's `mysqld` process in [--bootstrap](/kb/en/mysqld-options/#-bootstrap) mode and sending commands to create the [system tables](/kb/en/system-tables/) and their content.

There is a version specifically for Windows, [mysql_install_db.exe](/kb/en/mysql_install_dbexe/).

To invoke `mariadb-install-db`, use the following syntax:

```
mariadb-install-db --user=mysql
```

For the options supported by [mariadb-install-db](../../clients-and-utilities/mariadb-install-db.md), see [mariadb-install-db: Options](../../clients-and-utilities/mariadb-install-db.md#options).

For the option groups read by [mariadb-install-db](../../clients-and-utilities/mariadb-install-db.md), see [mariadb-install-db: Option Groups](../../clients-and-utilities/mariadb-install-db.md#option-groups).

See [mariadb-install-db: Installing System Tables](../../clients-and-utilities/mariadb-install-db.md#installing-system-tables) for information on the installation process.

See [mariadb-install-db: Troubleshooting Issues](../../clients-and-utilities/mariadb-install-db.md#troubleshooting-issues) for information on how to troubleshoot the installation process.

#

# See Also

* [mariadb-install-db](../../clients-and-utilities/mariadb-install-db.md)
* The Windows version of `mariadb-install-db`: [mysql_install_db.exe](/kb/en/mysql_install_dbexe/)