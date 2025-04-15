
# Installing System Tables (mariadb-install-db)

`<code>mariadb-install-db</code>` initializes the MariaDB data directory and creates the
[system tables](../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/README.md) in the [mysql](../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/the-mysql-database-tables/README.md) database, if they do not exist. MariaDB uses these tables to manage [privileges](../../reference/sql-statements-and-structure/sql-statements/account-management-sql-commands/grant.md#privilege-levels), [roles](../../security/user-account-management/roles/roles_overview.md), and [plugins](../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/general-development-information/development-plans/old-plans/plugins-storage-engines-summit-for-mysqlmariadbdrizzle-2011.md). It also uses them to provide the data for the [help](../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/help-command.md) command in the [mariadb](../../clients-and-utilities/mariadb-client/mariadb-command-line-client.md) client.


[mariadb-install-db](mariadb-install-db-exe.md) works by starting MariaDB Server's `<code>mysqld</code>` process in [--bootstrap](starting-and-stopping-mariadb/mariadbd-options.md) mode and sending commands to create the [system tables](../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/README.md) and their content.


There is a version specifically for Windows, [mysql_install_db.exe](mariadb-install-db-exe.md).


To invoke `<code>mariadb-install-db</code>`, use the following syntax:


```
mariadb-install-db --user=mysql
```

For the options supported by [mariadb-install-db](mariadb-install-db-exe.md), see [mariadb-install-db: Options](mariadb-install-db-exe.md#options).


For the option groups read by [mariadb-install-db](mariadb-install-db-exe.md), see [mariadb-install-db: Option Groups](mariadb-install-db-exe.md#option-groups).


See [mariadb-install-db: Installing System Tables](mariadb-install-db-exe.md#installing-system-tables) for information on the installation process.


See [mariadb-install-db: Troubleshooting Issues](mariadb-install-db-exe.md#troubleshooting-issues) for information on how to troubleshoot the installation process.


## See Also


* [mariadb-install-db](mariadb-install-db-exe.md)
* The Windows version of `<code>mariadb-install-db</code>`: [mysql_install_db.exe](mariadb-install-db-exe.md)

