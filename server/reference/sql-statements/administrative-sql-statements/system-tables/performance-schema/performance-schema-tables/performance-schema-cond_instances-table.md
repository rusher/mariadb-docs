
# Performance Schema cond_instances Table

## Description


The `cond_instances` table lists all conditions while the server is executing. A condition, or instrumented condition object, is an internal code mechanism used for signalling that a specific event has occurred so that any threads waiting for this condition can continue.


The maximum number of conditions stored in the performance schema is determined by the [performance_schema_max_cond_instances](../performance-schema-system-variables.md#performance_schema_max_cond_instances) system variable.



| Column | Description |
| --- | --- |
| Column | Description |
| NAME | Client user name for the connection, or NULL if an internal thread. |
| OBJECT_INSTANCE_BEGIN | Address in memory of the instrumented condition. |




<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>


{% @marketo/form formId="4316" %}
