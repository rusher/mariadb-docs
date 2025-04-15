
# CREATE EVENT

## Syntax


```
CREATE [OR REPLACE]
    [DEFINER = { user | CURRENT_USER | role | CURRENT_ROLE }]
    EVENT 
    [IF NOT EXISTS]
    event_name    
    ON SCHEDULE schedule
    [ON COMPLETION [NOT] PRESERVE]
    [ENABLE | DISABLE | DISABLE ON SLAVE]
    [COMMENT 'comment']
    DO sql_statement;

schedule:
    AT timestamp [+ INTERVAL interval] ...
  | EVERY interval 
    [STARTS timestamp [+ INTERVAL interval] ...] 
    [ENDS timestamp [+ INTERVAL interval] ...]

interval:
    quantity {YEAR | QUARTER | MONTH | DAY | HOUR | MINUTE |
              WEEK | SECOND | YEAR_MONTH | DAY_HOUR | DAY_MINUTE |
              DAY_SECOND | HOUR_MINUTE | HOUR_SECOND | MINUTE_SECOND}
```


## Description


This statement creates and schedules a new [event](../../../../../server-usage/programming-customizing-mariadb/triggers-events/event-scheduler/events.md). It requires the
`<code>[EVENT](../../account-management-sql-commands/grant.md#database-privileges)</code>` privilege for the schema in which the event is to be created.


The minimum requirements for a valid CREATE EVENT statement are as
follows:


* The keywords `<code>CREATE EVENT</code>` plus an event name, which uniquely identifies
 the event in the current schema. (Prior to MySQL 5.1.12, the event name
 needed to be unique only among events created by the same user on a given
 database.)
* An `<code>ON SCHEDULE</code>` clause, which determines when and how often the event
 executes.
* A `<code>DO</code>` clause, which contains the SQL statement to be executed by an
 event.


Here is an example of a minimal `<code>CREATE EVENT</code>` statement:


```
CREATE EVENT myevent
    ON SCHEDULE AT CURRENT_TIMESTAMP + INTERVAL 1 HOUR
    DO
      UPDATE myschema.mytable SET mycol = mycol + 1;
```

The previous statement creates an event named myevent. This event executes once
— one hour following its creation
— by running an SQL statement that increments the
value of the myschema.mytable table's mycol column by 1.


The event_name must be a valid MariaDB identifier with a maximum length
of 64 characters. It may be delimited using back ticks, and may be
qualified with the name of a database schema. An event is associated
with both a MariaDB user (the definer) and a schema, and its name must
be unique among names of events within that schema. In general, the
rules governing event names are the same as those for names of stored
routines. See [Identifier Names](../../../sql-language-structure/identifier-names.md).


If no schema is indicated as part of event_name, the default (current)
schema is assumed.


For valid identifiers to use as event names, see [Identifier Names](../../../sql-language-structure/identifier-names.md).


#### OR REPLACE


The `<code>OR REPLACE</code>` clause was included in [MariaDB 10.1.4](../../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-4-release-notes.md). If used and the event already exists, instead of an error being returned, the existing event will be dropped and replaced by the newly defined event.


#### IF NOT EXISTS


If the `<code>IF NOT EXISTS</code>` clause is used, MariaDB will return a warning instead of an error if the event already exists. Cannot be used together with OR REPLACE.


#### ON SCHEDULE


The `<code>ON SCHEDULE</code>` clause can be used to specify when the event must be triggered.


#### AT


If you want to execute the event only once (one time event), you can use the `<code>AT</code>` keyword, followed by a timestamp. If you use `<code>[CURRENT_TIMESTAMP](../../built-in-functions/date-time-functions/current_timestamp.md)</code>`, the event acts as soon as it is created. As a convenience, you can add one or more intervals to that timestamp. You can also specify a timestamp in the past, so that the event is stored but not triggered, until you modify it via [ALTER EVENT](../../../../../server-usage/programming-customizing-mariadb/triggers-events/event-scheduler/alter-event.md).


The following example shows how to create an event that will be triggered tomorrow at a certain time:


```
CREATE EVENT example
ON SCHEDULE AT CURRENT_TIMESTAMP + INTERVAL 1 DAY + INTERVAL 3 HOUR
DO something;
```

You can also specify that an event must be triggered at a regular interval (recurring event). In such cases, use the `<code>EVERY</code>` clause followed by the interval.


If an event is recurring, you can specify when the first execution must happen via the `<code>STARTS</code>` clause and a maximum time for the last execution via the `<code>ENDS</code>` clause. `<code>STARTS</code>` and `<code>ENDS</code>` clauses are followed by a timestamp and, optionally, one or more intervals. The `<code>ENDS</code>` clause can specify a timestamp in the past, so that the event is stored but not executed until you modify it via [ALTER EVENT](../../../../../server-usage/programming-customizing-mariadb/triggers-events/event-scheduler/alter-event.md).


In the following example, next month a recurring event will be triggered hourly for a week:


```
CREATE EVENT example
ON SCHEDULE EVERY 1 HOUR
STARTS CURRENT_TIMESTAMP + INTERVAL 1 MONTH
ENDS CURRENT_TIMESTAMP + INTERVAL 1 MONTH + INTERVAL 1 WEEK
DO some_task;
```

