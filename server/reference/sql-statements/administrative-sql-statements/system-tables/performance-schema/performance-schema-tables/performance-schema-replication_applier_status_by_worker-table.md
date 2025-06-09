# Performance Schema replication\_applier\_status\_by\_worker Table

**MariaDB starting with** [**10.6.0**](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-6-series/mariadb-1060-release-notes)

The `replication_applier_status_by_worker` table was added in [MariaDB 10.6.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-6-series/mariadb-1060-release-notes).

The [Performance Schema](../) replication\_applier\_status\_by\_worker table displays replica worker thread specific information.

It contains the following fields.

| Column                    | Description                                                                                                                                                                                                                                       |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Column                    | Description                                                                                                                                                                                                                                       |
| CHANNEL\_NAME             | Name of replication channel through which the transaction is received.                                                                                                                                                                            |
| THREAD\_ID                | Thread\_Id as displayed in the [performance\_schema.threads](performance-schema-threads-table.md) table for thread with name 'thread/sql/rpl\_parallel\_thread'. THREAD\_ID will be NULL when worker threads are stopped due to error/force stop. |
| SERVICE\_STATE            | Whether or not the thread is running.                                                                                                                                                                                                             |
| LAST\_SEEN\_TRANSACTION   | Last GTID executed by worker                                                                                                                                                                                                                      |
| LAST\_ERROR\_NUMBER       | Last Error that occurred on a particular worker.                                                                                                                                                                                                  |
| LAST\_ERROR\_MESSAGE      | Last error specific message.                                                                                                                                                                                                                      |
| LAST\_ERROR\_TIMESTAMP    | Time stamp of last error.                                                                                                                                                                                                                         |
| WORKER\_IDLE\_TIME        | Total idle time in seconds that the worker thread has spent waiting for work from SQL thread.                                                                                                                                                     |
| LAST\_TRANS\_RETRY\_COUNT | Total number of retries attempted by last transaction.                                                                                                                                                                                            |

CC BY-SA / Gnu FDL

{% @marketo/form formId="4316" %}
