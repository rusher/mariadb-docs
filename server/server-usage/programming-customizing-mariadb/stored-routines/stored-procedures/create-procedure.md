
# CREATE PROCEDURE

## Syntax


```
CREATE
    [OR REPLACE]
    [DEFINER = { user | CURRENT_USER | role | CURRENT_ROLE }]
    PROCEDURE [IF NOT EXISTS] sp_name ([proc_parameter[,...]])
    [characteristic ...] routine_body

proc_parameter:
    [ IN | OUT | INOUT ] param_name type

type:
    Any valid MariaDB data type

characteristic:
    LANGUAGE SQL
  | [NOT] DETERMINISTIC
  | { CONTAINS SQL | NO SQL | READS SQL DATA | MODIFIES SQL DATA }
  | SQL SECURITY { DEFINER | INVOKER }
  | COMMENT 'string'

routine_body:
    Valid SQL procedure statement
```


## Description


Creates a [stored procedure](README.md). By default, a routine is
associated with the default database. To associate the routine
explicitly with a given database, specify the name as db_name.sp_name
when you create it.


When the routine is invoked, an implicit USE db_name is performed (and
undone when the routine terminates). The causes the routine to have
the given default database while it executes. USE statements within
stored routines are disallowed.


When a stored procedure has been created, you invoke it by
using the `<code>CALL</code>` statement (see [CALL](../../../../reference/sql-statements-and-structure/sql-statements/stored-routine-statements/call.md)).


To execute the `<code>CREATE PROCEDURE</code>` statement, it is
necessary to have the `<code>CREATE ROUTINE</code>` privilege. By default, MariaDB
automatically grants the `<code>ALTER ROUTINE</code>` and `<code>EXECUTE</code>` privileges to the
routine creator. See also [Stored Routine Privileges](../stored-functions/stored-routine-privileges.md).


