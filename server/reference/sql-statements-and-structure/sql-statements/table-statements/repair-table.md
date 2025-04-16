
# REPAIR TABLE

## Syntax


<= [MariaDB 11.4](../../../../../release-notes/mariadb-community-server/what-is-mariadb-114.md)


```
REPAIR [NO_WRITE_TO_BINLOG | LOCAL] TABLE
    tbl_name [, tbl_name] ...
    [QUICK] [EXTENDED] [USE_FRM]
```

>= [MariaDB 11.5](../../../../../release-notes/mariadb-community-server/what-is-mariadb-115.md)


```
REPAIR [NO_WRITE_TO_BINLOG | LOCAL] TABLE
    tbl_name [, tbl_name] ...
    [QUICK] [EXTENDED] [USE_FRM] [FORCE]
```


## Description


`REPAIR TABLE` repairs a possibly corrupted table. By default,
it has the same effect as


```
myisamchk --recover tbl_name
```

or


```
aria_chk --recover tbl_name
```

See [aria_chk](../../../../clients-and-utilities/aria-clients-and-utilities/aria_chk.md) and [myisamchk](../../../../clients-and-utilities/myisam-clients-and-utilities/myisamchk-table-information.md) for more.


`REPAIR TABLE` works for [Archive](../../../storage-engines/archive/README.md), [Aria](../../../storage-engines/s3-storage-engine/aria_s3_copy.md), [CSV](../../../storage-engines/csv/csv-overview.md) and [MyISAM](../../../storage-engines/myisam-storage-engine/myisam-system-variables.md) tables. For [InnoDB](../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/innodb-upgrade-tests/README.md), see [recovery modes](../../../storage-engines/innodb/innodb-troubleshooting/innodb-recovery-modes.md). For CSV, see also [Checking and Repairing CSV Tables](../../../storage-engines/csv/checking-and-repairing-csv-tables.md). For Archive, this statement also improves compression. If the storage engine does not support this statement, a warning is issued.


This statement requires [SELECT and INSERT privileges](../account-management-sql-commands/grant.md) for the table.


By default, `REPAIR TABLE` statements are written to the [binary log](../../../storage-engines/innodb/binary-log-group-commit-and-innodb-flushing-performance.md) and will be [replicated](../administrative-sql-statements/replication-statements/README.md). The `NO_WRITE_TO_BINLOG` keyword (`LOCAL` is an alias) will ensure the statement is not written to the binary log.


From [MariaDB 10.3.19](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-10319-release-notes.md), `REPAIR TABLE` statements are not logged to the binary log if [read_only](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#read_only) is set. See also [Read-Only Replicas](../../../../server-usage/replication-cluster-multi-master/standard-replication/read-only-replicas.md).


When an index is recreated, the storage engine may use a configurable buffer in the process. Incrementing the buffer speeds up the index creation. [Aria](../../../storage-engines/s3-storage-engine/aria_s3_copy.md) and [MyISAM](../../../storage-engines/myisam-storage-engine/myisam-system-variables.md) allocate a buffer whose size is defined by [aria_sort_buffer_size](../../../storage-engines/aria/aria-system-variables.md) or [myisam_sort_buffer_size](../../../storage-engines/myisam-storage-engine/myisam-system-variables.md), also used for [ALTER TABLE](../data-definition/alter/alter-tablespace.md).


### QUICK


When specified, `REPAIR TABLE` will not modify the data file, only attempting to repair the index file. The same behavior can be achieved with [myisamchk --recover --quick](../../../../clients-and-utilities/myisam-clients-and-utilities/myisamchk-table-information.md#repairing-tables).


### EXTENDED


Creates the index row by row rather than sorting and creating a single index. Similar to [myisamchk --safe-recover](../../../../clients-and-utilities/myisam-clients-and-utilities/myisamchk-table-information.md#repairing-tables).


### USE_FRM


For use only when the index file is missing or its header corrupted. MariaDB then attempts to recreate it using the .frm file. There is no equivalent [myisamchk](../../../../clients-and-utilities/myisam-clients-and-utilities/myisamchk-table-information.md) option.



##### MariaDB starting with [11.5](../../../../../release-notes/mariadb-community-server/what-is-mariadb-115.md)

### FORCE

The FORCE argument was added in [MariaDB 11.5](../../../../../release-notes/mariadb-community-server/what-is-mariadb-115.md) to allow one to first run internal repair to fix damaged blocks and then follow it with ALTER TABLE ([MDEV-33449](https://jira.mariadb.org/browse/MDEV-33449)).


### Partitioned Tables


`REPAIR TABLE` is also supported for [partitioned tables](../../../../server-management/partitioning-tables/README.md) with the [ALTER TABLE ... REPAIR PARTITION](../data-definition/alter/alter-tablespace.md) statement. However, the `USE_FRM` option cannot be used with this statement on a partitioned table. See [Repairing Partitions](../../../../server-management/partitioning-tables/partitioning-overview.md#repairing-partitions) for details.


### Progress Reporting


The [Aria](../../../storage-engines/s3-storage-engine/aria_s3_copy.md) storage engine supports [progress reporting](../../../mariadb-internals/using-mariadb-with-your-programs-api/progress-reporting.md) for this statement.


## See Also


* [mariadb-check](../../../../clients-and-utilities/mariadb-check.md)
* [aria_chk](../../../../clients-and-utilities/aria-clients-and-utilities/aria_chk.md)
* [myisamchk](../../../../clients-and-utilities/myisam-clients-and-utilities/myisamchk-table-information.md)

