
# OPTIMIZE TABLE

## Syntax


```
OPTIMIZE [NO_WRITE_TO_BINLOG | LOCAL] TABLE
    tbl_name [, tbl_name] ...
    [WAIT n | NOWAIT]
```


## Description


`OPTIMIZE TABLE` has two main functions. It can either be used to defragment tables, or to update the InnoDB fulltext index.


#### WAIT/NOWAIT


Set the lock wait timeout. See [WAIT and NOWAIT](../../../../ref/sql-statements-and-structure/sql-statements/transactions/wait-and-nowait.md).


### Defragmenting


`OPTIMIZE TABLE` works for [InnoDB](../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/innodb-upgrade-tests/README.md) (before [MariaDB 10.1.1](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-1-release-notes.md), only if the [innodb_file_per_table](../../../../ref/storage-engines/innodb/innodb-system-variables.md#innodb_file_per_table) server system variable is set), [Aria](../../../../ref/storage-engines/s3-storage-engine/aria_s3_copy.md), [MyISAM](../../../../ref/storage-engines/myisam-storage-engine/myisam-system-variables.md) and [ARCHIVE](../../../../ref/storage-engines/archive/README.md) tables, and should be used if you have deleted a large part of a table or if you have made many changes to a table with variable-length
rows (tables that have [VARCHAR](../../../../ref/data-types/string-data-types/varchar.md), [VARBINARY](../../../../ref/data-types/string-data-types/varbinary.md), [BLOB](../../../../ref/data-types/string-data-types/blob.md), or [TEXT](../../../../ref/data-types/string-data-types/text.md) columns). Deleted rows are maintained in a
linked list and subsequent `INSERT` operations reuse old row positions.


This statement requires [SELECT and INSERT privileges](../../../../ref/sql-statements-and-structure/sql-statements/account-management-sql-commands/grant.md) for the table.


By default, `OPTIMIZE TABLE` statements are written to the [binary log](../../../../ref/storage-engines/innodb/binary-log-group-commit-and-innodb-flushing-performance.md) and will be [replicated](../../../../ref/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/README.md). The `NO_WRITE_TO_BINLOG` keyword (`LOCAL` is an alias) will ensure the statement is not written to the binary log.


`OPTIMIZE TABLE` statements are not logged to the binary log if [read_only](../system-variables/server-system-variables.md#read_only) is set. See also [Read-Only Replicas](../../standard-replication/read-only-replicas.md).


`OPTIMIZE TABLE` is also supported for partitioned tables. You
can use 
`[ALTER TABLE](../../../../ref/sql-statements-and-structure/sql-statements/data-definition/alter/alter-tablespace.md) ... OPTIMIZE PARTITION` 
to optimize one or more partitions.


You can use `OPTIMIZE TABLE` to reclaim the unused
space and to defragment the data file. With other storage engines, `OPTIMIZE TABLE` does nothing by default, and returns this message: " The storage engine for the table doesn't support optimize". However, if the server has been started with the `--skip-new` option, `OPTIMIZE TABLE` is linked to [ALTER TABLE](../../../../ref/sql-statements-and-structure/sql-statements/data-definition/alter/alter-tablespace.md), and recreates the table. This operation frees the unused space and updates index statistics.


The [Aria](../../../../ref/storage-engines/s3-storage-engine/aria_s3_copy.md) storage engine supports [progress reporting](../../../../ref/mariadb-internals/using-mariadb-with-your-programs-api/progress-reporting.md) for this statement.


If a [MyISAM](../../../../ref/storage-engines/myisam-storage-engine/myisam-system-variables.md) table is fragmented, [concurrent inserts](../../../../ref/sql-statements-and-structure/sql-statements/data-manipulation/inserting-loading-data/concurrent-inserts.md) will not be performed until an `OPTIMIZE TABLE` statement is executed on that table, unless the [concurrent_insert](../system-variables/server-system-variables.md#concurrent_insert) server system variable is set to `ALWAYS`.


### Updating an InnoDB fulltext index


When rows are added or deleted to an InnoDB [fulltext index](../optimization-and-indexes/full-text-indexes/README.md), the index is not immediately re-organized, as this can be an expensive operation. Change statistics are stored in a separate location . The fulltext index is only fully re-organized when an `OPTIMIZE TABLE` statement is run.


By default, an OPTIMIZE TABLE will defragment a table. In order to use it to update fulltext index statistics, the [innodb_optimize_fulltext_only](../../../../ref/storage-engines/innodb/innodb-system-variables.md#innodb_optimize_fulltext_only) system variable must be set to `1`. This is intended to be a temporary setting, and should be reset to `0` once the fulltext index has been re-organized.


Since fulltext re-organization can take a long time, the [innodb_ft_num_word_optimize](../../../../ref/storage-engines/innodb/innodb-system-variables.md#innodb_ft_num_word_optimize) variable limits the re-organization to a number of words (2000 by default). You can run multiple OPTIMIZE statements to fully re-organize the index.


### Defragmenting InnoDB tablespaces


[MariaDB 10.1.1](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-1-release-notes.md) merged the Facebook/Kakao defragmentation patch, allowing one to use `OPTIMIZE TABLE` to defragment InnoDB tablespaces. For this functionality to be enabled, the [innodb_defragment](../../../../ref/storage-engines/innodb/innodb-system-variables.md#innodb_defragment) system variable must be enabled. No new tables are created and there is no need to copy data from old tables to new tables. Instead, this feature loads `n` pages (determined by [innodb-defragment-n-pages](../../../../ref/storage-engines/innodb/innodb-system-variables.md#innodb_defragment_n_pages)) and tries to move records so that pages would be full of records and then frees pages that are fully empty after the operation. Note that tablespace files (including ibdata1) will not shrink as the result of defragmentation, but one will get better memory utilization in the InnoDB buffer pool as there are fewer data pages in use.


See [Defragmenting InnoDB Tablespaces](defragmenting-innodb-tablespaces.md) for more details.


## See Also


* [Optimize Table in InnoDB with ALGORITHM set to INPLACE](../../../../ref/storage-engines/innodb/innodb-online-ddl/innodb-online-ddl-operations-with-the-inplace-alter-algorithm.md#optimize-table)
* [Optimize Table in InnoDB with ALGORITHM set to NOCOPY](../../../../ref/storage-engines/innodb/innodb-online-ddl/innodb-online-ddl-operations-with-the-nocopy-alter-algorithm.md#optimize-table)
* [Optimize Table in InnoDB with ALGORITHM set to INSTANT](../../../../ref/storage-engines/innodb/innodb-online-ddl/innodb-online-ddl-operations-with-the-instant-alter-algorithm.md#optimize-table)

