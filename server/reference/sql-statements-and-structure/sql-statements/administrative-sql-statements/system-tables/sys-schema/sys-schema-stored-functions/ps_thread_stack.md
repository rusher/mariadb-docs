
# ps_thread_stack

## Syntax


```
sys.ps_thread_stack(thread_id, verbose)
```

## Description


`ps_thread_stack` is a [stored function](../../../../../../../server-usage/programming-customizing-mariadb/stored-routines/stored-functions/README.md) available with the [Sys Schema](../README.md) that, for a given *thread_id*, returns all statements, stages, and events within the Performance Schema, as a JSON formatted stack.


The boolean *verbose* argument specifies whether or not to include `file:lineno` information in the events.


## Examples


```
SELECT sys.ps_thread_stack(13, FALSE) AS thread_stack\G
*************************** 1. row ***************************
thread_stack: {"rankdir": "LR","nodesep": "0.10",
  "stack_created": "2022-03-28 16:01:06",
  "mysql_version": "10.8.2-MariaDB",
  "mysql_user": "msandbox@localhost",
  "events": []}
```


CC BY-SA / Gnu FDL

