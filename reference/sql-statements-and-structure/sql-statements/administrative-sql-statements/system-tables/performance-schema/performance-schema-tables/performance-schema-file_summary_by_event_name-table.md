# Performance Schema file_summary_by_event_name Table

The [Performance Schema](../performance-schema-status-variables.md) `file_summary_by_event_name` table contains file events summarized by event name. It contains the following columns:

| Column | Description |
| --- | --- |
| Column | Description |
| EVENT_NAME | Event name. |
| COUNT_STAR | Number of summarized events |
| SUM_TIMER_WAIT | Total wait time of the summarized events that are timed. |
| MIN_TIMER_WAIT | Minimum wait time of the summarized events that are timed. |
| AVG_TIMER_WAIT | Average wait time of the summarized events that are timed. |
| MAX_TIMER_WAIT | Maximum wait time of the summarized events that are timed. |
| COUNT_READ | Number of all read operations, including FGETS, FGETC, FREAD, and READ. |
| SUM_TIMER_READ | Total wait time of all read operations that are timed. |
| MIN_TIMER_READ | Minimum wait time of all read operations that are timed. |
| AVG_TIMER_READ | Average wait time of all read operations that are timed. |
| MAX_TIMER_READ | Maximum wait time of all read operations that are timed. |
| SUM_NUMBER_OF_BYTES_READ | Bytes read by read operations. |
| COUNT_WRITE | Number of all write operations, including FPUTS, FPUTC, FPRINTF, VFPRINTF, FWRITE, and PWRITE. |
| SUM_TIMER_WRITE | Total wait time of all write operations that are timed. |
| MIN_TIMER_WRITE | Minimum wait time of all write operations that are timed. |
| AVG_TIMER_WRITE | Average wait time of all write operations that are timed. |
| MAX_TIMER_WRITE | Maximum wait time of all write operations that are timed. |
| SUM_NUMBER_OF_BYTES_WRITE | Bytes written by write operations. |
| COUNT_MISC | Number of all miscellaneous operations not counted above, including CREATE, DELETE, OPEN, CLOSE, STREAM_OPEN, STREAM_CLOSE, SEEK, TELL, FLUSH, STAT, FSTAT, CHSIZE, RENAME, and SYNC. |
| SUM_TIMER_MISC | Total wait time of all miscellaneous operations that are timed. |
| MIN_TIMER_MISC | Minimum wait time of all miscellaneous operations that are timed. |
| AVG_TIMER_MISC | Average wait time of all miscellaneous operations that are timed. |
| MAX_TIMER_MISC | Maximum wait time of all miscellaneous operations that are timed. |

I/O operations can be avoided by caching, in which case they will not be recorded in this table.

You can [TRUNCATE](../../../../table-statements/truncate-table.md) the table, which will reset all counters to zero.

#

# Example

```
SELECT * FROM file_summary_by_event_name\G
...
*************************** 49. row ***************************
 EVENT_NAME: wait/io/file/aria/MAD
 COUNT_STAR: 60
 SUM_TIMER_WAIT: 397234368
 MIN_TIMER_WAIT: 0
 AVG_TIMER_WAIT: 6620224
 MAX_TIMER_WAIT: 16808672
 COUNT_READ: 0
 SUM_TIMER_READ: 0
 MIN_TIMER_READ: 0
 AVG_TIMER_READ: 0
 MAX_TIMER_READ: 0
 SUM_NUMBER_OF_BYTES_READ: 0
 COUNT_WRITE: 0
 SUM_TIMER_WRITE: 0
 MIN_TIMER_WRITE: 0
 AVG_TIMER_WRITE: 0
 MAX_TIMER_WRITE: 0
SUM_NUMBER_OF_BYTES_WRITE: 0
 COUNT_MISC: 60
 SUM_TIMER_MISC: 397234368
 MIN_TIMER_MISC: 0
 AVG_TIMER_MISC: 6620224
 MAX_TIMER_MISC: 16808672
*************************** 50. row ***************************
 EVENT_NAME: wait/io/file/aria/control
 COUNT_STAR: 3
 SUM_TIMER_WAIT: 24055778544
 MIN_TIMER_WAIT: 0
 AVG_TIMER_WAIT: 8018592848
 MAX_TIMER_WAIT: 24027262400
 COUNT_READ: 1
 SUM_TIMER_READ: 24027262400
 MIN_TIMER_READ: 0
 AVG_TIMER_READ: 24027262400
 MAX_TIMER_READ: 24027262400
 SUM_NUMBER_OF_BYTES_READ: 52
 COUNT_WRITE: 0
 SUM_TIMER_WRITE: 0
 MIN_TIMER_WRITE: 0
 AVG_TIMER_WRITE: 0
 MAX_TIMER_WRITE: 0
SUM_NUMBER_OF_BYTES_WRITE: 0
 COUNT_MISC: 2
 SUM_TIMER_MISC: 28516144
 MIN_TIMER_MISC: 0
 AVG_TIMER_MISC: 14258072
 MAX_TIMER_MISC: 27262208
```