
# mysql.tables_priv Table

**System tables should not normally be edited directly. Use the related SQL statements instead.**



The `<code>mysql.tables_priv</code>` table contains information about table-level privileges. The table can be queried and although it is possible to directly update it, it is best to use [GRANT](../../../account-management-sql-commands/grant.md) for setting privileges.


Note that the MariaDB privileges occur at many levels. A user may be granted a privilege at the table level, but may still not have permission on a database level, for example. See [privileges](../../../account-management-sql-commands/grant.md) for a more complete view of the MariaDB privilege system.


The [INFORMATION_SCHEMA.TABLE_PRIVILEGES](../information-schema/information-schema-tables/information-schema-table_privileges-table.md) table derives its contents from `<code>mysql.tables_priv</code>`.


This table uses the [Aria](../../../../../storage-engines/s3-storage-engine/aria_s3_copy.md) storage engine.


The `<code>mysql.tables_priv</code>` table contains the following fields:



| Field | Type | Null | Key | Default | Description |
| --- | --- | --- | --- | --- | --- |
| Field | Type | Null | Key | Default | Description |
| Host | char(60) | NO | PRI |  | Host (together with User, Db and Table_namemakes up the unique identifier for this record. |
| Db | char(64) | NO | PRI |  | Database (together with User, Host and Table_namemakes up the unique identifier for this record. |
| User | char(80) | NO | PRI |  | User (together with Host, Db and Table_namemakes up the unique identifier for this record. |
| Table_name | char(64) | NO | PRI |  | Table name (together with User, Db and Tablemakes up the unique identifier for this record. |
| Grantor | char(141) | NO | MUL |  |  |
| Timestamp | timestamp | NO |  | CURRENT_TIMESTAMP |  |
| Table_priv | set('Select', 'Insert', 'Update', 'Delete', 'Create', 'Drop', 'Grant', 'References', 'Index', 'Alter', 'Create View', 'Show view', 'Trigger', 'Delete versioning rows') | NO |  |  | The table privilege type. See [Table Privileges](../../../account-management-sql-commands/grant.md#table-privileges) for details. |
| Column_priv | set('Select', 'Insert', 'Update', 'References') | NO |  |  | The column privilege type. See [Column Privileges](../../../account-management-sql-commands/grant.md#column-privileges) for details. |



The [Acl_table_grants](../../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-status-variables.md#acl_table_grants) status variable indicates how many rows the `<code>mysql.tables_priv</code>` table contains.

