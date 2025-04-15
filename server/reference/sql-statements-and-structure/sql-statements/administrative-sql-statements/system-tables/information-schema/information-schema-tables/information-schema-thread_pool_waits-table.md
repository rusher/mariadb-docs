
# Information Schema THREAD_POOL_WAITS Table


##### MariaDB starting with [10.5](../../../../../../../../release-notes/mariadb-community-server/what-is-mariadb-105.md)
The [Information Schema](../../../../../../mariadb-internals/information-schema-plugins-show-and-flush-statements.md) `<code>THREAD_POOL_WAITS</code>` table was introduced in [MariaDB 10.5.0](../../../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1050-release-notes.md).


The table provides wait counters for the [thread pool](../../../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/buffers-caches-and-threads/thread-pool/thread-pool-in-mariadb-51-53.md), and contains the following columns:



| Column | Description |
| --- | --- |
| Column | Description |
| REASON | name of the reason for waiting, e.g. ROW_LOCK, DISKIO, NET ... |
| COUNT | how often a wait for this specific reason has happened so far |


