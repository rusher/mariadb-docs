
# Semisynchronous Replication Plugin Status Variables


This page documents status variables related to the [Semisynchronous Replication Plugin](semisynchronous-replication-plugin-status-variables.md) (which has been merged into the main server from [MariaDB 10.3.3](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1033-release-notes.md)). See [Server Status Variables](server-status-variables.md) for a complete list of status variables that can be viewed with [SHOW STATUS](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-status.md).


See also the [Full list of MariaDB options, system and status variables](../../../../server-management/variables-and-modes/full-list-of-mariadb-options-system-and-status-variables.md).


#### `<code>Rpl_semi_sync_master_clients</code>`


* Description: Number of semisynchronous slaves.
* Data Type: `<code>numeric</code>`



#### `<code>Rpl_semi_sync_master_get_ack</code>`


* Description: Number of acknowledgements received by the master from slaves.
* Data Type: `<code>numeric</code>`



#### `<code>Rpl_semi_sync_master_net_avg_wait_time</code>`


* Description: Average time the master waited for a slave to reply, in microseconds.
* Data Type: `<code>numeric</code>`



#### `<code>Rpl_semi_sync_master_net_wait_time</code>`


* Description: Total time the master waited for slave replies, in microseconds.
* Data Type: `<code>numeric</code>`



#### `<code>Rpl_semi_sync_master_net_waits</code>`


* Description: Total number of times the master waited for slave replies.
* Data Type: `<code>numeric</code>`



#### `<code>Rpl_semi_sync_master_no_times</code>`


* Description: Number of times the master turned off semisynchronous replication. The global value can be flushed by `<code>[FLUSH STATUS](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/flush-commands/flush-tables-for-export.md)</code>`.
* Data Type: `<code>numeric</code>`



#### `<code>Rpl_semi_sync_master_no_tx</code>`


* Description: Number of commits that have not been successfully acknowledged by a slave. The global value can be flushed by `<code>[FLUSH STATUS](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/flush-commands/flush-tables-for-export.md)</code>`.
* Data Type: `<code>numeric</code>`



#### `<code>Rpl_semi_sync_master_request_ack</code>`


* Description: Number of acknowledgement requests sent to slaves.
* Data Type: `<code>numeric</code>`



#### `<code>Rpl_semi_sync_master_status</code>`


* Description: Whether or not semisynchronous replication is currently operating on the master. The value will be `<code>ON</code>` if both the plugin has been enabled and a commit acknowledgment has occurred. It will be `<code>OFF</code>` if either the plugin has not been enabled, or the master is replicating asynchronously due to a commit acknowledgment timeout.
* Data Type: `<code>boolean</code>`



#### `<code>Rpl_semi_sync_master_timefunc_failures</code>`


* Description: Number of times the master failed when calling a time function, such as gettimeofday(). The global value can be flushed by `<code>[FLUSH STATUS](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/flush-commands/flush-tables-for-export.md)</code>`.
* Data Type: `<code>numeric</code>`



#### `<code>Rpl_semi_sync_master_tx_avg_wait_time</code>`


* Description: Average time the master waited for each transaction, in microseconds.
* Data Type: `<code>numeric</code>`



#### `<code>Rpl_semi_sync_master_tx_wait_time</code>`


* Description: Total time the master waited for transactions, in microseconds.
* Data Type: `<code>numeric</code>`



#### `<code>Rpl_semi_sync_master_tx_waits</code>`


* Description: Total number of times the master waited for transactions.
* Data Type: `<code>numeric</code>`



#### `<code>Rpl_semi_sync_master_wait_pos_backtraverse</code>`


* Description: Total number of times the master waited for an event that had binary coordinates lower than previous events waited for. Occurs if the order in which transactions start waiting for a reply is different from the order in which their binary log events were written. The global value can be flushed by `<code>[FLUSH STATUS](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/flush-commands/flush-tables-for-export.md)</code>`.
* Data Type: `<code>numeric</code>`



#### `<code>Rpl_semi_sync_master_wait_sessions</code>`


* Description: Number of sessions that are currently waiting for slave replies.
* Data Type: `<code>numeric</code>`



#### `<code>Rpl_semi_sync_master_yes_tx</code>`


* Description: Number of commits that have been successfully acknowledged by a slave. The global value can be flushed by `<code>[FLUSH STATUS](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/flush-commands/flush-tables-for-export.md)</code>`.
* Data Type: `<code>numeric</code>`



#### `<code>Rpl_semi_sync_slave_status</code>`


* Description: Whether or not semisynchronous replication is currently operating on the slave. `<code>ON</code>` if both semi-sync has been enabled for the replica (i.e. by setting the variable [rpl_semi_sync_slave_enabled](semisynchronous-replication-plugin-status-variables.md#rpl_semi_sync_slave_enabled) to `<code>TRUE</code>`) and the slave I/O thread is running.
* Data Type: `<code>boolean</code>`



#### `<code>Rpl_semi_sync_slave_send_ack</code>`


* Description: Number of acknowledgements the slave sent to the master.
* Data Type: `<code>numeric</code>`


