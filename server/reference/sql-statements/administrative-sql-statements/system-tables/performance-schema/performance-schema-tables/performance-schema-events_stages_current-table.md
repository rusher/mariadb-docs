
# Performance Schema events_stages_current Table

The `events_stages_current` table contains current stage events, with each row being a record of a thread and its most recent stage event.


The table contains the following columns:



| Column | Description |
| --- | --- |
| Column | Description |
| THREAD_ID | Thread associated with the event. Together with EVENT_ID uniquely identifies the row. |
| EVENT_ID | Thread's current event number at the start of the event. Together with THREAD_ID uniquely identifies the row. |
| END_EVENT_ID | NULL when the event starts, set to the thread's current event number at the end of the event. |
| EVENT_NAME | Event instrument name and a NAME from the setup_instruments table |
| SOURCE | Name and line number of the source file containing the instrumented code that produced the event. |
| TIMER_START | Value in picoseconds when the event timing started or NULL if timing is not collected. Relative to the server start, not to the epoch, so cannot directly be converted to a timestamp. |
| TIMER_END | Value in picoseconds when the event timing ended, or NULL if the event has not ended or timing is not collected. Relative to the server start, not to the epoch, so cannot directly be converted to a timestamp. |
| TIMER_WAIT | Value in picoseconds of the event's duration or NULL if the event has not ended or timing is not collected. |
| NESTING_EVENT_ID | EVENT_ID of event within which this event nests. |
| NESTING_EVENT_TYPE | Nesting event type. One of transaction, statement, stage or wait. |



It is possible to empty this table with a `TRUNCATE TABLE` statement.


The related tables, [events_stages_history](performance-schema-events_stages_history-table.md) and [events_stages_history_long](performance-schema-events_stages_history_long-table.md) derive their values from the current events.


CC BY-SA / Gnu FDL

