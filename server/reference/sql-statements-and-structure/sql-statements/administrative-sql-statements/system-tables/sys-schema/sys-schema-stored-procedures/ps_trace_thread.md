
# ps_trace_thread

## Syntax


```
ps_trace_thread(thread_id, outfile, max_runtime, interval, start_fresh, auto_setup, debug)
```

## Description


`ps_trace_thread` is a [stored procedure](../../../../../../../server-usage/programming-customizing-mariadb/stored-routines/stored-procedures/README.md) available with the [Sys Schema](../README.md).


Parameters:


* thread_id INT: The thread to trace.
* outfile VARCHAR(255): Name of the .dot file to be create.
* max_runtime DECIMAL(20,2): Maximum time in seconds to collect data. Fractional seconds can be used, and NULL results in data being collected for the default sixty seconds.
* interval DECIMAL(20,2): Time in seconds to sleep between data collection. Fractional seconds can be used, and NULL results in the sleep being the default one second.
* start_fresh BOOLEAN: Whether to reset all Performance Schema data before tracing.
* auto_setup BOOLEAN: Whether to disable all other threads, enable all instruments and consumers, and reset the settings at the end of the run.
* debug BOOLEAN: Whether to include file:lineno information in the graph.


Dumps all Performance Schema data for an instrumented thread to a .dot formatted graph file (for use with the [DOT graph description language](https://en.wikipedia.org/wiki/DOT_%28graph_description_language%29)). All returned result sets should be used for a complete graph.


Session [binary logging](../../../../../../../server-management/server-monitoring-logs/binary-log/README.md) is disabled during execution, by adjusting the [sql_log_bin](../../../../../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md#sql_log_bin) session value (note the permissions required).


## Examples


```
CALL sys.ps_trace_thread(25, CONCAT('/tmp/stack-', REPLACE(NOW(), ' ', '-'), '.dot'), 
  NULL, NULL, TRUE, TRUE, TRUE);

--------------------+
| summary            |
+--------------------+
| Disabled 0 threads |
+--------------------+

+---------------------------------------------+
| Info                                        |
+---------------------------------------------+
| Data collection starting for THREAD_ID = 25 |
+---------------------------------------------+

+-----------------------------------------------------------+
| Info                                                      |
+-----------------------------------------------------------+
| Stack trace written to /tmp/stack-2023-04-05-19:06:29.dot |
+-----------------------------------------------------------+

+-------------------------------------------------------------------+
| Convert to PDF                                                    |
+-------------------------------------------------------------------+
| dot -Tpdf -o /tmp/stack_25.pdf /tmp/stack-2023-04-05-19:06:29.dot |
+-------------------------------------------------------------------+

+-------------------------------------------------------------------+
| Convert to PNG                                                    |
+-------------------------------------------------------------------+
| dot -Tpng -o /tmp/stack_25.png /tmp/stack-2023-04-05-19:06:29.dot |
+-------------------------------------------------------------------+
```


CC BY-SA / Gnu FDL

