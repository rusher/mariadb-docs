
# SHOW CREATE VIEW

## Syntax


```
SHOW CREATE VIEW view_name
```

## Description


This statement shows a [CREATE VIEW](../../../../../server-usage/programming-customizing-mariadb/views/create-view.md) statement that creates the given [view](../../../../../server-usage/programming-customizing-mariadb/views/README.md), as well as the character set used by the connection when the view was created. This statement
also works with views.


`<code class="highlight fixed" style="white-space:pre-wrap">SHOW CREATE VIEW</code>` quotes table, column and stored function names according to the value of the [sql_quote_show_create](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#sql_quote_show_create) server system variable.


## Examples


```
SHOW CREATE VIEW example\G
*************************** 1. row ***************************
                View: example
         Create View: CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL
SECURITY DEFINER VIEW `example` AS (select `t`.`id` AS `id`,`t`.`s` AS `s` from
`t`)
character_set_client: cp850
collation_connection: cp850_general_ci
```

With [sql_quote_show_create](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#sql_quote_show_create) off:


```
SHOW CREATE VIEW example\G
*************************** 1. row ***************************
                View: example
         Create View: CREATE ALGORITHM=UNDEFINED DEFINER=root@localhost SQL SECU
RITY DEFINER VIEW example AS (select t.id AS id,t.s AS s from t)
character_set_client: cp850
collation_connection: cp850_general_ci
```

## Grants


To be able to see a view, you need to have the [SHOW VIEW](../../account-management-sql-commands/grant.md#table-privileges) and the [SELECT](../../account-management-sql-commands/grant.md#table-privileges) privilege on the view:


```
GRANT SHOW VIEW,SELECT ON test_database.test_view TO 'test'@'localhost';
```

## See Also


* [Grant privileges to tables, views etc](../../account-management-sql-commands/grant.md)

