# Information Schema INNODB\_CHANGED\_PAGES Table

The [Information Schema](../../) `INNODB_CHANGED_PAGES` Table contains data about modified pages from the bitmap file. It is updated at checkpoints by the log tracking thread parsing the log, so does not contain real-time data.

The number of records is limited by the value of the [innodb\_max\_changed\_pages](../../../../../../storage-engines/innodb/innodb-system-variables.md) system variable.

The `PROCESS` [privilege](../../../../../account-management-sql-statements/grant.md) is required to view the table.

It has the following columns:

| Column     | Description                                                           |
| ---------- | --------------------------------------------------------------------- |
| Column     | Description                                                           |
| SPACE\_ID  | Modified page space id                                                |
| PAGE\_ID   | Modified page id                                                      |
| START\_LSN | Interval start after which page was changed (equal to checkpoint LSN) |
| END\_LSN   | Interval end before which page was changed (equal to checkpoint LSN)  |

CC BY-SA / Gnu FDL
