# Information Schema USER\_PRIVILEGES Table

The [Information Schema](../) `USER_PRIVILEGES` table contains global user privilege information derived from the [mysql.global\_priv](../../the-mysql-database-tables/mysql-global_priv-table.md) grant table.

It contains the following columns:

| Column          | Description                                                                                                                                    |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| Column          | Description                                                                                                                                    |
| GRANTEE         | In the format user\_name@host\_name.                                                                                                           |
| TABLE\_CATALOG  | Always def.                                                                                                                                    |
| PRIVILEGE\_TYPE | The specific privilege, for example CREATE USER, RELOAD, SHUTDOWN, SELECT, INSERT, UPDATE or REFERENCES.                                       |
| IS\_GRANTABLE   | Whether the user has the [GRANT OPTION](../../../../account-management-sql-statements/grant.md#the-grant-option-privilege) for this privilege. |

The database, table and column privileges returned here are the ones granted on all databases and tables, and by implication all columns.

Similar information can be accessed with the [SHOW GRANTS](../../../show/show-grants.md) statement. See the [GRANT](../../../../account-management-sql-statements/grant.md) article for more about privileges.

This information is also stored in the [mysql.global\_priv](../../the-mysql-database-tables/mysql-global_priv-table.md) table, in the `mysql` system database.

CC BY-SA / Gnu FDL

{% @marketo/form formId="4316" %}