Intervals consist of a quantity and a time unit. The time units are the same used for other statements and time functions, except that you can't use microseconds for events. For simple time units, like `<code>HOUR</code>` or `<code>MINUTE</code>`, the quantity is an integer number, for example '10 MINUTE'. For composite time units, like `<code>HOUR_MINUTE</code>` or `<code>HOUR_SECOND</code>`, the quantity must be a string with all involved simple values and their separators, for example '2:30' or '2:30:30'.


#### ON COMPLETION [NOT] PRESERVE


The `<code>ON COMPLETION</code>` clause can be used to specify if the event must be deleted after its last execution (that is, after its `<code>AT</code>` or `<code>ENDS</code>` timestamp is past). By default, events are dropped when they are expired. To explicitly state that this is the desired behaviour, you can use `<code>ON COMPLETION NOT PRESERVE</code>`. Instead, if you want the event to be preserved, you can use `<code>ON COMPLETION PRESERVE</code>`.


In you specify `<code>ON COMPLETION NOT PRESERVE</code>`, and you specify a timestamp in the past for `<code>AT</code>` or `<code>ENDS</code>` clause, the event will be immediately dropped. In such cases, you will get a Note 1558: "Event execution time is in the past and ON COMPLETION NOT PRESERVE is set. The event was dropped immediately after creation".


#### ENABLE/DISABLE/DISABLE ON SLAVE


Events are `<code>ENABLE</code>`d by default. If you want to stop MariaDB from executing
an event, you may specify `<code>DISABLE</code>`. When it is ready to be activated, you
may enable it using `<code>[ALTER EVENT](../../../../../server-usage/programming-customizing-mariadb/triggers-events/event-scheduler/alter-event.md)</code>`. Another option is
`<code>DISABLE ON SLAVE</code>`, which indicates that an event was created on a master and has been replicated to the slave, which is prevented from executing the event. If `<code>DISABLE ON SLAVE</code>` is specifically set, the event will be disabled everywhere. It will not be executed on the master or the slaves.


#### COMMENT


The `<code>COMMENT</code>` clause may be used to set a comment for the event. Maximum
length for comments is 64 characters. The comment is a string, so it must be
quoted. To see events comments, you can query the [INFORMATION_SCHEMA.EVENTS table](../../administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-events-table.md) (the column is named `<code>EVENT_COMMENT</code>`).


## Examples


Minimal `<code>CREATE EVENT</code>` statement:


```
CREATE EVENT myevent
    ON SCHEDULE AT CURRENT_TIMESTAMP + INTERVAL 1 HOUR
    DO
      UPDATE myschema.mytable SET mycol = mycol + 1;
```

An event that will be triggered tomorrow at a certain time:


```
CREATE EVENT example
ON SCHEDULE AT CURRENT_TIMESTAMP + INTERVAL 1 DAY + INTERVAL 3 HOUR
DO something;
```

Next month a recurring event will be triggered hourly for a week:


```
CREATE EVENT example
ON SCHEDULE EVERY 1 HOUR
STARTS CURRENT_TIMESTAMP + INTERVAL 1 MONTH
ENDS CURRENT_TIMESTAMP + INTERVAL 1 MONTH + INTERVAL 1 WEEK
DO some_task;
```

OR REPLACE and IF NOT EXISTS:


```
CREATE EVENT myevent
    ON SCHEDULE AT CURRENT_TIMESTAMP + INTERVAL 1 HOUR
    DO
      UPDATE myschema.mytable SET mycol = mycol + 1;
ERROR 1537 (HY000): Event 'myevent' already exists

CREATE OR REPLACE EVENT myevent
    ON SCHEDULE AT CURRENT_TIMESTAMP + INTERVAL 1 HOUR
    DO
      UPDATE myschema.mytable SET mycol = mycol + 1;;
Query OK, 0 rows affected (0.00 sec)

CREATE EVENT IF NOT EXISTS myevent
    ON SCHEDULE AT CURRENT_TIMESTAMP + INTERVAL 1 HOUR
    DO
      UPDATE myschema.mytable SET mycol = mycol + 1;
Query OK, 0 rows affected, 1 warning (0.00 sec)

 SHOW WARNINGS;
+-------+------+--------------------------------+
| Level | Code | Message                        |
+-------+------+--------------------------------+
| Note  | 1537 | Event 'myevent' already exists |
+-------+------+--------------------------------+
```

## See Also


* [Event Limitations](../../../../../server-usage/programming-customizing-mariadb/triggers-events/event-scheduler/event-limitations.md)
* [Identifier Names](../../../sql-language-structure/identifier-names.md)
* [Events Overview](../../../../../server-usage/programming-customizing-mariadb/triggers-events/event-scheduler/events.md)
* [SHOW CREATE EVENT](../../administrative-sql-statements/show/show-create-event.md)
* [ALTER EVENT](../../../../../server-usage/programming-customizing-mariadb/triggers-events/event-scheduler/alter-event.md)
* [DROP EVENT](../drop/drop-event.md)