The `<code>DEFINER</code>` and SQL SECURITY clauses specify the security context to
be used when checking access privileges at routine execution time, as
described [here](../stored-functions/stored-routine-privileges.md). Requires the [SUPER](../../../../reference/sql-statements-and-structure/sql-statements/account-management-sql-commands/grant.md#super) privilege, or, from [MariaDB 10.5.2](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1052-release-notes.md), the [SET USER](../../../../reference/sql-statements-and-structure/sql-statements/account-management-sql-commands/grant.md#set-user) privilege.


If the routine name is the same as the name of a built-in SQL
function, you must use a space between the name and the following
parenthesis when defining the routine, or a syntax error occurs. This
is also true when you invoke the routine later. For this reason, we
suggest that it is better to avoid re-using the names of existing SQL
functions for your own stored routines.


The IGNORE_SPACE SQL mode applies to built-in functions, not to stored
routines. It is always allowable to have spaces after a routine name,
regardless of whether IGNORE_SPACE is enabled.


The parameter list enclosed within parentheses must always be present.
If there are no parameters, an empty parameter list of () should be
used. Parameter names are not case sensitive.


Each parameter can be declared to use any valid data type, except that
the COLLATE attribute cannot be used.


For valid identifiers to use as procedure names, see [Identifier Names](../../../../reference/sql-statements-and-structure/sql-language-structure/identifier-names.md).


### Things to be Aware of With CREATE OR REPLACE


* One can't use `<code class="highlight fixed" style="white-space:pre-wrap">OR REPLACE</code>` together with `<code class="highlight fixed" style="white-space:pre-wrap">IF EXISTS</code>`.


## CREATE PROCEDURE IF NOT EXISTS


If the `<code>IF NOT EXISTS</code>` clause is used, then the procedure will only be created if a procedure with the same name does not already exist. If the procedure already exists, then a warning will be triggered by default.


### IN/OUT/INOUT


Each parameter is an `<code>IN</code>` parameter by default. To specify otherwise for
a parameter, use the keyword `<code>OUT</code>` or `<code>INOUT</code>` before the parameter name.


An `<code>IN</code>` parameter passes a value into a procedure. The procedure might
modify the value, but the modification is not visible to the caller
when the procedure returns. An `<code>OUT</code>` parameter passes a value from the
procedure back to the caller. Its initial value is NULL within the
procedure, and its value is visible to the caller when the procedure
returns. An `<code>INOUT</code>` parameter is initialized by the caller, can be
modified by the procedure, and any change made by the procedure is
visible to the caller when the procedure returns.


For each `<code>OUT</code>` or `<code>INOUT</code>` parameter, pass a user-defined variable in the
`<code>CALL</code>` statement that invokes the procedure so that you can obtain its
value when the procedure returns. If you are calling the procedure
from within another stored procedure or function, you can also pass a
routine parameter or local routine variable as an `<code>IN</code>` or `<code>INOUT</code>`
parameter.


### DETERMINISTIC/NOT DETERMINISTIC


`<code>DETERMINISTIC</code>` and `<code>NOT DETERMINISTIC</code>` apply only to [functions](../stored-functions/README.md). Specifying `<code>DETERMINISTC</code>` or `<code>NON-DETERMINISTIC</code>` in procedures has no effect. The default value is `<code>NOT DETERMINISTIC</code>`. Functions are `<code>DETERMINISTIC</code>` when they always return the same value for the same input. For example, a truncate or substring function. Any function involving data, therefore, is always `<code>NOT DETERMINISTIC</code>`.


### CONTAINS SQL/NO SQL/READS SQL DATA/MODIFIES SQL DATA


`<code>CONTAINS SQL</code>`, `<code>NO SQL</code>`, `<code>READS SQL DATA</code>`, and `<code>MODIFIES SQL DATA</code>` are informative clauses that tell the server what the function does. MariaDB does not check in any way whether the specified clause is correct. If none of these clauses are specified, `<code>CONTAINS SQL</code>` is used by default.


`<code>MODIFIES SQL DATA</code>` means that the function contains statements that may modify data stored in databases. This happens if the function contains statements like [DELETE](../../../../reference/sql-statements-and-structure/sql-statements/data-manipulation/changing-deleting-data/delete.md), [UPDATE](../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/tools/buildbot/buildbot-setup/buildbot-setup-for-virtual-machines/buildbot-setup-for-virtual-machines-additional-steps/update-debian-4-mirrors-for-buildbot-vms.md), [INSERT](../../../../reference/sql-statements-and-structure/sql-statements/built-in-functions/string-functions/insert-function.md), [REPLACE](../../../../reference/sql-statements-and-structure/sql-statements/built-in-functions/string-functions/replace-function.md) or DDL.


`<code>READS SQL DATA</code>` means that the function reads data stored in databases, but does not modify any data. This happens if [SELECT](../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/benchmarks-and-long-running-tests/benchmark-results/select-random-ranges-and-select-random-point.md) statements are used, but there no write operations are executed.


`<code>CONTAINS SQL</code>` means that the function contains at least one SQL statement, but it does not read or write any data stored in a database. Examples include [SET](../../../../../connectors/mariadb-connector-cpp/setup-for-connector-cpp-examples.md) or [DO](../../../../../general-resources/company-and-community/contributing-participating/donate-to-the-foundation.md).


`<code>NO SQL</code>` means nothing, because MariaDB does not currently support any language other than SQL.


The routine_body consists of a valid SQL procedure statement. This can
be a simple statement such as [SELECT](../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/benchmarks-and-long-running-tests/benchmark-results/select-random-ranges-and-select-random-point.md) or [INSERT](../../../../reference/sql-statements-and-structure/sql-statements/built-in-functions/string-functions/insert-function.md), or it can be a
compound statement written using [BEGIN and END](../../programmatic-compound-statements/begin-end.md). Compound statements
can contain declarations, loops, and other control structure
statements. See [Programmatic and Compound Statements](../../programmatic-compound-statements/programmatic-compound-statements-cursors/README.md) for syntax details.


MariaDB allows routines to contain DDL statements, such as `<code>CREATE</code>` and
DROP. MariaDB also allows [stored procedures](README.md) (but not [stored functions](../stored-functions/README.md))
to contain SQL transaction statements such as `<code>COMMIT</code>`.


For additional information about statements that are not allowed in
stored routines, see [Stored Routine Limitations](../stored-routine-limitations.md).


### Invoking stored procedure from within programs


For information about invoking [stored procedures](README.md) from within programs written in a language that has a MariaDB/MySQL interface, see [CALL](../../../../reference/sql-statements-and-structure/sql-statements/stored-routine-statements/call.md).


### OR REPLACE


If the optional `<code>OR REPLACE</code>` clause is used, it acts as a shortcut for:


```
DROP PROCEDURE IF EXISTS name;
CREATE PROCEDURE name ...;
```

with the exception that any existing [privileges](../stored-functions/stored-routine-privileges.md) for the procedure are not dropped.


### sql_mode


MariaDB stores the [sql_mode](../../../replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#sql_mode) system variable setting that is in effect at the time a routine is created, and always executes the routine with this setting in force, regardless of the server [SQL mode](../../../../../release-notes/mariadb-community-server/compatibility-and-differences/sql_modemssql.md) in effect when the routine is invoked.


### Character Sets and Collations


Procedure parameters can be declared with any character set/collation. If the character set and collation are not specifically set, the database defaults at the time of creation will be used. If the database defaults change at a later stage, the stored procedure character set/collation will not be changed at the same time; the stored procedure needs to be dropped and recreated to ensure the same character set/collation as the database is used.


### Oracle Mode


A subset of Oracle's PL/SQL language is supported in addition to the traditional SQL/PSM-based MariaDB syntax. See [Oracle mode](../../../../../release-notes/mariadb-community-server/compatibility-and-differences/sql_modeoracle.md) for details on changes when running Oracle mode.


## Examples


The following example shows a simple stored procedure that uses an `<code>OUT</code>`
parameter. It uses the DELIMITER command to set a new delimiter for the duration of the process — see [Delimiters in the mariadb client](../../../../clients-and-utilities/mariadb-client/delimiters.md).


```
DELIMITER //

CREATE PROCEDURE simpleproc (OUT param1 INT)
 BEGIN
  SELECT COUNT(*) INTO param1 FROM t;
 END;
//

DELIMITER ;

CALL simpleproc(@a);

SELECT @a;
+------+
| @a   |
+------+
|    1 |
+------+
```

Character set and collation:


```
DELIMITER //

CREATE PROCEDURE simpleproc2 (
  OUT param1 CHAR(10) CHARACTER SET 'utf8' COLLATE 'utf8_bin'
)
 BEGIN
  SELECT CONCAT('a'),f1 INTO param1 FROM t;
 END;
//

DELIMITER ;
```

CREATE OR REPLACE:


```
DELIMITER //

CREATE PROCEDURE simpleproc2 (
  OUT param1 CHAR(10) CHARACTER SET 'utf8' COLLATE 'utf8_bin'
)
 BEGIN
  SELECT CONCAT('a'),f1 INTO param1 FROM t;
 END;
//
ERROR 1304 (42000): PROCEDURE simpleproc2 already exists

DELIMITER ;

DELIMITER //

CREATE OR REPLACE PROCEDURE simpleproc2 (
  OUT param1 CHAR(10) CHARACTER SET 'utf8' COLLATE 'utf8_bin'
)
 BEGIN
  SELECT CONCAT('a'),f1 INTO param1 FROM t;
 END;
//
ERROR 1304 (42000): PROCEDURE simpleproc2 already exists

DELIMITER ;
Query OK, 0 rows affected (0.03 sec)
```

## See Also


* [Identifier Names](../../../../reference/sql-statements-and-structure/sql-language-structure/identifier-names.md)
* [Stored Procedure Overview](stored-procedure-overview.md)
* [ALTER PROCEDURE](alter-procedure.md)
* [DROP PROCEDURE](drop-procedure.md)
* [SHOW CREATE PROCEDURE](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-create-procedure.md)
* [SHOW PROCEDURE STATUS](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-procedure-status.md)
* [Stored Routine Privileges](../stored-functions/stored-routine-privileges.md)
* [Information Schema ROUTINES Table](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-routines-table.md)

