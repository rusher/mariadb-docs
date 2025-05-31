# Performance Schema replication\_applier\_status\_by\_coordinator Table

**MariaDB starting with** [**10.5.2**](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-5-series/mariadb-1052-release-notes)

The `replication_applier_status_by_coordinator` table was added in [MariaDB 10.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-5-series/mariadb-1052-release-notes).

The [Performance Schema](../) replication\_applier\_status\_by\_coordinator table displays the status of the coordinator thread used in multi-threaded replicas to manage multiple worker threads.

It contains the following fields.

| Column                    | Type                | Null | Description                                                                |
| ------------------------- | ------------------- | ---- | -------------------------------------------------------------------------- |
| Column                    | Type                | Null | Description                                                                |
| CHANNEL\_NAME             | varchar(256)        | NO   | Replication channel name.                                                  |
| THREAD\_ID                | bigint(20) unsigned | YES  | The SQL/coordinator thread ID.                                             |
| SERVICE\_STATE            | enum('ON','OFF')    | NO   | ON (thread exists and is active or idle) or OFF (thread no longer exists). |
| LAST\_ERROR\_NUMBER       | int(11)             | NO   | Last error number that caused the SQL/coordinator thread to stop.          |
| LAST\_ERROR\_MESSAGE      | varchar(1024)       | NO   | Last error message that caused the SQL/coordinator thread to stop.         |
| LAST\_ERROR\_TIMESTAMP    | timestamp           | NO   | Timestamp that shows when the most recent SQL/coordinator error occured.   |
| LAST\_SEEN\_TRANSACTION   | char(57)            | NO   | The transaction the worker has last seen.                                  |
| LAST\_TRANS\_RETRY\_COUNT | int(11)             | NO   | Total number of retries attempted by last transaction.                     |

CC BY-SA / Gnu FDL
