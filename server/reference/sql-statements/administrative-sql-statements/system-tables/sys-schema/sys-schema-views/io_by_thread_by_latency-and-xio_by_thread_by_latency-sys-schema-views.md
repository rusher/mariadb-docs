# io\_by\_thread\_by\_latency and x$io\_by\_thread\_by\_latency Sys Schema Views

**MariaDB starting with** [**10.6**](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-6-series/what-is-mariadb-106)

These [Sys Schema](../) views were introduced in [MariaDB 10.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-6-series/what-is-mariadb-106).

## Description

The `io_by_thread_by_latency` and `x$io_by_thread_by_latency` view summarize I/O consumers to display time waiting for I/O, grouped by thread. Rows are sorted by descending total I/O latency by default.

The `io_by_thread_by_latency` view is intended to be easier for human reading, while the `x$io_by_thread_by_latency` view provides the data in raw form, intended for tools that process the data.

They contain the following columns:

| Column          | Description                                                                    |
| --------------- | ------------------------------------------------------------------------------ |
| Column          | Description                                                                    |
| user            | The account associated with a foreground thread, or the background thread name |
| total           | Total number of I/O events allocated for the thread.                           |
| total\_latency  | Total wait time of timed I/O events for the thread.                            |
| min\_latency    | Minimum single wait time of timed I/O events for the thread.                   |
| avg\_latency    | Average wait time per timed I/O event for the thread.                          |
| min\_latency    | Maximum single wait time of timed I/O events for the thread.                   |
| thread\_id      | Thread id.                                                                     |
| processlist\_id | Processlist id for foreground threads, or NULL for background threads.         |

## Example

```
SELECT * FROM sys.io_by_thread_by_latency\G
*************************** 1. row ***************************
          user: main
         total: 378
 total_latency: 40.11 ms
   min_latency: 570.21 ns
   avg_latency: 206.02 us
   max_latency: 4.33 ms
     thread_id: 1
processlist_id: NULL
*************************** 2. row ***************************
          user: msandbox@localhost
         total: 521
 total_latency: 10.28 ms
   min_latency: 775.04 ns
   avg_latency: 21.79 us
   max_latency: 977.79 us
     thread_id: 89
processlist_id: 7

...

SELECT * FROM sys.x$io_by_thread_by_latency\G
*************************** 1. row ***************************
          user: main
         total: 378
 total_latency: 40106340880
   min_latency: 570208
   avg_latency: 206016046.6000
   max_latency: 4327780456
     thread_id: 1
processlist_id: NULL
*************************** 2. row ***************************
          user: msandbox@localhost
         total: 498
 total_latency: 9637694714
   min_latency: 775040
   avg_latency: 21364289.0000
   max_latency: 977787350
     thread_id: 89
processlist_id: 7

...
```

CC BY-SA / Gnu FDL
