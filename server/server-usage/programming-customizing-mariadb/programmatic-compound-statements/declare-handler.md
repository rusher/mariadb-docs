
# DECLARE HANDLER

## Syntax


```
DECLARE handler_type HANDLER
    FOR condition_value [, condition_value] ...
    statement

handler_type:
    CONTINUE
  | EXIT 
  | UNDO

condition_value:
    SQLSTATE [VALUE] sqlstate_value
  | condition_name
  | SQLWARNING
  | NOT FOUND
  | SQLEXCEPTION
  | mariadb_error_code
```

## Description


The `<code>DECLARE ... HANDLER</code>` statement specifies handlers that each may
deal with one or more conditions. If one of these conditions occurs,
the specified statement is executed. statement can be a simple
statement (for example, `<code>SET var_name = value</code>`), or it can be a compound
statement written using [BEGIN and END](begin-end.md).


Handlers must be declared after local variables, a `<code>CONDITION</code>` and a [CURSOR](programmatic-compound-statements-cursors/README.md).


For a `<code>CONTINUE</code>` handler, execution of the current program continues
after execution of the handler statement. For an EXIT handler,
execution terminates for the [BEGIN ... END](begin-end.md) compound statement in which
the handler is declared. (This is true even if the condition occurs in
an inner block.) The `<code>UNDO</code>` handler type statement is not supported.


If a condition occurs for which no handler has been declared, the
default action is `<code>EXIT</code>`.


A condition_value for `<code>DECLARE ... HANDLER</code>` can be any of the following
values:


* An [SQLSTATE](programmatic-compound-statements-diagnostics/sqlstate.md) value (a 5-character string literal) or a MariaDB error
code (a number). You should not use `<code>SQLSTATE</code>` value '00000' or MariaDB
error code 0, because those indicate sucess rather than an error
condition. For a list of `<code>SQLSTATE</code>` values and MariaDB error codes, see
[MariaDB Error Codes](../../../reference/mariadb-internals/using-mariadb-with-your-programs-api/error-codes/mariadb-error-codes-4000-to-4099/README.md).
* A condition name previously specified with `<code>DECLARE ... CONDITION</code>`. It must be in the same stored program. See [DECLARE CONDITION](declare-condition.md).
* `<code>SQLWARNING</code>` is shorthand for the class of SQLSTATE values that begin
with '01'.
* `<code>NOT FOUND</code>` is shorthand for the class of `<code>SQLSTATE</code>` values that begin
with '02'. This is relevant only the context of cursors and is used to
control what happens when a cursor reaches the end of a data set. If
no more rows are available, a No Data condition occurs with `<code>SQLSTATE</code>`
value 02000. To detect this condition, you can set up a handler for it
(or for a `<code>NOT FOUND</code>` condition). An example is shown in [Cursor Overview](programmatic-compound-statements-cursors/cursor-overview.md). This condition also occurs for [SELECT ... INTO](../../../reference/sql-statements-and-structure/sql-statements/data-manipulation/selecting-data/select-into-outfile.md) var_list statements that retrieve no
rows.
* SQLEXCEPTION is shorthand for the class of SQLSTATE values that do
not begin with '00', '01', or '02'.


When an error raises, in some cases it could be handled by multiple `<code>HANDLER</code>`s. For example, there may be an handler for 1050 error, a separate handler for the 42S01 SQLSTATE, and another separate handler for the `<code>SQLEXCEPTION</code>` class: in theory all occurrences of `<code>HANDLER</code>` may catch the 1050 error, but MariaDB chooses the `<code>HANDLER</code>` with the highest precedence. Here are the precedence rules:


* Handlers which refer to an error code have the highest precedence.
* Handlers which refer to a SQLSTATE come next.
* Handlers which refer to an error class have the lowest precedence.


In some cases, a statement could produce multiple errors. If this happens, in some cases multiple handlers could have the highest precedence. In such cases, the choice of the handler is indeterminate.


Note that if an error occurs within a `<code>CONTINUE HANDLER</code>` block, it can be handled by another `<code>HANDLER</code>`. However, a `<code>HANDLER</code>` which is already in the stack (that is, it has been called to handle an error and its execution didn't finish yet) cannot handle new errors—this prevents endless loops. For example, suppose that a stored procedure contains a `<code>CONTINUE HANDLER</code>` for `<code>SQLWARNING</code>` and another `<code>CONTINUE HANDLER</code>` for `<code>NOT FOUND</code>`. At some point, a NOT FOUND error occurs, and the execution enters the `<code>NOT FOUND HANDLER</code>`. But within that handler, a warning occurs, and the execution enters the `<code>SQLWARNING HANDLER</code>`. If another `<code>NOT FOUND</code>` error occurs, it cannot be handled again by the `<code>NOT FOUND HANDLER</code>`, because its execution is not finished.


When a `<code>DECLARE HANDLER</code>` block can handle more than one error condition, it may be useful to know which errors occurred. To do so, you can use the [GET DIAGNOSTICS](programmatic-compound-statements-diagnostics/get-diagnostics.md) statement.


An error that is handled by a `<code>DECLARE HANDLER</code>` construct can be issued again using the [RESIGNAL](resignal.md) statement.


Below is an example using `<code>DECLARE HANDLER</code>`:


```
CREATE TABLE test.t (s1 INT, PRIMARY KEY (s1));

DELIMITER //

CREATE PROCEDURE handlerdemo ( )
     BEGIN
       DECLARE CONTINUE HANDLER FOR SQLSTATE '23000' SET @x2 = 1;
       SET @x = 1;
       INSERT INTO test.t VALUES (1);
       SET @x = 2;
       INSERT INTO test.t VALUES (1);
       SET @x = 3;
     END;
     //

DELIMITER ;

CALL handlerdemo( );

SELECT @x;
+------+
| @x   |
+------+
|    3 |
+------+
```
