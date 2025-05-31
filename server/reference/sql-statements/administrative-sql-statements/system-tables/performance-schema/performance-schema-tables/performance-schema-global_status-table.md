# Performance Schema global\_status Table

**MariaDB starting with** [**10.5.2**](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-5-series/mariadb-1052-release-notes)

The `global_status` table was added in [MariaDB 10.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-5-series/mariadb-1052-release-notes).

The `global_status` table contains a list of status variables and their global values. The table only stores status variable statistics for threads which are instrumented, and does not collect statistics for `Com_xxx` variables.

The table contains the following columns:

| Column          | Description                       |
| --------------- | --------------------------------- |
| Column          | Description                       |
| VARIABLE\_NAME  | The global status variable name.  |
| VARIABLE\_VALUE | The global status variable value. |

[TRUNCATE TABLE](../../../../table-statements/truncate-table.md) resets global status variables, including thread, account, host, and user status, but not those that are never reset by the server.

CC BY-SA / Gnu FDL
