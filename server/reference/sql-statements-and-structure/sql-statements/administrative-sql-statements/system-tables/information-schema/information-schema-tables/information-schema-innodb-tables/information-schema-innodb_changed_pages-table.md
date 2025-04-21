
# Information Schema INNODB_CHANGED_PAGES Table

The [Information Schema](../../README.md) `INNODB_CHANGED_PAGES` Table contains data about modified pages from the bitmap file. It is updated at checkpoints by the log tracking thread parsing the log, so does not contain real-time data.


The number of records is limited by the value of the [innodb_max_changed_pages](../../../../../../../storage-engines/innodb/innodb-system-variables.md) system variable.


The `PROCESS` [privilege](../../../../../account-management-sql-commands/grant.md) is required to view the table.


It has the following columns:



| Column | Description |
| --- | --- |
| Column | Description |
| SPACE_ID | Modified page space id |
| PAGE_ID | Modified page id |
| START_LSN | Interval start after which page was changed (equal to checkpoint LSN) |
| END_LSN | Interval end before which page was changed (equal to checkpoint LSN) |


