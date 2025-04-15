
# Information Schema USER_PRIVILEGES Table

The [Information Schema](../../../../../../mariadb-internals/information-schema-plugins-show-and-flush-statements.md) `<code>USER_PRIVILEGES</code>` table contains global user privilege information derived from the [mysql.global_priv](../../the-mysql-database-tables/mysql-global_priv-table.md) grant table.


It contains the following columns:



| Column | Description |
| --- | --- |
| Column | Description |
| GRANTEE | In the format user_name@host_name. |
| TABLE_CATALOG | Always def. |
| PRIVILEGE_TYPE | The specific privilege, for example CREATE USER, RELOAD, SHUTDOWN, SELECT, INSERT, UPDATE or REFERENCES. |
| IS_GRANTABLE | Whether the user has the [GRANT OPTION](../../../../account-management-sql-commands/grant.md#the-grant-option-privilege) for this privilege. |



The database, table and column privileges returned here are the ones granted on all databases and tables, and by implication all columns.


Similar information can be accessed with the [SHOW GRANTS](../../../show/show-grants.md) statement. See the [GRANT](../../../../account-management-sql-commands/grant.md) article for more about privileges.


This information is also stored in the [mysql.global_priv](../../the-mysql-database-tables/mysql-global_priv-table.md) table, in the `<code>mysql</code>` system database.

