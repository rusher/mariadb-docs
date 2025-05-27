
# Information Schema INNODB_LOCK_WAITS Table

The [Information Schema](../../README.md) `INNODB_LOCK_WAITS` table contains information about blocked InnoDB transactions. The `PROCESS` [privilege](../../../../../account-management-sql-commands/grant.md) is required to view the table.


It contains the following columns:



| Column | Description |
| --- | --- |
| Column | Description |
| REQUESTING_TRX_ID | Requesting transaction ID from the [INNODB_TRX](information-schema-innodb_trx-table.md) table. |
| REQUESTED_LOCK_ID | Lock ID from the [INNODB.LOCKS](information-schema-innodb_locks-table.md) table for the waiting transaction. |
| BLOCKING_TRX_ID | Blocking transaction ID from the [INNODB_TRX](information-schema-innodb_trx-table.md) table. |
| BLOCKING_LOCK_ID | Lock ID from the [INNODB.LOCKS](information-schema-innodb_locks-table.md) table of a lock held by a transaction that is blocking another transaction. |



The table is often used in conjunction with the [INNODB_LOCKS](information-schema-innodb_locks-table.md) and [INNODB_TRX](information-schema-innodb_trx-table.md) tables to diagnose problematic locks and transactions.


CC BY-SA / Gnu FDL

