
# Performance Schema users Table

## Description


Each user that connects to the server is stored as a row in the `users` table, along with current and total connections.


The table size is determined at startup by the value of the [performance_schema_users_size](../performance-schema-system-variables.md#performance_schema_users_size) system variable. If this is set to `0`, user statistics will be disabled.



| Column | Description |
| --- | --- |
| Column | Description |
| USER | The connection's client user name for the connection, or NULL if an internal thread. |
| CURRENT_CONNECTIONS | Current connections for the user. |
| TOTAL_CONNECTIONS | Total connections for the user. |



## Example


```
SELECT * FROM performance_schema.users;
+------------------+---------------------+-------------------+
| USER             | CURRENT_CONNECTIONS | TOTAL_CONNECTIONS |
+------------------+---------------------+-------------------+
| debian-sys-maint |                   0 |                35 |
| NULL             |                  20 |                23 |
| root             |                   1 |                 2 |
+------------------+---------------------+-------------------+
```
