# Information Schema VIEWS Table

The [Information Schema](/en/information_schema/) `VIEWS` table contains information about [views](/en/views/). The `SHOW VIEW` [privilege](../../../reference/sql-statements-and-structure/sql-statements/account-management-sql-commands/grant.md) is required to view the table.

It has the following columns:

| Column | Description |
| --- | --- |
| Column | Description |
| TABLE_CATALOG | Aways def. |
| TABLE_SCHEMA | Database name containing the view. |
| TABLE_NAME | View table name. |
| VIEW_DEFINITION | Definition of the view. |
| CHECK_OPTION | YES if the WITH CHECK_OPTION clause has been specified, NO otherwise. |
| IS_UPDATABLE | Whether the view is updatable or not. |
| DEFINER | Account specified in the DEFINER clause (or the default when created). |
| SECURITY_TYPE | SQL SECURITY characteristic, either DEFINER or INVOKER. |
| CHARACTER_SET_CLIENT | The client [character set](/en/data-types-character-sets-and-collations/) when the view was created, from the session value of the [character_set_client](../../replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#character_set_client) system variable. |
| COLLATION_CONNECTION | The client [collation](/en/data-types-character-sets-and-collations/) when the view was created, from the session value of the [collation_connection](../../replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#collation_connection) system variable. |
| ALGORITHM | The algorithm used in the view. See [View Algorithms](view-algorithms.md). |

#

# Example

```
SELECT * FROM information_schema.VIEWS\G
*************************** 1. row ***************************
 TABLE_CATALOG: def
 TABLE_SCHEMA: test
 TABLE_NAME: v
 VIEW_DEFINITION: select `test`.`t`.`qty` AS `qty`,`test`.`t`.`price` AS `price`,(`test`.`t`.`qty` * `test`.`t`.`price`) AS `value` from `test`.`t`
 CHECK_OPTION: NONE
 IS_UPDATABLE: YES
 DEFINER: root@localhost
 SECURITY_TYPE: DEFINER
CHARACTER_SET_CLIENT: utf8
COLLATION_CONNECTION: utf8_general_ci
 ALGORITHM: UNDEFINED
```

#

# See Also

* [CREATE VIEW](create-view.md)
* [ALTER VIEW](alter-view.md)
* [DROP VIEW](drop-view.md)
* [SHOW CREATE VIEWS](show-create-views)