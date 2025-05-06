
# Information Schema TRIGGERS Table

The [Information Schema](../README.md) `TRIGGERS` table contains information about [triggers](../../../../../../../server-usage/programming-customizing-mariadb/triggers-events/triggers/README.md).


It has the following columns:



| Column | Description |
| --- | --- |
| Column | Description |
| TRIGGER_CATALOG | Always def. |
| TRIGGER_SCHEMA | Database name in which the trigger occurs. |
| TRIGGER_NAME | Name of the trigger. |
| EVENT_MANIPULATION | The event that activates the trigger. One of INSERT, UPDATE or 'DELETE. |
| EVENT_OBJECT_CATALOG | Always def. |
| EVENT_OBJECT_SCHEMA | Database name on which the trigger acts. |
| EVENT_OBJECT_TABLE | Table name on which the trigger acts. |
| ACTION_ORDER | Indicates the order that the action will be performed in (of the list of a table's triggers with identical EVENT_MANIPULATION and ACTION_TIMING values). Before [MariaDB 10.2.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1023-release-notes) introduced the [FOLLOWS and PRECEDES clauses](../../../../../../../server-usage/programming-customizing-mariadb/triggers-events/triggers/create-trigger.md#followsprecedes-other_trigger_name), always 0 |
| ACTION_CONDITION | NULL |
| ACTION_STATEMENT | Trigger body, UTF-8 encoded. |
| ACTION_ORIENTATION | Always ROW. |
| ACTION_TIMING | Whether the trigger acts BEFORE or AFTER the event that triggers it. |
| ACTION_REFERENCE_OLD_TABLE | Always NULL. |
| ACTION_REFERENCE_NEW_TABLE | Always NULL. |
| ACTION_REFERENCE_OLD_ROW | Always OLD. |
| ACTION_REFERENCE_NEW_ROW | Always NEW. |
| CREATED | Always NULL. |
| SQL_MODE | The [SQL_MODE](../../../../../../../server-management/variables-and-modes/sql-mode.md) when the trigger was created, and which it uses for execution. |
| DEFINER | The account that created the trigger, in the form user_name@host_name |
| CHARACTER_SET_CLIENT | The client [character set](../../../../../../data-types/string-data-types/character-sets/README.md) when the trigger was created, from the session value of the [character_set_client](../../../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#character_set_client) system variable. |
| COLLATION_CONNECTION | The client [collation](../../../../../../data-types/string-data-types/character-sets/README.md) when the trigger was created, from the session value of the [collation_connection](../../../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#collation_connection) system variable. |
| DATABASE_COLLATION | [Collation](../../../../../../data-types/string-data-types/character-sets/README.md) of the associated database. |



Queries to the `TRIGGERS` table will return information only for databases and tables for which you have the `TRIGGER` [privilege](../../../../account-management-sql-commands/grant.md#table-privileges). Similar information is returned by the `[SHOW TRIGGERS](../../../show/show-triggers.md)` statement.


## See also


* [Trigger Overview](../../../../../../../server-usage/programming-customizing-mariadb/triggers-events/triggers/trigger-overview.md)
* `[CREATE TRIGGER](../../../../../../../server-usage/programming-customizing-mariadb/triggers-events/triggers/create-trigger.md)`
* `[DROP TRIGGER](../../../../data-definition/drop/drop-trigger.md)`
* `[SHOW TRIGGERS](../../../show/show-triggers.md)`
* `[SHOW CREATE TRIGGER](../../../show/show-create-trigger.md)`
* [Trigger Limitations](../../../../../../../server-usage/programming-customizing-mariadb/triggers-events/triggers/trigger-limitations.md)


CC BY-SA / Gnu FDL

