
# TRUNCATE TABLE

## Syntax


```
TRUNCATE [TABLE] tbl_name
  [WAIT n | NOWAIT]
```


## Description


`<code>TRUNCATE TABLE</code>` empties a table completely. It requires the `<code>DROP</code>` privilege. See [GRANT](../account-management-sql-commands/grant.md).


`<code>tbl_name</code>` can also be specified in the form `<code>db_name</code>`.`<code>tbl_name</code>` (see [Identifier Qualifiers](../../sql-language-structure/identifier-qualifiers.md)).


Logically, `<code>TRUNCATE TABLE</code>` is equivalent to a [DELETE](../data-manipulation/changing-deleting-data/delete.md) statement that deletes all rows, but there are practical differences under some circumstances.


`<code>TRUNCATE TABLE</code>` will fail for an [InnoDB table](../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/innodb-upgrade-tests/README.md) if any FOREIGN KEY constraints from other tables reference the table, returning the error:


```
ERROR 1701 (42000): Cannot truncate a table referenced in a foreign key constraint
```

Foreign Key constraints between columns in the same table are permitted.


For an InnoDB table, if there are no `<code>FOREIGN KEY</code>` constraints, InnoDB performs fast truncation by dropping the original table and creating an empty one with the same definition, which is much faster than deleting rows one by one. The [AUTO_INCREMENT](../../../storage-engines/innodb/auto_increment-handling-in-innodb.md) counter is reset by `<code>TRUNCATE TABLE</code>`, regardless of whether there is a `<code>FOREIGN KEY</code>` constraint.


The count of rows affected by `<code>TRUNCATE TABLE</code>` is accurate only
when it is mapped to a `<code>DELETE</code>` statement.


For other storage engines, `<code>TRUNCATE TABLE</code>` differs from
`<code>DELETE</code>` in the following ways:


* Truncate operations drop and re-create the table, which is much
 faster than deleting rows one by one, particularly for large tables.
* Truncate operations cause an implicit commit.
* Truncation operations cannot be performed if the session holds an
 active table lock.
* Truncation operations do not return a meaningful value for the number
 of deleted rows. The usual result is "0 rows affected," which should
 be interpreted as "no information."
* As long as the table format file `<code>tbl_name.frm</code>` is valid, the
 table can be re-created as an empty table
 with `<code>TRUNCATE TABLE</code>`, even if the data or index files have become
 corrupted.
* The table handler does not remember the last
 used [AUTO_INCREMENT](../../../storage-engines/innodb/auto_increment-handling-in-innodb.md) value, but starts counting
 from the beginning. This is true even for MyISAM and InnoDB, which normally
 do not reuse sequence values.
* When used with partitioned tables, `<code>TRUNCATE TABLE</code>` preserves
 the partitioning; that is, the data and index files are dropped and
 re-created, while the partition definitions (.par) file is
 unaffected.
* Since truncation of a table does not make any use of `<code>DELETE</code>`,
 the `<code>TRUNCATE</code>` statement does not invoke `<code>ON DELETE</code>` triggers.
* `<code>TRUNCATE TABLE</code>` will only reset the values in the [Performance Schema summary tables](../administrative-sql-statements/system-tables/performance-schema/performance-schema-tables/list-of-performance-schema-tables.md) to zero or null, and will not remove the rows.


For the purposes of binary logging and [replication](../administrative-sql-statements/replication-statements/README.md), `<code>TRUNCATE TABLE</code>` is treated as [DROP TABLE](../data-definition/drop/drop-tablespace.md) followed by [CREATE TABLE](../../vectors/create-table-with-vectors.md) (DDL rather than DML).


`<code>TRUNCATE TABLE</code>` does not work on [views](../../../../server-usage/programming-customizing-mariadb/views/README.md). Currently, `<code>TRUNCATE TABLE</code>` drops all historical records from a [system-versioned table](../../temporal-tables/system-versioned-tables.md).


#### WAIT/NOWAIT


Set the lock wait timeout. See [WAIT and NOWAIT](../transactions/wait-and-nowait.md).


### Oracle-mode


[Oracle-mode](../../../../../release-notes/mariadb-community-server/compatibility-and-differences/sql_modeoracle.md) from [MariaDB 10.3](../../../../../release-notes/mariadb-community-server/what-is-mariadb-103.md) permits the optional keywords REUSE STORAGE or DROP STORAGE to be used.


```
TRUNCATE [TABLE] tbl_name [{DROP | REUSE} STORAGE] [WAIT n | NOWAIT]
```

These have no effect on the operation.


### Performance


`<code>TRUNCATE TABLE</code>` is faster than [DELETE](https://mariadb.com/kb/en/delete-table), because it drops and re-creates a table.


With [InnoDB](../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/innodb-upgrade-tests/README.md), `<code>TRUNCATE TABLE</code>` is slower if [innodb_file_per_table=ON](../../../storage-engines/innodb/innodb-system-variables.md#innodb_file_per_table) is set (the default). This is because `<code>TRUNCATE TABLE</code>` unlinks the underlying tablespace file, which can be an expensive operation. See [MDEV-8069](https://jira.mariadb.org/browse/MDEV-8069) for more details.


The performance issues with [innodb_file_per_table=ON](../../../storage-engines/innodb/innodb-system-variables.md#innodb_file_per_table) can be exacerbated in cases where the [InnoDB buffer pool](../../../storage-engines/innodb/innodb-buffer-pool.md) is very large and [innodb_adaptive_hash_index=ON](../../../storage-engines/innodb/innodb-system-variables.md#innodb_adaptive_hash_index) is set. In that case, using [DROP TABLE](../data-definition/drop/drop-tablespace.md) followed by [CREATE TABLE](../../vectors/create-table-with-vectors.md) instead of `<code>TRUNCATE TABLE</code>` may perform better. Setting [innodb_adaptive_hash_index=OFF](../../../storage-engines/innodb/innodb-system-variables.md#innodb_adaptive_hash_index) (it defaults to ON before [MariaDB 10.5](../../../../../release-notes/mariadb-community-server/what-is-mariadb-105.md)) can also help. In [MariaDB 10.2](../../../../../release-notes/mariadb-community-server/what-is-mariadb-102.md) only, from [MariaDB 10.2.19](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-10219-release-notes.md), this performance can also be improved by setting [innodb_safe_truncate=OFF](../../../storage-engines/innodb/innodb-system-variables.md#innodb_safe_truncate). See [MDEV-9459](https://jira.mariadb.org/browse/MDEV-9459) for more details.


Setting [innodb_adaptive_hash_index=OFF](../../../storage-engines/innodb/innodb-system-variables.md#innodb_adaptive_hash_index) can also improve `<code>TRUNCATE TABLE</code>` performance in general. See [MDEV-16796](https://jira.mariadb.org/browse/MDEV-16796) for more details.


## See Also


* [TRUNCATE function](truncate-table.md)
* [innodb_safe_truncate](../../../storage-engines/innodb/innodb-system-variables.md#innodb_safe_truncate) system variable
* [Oracle mode from MariaDB 10.3](../../../../../release-notes/mariadb-community-server/compatibility-and-differences/sql_modeoracle.md)

