
# CALL

## Syntax


```
CALL sp_name([parameter[,...]])
CALL sp_name[()]
```

## Description


The `<code class="highlight fixed" style="white-space:pre-wrap">CALL</code>` statement invokes a [stored procedure](../../../../server-usage/programming-customizing-mariadb/stored-routines/stored-procedures/README.md) that was
defined previously with [CREATE PROCEDURE](../../../../server-usage/programming-customizing-mariadb/stored-routines/stored-procedures/create-procedure.md).


Stored procedure names can be specified as `<code>database_name.procedure_name</code>`. Procedure names and database names can be quoted with backticks (). This is necessary if they are reserved words, or contain special characters. See [identifier qualifiers](../../sql-language-structure/identifier-qualifiers.md) for details.


`<code>CALL p()</code>` and `<code>CALL p</code>` are equivalent.


If parentheses are used, any number of spaces, tab characters and newline characters are allowed between the procedure's name and the open parenthesis.


`<code class="highlight fixed" style="white-space:pre-wrap">CALL</code>` can pass back values to its caller using parameters
that are declared as `<code class="highlight fixed" style="white-space:pre-wrap">OUT</code>` or `<code class="highlight fixed" style="white-space:pre-wrap">INOUT</code>`
parameters. If no value is assigned to an `<code>OUT</code>` parameter, `<code>NULL</code>` is assigned (and its former value is lost). To pass such values from another stored program you can use [user-defined variables](../../sql-language-structure/user-defined-variables.md), [local variables](../../../../server-usage/programming-customizing-mariadb/programmatic-compound-statements/declare-variable.md) or routine's parameters; in other contexts, you can only use user-defined variables.


`<code>CALL</code>` can also be executed as a prepared statement. Placeholders can be used for `<code>IN</code>` parameters in all versions of MariaDB; for `<code>OUT</code>` and `<code>INOUT</code>` parameters, placeholders can be used since [MariaDB 5.5](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5.md).


When the procedure returns, a client program can also obtain the
number of rows affected for the final statement executed within the routine: At
the SQL level, call the `<code>[ROW_COUNT()](../built-in-functions/secondary-functions/information-functions/row_count.md)</code>` function; from the C
API, call the `<code class="highlight fixed" style="white-space:pre-wrap">mysql_affected_rows()</code>` function.


If the `<code>CLIENT_MULTI_RESULTS</code>` API flag is set, `<code>CALL</code>` can return any number of resultsets and the called stored procedure can execute prepared statements. If it is not set, at most one resultset can be returned and prepared statements cannot be used within procedures.

