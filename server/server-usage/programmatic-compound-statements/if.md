# IF

## Syntax

```
IF search_condition THEN statement_list
    [ELSEIF search_condition THEN statement_list] ...
    [ELSE statement_list]
END IF;
```

## Description

`IF` implements a basic conditional construct. If the `search_condition`\
evaluates to true, the corresponding SQL statement list is executed.\
If no `search_condition` matches, the statement list in the `ELSE` clause\
is executed. Each statement\_list consists of one or more statements.

## See Also

* The [IF() function](../../reference/sql-statements-and-structure/sql-statements/built-in-functions/control-flow-functions/if-function.md), which differs from the `IF` statement described above.
* [Changes in Oracle mode from MariaDB 10.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/compatibility-and-differences/sql_modeoracle)
* The [CASE statement](case-statement.md).

GPLv2 fill\_help\_tables.sql
