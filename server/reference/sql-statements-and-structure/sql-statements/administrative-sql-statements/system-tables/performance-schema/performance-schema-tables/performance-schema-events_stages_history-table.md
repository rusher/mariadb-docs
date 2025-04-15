# Performance Schema events_stages_history Table

The `events_stages_history` table by default contains the ten most recent completed stage events per thread. This number can be adjusted by setting the [performance_schema_events_stages_history_size](../performance-schema-system-variables.md#performance_schema_events_stages_history_size) system variable when the server starts up.

The table structure is identical to the [events_stage_current](performance-schema-events_stages_current-table.md) table structure, and contains the following columns:

| Column | Description |
| --- | --- |
| Column | Description |
| THREAD_ID | Thread associated with the event. Together with EVENT_ID uniquely identifies the row. |
| EVENT_ID | Thread's current event number at the start of the event. Together with THREAD_ID uniquely identifies the row. |
| END_EVENT_ID | NULL when the event starts, set to the thread's current event number at the end of the event. |
| EVENT_NAME | Event instrument name and a NAME from the setup_instruments table |
| SOURCE | Name and line number of the source file containing the instrumented code that produced the event. |
| TIMER_START | Value in picoseconds when the event timing started or NULL if timing is not collected. Relative to the server start, not to the epoch, so cannot directly be converted to a timestamp. |
| TIMER_END | Value in picoseconds when the event timing ended, or NULL if timing is not collected. Relative to the server start, not to the epoch, so cannot directly be converted to a timestamp. |
| TIMER_WAIT | Value in picoseconds of the event's duration or NULL if timing is not collected. |
| NESTING_EVENT_ID | EVENT_ID of event within which this event nests. |
| NESTING_EVENT_TYPE | Nesting event type. One of transaction, statement, stage or wait. |

It is possible to empty this table with a `TRUNCATE TABLE` statement.

[events_stages_current](performance-schema-events_stages_current-table.md) and [events_stages_history_long](performance-schema-events_stages_history_long-table.md) are related tables.