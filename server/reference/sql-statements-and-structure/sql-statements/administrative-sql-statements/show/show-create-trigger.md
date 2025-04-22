
# SHOW CREATE TRIGGER

## Syntax


```
SHOW CREATE TRIGGER trigger_name
```


## Description


This statement shows a `[CREATE TRIGGER](../../../../../server-usage/programming-customizing-mariadb/triggers-events/triggers/create-trigger.md)`
statement that creates the given trigger, as well as the [SQL_MODE](../../../../../server-management/variables-and-modes/sql-mode.md) that was used when the trigger has been created and the character set used by the connection.


The `[TRIGGER](../../account-management-sql-commands/grant.md#table-privileges)` privilege is required on the table the trigger is defined for to execute this statement.


`SHOW CREATE TRIGGER` quotes identifiers according to the value of the [sql_quote_show_create](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#sql_quote_show_create) system variable. Prior to [MariaDB 10.6.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-6-series/mariadb-1065-release-notes), [MariaDB 10.5.13](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-5-series/mariadb-10513-release-notes) and [MariaDB 10.4.22](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/mariadb-10422-release-notes), the output of this statement was unreliably affected by the [sql_quote_show_create](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#sql_quote_show_create) system variable.


## Examples


```
SHOW CREATE TRIGGER example\G
*************************** 1. row ***************************
               Trigger: example
              sql_mode: ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,STRICT_ALL_TABLES
,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_
ENGINE_SUBSTITUTION
SQL Original Statement: CREATE DEFINER=`root`@`localhost` TRIGGER example BEFORE
 INSERT ON t FOR EACH ROW
BEGIN
        SET NEW.c = NEW.c * 2;
END
  character_set_client: cp850
  collation_connection: cp850_general_ci
  Database Collation: utf8_general_ci
  Created: 2016-09-29 13:53:34.35
```

The `Created` column was added in [MariaDB 10.2.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1023-release-notes) as part of introducing multiple trigger events per action.


## See Also


* [Trigger Overview](../../../../../server-usage/programming-customizing-mariadb/triggers-events/triggers/trigger-overview.md)
* [CREATE TRIGGER](../../../../../server-usage/programming-customizing-mariadb/triggers-events/triggers/create-trigger.md)
* [DROP TRIGGER](../../data-definition/drop/drop-trigger.md)
* [information_schema.TRIGGERS Table](../system-tables/information-schema/information-schema-tables/information-schema-triggers-table.md)
* [SHOW TRIGGERS](show-triggers.md)
* [Trigger Limitations](../../../../../server-usage/programming-customizing-mariadb/triggers-events/triggers/trigger-limitations.md)

