# Performance Schema accounts Table

#

# Description

Each account that connects to the server is stored as a row in the accounts table, along with current and total connections.

The table size is determined at startup by the value of the [performance_schema_accounts_size](../performance-schema-system-variables.md#performance_schema_accounts_size) system variable. If this is set to 0, account statistics will be disabled.

| Column | Description |
| --- | --- |
| Column | Description |
| USER | The connection's client user name for the connection, or NULL if an internal thread. |
| HOST | The connection client's host name, or NULL if an internal thread. |
| CURRENT_CONNECTIONS | Current connections for the account. |
| TOTAL_CONNECTIONS | Total connections for the account. |

The `USER` and `HOST` values shown here are the username and host used for user connections, not the patterns used to check permissions.

#

# Example

```
SELECT * FROM performance_schema.accounts;
+------------------+-----------+---------------------+-------------------+
| USER | HOST | CURRENT_CONNECTIONS | TOTAL_CONNECTIONS |
+------------------+-----------+---------------------+-------------------+
| root | localhost | 1 | 2 |
| NULL | NULL | 20 | 23 |
| debian-sys-maint | localhost | 0 | 35 |
+------------------+-----------+---------------------+-------------------+
```