# Information Schema SCHEMA_PRIVILEGES Table

The [Information Schema](/en/information_schema/) `SCHEMA_PRIVILEGES` table contains information about [database privileges](../../../../account-management-sql-commands/grant.md#database-privileges).

It contains the following columns:

| Column | Description |
| --- | --- |
| Column | Description |
| GRANTEE | Account granted the privilege in the format user_name@host_name. |
| TABLE_CATALOG | Always def |
| TABLE_SCHEMA | Database name. |
| PRIVILEGE_TYPE | The granted privilege. |
| IS_GRANTABLE | Whether the privilege can be granted. |

The same information in a different format can be found in the `[mysql.db](/en/mysqldb-table/)` table.