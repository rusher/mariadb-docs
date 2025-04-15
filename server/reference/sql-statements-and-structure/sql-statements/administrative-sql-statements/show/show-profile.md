
# SHOW PROFILE

## Syntax


```
SHOW PROFILE [type [, type] ... ]
    [FOR QUERY n]
    [LIMIT row_count [OFFSET offset]]

type:
    ALL
  | BLOCK IO
  | CONTEXT SWITCHES
  | CPU
  | IPC
  | MEMORY
  | PAGE FAULTS
  | SOURCE
  | SWAPS
```

## Description


The `<code class="highlight fixed" style="white-space:pre-wrap">SHOW PROFILE</code>` and 
`<code class="highlight fixed" style="white-space:pre-wrap">[SHOW PROFILES](show-profiles.md)</code>` statements display profiling
information that indicates resource usage for statements executed during the
course of the current session.


Profiling is controlled by the [profiling](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#profiling) session variable, which has a default value of `<code>0</code>` (`<code>OFF</code>`). Profiling is enabled by setting profiling to `<code>1</code>` or `<code>ON</code>`:


```
SET profiling = 1;
```

`<code class="highlight fixed" style="white-space:pre-wrap">SHOW PROFILES</code>` displays a list of the most recent statements
sent to the master. The size of the list is controlled by the
`<code>[profiling_history_size](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#profiling_history_size)</code>` session variable, which has a default value of `<code>15</code>`. The maximum value is `<code>100</code>`. Setting the value to `<code>0</code>` has the practical effect of disabling profiling.


All statements are profiled except `<code class="highlight fixed" style="white-space:pre-wrap">SHOW PROFILES</code>` and 
`<code class="highlight fixed" style="white-space:pre-wrap">SHOW PROFILE</code>`, so you will find neither of those statements
in the profile list. Malformed statements are profiled. For example, 
 `<code class="highlight fixed" style="white-space:pre-wrap">SHOW PROFILING</code>` is an illegal statement, and a syntax error
occurs if you try to execute it, but it will show up in the profiling list.


`<code class="highlight fixed" style="white-space:pre-wrap">SHOW PROFILE</code>` displays detailed information about a single
statement. Without the `<code class="highlight fixed" style="white-space:pre-wrap">FOR QUERY <em>n</em></code>` clause, the output
pertains to the most recently executed statement. If 
 `<code class="highlight fixed" style="white-space:pre-wrap">FOR QUERY <em>n</em></code>` is included,
 `<code class="highlight fixed" style="white-space:pre-wrap">SHOW PROFILE</code>` displays information for statement *n*. The
values of *n* correspond to
the `<code class="highlight fixed" style="white-space:pre-wrap">Query_ID</code>` values displayed by `<code class="highlight fixed" style="white-space:pre-wrap">SHOW PROFILES</code>`.


The `<code class="highlight fixed" style="white-space:pre-wrap">LIMIT <em>row_count</em></code>` clause may be given to limit the
output to *row_count* rows. If `<code class="highlight fixed" style="white-space:pre-wrap">LIMIT</code>` is given, 
 `<code class="highlight fixed" style="white-space:pre-wrap">OFFSET <em>offset</em></code>` may be added to begin the output offset
rows into the full set of rows.


By default, `<code class="highlight fixed" style="white-space:pre-wrap">SHOW PROFILE</code>` displays Status and Duration
columns. The Status values are like the State values displayed by [SHOW PROCESSLIST](show-processlist.md) (see [General Thread States](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/buffers-caches-and-threads/thread-states/general-thread-states.md)), although there might be some minor differences in interpretation for the two statements for some status values.


Optional type values may be specified to display specific additional types of information:


* `<code class="highlight fixed" style="white-space:pre-wrap"><strong>ALL</strong></code>` displays all information
* `<code class="highlight fixed" style="white-space:pre-wrap"><strong>BLOCK IO</strong></code>` displays counts for block input and output operations
* `<code class="highlight fixed" style="white-space:pre-wrap"><strong>CONTEXT SWITCHES</strong></code>` displays counts for voluntary and involuntary context switches
* `<code class="highlight fixed" style="white-space:pre-wrap"><strong>CPU</strong></code>` displays user and system CPU usage times
* `<code class="highlight fixed" style="white-space:pre-wrap"><strong>IPC</strong></code>` displays counts for messages sent and received
* `<code class="highlight fixed" style="white-space:pre-wrap"><strong>MEMORY</strong></code>` is not currently implemented
* `<code class="highlight fixed" style="white-space:pre-wrap"><strong>PAGE FAULTS</strong></code>` displays counts for major and minor page faults
* `<code class="highlight fixed" style="white-space:pre-wrap"><strong>SOURCE</strong></code>` displays the names of functions from the source code, together with the name and line number of the file in which the function occurs
* `<code class="highlight fixed" style="white-space:pre-wrap"><strong>SWAPS</strong></code>` displays swap counts


Profiling is enabled per session. When a session ends, its profiling information is lost.


The `<code>[information_schema.PROFILING](../system-tables/information-schema/information-schema-tables/information-schema-profiling-table.md) table contains similar information.</code>`


## Examples


```
SELECT @@profiling;
+-------------+
| @@profiling |
+-------------+
|           0 |
+-------------+

SET profiling = 1;

USE test;

DROP TABLE IF EXISTS t1;

CREATE TABLE T1 (id INT);

SHOW PROFILES;
+----------+------------+--------------------------+
| Query_ID | Duration   | Query                    |
+----------+------------+--------------------------+
|        1 | 0.00009200 | SELECT DATABASE()        |
|        2 | 0.00023800 | show databases           |
|        3 | 0.00018900 | show tables              |
|        4 | 0.00014700 | DROP TABLE IF EXISTS t1  |
|        5 | 0.24476900 | CREATE TABLE T1 (id INT) |
+----------+------------+--------------------------+

SHOW PROFILE;
+----------------------+----------+
| Status               | Duration |
+----------------------+----------+
| starting             | 0.000042 |
| checking permissions | 0.000044 |
| creating table       | 0.244645 |
| After create         | 0.000013 |
| query end            | 0.000003 |
| freeing items        | 0.000016 |
| logging slow query   | 0.000003 |
| cleaning up          | 0.000003 |
+----------------------+----------+

SHOW PROFILE FOR QUERY 4;
+--------------------+----------+
| Status             | Duration |
+--------------------+----------+
| starting           | 0.000126 |
| query end          | 0.000004 |
| freeing items      | 0.000012 |
| logging slow query | 0.000003 |
| cleaning up        | 0.000002 |
+--------------------+----------+

SHOW PROFILE CPU FOR QUERY 5;
+----------------------+----------+----------+------------+
| Status               | Duration | CPU_user | CPU_system |
+----------------------+----------+----------+------------+
| starting             | 0.000042 | 0.000000 |   0.000000 |
| checking permissions | 0.000044 | 0.000000 |   0.000000 |
| creating table       | 0.244645 | 0.000000 |   0.000000 |
| After create         | 0.000013 | 0.000000 |   0.000000 |
| query end            | 0.000003 | 0.000000 |   0.000000 |
| freeing items        | 0.000016 | 0.000000 |   0.000000 |
| logging slow query   | 0.000003 | 0.000000 |   0.000000 |
| cleaning up          | 0.000003 | 0.000000 |   0.000000 |
+----------------------+----------+----------+------------+
```
