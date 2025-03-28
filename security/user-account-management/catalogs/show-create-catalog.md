# SHOW CREATE CATALOG

#

#### MariaDB starting with [12.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/what-is-mariadb-120)

Catalog support is planned for 12.0.

#

# Syntax

```
SHOW CREATE CATALOG catalog_name
```

#

# Description

Shows the [CREATE CATALOG](create-catalog.md) statement that creates the given [catalog](catalogs-overview.md).

#

# Examples

```
SHOW CREATE CATALOG def;
+---------+-------------------------------------------------------------------------------------------------------+
| Catalog | Create Catalog |
+---------+-------------------------------------------------------------------------------------------------------+
| def | CREATE CATALOG `def` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci COMMENT 'default catalog' |
+---------+-------------------------------------------------------------------------------------------------------+
```

#

# See Also

* [CREATE CATALOG](create-catalog.md)
* [Character Sets and Collations](/en/character-sets-and-collations/)