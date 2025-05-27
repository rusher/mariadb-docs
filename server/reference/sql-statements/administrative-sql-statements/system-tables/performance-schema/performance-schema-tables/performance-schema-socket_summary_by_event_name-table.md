
# Performance Schema socket_summary_by_event_name Table

It aggregates timer and byte count statistics for all socket I/O operations by socket instrument.



| Column | Description |
| --- | --- |
| Column | Description |
| EVENT_NAME | Socket instrument. |
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



You can [TRUNCATE](../../../../table-statements/truncate-table.md) the table, which will reset all counters to zero.


## Example


```
SELECT * FROM socket_summary_by_event_name\G
*************************** 1. row ***************************
               EVENT_NAME: wait/io/socket/sql/server_tcpip_socket
               COUNT_STAR: 0
           SUM_TIMER_WAIT: 0
           MIN_TIMER_WAIT: 0
           AVG_TIMER_WAIT: 0
           MAX_TIMER_WAIT: 0
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
               COUNT_MISC: 0
           SUM_TIMER_MISC: 0
           MIN_TIMER_MISC: 0
           AVG_TIMER_MISC: 0
           MAX_TIMER_MISC: 0
*************************** 2. row ***************************
               EVENT_NAME: wait/io/socket/sql/server_unix_socket
               COUNT_STAR: 0
           SUM_TIMER_WAIT: 0
           MIN_TIMER_WAIT: 0
           AVG_TIMER_WAIT: 0
           MAX_TIMER_WAIT: 0
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
               COUNT_MISC: 0
           SUM_TIMER_MISC: 0
           MIN_TIMER_MISC: 0
           AVG_TIMER_MISC: 0
           MAX_TIMER_MISC: 0
...
```


CC BY-SA / Gnu FDL

