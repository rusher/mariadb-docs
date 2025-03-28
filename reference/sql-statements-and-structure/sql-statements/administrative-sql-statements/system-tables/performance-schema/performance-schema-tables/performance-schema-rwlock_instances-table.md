# Performance Schema rwlock_instances Table

The `rwlock_instances` table lists all read write lock (rwlock) instances that the Performance Schema sees while the server is executing. A read write is a mechanism for ensuring threads can either share access to common resources, or have exclusive access.

The [performance_schema_max_rwlock_instances](../performance-schema-system-variables.md#performance_schema_max_rwlock_instances) system variable specifies the maximum number of instrumented rwlock objects.

The `rwlock_instances` table contains the following columns:

| Column | Description |
| --- | --- |
| Column | Description |
| NAME | Instrument name associated with the read write lock |
| OBJECT_INSTANCE_BEGIN | Address in memory of the instrumented lock |
| WRITE_LOCKED_BY_THREAD_ID | THREAD_ID of the locking thread if locked in write (exclusive) mode, otherwise NULL. |
| READ_LOCKED_BY_COUNT | Count of current read locks held |