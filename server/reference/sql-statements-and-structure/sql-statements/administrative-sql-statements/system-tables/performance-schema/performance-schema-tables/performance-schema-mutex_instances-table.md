
# Performance Schema mutex_instances Table

## Description


The `mutex_instances` table lists all mutexes that the Performance Schema seeing while the server is executing.


A mutex is a code mechanism for ensuring that threads can only access resources one at a time. A second thread attempting to access a resource will find it protected by a mutex, and will wait for it to be unlocked.


The [performance_schema_max_mutex_instances](../performance-schema-system-variables.md#performance_schema_max_mutex_instances) system variable specifies the maximum number of instrumented mutex instances.



| Column | Description |
| --- | --- |
| Column | Description |
| NAME | Instrument name associated with the mutex. |
| OBJECT_INSTANCE_BEGIN | Memory address of the instrumented mutex. |
| LOCKED_BY_THREAD_ID | The THREAD_ID of the locking thread if a thread has a mutex locked, otherwise NULL. |


