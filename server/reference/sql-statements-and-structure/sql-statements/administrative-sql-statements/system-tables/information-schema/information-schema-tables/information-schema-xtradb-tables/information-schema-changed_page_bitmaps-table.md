
# Information Schema CHANGED_PAGE_BITMAPS Table

The [Information Schema](../../README.md) `CHANGED_PAGE_BITMAPS` table is a dummy table added to [XtraDB](../../../../../../../storage-engines/innodb/README.md) with reset_table callback to allow `FLUSH NO_WRITE_TO_BINLOG CHANGED_PAGE_BITMAPS` to be called from `innobackupex`. It contains only one column, *dummy*.


For more information, see [MDEV-7472](https://jira.mariadb.org/browse/MDEV-7472).


The `PROCESS` [privilege](../../../../../account-management-sql-commands/grant.md) is required to view the table.


CC BY-SA / Gnu FDL

