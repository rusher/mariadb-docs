
# Information Schema INNODB_BUFFER_POOL_STATS Table

The [Information Schema](../../README.md) `INNODB_BUFFER_POOL_STATS` table contains information about pages in the [buffer pool](../../../../../../../storage-engines/innodb/innodb-buffer-pool.md), similar to what is returned with the `[SHOW ENGINE INNODB STATUS](../../../../show/show-engine-innodb-status.md)` statement.


The `PROCESS` [privilege](../../../../../account-management-sql-commands/grant.md) is required to view the table.


It has the following columns:



| Column | Description |
| --- | --- |
| Column | Description |
| POOL_ID | Buffer Pool identifier. From [MariaDB 10.5.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-5-series/mariadb-1051-release-notes) returns a value of 0, since multiple InnoDB buffer pool instances has been removed. |
| POOL_SIZE | Size in pages of the buffer pool. |
| FREE_BUFFERS | Number of free pages in the buffer pool. |
| DATABASE_PAGES | Total number of pages in the buffer pool. |
| OLD_DATABASE_PAGES | Number of pages in the old sublist. |
| MODIFIED_DATABASE_PAGES | Number of dirty pages. |
| PENDING_DECOMPRESS | Number of pages pending decompression. |
| PENDING_READS | Pending buffer pool level reads. |
| PENDING_FLUSH_LRU | Number of pages in the LRU pending flush. |
| PENDING_FLUSH_LIST | Number of pages in the flush list pending flush. |
| PAGES_MADE_YOUNG | Pages moved from the old sublist to the new sublist. |
| PAGES_NOT_MADE_YOUNG | Pages that have remained in the old sublist without moving to the new sublist. |
| PAGES_MADE_YOUNG_RATE | Hits that cause blocks to move to the top of the new sublist. |
| PAGES_MADE_NOT_YOUNG_RATE | Hits that do not cause blocks to move to the top of the new sublist due to the [innodb_old_blocks](../../../../../../../storage-engines/innodb/innodb-system-variables.md) delay not being met. |
| NUMBER_PAGES_READ | Number of pages read. |
| NUMBER_PAGES_CREATED | Number of pages created. |
| NUMBER_PAGES_WRITTEN | Number of pages written. |
| PAGES_READ_RATE | Number of pages read since the last printout divided by the time elapsed, giving pages read per second. |
| PAGES_CREATE_RATE | Number of pages created since the last printout divided by the time elapsed, giving pages created per second. |
| PAGES_WRITTEN_RATE | Number of pages written since the last printout divided by the time elapsed, giving pages written per second. |
| NUMBER_PAGES_GET | Number of logical read requests. |
| HIT_RATE | Buffer pool hit rate. |
| YOUNG_MAKE_PER_THOUSAND_GETS | For every 1000 gets, the number of pages made young. |
| NOT_YOUNG_MAKE_PER_THOUSAND_GETS | For every 1000 gets, the number of pages not made young. |
| NUMBER_PAGES_READ_AHEAD | Number of pages read ahead. |
| NUMBER_READ_AHEAD_EVICTED | Number of pages read ahead by the read-ahead thread that were later evicted without being accessed by any queries. |
| READ_AHEAD_RATE | Pages read ahead since the last printout divided by the time elapsed, giving read-ahead rate per second. |
| READ_AHEAD_EVICTED_RATE | Read-ahead pages not accessed since the last printout divided by time elapsed, giving the number of read-ahead pages evicted without access per second. |
| LRU_IO_TOTAL | Total least-recently used I/O. |
| LRU_IO_CURRENT | Least-recently used I/O for the current interval. |
| UNCOMPRESS_TOTAL | Total number of pages decompressed. |
| UNCOMPRESS_CURRENT | Number of pages decompressed in the current interval |



## Examples


```
DESC information_schema.innodb_buffer_pool_stats;
+----------------------------------+---------------------+------+-----+---------+-------+
| Field                            | Type                | Null | Key | Default | Extra |
+----------------------------------+---------------------+------+-----+---------+-------+
| POOL_ID                          | bigint(21) unsigned | NO   |     | 0       |       |
| POOL_SIZE                        | bigint(21) unsigned | NO   |     | 0       |       |
| FREE_BUFFERS                     | bigint(21) unsigned | NO   |     | 0       |       |
| DATABASE_PAGES                   | bigint(21) unsigned | NO   |     | 0       |       |
| OLD_DATABASE_PAGES               | bigint(21) unsigned | NO   |     | 0       |       |
| MODIFIED_DATABASE_PAGES          | bigint(21) unsigned | NO   |     | 0       |       |
| PENDING_DECOMPRESS               | bigint(21) unsigned | NO   |     | 0       |       |
| PENDING_READS                    | bigint(21) unsigned | NO   |     | 0       |       |
| PENDING_FLUSH_LRU                | bigint(21) unsigned | NO   |     | 0       |       |
| PENDING_FLUSH_LIST               | bigint(21) unsigned | NO   |     | 0       |       |
| PAGES_MADE_YOUNG                 | bigint(21) unsigned | NO   |     | 0       |       |
| PAGES_NOT_MADE_YOUNG             | bigint(21) unsigned | NO   |     | 0       |       |
| PAGES_MADE_YOUNG_RATE            | double              | NO   |     | 0       |       |
| PAGES_MADE_NOT_YOUNG_RATE        | double              | NO   |     | 0       |       |
| NUMBER_PAGES_READ                | bigint(21) unsigned | NO   |     | 0       |       |
| NUMBER_PAGES_CREATED             | bigint(21) unsigned | NO   |     | 0       |       |
| NUMBER_PAGES_WRITTEN             | bigint(21) unsigned | NO   |     | 0       |       |
| PAGES_READ_RATE                  | double              | NO   |     | 0       |       |
| PAGES_CREATE_RATE                | double              | NO   |     | 0       |       |
| PAGES_WRITTEN_RATE               | double              | NO   |     | 0       |       |
| NUMBER_PAGES_GET                 | bigint(21) unsigned | NO   |     | 0       |       |
| HIT_RATE                         | bigint(21) unsigned | NO   |     | 0       |       |
| YOUNG_MAKE_PER_THOUSAND_GETS     | bigint(21) unsigned | NO   |     | 0       |       |
| NOT_YOUNG_MAKE_PER_THOUSAND_GETS | bigint(21) unsigned | NO   |     | 0       |       |
| NUMBER_PAGES_READ_AHEAD          | bigint(21) unsigned | NO   |     | 0       |       |
| NUMBER_READ_AHEAD_EVICTED        | bigint(21) unsigned | NO   |     | 0       |       |
| READ_AHEAD_RATE                  | double              | NO   |     | 0       |       |
| READ_AHEAD_EVICTED_RATE          | double              | NO   |     | 0       |       |
| LRU_IO_TOTAL                     | bigint(21) unsigned | NO   |     | 0       |       |
| LRU_IO_CURRENT                   | bigint(21) unsigned | NO   |     | 0       |       |
| UNCOMPRESS_TOTAL                 | bigint(21) unsigned | NO   |     | 0       |       |
| UNCOMPRESS_CURRENT               | bigint(21) unsigned | NO   |     | 0       |       |
+----------------------------------+---------------------+------+-----+---------+-------+
```


CC BY-SA / Gnu FDL

