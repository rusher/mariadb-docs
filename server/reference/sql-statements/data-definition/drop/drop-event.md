# DROP EVENT

## Syntax

```
DROP EVENT [IF EXISTS] event_name
```

## Description

This statement drops the [event](../../../../server-usage/triggers-events/event-scheduler/events.md) named `event_name`. The event immediately\
ceases being active, and is deleted completely from the server.

If the event does not exist, the error`ERROR 1517 (HY000): Unknown event 'event_name'`\
results. You can override this and cause the\
statement to generate a `NOTE` for non-existent events instead by using`IF EXISTS`. See `[SHOW WARNINGS](../../administrative-sql-statements/show/show-warnings.md)`.

This statement requires the `[EVENT](../../account-management-sql-commands/grant.md#database-privileges)` privilege. In MySQL 5.1.11 and earlier, an event could be dropped only\
by its definer, or by a user having the `[SUPER](../../account-management-sql-commands/grant.md#global-privileges)` privilege.

## Examples

```
DROP EVENT myevent3;
```

Using the IF EXISTS clause:

```
DROP EVENT IF EXISTS myevent3;
Query OK, 0 rows affected, 1 warning (0.01 sec)

SHOW WARNINGS;
+-------+------+-------------------------------+
| Level | Code | Message                       |
+-------+------+-------------------------------+
| Note  | 1305 | Event myevent3 does not exist |
+-------+------+-------------------------------+
```

## See also

* [Events Overview](../../../../server-usage/triggers-events/event-scheduler/events.md)
* [CREATE EVENT](../create/create-event.md)
* [SHOW CREATE EVENT](../../administrative-sql-statements/show/show-create-event.md)
* [ALTER EVENT](../../../../server-usage/triggers-events/event-scheduler/alter-event.md)

GPLv2 fill\_help\_tables.sql
