# Configuring MariaDB for Optimal Performance

This article is to help you configure MariaDB for optimal performance.

Note that by default MariaDB is configured to work on a desktop system and should because of this not take a lot of resources. To get things to work for a dedicated server, you have to do a few minutes of work.

For this article we assume that you are going to run MariaDB on a dedicated server.

Feel free to update this article if you have more ideas.

#

# [my.cnf](/kb/en/configuring-mariadb-with-mycnf/) Files

MariaDB is normally configured by editing the [my.cnf](/kb/en/mysqld-configuration-files-and-groups/) file. In the next section you have a list of variables that you may want to configure for dedicated MariaDB servers.

#

# [InnoDB](../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/innodb-encryption/innodb-encryption-troubleshooting.md) Storage Engine

InnoDB is normally the default storage engine with MariaDB.

* You should set [innodb_buffer_pool_size](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_buffer_pool_size) to about 80% of your memory. The goal is to ensure that 80 % of your working set is in memory.

The other most important InnoDB variables are:

* [innodb_log_file_size](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_log_file_size)
* [innodb_flush_method](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_flush_method)
* [innodb_thread_sleep_delay](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_thread_sleep_delay)

Some other important InnoDB variables:

* [innodb_max_dirty_pages_pct_lwm](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_max_dirty_pages_pct_lwm)
* [innodb_read_ahead_threshold](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_read_ahead_threshold)
* [innodb_buffer_pool_instances](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_buffer_pool_instances). Deprecated and ignored from [MariaDB 10.5.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/release-notes-mariadb-105-series/mariadb-1051-release-notes).
* [innodb_adaptive_max_sleep_delay](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_adaptive_max_sleep_delay). Deprecated and ignored from [MariaDB 10.5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/release-notes-mariadb-105-series/mariadb-1055-release-notes).
* [innodb_thread_concurrency](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_thread_concurrency). Deprecated and ignored from [MariaDB 10.5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/release-notes-mariadb-105-series/mariadb-1055-release-notes).

#

# [Aria](../../../reference/storage-engines/aria/aria-storage-engine.md) Storage Engine

* MariaDB uses by default the Aria storage engine for internal temporary files. If you have many temporary files, you should set [aria_pagecache_buffer_size](/kb/en/aria-server-system-variables/#aria_pagecache_buffer_size) to a reasonably large value so that temporary overflow data is not flushed to disk. The default is 128M.

You can check if Aria is configured properly by executing:

```
MariaDB [test]> show global status like "Aria%";
+-----------------------------------+-------+
| Variable_name | Value |
+-----------------------------------+-------+
| Aria_pagecache_blocks_not_flushed | 0 |
| Aria_pagecache_blocks_unused | 964 |
| Aria_pagecache_blocks_used | 232 |
| Aria_pagecache_read_requests | 9598 |
| Aria_pagecache_reads | 0 |
| Aria_pagecache_write_requests | 222 |
| Aria_pagecache_writes | 0 |
| Aria_transaction_log_syncs | 0 |
+-----------------------------------+-------+
```

If `Aria_pagecache_reads` is much smaller than `Aria_pagecache_read_request` and
 `Aria_pagecache_writes` is much smaller than Aria_pagecache_write_request#, then your setup is good. If the [aria_pagecache_buffer_size](/kb/en/aria-server-system-variables/#aria_pagecache_buffer_size) is big enough, the two variables should be 0, like above.

#

# [MyISAM](../../../clients-and-utilities/myisam-clients-and-utilities/myisamchk-table-information.md)

* If you don't use MyISAM tables explicitly (true for most [MariaDB 10.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/what-is-mariadb-104)+ users), you can set [key_buffer_size](../../../reference/storage-engines/myisam-storage-engine/myisam-system-variables.md#key_buffer_size) to a very low value, like 64K.

#

# Using in memory temporary tables

Using memory tables for internal temporary results can speed up execution.
However, if the memory table gets full, then the memory table will be moved to
disk, which can hurt performance.

You can check how the internal memory tables are performing by executing:

```
MariaDB [test]> show global status like "Created%tables%";
+-------------------------+-------+
| Variable_name | Value |
+-------------------------+-------+
| Created_tmp_disk_tables | 1 |
| Created_tmp_tables | 2 |
+-------------------------+-------+
```

`Created_tmp_tables` is the total number of internal temporary tables created as part of executing queries like SELECT.
`Created_tmp_disk_tables` shows how many of these did hit the storage.

You can increase the storage for internal temporary tables by setting [max_heap_table_size](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#max_heap_table_size) and [tmp_memory_table_size](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#tmp_memory_table_size) high enough. These values are per connection.

#

# Lots of Connections

#

## A Lot of Fast Connections + Small Set of Queries + Disconnects

* If you are doing a lot of fast connections / disconnects, you should increase [back_log](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#back_log) and if you are running [MariaDB 10.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/what-is-mariadb-1011) or below [thread_cache_size](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#thread_cache_size).
* If you have a lot (> 128) of simultaneous running fast queries, you should consider setting [thread_handling](/kb/en/thread-pool-system-and-status-variables/#thread_handling) to `pool_of_threads`.

#

## Connecting From a Lot of Different Machines

* If you are connecting from a lot of different machines you should increase [host_cache_size](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#host_cache_size) to the max number of machines (default 128) to cache the resolving of hostnames. If you don't connect from a lot of machines, you can set this to a very low value!

#

# See Also

* [MariaDB Memory Allocation](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/mariadb-memory-allocation.md)
* [Full List of MariaDB Options, System and Status Variables](../../variables-and-modes/full-list-of-mariadb-options-system-and-status-variables.md)
* [Server system variables](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md)
* [mysqld options](/kb/en/mysqld-options-full-list/)
* [Performance schema](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/performance-schema/performance-schema-status-variables.md) helps you understand what is taking time and resources.
* [Slow query log](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/query-optimizations/statistics-for-optimizing-queries/slow-query-log-extended-statistics.md) is used to find queries that are running slow.
* [OPTIMIZE TABLE](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/optimizing-tables/optimize-table.md) helps you defragment tables.

#

# External Links

* [http://www.tocker.ca/2013/09/17/what-to-tune-in-mysql-56-after-installation.html](http://www.tocker.ca/2013/09/17/what-to-tune-in-mysql-56-after-installation.html)
* [http://www.percona.com/resources/technical-presentations/optimizing-mysql-configuration-percona-mysql-university-montevideo](http://www.percona.com/resources/technical-presentations/optimizing-mysql-configuration-percona-mysql-university-montevideo)