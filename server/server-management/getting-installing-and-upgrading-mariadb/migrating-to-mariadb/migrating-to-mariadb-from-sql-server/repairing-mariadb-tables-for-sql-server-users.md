
# Repairing MariaDB Tables for SQL Server Users


Repairing tables in MariaDB is not similar to repairing tables in SQL Server.


The first thing to understand is that every MariaDB table is handled by a [storage engine](understanding-mariadb-architecture.md#storage-engines). Storage engines are plugins that know how to physically read and write a table, so each storage engine allows one to repair tables in different ways. The default storage engine is [InnoDB](../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/innodb-upgrade-tests/README.md).


MariaDB provides specific SQL statements to deal with corrupted tables:


* [CHECK TABLE](../../../../reference/sql-statements-and-structure/sql-statements/table-statements/check-table.md) checks if a table is corrupted;
* [REPAIR TABLE](../../../../reference/sql-statements-and-structure/sql-statements/table-statements/repair-table.md) repairs a table if it is corrupted.


As a general rule, there is no reason why a table that is corrupted on a master should also be corrupted on the slaves. Therefore, `REPAIR` is generally used with the `NO_WRITE_TO_BINLOG` option, to avoid replicating it to the slaves.


## Partitioned Tables


[Partitioned tables](../../../partitioning-tables/README.md) are normally split into multiple physical files (one per partition). Even if one of the partitions is corrupted, in most cases other partitions are healthy.


For this reason, `CHECK TABLE` and `REPAIR TABLE` don't work on partitioned tables. Instead, use [ALTER TABLE](../../../../reference/sql-statements-and-structure/sql-statements/data-definition/alter/alter-tablespace.md) to check or repair a single partition.


For example:


```
ALTER TABLE orders CHECK PARTITION p_2019, p_2020;
ALTER TABLE orders REPAIR PARTITION p_2019, p_2020;
```

## Indexes


Indexes can get corrupted. However, as long as data is not corrupted, indexes can always be dropped and rebuilt with [ALTER TABLE](../../../../reference/sql-statements-and-structure/sql-statements/data-definition/alter/alter-tablespace.md):


```
ALTER TABLE customer DROP INDEX idx_email;
ALTER TABLE customer ADD INDEX idx_email (email);
```

## Checking and Repairing Tables


Here we discuss how to repair tables, depending on the storage engine.


### InnoDB


InnoDB follows the "fail fast" philosophy. If table corruption is detected, by default InnoDB deliberately causes MariaDB to crash to avoid corruption propagation, logging an error into the [error log](../../../server-monitoring-logs/error-log.md). This happens even if the corruption is found with a `CHECK TABLE` statement. This behavior can be changed with the [innodb_corrupt_table_action](../../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_corrupt_table_action) server variable.


To repair an InnoDB table after a crash:


1. Restart MariaDB with the `[--innodb-force-recovery](../../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_force_recovery)` option set to a low but non-zero value.
1. If MariaDB fails to start, retry with a higher value. Repeat until you succeed.


At this point, you can follow two different procedures, depending if you can use a backup or not. Provided that you have a usable backup, it is often the best option to bring the database up quickly. But if you want to reduce the data loss as much as possible, you prefer to follow the second method.


Restoring a backup:


1. Drop the whole database with [DROP DATABASE](../../../../reference/sql-statements-and-structure/sql-statements/data-definition/drop/drop-database.md).
1. Restore a backup of the database. The exact procedure depends on the [type of backup](mariadb-backups-overview-for-sql-server-users.md).


Recovering existing data:


1. Dump data from the corrupter table, ordered by primary key. MariaDB could crash when it finds damaged data. Repeat the process skipping damaged data.
1. Save somewhere the table structure with [SHOW CREATE TABLE](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-create-table.md).
1. Restart MariaDB.
1. Drop the table with [DROP TABLE](../../../../reference/sql-statements-and-structure/sql-statements/data-definition/drop/drop-tablespace.md).
1. Recreate the table and restore the dump.


For more details, see [InnoDB Recovery Modes](../../../../reference/storage-engines/innodb/innodb-troubleshooting/innodb-recovery-modes.md).


### Aria and MyISAM


[MyISAM](../../../../reference/storage-engines/myisam-storage-engine/README.md) is not crash-safe. In case of a MariaDB crash, the changes applied to MyISAM tables but not yet flushed to the disk are lost.


[Aria](../../../../reference/storage-engines/s3-storage-engine/aria_s3_copy.md) is crash-safe by default, which means that in case of a crash, after repairing any table that is damaged, no changes are lost. However, Aria tables are not crash-safe if created with `TRANSACTIONAL=0` or `ROW_FORMAT` set to `FIXED` or `DYNAMIC`.


System tables use the Aria storage engine and they are crash-safe.


To check if a MyISAM/Aria table is corrupted, we can use [CHECK TABLE](../../../../reference/sql-statements-and-structure/sql-statements/table-statements/check-table.md). To repair a MyISAM/Aria table, one can use [REPAIR TABLE](../../../../reference/sql-statements-and-structure/sql-statements/table-statements/repair-table.md). Before running `REPAIR TABLE` against big tables, consider increasing [myisam_repair_threads](../../../../reference/storage-engines/myisam-storage-engine/myisam-system-variables.md#myisam_repair_threads) or [aria_repair_threads](../../../../reference/storage-engines/aria/aria-system-variables.md#aria_repair_threads).


MyISAM and Aria tables can also be automatically repaired when corruption is detected. This is particularly useful for Aria, in case corrupted system tables prevent MariaDB from starting. See [myisam_recover_options](../../../../reference/storage-engines/myisam-storage-engine/myisam-system-variables.md#myisam_recover_options) and [aria_recover_options](../../../../reference/storage-engines/aria/aria-system-variables.md#aria_recover_options). By default Aria runs the quickest repair type. Occasionally, to repair a system table, we may have to start MariaDB in this way:


```
mysqld --aria-recover-options=BACKUP,FORCE
```

It is also possible to stop MariaDB and repair MyISAM tables with [myisamchk](../../../../clients-and-utilities/myisam-clients-and-utilities/myisamchk-table-information.md), and Aria tables with [aria_chk](../../../../clients-and-utilities/aria-clients-and-utilities/aria_chk.md). With default values, a repair can be unnecessarily very slow. Before running these tools, be sure to check the [Memory and Disk Use With myisamchk](../../../../clients-and-utilities/myisam-clients-and-utilities/memory-and-disk-use-with-myisamchk.md) page.


### Other Storage Engines


Notes on the different storage engines:


* For [MyRocks](../../../../reference/storage-engines/myrocks/myrocks-in-mariadb-102-vs-mariadb-103.md), see [MyRocks and CHECK TABLE](../../../../reference/storage-engines/myrocks/myrocks-and-check-table.md).
* With [ARCHIVE](../../../../reference/storage-engines/archive/README.md), `REPAIR TABLE` also improves the compression rate.
* For [CSV](../../../../reference/storage-engines/csv/csv-overview.md), see [Checking and Rpairing CSV Tables](../../../../reference/storage-engines/csv/checking-and-repairing-csv-tables.md).
* Some special storage engines, like [MEMORY](../../../../reference/storage-engines/memory-storage-engine.md) or [BLACKHOLE](../../../../reference/storage-engines/blackhole.md), do not support any form of check and repair.

<span></span>
