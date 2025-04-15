
# Aria Status Variables


This page documents status variables related to the [Aria storage engine](../s3-storage-engine/aria_s3_copy.md). See [Server Status Variables](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-status-variables.md) for a complete list of status variables that can be viewed with [SHOW STATUS](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-status.md).


See also the [Full list of MariaDB options, system and status variables](../../../server-management/variables-and-modes/full-list-of-mariadb-options-system-and-status-variables.md).


#### `<code>Aria_pagecache_blocks_not_flushed</code>`


* Description: The number of dirty blocks in the Aria page cache. The global value can be flushed by `<code>[FLUSH STATUS](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/flush-commands/flush-tables-for-export.md)</code>`.
* Scope: Global
* Data Type: `<code>numeric</code>`



#### `<code>Aria_pagecache_blocks_unused</code>`


* Description: Free blocks in the Aria page cache. The global value can be flushed by `<code>[FLUSH STATUS](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/flush-commands/flush-tables-for-export.md)</code>`.
* Scope: Global
* Data Type: `<code>numeric</code>`



#### `<code>Aria_pagecache_blocks_used</code>`


* Description: Blocks used in the Aria page cache. The global value can be flushed by `<code>[FLUSH STATUS](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/flush-commands/flush-tables-for-export.md)</code>`.
* Scope: Global
* Data Type: `<code>numeric</code>`



#### `<code>Aria_pagecache_read_requests</code>`


* Description: The number of requests to read something from the Aria page cache.
* Scope: Global
* Data Type: `<code>numeric</code>`



#### `<code>Aria_pagecache_reads</code>`


* Description: The number of Aria page cache read requests that caused a block to be read from the disk.
* Scope: Global
* Data Type: `<code>numeric</code>`



#### `<code>Aria_pagecache_write_requests</code>`


* Description: The number of requests to write a block to the Aria page cache.
* Scope: Global
* Data Type: `<code>numeric</code>`



#### `<code>Aria_pagecache_writes</code>`


* Description: The number of blocks written to disk from the Aria page cache.
* Scope: Global
* Data Type: `<code>numeric</code>`



#### `<code>Aria_transaction_log_syncs</code>`


* Description: The number of Aria log fsyncs.
* Scope: Global
* Data Type: `<code>numeric</code>`


