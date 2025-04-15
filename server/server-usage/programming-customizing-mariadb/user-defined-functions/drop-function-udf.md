
# DROP FUNCTION UDF

## Syntax


```
DROP FUNCTION [IF EXISTS] function_name
```


## Description


This statement drops the [user-defined function](user-defined-functions-security.md) (UDF) named `<code class="highlight fixed" style="white-space:pre-wrap">function_name</code>`.


To drop a function, you must have the `<code class="highlight fixed" style="white-space:pre-wrap">[DELETE privilege](../../../reference/sql-statements-and-structure/sql-statements/account-management-sql-commands/grant.md)</code>` for the mysql database. This is because `<code class="highlight fixed" style="white-space:pre-wrap">DROP FUNCTION</code>` removes the row from the [mysql.func](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/the-mysql-database-tables/mysql-func-table.md) system table that records the function's name, type and shared library name.


For dropping a stored function, see [DROP FUNCTION](../stored-routines/stored-functions/drop-function.md).


### Upgrading a UDF


To upgrade the UDF's shared library, first run a [DROP FUNCTION](../stored-routines/stored-functions/drop-function.md) statement, then upgrade the shared library and finally run the CREATE FUNCTION statement. If you upgrade without following this process, you may crash the server.


## Examples


```
DROP FUNCTION jsoncontains_path;
```

IF EXISTS:


```
DROP FUNCTION jsoncontains_path;
ERROR 1305 (42000): FUNCTION test.jsoncontains_path does not exist

DROP FUNCTION IF EXISTS jsoncontains_path;
Query OK, 0 rows affected, 1 warning (0.00 sec)

SHOW WARNINGS;
+-------+------+------------------------------------------------+
| Level | Code | Message                                        |
+-------+------+------------------------------------------------+
| Note  | 1305 | FUNCTION test.jsoncontains_path does not exist |
+-------+------+------------------------------------------------+
```
