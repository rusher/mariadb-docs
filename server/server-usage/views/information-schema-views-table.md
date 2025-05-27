# Information Schema VIEWS Table

The [Information Schema](../../reference/sql-statements/administrative-sql-statements/system-tables/information-schema/) `VIEWS` table contains information about [views](./). The `SHOW VIEW` [privilege](../../reference/sql-statements/account-management-sql-statements/grant.md) is required to view the table.

It has the following columns:

| Column                 | Description                                                                                                                                                                                                                                                                                                    |
| ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Column                 | Description                                                                                                                                                                                                                                                                                                    |
| TABLE\_CATALOG         | Aways def.                                                                                                                                                                                                                                                                                                     |
| TABLE\_SCHEMA          | Database name containing the view.                                                                                                                                                                                                                                                                             |
| TABLE\_NAME            | View table name.                                                                                                                                                                                                                                                                                               |
| VIEW\_DEFINITION       | Definition of the view.                                                                                                                                                                                                                                                                                        |
| CHECK\_OPTION          | YES if the WITH CHECK\_OPTION clause has been specified, NO otherwise.                                                                                                                                                                                                                                         |
| IS\_UPDATABLE          | Whether the view is updatable or not.                                                                                                                                                                                                                                                                          |
| DEFINER                | Account specified in the DEFINER clause (or the default when created).                                                                                                                                                                                                                                         |
| SECURITY\_TYPE         | SQL SECURITY characteristic, either DEFINER or INVOKER.                                                                                                                                                                                                                                                        |
| CHARACTER\_SET\_CLIENT | The client [character set](../../reference/data-types/string-data-types/character-sets/) when the view was created, from the session value of the [character\_set\_client](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#character_set_client) system variable. |
| COLLATION\_CONNECTION  | The client [collation](../../reference/data-types/string-data-types/character-sets/) when the view was created, from the session value of the [collation\_connection](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#collation_connection) system variable.      |
| ALGORITHM              | The algorithm used in the view. See [View Algorithms](view-algorithms.md).                                                                                                                                                                                                                                     |

## Example

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

## See Also

* [CREATE VIEW](create-view.md)
* [ALTER VIEW](alter-view.md)
* [DROP VIEW](drop-view.md)
* [SHOW CREATE VIEWS](../programming-customizing-mariadb/views/show-create-views/)

CC BY-SA / Gnu FDL
