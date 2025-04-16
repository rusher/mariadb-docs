
# Performance Schema session_status Table


##### MariaDB starting with [10.5.2](../../../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1052-release-notes.md)
The `session_status` table was added in [MariaDB 10.5.2](../../../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1052-release-notes.md).


The `session_status` table contains a list of status variables for the current session. The table only stores status variable statistics for threads which are instrumented, and does not collect statistics for `Com_xxx` variables.


The table contains the following columns:



| Column | Description |
| --- | --- |
| Column | Description |
| VARIABLE_NAME | The session status variable name. |
| VARIABLE_VALUE | The session status variable value. |



It is not possible to empty this table with a `TRUNCATE TABLE` statement.

