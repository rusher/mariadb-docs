
# DROP EVENT

## Syntax


```
DROP EVENT [IF EXISTS] event_name
```

## Description


This statement drops the [event](../../../../../server-usage/programming-customizing-mariadb/triggers-events/event-scheduler/events.md) named `<code>event_name</code>`. The event immediately
ceases being active, and is deleted completely from the server.


If the event does not exist, the error
`<code class="fixed" style="white-space:pre-wrap">ERROR 1517 (HY000): Unknown event 'event_name'</code>`
results. You can override this and cause the
statement to generate a `<code>NOTE</code>` for non-existent events instead by using
`<code>IF EXISTS</code>`. See `<code>[SHOW WARNINGS](../../administrative-sql-statements/show/show-warnings.md)</code>`.


This statement requires the `<code>[EVENT](../../account-management-sql-commands/grant.md#database-privileges)</code>` privilege. In MySQL 5.1.11 and earlier, an event could be dropped only
by its definer, or by a user having the `<code>[SUPER](../../account-management-sql-commands/grant.md#global-privileges)</code>` privilege.


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


* [Events Overview](../../../../../server-usage/programming-customizing-mariadb/triggers-events/event-scheduler/events.md)
* [CREATE EVENT](../create/create-event.md)
* [SHOW CREATE EVENT](../../administrative-sql-statements/show/show-create-event.md)
* [ALTER EVENT](../../../../../server-usage/programming-customizing-mariadb/triggers-events/event-scheduler/alter-event.md)

