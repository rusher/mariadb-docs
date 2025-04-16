
# mysql.procs_priv Table

**System tables should not normally be edited directly. Use the related SQL statements instead.**



The `mysql.procs_priv` table contains information about [stored procedure](../../../../../../server-usage/programming-customizing-mariadb/stored-routines/stored-procedures/README.md) and [stored function](../../../../../../server-usage/programming-customizing-mariadb/stored-routines/stored-functions/README.md) privileges. See [CREATE PROCEDURE](../../../../../../server-usage/programming-customizing-mariadb/stored-routines/stored-procedures/create-procedure.md) and [CREATE FUNCTION](../../../data-definition/create/create-function.md) on creating these.


The [INFORMATION_SCHEMA.ROUTINES](../information-schema/information-schema-tables/information-schema-routines-table.md) table derives its contents from `mysql.procs_priv`.


This table uses the [Aria](../../../../../storage-engines/s3-storage-engine/aria_s3_copy.md) storage engine.


The `mysql.procs_priv` table contains the following fields:



| Field | Type | Null | Key | Default | Description |
| --- | --- | --- | --- | --- | --- |
| Field | Type | Null | Key | Default | Description |
| Host | char(60) | NO | PRI |  | Host (together with Db, User, Routine_name and Routine_type makes up the unique identifier for this record). |
| Db | char(64) | NO | PRI |  | Database (together with Host, User, Routine_name and Routine_type makes up the unique identifier for this record). |
| User | char(80) | NO | PRI |  | User (together with Host, Db, Routine_name and Routine_type makes up the unique identifier for this record). |
| Routine_name | char(64) | NO | PRI |  | Routine_name (together with Host, Db User and Routine_type makes up the unique identifier for this record). |
| Routine_type | enum('FUNCTION','PROCEDURE', 'PACKAGE', 'PACKAGE BODY') | NO | PRI | NULL | Whether the routine is a [stored procedure](../../../../../../server-usage/programming-customizing-mariadb/stored-routines/stored-procedures/README.md), [stored function](../../../../../../server-usage/programming-customizing-mariadb/stored-routines/stored-functions/README.md), [package](../../../data-definition/create/create-package-body.md) or [package body](../../../data-definition/create/create-package-body.md). |
| Grantor | char(141) | NO | MUL |  |  |
| Proc_priv | set('Execute','Alter Routine','Grant') | NO |  |  | The routine privilege. See [Function Privileges](../../../account-management-sql-commands/grant.md#function-privileges) and [Procedure Privileges](../../../account-management-sql-commands/grant.md#procedure-privileges) for details. |
| Timestamp | timestamp | NO |  | CURRENT_TIMESTAMP |  |



The [Acl_function_grants](../../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-status-variables.md#acl_function_grants) status variable indicates how many rows the `mysql.columns_priv` table contains with the `FUNCTION` routine type.


The [Acl_procedure_grants](../../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-status-variables.md#acl_procedure_grants) status variable indicates how many rows the `mysql.columns_priv` table contains with the `PROCEDURE` routine type.

