
# SHOW OPEN TABLES

## Syntax


```
SHOW OPEN TABLES [FROM db_name]
    [LIKE 'pattern' | WHERE expr]
```

## Description


`<code class="highlight fixed" style="white-space:pre-wrap">SHOW OPEN TABLES</code>` lists the non-`<code class="highlight fixed" style="white-space:pre-wrap">TEMPORARY</code>`
tables that are currently open in the table cache. See
[table-cache.html](https://dev.mysql.com/doc/refman/5.1/en/table-cache.html).


The `<code class="highlight fixed" style="white-space:pre-wrap">FROM</code>` and `<code class="highlight fixed" style="white-space:pre-wrap">LIKE</code>` clauses may be used.


The `<code class="highlight fixed" style="white-space:pre-wrap">FROM</code>`
clause, if present, restricts the tables shown to those present in the
`<code class="highlight fixed" style="white-space:pre-wrap">db_name</code>` database.


The `<code class="highlight fixed" style="white-space:pre-wrap">LIKE</code>` clause, if
present on its own, indicates which table names to match. The `<code class="highlight fixed" style="white-space:pre-wrap">WHERE</code>` and `<code class="highlight fixed" style="white-space:pre-wrap">LIKE</code>` clauses can be given to select rows using more general conditions, as discussed in [Extended SHOW](extended-show.md).


The following information is returned:



| Column | Description |
| --- | --- |
| Column | Description |
| Database | Database name. |
| Name | Table name. |
| In_use | Number of table instances being used. |
| Name_locked | 1 if the table is name-locked, e.g. if it is being dropped or renamed, otherwise 0. |



Before [MariaDB 5.5](../../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5.md), each use of, for example, [LOCK TABLE ... WRITE](../../transactions/lock-tables.md) would increment `<code>In_use</code>` for that table. With the implementation of the metadata locking improvements in [MariaDB 5.5](../../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5.md), `<code>LOCK TABLE... WRITE</code>` acquires a strong MDL lock, and concurrent connections will wait on this MDL lock, so any subsequent `<code>LOCK TABLE... WRITE</code>` will not increment `<code>In_use</code>`.


## Example


```
SHOW OPEN TABLES;
+----------+---------------------------+--------+-------------+
| Database | Table                     | In_use | Name_locked |
+----------+---------------------------+--------+-------------+
...
| test     | xjson                     |      0 |           0 |
| test     | jauthor                   |      0 |           0 |
| test     | locks                     |      1 |           0 |
...
+----------+---------------------------+--------+-------------+
```
