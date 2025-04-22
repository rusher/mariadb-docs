
# Performance Schema status_by_host Table


##### MariaDB starting with [10.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-5-series/mariadb-1052-release-notes)
The `status_by_host` table was added in [MariaDB 10.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-5-series/mariadb-1052-release-notes).


The `status_by_host` table contains status variable information by host. The table does not collect statistics for `Com_xxx` variables.


The table contains the following columns:



| Column | Description |
| --- | --- |
| Column | Description |
| HOST | Host for which the status variable is reported. |
| VARIABLE_NAME | Status variable name. |
| VARIABLE_VALUE | Aggregated status variable value |



If [TRUNCATE TABLE](../../../../table-statements/truncate-table.md) is run, will reset the aggregated host status from terminated sessions.


If [FLUSH STATUS](flush-status) is run, session status from all active sessions are added to the global status variables, the status of all active sessions are reset, and values aggregated from disconnected sessions are reset.

