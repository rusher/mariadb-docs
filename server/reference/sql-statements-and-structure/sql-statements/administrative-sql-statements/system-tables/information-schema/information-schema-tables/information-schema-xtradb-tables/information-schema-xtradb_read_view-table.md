
# Information Schema XTRADB_READ_VIEW Table

The [Information Schema](../../README.md) `XTRADB_READ_VIEW` table contains information about the oldest active transaction in the system.


The `PROCESS` [privilege](../../../../../account-management-sql-commands/grant.md) is required to view the table.


It has the following columns:



| Column | Description |
| --- | --- |
| Column | Description |
| READ_VIEW_UNDO_NUMBER |  |
| READ_VIEW_LOW_LIMIT_TRX_NUMBER | Highest transaction number at the time the view was created. |
| READ_VIEW_UPPER_LIMIT_TRX_ID | Highest transaction ID at the time the view was created. Should not see newer transactions with IDs equal to or greater than the value. |
| READ_VIEW_LOW_LIMIT_TRX_ID | Latest committed transaction ID at the time the oldest view was created. Should see all transactions with IDs equal to or less than the value. |


