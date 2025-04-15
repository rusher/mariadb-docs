
# mysql.roles_mapping Table

**System tables should not normally be edited directly. Use the related SQL statements instead.**



The `<code>mysql.roles_mapping</code>` table contains information about mariaDB [roles](../../../../../../security/user-account-management/roles/roles_overview.md).


This table uses the [Aria](../../../../../storage-engines/s3-storage-engine/aria_s3_copy.md) storage engine.


The `<code>mysql.roles_mapping</code>` table contains the following fields:



| Field | Type | Null | Key | Default | Description |
| --- | --- | --- | --- | --- | --- |
| Field | Type | Null | Key | Default | Description |
| Host | char(60) | NO | PRI |  | Host (together with User and Role makes up the unique identifier for this record. |
| User | char(80) | NO | PRI |  | User (together with Host and Role makes up the unique identifier for this record. |
| Role | char(80) | NO | PRI |  | Role (together with Host and User makes up the unique identifier for this record. |
| Admin_option | enum('N','Y') | NO |  | N | Whether the role can be granted (see the [CREATE ROLE](../../../account-management-sql-commands/create-role.md) WITH ADMIN clause). |



The [Acl_role_grants](../../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-status-variables.md#acl_role_grants) status variable indicates how many rows the `<code>mysql.roles_mapping</code>` table contains.

