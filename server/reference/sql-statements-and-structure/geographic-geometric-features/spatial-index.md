
# SPATIAL INDEX


## Description


On [MyISAM](../../storage-engines/myisam-storage-engine/myisam-system-variables.md), [Aria](../../storage-engines/s3-storage-engine/aria_s3_copy.md) and [InnoDB](../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/innodb-upgrade-tests/README.md) tables, MariaDB can create spatial indexes (an R-tree index) using syntax similar to that for creating regular indexes, but extended with the `SPATIAL` keyword.
Currently, columns in spatial indexes must be declared `NOT NULL`.


Spatial indexes can be created when the table is created, or added after the fact like so:


* with [CREATE TABLE](../vectors/create-table-with-vectors.md): 
```
CREATE TABLE geom (g GEOMETRY NOT NULL, SPATIAL INDEX(g));
```
* with [ALTER TABLE](../sql-statements/data-definition/alter/alter-tablespace.md): 
```
ALTER TABLE geom ADD SPATIAL INDEX(g);
```
* with [CREATE INDEX](../sql-statements/data-definition/create/create-index.md): 
```
CREATE SPATIAL INDEX sp_index ON geom (g);
```


`SPATIAL INDEX` creates an `R-tree` index. For storage
engines that support non-spatial indexing of spatial columns, the engine
creates a `B-tree` index. A `B-tree` index on spatial values is useful for
exact-value lookups, but not for range scans.


For more information on indexing spatial columns, see [CREATE INDEX](../sql-statements/data-definition/create/create-index.md).


To drop spatial indexes, use [ALTER TABLE](../sql-statements/data-definition/alter/alter-tablespace.md) or [DROP INDEX](../sql-statements/data-definition/drop/drop-index.md):


* with [ALTER TABLE](../sql-statements/data-definition/alter/alter-tablespace.md): 
```
ALTER TABLE geom DROP INDEX g;
```
* with [DROP INDEX](../sql-statements/data-definition/drop/drop-index.md): 
```
DROP INDEX sp_index ON geom;
```


### Data-at-Rest Encyption


Before [MariaDB 10.4.3](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-4-series/mariadb-1043-release-notes.md), InnoDB's spatial indexes could not be [encrypted](../../mariadb-internals/encryption-plugin-api.md). If an InnoDB table was encrypted and if it contained spatial indexes, then those indexes would be unencrypted.


In [MariaDB 10.4.3](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-4-series/mariadb-1043-release-notes.md) and later, if `[innodb_checksum_algorithm](../../storage-engines/innodb/innodb-system-variables.md#innodb_checksum_algorithm)` is set to `full_crc32` or `strict_full_crc32`, and if the table does not use `[ROW_FORMAT=COMPRESSED](../../storage-engines/innodb/innodb-row-formats/innodb-row-formats-overview.md)`, then InnoDB spatial indexes will be encrypted if the table is encrypted.


See [MDEV-12026](https://jira.mariadb.org/browse/MDEV-12026) for more information.

