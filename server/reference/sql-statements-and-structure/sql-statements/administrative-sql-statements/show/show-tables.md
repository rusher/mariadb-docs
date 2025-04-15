
# SHOW TABLES

## Syntax


```
SHOW [FULL] TABLES [FROM db_name]
    [LIKE 'pattern' | WHERE expr]
```


## Description


`<code>SHOW TABLES</code>` lists the tables (until [MariaDB 11.2.0](../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-2-series/mariadb-11-2-0-release-notes.md), only non-`<code>TEMPORARY</code>` tables are shown), [sequences](../../../sequences/README.md) and [views](../../../../../server-usage/programming-customizing-mariadb/views/README.md) in a given database.


The `<code>LIKE</code>` clause, if present on its own, indicates which table names to match. The `<code>WHERE</code>` and `<code>LIKE</code>` clauses can be given to select rows using more general conditions, as discussed in [Extended SHOW](extended-show.md). For example, when searching for tables in the `<code>test</code>` database, the column name for use in the `<code>WHERE</code>` and `<code>LIKE</code>` clauses will be `<code>Tables_in_test</code>`


The `<code>FULL</code>` modifier is supported such that `<code>SHOW FULL TABLES</code>` displays a second output column. Values for the second column, `<code>Table_type</code>`, are `<code>BASE TABLE</code>` for a table, `<code>VIEW</code>` for a [view](../../../../../server-usage/programming-customizing-mariadb/views/README.md) and `<code>SEQUENCE</code>` for a [sequence](../../../sequences/README.md).


You can also get this information using:


```
mariadb-show db_name
```

See [mariadb-show](../../../../../clients-and-utilities/mariadb-show.md) for more details.


If you have no privileges for a base table or view, it does not show up in the output from `<code>SHOW TABLES</code>` or `<code>mariadb-show <em>db_name</em></code>`.


The [information_schema.TABLES](../system-tables/information-schema/information-schema-tables/information-schema-tables-table.md) table, as well as the [SHOW TABLE STATUS](show-table-status.md) statement, provide extended information about tables.


## Examples


```
SHOW TABLES;
+----------------------+
| Tables_in_test       |
+----------------------+
| animal_count         |
| animals              |
| are_the_mooses_loose |
| aria_test2           |
| t1                   |
| view1                |
+----------------------+
```

Showing the tables beginning with *a* only.


```
SHOW TABLES WHERE Tables_in_test LIKE 'a%';
+----------------------+
| Tables_in_test       |
+----------------------+
| animal_count         |
| animals              |
| are_the_mooses_loose |
| aria_test2           |
+----------------------+
```

Showing tables and table types:


```
SHOW FULL TABLES;
+----------------+------------+
| Tables_in_test | Table_type |
+----------------+------------+
| s1             | SEQUENCE   |
| student        | BASE TABLE |
| v1             | VIEW       |
+----------------+------------+
```

Showing temporary tables:
<= [MariaDB 11.1](../../../../../../release-notes/mariadb-community-server/what-is-mariadb-111.md)


```
CREATE TABLE t (t int(11));
CREATE TEMPORARY TABLE t (t int(11));
CREATE TEMPORARY TABLE te (t int(11));

SHOW TABLES;
+----------------+
| Tables_in_test |
+----------------+
| t              |
+----------------+
```

From [MariaDB 11.2.0](../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-2-series/mariadb-11-2-0-release-notes.md):


```
CREATE TABLE t (t int(11));
CREATE TEMPORARY TABLE t (t int(11));
CREATE TEMPORARY TABLE te (t int(11));

SHOW TABLES;
+----------------+
| Tables_in_test |
+----------------+
| te             |
| t              |
| t              |
+----------------+
```

## See Also


* [SHOW TABLE STATUS](show-table-status.md)
* The [information_schema.TABLES](../system-tables/information-schema/information-schema-tables/information-schema-tables-table.md) table

