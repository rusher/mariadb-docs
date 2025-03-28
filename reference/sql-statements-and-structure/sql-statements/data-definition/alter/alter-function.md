# ALTER FUNCTION

#

# Syntax

```
ALTER FUNCTION func_name [characteristic ...]

characteristic:
 { CONTAINS SQL | NO SQL | READS SQL DATA | MODIFIES SQL DATA }
 | SQL SECURITY { DEFINER | INVOKER }
 | COMMENT 'string'
```

#

# Description

This statement can be used to change the characteristics of a stored
function. More than one change may be specified in an `ALTER FUNCTION`
statement. However, you cannot change the parameters or body of a
stored function using this statement; to make such changes, you must
drop and re-create the function using [DROP FUNCTION](../../../../../server-usage/programming-customizing-mariadb/user-defined-functions/drop-function-udf.md) and [CREATE FUNCTION](../../../../../server-usage/programming-customizing-mariadb/user-defined-functions/create-function-udf.md).

You must have the `ALTER ROUTINE` privilege for the function. (That
privilege is granted automatically to the function creator.) If binary
logging is enabled, the `ALTER FUNCTION` statement might also require
the `SUPER` privilege, as described in [Binary Logging of Stored Routines](../../../../../server-usage/programming-customizing-mariadb/stored-routines/binary-logging-of-stored-routines.md).

#

# Example

```
ALTER FUNCTION hello SQL SECURITY INVOKER;
```

#

# See Also

* [CREATE FUNCTION](../../../../../server-usage/programming-customizing-mariadb/user-defined-functions/create-function-udf.md)
* [SHOW CREATE FUNCTION](../../administrative-sql-statements/show/show-create-function.md)
* [DROP FUNCTION](../../../../../server-usage/programming-customizing-mariadb/user-defined-functions/drop-function-udf.md)
* [SHOW FUNCTION STATUS](../../administrative-sql-statements/show/show-function-status.md)
* [Information Schema ROUTINES Table](../../administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-routines-table.md)