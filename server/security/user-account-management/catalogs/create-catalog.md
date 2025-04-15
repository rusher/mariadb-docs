
# CREATE CATALOG


##### MariaDB starting with [12.0](../../../../release-notes/mariadb-community-server/what-is-mariadb-120.md)
Catalog support is planned for 12.0.



## Syntax


```
CREATE CATALOG [IF NOT EXISTS] catalog_name
    [create_specification] ...

create_specification:
    [DEFAULT] CHARACTER SET [=] charset_name
  | [DEFAULT] COLLATE [=] collation_name
  | COMMENT [=] 'comment'
```

## Description


Creates a [catalog](catalogs-overview.md) and the `<code>mysql</code>`, `<code>sys</code>` and `<code>performance_schema</code>` schemas inside the catalog.


`<code>CREATE CATALOG</code>` can only be performed by a user in the `<code>def</code>` catalog with the CATALOG privilege.


Note that no users are created.


## Example


```
create catalog cat1;
use catalog cat1;
create user root@localhost;
grant all privileges on *.* to root@localhost;
create database test;
```

## Limitations


The catalog name is limited to 64 characters. All characters must be in the basic ASCII set:
(A-Z, a-z, -, _)
This limitations is to be able to run catalogs with engines like InnoDB which has limited
space in their internal data dictionary.


## Pre-Creating Catalog Directories


`<code>CREATE CATALOG</code>` works even if the catalog directory already exists (as long as there is no `<code>mysql</code>` sub directory). This is to allow a database administrator to pre-create the catalog directory and mount it to disk volume and optionally add a [configuration file](../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md) inside the catalog directory.
The directory will not be recognized as a catalog or show up in [SHOW CATALOGS](show-catalogs.md) until the `<code>mysql</code>` sub directory is created by [CREATE CATALOG](create-catalog.md) or [mariadb-install-db](../../../server-management/getting-installing-and-upgrading-mariadb/mariadb-install-db-exe.md).


## See Also


* [marriadb-install-db](../../../server-management/getting-installing-and-upgrading-mariadb/mariadb-install-db-exe.md) can be used to create multiple catalogs with a default root user in one go.
* [DROP CATALOG](drop-catalog.md)

