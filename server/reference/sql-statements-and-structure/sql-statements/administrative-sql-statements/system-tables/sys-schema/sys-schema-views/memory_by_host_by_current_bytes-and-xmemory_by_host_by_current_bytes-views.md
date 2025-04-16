
# memory_by_host_by_current_bytes and x$memory_by_host_by_current_bytes Views


##### MariaDB starting with [10.6](../../../../../../../../release-notes/mariadb-community-server/what-is-mariadb-106.md)
These [Sys Schema](sys-schema-views-host_summary_by_statement_latency-and-xhost_summary_by_sta.md) views were introduced in [MariaDB 10.6](../../../../../../../../release-notes/mariadb-community-server/what-is-mariadb-106.md).


## Description


The `memory_by_host_by_current_bytes` and `x$memory_by_host_by_current_bytes` summarize memory use grouped by host. Rows by default are sorted by descending amount of memory used.


The `memory_by_host_by_current_bytes` view is intended to be easier for human reading, while the `x$memory_by_host_by_current_bytes` view provides the data in raw form, intended for tools that process the data.


They contain the following columns:



| Column | Description |
| --- | --- |
| Column | Description |
| host | Host from which the client connected. If the HOST column in the underlying Performance Schema table is NULL, rows are assumed to be for background threads, and the background host name is used. |
| current_count_used | Current number of allocated memory blocks that have not yet been freed for the host. |
| current_allocated | Current number of allocated bytes that have not yet been freed for the host. |
| current_avg_alloc | Current number of allocated bytes per memory block for the host. |
| current_max_alloc | Largest single current memory allocation in bytes for the host. |
| total_allocated | Total memory allocation in bytes for the host. |


