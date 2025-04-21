
# USE CATALOG


##### MariaDB starting with [12.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/what-is-mariadb-120)
Catalog support is planned for 12.0.



## Syntax


```
USE CATALOG catalog_name
```

## Description


Changes to another [catalog](README.md).
Can only be done by a super user in the 'def' catalog.
Changing catalog will update catalog status and reset all session status.


A tenant (a user in any other catalog than 'def') cannot change to another catalog.
However tenants can execute `USE CATALOG current_catalog`. This is to allow the
user to import SQL scripts that use `USE CATALOG...`.


## See Also


* [USE database](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/use-database.md). Changing database.

