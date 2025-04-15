
# CASE Statement

## Syntax


```
CASE case_value
    WHEN when_value THEN statement_list
    [WHEN when_value THEN statement_list] ...
    [ELSE statement_list]
END CASE
```

Or:


```
CASE
    WHEN search_condition THEN statement_list
    [WHEN search_condition THEN statement_list] ...
    [ELSE statement_list] 
END CASE
```

## Description


The text on this page describes the `<code>CASE</code>` statement for [stored programs](../stored-routines/README.md). See the [CASE OPERATOR](../../../reference/sql-statements-and-structure/sql-statements/built-in-functions/control-flow-functions/case-operator.md) for details on the CASE operator outside of [stored programs](../stored-routines/README.md).


The `<code>CASE</code>` statement for [stored programs](../stored-routines/README.md) implements a complex conditional
construct. If a `<code>search_condition</code>` evaluates to true, the corresponding SQL
statement list is executed. If no search condition matches, the statement list
in the `<code>ELSE</code>` clause is executed. Each `<code>statement_list</code>` consists of one or
more statements.


The `<code>CASE</code>` statement cannot have an `<code>ELSE NULL</code>` clause, and it is
terminated with `<code>END CASE</code>` instead of `<code>END</code>`. implements a complex conditional
construct. If a `<code>search_condition</code>` evaluates to true, the corresponding SQL
statement list is executed. If no search condition matches, the statement list
in the `<code>ELSE</code>` clause is executed. Each `<code>statement_list</code>` consists of one or
more statements.


If no when_value or search_condition matches the value tested and the `<code>CASE</code>`
statement contains no `<code>ELSE</code>` clause, a Case not found for `<code>CASE</code>` statement
error results.


Each statement_list consists of one or more statements; an empty
`<code>statement_list</code>` is not allowed. To handle situations where no value is
matched by any `<code>WHEN</code>` clause, use an `<code>ELSE</code>` containing an
empty [BEGIN ... END](begin-end.md) block, as shown in this example:


```
DELIMITER |
CREATE PROCEDURE p()
BEGIN
  DECLARE v INT DEFAULT 1;
  CASE v
    WHEN 2 THEN SELECT v;
    WHEN 3 THEN SELECT 0;
    ELSE BEGIN END;
  END CASE;
END;
|
```

The indentation used here in the `<code>ELSE</code>` clause is for purposes of clarity only,
and is not otherwise significant. See [Delimiters in the mariadb client](../../../clients-and-utilities/mariadb-client/delimiters.md) for more on the use of the delimiter command.


**Note:** The syntax of the `<code>CASE</code>` statement used inside stored programs
differs slightly from that of the SQL CASE expression described in
[CASE OPERATOR](../../../reference/sql-statements-and-structure/sql-statements/built-in-functions/control-flow-functions/case-operator.md).
The `<code>CASE</code>` statement cannot have an `<code>ELSE NULL</code>` clause, and it is
terminated with `<code>END CASE</code>` instead of `<code>END</code>`.


## See Also


* The [CASE operator](../../../reference/sql-statements-and-structure/sql-statements/built-in-functions/control-flow-functions/case-operator.md), which differs from the CASE statement described above.
* The [IF statement](../../../reference/sql-statements-and-structure/sql-statements/built-in-functions/control-flow-functions/ifnull.md).

