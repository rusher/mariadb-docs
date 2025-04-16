
# Performance Schema status_by_user Table


##### MariaDB starting with [10.5.2](../../../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1052-release-notes.md)
The `status_by_account` table was added in [MariaDB 10.5.2](../../../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1052-release-notes.md).


The `status_by_account` table contains status variable information by user. The table does not collect statistics for `Com_xxx` variables.


The table contains the following columns:



| Column | Description |
| --- | --- |
| Column | Description |
| USER | User for which the status variable is reported. |
| VARIABLE_NAME | Status variable name. |
| VARIABLE_VALUE | Aggregated status variable value |



If [TRUNCATE TABLE](../../../../table-statements/truncate-table.md) is run, will reset the aggregated user status from terminated sessions.


If [FLUSH STATUS](https://mariadb.com/kb/en/flush-status) is run, session status from all active sessions are added to the global status variables, the status of all active sessions are reset, and values aggregated from disconnected sessions are reset.

