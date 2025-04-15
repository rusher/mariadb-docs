
# Information Schema EVENTS Table

The [Information Schema](../../../../../../mariadb-internals/information-schema-plugins-show-and-flush-statements.md) `<code>EVENTS</code>` table stores information about [Events](../../../../../../../server-usage/programming-customizing-mariadb/triggers-events/event-scheduler/README.md) on the server.


It contains the following columns:



| Column | Description |
| --- | --- |
| Column | Description |
| EVENT_CATALOG | Always def. |
| EVENT_SCHEMA | Database where the event was defined. |
| EVENT_NAME | Event name. |
| DEFINER | Event definer. |
| TIME_ZONE | Time zone used for the event's scheduling and execution, by default SYSTEM. |
| EVENT_BODY | SQL. |
| EVENT_DEFINITION | The SQL defining the event. |
| EVENT_TYPE | Either ONE TIME or RECURRING. |
| EXECUTE_AT | [DATETIME](../../../../../../data-types/date-and-time-data-types/datetime.md) when the event is set to execute, or NULL if recurring. |
| INTERVAL_VALUE | Numeric interval between event executions for a recurring event, or NULL if not recurring. |
| INTERVAL_FIELD | Interval unit (e.g., HOUR) |
| SQL_MODE | The [SQL_MODE](../../../../../../../server-management/variables-and-modes/sql-mode.md) at the time the event was created. |
| STARTS | Start [DATETIME](../../../../../../data-types/date-and-time-data-types/datetime.md) for a recurring event, NULL if not defined or not recurring. |
| ENDS | End [DATETIME](../../../../../../data-types/date-and-time-data-types/datetime.md) for a recurring event, NULL if not defined or not recurring. |
| STATUS | One of ENABLED, DISABLED or /SLAVESIDE_DISABLED. |
| ON_COMPLETION | The ON COMPLETION clause, either PRESERVE or NOT PRESERVE . |
| CREATED | When the event was created. |
| LAST_ALTERED | When the event was last changed. |
| LAST_EXECUTED | When the event was last run. |
| EVENT_COMMENT | The comment provided in the [CREATE EVENT](../../../../data-definition/create/create-event.md) statement, or an empty string if none. |
| ORIGINATOR | MariaDB server ID on which the event was created. |
| CHARACTER_SET_CLIENT | [character_set_client](../../../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#character_set_client) system variable session value at the time the event was created. |
| COLLATION_CONNECTION | [collation_connection](../../../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#collation_connection) system variable session value at the time the event was created. |
| DATABASE_COLLATION | Database [collation](../../../../../../data-types/string-data-types/character-sets/README.md) with which the event is linked. |



The `<code>[SHOW EVENTS](../../../show/show-events.md)</code>` and `<code>[SHOW CREATE EVENT](../../../show/show-create-event.md)</code>` statements provide similar information.

