
# io_global_by_file_by_bytes and x$io_global_by_file_by_bytes Sys Schema Views


##### MariaDB starting with [10.6](../../../../../../../../release-notes/mariadb-community-server/what-is-mariadb-106.md)
These [Sys Schema](sys-schema-views-host_summary_by_statement_latency-and-xhost_summary_by_sta.md) views were introduced in [MariaDB 10.6](../../../../../../../../release-notes/mariadb-community-server/what-is-mariadb-106.md).


## Description


The `<code>io_global_by_file_by_bytes</code>` and `<code>x$io_global_by_file_by_bytes</code>` views summarize global I/O consumers showing I/O in bytes, grouped by file. Rows are sorted by descending total I/O (bytes read and written) by default.


The `<code>io_global_by_file_by_bytes</code>` view is intended to be easier for human reading, while the `<code>x$io_global_by_file_by_bytes</code>` view provides the data in raw form, intended for tools that process the data.


They contain the following columns:



| Column | Description |
| --- | --- |
| Column | Description |
| file | File path name. |
| count_read | Total number of read events for the file. |
| total_read | Total number of bytes read from the file. |
| avg_read | Average number of bytes per read from the file. |
| count_write | Total number of write events for the file. |
| total_written | Total number of bytes written to the file. |
| avg_write | Average number of bytes per write to the file. |
| total | Total number of bytes read and written for the file. |
| write_pct | Percentage of total I/O bytes that were writes. |



## Example


```
SELECT * FROM sys.io_global_by_file_by_bytes\G
...
*************************** 3. row ***************************
         file: @@datadir/ddl_recovery.log
   count_read: 0
   total_read: 0 bytes
     avg_read: 0 bytes
  count_write: 114
total_written: 220.17 KiB
    avg_write: 1.93 KiB
        total: 220.17 KiB
    write_pct: 100.00
*************************** 4. row ***************************
         file: @@datadir/ib_logfile0
   count_read: 6
   total_read: 66.50 KiB
     avg_read: 11.08 KiB
  count_write: 43
total_written: 81.00 KiB
    avg_write: 1.88 KiB
        total: 147.50 KiB
    write_pct: 54.92
...

SELECT * FROM sys.x$io_global_by_file_by_bytes\G
...
*************************** 3. row ***************************
         file: /home/ian/sandboxes/msb_10_6_19/data/ddl_recovery.log
   count_read: 0
   total_read: 0
     avg_read: 0.0000
  count_write: 114
total_written: 225459
    avg_write: 1977.7105
        total: 225459
    write_pct: 100.00
*************************** 4. row ***************************
         file: /home/ian/sandboxes/msb_10_6_19/data/ib_logfile0
   count_read: 6
   total_read: 68096
     avg_read: 11349.3333
  count_write: 43
total_written: 82944
    avg_write: 1928.9302
        total: 151040
    write_pct: 54.92
...
```
