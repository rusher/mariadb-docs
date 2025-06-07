# Information Schema THREAD\_POOL\_WAITS Table

**MariaDB starting with** [**10.5**](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/what-is-mariadb-105)

The [Information Schema](../) `THREAD_POOL_WAITS` table was introduced in [MariaDB 10.5.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/mariadb-1050-release-notes).

The table provides wait counters for the [thread pool](../../../../../../ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/thread-pool/thread-pool-in-mariadb.md), and contains the following columns:

| Column | Description                                                     |
| ------ | --------------------------------------------------------------- |
| Column | Description                                                     |
| REASON | name of the reason for waiting, e.g. ROW\_LOCK, DISKIO, NET ... |
| COUNT  | how often a wait for this specific reason has happened so far   |

CC BY-SA / Gnu FDL
