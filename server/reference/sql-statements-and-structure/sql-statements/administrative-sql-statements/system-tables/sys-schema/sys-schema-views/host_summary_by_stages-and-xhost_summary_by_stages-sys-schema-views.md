
# host_summary_by_stages and x$host_summary_by_stages Sys Schema Views


##### MariaDB starting with [10.6](../../../../../../../../release-notes/mariadb-community-server/what-is-mariadb-106.md)
These [Sys Schema](sys-schema-views-host_summary_by_statement_latency-and-xhost_summary_by_sta.md) views were introduced in [MariaDB 10.6](../../../../../../../../release-notes/mariadb-community-server/what-is-mariadb-106.md).


## Description


The `<code>host_summary_by_stages</code>` and `<code>x$host_summary_by_stages</code>` views summarize statement stages, grouped by host. Rows are sorted by host and descending total latency by default. The `<code>host_summary_by_stages</code>` view is intended to be easier for human reading, while the `<code>x$host_summary_by_stages</code>` view provides the data in raw form, intended for tools that process the data.


They contain the following columns:



| Column | Description |
| --- | --- |
| Column | Description |
| host | Host that the client connected from, or background for background threads (where the HOST column in the underlying Performance Schema table is NULL). |
| event_name | Stage event name. |
| total | Total number of occurrences of the file stage event for the host. |
| total_latency | Total wait time of timed occurrences of the stage event for the host. |
| avg_latency | Average wait time per timed occurrence of the stage event for the host. |



## Example


```
SELECT * FROM sys.host_summary_by_stages\G
*************************** 1. row ***************************
         host: background
   event_name: stage/innodb/buffer pool load
        total: 1
total_latency: 3.75 ms
  avg_latency: 3.75 ms

SELECT * FROM sys.x$host_summary_by_stages\G
*************************** 1. row ***************************
         host: background
   event_name: stage/innodb/buffer pool load
        total: 1
total_latency: 3747098000
  avg_latency: 3747098000
```
