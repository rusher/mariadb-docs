
# Information Schema COLUMN_PRIVILEGES Table

The [Information Schema](../../../../../../mariadb-internals/information-schema-plugins-show-and-flush-statements.md) `<code>COLUMN_PRIVILEGES</code>` table contains column privilege information derived from the `<code>[mysql.columns_priv](../../the-mysql-database-tables/mysql-columns_priv-table.md)</code>` grant table.


It has the following columns:



| Column | Description |
| --- | --- |
| Column | Description |
| GRANTEE | In the format user_name@host_name. |
| TABLE_CATALOG | Always def. |
| TABLE_SCHEMA | Database name. |
| TABLE_NAME | Table name. |
| COLUMN_NAME | Column name. |
| PRIVILEGE_TYPE | One of SELECT, INSERT, UPDATE or REFERENCES. |
| IS_GRANTABLE | Whether the user has the [GRANT OPTION](../../../../account-management-sql-commands/grant.md#the-grant-option-privilege) for this privilege. |



Similar information can be accessed with the `<code>[SHOW FULL COLUMNS](../../../show/show-columns.md)</code>` and `<code>[SHOW GRANTS](../../../show/show-grants.md)</code>` statements. See the `<code>[GRANT](../../../../account-management-sql-commands/grant.md)</code>` article for more about privileges.


This information is also stored in the `<code>[columns_priv](../../the-mysql-database-tables/mysql-columns_priv-table.md)</code>` table, in the `<code>mysql</code>` system database.


For a description of the privileges that are shown in this table, see [column privileges](../../../../account-management-sql-commands/grant.md#column-privileges).


## Example


In the following example, no column-level privilege has been explicitly assigned:


```
SELECT * FROM information_schema.COLUMN_PRIVILEGES;
Empty set
```
