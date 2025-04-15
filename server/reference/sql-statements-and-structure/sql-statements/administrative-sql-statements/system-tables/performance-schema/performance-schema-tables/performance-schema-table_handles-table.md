# Performance Schema table_handles Table

#

#### MariaDB starting with [10.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/release-notes-mariadb-105-series/mariadb-1052-release-notes)

The `table_handles` table was added in [MariaDB 10.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/release-notes-mariadb-105-series/mariadb-1052-release-notes).

The `table_handles` table contains table lock information. It uses the `wait/lock/table/sql/handler` instrument, which is enabled by default.

Information includes which table handles are open, which sessions are holding the locks, and how they are locked.

The table is read-only, and [TRUNCATE TABLE](../../../../table-statements/truncate-table.md) cannot be performed on the table.

The maximum number of opened table objects is determined by the [performance_schema_max_table_handles](../performance-schema-system-variables.md#performance_schema_max_table_handles) system variable.

The table contains the following columns:

| Column | Description |
| --- | --- |
| Column | Description |
| OBJECT_TYPE | The table opened by a table handle. |
| OBJECT_SCHEMA | The schema that contains the object. |
| OBJECT_NAME | The name of the instrumented object. |
| OBJECT_INSTANCE_BEGIN | The table handle address in memory. |
| OWNER_THREAD_ID | The thread owning the table handle. |
| OWNER_EVENT_ID | The event which caused the table handle to be opened. |
| INTERNAL_LOCK | The table lock used at the SQL level. |
| EXTERNAL_LOCK | The table lock used at the storage engine level. |