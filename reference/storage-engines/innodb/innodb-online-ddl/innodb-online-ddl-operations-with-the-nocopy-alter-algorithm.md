# InnoDB Online DDL Operations with the NOCOPY Alter Algorithm

#

# Supported Operations by Inheritance

When the [ALGORITHM](../../../sql-statements-and-structure/sql-statements/data-definition/alter/alter-table.md#algorithm) clause is set to `NOCOPY`, the supported operations are a superset of the operations that are supported when the [ALGORITHM](../../../sql-statements-and-structure/sql-statements/data-definition/alter/alter-table.md#algorithm) clause is set to `INSTANT`.

Therefore, when the [ALGORITHM](../../../sql-statements-and-structure/sql-statements/data-definition/alter/alter-table.md#algorithm) clause is set to `NOCOPY`, some operations are supported by inheritance. See the following additional pages for more information about these supported operations:

* [InnoDB Online DDL Operations with ALGORITHM=INSTANT](/en/innodb-online-ddl-operations-with-algorithminstant/)

#

# Column Operations

#

## `ALTER TABLE ... ADD COLUMN`

In [MariaDB 10.3.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1032-release-notes) and later, InnoDB supports adding columns to a table with [ALGORITHM](../../../sql-statements-and-structure/sql-statements/data-definition/alter/alter-table.md#algorithm) set to `NOCOPY` in the cases where the operation supports having the [ALGORITHM](../../../sql-statements-and-structure/sql-statements/data-definition/alter/alter-table.md#algorithm) clause set to `INSTANT`.

See [InnoDB Online DDL Operations with ALGORITHM=INSTANT: ALTER TABLE ... ADD COLUMN](/en/innodb-online-ddl-operations-with-algorithminstant/#alter-table-add-column) for more information.

This applies to [ALTER TABLE ... ADD COLUMN](../../../sql-statements-and-structure/sql-statements/data-definition/alter/alter-table.md#add-column) for [InnoDB](../../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/innodb-encryption/innodb-encryption-troubleshooting.md) tables.

#

## `ALTER TABLE ... DROP COLUMN`

In [MariaDB 10.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/what-is-mariadb-104) and later, InnoDB supports dropping columns from a table with [ALGORITHM](../../../sql-statements-and-structure/sql-statements/data-definition/alter/alter-table.md#algorithm) set to `NOCOPY` in the cases where the operation supports having the [ALGORITHM](../../../sql-statements-and-structure/sql-statements/data-definition/alter/alter-table.md#algorithm) clause set to `INSTANT`.

See [InnoDB Online DDL Operations with ALGORITHM=INSTANT: ALTER TABLE ... DROP COLUMN](/en/innodb-online-ddl-operations-with-algorithminstant/#alter-table-drop-column) for more information.

This applies to [ALTER TABLE ... DROP COLUMN](../../../sql-statements-and-structure/sql-statements/data-definition/alter/alter-table.md#drop-column) for [InnoDB](../../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/innodb-encryption/innodb-encryption-troubleshooting.md) tables.

#

## `ALTER TABLE ... MODIFY COLUMN`

This applies to [ALTER TABLE ... MODIFY COLUMN](../../../sql-statements-and-structure/sql-statements/data-definition/alter/alter-table.md#modify-column) for [InnoDB](../../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/innodb-encryption/innodb-encryption-troubleshooting.md) tables.

#

### Reordering Columns

In [MariaDB 10.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/what-is-mariadb-104) and later, InnoDB supports reordering columns within a table with [ALGORITHM](../../../sql-statements-and-structure/sql-statements/data-definition/alter/alter-table.md#algorithm) set to `NOCOPY` in the cases where the operation supports having the [ALGORITHM](../../../sql-statements-and-structure/sql-statements/data-definition/alter/alter-table.md#algorithm) clause set to `INSTANT`.

See [InnoDB Online DDL Operations with ALGORITHM=INSTANT: Reordering Columns](/en/innodb-online-ddl-operations-with-algorithminstant/#reordering-columns) for more information.

#

### Changing the Data Type of a Column

InnoDB does **not** support modifying a column's data type with [ALGORITHM](../../../sql-statements-and-structure/sql-statements/data-definition/alter/alter-table.md#algorithm) set to `NOCOPY` in most cases. There are a few exceptions in the cases where the operation supports having the [ALGORITHM](../../../sql-statements-and-structure/sql-statements/data-definition/alter/alter-table.md#algorithm) clause set to `INSTANT`.

See [InnoDB Online DDL Operations with ALGORITHM=INSTANT: Changing the Data Type of a Column](/en/innodb-online-ddl-operations-with-algorithminstant/#changing-the-data-type-of-a-column) for more information.

#

### Changing a Column to NULL

In [MariaDB 10.4.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/release-notes-mariadb-104-series/mariadb-1043-release-notes) and later, InnoDB supports modifying a column to allow [NULL](../../../sql-statements-and-structure/sql-statements/data-definition/create/create-tablespace.md#null-and-not-null) values with [ALGORITHM](../../../sql-statements-and-structure/sql-statements/data-definition/alter/alter-table.md#algorithm) set to `NOCOPY` in the cases where the operation supports having the [ALGORITHM](../../../sql-statements-and-structure/sql-statements/data-definition/alter/alter-table.md#algorithm) clause set to `INSTANT`.

See [InnoDB Online DDL Operations with ALGORITHM=INSTANT: Changing a Column to NULL](/en/innodb-online-ddl-operations-with-algorithminstant/#changing-a-column-to-null) for more information.

#

### Changing a Column to NOT NULL

InnoDB does **not** support modifying a column to **not** allow [NULL](../../../sql-statements-and-structure/sql-statements/data-definition/create/create-tablespace.md#null-and-not-null) values with [ALGORITHM](../../../sql-statements-and-structure/sql-statements/data-definition/alter/alter-table.md#algorithm) set to `NOCOPY`.

For example:

```
CREATE OR REPLACE TABLE tab (
 a int PRIMARY KEY,
 b varchar(50),
 c varchar(50)
) ROW_FORMAT=REDUNDANT;

SET SESSION alter_algorithm='NOCOPY';
ALTER TABLE tab MODIFY COLUMN c varchar(50) NOT NULL;
ERROR 1845 (0A000): ALGORITHM=NOCOPY is not supported for this operation. Try ALGORITHM=INPLACE
```

#

### Adding a New `ENUM` Option

InnoDB supports adding a new [ENUM](../../../data-types/string-data-types/enum.md) option to a column with [ALGORITHM](../../../sql-statements-and-structure/sql-statements/data-definition/alter/alter-table.md#algorithm) set to `NOCOPY` in the cases where the operation supports having the [ALGORITHM](../../../sql-statements-and-structure/sql-statements/data-definition/alter/alter-table.md#algorithm) clause set to `INSTANT`.

See [InnoDB Online DDL Operations with ALGORITHM=INSTANT: Adding a New ENUM Option](/en/innodb-online-ddl-operations-with-algorithminstant/#adding-a-new-enum-option) for more information.

#

### Adding a New `SET` Option

InnoDB supports adding a new [SET](../../../data-types/string-data-types/set-data-type.md) option to a column with [ALGORITHM](../../../sql-statements-and-structure/sql-statements/data-definition/alter/alter-table.md#algorithm) set to `NOCOPY` in the cases where the operation supports having the [ALGORITHM](../../../sql-statements-and-structure/sql-statements/data-definition/alter/alter-table.md#algorithm) clause set to `INSTANT`.

See [InnoDB Online DDL Operations with ALGORITHM=INSTANT: Adding a New SET Option](/en/innodb-online-ddl-operations-with-algorithminstant/#adding-a-new-set-option) for more information.

#

### Removing System Versioning from a Column

In [MariaDB 10.3.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1038-release-notes) and later, InnoDB supports removing [system versioning](../../../sql-statements-and-structure/temporal-tables/system-versioned-tables.md) from a column with [ALGORITHM](../../../sql-statements-and-structure/sql-statements/data-definition/alter/alter-table.md#algorithm) set to `NOCOPY` in the cases where the operation supports having the [ALGORITHM](../../../sql-statements-and-structure/sql-statements/data-definition/alter/alter-table.md#algorithm) clause set to `INSTANT`.

See [InnoDB Online DDL Operations with ALGORITHM=INSTANT: Removing System Versioning from a Column](/en/innodb-online-ddl-operations-with-algorithminstant/#removing-system-versioning-from-a-column) for more information.

#

## `ALTER TABLE ... ALTER COLUMN`

This applies to [ALTER TABLE ... ALTER COLUMN](../../../sql-statements-and-structure/sql-statements/data-definition/alter/alter-table.md#alter-column) for [InnoDB](../../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/innodb-encryption/innodb-encryption-troubleshooting.md) tables.

#

### Setting a Column's Default Value

InnoDB supports modifying a column's [DEFAULT](../../../sql-statements-and-structure/sql-statements/data-definition/create/create-tablespace.md#default-column-option) value with [ALGORITHM](../../../sql-statements-and-structure/sql-statements/data-definition/alter/alter-table.md#algorithm) set to `NOCOPY` in the cases where the operation supports having the [ALGORITHM](../../../sql-statements-and-structure/sql-statements/data-definition/alter/alter-table.md#algorithm) clause set to `INSTANT`.

See [InnoDB Online DDL Operations with ALGORITHM=INSTANT: Setting a Column's Default Value](/en/innodb-online-ddl-operations-with-algorithminstant/#setting-a-columns-default-value) for more information.

#

### Removing a Column's Default Value

InnoDB supports removing a column's [DEFAULT](../../../sql-statements-and-structure/sql-statements/data-definition/create/create-tablespace.md#default-column-option) value with [ALGORITHM](../../../sql-statements-and-structure/sql-statements/data-definition/alter/alter-table.md#algorithm) set to `NOCOPY` in the cases where the operation supports having the [ALGORITHM](../../../sql-statements-and-structure/sql-statements/data-definition/alter/alter-table.md#algorithm) clause set to `INSTANT`.

See [InnoDB Online DDL Operations with ALGORITHM=INSTANT: Removing a Column's Default Value](/en/innodb-online-ddl-operations-with-algorithminstant/#removing-a-columns-default-value) for more information.

#

## `ALTER TABLE ... CHANGE COLUMN`

InnoDB supports renaming a column with [ALGORITHM](../../../sql-statements-and-structure/sql-statements/data-definition/alter/alter-table.md#algorithm) set to `NOCOPY` in the cases where the operation supports having the [ALGORITHM](../../../sql-statements-and-structure/sql-statements/data-definition/alter/alter-table.md#algorithm) clause set to `INSTANT`.

See [InnoDB Online DDL Operations with ALGORITHM=INSTANT: ALTER TABLE ... CHANGE COLUMN](/en/innodb-online-ddl-operations-with-algorithminstant/#alter-table-change-column) for more information.

This applies to [ALTER TABLE ... CHANGE COLUMN](../../../sql-statements-and-structure/sql-statements/data-definition/alter/alter-table.md#change-column) for [InnoDB](../../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/innodb-encryption/innodb-encryption-troubleshooting.md) tables.

#

# Index Operations

#

## `ALTER TABLE ... ADD PRIMARY KEY`

InnoDB does **not** support adding a primary key to a table with [ALGORITHM](../../../sql-statements-and-structure/sql-statements/data-definition/alter/alter-table.md#algorithm) set to `NOCOPY`.

For example:

```
CREATE OR REPLACE TABLE tab (
 a int,
 b varchar(50),
 c varchar(50)
);

SET SESSION sql_mode='STRICT_TRANS_TABLES';
SET SESSION alter_algorithm='NOCOPY';
ALTER TABLE tab ADD PRIMARY KEY (a);
ERROR 1845 (0A000): ALGORITHM=NOCOPY is not supported for this operation. Try ALGORITHM=INPLACE
```

This applies to [ALTER TABLE ... ADD PRIMARY KEY](../../../sql-statements-and-structure/sql-statements/data-definition/alter/alter-table.md#add-primary-key) for [InnoDB](../../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/innodb-encryption/innodb-encryption-troubleshooting.md) tables.

#

## `ALTER TABLE ... DROP PRIMARY KEY`

InnoDB does **not** support dropping a primary key with [ALGORITHM](../../../sql-statements-and-structure/sql-statements/data-definition/alter/alter-table.md#algorithm) set to `NOCOPY`.

For example:

```
CREATE OR REPLACE TABLE tab (
 a int PRIMARY KEY,
 b varchar(50),
 c varchar(50)
);

SET SESSION alter_algorithm='NOCOPY';
ALTER TABLE tab DROP PRIMARY KEY;
ERROR 1846 (0A000): ALGORITHM=NOCOPY is not supported. Reason: Dropping a primary key is not allowed without also adding a new primary key. Try ALGORITHM=COPY
```

This applies to [ALTER TABLE ... DROP PRIMARY KEY](../../../sql-statements-and-structure/sql-statements/data-definition/alter/alter-table.md#drop-primary-key) for [InnoDB](../../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/innodb-encryption/innodb-encryption-troubleshooting.md) tables.

#

## `ALTER TABLE ... ADD INDEX` and `CREATE INDEX`

This applies to [ALTER TABLE ... ADD INDEX](../../../sql-statements-and-structure/sql-statements/data-definition/alter/alter-table.md#add-index) and [CREATE INDEX](../../../sql-statements-and-structure/sql-statements/data-definition/create/create-index.md) for [InnoDB](../../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/innodb-encryption/innodb-encryption-troubleshooting.md) tables.

#

### Adding a Plain Index

InnoDB supports adding a plain index to a table with [ALGORITHM](../../../sql-statements-and-structure/sql-statements/data-definition/alter/alter-table.md#algorithm) set to `NOCOPY`.

This operation supports the non-locking strategy. This strategy can be explicitly chosen by setting the [LOCK](../../../sql-statements-and-structure/sql-statements/data-definition/alter/alter-table.md#lock) clause to `NONE`. When this strategy is used, all concurrent DML is permitted.

For example, this succeeds:

```
CREATE OR REPLACE TABLE tab (
 a int PRIMARY KEY,
 b varchar(50),
 c varchar(50)
);

SET SESSION alter_algorithm='NOCOPY';
ALTER TABLE tab ADD INDEX b_index (b);
Query OK, 0 rows affected (0.009 sec)
```

And this succeeds:

```
CREATE OR REPLACE TABLE tab (
 a int PRIMARY KEY,
 b varchar(50),
 c varchar(50)
);

SET SESSION alter_algorithm='NOCOPY';
CREATE INDEX b_index ON tab (b);
Query OK, 0 rows affected (0.009 sec)
```

#

### Adding a Fulltext Index

InnoDB supports adding a [FULLTEXT](/en/full-text-indexes/) index to a table with [ALGORITHM](../../../sql-statements-and-structure/sql-statements/data-definition/alter/alter-table.md#algorithm) set to `NOCOPY`.

However, there are some limitations, such as:

* Adding a [FULLTEXT](/en/full-text-indexes/) index to a table that does not have a user-defined `FTS_DOC_ID` column will require the table to be rebuilt once. When the table is rebuilt, the system adds a hidden `FTS_DOC_ID` column. This initial operation will have to be performed with [ALGORITHM](../../../sql-statements-and-structure/sql-statements/data-definition/alter/alter-table.md#algorithm) set to `INPLACE`.From that point forward, adding additional [FULLTEXT](/en/full-text-indexes/) indexes to the same table will not require the table to be rebuilt, and [ALGORITHM](../../../sql-statements-and-structure/sql-statements/data-definition/alter/alter-table.md#algorithm) can be set to `NOCOPY`.

* Only one [FULLTEXT](/en/full-text-indexes/) index may be added at a time when [ALGORITHM](../../../sql-statements-and-structure/sql-statements/data-definition/alter/alter-table.md#algorithm) is set to `NOCOPY`.

This operation supports a read-only locking strategy. This strategy can be explicitly chosen by setting the [LOCK](../../../sql-statements-and-structure/sql-statements/data-definition/alter/alter-table.md#lock) clause to `SHARED`. When this strategy is used, read-only concurrent DML is permitted.

For example, this succeeds, but the first operation requires the table to be rebuilt [ALGORITHM](../../../sql-statements-and-structure/sql-statements/data-definition/alter/alter-table.md#algorithm) set to `INPLACE`, so that the hidden `FTS_DOC_ID` column can be added:

```
CREATE OR REPLACE TABLE tab (
 a int PRIMARY KEY,
 b varchar(50),
 c varchar(50)
);

SET SESSION alter_algorithm='INPLACE';
ALTER TABLE tab ADD FULLTEXT INDEX b_index (b);
Query OK, 0 rows affected (0.043 sec)

SET SESSION alter_algorithm='NOCOPY';
ALTER TABLE tab ADD FULLTEXT INDEX c_index (c);
Query OK, 0 rows affected (0.017 sec)
```

And this succeeds in the same way as above:

```
CREATE OR REPLACE TABLE tab (
 a int PRIMARY KEY,
 b varchar(50),
 c varchar(50)
);

SET SESSION alter_algorithm='INPLACE';
CREATE FULLTEXT INDEX b_index ON tab (b);
Query OK, 0 rows affected (0.048 sec)

SET SESSION alter_algorithm='NOCOPY';
CREATE FULLTEXT INDEX c_index ON tab (c);
Query OK, 0 rows affected (0.016 sec)
```

But this second command fails, because only one [FULLTEXT](/en/full-text-indexes/) index can be added at a time:

```
CREATE OR REPLACE TABLE tab (
 a int PRIMARY KEY,
 b varchar(50),
 c varchar(50),
 d varchar(50)
);

SET SESSION alter_algorithm='INPLACE';
ALTER TABLE tab ADD FULLTEXT INDEX b_index (b);
Query OK, 0 rows affected (0.041 sec)

SET SESSION alter_algorithm='NOCOPY';
ALTER TABLE tab ADD FULLTEXT INDEX c_index (c), ADD FULLTEXT INDEX d_index (d);
ERROR 1846 (0A000): ALGORITHM=NOCOPY is not supported. Reason: InnoDB presently supports one FULLTEXT index creation at a time. Try ALGORITHM=COPY
```

#

### Adding a Spatial Index

InnoDB supports adding a [SPATIAL](../../../sql-statements-and-structure/geographic-geometric-features/spatial-index.md) index to a table with [ALGORITHM](../../../sql-statements-and-structure/sql-statements/data-definition/alter/alter-table.md#algorithm) set to `NOCOPY`.

This operation supports a read-only locking strategy. This strategy can be explicitly chosen by setting the [LOCK](../../../sql-statements-and-structure/sql-statements/data-definition/alter/alter-table.md#lock) clause to `SHARED`. When this strategy is used, read-only concurrent DML is permitted.

For example, this succeeds:

```
CREATE OR REPLACE TABLE tab (
 a int PRIMARY KEY,
 b varchar(50),
 c GEOMETRY NOT NULL
);

SET SESSION alter_algorithm='NOCOPY';
ALTER TABLE tab ADD SPATIAL INDEX c_index (c);
Query OK, 0 rows affected (0.005 sec)
```

And this succeeds in the same way as above:

```
CREATE OR REPLACE TABLE tab (
 a int PRIMARY KEY,
 b varchar(50),
 c GEOMETRY NOT NULL
);

SET SESSION alter_algorithm='NOCOPY';
CREATE SPATIAL INDEX c_index ON tab (c);
Query OK, 0 rows affected (0.005 sec)
```

#

## `ALTER TABLE ... DROP INDEX` and `DROP INDEX`

InnoDB supports dropping indexes from a table with [ALGORITHM](../../../sql-statements-and-structure/sql-statements/data-definition/alter/alter-table.md#algorithm) set to `NOCOPY` in the cases where the operation supports having the [ALGORITHM](../../../sql-statements-and-structure/sql-statements/data-definition/alter/alter-table.md#algorithm) clause set to `INSTANT`.

See [InnoDB Online DDL Operations with ALGORITHM=INSTANT: ALTER TABLE ... DROP INDEX and DROP INDEX](/en/innodb-online-ddl-operations-with-algorithminstant/#alter-table-drop-index-and-drop-index) for more information.

This applies to [ALTER TABLE ... DROP INDEX](../../../sql-statements-and-structure/sql-statements/data-definition/alter/alter-table.md#drop-index) and [DROP INDEX](../../../sql-statements-and-structure/sql-statements/data-definition/drop/drop-index.md) for [InnoDB](../../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/innodb-encryption/innodb-encryption-troubleshooting.md) tables.

#

## `ALTER TABLE ... ADD FOREIGN KEY`

InnoDB does supports adding foreign key constraints to a table with [ALGORITHM](../../../sql-statements-and-structure/sql-statements/data-definition/alter/alter-table.md#algorithm) set to `NOCOPY`. In order to add a new foreign key constraint to a table with [ALGORITHM](../../../sql-statements-and-structure/sql-statements/data-definition/alter/alter-table.md#algorithm) set to `NOCOPY`, the [foreign_key_checks](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#foreign_key_checks) system variable needs to be set to `OFF`. If it is set to `ON`, then `ALGORITHM=COPY` is required.

This operation supports the non-locking strategy. This strategy can be explicitly chosen by setting the [LOCK](../../../sql-statements-and-structure/sql-statements/data-definition/alter/alter-table.md#lock) clause to `NONE`. When this strategy is used, all concurrent DML is permitted.

For example, this fails:

```
CREATE OR REPLACE TABLE tab1 (
 a int PRIMARY KEY,
 b varchar(50),
 c varchar(50),
 d int
);

CREATE OR REPLACE TABLE tab2 (
 a int PRIMARY KEY,
 b varchar(50)
);

SET SESSION alter_algorithm='NOCOPY';
ALTER TABLE tab1 ADD FOREIGN KEY tab2_fk (d) REFERENCES tab2 (a);
ERROR 1846 (0A000): ALGORITHM=NOCOPY is not supported. Reason: Adding foreign keys needs foreign_key_checks=OFF. Try ALGORITHM=COPY
```

But this succeeds:

```
CREATE OR REPLACE TABLE tab1 (
 a int PRIMARY KEY,
 b varchar(50),
 c varchar(50),
 d int
);

CREATE OR REPLACE TABLE tab2 (
 a int PRIMARY KEY,
 b varchar(50)
);

SET SESSION foreign_key_checks=OFF;
SET SESSION alter_algorithm='NOCOPY';
ALTER TABLE tab1 ADD FOREIGN KEY tab2_fk (d) REFERENCES tab2 (a);
Query OK, 0 rows affected (0.011 sec)
```

This applies to [ALTER TABLE ... ADD FOREIGN KEY](../../../sql-statements-and-structure/sql-statements/data-definition/alter/alter-table.md#add-foreign-key) for [InnoDB](../../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/innodb-encryption/innodb-encryption-troubleshooting.md) tables.

#

## `ALTER TABLE ... DROP FOREIGN KEY`

InnoDB supports dropping foreign key constraints from a table with [ALGORITHM](../../../sql-statements-and-structure/sql-statements/data-definition/alter/alter-table.md#algorithm) set to `NOCOPY` in the cases where the operation supports having the [ALGORITHM](../../../sql-statements-and-structure/sql-statements/data-definition/alter/alter-table.md#algorithm) clause set to `INSTANT`.

See [InnoDB Online DDL Operations with ALGORITHM=INSTANT: ALTER TABLE ... DROP FOREIGN KEY](/en/innodb-online-ddl-operations-with-algorithminstant/#alter-table-drop-foreign-key) for more information.

This applies to [ALTER TABLE ... DROP FOREIGN KEY](../../../sql-statements-and-structure/sql-statements/data-definition/alter/alter-table.md#drop-foreign-key) for [InnoDB](../../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/innodb-encryption/innodb-encryption-troubleshooting.md) tables.

#

# Table Operations

#

## `ALTER TABLE ... AUTO_INCREMENT=...`

InnoDB supports changing a table's [AUTO_INCREMENT](../../../data-types/auto_increment.md) value with [ALGORITHM](../../../sql-statements-and-structure/sql-statements/data-definition/alter/alter-table.md#algorithm) set to `NOCOPY` in the cases where the operation supports having the [ALGORITHM](../../../sql-statements-and-structure/sql-statements/data-definition/alter/alter-table.md#algorithm) clause set to `INSTANT`.

See [InnoDB Online DDL Operations with ALGORITHM=INSTANT: ALTER TABLE ... AUTO_INCREMENT=...](/en/innodb-online-ddl-operations-with-algorithminstant/#alter-table-auto_increment) for more information.

This applies to [ALTER TABLE ... AUTO_INCREMENT=...](../../../sql-statements-and-structure/sql-statements/data-definition/create/create-tablespace.md#auto_increment) for [InnoDB](../../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/innodb-encryption/innodb-encryption-troubleshooting.md) tables.

#

## `ALTER TABLE ... ROW_FORMAT=...`

InnoDB does **not** support changing a table's [row format](/en/innodb-storage-formats/) with [ALGORITHM](../../../sql-statements-and-structure/sql-statements/data-definition/alter/alter-table.md#algorithm) set to `NOCOPY`.

For example:

```
CREATE OR REPLACE TABLE tab (
 a int PRIMARY KEY,
 b varchar(50),
 c varchar(50)
) ROW_FORMAT=DYNAMIC;

SET SESSION alter_algorithm='NOCOPY';
ALTER TABLE tab ROW_FORMAT=COMPRESSED;
ERROR 1846 (0A000): ALGORITHM=NOCOPY is not supported. Reason: Changing table options requires the table to be rebuilt. Try ALGORITHM=INPLACE
```

This applies to [ALTER TABLE ... ROW_FORMAT=...](../../../sql-statements-and-structure/sql-statements/data-definition/create/create-tablespace.md#row_format) for [InnoDB](../../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/innodb-encryption/innodb-encryption-troubleshooting.md) tables.

#

## `ALTER TABLE ... KEY_BLOCK_SIZE=...`

InnoDB does **not** support changing a table's [KEY_BLOCK_SIZE](/en/innodb-storage-formats/#using-the-compressed-row-format) with [ALGORITHM](../../../sql-statements-and-structure/sql-statements/data-definition/alter/alter-table.md#algorithm) set to `NOCOPY`.

For example:

```
CREATE OR REPLACE TABLE tab (
 a int PRIMARY KEY,
 b varchar(50),
 c varchar(50)
) ROW_FORMAT=COMPRESSED
 KEY_BLOCK_SIZE=4;

SET SESSION alter_algorithm='NOCOPY';
ALTER TABLE tab KEY_BLOCK_SIZE=2;
ERROR 1846 (0A000): ALGORITHM=NOCOPY is not supported. Reason: Changing table options requires the table to be rebuilt. Try ALGORITHM=INPLACE
```

This applies to [KEY_BLOCK_SIZE=...](../../../sql-statements-and-structure/sql-statements/data-definition/create/create-tablespace.md#key_block_size) for [InnoDB](../../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/innodb-encryption/innodb-encryption-troubleshooting.md) tables.

#

## `ALTER TABLE ... PAGE_COMPRESSED=1` and `ALTER TABLE ... PAGE_COMPRESSION_LEVEL=...`

In [MariaDB 10.3.10](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-10310-release-notes) and later, InnoDB supports setting a table's [PAGE_COMPRESSED](../../../sql-statements-and-structure/sql-statements/data-definition/create/create-tablespace.md#page_compressed) value to `1` with [ALGORITHM](../../../sql-statements-and-structure/sql-statements/data-definition/alter/alter-table.md#algorithm) set to `NOCOPY` in the cases where the operation supports having the [ALGORITHM](../../../sql-statements-and-structure/sql-statements/data-definition/alter/alter-table.md#algorithm) clause set to `INSTANT`.

InnoDB does **not** support changing a table's [PAGE_COMPRESSED](../../../sql-statements-and-structure/sql-statements/data-definition/create/create-tablespace.md#page_compressed) value from `1` to `0` with [ALGORITHM](../../../sql-statements-and-structure/sql-statements/data-definition/alter/alter-table.md#algorithm) set to `NOCOPY`.

In these versions, InnoDB also supports changing a table's [PAGE_COMPRESSION_LEVEL](../../../sql-statements-and-structure/sql-statements/data-definition/create/create-tablespace.md#page_compression_level) value with [ALGORITHM](../../../sql-statements-and-structure/sql-statements/data-definition/alter/alter-table.md#algorithm) set to `NOCOPY` in the cases where the operation supports having the [ALGORITHM](../../../sql-statements-and-structure/sql-statements/data-definition/alter/alter-table.md#algorithm) clause is set to `INSTANT`.

See [InnoDB Online DDL Operations with ALGORITHM=INSTANT: ALTER TABLE ... PAGE_COMPRESSED=1 and ALTER TABLE ... PAGE_COMPRESSION_LEVEL=...](/en/innodb-online-ddl-operations-with-algorithminstant/#alter-table-page_compressed1-and-alter-table-page_compression_level) for more information.

This applies to [ALTER TABLE ... PAGE_COMPRESSED=...](../../../sql-statements-and-structure/sql-statements/data-definition/create/create-tablespace.md#page_compressed) and [ALTER TABLE ... PAGE_COMPRESSION_LEVEL=...](../../../sql-statements-and-structure/sql-statements/data-definition/create/create-tablespace.md#page_compression_level) for [InnoDB](../../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/innodb-encryption/innodb-encryption-troubleshooting.md) tables.

#

## `ALTER TABLE ... DROP SYSTEM VERSIONING`

InnoDB does **not** support dropping [system versioning](../../../sql-statements-and-structure/temporal-tables/system-versioned-tables.md) from a table with [ALGORITHM](../../../sql-statements-and-structure/sql-statements/data-definition/alter/alter-table.md#algorithm) set to `NOCOPY`.

For example:

```
CREATE OR REPLACE TABLE tab (
 a int PRIMARY KEY,
 b varchar(50),
 c varchar(50)
) WITH SYSTEM VERSIONING;

SET SESSION alter_algorithm='NOCOPY';
ALTER TABLE tab DROP SYSTEM VERSIONING;
ERROR 1845 (0A000): ALGORITHM=NOCOPY is not supported for this operation. Try ALGORITHM=INPLACE
```

This applies to [ALTER TABLE ... DROP SYSTEM VERSIONING](../../../sql-statements-and-structure/sql-statements/data-definition/alter/alter-table.md#drop-system-versioning) for [InnoDB](../../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/innodb-encryption/innodb-encryption-troubleshooting.md) tables.

#

## `ALTER TABLE ... DROP CONSTRAINT`

In [MariaDB 10.3.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1036-release-notes) and later, InnoDB supports dropping a [CHECK](../../../sql-statements-and-structure/sql-statements/data-definition/constraint.md#check-constraints) constraint from a table with [ALGORITHM](../../../sql-statements-and-structure/sql-statements/data-definition/alter/alter-table.md#algorithm) set to `NOCOPY` in the cases where the operation supports having the [ALGORITHM](../../../sql-statements-and-structure/sql-statements/data-definition/alter/alter-table.md#algorithm) clause set to `INSTANT`.

See [InnoDB Online DDL Operations with ALGORITHM=INSTANT: ALTER TABLE ... DROP CONSTRAINT](/en/innodb-online-ddl-operations-with-algorithminstant/#alter-table-drop-constraint) for more information.

This applies to [ALTER TABLE ... DROP CONSTRAINT](../../../sql-statements-and-structure/sql-statements/data-definition/alter/alter-table.md#drop-constraint) for [InnoDB](../../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/innodb-encryption/innodb-encryption-troubleshooting.md) tables.

#

## `ALTER TABLE ... FORCE`

InnoDB does **not** support forcing a table rebuild with [ALGORITHM](../../../sql-statements-and-structure/sql-statements/data-definition/alter/alter-table.md#algorithm) set to `NOCOPY`.

For example:

```
CREATE OR REPLACE TABLE tab (
 a int PRIMARY KEY,
 b varchar(50),
 c varchar(50)
);

SET SESSION alter_algorithm='NOCOPY';
ALTER TABLE tab FORCE;
ERROR 1845 (0A000): ALGORITHM=NOCOPY is not supported for this operation. Try ALGORITHM=INPLACE
```

This applies to [ALTER TABLE ... FORCE](../../../sql-statements-and-structure/sql-statements/data-definition/alter/alter-table.md#force) for [InnoDB](../../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/innodb-encryption/innodb-encryption-troubleshooting.md) tables.

#

## `ALTER TABLE ... ENGINE=InnoDB`

InnoDB does **not** support forcing a table rebuild with [ALGORITHM](../../../sql-statements-and-structure/sql-statements/data-definition/alter/alter-table.md#algorithm) set to `NOCOPY`.

For example:

```
CREATE OR REPLACE TABLE tab (
 a int PRIMARY KEY,
 b varchar(50),
 c varchar(50)
);

SET SESSION alter_algorithm='NOCOPY';
ALTER TABLE tab ENGINE=InnoDB;
ERROR 1845 (0A000): ALGORITHM=NOCOPY is not supported for this operation. Try ALGORITHM=INPLACE
```

This applies to [ALTER TABLE ... ENGINE=InnoDB](../../../sql-statements-and-structure/sql-statements/data-definition/create/create-tablespace.md#storage-engine) for [InnoDB](../../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/innodb-encryption/innodb-encryption-troubleshooting.md) tables.

#

## `OPTIMIZE TABLE ...`

InnoDB does **not** support optimizing a table with with [ALGORITHM](../../../sql-statements-and-structure/sql-statements/data-definition/alter/alter-table.md#algorithm) set to `NOCOPY`.

For example:

```
CREATE OR REPLACE TABLE tab (
 a int PRIMARY KEY,
 b varchar(50),
 c varchar(50)
);

SHOW GLOBAL VARIABLES WHERE Variable_name IN('innodb_defragment', 'innodb_optimize_fulltext_only');
+-------------------------------+-------+
| Variable_name | Value |
+-------------------------------+-------+
| innodb_defragment | OFF |
| innodb_optimize_fulltext_only | OFF |
+-------------------------------+-------+
2 rows in set (0.001 sec)

SET SESSION alter_algorithm='NOCOPY';
OPTIMIZE TABLE tab;
+---------+----------+----------+-----------------------------------------------------------------------------+
| Table | Op | Msg_type | Msg_text |
+---------+----------+----------+-----------------------------------------------------------------------------+
| db1.tab | optimize | note | Table does not support optimize, doing recreate + analyze instead |
| db1.tab | optimize | error | ALGORITHM=NOCOPY is not supported for this operation. Try ALGORITHM=INPLACE |
| db1.tab | optimize | status | Operation failed |
+---------+----------+----------+-----------------------------------------------------------------------------+
3 rows in set, 1 warning (0.002 sec)
```

This applies to [OPTIMIZE TABLE](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/optimizing-tables/optimize-table.md) for [InnoDB](../../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/innodb-encryption/innodb-encryption-troubleshooting.md) tables.

#

## `ALTER TABLE ... RENAME TO` and `RENAME TABLE ...`

InnoDB supports renaming a table with [ALGORITHM](../../../sql-statements-and-structure/sql-statements/data-definition/alter/alter-table.md#algorithm) set to `NOCOPY` in the cases where the operation supports having the [ALGORITHM](../../../sql-statements-and-structure/sql-statements/data-definition/alter/alter-table.md#algorithm) clause set to `INSTANT`.

See [InnoDB Online DDL Operations with ALGORITHM=INSTANT: ALTER TABLE ... RENAME TO and RENAME TABLE ...](/en/innodb-online-ddl-operations-with-algorithminstant/#alter-table-rename-to-and-rename-table) for more information.

This applies to [ALTER TABLE ... RENAME TO](../../../sql-statements-and-structure/sql-statements/data-definition/alter/alter-table.md#rename-to) and [RENAME TABLE](../../../sql-statements-and-structure/sql-statements/data-definition/rename-table.md) for [InnoDB](../../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/innodb-encryption/innodb-encryption-troubleshooting.md) tables.

#

# Limitations

#

## Limitations Related to Generated (Virtual and Persistent/Stored) Columns

[Generated columns](../../../sql-statements-and-structure/sql-statements/data-definition/create/generated-columns.md) do not currently support online DDL for all of the same operations that are supported for "real" columns.

See [Generated (Virtual and Persistent/Stored) Columns: Statement Support](../../../sql-statements-and-structure/sql-statements/data-definition/create/generated-columns.md#statement-support) for more information on the limitations.