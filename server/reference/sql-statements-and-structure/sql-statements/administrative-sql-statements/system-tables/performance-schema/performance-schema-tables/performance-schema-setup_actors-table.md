
# Performance Schema setup_actors Table

The `<code>setup_actors</code>` table contains information for determining whether
monitoring should be enabled for new client connection threads.


The default size is 100 rows, which can be changed by modifying the
`<code>[performance_schema_setup_actors_size](../performance-schema-system-variables.md#performance_schema_setup_actors_size)</code>`
system variable at server startup.


If a row in the table matches a new foreground thread's client and host, the
matching `<code>INSTRUMENTED</code>` column in the
[threads](performance-schema-threads-table.md) table is set to either `<code>YES</code>` or
`<code>NO</code>`, which allows selective application of instrumenting by host, by user,
or combination thereof.



| Column | Description |
| --- | --- |
| Column | Description |
| HOST | Host name, either a literal, or the % wildcard representing any host. |
| USER | User name, either a literal or the % wildcard representing any name. |
| ROLE | Unused |



Initially, any user and host is matched:


```
SELECT * FROM performance_schema.setup_actors;
+------+------+------+
| HOST | USER | ROLE |
+------+------+------+
| %    | %    | %    |
+------+------+------+
```
