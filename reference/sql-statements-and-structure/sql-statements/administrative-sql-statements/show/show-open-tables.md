# SHOW OPEN TABLES

#

# Syntax

```
SHOW OPEN TABLES [FROM db_name]
 [LIKE 'pattern' | WHERE expr]
```

#

# Description

`SHOW OPEN TABLES` lists the non-`TEMPORARY`
tables that are currently open in the table cache. See
[http://dev.mysql.com/doc/refman/5.1/en/table-cache.html](http://dev.mysql.com/doc/refman/5.1/en/table-cache.html).

The `FROM` and `LIKE` clauses may be used.

The `FROM`
clause, if present, restricts the tables shown to those present in the
`db_name` database.

The `LIKE` clause, if
present on its own, indicates which table names to match. The `WHERE` and `LIKE` clauses can be given to select rows using more general conditions, as discussed in [Extended SHOW](extended-show.md).

The following information is returned:

| Column | Description |
| --- | --- |
| Column | Description |
| Database | Database name. |
| Name | Table name. |
| In_use | Number of table instances being used. |
| Name_locked | 1 if the table is name-locked, e.g. if it is being dropped or renamed, otherwise 0. |

Before [MariaDB 5.5](/kb/en/what-is-mariadb-55/), each use of, for example, [LOCK TABLE ... WRITE](/kb/en/lock-tables-and-unlock-tables/) would increment `In_use` for that table. With the implementation of the metadata locking improvements in [MariaDB 5.5](/kb/en/what-is-mariadb-55/), `LOCK TABLE... WRITE` acquires a strong MDL lock, and concurrent connections will wait on this MDL lock, so any subsequent `LOCK TABLE... WRITE` will not increment `In_use`.

#

# Example

```
SHOW OPEN TABLES;
+----------+---------------------------+--------+-------------+
| Database | Table | In_use | Name_locked |
+----------+---------------------------+--------+-------------+
...
| test | xjson | 0 | 0 |
| test | jauthor | 0 | 0 |
| test | locks | 1 | 0 |
...
+----------+---------------------------+--------+-------------+
```