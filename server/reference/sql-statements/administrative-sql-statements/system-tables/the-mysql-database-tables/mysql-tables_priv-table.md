# mysql.tables\_priv Table

**System tables should not normally be edited directly. Use the related SQL statements instead.**

The `mysql.tables_priv` table contains information about table-level privileges. The table can be queried and although it is possible to directly update it, it is best to use [GRANT](../../../account-management-sql-commands/grant.md) for setting privileges.

Note that the MariaDB privileges occur at many levels. A user may be granted a privilege at the table level, but may still not have permission on a database level, for example. See [privileges](../../../account-management-sql-commands/grant.md) for a more complete view of the MariaDB privilege system.

The [INFORMATION\_SCHEMA.TABLE\_PRIVILEGES](../information-schema/information-schema-tables/information-schema-table_privileges-table.md) table derives its contents from `mysql.tables_priv`.

This table uses the [Aria](../../../../storage-engines/aria/) storage engine.

The `mysql.tables_priv` table contains the following fields:

| Field        | Type                                                                                                                                                                    | Null | Key | Default            | Description                                                                                                                          |
| ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---- | --- | ------------------ | ------------------------------------------------------------------------------------------------------------------------------------ |
| Field        | Type                                                                                                                                                                    | Null | Key | Default            | Description                                                                                                                          |
| Host         | char(60)                                                                                                                                                                | NO   | PRI |                    | Host (together with User, Db and Table\_namemakes up the unique identifier for this record.                                          |
| Db           | char(64)                                                                                                                                                                | NO   | PRI |                    | Database (together with User, Host and Table\_namemakes up the unique identifier for this record.                                    |
| User         | char(80)                                                                                                                                                                | NO   | PRI |                    | User (together with Host, Db and Table\_namemakes up the unique identifier for this record.                                          |
| Table\_name  | char(64)                                                                                                                                                                | NO   | PRI |                    | Table name (together with User, Db and Tablemakes up the unique identifier for this record.                                          |
| Grantor      | char(141)                                                                                                                                                               | NO   | MUL |                    |                                                                                                                                      |
| Timestamp    | timestamp                                                                                                                                                               | NO   |     | CURRENT\_TIMESTAMP |                                                                                                                                      |
| Table\_priv  | set('Select', 'Insert', 'Update', 'Delete', 'Create', 'Drop', 'Grant', 'References', 'Index', 'Alter', 'Create View', 'Show view', 'Trigger', 'Delete versioning rows') | NO   |     |                    | The table privilege type. See [Table Privileges](../../../account-management-sql-commands/grant.md#table-privileges) for details.    |
| Column\_priv | set('Select', 'Insert', 'Update', 'References')                                                                                                                         | NO   |     |                    | The column privilege type. See [Column Privileges](../../../account-management-sql-commands/grant.md#column-privileges) for details. |

The [Acl\_table\_grants](../../../../../ha-and-performance/optimization-and-tuning/system-variables/server-status-variables.md#acl_table_grants) status variable indicates how many rows the `mysql.tables_priv` table contains.

CC BY-SA / Gnu FDL
