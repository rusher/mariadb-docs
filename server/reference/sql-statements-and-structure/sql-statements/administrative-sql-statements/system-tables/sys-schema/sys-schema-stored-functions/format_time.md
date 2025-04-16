
# format_time

## Syntax


```
sys.format_time(picoseconds)
```

## Description


`format_time` is a [stored function](../../../../../../../server-usage/programming-customizing-mariadb/stored-routines/stored-functions/README.md) available with the [Sys Schema](../sys-schema-views/sys-schema-views-host_summary_by_statement_latency-and-xhost_summary_by_sta.md). Given a time in picoseconds, returns a human-readable time value and unit indicator. Unit can be:


* ps - picoseconds
* ns - nanoseconds
* us - microseconds
* ms - milliseconds
* s - seconds
* m - minutes
* h - hours
* d - days
* w - weeks


This function is very similar to the [FORMAT_PICO_TIME](../../../../built-in-functions/date-time-functions/format_pico_time.md) function introduced in [MariaDB 11.0.2](../../../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-0-series/mariadb-11-0-2-release-notes.md), but with the following differences:


* Represents minutes as `m` rather than `min`.
* Represent weeks.


## Examples


```
SELECT
    sys.format_time(43) AS ps,
    sys.format_time(4321) AS ns, 
    sys.format_time(43211234) AS us,
    sys.format_time(432112344321) AS ms,
    sys.format_time(43211234432123) AS s,
    sys.format_time(432112344321234) AS m,
    sys.format_time(4321123443212345) AS h,
    sys.format_time(432112344321234545) AS d,
    sys.format_time(43211234432123444543) AS w;
+-------+---------+----------+-----------+---------+--------+--------+--------+---------+
| ps    | ns      | us       | ms        | s       | m      | h      | d      | w       |
+-------+---------+----------+-----------+---------+--------+--------+--------+---------+
| 43 ps | 4.32 ns | 43.21 us | 432.11 ms | 43.21 s | 7.20 m | 1.20 h | 5.00 d | 71.45 w |
+-------+---------+----------+-----------+---------+--------+--------+--------+---------+
```
