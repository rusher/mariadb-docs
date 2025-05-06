# RENAME TABLE

## Syntax

```
RENAME TABLE[S] [IF EXISTS] tbl_name 
  [WAIT n | NOWAIT]
  TO new_tbl_name
    [, tbl_name2 TO new_tbl_name2] ...
```

## Description

This statement renames one or more tables or [views](../../../../server-usage/views/), but not the privileges associated with them. For InnoDB tables, it also triggers a reload of [InnoDB statistics](../../../../ha-and-performance/optimization-and-tuning/query-optimizations/statistics-for-optimizing-queries/innodb-persistent-statistics.md).

### IF EXISTS

If this directive is used, one will not get an error if the table to be renamed doesn't exist.

The rename operation is done atomically, which means that no other session can\
access any of the tables while the rename is running. For example, if you have\
an existing table `old_table`, you can create another table`new_table` that has the same structure but is empty, and then\
replace the existing table with the empty one as follows (assuming that`backup_table` does not already exist):

```
CREATE TABLE new_table (...);
RENAME TABLE old_table TO backup_table, new_table TO old_table;
```

`tbl_name` can optionally be specified as `db_name`.`tbl_name`. See [Identifier Qualifiers](../../sql-language-structure/identifier-qualifiers.md). This allows to use `RENAME` to move a table from a database to another (as long as they are on the same filesystem):

```
RENAME TABLE db1.t TO db2.t;
```

Note that moving a table to another database is not possible if it has some [triggers](../../../../server-usage/triggers-events/triggers/). Trying to do so produces the following error:

```
ERROR 1435 (HY000): Trigger in wrong schema
```

Also, views cannot be moved to another database:

```
ERROR 1450 (HY000): Changing schema from 'old_db' to 'new_db' is not allowed.
```

Multiple tables can be renamed in a single statement. The presence or absence of the optional `S` (`RENAME TABLE` or `RENAME TABLES`) has no impact, whether a single or multiple tables are being renamed.

If a `RENAME TABLE` renames more than one table and one renaming fails, all renames executed by the same statement are rolled back.

Renames are always executed in the specified order. Knowing this, it is also possible to swap two tables' names:

```
RENAME TABLE t1 TO tmp_table,
    t2 TO t1,
    tmp_table TO t2;
```

### WAIT/NOWAIT

Set the lock wait timeout. See [WAIT and NOWAIT](../transactions/wait-and-nowait.md).

### Privileges

Executing the `RENAME TABLE` statement requires the [DROP](../account-management-sql-commands/grant.md#table-privileges), [CREATE](../account-management-sql-commands/grant.md#table-privileges) and [INSERT](../account-management-sql-commands/grant.md#table-privileges) privileges for the table or the database.

### Atomic RENAME TABLE

**MariaDB starting with** [**10.6.1**](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-6-series/mariadb-1061-release-notes)

From [MariaDB 10.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-6-series/what-is-mariadb-106), `RENAME TABLE` is atomic for most engines, including InnoDB, MyRocks, MyISAM and Aria ([MDEV-23842](https://jira.mariadb.org/browse/MDEV-23842)).\
This means that if there is a crash (server down or power outage) during `RENAME TABLE`, all tables will revert to their original names and any changes to trigger files will be reverted.\
In older MariaDB version there was a small chance that, during a server crash happening in the middle of `RENAME TABLE`, some tables could have been renamed (in the worst case partly) while others would not be renamed.\
See [Atomic DDL](atomic-ddl.md) for more information.

GPLv2 fill\_help\_tables.sql
