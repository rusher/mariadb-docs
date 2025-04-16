
# ALTER VIEW

## Syntax


```
ALTER
    [ALGORITHM = {UNDEFINED | MERGE | TEMPTABLE}]
    [DEFINER = { user | CURRENT_USER }]
    [SQL SECURITY { DEFINER | INVOKER }]
    VIEW view_name [(column_list)]
    AS select_statement
    [WITH [CASCADED | LOCAL] CHECK OPTION]
```


## Description


This statement changes the definition of a [view](README.md), which must exist. The
syntax is similar to that for [CREATE VIEW](create-view.md) and the effect is the same
as for `CREATE OR REPLACE VIEW` if the view exists. This statement
requires the `CREATE VIEW` and `DROP` [privileges](../../../reference/sql-statements-and-structure/sql-statements/account-management-sql-commands/grant.md#table-privileges) for the view, and some
privilege for each column referred to in the `SELECT` statement. `ALTER VIEW` is allowed only to the definer or users with the [SUPER](../../../reference/sql-statements-and-structure/sql-statements/account-management-sql-commands/grant.md#global-privileges) privilege.


## Example


```
ALTER VIEW v AS SELECT a, a*3 AS a2 FROM t;
```

## See Also


* [CREATE VIEW](create-view.md)
* [DROP VIEW](drop-view.md)
* [SHOW CREATE VIEW](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-create-view.md)
* [INFORMATION SCHEMA VIEWS Table](information-schema-views-table.md)

<span></span>
