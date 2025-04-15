
# Galera Cluster System Variables

This page documents system variables related to [Galera Cluster](../../../reference/sql-statements-and-structure/sql-statements/built-in-functions/special-functions/galera-functions/README.md). For options that are not system variables, see [Galera Options](../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md).


See [Server System Variables](../optimization-and-tuning/system-variables/server-system-variables.md) for a complete list of system variables and instructions on setting them.


Also see the [Full list of MariaDB options, system and status variables](../../../server-management/variables-and-modes/full-list-of-mariadb-options-system-and-status-variables.md).


#### `<code>wsrep_allowlist</code>`


* Description: Allowed IP addresses, comma delimited.
* Commandline: `<code>--wsrep-allowlist=value1[,value2...]</code>`
* Scope: Global
* Dynamic: No
* Data Type: String
* Default Value: None
* Introduced: [MariaDB 10.10](../../../../release-notes/mariadb-community-server/what-is-mariadb-1010.md)



#### `<code>wsrep_auto_increment_control</code>`


* Description: If set to `<code>1</code>` (the default), will automatically adjust the [auto_increment_increment](../standard-replication/replication-and-binary-log-system-variables.md) and [auto_increment_offset](../standard-replication/replication-and-binary-log-system-variables.md) variables according to the size of the cluster, and when the cluster size changes. This avoids replication conflicts due to [auto_increment](../../../reference/storage-engines/innodb/auto_increment-handling-in-innodb.md). In a primary-replica environment, can be set to `<code>OFF</code>`.
* Commandline: `<code>--wsrep-auto-increment-control[={0|1}]</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: Boolean
* Default Value: `<code>ON</code>`



#### `<code>wsrep_causal_reads</code>`


* Description: If set to `<code>ON</code>` (`<code>OFF</code>` is default), enforces [read-committed](../../../reference/sql-statements-and-structure/sql-statements/transactions/set-transaction.md#read-committed) characteristics across the cluster. In the case that a primary applies an event more quickly than a replica, the two could briefly be out-of-sync. With this variable set to `<code>ON</code>`, the replica will wait for the event to be applied before processing further queries. Setting to `<code>ON</code>` also results in larger read latencies. Deprecated by [wsrep_sync_wait=1](#wsrep_sync_wait).
* Commandline: `<code>--wsrep-causal-reads[={0|1}]</code>`
* Scope: Session
* Dynamic: Yes
* Data Type: Boolean
* Default Value: `<code>OFF</code>`
* Deprecated: [MariaDB 10.1.3](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-3-release-notes.md)
* Removed: [MariaDB 11.3.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-0-release-notes.md)



#### `<code>wsrep_certification_rules</code>`


* Description: Certification rules to use in the cluster. Possible values are: 

  * `<code>strict</code>`: Stricter rules that could result in more certification failures. For example with foreign keys, certification failure could result if different nodes receive non-conflicting insertions at about the same time that point to the same row in a parent table
  * `<code>optimized</code>`: relaxed rules that allow more concurrency and cause less certification failures.
* Commandline: `<code>--wsrep-certifcation-rules</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: Enumeration
* Default Value: `<code>strict</code>`
* Valid Values: `<code>strict</code>`, `<code>optimized</code>`
* Introduced: [MariaDB 10.4.3](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-4-series/mariadb-1043-release-notes.md), MariazDB 10.3.13, [MariaDB 10.2.22](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-10222-release-notes.md), [MariaDB 10.1.38](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10138-release-notes.md)



#### `<code>wsrep_certify_nonPK</code>`


