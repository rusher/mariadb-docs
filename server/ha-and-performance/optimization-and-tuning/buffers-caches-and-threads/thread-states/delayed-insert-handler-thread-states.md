# Delayed Insert Handler Thread States

This article documents thread states that are related to the handler thread that inserts the results of [INSERT DELAYED](../../../../reference/sql-statements/data-manipulation/inserting-loading-data/insert-delayed.md) statements.

These correspond to the `STATE` values listed by the [SHOW PROCESSLIST](../../../../reference/sql-statements/administrative-sql-statements/show/show-processlist.md) statement or in the [Information Schema PROCESSLIST Table](../../../../reference/system-tables/information-schema/information-schema-tables/information-schema-processlist-table.md) as well as the `PROCESSLIST_STATE` value listed in the [Performance Schema threads Table](../../../../reference/system-tables/performance-schema/performance-schema-tables/performance-schema-threads-table.md).

| Value              | Description                                                                                       |
| ------------------ | ------------------------------------------------------------------------------------------------- |
| insert             | About to insert rows into the table.                                                              |
| reschedule         | Sleeping in order to let other threads function, after inserting a number of rows into the table. |
| upgrading lock     | Attempting to get lock on the table in order to insert rows.                                      |
| Waiting for INSERT | Waiting for the delayed-insert connection thread to add rows to the queue.                        |

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
