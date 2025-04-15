
# wsrep_provider_options


## wsrep_provider_options


The following options can be set as part of the Galera [wsrep_provider_options](galera-cluster-system-variables.md#wsrep_provider_options) variable. Dynamic options can be changed while the server is running.


Options need to be provided as a semicolon (;) separated list on a single line. Options that are not explicitly set are set to their default value.


Note that before Galera 3, the `<code>repl</code>` tag was named `<code>replicator</code>`.


#### `<code>base_dir</code>`


* Description: Specifies the data directory



#### `<code>base_host</code>`


* Description: For internal use. Should not be manually set.
* Default: `<code>127.0.0.1</code>` (detected network address)



#### `<code>base_port</code>`


* Description: For internal use. Should not be manually set.
* Default: `<code>4567</code>`



#### `<code>cert.log_conflicts</code>`


* Description: Certification failure log details.
* Dynamic: Yes
* Default: `<code>no</code>`



#### `<code>cert.optimistic_pa</code>`


* Description: Controls parallel application of actions on the replica. If set, the full range of parallelization as determined by the certification algorithm is permitted. If not set, the parallel applying window will not exceed that seen on the primary, and applying will start no sooner than after all actions it has seen on the master are committed.
* Dynamic: Yes
* Default: `<code>yes</code>`



#### `<code>debug</code>`


* Description: Enable debugging.
* Dynamic: Yes
* Default: `<code>no</code>`



#### `<code>evs.auto_evict</code>`


* Description: Number of entries the node permits for a given delayed node before triggering the Auto Eviction protocol. An entry is added to a delayed list for each delayed response from a node. If set to `<code>0</code>`, the default, the Auto Eviction protocol is disabled for this node. See [Auto Eviction](https://galeracluster.com/library/documentation/auto-eviction.html) for more.
* Dynamic: No
* Default: `<code>0</code>`



#### `<code>evs.causal_keepalive_period</code>`


* Description: Used by the developers only, and not manually serviceable.
* Dynamic: No
* Default: The [evs.keepalive_period](#evskeepalive_period).



#### `<code>evs.debug_log_mask</code>`


* Description: Controls EVS debug logging. Only effective when [wsrep_debug](galera-cluster-system-variables.md#wsrep_debug) is on.
* Dynamic: Yes
* Default: `<code>0x1</code>`



#### `<code>evs.delay_margin</code>`


* Description: Time that response times can be delayed before this node adds an entry to the delayed list. See [evs.auto_evict](#evsauto_evict). Must be set to a higher value than the round-trip delay time between nodes.
* Dynamic: No
* Default: `<code>PT1S</code>`



#### `<code>evs.delayed_keep_period</code>`


* Description: Time that this node requires a previously delayed node to remain responsive before being removed from the delayed list. See [evs.auto_evict](#evsauto_evict).
* Dynamic: No
* Default: `<code>PT30S</code>`



#### `<code>evs.evict</code>`


* Description: When set to the gcomm UUID of a node, that node is evicted from the cluster. When set to an empty string, the eviction list is cleared on the node where it is set. See [evs.auto_evict](#evsauto_evict).
* Dynamic: No
* Default: Empty string



#### `<code>evs.inactive_check_period</code>`


* Description: Frequency of checks for peer inactivity (looking for nodes with delayed responses), after which nodes may be added to the delayed list, and later evicted.
* Dynamic: No
* Default: `<code> PT0.5S </code>`



#### `<code>evs.inactive_timeout</code>`


* Description: Time limit that a node can be inactive before being pronounced as dead.
* Dynamic: No
* Default: `<code>PT15S</code>`



#### `<code>evs.info_log_mask </code>`


* Description: Controls extra EVS info logging. Bits:

  * 0x1 – extra view change information
  * 0x2 – extra state change information
  * 0x4 – statistics
  * 0x8 – profiling (only available in builds with profiling enabled)
* Dynamic: No
* Default: `<code>0</code>`



#### `<code>evs.install_timeout</code>`


* Description: Timeout on waits for install message acknowledgments. Replaces evs.consensus_timeout.
* Dynamic: Yes
* Default: `<code>PT7.5S</code>`



#### `<code>evs.join_retrans_period</code>`


* Description: Time period for how often retransmission of EVS join messages when forming cluster membership should occur.
* Dynamic: Yes
* Default: `<code>PT1S</code>`



#### `<code>evs.keepalive_period</code>`


* Description: How often keepalive signals should be transmitted when there's no other traffic.
* Dynamic: Yes
* Default: `<code>PT1S</code>`



#### `<code>evs.max_install_timeouts</code>`


* Description: Number of membership install rounds to attempt before timing out. The total rounds will be this value plus two.
* Dynamic: No
* Default: `<code>3</code>`



#### `<code>evs.send_window</code>`


* Description: Maximum number of packets that can be replicated at a time, Must be more than [evs.user_send_window](#evsuser_send_window), which applies to data packets only (double is recommended). In WAN environments can be set much higher than the default, for example `<code>512</code>`.
* Dynamic: Yes
* Default: `<code>4</code>`



#### `<code>evs.stats_report_period</code>`


* Description: Reporting period for EVS statistics.
* Dynamic: No
* Default: `<code>PT1M</code>`



#### `<code>evs.suspect_timeout</code>`


* Description: A node will be suspected to be dead after this period of inactivity. If all nodes agree, the node is dropped from the cluster before [evs.inactive_timeout](#evsinactive_timeout) is reached.
* Dynamic: No
* Default: `<code>PT5S</code>`



#### `<code>evs.use_aggregate</code>`


* Description: If set to `<code>true</code>` (the default), small packets will be aggregated into one where possible.
* Dynamic: No
* Default: `<code>true</code>`



#### `<code>evs.user_send_window</code>`


* Description: Maximum number of data packets that can be replicated at a time. Must be smaller than [evs.send_window](#evssend_window) (half is recommended). In WAN environments can be set much higher than the default, for example `<code>512</code>`.
* Dynamic: Yes
* Default: `<code>2</code>`



#### `<code>evs.version</code>`


* Description: EVS protocol version. Defaults to `<code>0</code>` for backward compatibility. Certain EVS features (e.g. auto eviction) require more recent versions.
* Dynamic: No
* Default: `<code>0</code>`



#### `<code>evs.view_forget_timeout</code>`


* Description: Time after which past views will be dropped from the view history.
* Dynamic: No
* Default: `<code>P1D</code>`



#### `<code>gcache.dir</code>`


* Description: Directory where GCache files are placed.
* Dynamic: No
* Default: The working directory



#### `<code>gcache.keep_pages_size</code>`


* Description: Total size of the page storage pages for caching. One page is always present if only page storage is enabled.
* Dynamic: No
* Default: `<code>0</code>`



#### `<code>gcache.mem_size</code>`


* Description: Maximum size of size of the malloc() store for setups that have spare RAM.
* Dynamic: No
* Default: `<code>0</code>`



#### `<code>gcache.name</code>`


* Description: Gcache ring buffer storage file name. By default placed in the working directory, changing to another location or partition can reduce disk IO.
* Dynamic: No
* Default: `<code>./galera.cache</code>`
---


#### `<code>gcache.page_size</code>`


* Description: Size of the page storage page files. These are prefixed by `<code>gcache.page</code>`. Can be set to as large as the disk can handle.
* Dynamic: No
* Default: `<code>128M</code>`



#### `<code>gcache.recover</code>`


* Description: Whether or not gcache recovery takes place when the node starts up. If it is possible to recover gcache, the node can then provide IST to other joining nodes, which assists when the whole cluster is restarted.
* Dynamic: No
* Default: `<code>no</code>`
* Introduced: [MariaDB 10.1.20](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10120-release-notes.md), [MariaDB Galera 10.0.29](../../../../release-notes/mariadb-community-server/mariadb-galera-cluster-releases/mariadb-galera-100-release-notes/mariadb-galera-cluster-10029-release-notes.md), [MariaDB Galera 5.5.54](../../../../release-notes/mariadb-community-server/mariadb-galera-cluster-releases/mariadb-galera-55-release-notes/mariadb-galera-cluster-5554-release-notes.md)



#### `<code>gcache.size</code>`


* Description: Gcache ring buffer storage size (the space the node uses for caching write sets), preallocated on startup.
* Dynamic: No
* Default: `<code>128M</code>`



#### `<code>gcomm.thread_prio</code>`


* Description: Gcomm thread policy and priority (in the format `<code>policy:priority</code>`. Priority is an integer, while policy can be one of:

  * `<code>fifo</code>`: First-in, first-out scheduling. Always preempt other, batch or idle threads and can only be preempted by other `<code>fifo</code>` threads of a higher priority or blocked by an I/O request.
  * `<code>rr</code>`: Round-robin scheduling. Always preempt other, batch or idle threads. Runs for a fixed period of time after which the thread is stopped and moved to the end of the list, being replaced by another round-robin thread with the same priority. Otherwise runs until preempted by other `<code>rr</code>` threads of a higher priority or blocked by an I/O request.
  * `<code>other</code>`: Default scheduling on Linux. Threads run until preempted by a thread of a higher priority or a superior scheduling designation, or blocked by an I/O request.
* Dynamic: No
* Default: Empty string



#### `<code>gcs.fc_debug</code>`


* Description: If set to a value greater than zero (the default), debug statistics about SST flow control will be posted each time after the specified number of writesets.
* Dynamic: No
* Default: `<code>0</code>`



#### `<code>gcs.fc_factor</code>`


* Description:Fraction below [gcs.fc_limit](#gcsfc_limit) which if the recv queue drops below, replication resumes.
* Dynamic: Yes
* Default: `<code>1.0</code>`



#### `<code>gcs.fc_limit</code>`


* Description: If the recv queue exceeds this many writesets, replication is paused. Can increase greatly in master-slave setups. Replication will resume again according to the [gcs.fc_factor](#gcsfc_factor) setting.
* Dynamic: Yes
* Default: `<code>16</code>`



#### `<code>gcs.fc_master_slave</code>`


* Description: Whether to assume that the cluster only contains one master. Deprecated since Galera 4.10 ([MariaDB 10.8.1](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-8-series/mariadb-1081-release-notes.md), [MariaDB 10.7.2](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-7-series/mariadb-1072-release-notes.md), [MariaDB 10.6.6](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-1066-release-notes.md), [MariaDB 10.5.14](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-10514-release-notes.md), [MariaDB 10.4.22](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-4-series/mariadb-10422-release-notes.md)) - see [gcs.fc_single_primary](#gcsfc_single_primary)
* Dynamic: No
* Default: `<code>no</code>`


#### `<code>gcs.fc_single_primary</code>`


* Description: Defines whether there is more than one source of replication.
As the number of nodes in the cluster grows, the larger the calculated gcs.fc_limit gets. At the same time, the number of writes from the nodes increases.
When this parameter value is set to NO (multi-primary), the gcs.fc_limit parameter is dynamically modified to give more margin for each node to be a bit further behind applying writes.
The gcs.fc_limit parameter is modified by the square root of the cluster size, that is, in a four-node cluster it is two times higher than the base value. This is done to compensate for the increasing replication rate noise.
* Dynamic: No
* Default: `<code>no</code>`



#### `<code>gcs.max_packet_size</code>`


* Description: Maximum packet size, after which writesets become fragmented.
* Dynamic: No
* Default: `<code>64500</code>`



#### `<code>gcs.max_throttle</code>`


* Description: How much we can throttle replication rate during state transfer (to avoid running out of memory). Set it to 0.0 if stopping replication is acceptable for the sake of completing state transfer.
* Dynamic: No
* Default: `<code>0.25</code>`



#### `<code>gcs.recv_q_hard_limit</code>`


* Description: Maximum size of the recv queue. If exceeded, the server aborts. Half of available RAM plus swap is a recommended size.
* Dynamic: No
* Default: LLONG_MAX



#### `<code>gcs.recv_q_soft_limit</code>`


* Description: Fraction of [gcs.recv_q_hard_limit](#gcsrecv_q_hard_limit) after which replication rate is throttled. The rate of throttling increases linearly from zero (the regular, varying rate of replication) at and below `<code>csrecv_q_soft_limit</code>` to one (full throttling) at [gcs.recv_q_hard_limit](#gcsrecv_q_hard_limit)
* Dynamic: No
* Default: `<code>0.25</code>`



#### `<code>gcs.sync_donor</code>`


* Description: Whether or not the rest of the cluster should stay in sync with the donor. If set to `<code>YES</code>` (`<code>NO</code>` is default), if the donor is blocked by state transfer, the whole cluster is also blocked.
* Dynamic: No
* Default: `<code>no</code>`



#### `<code>gmcast.listen_addr</code>`


* Description: Address Galera listens for connections from other nodes. Can be used to override the default port to listen, which is obtained from the connection address.
* Dynamic: No
* Default: `<code>tcp://0.0.0.0:4567</code>`



#### `<code>gmcast.mcast_addr</code>`


* Description: Not set by default, but if set, UDP multicast will be used for replication. Must be identical on all nodes.For example, `<code>gmcast.mcast_addr=239.192.0.11</code>`
* Dynamic: No
* Default: None



#### `<code>gmcast.mcast_ttl</code>`


* Description: Multicast packet TTL (time to live) value.
* Dynamic: No
* Default: `<code>1</code>`



#### `<code>gmcast.peer_timeout</code>`


* Description: Connection timeout for initiating message relaying.
* Dynamic: No
* Default: `<code>PT3S</code>`



#### `<code>gmcast.segment</code>`


* Description: Defines the segment to which the node belongs. By default, all nodes are placed in the same segment (`<code>0</code>`). Usually, you would place all nodes in the same datacenter in the same segment. Galera protocol traffic is only redirected to one node in each segment, and then relayed to other nodes in that same segment, which saves cross-datacenter network traffic at the expense of some extra latency. State transfers are also, preferably but not exclusively, taken from the same segment. If there are no nodes available in the same segment, state transfer will be taken from a node in another segment.
* Dynamic: No
* Default: `<code>0</code>`
* Range: `<code>0</code>` to `<code>255</code>`



#### `<code>gmcast.time_wait</code>`


* Description: Waiting time before allowing a peer that was declared outside of the stable view to reconnect.
* Dynamic: No
* Default: `<code>PT5S</code>`



#### `<code>gmcast.version</code>`


* Description: Deprecated option. Gmcast version.
* Dynamic: No
* Default: `<code>0</code>`



#### `<code>ist.recv_addr</code>`


* Description: Address for listening for Incremental State Transfer.
* Dynamic: No
* Default: <address>:<port+1> from [wsrep_node_address](galera-cluster-system-variables.md#wsrep_node_address)



#### `<code>ist.recv_bind</code>`


* Description:
* Dynamic: No
* Default: Empty string
* Introduced: [MariaDB 10.1.17](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10117-release-notes.md), [MariaDB Galera 10.0.27](../../../../release-notes/mariadb-community-server/mariadb-galera-cluster-releases/mariadb-galera-100-release-notes/mariadb-galera-cluster-10027-release-notes.md), [MariaDB Galera 5.5.51](../../../../release-notes/mariadb-community-server/mariadb-galera-cluster-releases/mariadb-galera-55-release-notes/mariadb-galera-cluster-5551-release-notes.md)



#### `<code>pc.announce_timeout</code>`


* Description: Period of time for which cluster joining announcements are sent every 1/2 second.
* Dynamic: No
* Default: `<code>PT3S</code>`



#### `<code>pc.checksum</code>`


* Description: For debug purposes, by default `<code>false</code>` (`<code>true</code>` in earlier releases), indicates whether to checksum replicated messages on PC level. Safe to turn off.
* Dynamic: No
* Default: `<code>false</code>`



#### `<code>pc.ignore_quorum</code>`


* Description: Whether to ignore quorum calculations, for example when a master splits from several slaves, it will remain in operation if set to `<code>true</code>` (`<code>false is default</code>`). Use with care however, as in master-slave setups, slaves will not automatically reconnect to the master if set.
* Dynamic: Yes
* Default: `<code>false</code>`



#### `<code>pc.ignore_sb</code>`


* Description: Whether to permit updates to be processed even in the case of split brain (when a node is disconnected from its remaining peers). Safe in master-slave setups, but could lead to data inconsistency in a multi-master setup.
* Dynamic: Yes
* Default: `<code>false</code>`



#### `<code>pc.linger</code>`


* Description: Time that the PC protocol waits for EVS termination.
* Dynamic: No
* Default: `<code>PT20S</code>`



#### `<code>pc.npvo</code>`


* Description: If set to `<code>true</code>` (`<code>false</code>` is default), when there are primary component conficts, the most recent component will override the older.
* Dynamic: No
* Default: `<code>false</code>`



#### `<code>pc.recovery</code>`


* Description: If set to `<code>true</code>` (the default), the Primary Component state is stored on disk and in the case of a full cluster crash (e.g power outages), automatic recovery is then possible. Subsequent graceful full cluster restarts will require explicit bootstrapping for a new Primary Component.
* Dynamic: No
* Default: `<code>true</code>`



#### `<code>pc.version</code>`


* Description: Deprecated option. PC protocol version.
* Dynamic: No
* Default: `<code>0</code>`



#### `<code>pc.wait_prim</code>`


* Description: When set to `<code>true</code>`, the default, the node will wait for a primary component for the period of time specified by [pc.wait_prim_timeout](#pc.wait_prim_timeout). Used to bring up non-primary components and make them primary using [pc.bootstrap](#pcbootstrap.).
* Dynamic: No
* Default: `<code>true</code>`



#### `<code>pc.wait_prim_timeout</code>`


* Description: Ttime to wait for a primary component. See [pc.wait_prim](#pcwait_prim).
* Dynamic: No
* Default: `<code>PT30S</code>`



#### `<code>pc.weight</code>`


* Description: Node weight, used for quorum calculation. See the Codership article [Weighted Quorum](https://galeracluster.com/library/documentation/weighted-quorum.html#weighted-quorum).
* Dynamic: Yes
* Default: `<code>1</code>`



#### `<code>protonet.backend </code>`


* Description: Deprecated option. Transport backend to use. Only ASIO is supported currently.
* Dynamic: No
* Default: `<code>asio</code>`



#### `<code>protonet.version</code>`


* Description: Deprecated option. Protonet version.
* Dynamic: No
* Default: `<code>0</code>`



#### `<code>repl.causal_read_timeout</code>`


* Description: Timeout period for causal reads.
* Dynamic: Yes
* Default: `<code>PT30S</code>`



#### `<code>repl.commit_order</code>`


* Description: Whether or not out-of-order committing is permitted, and under what conditions. By default it is not permitted, but setting this can improve parallel performance.

  * `<code>0</code>` BYPASS: No commit order monitoring is done (useful for measuring the performance penalty).
  * `<code>1</code>` OOOC: Out-of-order committing is permitted for all transactions.
  * `<code>2</code>` LOCAL_OOOC: Out-of-order committing is permitted for local transactions only.
  * `<code>3</code>` NO_OOOC: Out-of-order committing is not permitted at all.
* Dynamic: No
* Default: `<code>3</code>`



#### `<code>repl.key_format</code>`


* Description: Format for key replication. Can be one of:

  * `<code>FLAT8</code>` - shorter key with a higher probability of false positives when matching
  * `<code>FLAT16</code>` - longer key with a lower probability of false positives when matching
  * `<code>FLAT8A</code>` - shorter key with a higher probability of false positives when matching, includes annotations for debug purposes
  * `<code>FLAT16A</code>` - longer key with a lower probability of false positives when matching, includes annotations for debug purposes
* Dynamic: Yes
* Default: `<code>FLAT8</code>`



#### `<code>repl.max_ws_size</code>`


* Description:
* Dynamic:
* Default: `<code>2147483647</code>`



#### `<code>repl.proto_max</code>`


* Description:
* Dynamic:
* Default: `<code>9</code>`



#### `<code>socket.checksum</code>`


* Description: Method used for generating checksum. Note: If Galera 25.2.x and 25.3.x are both being used in the cluster, MariaDB with Galera 25.3.x must be started with `<code>wsrep_provider_options='socket.checksum=1'</code>` in order to make it backward compatible with Galera v2. Galera wsrep providers other than 25.3.x or 25.2.x are not supported.
* Dynamic: No
* Default: `<code>2</code>`



#### `<code>socket.dynamic</code>`


* Description: Allow both encrypted and unencrypted connections between nodes. Typically this should be set to `<code>false</code>` (the default), when set to `<code>true</code>` encrypted connections will still be preferred, but will fall back to unencrypted connections when encryption is not possible, e.g. not enabled on all nodes yet. Needs to be `<code>true</code>` on all nodes when wanting to enable or disable encryption via a rolling restart. As this can't be changed at runtime a rolling restart to enable or disable encryption may need three restarts per node in total: one to enable `<code>socket.dynamic</code>` on each node, one to change the actual encryption settings on each node, and a final round to change `<code>socket.dynamic</code>` back to `<code>false</code>`.
* Dynamic: No
* Default: `<code>false</code>`
* Introduced: [MariaDB 10.4.19](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-4-series/mariadb-10419-release-notes.md), [MariaDB 10.5.10](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-10510-release-notes.md), [MariaDB 10.6.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-1060-release-notes.md)



#### `<code>socket.recv_buf_size</code>`


* Description: Size in bytes of the receive buffer used on the network sockets between nodes, passed on to the kernel via the SO_RCVBUF socket option.
* Dynamic: No
* Default:

  * >= [MariaDB 10.3.23](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-10323-release-notes.md), [MariaDB 10.2.32](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-10232-release-notes.md), [MariaDB 10.1.45](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10145-release-notes.md): Auto
  * < [MariaDB 10.3.22](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-10322-release-notes.md): [MariaDB 10.2.31](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-10231-release-notes.md), [MariaDB 10.1.44](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10144-release-notes.md): `<code>212992</code>`



#### `<code>socket.send_buf_size</code>`


* Description: Size in bytes of the send buffer used on the network sockets between nodes, passed on to the kernel via the SO_SNDBUF socket option.
* Dynamic: No
* Default:: Auto
* Introduced: [MariaDB 10.3.23](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-10323-release-notes.md), [MariaDB 10.2.32](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-10232-release-notes.md), [MariaDB 10.1.45](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10145-release-notes.md)



#### `<code>socket.ssl</code>`


* Description: Explicitly enables TLS usage by the wsrep Provider.
* Dynamic: No
* Default: `<code>NO</code>`



#### `<code>socket.ssl_ca</code>`


* Description: Path to Certificate Authority (CA) file. Implicitly enables the `<code>[socket.ssl](#socket.ssl)</code>` option.
* Dynamic: No



#### `<code>socket.ssl_cert</code>`


* Description: Path to TLS certificate. Implicitly enables the `<code>[socket.ssl](#socket.ssl)</code>` option.
* Dynamic: No



#### `<code>socket.ssl_cipher</code>`


* Description: TLS cipher to use. Implicitly enables the `<code>[socket.ssl](#socket.ssl)</code>` option. Since [MariaDB 10.2.18](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-10218-release-notes.md) defaults to the value of the `<code>[ssl_cipher](../../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/ssltls-system-variables.md#ssl_cipher)</code>` system variable.
* Dynamic: No
* Default: system default, before [MariaDB 10.2.18](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-10218-release-notes.md) defaults to `<code>AES128-SHA</code>`.



#### `<code>socket.ssl_compression</code>`


* Description: Compression to use on TLS connections. Implicitly enables the `<code>[socket.ssl](#socket.ssl)</code>` option.
* Dynamic: No



#### `<code>socket.ssl_key</code>`


* Description: Path to TLS key file. Implicitly enables the `<code>[socket.ssl](#socket.ssl)</code>` option.
* Dynamic: No



#### `<code>socket.ssl_password_file</code>`


* Description: Path to password file to use in TLS connections. Implicitly enables the `<code>[socket.ssl](#socket.ssl)</code>` option.
* Dynamic: No



## See Also


* [Galera parameters documentation from Codership](https://galeracluster.com/library/documentation/galera-parameters.html)

