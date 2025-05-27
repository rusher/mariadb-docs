
# Performance Schema socket_summary_by_instance Table

It aggregates timer and byte count statistics for all socket I/O operations by socket instance.



| Column | Description |
| --- | --- |
| Column | Description |
| EVENT_NAME | Socket instrument. |
| OBJECT_INSTANCE_BEGIN | Address in memory. |
| COUNT_STAR | Number of summarized events |
| SUM_TIMER_WAIT | Total wait time of the summarized events that are timed. |
| MIN_TIMER_WAIT | Minimum wait time of the summarized events that are timed. |
| AVG_TIMER_WAIT | Average wait time of the summarized events that are timed. |
| MAX_TIMER_WAIT | Maximum wait time of the summarized events that are timed. |
| COUNT_READ | Number of all read operations, including RECV, RECVFROM, and RECVMSG. |
| SUM_TIMER_READ | Total wait time of all read operations that are timed. |
| MIN_TIMER_READ | Minimum wait time of all read operations that are timed. |
| AVG_TIMER_READ | Average wait time of all read operations that are timed. |
| MAX_TIMER_READ | Maximum wait time of all read operations that are timed. |
| SUM_NUMBER_OF_BYTES_READ | Bytes read by read operations. |
| COUNT_WRITE | Number of all write operations, including SEND, SENDTO, and SENDMSG. |
| SUM_TIMER_WRITE | Total wait time of all write operations that are timed. |
| MIN_TIMER_WRITE | Minimum wait time of all write operations that are timed. |
| AVG_TIMER_WRITE | Average wait time of all write operations that are timed. |
| MAX_TIMER_WRITE | Maximum wait time of all write operations that are timed. |
| SUM_NUMBER_OF_BYTES_WRITE | Bytes written by write operations. |
| COUNT_MISC | Number of all miscellaneous operations not counted above, including CONNECT, LISTEN, ACCEPT, CLOSE, and SHUTDOWN. |
| SUM_TIMER_MISC | Total wait time of all miscellaneous operations that are timed. |
| MIN_TIMER_MISC | Minimum wait time of all miscellaneous operations that are timed. |
| AVG_TIMER_MISC | Average wait time of all miscellaneous operations that are timed. |
| MAX_TIMER_MISC | Maximum wait time of all miscellaneous operations that are timed. |



The corresponding row in the table is deleted when a connection terminates.


You can [TRUNCATE](../../../../table-statements/truncate-table.md) the table, which will reset all counters to zero.


CC BY-SA / Gnu FDL

