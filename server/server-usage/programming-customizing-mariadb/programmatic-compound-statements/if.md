
# IF

## Syntax


```
IF search_condition THEN statement_list
    [ELSEIF search_condition THEN statement_list] ...
    [ELSE statement_list]
END IF;
```

## Description


`<code>IF</code>` implements a basic conditional construct. If the `<code>search_condition</code>`
evaluates to true, the corresponding SQL statement list is executed.
If no `<code>search_condition</code>` matches, the statement list in the `<code>ELSE</code>` clause
is executed. Each statement_list consists of one or more statements.


## See Also


* The [IF() function](../../../reference/sql-statements-and-structure/sql-statements/built-in-functions/control-flow-functions/if-function.md), which differs from the `<code>IF</code>` statement described above.
* [Changes in Oracle mode from MariaDB 10.3](../../../../release-notes/mariadb-community-server/compatibility-and-differences/sql_modeoracle.md)
* The [CASE statement](case-statement.md).

