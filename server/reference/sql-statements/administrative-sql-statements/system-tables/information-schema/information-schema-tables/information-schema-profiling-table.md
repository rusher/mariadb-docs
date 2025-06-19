
# Information Schema PROFILING Table

The [Information Schema](../README.md) `PROFILING` table contains information about statement resource usage. Profiling information is only recorded if the [profiling](../../../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#profiling) session variable is set to 1.


It contains the following columns:



| Column Name | Description |
| --- | --- |
| Column Name | Description |
| QUERY_ID | Query_ID. |
| SEQ | Sequence number showing the display order for rows with the same QUERY_ID. |
| STATE | Profiling state. |
| DURATION | Time in seconds that the statement has been in the current state. |
| CPU_USER | User CPU usage in seconds. |
| CPU_SYSTEM | System CPU usage in seconds. |
| CONTEXT_VOLUNTARY | Number of voluntary context switches. |
| CONTEXT_INVOLUNTARY | Number of involuntary context switches. |
| BLOCK_OPS_IN | Number of block input operations. |
| BLOCK_OPS_OUT | Number of block output operations. |
| MESSAGES_SENT | Number of communications sent. |
| MESSAGES_RECEIVED | Number of communications received. |
| PAGE_FAULTS_MAJOR | Number of major page faults. |
| PAGE_FAULTS_MINOR | Number of minor page faults. |
| SWAPS | Number of swaps. |
| SOURCE_FUNCTION | Function in the source code executed by the profiled state. |
| SOURCE_FILE | File in the source code executed by the profiled state. |
| SOURCE_LINE | Line in the source code executed by the profiled state. |



It contains similar information to the `[SHOW PROFILE](../../../show/show-profile.md) and [SHOW PROFILES](../../../show/show-profiles.md)` statements.


Profiling is enabled per session. When a session ends, its profiling information is lost.


<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>


{% @marketo/form formId="4316" %}
