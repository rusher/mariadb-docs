
# SHOW DATABASES

## Syntax


```
SHOW {DATABASES | SCHEMAS}
    [LIKE 'pattern' | WHERE expr]
```


## Description


`<code class="highlight fixed" style="white-space:pre-wrap">SHOW DATABASES</code>` lists the databases on the MariaDB server host.
`<code class="highlight fixed" style="white-space:pre-wrap">SHOW SCHEMAS</code>` is a synonym for 
`<code class="highlight fixed" style="white-space:pre-wrap">SHOW DATABASES</code>`. The `<code class="highlight fixed" style="white-space:pre-wrap">LIKE</code>` clause, if
present on its own, indicates which database names to match. The `<code class="highlight fixed" style="white-space:pre-wrap">WHERE</code>` and `<code class="highlight fixed" style="white-space:pre-wrap">LIKE</code>` clauses can be given to select rows using more general conditions, as discussed in [Extended SHOW](extended-show.md).


You see only those databases for which you have some kind of
privilege, unless you have the global 
[SHOW DATABASES privilege](../../account-management-sql-commands/grant.md). You
can also get this list using the [mariadb-show](../../../../../clients-and-utilities/mariadb-show.md) command.


If the server was started with the `<code class="highlight fixed" style="white-space:pre-wrap">--skip-show-database</code>`
option, you cannot use this statement at all unless you have the
[SHOW DATABASES privilege](../../account-management-sql-commands/grant.md).


The list of results returned by `<code>SHOW DATABASES</code>` is based on directories in the data directory, which is how MariaDB implements databases. It's possible that output includes directories that do not correspond to actual databases.


The [Information Schema SCHEMATA table](../system-tables/information-schema/information-schema-tables/information-schema-schemata-table.md) also contains database information.


## Examples


```
SHOW DATABASES;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| test               |
+--------------------+
```

```
SHOW DATABASES LIKE 'm%';
+---------------+
| Database (m%) |
+---------------+
| mysql         |
+---------------+
```

## See Also


* [CREATE DATABASE](../../data-definition/create/create-database.md)
* [ALTER DATABASE](../../data-definition/alter/alter-database.md)
* [DROP DATABASE](../../data-definition/drop/drop-database.md)
* [SHOW CREATE DATABASE](show-create-database.md)
* [Character Sets and Collations](../../../../data-types/string-data-types/character-sets/supported-character-sets-and-collations.md)
* [Information Schema SCHEMATA Table](../system-tables/information-schema/information-schema-tables/information-schema-schemata-table.md)

