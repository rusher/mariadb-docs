# SHOW CREATE CATALOG

**MariaDB starting with** [**12.0**](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/what-is-mariadb-120)

Catalog support is planned for 12.0.

## Syntax

```bnf
SHOW CREATE CATALOG catalog_name
```

## Description

Shows the [CREATE CATALOG](create-catalog.md) statement that creates the given [catalog](./).

## Examples

```sql
SHOW CREATE CATALOG def;
+---------+-------------------------------------------------------------------------------------------------------+
| Catalog | Create Catalog                                                                                        |
+---------+-------------------------------------------------------------------------------------------------------+
| def     | CREATE CATALOG `def` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci COMMENT 'default catalog' |
+---------+-------------------------------------------------------------------------------------------------------+
```

## See Also

* [CREATE CATALOG](create-catalog.md)
* [Character Sets and Collations](../../../reference/data-types/string-data-types/character-sets/supported-character-sets-and-collations.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
