# mysql.host Table

### Usage

Until [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5), the `mysql.host` table contained information about hosts and their related privileges. When determining permissions, if a matching record in the [mysql.db table](../mysql-db-table.md) had a blank host value, the mysql.host table would be examined.

This table is not affected by any [GRANT](../../../../account-management-sql-statements/grant.md) statements, and had to be updated manually.

This table is no longer used.

See [privileges](../../../../account-management-sql-statements/grant.md) for a more complete view of the MariaDB privilege system.

This table is no longer created. However if the table is created it will be used.

### Table fields

The `mysql.host` table contains the following fields:

| Field                    | Type          | Null | Key | Default | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ------------------------ | ------------- | ---- | --- | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Host                     | char(60)      | NO   | PRI |         | Host (together with Db makes up the unique identifier for this record.                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Db                       | char(64)      | NO   | PRI |         | Database (together with Host makes up the unique identifier for this record.                                                                                                                                                                                                                                                                                                                                                                                                              |
| Select\_priv             | enum('N','Y') | NO   |     | N       | Can perform [SELECT](../../../../data-manipulation/selecting-data/select.md) statements.                                                                                                                                                                                                                                                                                                                                                                                                  |
| Insert\_priv             | enum('N','Y') | NO   |     | N       | Can perform [INSERT](../../../../data-manipulation/inserting-loading-data/insert.md) statements.                                                                                                                                                                                                                                                                                                                                                                                          |
| Update\_priv             | enum('N','Y') | NO   |     | N       | Can perform [UPDATE](../../../../data-manipulation/changing-deleting-data/update.md) statements.                                                                                                                                                                                                                                                                                                                                                                                          |
| Delete\_priv             | enum('N','Y') | NO   |     | N       | Can perform [DELETE](../../../../data-manipulation/changing-deleting-data/delete.md) statements.                                                                                                                                                                                                                                                                                                                                                                                          |
| Create\_priv             | enum('N','Y') | NO   |     | N       | Can [CREATE TABLEs](../../../../data-definition/create/create-table.md).                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Drop\_priv               | enum('N','Y') | NO   |     | N       | Can [DROP DATABASEs](../../../../data-definition/drop/drop-database.md) or [DROP TABLEs](../../../../data-definition/drop/drop-table.md).                                                                                                                                                                                                                                                                                                                                                 |
| Grant\_priv              | enum('N','Y') | NO   |     | N       | User can [grant](../../../../account-management-sql-statements/grant.md) privileges they possess.                                                                                                                                                                                                                                                                                                                                                                                         |
| References\_priv         | enum('N','Y') | NO   |     | N       | Unused                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Index\_priv              | enum('N','Y') | NO   |     | N       | Can create an index on a table using the [CREATE INDEX](../../../../data-definition/create/create-index.md) statement. Without the INDEX privilege, user can still create indexes when creating a table using the [CREATE TABLE](../../../../data-definition/create/create-table.md) statement if the user has have the CREATE privilege, and user can create indexes using the [ALTER TABLE](../../../../data-definition/alter/alter-table/) statement if they have the ALTER privilege. |
| Alter\_priv              | enum('N','Y') | NO   |     | N       | Can perform [ALTER TABLE](../../../../data-definition/alter/alter-table/) statements.                                                                                                                                                                                                                                                                                                                                                                                                     |
| Create\_tmp\_table\_priv | enum('N','Y') | NO   |     | N       | Can create temporary tables with the [CREATE TEMPORARY TABLE](../../../../data-definition/create/create-table.md) statement.                                                                                                                                                                                                                                                                                                                                                              |
| Lock\_tables\_priv       | enum('N','Y') | NO   |     | N       | Acquire explicit locks using the [LOCK TABLES](../../../../transactions/lock-tables.md) statement; user also needs to have the SELECT privilege on a table in order to lock it.                                                                                                                                                                                                                                                                                                           |
| Create\_view\_priv       | enum('N','Y') | NO   |     | N       | Can create a view using the [CREATE\_VIEW](../../../../../../server-usage/views/create-view.md) statement.                                                                                                                                                                                                                                                                                                                                                                                |
| Show\_view\_priv         | enum('N','Y') | NO   |     | N       | Can show the [CREATE VIEW](../../../../../../server-usage/views/create-view.md) statement to create a view using the [SHOW CREATE VIEW](../../../show/show-create-view.md) statement.                                                                                                                                                                                                                                                                                                     |
| Create\_routine\_priv    | enum('N','Y') | NO   |     | N       | Can create stored programs using the [CREATE PROCEDURE](../../../../../../server-usage/stored-routines/stored-procedures/create-procedure.md) and [CREATE FUNCTION](../../../../data-definition/create/create-function.md) statements.                                                                                                                                                                                                                                                    |
| Alter\_routine\_priv     | enum('N','Y') | NO   |     | N       | Can change the characteristics of a stored function using the [ALTER FUNCTION](../../../../data-definition/alter/alter-function.md) statement.                                                                                                                                                                                                                                                                                                                                            |
| Execute\_priv            | enum('N','Y') | NO   |     | N       | Can execute [stored procedure](../../../../../../server-usage/stored-routines/stored-procedures/) or functions.                                                                                                                                                                                                                                                                                                                                                                           |
| Trigger\_priv            | enum('N','Y') | NO   |     | N       | Can execute [triggers](../../../../../../server-usage/triggers-events/triggers/) associated with tables the user updates, execute the [CREATE TRIGGER](../../../../../../server-usage/triggers-events/triggers/create-trigger.md) and [DROP TRIGGER](../../../../data-definition/drop/drop-trigger.md) statements.                                                                                                                                                                        |

### How to Create

If you need the functionality to only allow access to your database from a given set of hosts, you can create the host table with the following command:

```
CREATE TABLE IF NOT EXISTS mysql.host (HOST CHAR(60) BINARY DEFAULT '' NOT NULL,
Db CHAR(64) BINARY DEFAULT '' NOT NULL,
Select_priv ENUM('N','Y') COLLATE utf8_general_ci DEFAULT 'N' NOT NULL,
Insert_priv ENUM('N','Y') COLLATE utf8_general_ci DEFAULT 'N' NOT NULL,
Update_priv ENUM('N','Y') COLLATE utf8_general_ci DEFAULT 'N' NOT NULL,
Delete_priv ENUM('N','Y') COLLATE utf8_general_ci DEFAULT 'N' NOT NULL,
Create_priv ENUM('N','Y') COLLATE utf8_general_ci DEFAULT 'N' NOT NULL,
Drop_priv ENUM('N','Y') COLLATE utf8_general_ci DEFAULT 'N' NOT NULL,
Grant_priv ENUM('N','Y') COLLATE utf8_general_ci DEFAULT 'N' NOT NULL,
References_priv ENUM('N','Y') COLLATE utf8_general_ci DEFAULT 'N' NOT NULL,
Index_priv ENUM('N','Y') COLLATE utf8_general_ci DEFAULT 'N' NOT NULL,
Alter_priv ENUM('N','Y') COLLATE utf8_general_ci DEFAULT 'N' NOT NULL,
Create_tmp_table_priv ENUM('N','Y') COLLATE utf8_general_ci DEFAULT 'N' NOT NULL,
Lock_tables_priv ENUM('N','Y') COLLATE utf8_general_ci DEFAULT 'N' NOT NULL,
Create_view_priv ENUM('N','Y') COLLATE utf8_general_ci DEFAULT 'N' NOT NULL,
Show_view_priv ENUM('N','Y') COLLATE utf8_general_ci DEFAULT 'N' NOT NULL,
Create_routine_priv ENUM('N','Y') COLLATE utf8_general_ci DEFAULT 'N' NOT NULL,
Alter_routine_priv ENUM('N','Y') COLLATE utf8_general_ci DEFAULT 'N' NOT NULL,
Execute_priv ENUM('N','Y') COLLATE utf8_general_ci DEFAULT 'N' NOT NULL,
Trigger_priv ENUM('N','Y') COLLATE utf8_general_ci DEFAULT 'N' NOT NULL,
PRIMARY KEY /*Host*/ (HOST,Db) )
ENGINE=MyISAM CHARACTER SET utf8 COLLATE utf8_bin
COMMENT='Host privileges;  Merged with database privileges';
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
