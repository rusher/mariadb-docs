
# Information Schema ROCKSDB_DEADLOCK Table

The [Information Schema](../../../../../../../mariadb-internals/information-schema-plugins-show-and-flush-statements.md) `ROCKSDB_DEADLOCK` table is included as part of the [MyRocks](../../../../../../../storage-engines/myrocks/myrocks-in-mariadb-102-vs-mariadb-103.md) storage engine.


The `PROCESS` [privilege](../../../../../account-management-sql-commands/grant.md) is required to view the table.


It contains the following columns:



| Column | Description |
| --- | --- |
| Column | Description |
| DEADLOCK_ID |  |
| TIMESTAMP |  |
| TRANSACTION_ID |  |
| CF_NAME |  |
| WAITING_KEY |  |
| LOCK_TYPE |  |
| INDEX_NAME |  |
| TABLE_NAME |  |
| ROLLED_BACK |  |


