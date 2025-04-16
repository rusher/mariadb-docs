
# USE CATALOG


##### MariaDB starting with [12.0](../../../../release-notes/mariadb-community-server/what-is-mariadb-120.md)
Catalog support is planned for 12.0.



## Syntax


```
USE CATALOG catalog_name
```

## Description


Changes to another [catalog](catalogs-overview.md).
Can only be done by a super user in the 'def' catalog.
Changing catalog will update catalog status and reset all session status.


A tenant (a user in any other catalog than 'def') cannot change to another catalog.
However tenants can execute `USE CATALOG current_catalog`. This is to allow the
user to import SQL scripts that use `USE CATALOG...`.


## See Also


* [USE database](../../../../general-resources/learning-and-training/training-and-tutorials/beginner-mariadb-articles/useful-mariadb-queries.md). Changing database.