* Description: When set to `<code>ON</code>` (the default), Galera will still certify transactions for tables with no [primary key](../optimization-and-tuning/optimization-and-indexes/getting-started-with-indexes.md#primary-key). However, this can still cause undefined behavior in some circumstances. It is recommended to define primary keys for every InnoDB table when using Galera.
* Commandline: `<code>--wsrep-certify-nonPK[={0|1}]</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: Boolean
* Default Value: `<code>ON</code>`



#### `<code>wsrep_cluster_address</code>`


* Description: The addresses of cluster nodes to connect to when starting up. 

  * Good practice is to specify all possible cluster nodes, in the form `<code>gcomm://<node1 or ip:port>,<node2 or ip2:port>,<node3 or ip3:port></code>`.
  * Specifying an empty ip (`<code>gcomm://</code>`) will cause the node to start a new cluster (which should not be done in the my.cnf file, as after each restart the server will not rejoin the current cluster).
  * The variable can be changed at runtime in some configurations, and will result in the node closing the connection to any current cluster, and connecting to the new address.
  * If specifying a port, note that this is the Galera port, not the MariaDB port.
  * For example:

    * `<code>gcomm://192.168.0.1,192.168.0.2,192.168.0.3</code>`
    * `<code>gcomm://192.168.0.1:1234,192.168.0.2:1234,192.168.0.3:1234?gmcast.listen_addr=tcp://0.0.0.0:1234</code>`
  * See also [gmcast.listen_addr](wsrep_provider_options.md#gmcastlisten_addr)
* Commandline: `<code>--wsrep-cluster-address=value</code>`
* Scope: Global
* Dynamic: No
* Data Type: String



#### `<code>wsrep_cluster_name</code>`


* Description: The name of the cluster. Nodes cannot connect to clusters with a different name, so needs to be identical on all nodes in the same cluster. The variable can be set dynamically, but note that doing so may be unsafe and cause an outage, and that the wsrep provider is unloaded and loaded.
* Commandline: `<code>--wsrep-cluster-name=value</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: String
* Default Value: `<code>my_wsrep_cluster</code>`



#### `<code>wsrep_convert_LOCK_to_trx</code>`


* Description: Converts [LOCK/UNLOCK TABLES](../../../reference/sql-statements-and-structure/sql-statements/transactions/lock-tables.md) statements to [BEGIN](../../../reference/sql-statements-and-structure/sql-statements/transactions/start-transaction.md) and [COMMIT](../../../reference/sql-statements-and-structure/sql-statements/transactions/commit.md). Used mainly for getting older applications to work with a multi-primary setup, use carefully, as can result in extremely large writesets.
* Commandline: `<code>--wsrep-convert-LOCK-to-trx[={0|1}]</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: Boolean
* Default Value: `<code>OFF</code>`



#### `<code>wsrep_data_home_dir</code>`


* Description: Directory where wsrep provider will store its internal files.
* Commandline: `<code>--wsrep-data-home-dir=value</code>`
* Scope: Global
* Dynamic: No
* Data Type: String
* Default Value: The [datadir](../optimization-and-tuning/system-variables/server-system-variables.md#datadir) variable value.



#### `<code>wsrep_dbug_option</code>`


* Description: Unused. The mechanism to pass the DBUG options to the wsrep provider hasn't been implemented.
* Commandline: `<code>--wsrep-dbug-option=value</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: String



#### `<code>wsrep_debug</code>`


* Description: WSREP debug level logging.

  * Before [MariaDB 10.6.1](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-1061-release-notes.md), DDL logging was only logged on the originating node. From [MariaDB 10.6.1](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-1061-release-notes.md), it is logged on other nodes as well.


It is an enum. Valid values are: 
`<code>0: NONE</code>`: Off (default)
`<code>1: SERVER</code>`: MariaDB server code contains WSREP_DEBUG log writes, and these will be added to server error log
`<code>2: TRANSACTION</code>`: Logging from wsrep-lib transaction is added to the error log
`<code>3: STREAMING</code>`: Logging from streaming transactions in wsrep-lib is added to the error log
`<code>4: CLIENT</code>`: Logging from wsrep-lib client state is added to the error log
<</product>>


* Commandline:

  * `<code>--wsrep-debug[={NONE|SERVER|TRANSACTION|STREAMING|CLIENT}]</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: Enumeration
* Default Value: `<code>NONE</code>`
* Valid Values: `<code>NONE</code>`, `<code>SERVER</code>`, `<code>TRANSACTION</code>`, `<code>STREAMING</code>`, `<code>CLIENT</code>`



#### `<code>wsrep_desync</code>`


* Description: When a node receives more write-sets than it can apply, the transactions are placed in a received queue. If the node's received queue has too many write-sets waiting to be applied (as defined by the `<code>[gcs.fc_limit](wsrep_provider_options.md#gcsfc_limit)</code>` WSREP provider option), then the node would usually engage Flow Control. However, when this option is set to `<code>ON</code>`, Flow Control will be disabled for the desynced node. The desynced node works through the received queue until it reaches a more manageable size. The desynced node continues to receive write-sets from the other nodes in the cluster. The other nodes in the cluster do not wait for the desynced node to catch up, so the desynced node can fall even further behind the other nodes in the cluster. You can check if a node is desynced by checking if the `<code>[wsrep_local_state_comment](galera-cluster-status-variables.md#wsrep_local_state_comment)</code>` status variable is equal to `<code>Donor/Desynced</code>`.
* Commandline: `<code>--wsrep-desync[={0|1}]</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: Boolean
* Default Value: `<code>OFF</code>`



#### `<code>wsrep_dirty_reads</code>`


* Description: By default, when not synchronized with the group ([wsrep_ready](galera-cluster-status-variables.md#wsrep_ready)=OFF) a node will reject all queries other than SET and SHOW. If `<code>wsrep_dirty_reads</code>` is set to `<code>1</code>`, queries which do not change data, like SELECT queries (dirty reads), creating of prepare statement, etc. will be accepted by the node.
* Commandline: `<code>--wsrep-dirty-reads[={0|1}]</code>`
* Scope: Global,Session
* Dynamic: Yes
* Data Type: Boolean
* Default Value: `<code>OFF</code>`
* Valid Values: `<code>ON</code>`, `<code>OFF</code>`



#### `<code>wsrep_drupal_282555_workaround</code>`


* Description: If set to `<code>ON</code>`, a workaround for [Drupal/MySQL/InnoDB bug #282555](https://www.drupal.org/node/282555) is enabled. This is a bug where, in some cases, when inserting a `<code>DEFAULT</code>` value into an [AUTO_INCREMENT](../../../reference/storage-engines/innodb/auto_increment-handling-in-innodb.md) column, a duplicate key error may be returned.
* Commandline: `<code>--wsrep-drupal-282555-workaround[={0|1}]</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: Boolean
* Default Value: `<code>OFF</code>`



#### `<code>wsrep_forced_binlog_format</code>`


* Description: A [binary log format](../../../server-management/server-monitoring-logs/binary-log/binary-log-formats.md) that will override any session binlog format settings.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--wsrep-forced-binlog-format=value</code>`
* Scope: Global
* Dynamic: Yes
* Default Value: `<code>NONE</code>`
* Data Type: Enum
* Valid Values: `<code>STATEMENT</code>`, `<code>ROW</code>`, `<code>MIXED</code>` or `<code>NONE</code>` (which resets the forced binlog format state).



#### `<code>wsrep_gtid_domain_id</code>`


* Description: This system variable defines the [GTID](../standard-replication/gtid.md) domain ID that is used for [wsrep GTID mode](using-mariadb-replication-with-mariadb-galera-cluster/using-mariadb-gtids-with-mariadb-galera-cluster.md#wsrep-gtid-mode).

  * When `<code>[wsrep_gtid_mode](#wsrep_gtid_mode)</code>` is set to `<code>ON</code>`, `<code>wsrep_gtid_domain_id</code>` is used in place of `<code>[gtid_domain_id](../standard-replication/gtid.md#gtid_domain_id)</code>` for all Galera Cluster write sets.
  * When `<code>[wsrep_gtid_mode](#wsrep_gtid_mode)</code>` is set to `<code>OFF</code>`, `<code>wsrep_gtid_domain_id</code>` is simply ignored to allow for backward compatibility.
  * There are some additional requirements that need to be met in order for this mode to generate consistent [GTIDs](../standard-replication/gtid.md). For more information, see [Using MariaDB GTIDs with MariaDB Galera Cluster](using-mariadb-replication-with-mariadb-galera-cluster/using-mariadb-gtids-with-mariadb-galera-cluster.md).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--wsrep-gtid-domain-id=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>0</code>`
* Range: `<code>0</code>` to `<code>4294967295</code>`



#### `<code>wsrep_gtid_mode</code>`


* Description: [Wsrep GTID mode](using-mariadb-replication-with-mariadb-galera-cluster/using-mariadb-gtids-with-mariadb-galera-cluster.md#wsrep-gtid-mode) attempts to keep [GTIDs](../standard-replication/gtid.md) consistent for Galera Cluster write sets on all cluster nodes. [GTID](../standard-replication/gtid.md) state is initially copied to a joiner node during an [SST](state-snapshot-transfers-ssts-in-galera-cluster/introduction-to-state-snapshot-transfers-ssts.md). If you are planning to use Galera Cluster with [MariaDB replication](../standard-replication/README.md), then wsrep GTID mode can be helpful.

  * When `<code>wsrep_gtid_mode</code>` is set to `<code>ON</code>`, `<code>[wsrep_gtid_domain_id](#wsrep_gtid_domain_id)</code>` is used in place of `<code>[gtid_domain_id](../standard-replication/gtid.md#gtid_domain_id)</code>` for all Galera Cluster write sets.
  * When `<code>wsrep_gtid_mode</code>` is set to `<code>OFF</code>`, `<code>[wsrep_gtid_domain_id](#wsrep_gtid_domain_id)</code>` is simply ignored to allow for backward compatibility.
  * There are some additional requirements that need to be met in order for this mode to generate consistent [GTIDs](../standard-replication/gtid.md). For more information, see [Using MariaDB GTIDs with MariaDB Galera Cluster](using-mariadb-replication-with-mariadb-galera-cluster/using-mariadb-gtids-with-mariadb-galera-cluster.md).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--wsrep-gtid-mode[={0|1}]</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`



#### `<code>wsrep_gtid_seq_no</code>`


* Description: Internal server usage, manually set WSREP GTID seqno.
* Commandline: None
* Scope: Session only
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Range: `<code>0</code>` to `<code>18446744073709551615</code>`
* Introduced: [MariaDB 10.5.1](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1051-release-notes.md)



#### `<code>wsrep_ignore_apply_errors</code>`


* Description: Bitmask determining whether errors are ignored, or reported back to the provider.

  * 0: No errors are skipped.
  * 1: Ignore some DDL errors (DROP DATABASE, DROP TABLE, DROP INDEX, ALTER TABLE).
  * 2: Skip DML errors (Only ignores DELETE errors).
  * 4: Ignore all DDL errors.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--wsrep-ignore-apply-errors</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: Numeric
* Default Value: `<code>7</code>`
* Range: `<code>0</code>` to `<code>7</code>`
* Introduced: [MariaDB 10.4.2](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-4-series/mariadb-1042-release-notes.md)



#### `<code>wsrep_load_data_splitting</code>`


* Description: If set to `<code>ON</code>`, [LOAD DATA INFILE](../../../reference/sql-statements-and-structure/sql-statements/data-manipulation/inserting-loading-data/load-data-into-tables-or-index/load-data-infile.md) supports big data files by introducing transaction splitting. The setting has been deprecated in Galera 4, and defaults to `<code>OFF</code>`
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--wsrep-load-data-splitting[={0|1}]</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: Boolean
* Default Value: `<code>OFF</code>`
* Deprecated: [MariaDB 10.4.2](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-4-series/mariadb-1042-release-notes.md)
* Removed: [MariaDB 11.5](../../../../release-notes/mariadb-community-server/what-is-mariadb-115.md)



#### `<code>wsrep_log_conflicts</code>`


* Description: If set to `<code>ON</code>` (`<code>OFF</code>` is default), details of conflicting MDL as well as InnoDB locks in the cluster will be logged.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--wsrep-log-conflicts[={0|1}]</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: Boolean
* Default Value: `<code>OFF</code>`



#### `<code>wsrep_max_ws_rows</code>`


* Description: Maximum permitted number of rows per writeset. The support for this variable has been added and in order to be backward compatible the default value has been changed to `<code>0</code>`, which essentially allows writesets to be any size.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--wsrep-max-ws-rows=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: Numeric
* Default Value:

  * `<code>0</code>`
* Range: `<code>0</code>` to `<code>1048576</code>`



#### `<code>wsrep_max_ws_size</code>`


* Description: Maximum permitted size in bytes per writeset. Writesets exceeding 2GB will be rejected.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--wsrep-max-ws-size=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: Numeric
* Default Value:

  * `<code>2147483647</code>` (2GB)
* Range: `<code>1024</code>` to `<code>2147483647</code>`



#### `<code>wsrep_mode</code>`


* Description: Turns on WSREP features which are not part of default behavior.

  * BINLOG_ROW_FORMAT_ONLY: Only ROW [binlog format](../../../server-management/server-monitoring-logs/binary-log/binary-log-formats.md) is supported.
  * DISALLOW_LOCAL_GTID: Nodes can have GTIDs for local transactions in a number of scenarios. If DISALLOW_LOCAL_GTID is set, these operations produce an error ERROR HY000: Galera replication not supported. Scenarios include:

    * A DDL statement is executed with wsrep_OSU_method=RSU set.
    * A DML statement writes to a non-InnoDB table.
    * A DML statement writes to an InnoDB table with wsrep_on=OFF set.
  * REPLICATE_ARIA: Whether or not DML updates for [Aria](../../../reference/storage-engines/s3-storage-engine/aria_s3_copy.md) tables will be replicated. This functionality is experimental and should not be relied upon in production systems.
  * REPLICATE_MYISAM: Whether or not DML updates for [MyISAM](../../../reference/storage-engines/myisam-storage-engine/myisam-system-variables.md) tables will be replicated. This functionality is experimental and should not be relied upon in production systems.
  * REQUIRED_PRIMARY_KEY: Table should have PRIMARY KEY defined.
  * STRICT_REPLICATION: Same as the old [wsrep_strict_ddl](#wsrep_strict_ddl) setting.
* Commandline: `<code>--wsrep-mode=value</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: Enumeration
* Default Value: (Empty)
* Valid Values: `<code>BINLOG_ROW_FORMAT_ONLY</code>`, `<code>DISALLOW_LOCAL_GTID</code>`, `<code>REQUIRED_PRIMARY_KEY</code>`, `<code>REPLICATE_ARIA</code>`, `<code>REPLICATE_MYISAM</code>` and `<code>STRICT_REPLICATION</code>`
* Introduced: [MariaDB 10.6.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-1060-release-notes.md)



#### `<code>wsrep_mysql_replication_bundle</code>`


* Description: Determines the number of replication events that are grouped together. Experimental implementation aimed to assist with bottlenecks when a single replica faces a large commit time delay. If set to `<code>0</code>` (the default), there is no grouping.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--wsrep-mysql-replication-bundle=#</code>`
* Scope: Global
* Dynamic: No
* Data Type: Numeric
* Default Value: `<code>0</code>`
* Range: `<code>0</code>` to `<code>1000</code>`



#### `<code>wsrep_node_address</code>`


* Description: Specifies the node's network address, in the format `<code>ip address[:port]</code>`. It supports IPv6. The default behavior is for the node to pull the address of the first network interface on the system and the default Galera port. This autoguessing can be unreliable, particularly in the following cases:

  * cloud deployments
  * container deployments
  * servers with multiple network interfaces.
  * servers running multiple nodes.
  * network address translation (NAT).
  * clusters with nodes in more than one region.
* See also [wsrep_provider_options -> gmcast.listen_addr](wsrep_provider_options.md#gmcastlisten_addr)
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--wsrep-node-address=value</code>`
* Scope: Global
* Dynamic: No
* Data Type: String
* Default Value: Primary network address, usually `<code>eth0</code>` with a default port of 4567, or `<code>0.0.0.0</code>` if no IP address.



#### `<code>wsrep_node_incoming_address</code>`


* Description: This is the address from which the node listens for client connections. If an address is not specified or it's set to `<code>AUTO</code>` (default), mysqld uses either [--bind-address](../optimization-and-tuning/system-variables/server-system-variables.md#bind_address) or [--wsrep-node-address](#wsrep_node_address), or tries to get one from the list of available network interfaces, in the same order. See also [wsrep_provider_options -> gmcast.listen_addr](wsrep_provider_options.md#gmcastlisten_addr).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--wsrep-node-incoming-address=value</code>`
* Scope: Global
* Dynamic: No
* Data Type: String
* Default Value: `<code>AUTO</code>`



#### `<code>wsrep_node_name</code>`


* Description: Name of this node. This name can be used in [wsrep_sst_donor](#wsrep_sst_donor) as a preferred donor. Note that multiple nodes in a cluster can have the same name.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--wsrep-node-name=value</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: String
* Default Value: The server's hostname.



#### `<code>wsrep_notify_cmd</code>`


* Description: Command to be executed each time the node state or the cluster membership changes. Can be used for raising an alarm, configuring load balancers and so on. See the [Codership Notification Script page](https://galeracluster.com/library/documentation/notification-cmd.html) for more details.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--wsrep-notify-command=value</code>`
* Scope: Global
* Dynamic:

  * No (>= [MariaDB 10.5.9](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1059-release-notes.md))
  * Yes (<= [MariaDB 10.5.8](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1058-release-notes.md))
* Data Type: String
* Default Value: Empty



#### `<code>wsrep_on</code>`


* Description: Whether or not wsrep replication is enabled. If the global value is set to `<code>OFF</code>` , it is not possible to load the provider and join the node in the cluster. If only the session value is set to `<code>OFF</code>`, the operations from that particular session are not replicated in the cluster, but other sessions and applier threads will continue as normal. The session value of the variable does not affect the node's membership and thus, regardless of its value, the node keeps receiving updates from other nodes in the cluster. It is set to `<code>OFF</code>` by default and must be turned on to enable Galera replication.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--wsrep-on[={0|1}]</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: Boolean
* Default Value: `<code>OFF</code>`
* Valid Values: `<code>ON</code>`, `<code>OFF</code>`



#### `<code>wsrep_OSU_method</code>`


* Description: Online schema upgrade method. The default is `<code>TOI</code>`, specifying the setting without the optional parameter will set to `<code>RSU</code>`.

  * `<code>TOI</code>`: Total Order Isolation. In each cluster node, DDL is processed in the same order regarding other transactions, guaranteeing data consistency. However, affected parts of the database will be locked for the whole cluster.
  * `<code>RSU</code>`: Rolling Schema Upgrade. DDL processing is only done locally on the node, and the user needs perform the changes manually on each node. The node is desynced from the rest of the cluster while the processing takes place to avoid the blocking other nodes. Schema changes [must be backwards compatible in the same way as for ROW based replication](../standard-replication/replication-when-the-primary-and-replica-have-different-table-definitions.md) to avoid breaking replication when the DDL processing is complete on the single node, and replication recommences.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--wsrep-OSU-method[=value]</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: Enum
* Default Value: `<code>TOI</code>`
* Valid Values: `<code>TOI</code>`, `<code>RSU</code>`



#### `<code>wsrep_patch_version</code>`


* Description: Wsrep patch version, for example `<code>wsrep_25.10</code>`.
* Commandline: None
* Scope: Global
* Dynamic: No
* Data Type: String
* Default Value: None



#### `<code>wsrep_provider</code>`


* Description: Location of the wsrep library, usually `<code>/usr/lib/libgalera_smm.so</code>` on Debian and Ubuntu, and `<code>/usr/lib64/libgalera_smm.so</code>` on Red Hat/CentOS.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--wsrep-provider=value</code>`
* Scope: Global

  * No (>= [MariaDB 10.5.9](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1059-release-notes.md))
  * Yes (<= [MariaDB 10.5.8](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1058-release-notes.md))
* Data Type: String
* Default Value: None



#### `<code>wsrep_provider_options</code>`


* Description: Semicolon (;) separated list of wsrep options (see [wsrep_provider_options](wsrep_provider_options.md)).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--wsrep-provider-options=value</code>`
* Scope: Global
* Dynamic: No
* Data Type: String
* Default Value: Empty



#### `<code>wsrep_recover</code>`


* Description: If set to `<code>ON</code>` when the server starts, the server will recover the sequence number of the most recent write set applied by Galera, and it will be output to `<code>stderr</code>`, which is usually redirected to the [error log](../../../server-management/server-monitoring-logs/error-log.md). At that point, the server will exit. This sequence number can be provided to the `<code>[wsrep_start_position](#wsrep_start_position)</code>` system variable.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--wsrep-recover[={0|1}]</code>`
* Scope: Global
* Dynamic: No
* Data Type: Boolean
* Default Value: `<code>OFF</code>`



#### `<code>wsrep_reject_queries</code>`


* Description: Variable to set to reject queries from client connections, useful for maintenance. The node continues to apply write-sets, but an `<code>Error 1047: Unknown command</code>` error is generated by a client query.

  * `<code>NONE</code>` - Not set. Queries will be processed as normal.
  * `<code>ALL</code>` - All queries from client connections will be rejected, but existing client connections will be maintained.
  * `<code>ALL_KILL</code>` All queries from client connections will be rejected, and existing client connections, including the current one, will be immediately killed.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--wsrep-reject-queries[=value]</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: Enum
* Default Value: `<code>NONE</code>`
* Valid Values: `<code>NONE</code>`, `<code>ALL</code>`, `<code>ALL_KILL</code>`
* Introduced: [MariaDB 10.3.6](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1036-release-notes.md), [MariaDB 10.2.14](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-10214-release-notes.md), [MariaDB 10.1.32](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10132-release-notes.md)



#### `<code>wsrep_replicate_myisam</code>`


* Description: Whether or not DML updates for [MyISAM](../../../reference/storage-engines/myisam-storage-engine/myisam-system-variables.md) tables will be replicated. This functionality is still experimental and should not be relied upon in production systems. Deprecated in [MariaDB 10.6](../../../../release-notes/mariadb-community-server/what-is-mariadb-106.md), and removed in [MariaDB 10.7](../../../../release-notes/mariadb-community-server/what-is-mariadb-107.md), use [wsrep_mode](#wsrep_mode) instead.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--wsrep-replicate-myisam[={0|1}]</code>`
* Scope: Global
* Dynamic: Yes
* Default Value: `<code>OFF</code>`
* Data Type: Boolean
* Valid Values: `<code>ON</code>`, `<code>OFF</code>`
* Deprecated: [MariaDB 10.6.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-1060-release-notes.md)
* Removed: [MariaDB 10.7.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-7-series/mariadb-1070-release-notes.md)



#### `<code>wsrep_restart_slave</code>`


* Description: If set to ON, the replica is restarted automatically, when node joins back to cluster.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--wsrep-restart-slave[={0|1}]</code>`
* Scope: Global
* Dynamic: Yes
* Default Value: `<code>OFF</code>`
* Data Type: Boolean



#### `<code>wsrep_retry_autocommit</code>`


* Description: Number of times autocommited queries will be retried due to cluster-wide conflicts before returning an error to the client. If set to `<code>0</code>`, no retries will be attempted, while a value of `<code>1</code>` (the default) or more specifies the number of retries attempted. Can be useful to assist applications using autocommit to avoid deadlocks.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--wsrep-retry-autocommit=value</code>`
* Scope: Global
* Dynamic: No
* Data Type: Numeric
* Default Value: `<code>1</code>`
* Range: `<code>0</code>` to `<code>10000</code>`



#### `<code>wsrep_slave_FK_checks</code>`


* Description: If set to ON (the default), the applier replica thread performs foreign key constraint checks.
* Commandline: `<code>--wsrep-slave-FK-checks[={0|1}]</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: Boolean
* Default Value: ON



#### `<code>wsrep_slave_threads</code>`


* Description: Number of replica threads used to apply Galera write sets in parallel. The Galera replica threads are able to determine which write sets are safe to apply in parallel. However, if your cluster nodes seem to have frequent consistency problems, then setting the value to `<code>1</code>` will probably fix the problem. See [About Galera Replication: Galera Replica Threads](about-galera-replication.md#galera-slave-threads) for more information.
* Commandline: `<code>--wsrep-slave-threads=</code>`#
* Scope: Global
* Dynamic: Yes
* Data Type: Numeric
* Default Value: `<code>1</code>`
* Range: `<code>1</code>` to `<code>512</code>`



#### `<code>wsrep_slave_UK_checks</code>`


* Description: If set to ON, the applier replica thread performs secondary index uniqueness checks.
* Commandline: `<code>--wsrep-slave-UK-checks[={0|1}]</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: Boolean
* Default Value: OFF



#### `<code>wsrep_sr_store</code>`


* Description: Storage for streaming replication fragments.
* Commandline: `<code>--wsrep-sr-store=val</code>`
* Scope: Global
* Dynamic: No
* Data Type: Enum
* Default Value: `<code>table</code>`
* Valid Values: `<code>table</code>`, `<code>none</code>`
* Introduced: [MariaDB 10.4.2](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-4-series/mariadb-1042-release-notes.md)



#### `<code>wsrep_sst_auth</code>`


* Description: Username and password of the user to use for replication. Unused if [wsrep_sst_method](#wsrep_sst_method) is set to `<code>rsync</code>`, while for other methods it should be in the format `<code><user>:<password></code>`. The contents are masked in logs and when querying the value with [SHOW VARIABLES](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-variables.md). See [Introduction to State Snapshot Transfers (SSTs)](state-snapshot-transfers-ssts-in-galera-cluster/introduction-to-state-snapshot-transfers-ssts.md) for more information.
* Commandline: `<code>--wsrep-sst-auth=value</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: String
* Default Value: (Empty)



#### `<code>wsrep_sst_donor</code>`


* Description: Comma-separated list (from 5.5.33) or name (as per [wsrep_node_name](galera-cluster-system-variables.md#wsrep_node_name)) of the servers as donors, or the source of the state transfer, in order of preference. The donor-selection algorithm, in general, prefers a donor capable of transferring only the missing transactions (IST) to the joiner node, instead of the complete state (SST). Thus, it starts by looking for an IST-capable node in the given donor list followed by rest of the nodes in the cluster. In case multiple candidate nodes are found outside the specified donor list, the node in the same segment ([gmcast.segment](wsrep_provider_options.md#gmcastsegment)) as the joiner is preferred. If none of the existing nodes in the cluster can serve the missing transactions through IST, the algorithm moves on to look for a suitable node to transfer the entire state (SST). It first looks at the nodes specified in the donor list (irrespective of their segment). If no suitable donor is still found, the rest of the donor nodes are checked for suitability only if the donor list has a "terminating-comma". Note that a stateless node (the Galera arbitrator) can never be a donor. See [Introduction to State Snapshot Transfers (SSTs)](state-snapshot-transfers-ssts-in-galera-cluster/introduction-to-state-snapshot-transfers-ssts.md) for more information.
[NOTE] Although the variable is dynamic, the node will not use the new value unless the node requiring SST or IST disconnects from the cluster. To force this, set [wsrep_cluster_address](galera-cluster-system-variables.md#wsrep_cluster_address) to an empty string and back to the nodes list. After setting this variable dynamically, on startup the value from the configuration file will be used again.
* Commandline: `<code>--wsrep-sst-donor=value</code>`
* Scope: Global
* Dynamic: Yes (read note above)
* Data Type: String
* Default Value:



#### `<code>wsrep_sst_donor_rejects_queries</code>`


* Description: If set to `<code>ON</code>` (`<code>OFF</code>` is default), the donor node will reject incoming queries, returning an `<code>UNKNOWN COMMAND</code>` error code. Can be used for informing load balancers that a node is unavailable.
* Commandline: `<code>--wsrep-sst-donor-rejects-queries[={0|1}]</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: Boolean
* Default Value: `<code>OFF</code>`



#### `<code>wsrep_sst_method</code>`


* Description: Method used for taking the [state snapshot transfer (SST)](state-snapshot-transfers-ssts-in-galera-cluster/introduction-to-state-snapshot-transfers-ssts.md). See [Introduction to State Snapshot Transfers (SSTs): SST Methods](state-snapshot-transfers-ssts-in-galera-cluster/introduction-to-state-snapshot-transfers-ssts.md#sst-methods) for more information.
* Commandline: `<code>--wsrep-sst-method=value</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: String
* Default Value: `<code>rsync</code>`
* Valid Values: `<code>rsync</code>`, `<code>mysqldump</code>`, `<code>xtrabackup</code>`, `<code>xtrabackup-v2</code>`, `<code>mariabackup</code>`



#### `<code>wsrep_sst_receive_address</code>`


* Description: This is the address where other nodes (donor) in the cluster connect to in order to send the state-transfer updates. If an address is not specified or its set to `<code>AUTO</code>` (default), mysqld uses [--wsrep_node_address](galera-cluster-system-variables.md#wsrep_node_address)'s value as the receiving address. However, if [--wsrep_node_address](galera-cluster-system-variables.md#wsrep_node_address) is not set, it uses address from either [--bind-address](../optimization-and-tuning/system-variables/server-system-variables.md#bind_address) or tries to get one from the list of available network interfaces, in the same order. Note: setting it to `<code>localhost</code>` will make it impossible for nodes running on other hosts to reach this node. See [Introduction to State Snapshot Transfers (SSTs)](state-snapshot-transfers-ssts-in-galera-cluster/introduction-to-state-snapshot-transfers-ssts.md) for more information.
* Commandline: `<code>--wsrep-sst-receive-address=value</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: String
* Default Value: `<code>AUTO</code>`



#### `<code>wsrep_start_position</code>`


* Description: The start position that the node should use in the format: `<code>UUID:seq_no</code>`. The proper value to use for this position can be recovered with `<code>[wsrep_recover](#wsrep_recover)</code>`.
* Commandline: `<code>--wsrep-start-position=value</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: String
* Default Value: `<code> 00000000-0000-0000-0000-000000000000:-1</code>`



#### `<code>wsrep_status_file</code>`


* Description: wsrep status output filename.
* Commandline: `<code>--wsrep-status-file=value</code>`
* Scope: Global
* Dynamic: No
* Data Type: String
* Default Value: None
* Introduced: [MariaDB 10.9](../../../../release-notes/mariadb-community-server/what-is-mariadb-109.md)



#### `<code>wsrep_strict_ddl</code>`


* Description: If set, reject DDL statements on affected tables not supporting Galera replication. This is done by checking if the table is InnoDB, which is the only table currently fully supporting Galera replication. MyISAM tables will not trigger the error if the experimental [wsrep_replicate_myisam](#wsrep_replicate_myisam) setting is `<code>ON</code>`. If set, should be set on all tables in the cluster. Affected DDL statements include:
[CREATE TABLE](../../../reference/sql-statements-and-structure/vectors/create-table-with-vectors.md) (e.g. CREATE TABLE t1(a int) engine=Aria)
[ALTER TABLE](../../../reference/sql-statements-and-structure/sql-statements/data-definition/alter/alter-tablespace.md)
[TRUNCATE TABLE](../../../reference/sql-statements-and-structure/sql-statements/table-statements/truncate-table.md)
[CREATE VIEW](../../programming-customizing-mariadb/views/create-view.md)
[CREATE TRIGGER](../../programming-customizing-mariadb/triggers-events/triggers/create-trigger.md)
[CREATE INDEX](../../../reference/sql-statements-and-structure/sql-statements/data-definition/create/create-index.md)
[DROP INDEX](../../../reference/sql-statements-and-structure/sql-statements/data-definition/drop/drop-index.md)
[RENAME TABLE](../../../reference/sql-statements-and-structure/sql-statements/data-definition/rename-table.md)
[DROP TABLE](../../../reference/sql-statements-and-structure/sql-statements/data-definition/drop/drop-tablespace.md)
Statements in [procedures](../../programming-customizing-mariadb/stored-routines/stored-procedures/README.md), [events](../../programming-customizing-mariadb/triggers-events/event-scheduler/README.md), and [functions](../../programming-customizing-mariadb/stored-routines/stored-functions/README.md) are permitted as the affected
tables are only known at execution. Furthermore, the various USER, ROLE, SERVER and 
DATABASE statements are also allowed as they do not have an affected table. Deprecated in [MariaDB 10.6.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-1060-release-notes.md) and removed in [MariaDB 10.7](../../../../release-notes/mariadb-community-server/what-is-mariadb-107.md). Use [wsrep_mode=STRICT_REPLICATION](#wsrep_mode) instead.
* Commandline: `<code>--wsrep-strict-ddl[={0|1}</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`
* Introduced: [MariaDB 10.5.1](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1051-release-notes.md)
* Deprecated: [MariaDB 10.6.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-1060-release-notes.md)
* Removed: [MariaDB 10.7.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-7-series/mariadb-1070-release-notes.md)



#### `<code>wsrep_sync_wait</code>`


* Description: Setting this variable ensures causality checks will take place before executing an operation of the type specified by the value, ensuring that the statement is executed on a fully synced node. While the check is taking place, new queries are blocked on the node to allow the server to catch up with all updates made in the cluster up to the point where the check was begun. Once reached, the original query is executed on the node. This can result in higher latency. Note that when [wsrep_dirty_reads](#wsrep_dirty_reads) is ON, values of wsrep_sync_wait become irrelevant. Sample usage (for a critical read that must have the most up-to-date data) `<code>SET SESSION wsrep_sync_wait=1; SELECT ...; SET SESSION wsrep_sync_wait=0;</code>`

  * `<code>0</code>` - Disabled (default)
  * `<code>1</code>` - READ (SELECT and BEGIN/START TRANSACTION). This is the same as [wsrep_causal_reads=1](#wsrep_causal_reads).
  * `<code>2</code>` - UPDATE and DELETE;
  * `<code>3</code>` - READ, UPDATE and DELETE;
  * `<code>4</code>` - INSERT and REPLACE;
  * `<code>5</code>` - READ, INSERT and REPLACE;
  * `<code>6</code>` - UPDATE, DELETE, INSERT and REPLACE;
  * `<code>7</code>` - READ, UPDATE, DELETE, INSERT and REPLACE;
  * `<code>8</code>` - SHOW
  * `<code>9</code>` - READ and SHOW
  * `<code>10</code>` - UPDATE, DELETE and SHOW
  * `<code>11</code>` - READ, UPDATE, DELETE and SHOW
  * `<code>12</code>` - INSERT, REPLACE and SHOW
  * `<code>13</code>` - READ, INSERT, REPLACE and SHOW
  * `<code>14</code>` - UPDATE, DELETE, INSERT, REPLACE and SHOW
  * `<code>15</code>` - READ, UPDATE, DELETE, INSERT, REPLACE and SHOW
* Commandline: `<code>--wsrep-sync-wait=</code>`#
* Scope: Session
* Dynamic: Yes
* Data Type: Numeric
* Default Value: `<code>0</code>`
* Range:

  * `<code>0</code>` to `<code>15</code>`



#### `<code>wsrep_trx_fragment_size</code>`


* Description: Size of transaction fragments for streaming replication (measured in units as specified by [wsrep_trx_fragment_unit](#wsrep_trx_fragment_unit))
* Commandline: `<code>--wsrep-trx-fragment-size=</code>`#
* Scope: Session
* Dynamic: Yes
* Data Type: numeric
* Default Value: `<code>0</code>`
* Range: `<code>0</code>` to `<code>2147483647</code>`
* Introduced: [MariaDB 10.4.2](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-4-series/mariadb-1042-release-notes.md)



#### `<code>wsrep_trx_fragment_unit</code>`


* Description: Unit for streaming replication transaction fragments' size:

  * `<code>bytes</code>`: transaction’s binlog events buffer size in bytes
  * `<code>rows</code>`: number of rows affected by the transaction
  * `<code>statements</code>`: number of SQL statements executed in the multi-statement transaction
* Commandline: `<code>--wsrep-trx-fragment-unit=value</code>`
* Scope: Session
* Dynamic: Yes
* Data Type: enum
* Default Value: `<code>bytes</code>`
* Valid Values: `<code>bytes</code>`, `<code>rows</code>` or `<code>statements</code>`
* Introduced: [MariaDB 10.4.2](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-4-series/mariadb-1042-release-notes.md)


