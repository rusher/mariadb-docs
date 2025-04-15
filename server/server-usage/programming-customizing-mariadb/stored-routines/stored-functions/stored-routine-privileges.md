
# Stored Routine Privileges

It's important to give careful thought to the privileges associated with [stored functions](README.md) and [stored procedures](../stored-procedures/README.md). The following is an explanation of how they work.


## Creating Stored Routines


* To create a stored routine, the `<code>[CREATE ROUTINE](../../../../reference/sql-statements-and-structure/sql-statements/account-management-sql-commands/grant.md#database-privileges)</code>` privilege is needed. The `<code>[SUPER](../../../../reference/sql-statements-and-structure/sql-statements/account-management-sql-commands/grant.md#global-privileges)</code>` privilege is required if a `<code>DEFINER</code>` is declared that's not the creator's account (see [DEFINER clause](#definer-clause) below). The `<code>SUPER</code>` privilege is also required if statement-based binary logging is used. See [Binary Logging of Stored Routines](../binary-logging-of-stored-routines.md) for more details.


## Altering Stored Routines


* To make changes to, or drop, a stored routine, the `<code>[ALTER ROUTINE](../../../../reference/sql-statements-and-structure/sql-statements/account-management-sql-commands/grant.md#function-privileges)</code>` privilege is needed. The creator of a routine is temporarily granted this privilege if they attempt to change or drop a routine they created, unless the [automatic_sp_privileges](../../../replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#automatic_sp_privileges) variable is set to `<code>0</code>` (it defaults to 1).
* The `<code>SUPER</code>` privilege is also required if statement-based binary logging is used. See [Binary Logging of Stored Routines](../binary-logging-of-stored-routines.md) for more details.


## Running Stored Routines


* To run a stored routine, the `<code>[EXECUTE](../../../../reference/sql-statements-and-structure/sql-statements/account-management-sql-commands/grant.md#procedure-privileges)</code>` privilege is needed. This is also temporarily granted to the creator if they attempt to run their routine unless the [automatic_sp_privileges](../../../replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#automatic_sp_privileges) variable is set to `<code>0</code>`.
* The `<code>[SQL SECURITY clause](#sql-security-clause)</code>` (by default `<code>DEFINER</code>`) specifies what privileges are used when a routine is called. If `<code>SQL SECURITY</code>` is `<code>INVOKER</code>`, the function body will be evaluated using the privileges of the user calling the function. If `<code>SQL SECURITY</code>` is `<code>DEFINER</code>`, the function body is always evaluated using the privileges of the definer account. `<code>DEFINER</code>` is the default. Thus, by default, users who can access the database associated with the stored routine can also run the routine, and potentially perform operations they wouldn't normally have permissions for.
* The creator of a routine is the account that ran the `<code>[CREATE FUNCTION](../../../../reference/sql-statements-and-structure/sql-statements/data-definition/create/create-function.md)</code>` or `<code>[CREATE PROCEDURE](../stored-procedures/create-procedure.md)</code>` statement, regardless of whether a `<code>DEFINER</code>` is provided. The definer is by default the creator unless otherwise specified.
* The server automatically changes the privileges in the [mysql.proc](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/the-mysql-database-tables/mysql-proc-table.md) table as required, but will not look out for manual changes.


### DEFINER Clause


If left out, the `<code>DEFINER</code>` is treated as the account that created the stored routine or view. If the account creating the routine has the `<code>SUPER</code>` privilege, another account can be specified as the `<code>DEFINER</code>`.


### SQL SECURITY Clause


This clause specifies the context the stored routine or view will run as. It can take two values - `<code>DEFINER</code>` or `<code>INVOKER</code>`. `<code>DEFINER</code>` is the account specified as the `<code>DEFINER</code>` when the stored routine or view was created (see the section above). `<code>INVOKER</code>` is the account invoking the routine or view.


As an example, let's assume a routine, created by a superuser who's specified as the `<code>DEFINER</code>`, deletes all records from a table. If `<code>SQL SECURITY=DEFINER</code>`, anyone running the routine, regardless of whether they have delete privileges, will be able to delete the records. If `<code>SQL SECURITY = INVOKER</code>`, the routine will only delete the records if the account invoking the routine has permission to do so.


`<code>INVOKER</code>` is usually less risky, as a user cannot perform any operations they're normally unable to. However, it's not uncommon for accounts to have relatively limited permissions, but be specifically granted access to routines, which are then invoked in the `<code>DEFINER</code>` context.


## Dropping Stored Routines


All privileges that are specific to a stored routine will be dropped when a [DROP FUNCTION](drop-function.md) or [DROP ROUTINE](https://mariadb.com/kb/en/drop-routine) is run. However, if a [CREATE OR REPLACE FUNCTION](../../../../reference/sql-statements-and-structure/sql-statements/data-definition/create/create-function.md) or [CREATE OR REPLACE PROCEDURE](../stored-procedures/create-procedure.md) is used to drop and replace and the routine, any privileges specific to that routine will not be dropped.


## See Also


* [Changing the DEFINER of MySQL stored routines etc.](https://mariadb.com/blog/changing-definer-mysql-stored-routines-etc) - maria.com post on what to do after you've dropped a user, and now want to change the DEFINER on all database objects that currently have it set to this dropped user.

