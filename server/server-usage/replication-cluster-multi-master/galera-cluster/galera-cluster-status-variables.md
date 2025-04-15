
# Galera Cluster Status Variables


## Viewing Galera Cluster Status Variables


Galera status variables can be viewed with the [SHOW STATUS](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-status.md) statement.


```
SHOW STATUS LIKE 'wsrep%';
```

See also the [Full list of MariaDB options, system and status variables](../../../server-management/variables-and-modes/full-list-of-mariadb-options-system-and-status-variables.md).


## List of Galera Cluster status variables


MariaDB Galera Cluster has the following status variables:


#### `<code>wsrep_applier_thread_count</code>`


* Description: Stores current number of applier threads to make clear how many slave threads of this type there are.
* Introduced: [MariaDB 10.2.26](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-10226-release-notes.md), [MariaDB 10.3.17](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-10317-release-notes.md), [MariaDB 10.4.7](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-4-series/mariadb-1047-release-notes.md)



#### `<code>wsrep_apply_oooe</code>`


* Description: How often writesets have been applied out of order, an indicators of parallelization efficiency.



#### `<code>wsrep_apply_oool</code>`


* Description: How often writesets with a higher sequence number were applied before ones with a lower sequence number, implying slow writesets.



#### `<code>wsrep_apply_window</code>`


* Description: Average distance between highest and lowest concurrently applied seqno.



#### `<code>wsrep_cert_deps_distance</code>`


* Description: Average distance between the highest and the lowest sequence numbers that can possibly be applied in parallel, or the potential degree of parallelization.



#### `<code>wsrep_cert_index_size</code>`


* Description: The number of entries in the certification index.



#### `<code>wsrep_cert_interval</code>`


* Description: Average number of transactions received while a transaction replicates.



#### `<code>wsrep_cluster_capabilities</code>`


* Description:



#### `<code>wsrep_cluster_conf_id</code>`


* Description: Total number of cluster membership changes that have taken place.



#### `<code>wsrep_cluster_size</code>`


* Description: Number of nodes currently in the cluster.



#### `<code>wsrep_cluster_state_uuid</code>`


