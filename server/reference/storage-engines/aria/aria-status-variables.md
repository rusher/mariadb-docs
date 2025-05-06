
# Aria Status Variables


This page documents status variables related to the [Aria storage engine](README.md). See [Server Status Variables](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-status-variables.md) for a complete list of status variables that can be viewed with [SHOW STATUS](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-status.md).


See also the [Full list of MariaDB options, system and status variables](../../../server-management/variables-and-modes/full-list-of-mariadb-options-system-and-status-variables.md).


#### `Aria_pagecache_blocks_not_flushed`


* Description: The number of dirty blocks in the Aria page cache. The global value can be flushed by `[FLUSH STATUS](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/flush-commands/flush.md)`.
* Scope: Global
* Data Type: `numeric`



#### `Aria_pagecache_blocks_unused`


* Description: Free blocks in the Aria page cache. The global value can be flushed by `[FLUSH STATUS](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/flush-commands/flush.md)`.
* Scope: Global
* Data Type: `numeric`



#### `Aria_pagecache_blocks_used`


* Description: Blocks used in the Aria page cache. The global value can be flushed by `[FLUSH STATUS](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/flush-commands/flush.md)`.
* Scope: Global
* Data Type: `numeric`



#### `Aria_pagecache_read_requests`


* Description: The number of requests to read something from the Aria page cache.
* Scope: Global
* Data Type: `numeric`



#### `Aria_pagecache_reads`


* Description: The number of Aria page cache read requests that caused a block to be read from the disk.
* Scope: Global
* Data Type: `numeric`



#### `Aria_pagecache_write_requests`


* Description: The number of requests to write a block to the Aria page cache.
* Scope: Global
* Data Type: `numeric`



#### `Aria_pagecache_writes`


* Description: The number of blocks written to disk from the Aria page cache.
* Scope: Global
* Data Type: `numeric`



#### `Aria_transaction_log_syncs`


* Description: The number of Aria log fsyncs.
* Scope: Global
* Data Type: `numeric`



CC BY-SA / Gnu FDL

