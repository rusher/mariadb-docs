# Event Scheduler Thread States

This article documents thread states that are related to [event](../../../../server-usage/triggers-events/event-scheduler/events.md) scheduling and execution. These include the Event Scheduler thread, threads that terminate the Event Scheduler, and threads for executing events.

These correspond to the `STATE` values listed by the [SHOW PROCESSLIST](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-processlist.md) statement or in the [Information Schema PROCESSLIST Table](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-processlist-table.md) as well as the `PROCESSLIST_STATE` value listed in the [Performance Schema threads Table](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/performance-schema/performance-schema-tables/performance-schema-threads-table.md)

| Value                         | Description                                                                            |
| ----------------------------- | -------------------------------------------------------------------------------------- |
| Value                         | Description                                                                            |
| Clearing                      | Thread is terminating.                                                                 |
| Initialized                   | Thread has be initialized.                                                             |
| Waiting for next activation   | The event queue contains items, but the next activation is at some time in the future. |
| Waiting for scheduler to stop | Waiting for the event scheduler to stop after issuing SET GLOBAL event\_scheduler=OFF. |
| Waiting on empty queue        | Sleeping, as the event scheduler's queue is empty.                                     |

CC BY-SA / Gnu FDL
