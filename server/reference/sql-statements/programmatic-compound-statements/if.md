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

* The [IF() function](../../sql-functions/control-flow-functions/if-function.md), which differs from the `IF` statement described above.
* [Changes in Oracle mode from MariaDB 10.3](https://github.com/mariadb-corporation/docs-server/blob/test/server/server-usage/programmatic-compound-statements/broken-reference/README.md)
* The [CASE statement](case-statement.md).

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
