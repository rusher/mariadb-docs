# Information Schema XTRADB_RSEG Table

The [Information Schema](/en/information_schema/) `XTRADB_RSEG` table contains information about the XtraDB rollback segments.

The `PROCESS` [privilege](../../../../../account-management-sql-commands/grant.md) is required to view the table.

It has the following columns:

| Column | Description |
| --- | --- |
| Column | Description |
| rseg_id | Rollback segment id. |
| space_id | Space where the segment is placed. |
| zip_size | Size in bytes of the compressed page size, or zero if uncompressed. |
| page_no | Page number of the segment header. |
| max_size | Maximum size in pages. |
| curr_size | Current size in pages. |

The number of records will match the value set in the `[innodb_undo_logs](/en/xtradbinnodb-server-system-variables/#innodb_undo_logs)` variable (by default 128).