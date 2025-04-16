
# ALTER PROCEDURE

## Syntax


```
ALTER PROCEDURE proc_name [characteristic ...]

characteristic:
    { CONTAINS SQL | NO SQL | READS SQL DATA | MODIFIES SQL DATA }
  | SQL SECURITY { DEFINER | INVOKER }
  | COMMENT 'string'
```

## Description


This statement can be used to change the characteristics of a [stored
procedure](README.md). More than one change may be specified in an `ALTER PROCEDURE`
statement. However, you cannot change the parameters or body of a
stored procedure using this statement. To make such changes, you must
drop and re-create the procedure using either [CREATE OR REPLACE PROCEDURE](create-procedure.md) (since [MariaDB 10.1.3](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-3-release-notes.md)) or [DROP PROCEDURE](drop-procedure.md) and [CREATE PROCEDURE](create-procedure.md) ([MariaDB 10.1.2](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-2-release-notes.md) and before).


You must have the `ALTER ROUTINE` privilege for the procedure. By default, that privilege is granted automatically to the procedure creator. See [Stored Routine Privileges](../stored-functions/stored-routine-privileges.md).


## Example


```
ALTER PROCEDURE simpleproc SQL SECURITY INVOKER;
```

## See Also


* [Stored Procedure Overview](stored-procedure-overview.md)
* [CREATE PROCEDURE](create-procedure.md)
* [SHOW CREATE PROCEDURE](../../../../ref/sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-create-procedure.md)
* [DROP PROCEDURE](drop-procedure.md)
* [SHOW CREATE PROCEDURE](../../../../ref/sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-create-procedure.md)
* [SHOW PROCEDURE STATUS](../../../../ref/sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-procedure-status.md)
* [Stored Routine Privileges](../stored-functions/stored-routine-privileges.md)
* [Information Schema ROUTINES Table](../../../../ref/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-routines-table.md)

