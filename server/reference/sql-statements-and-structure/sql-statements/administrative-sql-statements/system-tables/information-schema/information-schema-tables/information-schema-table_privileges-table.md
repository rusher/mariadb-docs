
# Information Schema TABLE_PRIVILEGES Table

The [Information Schema](../README.md) `TABLE_PRIVILEGES` table contains table privilege information derived from the [mysql.tables_priv](../../the-mysql-database-tables/mysql-tables_priv-table.md) grant table.


It has the following columns:



| Column | Description |
| --- | --- |
| Column | Description |
| GRANTEE | In the format user_name@host_name. |
| TABLE_CATALOG | Always def. |
| TABLE_SCHEMA | Database name. |
| TABLE_NAME | Table name. |
| PRIVILEGE_TYPE | One of SELECT, INSERT, UPDATE, REFERENCES, ALTER, INDEX, DROP or CREATE VIEW. |
| IS_GRANTABLE | Whether the user has the [GRANT OPTION](../../../../account-management-sql-commands/grant.md#the-grant-option-privilege) for this privilege. |



Similar information can be accessed with the [SHOW GRANTS](../../../show/show-grants.md) statement. See the [GRANT](../../../../account-management-sql-commands/grant.md) article for more about privileges.


The table only shows privileges granted on the table level. This differs from the Sys Schema [privileges_by_table_by_level view](../../sys-schema/sys-schema-views/privileges_by_table_by_level-sys-schema-view.md), which shows all privileges, broken down by table.


For a description of the privileges that are shown in this table, see [table privileges](../../../../account-management-sql-commands/grant.md#table-privileges).


## See Also


* [sys.privileges_by_table_by_level](../../sys-schema/sys-schema-views/privileges_by_table_by_level-sys-schema-view.md)

