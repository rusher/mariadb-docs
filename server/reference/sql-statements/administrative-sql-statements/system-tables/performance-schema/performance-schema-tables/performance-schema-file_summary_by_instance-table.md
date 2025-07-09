
# Performance Schema file_summary_by_instance Table

The [Performance Schema](../README.md) `file_summary_by_instance` table contains file events summarized by instance. It contains the following columns:



| Column | Description |
| --- | --- |
| Column | Description |
| FILE_NAME | File name. |
| EVENT_NAME | Event name. |
| OBJECT_INSTANCE_BEGIN | Address in memory. Together with FILE_NAME and EVENT_NAME uniquely identifies a row. |
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


## Example


```
SELECT * FROM file_summary_by_instance\G
...
*************************** 204. row ***************************
                FILE_NAME: /var/lib/mysql/test/db.opt
               EVENT_NAME: wait/io/file/sql/dbopt
    OBJECT_INSTANCE_BEGIN: 140578961971264
               COUNT_STAR: 6
           SUM_TIMER_WAIT: 39902495024
           MIN_TIMER_WAIT: 177888
           AVG_TIMER_WAIT: 6650415692
           MAX_TIMER_WAIT: 21026400404
               COUNT_READ: 1
           SUM_TIMER_READ: 21026400404
           MIN_TIMER_READ: 21026400404
           AVG_TIMER_READ: 21026400404
           MAX_TIMER_READ: 21026400404
 SUM_NUMBER_OF_BYTES_READ: 65
              COUNT_WRITE: 0
          SUM_TIMER_WRITE: 0
          MIN_TIMER_WRITE: 0
          AVG_TIMER_WRITE: 0
          MAX_TIMER_WRITE: 0
SUM_NUMBER_OF_BYTES_WRITE: 0
               COUNT_MISC: 5
           SUM_TIMER_MISC: 18876094620
           MIN_TIMER_MISC: 177888
           AVG_TIMER_MISC: 3775218924
           MAX_TIMER_MISC: 18864558060
*************************** 205. row ***************************
                FILE_NAME: /var/log/mysql/mariadb-bin.000157
               EVENT_NAME: wait/io/file/sql/binlog
    OBJECT_INSTANCE_BEGIN: 140578961971968
               COUNT_STAR: 6
           SUM_TIMER_WAIT: 73985877680
           MIN_TIMER_WAIT: 251136
           AVG_TIMER_WAIT: 12330979468
           MAX_TIMER_WAIT: 73846656340
               COUNT_READ: 0
           SUM_TIMER_READ: 0
           MIN_TIMER_READ: 0
           AVG_TIMER_READ: 0
           MAX_TIMER_READ: 0
 SUM_NUMBER_OF_BYTES_READ: 0
              COUNT_WRITE: 2
          SUM_TIMER_WRITE: 62583004
          MIN_TIMER_WRITE: 27630192
          AVG_TIMER_WRITE: 31291284
          MAX_TIMER_WRITE: 34952812
SUM_NUMBER_OF_BYTES_WRITE: 369
               COUNT_MISC: 4
           SUM_TIMER_MISC: 73923294676
           MIN_TIMER_MISC: 251136
           AVG_TIMER_MISC: 18480823560
           MAX_TIMER_MISC: 73846656340
```


<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>


{% @marketo/form formId="4316" %}
