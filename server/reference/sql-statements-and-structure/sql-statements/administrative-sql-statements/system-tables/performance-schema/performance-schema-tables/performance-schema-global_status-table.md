
# Performance Schema global_status Table


##### MariaDB starting with [10.5.2](../../../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1052-release-notes.md)
The `<code>global_status</code>` table was added in [MariaDB 10.5.2](../../../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1052-release-notes.md).


The `<code>global_status</code>` table contains a list of status variables and their global values. The table only stores status variable statistics for threads which are instrumented, and does not collect statistics for `<code>Com_xxx</code>` variables.


The table contains the following columns:



| Column | Description |
| --- | --- |
| Column | Description |
| VARIABLE_NAME | The global status variable name. |
| VARIABLE_VALUE | The global status variable value. |



[TRUNCATE TABLE](../../../../table-statements/truncate-table.md) resets global status variables, including thread, account, host, and user status, but not those that are never reset by the server.

