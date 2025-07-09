# Performance Schema status\_by\_thread Table

**MariaDB starting with** [**10.5.2**](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/mariadb-1052-release-notes)

The `session_status` table was added in [MariaDB 10.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/mariadb-1052-release-notes).

The `status_by_thread` table contains status variable information about active foreground threads. The table does not collect statistics for `Com_xxx` variables.

The table contains the following columns:

| Column          | Description                                                                   |
| --------------- | ----------------------------------------------------------------------------- |
| THREAD\_ID      | The thread identifier of the session in which the status variable is defined. |
| VARIABLE\_NAME  | Status variable name.                                                         |
| VARIABLE\_VALUE | Aggregated status variable value.                                             |

If [TRUNCATE TABLE](../../../../table-statements/truncate-table.md) is run, will aggregate the status for all threads to the global status and account status, then reset the thread status. If account statistics are not collected but host and user status are, the session status is added to host and user status.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
