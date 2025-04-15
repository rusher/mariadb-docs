
# Information Schema ROCKSDB_TRX Table

The [Information Schema](../../../../../../../mariadb-internals/information-schema-plugins-show-and-flush-statements.md) `<code>ROCKSDB_TRX</code>` table is included as part of the [MyRocks](../../../../../../../storage-engines/myrocks/myrocks-in-mariadb-102-vs-mariadb-103.md) storage engine.


The `<code>PROCESS</code>` [privilege](../../../../../account-management-sql-commands/grant.md) is required to view the table.


It contains the following columns:



| Column | Description |
| --- | --- |
| Column | Description |
| TRANSACTION_ID |  |
| STATE |  |
| NAME |  |
| WRITE_COUNT |  |
| LOCK_COUNT |  |
| TIMEOUT_SEC |  |
| WAITING_KEY |  |
| WAITING_COLUMN_FAMILY_ID |  |
| IS_REPLICATION |  |
| SKIP_TRX_API |  |
| READ_ONLY |  |
| HAS_DEADLOCK_DETECTION |  |
| NUM_ONGOING_BULKLOAD |  |
| THREAD_ID |  |
| QUERY |  |


