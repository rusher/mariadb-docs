
# mysql.db Table

The `mysql.db` table contains information about database-level privileges. The table can be queried and although it is possible to directly update it, it is best to use [GRANT](../../../account-management-sql-commands/grant.md) for setting privileges.


Note that the MariaDB privileges occur at many levels. A user may not be granted a privilege at the database level, but may still have permission on a table level, for example. See [privileges](../../../account-management-sql-commands/grant.md) for a more complete view of the MariaDB privilege system.


This table uses the [Aria](../../../../../storage-engines/aria/README.md) storage engine.


The `mysql.db` table contains the following fields:



| Field | Type | Null | Key | Default | Description | Introduced |
| --- | --- | --- | --- | --- | --- | --- |
| Field | Type | Null | Key | Default | Description | Introduced |
| Host | char(60) | NO | PRI |  | Host (together with User and Db makes up the unique identifier for this record. Until [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5), if the host field was blank, the corresponding record in the [mysql.host](obsolete-mysql-database-tables/mysql-host-table.md) table would be examined. From [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0), a blank host field is the same as the % wildcard. |  |
| Db | char(64) | NO | PRI |  | Database (together with User and Host makes up the unique identifier for this record. |  |
| User | char(80) | NO | PRI |  | User (together with Host and Db makes up the unique identifier for this record. |  |
| Select_priv | enum('N','Y') | NO |  | N | Can perform [SELECT](../../../data-manipulation/selecting-data/select.md) statements. |  |
| Insert_priv | enum('N','Y') | NO |  | N | Can perform [INSERT](../../../data-manipulation/inserting-loading-data/insert.md) statements. |  |
| Update_priv | enum('N','Y') | NO |  | N | Can perform [UPDATE](../../../data-manipulation/changing-deleting-data/update.md) statements. |  |
| Delete_priv | enum('N','Y') | NO |  | N | Can perform [DELETE](../../../data-manipulation/changing-deleting-data/delete.md) statements. |  |
| Create_priv | enum('N','Y') | NO |  | N | Can [CREATE TABLE's](../../../data-definition/create/create-table.md). |  |
| Drop_priv | enum('N','Y') | NO |  | N | Can [DROP DATABASE's](../../../data-definition/drop/drop-database.md) or [DROP TABLE's](../../../data-definition/drop/drop-table.md). |  |
| Grant_priv | enum('N','Y') | NO |  | N | User can [grant](../../../account-management-sql-commands/grant.md) privileges they possess. |  |
| References_priv | enum('N','Y') | NO |  | N | Unused |  |
| Index_priv | enum('N','Y') | NO |  | N | Can create an index on a table using the [CREATE INDEX](../../../data-definition/create/create-index.md) statement. Without the INDEX privilege, user can still create indexes when creating a table using the [CREATE TABLE](../../../data-definition/create/create-table.md) statement if the user has have the CREATE privilege, and user can create indexes using the [ALTER TABLE](../../../data-definition/alter/alter-table.md) statement if they have the ALTER privilege. |  |
| Alter_priv | enum('N','Y') | NO |  | N | Can perform [ALTER TABLE](../../../data-definition/alter/alter-table.md) statements. |  |
| Create_tmp_table_priv | enum('N','Y') | NO |  | N | Can create temporary tables with the [CREATE TEMPORARY TABLE](../../../data-definition/create/create-table.md) statement. |  |
| Lock_tables_priv | enum('N','Y') | NO |  | N | Acquire explicit locks using the [LOCK TABLES](../../../transactions/lock-tables.md) statement; user also needs to have the SELECT privilege on a table in order to lock it. |  |
| Create_view_priv | enum('N','Y') | NO |  | N | Can create a view using the [CREATE_VIEW](../../../../../../server-usage/programming-customizing-mariadb/views/create-view.md) statement. |  |
| Show_view_priv | enum('N','Y') | NO |  | N | Can show the [CREATE VIEW](../../../../../../server-usage/programming-customizing-mariadb/views/create-view.md) statement to create a view using the [SHOW CREATE VIEW](../../show/show-create-view.md) statement. |  |
| Create_routine_priv | enum('N','Y') | NO |  | N | Can create stored programs using the [CREATE PROCEDURE](../../../../../../server-usage/programming-customizing-mariadb/stored-routines/stored-procedures/create-procedure.md) and [CREATE FUNCTION](../../../data-definition/create/create-function.md) statements. |  |
| Alter_routine_priv | enum('N','Y') | NO |  | N | Can change the characteristics of a stored function using the [ALTER FUNCTION](../../../data-definition/alter/alter-function.md) statement. |  |
| Execute_priv | enum('N','Y') | NO |  | N | Can execute [stored procedure](../../../../../../server-usage/programming-customizing-mariadb/stored-routines/stored-procedures/README.md) or functions. |  |
| Event_priv | enum('N','Y') | NO |  | N | Create, drop and alter [events](../../../../../../server-usage/programming-customizing-mariadb/triggers-events/event-scheduler/README.md). |  |
| Trigger_priv | enum('N','Y') | NO |  | N | Can execute [triggers](../../../../../../server-usage/programming-customizing-mariadb/triggers-events/triggers/README.md) associated with tables the user updates, execute the [CREATE TRIGGER](../../../../../../server-usage/programming-customizing-mariadb/triggers-events/triggers/create-trigger.md) and [DROP TRIGGER](../../../data-definition/drop/drop-trigger.md) statements. |  |
| Delete_history_priv | enum('N','Y') | NO |  | N | Can delete rows created through [system versioning](../../../../temporal-tables/system-versioned-tables.md). | [MariaDB 10.3.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/old-releases/release-notes-mariadb-10-3-series/mariadb-1035-release-notes) |



The [Acl_database_grants](../../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-status-variables.md#acl_database_grants) status variable, added in [MariaDB 10.1.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-4-release-notes), indicates how many rows the `mysql.db` table contains.

