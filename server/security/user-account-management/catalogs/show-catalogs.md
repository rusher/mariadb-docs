
# SHOW CATALOGS


##### MariaDB starting with [12.0](../../../../release-notes/mariadb-community-server/what-is-mariadb-120.md)
Catalog support is planned for 12.0.



## Syntax


```
SHOW CATALOGS
    [LIKE 'pattern' | WHERE expr]
```


## Description


`<code class="highlight fixed" style="white-space:pre-wrap">SHOW CATALOGS</code>` lists the [catalogs](catalogs-overview.md) on the MariaDB server host.
The `<code class="highlight fixed" style="white-space:pre-wrap">LIKE</code>` clause, if present on its own, indicates which catalog names to match. The `<code class="highlight fixed" style="white-space:pre-wrap">WHERE</code>` and `<code class="highlight fixed" style="white-space:pre-wrap">LIKE</code>` clauses can be given to select rows using more general conditions, as discussed in [Extended SHOW](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/show/extended-show.md).


You see only use `<code class="highlight fixed" style="white-space:pre-wrap">SHOW CATALOGS</code>` have the [CATALOG privilege](../../../reference/sql-statements-and-structure/sql-statements/account-management-sql-commands/grant.md). Only users of the 'def' schema can have this privilege.


If the server was started with the [--skip-show-database](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#skip_show_database) option, you cannot use this statement unless you have the [SHOW DATABASES privilege](../../../reference/sql-statements-and-structure/sql-statements/account-management-sql-commands/grant.md#show-databases).


The list of results returned by `<code>SHOW CATALOGS</code>` is based on directories in the data directory, which is how MariaDB implements catalogs. It only list directories that have a `<code>mysql</code>` directory.


The [Information Schema Catalogs table](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-catalog-table.md) also contains catalog information.


## Examples


```
+---------+--------------------+
| Catalog | Comment            |
+---------+--------------------+
| c1      | This is catalog c1 |
| cat2    |                    |
| def     | default catalog    |
+---------+--------------------+
```

```
SHOW CATALOGS LIKE 'c%';
+--------------+--------------------+
| Catalog (c%) | Comment            |
+--------------+--------------------+
| c1           | This is catalog c1 |
| cat2         |                    |
+--------------+--------------------+
```

## See Also


* [CREATE CATALOG](create-catalog.md)
* [Character Sets and Collations](../../../reference/data-types/string-data-types/character-sets/supported-character-sets-and-collations.md)
* [Information Schema CATALOG Table](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-catalog-table.md)

