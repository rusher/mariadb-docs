
# RENAME TABLE

## Syntax


```
RENAME TABLE[S] [IF EXISTS] tbl_name 
  [WAIT n | NOWAIT]
  TO new_tbl_name
    [, tbl_name2 TO new_tbl_name2] ...
```


## Description


This statement renames one or more tables or [views](../../../../server-usage/programming-customizing-mariadb/views/README.md), but not the privileges associated with them. For InnoDB tables, it also triggers a reload of [InnoDB statistics](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/query-optimizations/statistics-for-optimizing-queries/innodb-persistent-statistics.md).


### IF EXISTS


If this directive is used, one will not get an error if the table to be renamed doesn't exist.


The rename operation is done atomically, which means that no other session can
access any of the tables while the rename is running. For example, if you have
an existing table `<code class="fixed" style="white-space:pre-wrap">old_table</code>`, you can create another table
`<code class="fixed" style="white-space:pre-wrap">new_table</code>` that has the same structure but is empty, and then
replace the existing table with the empty one as follows (assuming that
`<code class="fixed" style="white-space:pre-wrap">backup_table</code>` does not already exist):


```
CREATE TABLE new_table (...);
RENAME TABLE old_table TO backup_table, new_table TO old_table;
```

`<code>tbl_name</code>` can optionally be specified as `<code>db_name</code>`.`<code>tbl_name</code>`. See [Identifier Qualifiers](../../sql-language-structure/identifier-qualifiers.md). This allows to use `<code>RENAME</code>` to move a table from a database to another (as long as they are on the same filesystem):


```
RENAME TABLE db1.t TO db2.t;
```

Note that moving a table to another database is not possible if it has some [triggers](../../../../server-usage/programming-customizing-mariadb/triggers-events/triggers/triggers-and-implicit-locks.md). Trying to do so produces the following error:


```
ERROR 1435 (HY000): Trigger in wrong schema
```

Also, views cannot be moved to another database:


```
ERROR 1450 (HY000): Changing schema from 'old_db' to 'new_db' is not allowed.
```

Multiple tables can be renamed in a single statement. The presence or absence of the optional `<code>S</code>` (`<code>RENAME TABLE</code>` or `<code>RENAME TABLES</code>`) has no impact, whether a single or multiple tables are being renamed.


If a `<code>RENAME TABLE</code>` renames more than one table and one renaming fails, all renames executed by the same statement are rolled back.


Renames are always executed in the specified order. Knowing this, it is also possible to swap two tables' names:


```
RENAME TABLE t1 TO tmp_table,
    t2 TO t1,
    tmp_table TO t2;
```

### WAIT/NOWAIT


Set the lock wait timeout. See [WAIT and NOWAIT](../transactions/wait-and-nowait.md).


### Privileges


Executing the `<code>RENAME TABLE</code>` statement requires the [DROP](../account-management-sql-commands/grant.md#table-privileges), [CREATE](../account-management-sql-commands/grant.md#table-privileges) and [INSERT](../account-management-sql-commands/grant.md#table-privileges) privileges for the table or the database.


### Atomic RENAME TABLE



##### MariaDB starting with [10.6.1](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-1061-release-notes.md)
From [MariaDB 10.6](../../../../../release-notes/mariadb-community-server/what-is-mariadb-106.md), `<code>RENAME TABLE</code>` is atomic for most engines, including InnoDB, MyRocks, MyISAM and Aria ([MDEV-23842](https://jira.mariadb.org/browse/MDEV-23842)).
This means that if there is a crash (server down or power outage) during `<code>RENAME TABLE</code>`, all tables will revert to their original names and any changes to trigger files will be reverted.
In older MariaDB version there was a small chance that, during a server crash happening in the middle of `<code>RENAME TABLE</code>`, some tables could have been renamed (in the worst case partly) while others would not be renamed.
See [Atomic DDL](atomic-ddl.md) for more information.

