
# Performance Schema status_by_thread Table


##### MariaDB starting with [10.5.2](../../../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1052-release-notes.md)
The `<code>session_status</code>` table was added in [MariaDB 10.5.2](../../../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1052-release-notes.md).


The `<code>status_by_thread</code>` table contains status variable information about active foreground threads. The table does not collect statistics for `<code>Com_xxx</code>` variables.


The table contains the following columns:



| Column | Description |
| --- | --- |
| Column | Description |
| THREAD_ID | The thread identifier of the session in which the status variable is defined. |
| VARIABLE_NAME | Status variable name. |
| VARIABLE_VALUE | Aggregated status variable value. |



If [TRUNCATE TABLE](../../../../table-statements/truncate-table.md) is run, will aggregate the status for all threads to the global status and account status, then reset the thread status. If account statistics are not collected but host and user status are, the session status is added to host and user status.

