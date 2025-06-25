# SHOW CREATE PROCEDURE

## Syntax

```sql
SHOW CREATE PROCEDURE proc_name
```

## Description

This statement is a MariaDB extension. It returns the exact string that\
can be used to re-create the named [stored procedure](../../../../server-usage/stored-routines/stored-procedures/), as well as the [SQL\_MODE](../../../../server-management/variables-and-modes/sql-mode.md) that was used when the trigger has been created and the character set used by the connection.. A similar statement, [SHOW CREATE FUNCTION](show-create-function.md), displays information about [stored functions](../../../../server-usage/stored-routines/stored-functions/).

Both statements require that:

* you are the owner of the routine;
* you have the [SHOW CREATE ROUTINE](../../account-management-sql-statements/grant.md#database-privileges) privilege (from [MariaDB 11.3.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-0-release-notes)); or
* have the [SELECT](../../account-management-sql-statements/grant.md) privilege on the [mysql.proc](../system-tables/the-mysql-database-tables/mysql-proc-table.md) table.

When none of the above statements are true, the statements display `NULL` for the `Create Procedure` or `Create Function` field.

**Warning** Users with `SELECT` privileges on [mysql.proc](../system-tables/the-mysql-database-tables/mysql-proc-table.md) or `USAGE` privileges on `*.*` can view the text of routines, even when they do not have privileges for the function or procedure itself.

`SHOW CREATE PROCEDURE` quotes identifiers according to the value of the [sql\_quote\_show\_create](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#sql_quote_show_create) system variable. Prior to [MariaDB 10.6.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-6-series/mariadb-1065-release-notes), [MariaDB 10.5.13](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/mariadb-10513-release-notes) and [MariaDB 10.4.22](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/mariadb-10422-release-notes), the output of this statement was unreliably affected by the [sql\_quote\_show\_create](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#sql_quote_show_create) system variable.

## Examples

Here's a comparison of the `SHOW CREATE PROCEDURE` and [SHOW CREATE FUNCTION](show-create-function.md) statements.

```sql
SHOW CREATE PROCEDURE test.simpleproc\G
*************************** 1. row ***************************
           Procedure: simpleproc
            sql_mode: 
    Create Procedure: CREATE PROCEDURE `simpleproc`(OUT param1 INT)
                      BEGIN
                      SELECT COUNT(*) INTO param1 FROM t;
                      END
character_set_client: latin1
collation_connection: latin1_swedish_ci
  Database Collation: latin1_swedish_ci

SHOW CREATE FUNCTION test.hello\G
*************************** 1. row ***************************
            Function: hello
            sql_mode:
     Create Function: CREATE FUNCTION `hello`(s CHAR(20))
                      RETURNS CHAR(50)
                      RETURN CONCAT('Hello, ',s,'!')
character_set_client: latin1
collation_connection: latin1_swedish_ci
  Database Collation: latin1_swedish_ci
```

When the user issuing the statement does not have privileges on the routine, attempting to [CALL](../../stored-routine-statements/call.md) the procedure raises Error 1370.

```bash
CALL test.prc1();
Error 1370 (42000): execute command denied to 
  user 'test_user'@'localhost' for routine 'test'.'prc1'
```

If the user neither has privilege to the routine nor the [SELECT](../../account-management-sql-statements/grant.md) privilege on [mysql.proc](../system-tables/the-mysql-database-tables/mysql-proc-table.md) table, it raises Error 1305, informing them that the procedure does not exist.

```sql
SHOW CREATE TABLES test.prc1\G
Error 1305 (42000): PROCEDURE prc1 does not exist
```

## See Also

* [Stored Procedure Overview](../../../../server-usage/stored-routines/stored-procedures/stored-procedure-overview.md)
* [CREATE PROCEDURE](../../../../server-usage/stored-routines/stored-procedures/create-procedure.md)
* [ALTER PROCEDURE](../../../../server-usage/stored-routines/stored-procedures/alter-procedure.md)
* [DROP PROCEDURE](../../../../server-usage/stored-routines/stored-procedures/drop-procedure.md)
* [SHOW PROCEDURE STATUS](show-procedure-status.md)
* [Stored Routine Privileges](../../../../server-usage/stored-routines/stored-functions/stored-routine-privileges.md)
* [Information Schema ROUTINES Table](../system-tables/information-schema/information-schema-tables/information-schema-routines-table.md)

<sub>_This page is licensed: GPLv2, originally from [fill\_help\_tables.sql](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)_</sub>

{% @marketo/form formId="4316" %}
