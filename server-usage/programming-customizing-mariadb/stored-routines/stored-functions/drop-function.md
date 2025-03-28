# DROP FUNCTION

#

# Syntax

```
DROP FUNCTION [IF EXISTS] f_name
```

#

# Description

The DROP FUNCTION statement is used to drop a [stored function](/en/stored-functions/) or a user-defined function (UDF). That is, the specified routine is removed from the server, along with all privileges specific to the function. You must have the `ALTER ROUTINE` [privilege](../../../../reference/sql-statements-and-structure/sql-statements/account-management-sql-commands/grant.md) for the routine in order to drop it. If the [automatic_sp_privileges](../../../replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#automatic_sp_privileges) server system variable is set, both the `ALTER ROUTINE` and `EXECUTE` privileges are granted automatically to the routine creator - see [Stored Routine Privileges](stored-routine-privileges.md).

#

### IF EXISTS

The `IF EXISTS` clause is a MySQL/MariaDB extension. It
prevents an error from occurring if the function does not exist. A
`NOTE` is produced that can be viewed with [SHOW WARNINGS](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-warnings.md).

For dropping a [user-defined functions](../../user-defined-functions/user-defined-functions-calling-sequences.md) (UDF), see [DROP FUNCTION UDF](../../user-defined-functions/drop-function-udf.md).

#

# Examples

```
DROP FUNCTION hello;
Query OK, 0 rows affected (0.042 sec)

DROP FUNCTION hello;
ERROR 1305 (42000): FUNCTION test.hello does not exist

DROP FUNCTION IF EXISTS hello;
Query OK, 0 rows affected, 1 warning (0.000 sec)

SHOW WARNINGS;
+-------+------+------------------------------------+
| Level | Code | Message |
+-------+------+------------------------------------+
| Note | 1305 | FUNCTION test.hello does not exist |
+-------+------+------------------------------------+
```

#

# See Also

* [DROP PROCEDURE](../stored-procedures/drop-procedure.md)
* [Stored Function Overview](stored-function-overview.md)
* [CREATE FUNCTION](../../user-defined-functions/create-function-udf.md)
* [CREATE FUNCTION UDF](../../user-defined-functions/create-function-udf.md)
* [ALTER FUNCTION](../../../../reference/sql-statements-and-structure/sql-statements/data-definition/alter/alter-function.md)
* [SHOW CREATE FUNCTION](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-create-function.md)
* [SHOW FUNCTION STATUS](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-function-status.md)
* [Stored Routine Privileges](stored-routine-privileges.md)
* [INFORMATION_SCHEMA ROUTINES Table](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-routines-table.md)