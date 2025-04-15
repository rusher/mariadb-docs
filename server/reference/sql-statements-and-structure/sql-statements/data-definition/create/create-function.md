
# CREATE FUNCTION

## Syntax


```
|
```


## Description


Use the `<code>CREATE FUNCTION</code>` statement to create a new [stored function](../../../../../server-usage/programming-customizing-mariadb/stored-routines/stored-functions/README.md). You must have
the [CREATE ROUTINE](../../account-management-sql-commands/grant.md#database-privileges) database privilege to use `<code>CREATE FUNCTION</code>`.
A function takes any number of arguments and returns a value from the function body. The
function body can be any valid SQL expression as you would use, for example, in any select
expression. If you have the appropriate privileges, you can call the function exactly as you
would any built-in function. See [Security](#security) below for details on privileges.


You can also use a variant of the `<code>CREATE FUNCTION</code>` statement to install a user-defined
function (UDF) defined by a plugin. See [CREATE FUNCTION (UDF)](../../../../../server-usage/programming-customizing-mariadb/user-defined-functions/create-function-udf.md)
for details.


You can use a [SELECT](../../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/benchmarks-and-long-running-tests/benchmark-results/select-random-ranges-and-select-random-point.md) statement for the function body by enclosing it in
parentheses, exactly as you would to use a subselect for any other expression. The `<code>SELECT</code>`
statement must return a single value. If more than one column is returned when the function is called,
error 1241 results. If more than one row is returned when the function is called, error 1242
results. Use a `<code>LIMIT</code>` clause to ensure only one row is returned.


You can also replace the `<code>RETURN</code>` clause with a [BEGIN...END](../../../../../server-usage/programming-customizing-mariadb/programmatic-compound-statements/begin-end.md) compound
statement. The compound statement must contain a `<code>RETURN</code>` statement. When the function is
called, the `<code>RETURN</code>` statement immediately returns its result, and any statements after `<code>RETURN</code>`
are effectively ignored.


By default, a function is associated with the current database. To associate the function explicitly
with a given database, specify the fully-qualified name as `<code><em>db_name</em>.<em>func_name</em></code>`
when you create it. If the function name is the same as the name of a built-in function, you must
use the fully qualified name when you call it.


The parameter list enclosed within parentheses must always be present.
If there are no parameters, an empty parameter list of () should be
used. Parameter names are not case sensitive.


Each parameter can be declared to use any valid data type, except that
the COLLATE attribute cannot be used.


For valid identifiers to use as function names, see [Identifier Names](../../../sql-language-structure/identifier-names.md).


#### IN | OUT | INOUT | IN OUT



##### MariaDB starting with [10.8.0](../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-8-series/mariadb-10-8-0-release-notes.md)
The function parameter qualifiers for `<code>IN</code>`, `<code>OUT</code>`, `<code>INOUT</code>`, and `<code>IN OUT</code>` were added in a 10.8.0 preview release. Prior to 10.8.0 quantifiers were supported only in procedures.


`<code>OUT</code>`, `<code>INOUT</code>` and its equivalent `<code>IN OUT</code>`, are only valid if called from `<code>SET</code>` and not `<code>SELECT</code>`. These quantifiers are especially useful for creating functions with more than one return value. This allows functions to be more complex and nested.


```
DELIMITER $$
CREATE FUNCTION add_func3(IN a INT, IN b INT, OUT c INT) RETURNS INT
BEGIN
  SET c = 100;
  RETURN a + b;
END;
$$
DELIMITER ;
 
SET @a = 2;
SET @b = 3;
SET @c = 0;
SET @res= add_func3(@a, @b, @c);

SELECT add_func3(@a, @b, @c);
ERROR 4186 (HY000): OUT or INOUT argument 3 for function add_func3 is not allowed here

DELIMITER $$
CREATE FUNCTION add_func4(IN a INT, IN b INT, d INT) RETURNS INT
BEGIN
  DECLARE c, res INT;
  SET res = add_func3(a, b, c) + d;
  if (c > 99) then
    return  3;
  else
    return res;
  end if;
END;
$$

DELIMITER ;

SELECT add_func4(1,2,3);
+------------------+
| add_func4(1,2,3) |
+------------------+
|                3 |
+------------------+
```

#### AGGREGATE


It is possible to create stored aggregate functions as well. See [Stored Aggregate Functions](../../../../../server-usage/programming-customizing-mariadb/stored-routines/stored-functions/stored-aggregate-functions.md) for details.


#### RETURNS


The `<code>RETURNS</code>` clause specifies the return type of the function. `<code>NULL</code>` values are permitted with all return types.


What happens if the `<code>RETURN</code>` clause returns a value of a different type? It depends on the [SQL_MODE](../../../../../server-management/variables-and-modes/sql-mode.md) in effect at the moment of the function creation.


If the SQL_MODE is strict (STRICT_ALL_TABLES or STRICT_TRANS_TABLES flags are specified), a 1366 error will be produced.


Otherwise, the value is coerced to the proper type. For example, if a function
specifies an `<code>ENUM</code>` or `<code>SET</code>` value in the `<code>RETURNS</code>` clause, but the `<code>RETURN</code>`
clause returns an integer, the value returned from the function is the string for the corresponding `<code>ENUM</code>`
member of set of `<code>SET</code>` members.


MariaDB stores the SQL_MODE system variable setting that is in effect at the
time a routine is created, and always executes the routine with this setting in
force, regardless of the server SQL mode in effect when the routine is invoked.


#### LANGUAGE SQL


`<code>LANGUAGE SQL</code>` is a standard SQL clause, and it can be used in MariaDB for portability. However that clause has no meaning, because SQL is the only supported language for stored functions.


A function is deterministic if it can produce only one result for a given list of parameters. If the result may be affected by stored data, server variables, random numbers or any value that is not explicitly passed, then the function is not deterministic. Also, a function is non-deterministic if it uses non-deterministic functions like [NOW()](../../built-in-functions/date-time-functions/now.md) or [CURRENT_TIMESTAMP()](../../built-in-functions/date-time-functions/current_timestamp.md). The optimizer may choose a faster execution plan if it known that the function is deterministic. In such cases, you should declare the routine using the `<code>DETERMINISTIC</code>` keyword. If you want to explicitly state that the function is not deterministic (which is the default) you can use the `<code>NOT DETERMINISTIC</code>` keywords.


If you declare a non-deterministic function as `<code>DETERMINISTIC</code>`, you may get incorrect results. If you declare a deterministic function as `<code>NOT DETERMINISTIC</code>`, in some cases the queries will be slower.


#### OR REPLACE


If the optional `<code>OR REPLACE</code>` clause is used, it acts as a shortcut for:


```
DROP FUNCTION IF EXISTS function_name;
CREATE FUNCTION function_name ...;
```

with the exception that any existing [privileges](../../../../../server-usage/programming-customizing-mariadb/stored-routines/stored-functions/stored-routine-privileges.md) for the function are not dropped.


#### IF NOT EXISTS


If the IF NOT EXISTS clause is used, MariaDB will return a warning instead of an error if the function already exists. Cannot be used together with OR REPLACE.


#### [NOT] DETERMINISTIC


The `<code>[NOT] DETERMINISTIC</code>` clause also affects [binary logging](../../../../storage-engines/innodb/binary-log-group-commit-and-innodb-flushing-performance.md), because the `<code>STATEMENT</code>` format can not be used to store or replicate non-deterministic statements.


`<code>CONTAINS SQL</code>`, `<code>NO SQL</code>`, `<code>READS SQL DATA</code>`, and `<code>MODIFIES SQL DATA</code>` are informative clauses that tell the server what the function does. MariaDB does not check in any way whether the specified clause is correct. If none of these clauses are specified, `<code>CONTAINS SQL</code>` is used by default.


#### MODIFIES SQL DATA


`<code>MODIFIES SQL DATA</code>` means that the function contains statements that may modify data stored in databases. This happens if the function contains statements like [DELETE](../../data-manipulation/changing-deleting-data/delete.md), [UPDATE](../../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/tools/buildbot/buildbot-setup/buildbot-setup-for-virtual-machines/buildbot-setup-for-virtual-machines-additional-steps/update-debian-4-mirrors-for-buildbot-vms.md), [INSERT](../../built-in-functions/string-functions/insert-function.md), [REPLACE](../../built-in-functions/string-functions/replace-function.md) or DDL.


#### READS SQL DATA


`<code>READS SQL DATA</code>` means that the function reads data stored in databases, but does not modify any data. This happens if [SELECT](../../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/benchmarks-and-long-running-tests/benchmark-results/select-random-ranges-and-select-random-point.md) statements are used, but there no write operations are executed.


#### CONTAINS SQL


`<code>CONTAINS SQL</code>` means that the function contains at least one SQL statement, but it does not read or write any data stored in a database. Examples include [SET](../../../../../../connectors/mariadb-connector-cpp/setup-for-connector-cpp-examples.md) or [DO](../../../../../../general-resources/company-and-community/contributing-participating/donate-to-the-foundation.md).


#### NO SQL


`<code>NO SQL</code>` means nothing, because MariaDB does not currently support any language other than SQL.


#### Oracle Mode


A subset of Oracle's PL/SQL language is supported in addition to the traditional SQL/PSM-based MariaDB syntax. See [Oracle mode](../../../../../../release-notes/mariadb-community-server/compatibility-and-differences/sql_modeoracle.md) for details on changes when running Oracle mode.


## Security


You must have the [EXECUTE](../../account-management-sql-commands/grant.md#function-privileges) privilege on a function to call it.
MariaDB automatically grants the `<code>EXECUTE</code>` and `<code>ALTER ROUTINE</code>` privileges to the
account that called `<code>CREATE FUNCTION</code>`, even if the `<code>DEFINER</code>` clause was used.


Each function has an account associated as the definer. By default, the definer is the account
that created the function. Use the `<code>DEFINER</code>` clause to specify a different account as the
definer. You must have the [SUPER](../../account-management-sql-commands/grant.md#super) privilege, or, from [MariaDB 10.5.2](../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1052-release-notes.md), the [SET USER](../../account-management-sql-commands/grant.md#set-user) privilege, to use the `<code>DEFINER</code>`
clause. See [Account Names](../../account-management-sql-commands/create-user.md#account-names) for details on specifying accounts.


The `<code>SQL SECURITY</code>` clause specifies what privileges are used when a function is called.
If `<code>SQL SECURITY</code>` is `<code>INVOKER</code>`, the function body will be evaluated using the privileges
of the user calling the function. If `<code>SQL SECURITY</code>` is `<code>DEFINER</code>`, the function body is
always evaluated using the privileges of the definer account. `<code>DEFINER</code>` is the default.


This allows you to create functions that grant limited access to certain data. For example, say
you have a table that stores some employee information, and that you've granted `<code>SELECT</code>`
privileges [only on certain columns](../../account-management-sql-commands/grant.md#column-privileges) to the user account `<code>roger</code>`.


```
CREATE TABLE employees (name TINYTEXT, dept TINYTEXT, salary INT);
GRANT SELECT (name, dept) ON employees TO roger;
```

To allow the user the get the maximum salary for a department, define a function and grant
the `<code>EXECUTE</code>` privilege:


```
CREATE FUNCTION max_salary (dept TINYTEXT) RETURNS INT RETURN
  (SELECT MAX(salary) FROM employees WHERE employees.dept = dept);
GRANT EXECUTE ON FUNCTION max_salary TO roger;
```

Since `<code>SQL SECURITY</code>` defaults to `<code>DEFINER</code>`, whenever the user `<code>roger</code>` calls
this function, the subselect will execute with your privileges. As long as you have privileges to
select the salary of each employee, the caller of the function will be able to get the maximum
salary for each department without being able to see individual salaries.


## Character sets and collations


Function return types can be declared to use any valid [character set and collation](../../../../data-types/string-data-types/character-sets/README.md). If used, the COLLATE attribute needs to be preceded by a CHARACTER SET attribute.


If the character set and collation are not specifically set in the statement, the database defaults at the time of creation will be used. If the database defaults change at a later stage, the stored function character set/collation will not be changed at the same time; the stored function needs to be dropped and recreated to ensure the same character set/collation as the database is used.


## Examples


The following example function takes a parameter, performs an operation using
an SQL function, and returns the result.


```
CREATE FUNCTION hello (s CHAR(20))
    RETURNS CHAR(50) DETERMINISTIC
    RETURN CONCAT('Hello, ',s,'!');

SELECT hello('world');
+----------------+
| hello('world') |
+----------------+
| Hello, world!  |
+----------------+
```

You can use a compound statement in a function to manipulate data with statements
like `<code>INSERT</code>` and `<code>UPDATE</code>`. The following example creates a counter function
that uses a temporary table to store the current value. Because the compound statement
contains statements terminated with semicolons, you have to first change the statement
delimiter with the `<code>DELIMITER</code>` statement to allow the semicolon to be used in the
function body. See [Delimiters in the mariadb client](../../../../../clients-and-utilities/mariadb-client/delimiters.md) for more.


```
CREATE TEMPORARY TABLE counter (c INT);
INSERT INTO counter VALUES (0);
DELIMITER //
CREATE FUNCTION counter () RETURNS INT
  BEGIN
    UPDATE counter SET c = c + 1;
    RETURN (SELECT c FROM counter LIMIT 1);
  END //
DELIMITER ;
```

Character set and collation:


```
CREATE FUNCTION hello2 (s CHAR(20))
  RETURNS CHAR(50) CHARACTER SET 'utf8' COLLATE 'utf8_bin' DETERMINISTIC
  RETURN CONCAT('Hello, ',s,'!');
```

## See Also


* [Identifier Names](../../../sql-language-structure/identifier-names.md)
* [Stored Aggregate Functions](../../../../../server-usage/programming-customizing-mariadb/stored-routines/stored-functions/stored-aggregate-functions.md)
* [CREATE FUNCTION (UDF)](../../../../../server-usage/programming-customizing-mariadb/user-defined-functions/create-function-udf.md)
* [SHOW CREATE FUNCTION](../../administrative-sql-statements/show/show-create-function.md)
* [ALTER FUNCTION](../alter/alter-function.md)
* [DROP FUNCTION](../../../../../server-usage/programming-customizing-mariadb/stored-routines/stored-functions/drop-function.md)
* [SHOW FUNCTION STATUS](../../administrative-sql-statements/show/show-function-status.md)
* [Stored Routine Privileges](../../../../../server-usage/programming-customizing-mariadb/stored-routines/stored-functions/stored-routine-privileges.md)
* [Information Schema ROUTINES Table](../../administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-routines-table.md)

