# Information Schema COLUMN\_PRIVILEGES Table

The [Information Schema](../) `COLUMN_PRIVILEGES` table contains column privilege information derived from the `[mysql.columns_priv](../../the-mysql-database-tables/mysql-columns_priv-table.md)` grant table.

It has the following columns:

| Column          | Description                                                                                                                                    |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| Column          | Description                                                                                                                                    |
| GRANTEE         | In the format user\_name@host\_name.                                                                                                           |
| TABLE\_CATALOG  | Always def.                                                                                                                                    |
| TABLE\_SCHEMA   | Database name.                                                                                                                                 |
| TABLE\_NAME     | Table name.                                                                                                                                    |
| COLUMN\_NAME    | Column name.                                                                                                                                   |
| PRIVILEGE\_TYPE | One of SELECT, INSERT, UPDATE or REFERENCES.                                                                                                   |
| IS\_GRANTABLE   | Whether the user has the [GRANT OPTION](../../../../account-management-sql-statements/grant.md#the-grant-option-privilege) for this privilege. |

Similar information can be accessed with the `[SHOW FULL COLUMNS](../../../show/show-columns.md)` and `[SHOW GRANTS](../../../show/show-grants.md)` statements. See the `[GRANT](../../../../account-management-sql-commands/grant.md)` article for more about privileges.

This information is also stored in the `[columns_priv](../../the-mysql-database-tables/mysql-columns_priv-table.md)` table, in the `mysql` system database.

For a description of the privileges that are shown in this table, see [column privileges](../../../../account-management-sql-statements/grant.md#column-privileges).

## Example

In the following example, no column-level privilege has been explicitly assigned:

```
SELECT * FROM information_schema.COLUMN_PRIVILEGES;
Empty set
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
