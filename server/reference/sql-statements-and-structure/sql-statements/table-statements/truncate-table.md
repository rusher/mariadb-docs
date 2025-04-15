# TRUNCATE TABLE

#

# Syntax

```
TRUNCATE [TABLE] tbl_name
 [WAIT n | NOWAIT]
```

#

# Description

`TRUNCATE TABLE` empties a table completely. It requires the `DROP` privilege. See [GRANT](../account-management-sql-commands/grant.md).

`tbl_name` can also be specified in the form `db_name`.`tbl_name` (see [Identifier Qualifiers](../../sql-language-structure/identifier-qualifiers.md)).

Logically, `TRUNCATE TABLE` is equivalent to a [DELETE](../data-manipulation/changing-deleting-data/delete.md) statement that deletes all rows, but there are practical differences under some circumstances.

`TRUNCATE TABLE` will fail for an [InnoDB table](../../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/innodb-encryption/innodb-encryption-troubleshooting.md) if any FOREIGN KEY constraints from other tables reference the table, returning the error:

```
ERROR 1701 (42000): Cannot truncate a table referenced in a foreign key constraint
```

Foreign Key constraints between columns in the same table are permitted.

For an InnoDB table, if there are no `FOREIGN KEY` constraints, InnoDB performs fast truncation by dropping the original table and creating an empty one with the same definition, which is much faster than deleting rows one by one. The [AUTO_INCREMENT](../../../data-types/auto_increment.md) counter is reset by `TRUNCATE TABLE`, regardless of whether there is a `FOREIGN KEY` constraint.

The count of rows affected by `TRUNCATE TABLE` is accurate only
when it is mapped to a `DELETE` statement.

For other storage engines, `TRUNCATE TABLE` differs from
`DELETE` in the following ways:

* Truncate operations drop and re-create the table, which is much
 faster than deleting rows one by one, particularly for large tables.
* Truncate operations cause an implicit commit.
* Truncation operations cannot be performed if the session holds an
 active table lock.
* Truncation operations do not return a meaningful value for the number
 of deleted rows. The usual result is "0 rows affected," which should
 be interpreted as "no information."
* As long as the table format file `tbl_name.frm` is valid, the
 table can be re-created as an empty table
 with `TRUNCATE TABLE`, even if the data or index files have become
 corrupted.
* The table handler does not remember the last
 used [AUTO_INCREMENT](../../../data-types/auto_increment.md) value, but starts counting
 from the beginning. This is true even for MyISAM and InnoDB, which normally
 do not reuse sequence values.
* When used with partitioned tables, `TRUNCATE TABLE` preserves
 the partitioning; that is, the data and index files are dropped and
 re-created, while the partition definitions (.par) file is
 unaffected.
* Since truncation of a table does not make any use of `DELETE`,
 the `TRUNCATE` statement does not invoke `ON DELETE` triggers.
* `TRUNCATE TABLE` will only reset the values in the [Performance Schema summary tables](../administrative-sql-statements/system-tables/performance-schema/performance-schema-tables/list-of-performance-schema-tables.md) to zero or null, and will not remove the rows.

For the purposes of binary logging and [replication](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/mariadb-releases/compatibility-differences/replication-compatibility-between-mariadb-and-mysql), `TRUNCATE TABLE` is treated as [DROP TABLE](../data-definition/drop/drop-tablespace.md) followed by [CREATE TABLE](../data-definition/create/create-tablespace.md) (DDL rather than DML).

`TRUNCATE TABLE` does not work on [views](/kb/en/views/). Currently, `TRUNCATE TABLE` drops all historical records from a [system-versioned table](../../temporal-tables/system-versioned-tables.md).

#

### WAIT/NOWAIT

Set the lock wait timeout. See [WAIT and NOWAIT](../transactions/wait-and-nowait.md).

#

## Oracle-mode

[Oracle-mode](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/mariadb-releases/compatibility-differences/sql_modeoracle) from [MariaDB 10.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/what-is-mariadb-103) permits the optional keywords REUSE STORAGE or DROP STORAGE to be used.

```
TRUNCATE [TABLE] tbl_name [{DROP | REUSE} STORAGE] [WAIT n | NOWAIT]
```

These have no effect on the operation.

#

## Performance

`TRUNCATE TABLE` is faster than [DELETE](delete-table), because it drops and re-creates a table.

With [InnoDB](../../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/innodb-encryption/innodb-encryption-troubleshooting.md), `TRUNCATE TABLE` is slower if [innodb_file_per_table=ON](../../../storage-engines/innodb/innodb-system-variables.md#innodb_file_per_table) is set (the default). This is because `TRUNCATE TABLE` unlinks the underlying tablespace file, which can be an expensive operation. See [MDEV-8069](https://jira.mariadb.org/browse/MDEV-8069) for more details.

The performance issues with [innodb_file_per_table=ON](../../../storage-engines/innodb/innodb-system-variables.md#innodb_file_per_table) can be exacerbated in cases where the [InnoDB buffer pool](../../../storage-engines/innodb/innodb-buffer-pool.md) is very large and [innodb_adaptive_hash_index=ON](../../../storage-engines/innodb/innodb-system-variables.md#innodb_adaptive_hash_index) is set. In that case, using [DROP TABLE](../data-definition/drop/drop-tablespace.md) followed by [CREATE TABLE](../data-definition/create/create-tablespace.md) instead of `TRUNCATE TABLE` may perform better. Setting [innodb_adaptive_hash_index=OFF](../../../storage-engines/innodb/innodb-system-variables.md#innodb_adaptive_hash_index) (it defaults to ON before [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/what-is-mariadb-105)) can also help. In [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/what-is-mariadb-102) only, from [MariaDB 10.2.19](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/release-notes-mariadb-102-series/mariadb-10219-release-notes), this performance can also be improved by setting [innodb_safe_truncate=OFF](../../../storage-engines/innodb/innodb-system-variables.md#innodb_safe_truncate). See [MDEV-9459](https://jira.mariadb.org/browse/MDEV-9459) for more details.

Setting [innodb_adaptive_hash_index=OFF](../../../storage-engines/innodb/innodb-system-variables.md#innodb_adaptive_hash_index) can also improve `TRUNCATE TABLE` performance in general. See [MDEV-16796](https://jira.mariadb.org/browse/MDEV-16796) for more details.

#

# See Also

* [TRUNCATE function](../built-in-functions/numeric-functions/truncate.md)
* [innodb_safe_truncate](../../../storage-engines/innodb/innodb-system-variables.md#innodb_safe_truncate) system variable
* [Oracle mode from MariaDB 10.3](/kb/en/sql_modeoracle-from-mariadb-103/#simple-syntax-compatibility)