
# mysql.host Table


### Usage


Until [MariaDB 5.5](../../../../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5.md), the `<code>mysql.host</code>` table contained information about hosts and their related privileges. When determining permissions, if a matching record in the [mysql.db table](../mysql-db-table.md) had a blank host value, the mysql.host table would be examined.


This table is not affected by any [GRANT](../../../../account-management-sql-commands/grant.md) statements, and had to be updated manually.


This table is no longer used.


See [privileges](../../../../account-management-sql-commands/grant.md) for a more complete view of the MariaDB privilege system.


This table is no longer created. However if the table is created it will be used.


### Table fields


The `<code>mysql.host</code>` table contains the following fields:



| Field | Type | Null | Key | Default | Description |
| --- | --- | --- | --- | --- | --- |
| Field | Type | Null | Key | Default | Description |
| Host | char(60) | NO | PRI |  | Host (together with Db makes up the unique identifier for this record. |
| Db | char(64) | NO | PRI |  | Database (together with Host makes up the unique identifier for this record. |
| Select_priv | enum('N','Y') | NO |  | N | Can perform [SELECT](../../../../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/benchmarks-and-long-running-tests/benchmark-results/select-random-ranges-and-select-random-point.md) statements. |
| Insert_priv | enum('N','Y') | NO |  | N | Can perform [INSERT](../../../../built-in-functions/string-functions/insert-function.md) statements. |
| Update_priv | enum('N','Y') | NO |  | N | Can perform [UPDATE](../../../../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/tools/buildbot/buildbot-setup/buildbot-setup-for-virtual-machines/buildbot-setup-for-virtual-machines-additional-steps/update-debian-4-mirrors-for-buildbot-vms.md) statements. |
| Delete_priv | enum('N','Y') | NO |  | N | Can perform [DELETE](../../../../data-manipulation/changing-deleting-data/delete.md) statements. |
| Create_priv | enum('N','Y') | NO |  | N | Can [CREATE TABLEs](../../../../../vectors/create-table-with-vectors.md). |
| Drop_priv | enum('N','Y') | NO |  | N | Can [DROP DATABASEs](../../../../data-definition/drop/drop-database.md) or [DROP TABLEs](../../../../data-definition/drop/drop-tablespace.md). |
| Grant_priv | enum('N','Y') | NO |  | N | User can [grant](../../../../account-management-sql-commands/grant.md) privileges they possess. |
| References_priv | enum('N','Y') | NO |  | N | Unused |
| Index_priv | enum('N','Y') | NO |  | N | Can create an index on a table using the [CREATE INDEX](../../../../data-definition/create/create-index.md) statement. Without the INDEX privilege, user can still create indexes when creating a table using the [CREATE TABLE](../../../../../vectors/create-table-with-vectors.md) statement if the user has have the CREATE privilege, and user can create indexes using the [ALTER TABLE](../../../../data-definition/alter/alter-tablespace.md) statement if they have the ALTER privilege. |
| Alter_priv | enum('N','Y') | NO |  | N | Can perform [ALTER TABLE](../../../../data-definition/alter/alter-tablespace.md) statements. |
| Create_tmp_table_priv | enum('N','Y') | NO |  | N | Can create temporary tables with the [CREATE TEMPORARY TABLE](../../../../../vectors/create-table-with-vectors.md) statement. |
| Lock_tables_priv | enum('N','Y') | NO |  | N | Acquire explicit locks using the [LOCK TABLES](../../../../transactions/lock-tables.md) statement; user also needs to have the SELECT privilege on a table in order to lock it. |
| Create_view_priv | enum('N','Y') | NO |  | N | Can create a view using the [CREATE_VIEW](../../../../../../../server-usage/programming-customizing-mariadb/views/create-view.md) statement. |
| Show_view_priv | enum('N','Y') | NO |  | N | Can show the [CREATE VIEW](../../../../../../../server-usage/programming-customizing-mariadb/views/create-view.md) statement to create a view using the [SHOW CREATE VIEW](../../../show/show-create-view.md) statement. |
| Create_routine_priv | enum('N','Y') | NO |  | N | Can create stored programs using the [CREATE PROCEDURE](../../../../../../../server-usage/programming-customizing-mariadb/stored-routines/stored-procedures/create-procedure.md) and [CREATE FUNCTION](../../../../data-definition/create/create-function.md) statements. |
| Alter_routine_priv | enum('N','Y') | NO |  | N | Can change the characteristics of a stored function using the [ALTER FUNCTION](../../../../data-definition/alter/alter-function.md) statement. |
| Execute_priv | enum('N','Y') | NO |  | N | Can execute [stored procedure](../../../../../../../server-usage/programming-customizing-mariadb/stored-routines/stored-procedures/README.md) or functions. |
| Trigger_priv | enum('N','Y') | NO |  | N | Can execute [triggers](../../../../../../../server-usage/programming-customizing-mariadb/triggers-events/triggers/triggers-and-implicit-locks.md) associated with tables the user updates, execute the [CREATE TRIGGER](../../../../../../../server-usage/programming-customizing-mariadb/triggers-events/triggers/create-trigger.md) and [DROP TRIGGER](../../../../data-definition/drop/drop-trigger.md) statements. |


### How to Create

If you need the functionality to only allow access to your database from a given set of hosts, you can create the host table with the following command:

```
CREATE TABLE IF NOT EXISTS mysql.host (Host char(60) binary DEFAULT '' NOT NULL,
Db char(64) binary DEFAULT '' NOT NULL,
Select_priv enum('N','Y') COLLATE utf8_general_ci DEFAULT 'N' NOT NULL,
Insert_priv enum('N','Y') COLLATE utf8_general_ci DEFAULT 'N' NOT NULL,
Update_priv enum('N','Y') COLLATE utf8_general_ci DEFAULT 'N' NOT NULL,
Delete_priv enum('N','Y') COLLATE utf8_general_ci DEFAULT 'N' NOT NULL,
Create_priv enum('N','Y') COLLATE utf8_general_ci DEFAULT 'N' NOT NULL,
Drop_priv enum('N','Y') COLLATE utf8_general_ci DEFAULT 'N' NOT NULL,
Grant_priv enum('N','Y') COLLATE utf8_general_ci DEFAULT 'N' NOT NULL,
References_priv enum('N','Y') COLLATE utf8_general_ci DEFAULT 'N' NOT NULL,
Index_priv enum('N','Y') COLLATE utf8_general_ci DEFAULT 'N' NOT NULL,
Alter_priv enum('N','Y') COLLATE utf8_general_ci DEFAULT 'N' NOT NULL,
Create_tmp_table_priv enum('N','Y') COLLATE utf8_general_ci DEFAULT 'N' NOT NULL,
Lock_tables_priv enum('N','Y') COLLATE utf8_general_ci DEFAULT 'N' NOT NULL,
Create_view_priv enum('N','Y') COLLATE utf8_general_ci DEFAULT 'N' NOT NULL,
Show_view_priv enum('N','Y') COLLATE utf8_general_ci DEFAULT 'N' NOT NULL,
Create_routine_priv enum('N','Y') COLLATE utf8_general_ci DEFAULT 'N' NOT NULL,
Alter_routine_priv enum('N','Y') COLLATE utf8_general_ci DEFAULT 'N' NOT NULL,
Execute_priv enum('N','Y') COLLATE utf8_general_ci DEFAULT 'N' NOT NULL,
Trigger_priv enum('N','Y') COLLATE utf8_general_ci DEFAULT 'N' NOT NULL,
PRIMARY KEY /*Host*/ (Host,Db) )
engine=MyISAM CHARACTER SET utf8 COLLATE utf8_bin
comment='Host privileges;  Merged with database privileges';
```

