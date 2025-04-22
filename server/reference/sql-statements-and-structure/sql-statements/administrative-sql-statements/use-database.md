
# USE [DATABASE]

## Syntax


```
USE db_name
```

From [MariaDB 11.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-11-7-rolling-releases/what-is-mariadb-117), one can also use

```
USE DATABASE db_name;
```


## Description


The `'USE db_name'` statement tells MariaDB to use the
`db_name` database as the default (current) database for
subsequent statements. The database remains the default until the end of the
session or another `USE` statement is issued:


```
USE db1;
SELECT COUNT(*) FROM mytable;   # selects from db1.mytable
USE db2;
SELECT COUNT(*) FROM mytable;   # selects from db2.mytable
```

The [DATABASE()](../built-in-functions/secondary-functions/information-functions/database.md) function ([SCHEMA()](../built-in-functions/secondary-functions/information-functions/schema.md) is a synonym) returns the default database.


Another way to set the default database is specifying its name at [mariadb](../../../../clients-and-utilities/mariadb-client/mariadb-command-line-client.md) command line client startup.


One cannot use `USE DATABASE` to a database one has no privileges to. The reason is that
a user with no privileges to a database should not be able to know if a database exists or not.


## See Also


* [Identifier Qualifiers](../../sql-language-structure/identifier-qualifiers.md)
* [USE CATALOG](../../../../security/user-account-management/catalogs/use-catalog.md)