* Description: UUID state of the cluster. If it matches the value in [wsrep_local_state_uuid](#wsrep_local_state_uuid), the local and cluster nodes are in sync.



#### `<code>wsrep_cluster_status</code>`


* Description: Cluster component status. Possible values are `<code>PRIMARY</code>` (primary group configuration, quorum present), `<code>NON_PRIMARY</code>` (non-primary group configuration, quorum lost) or `<code>DISCONNECTED</code>` (not connected to group, retrying).



#### `<code>wsrep_cluster_weight</code>`


* Description: The total weight of the current members in the cluster. The value is counted as a sum of of pc.weight of the nodes in the current Primary Component.



#### `<code>wsrep_commit_oooe</code>`


* Description: How often a transaction was committed out of order.



#### `<code>wsrep_commit_oool</code>`


* Description: No meaning.



#### `<code>wsrep_commit_window</code>`


* Description: Average distance between highest and lowest concurrently committed seqno.



#### `<code>wsrep_connected</code>`


* Description: Whether or not MariaDB is connected to the wsrep provider. Possible values are `<code>ON</code>` or `<code>OFF</code>`.



#### `<code>wsrep_desync_count</code>`


* Description: Returns the number of operations in progress that require the node to temporarily desync from the cluster.



#### `<code>wsrep_evs_delayed</code>`


* Description: Provides a comma separated list of all the nodes this node has registered on its delayed list.



#### `<code>wsrep_evs_evict_list</code>`


* Description: Lists the UUID’s of all nodes evicted from the cluster. Evicted nodes cannot rejoin the cluster until you restart their mysqld processes.



#### `<code>wsrep_evs_repl_latency</code>`


* Description: This status variable provides figures for the replication latency on group communication. It measures latency (in seconds) from the time point when a message is sent out to the time point when a message is received. As replication is a group operation, this essentially gives you the slowest ACK and longest RTT in the cluster. Format is min/avg/​max/stddev



#### `<code>wsrep_evs_state</code>`


* Description: Shows the internal state of the EVS Protocol.



#### `<code>wsrep_flow_control_paused</code>`


* Description: The fraction of time since the last FLUSH STATUS command that replication was paused due to flow control.



#### `<code>wsrep_flow_control_paused_ns</code>`


* Description: The total time spent in a paused state measured in nanoseconds.



#### `<code>wsrep_flow_control_recv</code>`


* Description: Number of FC_PAUSE events received as well as sent since the most recent status query.



#### `<code>wsrep_flow_control_sent</code>`


* Description: Number of FC_PAUSE events sent since the most recent status query



#### `<code>wsrep_gcomm_uuid</code>`


* Description: The UUID assigned to the node.



#### `<code>wsrep_incoming_addresses</code>`


* Description: Comma-separated list of incoming server addresses in the cluster component.



#### `<code>wsrep_last_committed</code>`


* Description: Sequence number of the most recently committed transaction.



#### `<code>wsrep_local_bf_aborts</code>`


* Description: Total number of local transactions aborted by slave transactions while being executed



#### `<code>wsrep_local_cached_downto</code>`


* Description: The lowest sequence number, or seqno, in the write-set cache (GCache).



#### `<code>wsrep_local_cert_failures</code>`


* Description: Total number of local transactions that failed the certification test.



#### `<code>wsrep_local_commits</code>`


* Description: Total number of local transactions committed on the node.



#### `<code>wsrep_local_index</code>`


* Description: The node's index in the cluster. The index is zero-based.



#### `<code>wsrep_local_recv_queue</code>`


* Description: Current length of the receive queue, which is the number of writesets waiting to be applied.



#### `<code>wsrep_local_recv_queue_avg</code>`


* Description: Average length of the receive queue since the most recent status query. If this value is noticeably larger than zero, the node is likely to be overloaded, and cannot apply the writesets as quickly as they arrive, resulting in replication throttling.



#### `<code>wsrep_local_recv_queue_max</code>`


* Description: The maximum length of the recv queue since the last FLUSH STATUS command.



#### `<code>wsrep_local_recv_queue_min</code>`


* Description: The minimum length of the recv queue since the last FLUSH STATUS command.



#### `<code>wsrep_local_replays</code>`


* Description: Total number of transaction replays due to asymmetric lock granularity.



#### `<code>wsrep_local_send_queue</code>`


* Description: Current length of the send queue, which is the number of writesets waiting to be sent.



#### `<code>wsrep_local_send_queue_avg</code>`


* Description: Average length of the send queue since the most recent status query. If this value is noticeably larger than zero, there is most likely network throughput or replication throttling issues.



#### `<code>wsrep_local_send_queue_max</code>`


* Description: The maximum length of the send queue since the last FLUSH STATUS command.



#### `<code>wsrep_local_send_queue_min</code>`


* Description: The minimum length of the send queue since the last FLUSH STATUS command.



#### `<code>wsrep_local_state</code>`


* Description: Internal Galera Cluster FSM state number.



#### `<code>wsrep_local_state_comment</code>`


* Description: Human-readable explanation of the state.



#### `<code>wsrep_local_state_uuid</code>`


* Description: The node's UUID state. If it matches the value in [wsrep_cluster_state_uuid](#wsrep_cluster_state_uuid), the local and cluster nodes are in sync.



#### `<code>wsrep_open_connections</code>`


* Description: The number of open connection objects inside the wsrep provider.



#### `<code>wsrep_open_transactions</code>`


* Description: The number of locally running transactions which have been registered inside the wsrep provider. This means transactions which have made operations which have caused write set population to happen. Transactions which are read only are not counted.



#### `<code>wsrep_protocol_version</code>`


* Description: The wsrep protocol version being used.



#### `<code>wsrep_provider_name</code>`


* Description: The name of the provider. The default is "Galera".



#### `<code>wsrep_provider_vendor</code>`


* Description: The vendor string.



#### `<code>wsrep_provider_version</code>`


* Description: The version number of the Galera wsrep provider



#### `<code>wsrep_ready</code>`


* Description: Whether or not the Galera wsrep provider is ready. Possible values are `<code>ON</code>` or `<code>OFF</code>`



#### `<code>wsrep_received</code>`


* Description: Total number of writesets received from other nodes.



#### `<code>wsrep_received_bytes</code>`


* Description: Total size in bytes of all writesets received from other nodes.



#### `<code>wsrep_repl_data_bytes</code>`


* Description: Total size of data replicated.



#### `<code>wsrep_repl_keys</code>`


* Description: Total number of keys replicated.



#### `<code>wsrep_repl_keys_bytes</code>`


* Description: Total size of keys replicated.



#### `<code>wsrep_repl_other_bytes</code>`


* Description: Total size of other bits replicated.



#### `<code>wsrep_replicated</code>`


* Description: Total number of writesets replicated to other nodes.



#### `<code>wsrep_replicated_bytes</code>`


* Description: Total size in bytes of all writesets replicated to other nodes.



#### `<code>wsrep_rollbacker_thread_count</code>`


* Description: Stores current number of rollbacker threads to make clear how many slave threads of this type there are.
* Introduced: [MariaDB 10.2.26](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-10226-release-notes.md), [MariaDB 10.3.17](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-10317-release-notes.md), [MariaDB 10.4.7](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-4-series/mariadb-1047-release-notes.md)



#### `<code>wsrep_thread_count</code>`


* Description: Total number of wsrep (applier/rollbacker) threads.


