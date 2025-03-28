# Information Schema CATALOG Table

#

#### MariaDB starting with [12.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/what-is-mariadb-120)

Catalog support is planned for 12.0.

The [Information Schema](/kb/en/information_schema/) `CATALOG` table stores information about [catalogs](../../../../../../../security/user-account-management/catalogs/catalogs-overview.md) on the server.

It contains the following columns:

| Column | Description |
| --- | --- |
| Column | Description |
| CATALOG_NAME | Catalog name. |
| DEFAULT_CHARACTER_SET_NAME | Default [character set](/kb/en/data-types-character-sets-and-collations/) for the database. |
| DEFAULT_COLLATION_NAME | Default [collation](/kb/en/data-types-character-sets-and-collations/). |
| SCHEMA_COMMENT | Catalog comment |

#

# Example

```
MariaDB [def.test]> SELECT * FROM INFORMATION_SCHEMA.CATALOGS\G
*************************** 1. row ***************************
 CATALOG_NAME: c1
DEFAULT_CHARACTER_SET_NAME: latin1
 DEFAULT_COLLATION_NAME: latin1_swedish_ci
 CATALOG_COMMENT: This is catalog c1
*************************** 2. row ***************************
 CATALOG_NAME: cat2
DEFAULT_CHARACTER_SET_NAME: latin1
 DEFAULT_COLLATION_NAME: latin1_swedish_ci
 CATALOG_COMMENT: 
*************************** 3. row ***************************
 CATALOG_NAME: def
DEFAULT_CHARACTER_SET_NAME: latin1
 DEFAULT_COLLATION_NAME: latin1_swedish_ci
 CATALOG_COMMENT: default catalog
...
```

#

# See Also

* [SHOW CATALOGS](../../../../../../../security/user-account-management/catalogs/show-catalogs.md)
* [SHOW CREATE CATALOG](../../../../../../../security/user-account-management/catalogs/show-create-catalog.md)
* [CREATE CATALOG](../../../../../../../security/user-account-management/catalogs/create-catalog.md)
* [DROP CATALOG](../../../../../../../security/user-account-management/catalogs/drop-catalog.md)
* [Character Sets and Collations](/kb/en/character-sets-and-collations/)