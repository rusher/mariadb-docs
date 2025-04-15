
# Performance Schema session_account_connect_attrs Table

## Description


The `<code>session_account_connect_attrs</code>` table shows connection attributes for the current session.


Applications can pass key/value connection attributes to the server when a connection is made. The [session_connect_attrs](performance-schema-session_connect_attrs-table.md) and `<code>session_account_connect_attrs</code>` tables provide access to this information, for all sessions and the current session respectively.


The C API functions [mysql_options()](../../../../../../../../connectors/mariadb-connector-c/mariadb-connectorc-api-functions/mysql_options.md) and [mysql_optionsv()](../../../../../../../../connectors/mariadb-connector-c/mariadb-connectorc-api-functions/mysql_optionsv.md) are used for passing connection attributes to the server.


`<code>session_account_connect_attrs</code>` contains the following columns:



| Column | Description |
| --- | --- |
| Column | Description |
| PROCESSLIST_ID | Session connection identifier. |
| ATTR_NAME | Attribute name. |
| ATTR_VALUE | Attribute value. |
| ORDINAL_POSITION | Order in which attribute was added to the connection attributes. |



## Example


```
SELECT * FROM performance_schema.session_account_connect_attrs;
+----------------+-----------------+------------------+------------------+
| PROCESSLIST_ID | ATTR_NAME       | ATTR_VALUE       | ORDINAL_POSITION |
+----------------+-----------------+------------------+------------------+
|             45 | _os             | debian-linux-gnu |                0 |
|             45 | _client_name    | libmysql         |                1 |
|             45 | _pid            | 7711             |                2 |
|             45 | _client_version | 10.0.5           |                3 |
|             45 | _platform       | x86_64           |                4 |
|             45 | program_name    | mysql            |                5 |
+----------------+-----------------+------------------+------------------+
```
