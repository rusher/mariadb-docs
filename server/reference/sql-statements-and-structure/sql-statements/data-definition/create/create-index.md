
# CREATE INDEX

## Syntax


```
CREATE [OR REPLACE] [UNIQUE|FULLTEXT|SPATIAL] INDEX 
  [IF NOT EXISTS] index_name
    [index_type]
    ON tbl_name (index_col_name,...)
    [WAIT n | NOWAIT]
    [index_option]
    [algorithm_option | lock_option] ...

index_col_name:
    col_name [(length)] [ASC | DESC]

index_type:
    USING {BTREE | HASH | RTREE}

index_option:
    [ KEY_BLOCK_SIZE [=] value
  | index_type
  | WITH PARSER parser_name
  | COMMENT 'string'
  | CLUSTERING={YES| NO} ]
  [ IGNORED | NOT IGNORED ]

algorithm_option:
    ALGORITHM [=] {DEFAULT|INPLACE|COPY|NOCOPY|INSTANT}

lock_option:
    LOCK [=] {DEFAULT|NONE|SHARED|EXCLUSIVE}
```


## Description


The *CREATE INDEX* statement is used to add indexes to a table. Indexes can be created at the same as the table, with the [CREATE TABLE](../../../vectors/create-table-with-vectors.md) statement. In some cases, such as for InnoDB primary keys, doing so during creation is preferable, as adding a primary key will involve rebuilding the table.


The statement is mapped to an ALTER TABLE statement to create [indexes](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/optimization-and-indexes/README.md).
See [ALTER TABLE](../alter/alter-tablespace.md). CREATE INDEX cannot be used to create a
[PRIMARY KEY](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/optimization-and-indexes/getting-started-with-indexes.md#primary-key); use ALTER TABLE instead.


If another connection is using the table, a [metadata lock](../../transactions/metadata-locking.md) is active, and this statement will wait until the lock is released. This is also true for non-transactional tables.


Another shortcut, [DROP INDEX](../drop/drop-index.md), allows the removal of an index.


For valid identifiers to use as index names, see [Identifier Names](../../../sql-language-structure/identifier-names.md).


For limits on InnoDB indexes, see [InnoDB Limitations](../../../../storage-engines/innodb/innodb-limitations.md).


Note that KEY_BLOCK_SIZE is currently ignored in CREATE INDEX, although it is included in the output of [SHOW CREATE TABLE](../../administrative-sql-statements/show/show-create-table.md).


## Privileges


Executing the `CREATE INDEX` statement requires the `[INDEX](../../account-management-sql-commands/grant.md#table-privileges)` privilege for the table or the database.


## Online DDL


Online DDL is supported with the [ALGORITHM](#algorithm) and [LOCK](#lock) clauses.


See [InnoDB Online DDL Overview](../../../../storage-engines/innodb/innodb-online-ddl/innodb-online-ddl-overview.md) for more information on online DDL with [InnoDB](../../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/innodb-upgrade-tests/README.md).


## CREATE OR REPLACE INDEX


If the `OR REPLACE` clause is used and if the index already exists, then instead of returning an error, the server will drop the existing index and replace it with the newly defined index.


## CREATE INDEX IF NOT EXISTS


If the `IF NOT EXISTS` clause is used, then the index will only be created if an index with the same name does not already exist. If the index already exists, then a warning will be triggered by default.


## Index Definitions


See [CREATE TABLE: Index Definitions](../../../vectors/create-table-with-vectors.md#index-definitions) for information about index definitions.


## WAIT/NOWAIT


Set the lock wait timeout. See [WAIT and NOWAIT](../../transactions/wait-and-nowait.md).


## ALGORITHM


See [ALTER TABLE: ALGORITHM](../alter/alter-tablespace.md#algorithm) for more information.


## LOCK


See [ALTER TABLE: LOCK](../alter/alter-tablespace.md#lock) for more information.


## Progress Reporting


MariaDB provides progress reporting for `CREATE INDEX` statement for clients
that support the new progress reporting protocol. For example, if you were using the [mariadb](../../../../../clients-and-utilities/mariadb-client/mariadb-command-line-client.md) client, then the progress report might look like this::


```
CREATE INDEX i ON tab (num);
Stage: 1 of 2 'copy to tmp table'    46% of stage
```

The progress report is also shown in the output of the [SHOW PROCESSLIST](../../administrative-sql-statements/show/show-processlist.md) statement and in the contents of the [information_schema.PROCESSLIST](../../administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-processlist-table.md) table.


See [Progress Reporting](../../../../mariadb-internals/using-mariadb-with-your-programs-api/progress-reporting.md) for more information.


## WITHOUT OVERLAPS



##### MariaDB starting with [10.5.3](../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1053-release-notes.md)
The [WITHOUT OVERLAPS](../../../temporal-tables/application-time-periods.md#without-overlaps) clause allows one to constrain a primary or unique index such that [application-time periods](../../../temporal-tables/application-time-periods.md) cannot overlap.


## Examples


Creating a unique index:


```
CREATE UNIQUE INDEX HomePhone ON Employees(Home_Phone);
```

OR REPLACE and IF NOT EXISTS:


```
CREATE INDEX xi ON xx5 (x);
Query OK, 0 rows affected (0.03 sec)

CREATE INDEX xi ON xx5 (x);
ERROR 1061 (42000): Duplicate key name 'xi'

CREATE OR REPLACE INDEX xi ON xx5 (x);
Query OK, 0 rows affected (0.03 sec)

CREATE INDEX IF NOT EXISTS xi ON xx5 (x);
Query OK, 0 rows affected, 1 warning (0.00 sec)

SHOW WARNINGS;
+-------+------+-------------------------+
| Level | Code | Message                 |
+-------+------+-------------------------+
| Note  | 1061 | Duplicate key name 'xi' |
+-------+------+-------------------------+
```

From [MariaDB 10.5.3](../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1053-release-notes.md), creating a unique index for an [application-time period table](../../../temporal-tables/application-time-periods.md) with a [WITHOUT OVERLAPS](../../../temporal-tables/application-time-periods.md#without-overlaps) constraint:


```
CREATE UNIQUE INDEX u ON rooms (room_number, p WITHOUT OVERLAPS);
```

## See Also


* [Identifier Names](../../../sql-language-structure/identifier-names.md)
* [Getting Started with Indexes](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/optimization-and-indexes/getting-started-with-indexes.md)
* [What is an Index?](../../../../../../general-resources/learning-and-training/training-and-tutorials/basic-mariadb-articles/the-essentials-of-an-index.md)
* [ALTER TABLE](../alter/alter-tablespace.md)
* [DROP INDEX](../drop/drop-index.md)
* [SHOW INDEX](../../administrative-sql-statements/show/show-index.md)
* [SPATIAL INDEX](../../../geographic-geometric-features/spatial-index.md)
* [Full-text Indexes](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/optimization-and-indexes/full-text-indexes/README.md)
* [WITHOUT OVERLAPS](../../../temporal-tables/application-time-periods.md#without-overlaps)
* [Ignored Indexes](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/optimization-and-indexes/ignored-indexes.md)
* [InnoDB Limitations](../../../../storage-engines/innodb/innodb-limitations.md)

