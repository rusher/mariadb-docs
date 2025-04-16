
# Performance Schema setup_objects Table

## Description


The `setup_objects` table determines whether objects are monitored by the performance schema or not. By default limited to 100 rows, this can be changed by setting the [performance_schema_setup_objects_size](../performance-schema-system-variables.md#performance_schema_setup_objects_size) system variable when the server starts.


It contains the following columns:



| Column | Description |
| --- | --- |
| Column | Description |
| OBJECT_TYPE | Type of object to instrument, currently only . Currently, only TABLE', for base table. |
| OBJECT_SCHEMA | Schema containing the object, either the literal or % for any schema. |
| OBJECT_NAME | Name of the instrumented object, either the literal or % for any object. |
| ENABLED | Whether the object's events are instrumented or not. Can be disabled, in which case monitoring is not enabled for those objects. |
| TIMED | Whether the object's events are timed or not. Can be modified. |



When the Performance Schema looks for matches in the `setup_objects`, there may be more than one row matching, with different `ENABLED` and `TIMED` values. It looks for the most specific matches first, that is, it will first look for the specific database and table name combination, then the specific database, only then falling back to a wildcard for both.


Rows can be added or removed from the table, while for existing rows, only the `TIMED` and `ENABLED` columns can be updated. By default, all tables except those in the `performance_schema`, `information_schema` and `mysql` databases are instrumented.

