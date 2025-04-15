
# Information Schema OPTIMIZER_TRACE Table

## Description


The [Information Schema](../../../../../../mariadb-internals/information-schema-plugins-show-and-flush-statements.md) `<code>OPTIMIZER_TRACE</code>` table contains [Optimizer Trace](../../../../../../mariadb-internals/mariadb-internals-documentation-query-optimizer/mariadb-internals-documentation-optimizer-trace/optimizer-trace-for-developers.md) information.


It contains the following columns:



| Column | Description |
| --- | --- |
| Column | Description |
| QUERY | Displays the query that was asked to be traced. |
| TRACE | A JSON document displaying the stats we collected when the query was run. |
| MISSING_BYTES_BEYOND_MAX_MEM_SIZE | For huge trace, where the trace is truncated due to the optimizer_trace_max_mem_size limit being reached, displays the bytes that are missing in the trace |
| INSUFFICENT_PRIVILEGES | Set to 1 if the user running the trace does not have the privileges to see the trace. |



Structure:


```
SHOW CREATE TABLE INFORMATION_SCHEMA.OPTIMIZER_TRACE \G
*************************** 1. row ***************************
       Table: OPTIMIZER_TRACE
Create Table: CREATE TEMPORARY TABLE `OPTIMIZER_TRACE` (
  `QUERY` longtext NOT NULL DEFAULT '',
  `TRACE` longtext NOT NULL DEFAULT '',
  `MISSING_BYTES_BEYOND_MAX_MEM_SIZE` int(20) NOT NULL DEFAULT 0,
  `INSUFFICIENT_PRIVILEGES` tinyint(1) NOT NULL DEFAULT 0
) ENGINE=Aria DEFAULT CHARSET=utf8 PAGE_CHECKSUM=0
```
