
# Performance Schema table_lock_waits_summary_by_table Table

The `<code>table_lock_waits_summary_by_table</code>` table records table lock waits by table.



| Column | Description |
| --- | --- |
| Column | Description |
| OBJECT_TYPE | Since this table records waits by table, always set to TABLE. |
| OBJECT_SCHEMA | Schema name. |
| OBJECT_NAME | Table name. |
| COUNT_STAR | Number of summarized events and the sum of the x_READ and x_WRITE columns. |
| SUM_TIMER_WAIT | Total wait time of the summarized events that are timed. |
| MIN_TIMER_WAIT | Minimum wait time of the summarized events that are timed. |
| AVG_TIMER_WAIT | Average wait time of the summarized events that are timed. |
| MAX_TIMER_WAIT | Maximum wait time of the summarized events that are timed. |
| COUNT_READ | Number of all read operations, and the sum of the equivalent x_READ_NORMAL, x_READ_WITH_SHARED_LOCKS, x_READ_HIGH_PRIORITY and x_READ_NO_INSERT columns. |
| SUM_TIMER_READ | Total wait time of all read operations that are timed. |
| MIN_TIMER_READ | Minimum wait time of all read operations that are timed. |
| AVG_TIMER_READ | Average wait time of all read operations that are timed. |
| MAX_TIMER_READ | Maximum wait time of all read operations that are timed. |
| COUNT_WRITE | Number of all write operations, and the sum of the equivalent x_WRITE_ALLOW_WRITE, x_WRITE_CONCURRENT_INSERT, x_WRITE_DELAYED, x_WRITE_LOW_PRIORITY and x_WRITE_NORMAL columns. |
| SUM_TIMER_WRITE | Total wait time of all write operations that are timed. |
| MIN_TIMER_WRITE | Minimum wait time of all write operations that are timed. |
| AVG_TIMER_WRITE | Average wait time of all write operations that are timed. |
| MAX_TIMER_WRITE | Maximum wait time of all write operations that are timed. |
| COUNT_READ_NORMAL | Number of all internal read normal locks. |
| SUM_TIMER_READ_NORMAL | Total wait time of all internal read normal locks that are timed. |
| MIN_TIMER_READ_NORMAL | Minimum wait time of all internal read normal locks that are timed. |
| AVG_TIMER_READ_NORMAL | Average wait time of all internal read normal locks that are timed. |
| MAX_TIMER_READ_NORMAL | Maximum wait time of all internal read normal locks that are timed. |
| COUNT_READ_WITH_SHARED_LOCKS | Number of all internal read with shared locks. |
| SUM_TIMER_READ_WITH_SHARED_LOCKS | Total wait time of all internal read with shared locks that are timed. |
| MIN_TIMER_READ_WITH_SHARED_LOCKS | Minimum wait time of all internal read with shared locks that are timed. |
| AVG_TIMER_READ_WITH_SHARED_LOCKS | Average wait time of all internal read with shared locks that are timed. |
| MAX_TIMER_READ_WITH_SHARED_LOCKS | Maximum wait time of all internal read with shared locks that are timed. |
| COUNT_READ_HIGH_PRIORITY | Number of all internal read high priority locks. |
| SUM_TIMER_READ_HIGH_PRIORITY | Total wait time of all internal read high priority locks that are timed. |
| MIN_TIMER_READ_HIGH_PRIORITY | Minimum wait time of all internal read high priority locks that are timed. |
| AVG_TIMER_READ_HIGH_PRIORITY | Average wait time of all internal read high priority locks that are timed. |
| MAX_TIMER_READ_HIGH_PRIORITY | Maximum wait time of all internal read high priority locks that are timed. |
| COUNT_READ_NO_INSERT | Number of all internal read no insert locks. |
| SUM_TIMER_READ_NO_INSERT | Total wait time of all internal read no insert locks that are timed. |
| MIN_TIMER_READ_NO_INSERT | Minimum wait time of all internal read no insert locks that are timed. |
| AVG_TIMER_READ_NO_INSERT | Average wait time of all internal read no insert locks that are timed. |
| MAX_TIMER_READ_NO_INSERT | Maximum wait time of all internal read no insert locks that are timed. |
| COUNT_READ_EXTERNAL | Number of all external read locks. |
| SUM_TIMER_READ_EXTERNAL | Total wait time of all external read locks that are timed. |
| MIN_TIMER_READ_EXTERNAL | Minimum wait time of all external read locks that are timed. |
| AVG_TIMER_READ_EXTERNAL | Average wait time of all external read locks that are timed. |
| MAX_TIMER_READ_EXTERNAL | Maximum wait time of all external read locks that are timed. |
| COUNT_WRITE_ALLOW_WRITE | Number of all internal read normal locks. |
| SUM_TIMER_WRITE_ALLOW_WRITE | Total wait time of all internal write allow write locks that are timed. |
| MIN_TIMER_WRITE_ALLOW_WRITE | Minimum wait time of all internal write allow write locks that are timed. |
| AVG_TIMER_WRITE_ALLOW_WRITE | Average wait time of all internal write allow write locks that are timed. |
| MAX_TIMER_WRITE_ALLOW_WRITE | Maximum wait time of all internal write allow write locks that are timed. |
| COUNT_WRITE_CONCURRENT_INSERT | Number of all internal concurrent insert write locks. |
| SUM_TIMER_WRITE_CONCURRENT_INSERT | Total wait time of all internal concurrent insert write locks that are timed. |
| MIN_TIMER_WRITE_CONCURRENT_INSERT | Minimum wait time of all internal concurrent insert write locks that are timed. |
| AVG_TIMER_WRITE_CONCURRENT_INSERT | Average wait time of all internal concurrent insert write locks that are timed. |
| MAX_TIMER_WRITE_CONCURRENT_INSERT | Maximum wait time of all internal concurrent insert write locks that are timed. |
| COUNT_WRITE_DELAYED | Number of all internal write delayed locks. |
| SUM_TIMER_WRITE_DELAYED | Total wait time of all internal write delayed locks that are timed. |
| MIN_TIMER_WRITE_DELAYED | Minimum wait time of all internal write delayed locks that are timed. |
| AVG_TIMER_WRITE_DELAYED | Average wait time of all internal write delayed locks that are timed. |
| MAX_TIMER_WRITE_DELAYED | Maximum wait time of all internal write delayed locks that are timed. |
| COUNT_WRITE_LOW_PRIORITY | Number of all internal write low priority locks. |
| SUM_TIMER_WRITE_LOW_PRIORITY | Total wait time of all internal write low priority locks that are timed. |
| MIN_TIMER_WRITE_LOW_PRIORITY | Minimum wait time of all internal write low priority locks that are timed. |
| AVG_TIMER_WRITE_LOW_PRIORITY | Average wait time of all internal write low priority locks that are timed. |
| MAX_TIMER_WRITE_LOW_PRIORITY | Maximum wait time of all internal write low priority locks that are timed. |
| COUNT_WRITE_NORMAL | Number of all internal write normal locks. |
| SUM_TIMER_WRITE_NORMAL | Total wait time of all internal write normal locks that are timed. |
| MIN_TIMER_WRITE_NORMAL | Minimum wait time of all internal write normal locks that are timed. |
| AVG_TIMER_WRITE_NORMAL | Average wait time of all internal write normal locks that are timed. |
| MAX_TIMER_WRITE_NORMAL | Maximum wait time of all internal write normal locks that are timed. |
| COUNT_WRITE_EXTERNAL | Number of all external write locks. |
| SUM_TIMER_WRITE_EXTERNAL | Total wait time of all external write locks that are timed. |
| MIN_TIMER_WRITE_EXTERNAL | Minimum wait time of all external write locks that are timed. |
| AVG_TIMER_WRITE_EXTERNAL | Average wait time of all external write locks that are timed. |
| MAX_TIMER_WRITE_EXTERNAL | Maximum wait time of all external write locks that are timed. |



You can [TRUNCATE](../../../../table-statements/truncate-table.md) the table, which will reset all counters to zero.

