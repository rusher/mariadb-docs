
# io_global_by_file_by_latency and x$io_global_by_file_by_latency Sys Schema Views


##### MariaDB starting with [10.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-6-series/what-is-mariadb-106)
These [Sys Schema](../README.md) views were introduced in [MariaDB 10.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-6-series/what-is-mariadb-106).


## Description


The `io_global_by_file_by_latency` and `x$io_global_by_file_by_latency` views summarize global I/O consumers to display time waiting for I/O, grouped by file. Rows are sorted by descending total latency by default.


The `io_global_by_file_by_latency` view is intended to be easier for human reading, while the `x$io_global_by_file_by_latency` view provides the data in raw form, intended for tools that process the data.


They contain the following columns:



| Column | Description |
| --- | --- |
| Column | Description |
| file | File path name. |
| total | Total number of I/O events for the file. |
| total_latency | Total wait time of timed I/O events for the file. |
| count_read | Total number of read I/O events for the file. |
| read_latency | Total wait time of timed read I/O events for the file. |
| count_write | Total number of write I/O events for the file. |
| write_latency | Total wait time of timed write I/O events for the file. |
| count_misc | Total number of other I/O events for the file. |
| misc_latency | Total wait time of timed other I/O events for the file. |



## Example


```
SELECT * FROM sys.io_global_by_file_by_latency\G
*************************** 1. row ***************************
         file: @@datadir/ddl_recovery.log
        total: 222
total_latency: 288.64 ms
   count_read: 0
 read_latency: 0 ps
  count_write: 114
write_latency: 2.59 ms
   count_misc: 108
 misc_latency: 286.05 ms
*************************** 2. row ***************************
         file: @@datadir/ib_logfile0
        total: 95
total_latency: 165.29 ms
   count_read: 6
 read_latency: 61.04 us
  count_write: 43
write_latency: 1.31 ms
   count_misc: 46
 misc_latency: 163.92 ms
...

SELECT * FROM sys.x$io_global_by_file_by_latency\G
*************************** 1. row ***************************
         file: /home/ian/sandboxes/msb_10_6_19/data/ddl_recovery.log
        total: 222
total_latency: 288641408158
   count_read: 0
 read_latency: 0
  count_write: 114
write_latency: 2594925264
   count_misc: 108
 misc_latency: 286046482894
*************************** 2. row ***************************
         file: /home/ian/sandboxes/msb_10_6_19/data/ib_logfile0
        total: 95
total_latency: 165291020006
   count_read: 6
 read_latency: 61040974
  count_write: 43
write_latency: 1310187820
   count_misc: 46
 misc_latency: 163919791212
...
```
