# Information Schema ROCKSDB_TRX Table

The [Information Schema](/en/information_schema/) `ROCKSDB_TRX` table is included as part of the [MyRocks](../../../../../../../storage-engines/myrocks/myrocks-and-replication.md) storage engine.

The `PROCESS` [privilege](../../../../../account-management-sql-commands/grant.md) is required to view the table.

It contains the following columns:

| Column | Description |
| --- | --- |
| Column | Description |
| TRANSACTION_ID | |
| STATE | |
| NAME | |
| WRITE_COUNT | |
| LOCK_COUNT | |
| TIMEOUT_SEC | |
| WAITING_KEY | |
| WAITING_COLUMN_FAMILY_ID | |
| IS_REPLICATION | |
| SKIP_TRX_API | |
| READ_ONLY | |
| HAS_DEADLOCK_DETECTION | |
| NUM_ONGOING_BULKLOAD | |
| THREAD_ID | |
| QUERY | |