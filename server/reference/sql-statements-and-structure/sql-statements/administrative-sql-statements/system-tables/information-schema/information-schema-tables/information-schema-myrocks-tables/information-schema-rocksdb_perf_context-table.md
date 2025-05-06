
# Information Schema ROCKSDB_PERF_CONTEXT Table

The [Information Schema](../../README.md) `ROCKSDB_PERF_CONTEXT` table is included as part of the [MyRocks](../../../../../../../storage-engines/myrocks/README.md) storage engine and includes per-table/partition counters .


The `PROCESS` [privilege](../../../../../account-management-sql-commands/grant.md) is required to view the table.


It contains the following columns:



| Column | Description |
| --- | --- |
| Column | Description |
| TABLE_SCHEMA |  |
| TABLE_NAME |  |
| PARTITION_NAME |  |
| STAT_TYPE |  |
| VALUE |  |



Note: for multi-table queries, all counter increments are "billed" to the first table in the query:
[1018](https://github.com/facebook/mysql-5.6/issues/1018)


CC BY-SA / Gnu FDL

