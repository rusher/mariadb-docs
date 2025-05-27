# Information Schema SCHEMA\_PRIVILEGES Table

The [Information Schema](../) `SCHEMA_PRIVILEGES` table contains information about [database privileges](../../../../account-management-sql-statements/grant.md#database-privileges).

It contains the following columns:

| Column          | Description                                                        |
| --------------- | ------------------------------------------------------------------ |
| Column          | Description                                                        |
| GRANTEE         | Account granted the privilege in the format user\_name@host\_name. |
| TABLE\_CATALOG  | Always def                                                         |
| TABLE\_SCHEMA   | Database name.                                                     |
| PRIVILEGE\_TYPE | The granted privilege.                                             |
| IS\_GRANTABLE   | Whether the privilege can be granted.                              |

The same information in a different format can be found in the `[mysql.db](../../the-mysql-database-tables/mysql-db-table.md)` table.

CC BY-SA / Gnu FDL
