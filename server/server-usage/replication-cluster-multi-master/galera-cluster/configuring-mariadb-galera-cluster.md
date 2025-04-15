
# Configuring MariaDB Galera Cluster


A number of options need to be set in order for Galera Cluster to work when using MariaDB. These should be set in the [MariaDB option file](../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md).


## Mandatory Options


Several options are mandatory, which means that they *must* be set in order for Galera Cluster to be enabled or to work properly with MariaDB. The mandatory options are:


* `<code>[wsrep_provider](galera-cluster-system-variables.md#wsrep_provider)</code>` — Path to the Galera library
* `<code>[wsrep_cluster_address](galera-cluster-system-variables.md#wsrep_cluster_address)</code>` — See [Galera Cluster address format and usage](galera-cluster-address.md)
* `<code>[binlog_format=ROW](../standard-replication/replication-and-binary-log-system-variables.md)</code>` — See [Binary Log Formats](../../../server-management/server-monitoring-logs/binary-log/binary-log-formats.md)
* `<code>[wsrep_on=ON](galera-cluster-system-variables.md#wsrep_on)</code>` — Enable wsrep replication
* `<code>[default_storage_engine=InnoDB](../optimization-and-tuning/system-variables/server-system-variables.md#default_storage_engine)</code>` — This is the default value, or alternately `<code>[wsrep_replicate_myisam=1](galera-cluster-system-variables.md#wsrep_replicate_myisam)</code>` (before [MariaDB 10.6](../../../../release-notes/mariadb-community-server/what-is-mariadb-106.md)) or `<code>[galera-cluster-system-variables/#wsrep_mode=REPLICATE_ARIA,REPLICATE_MYISAM](galera-cluster-system-variables.md#wsrep_mode%3DREPLICATE_ARIA%2CREPLICATE_MYISAM)</code>` ([MariaDB 10.6](../../../../release-notes/mariadb-community-server/what-is-mariadb-106.md) and later)
* `<code>[innodb_doublewrite=1](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_doublewrite)</code>` — This is the default value, and should not be changed.


## Performance-related Options


These are optional optimizations that can be made to improve performance.


* `<code>[innodb_flush_log_at_trx_commit=0](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_flush_log_at_trx_commit)</code>` — This is not usually recommended in the case of standard MariaDB. However, it is a safer, recommended option with Galera Cluster, since inconsistencies can always be fixed by recovering from another node.


* `<code>[innodb_autoinc_lock_mode=2](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_autoinc_lock_mode)</code>` — This tells InnoDB to use interleaved method. Interleaved is the fastest and most scalable lock mode, and should be used when BINLOG_FORMAT is set to ROW.
Setting the auto-increment lock mode for InnoDB to interleaved, you’re allowing slaves threads to operate in parallel.


* `<code>[wsrep_slave_threads=4](galera-cluster-system-variables.md#wsrep_slave_threads)</code>` 
— This makes state transfers quicker for new nodes. You should start with four slave threads per CPU core.
The logic here is that, in a balanced system, four slave threads can typically saturate a CPU core. However, I/O performance can increase this figure several times over. For example, a single-core ThinkPad R51 with a 4200 RPM drive can use thirty-two slave threads. The value should not be set higher than [wsrep_cert_deps_distance](galera-cluster-status-variables.md#wsrep_cert_deps_distance).


## Writing Replicated Write Sets to the Binary Log


Like with [MariaDB replication](../standard-replication/README.md), write sets that are received by a node with [Galera Cluster's certification-based replication](about-galera-replication.md) are not written to the [binary log](../../../reference/storage-engines/innodb/binary-log-group-commit-and-innodb-flushing-performance.md) by default. If you would like a node to write its replicated write sets to the [binary log](../../../reference/storage-engines/innodb/binary-log-group-commit-and-innodb-flushing-performance.md), then you will have to set `<code>[log_slave_updates=ON](../standard-replication/replication-and-binary-log-system-variables.md#log_slave_updates)</code>`. This is especially helpful if the node is a replication master. See [Using MariaDB Replication with MariaDB Galera Cluster: Configuring a Cluster Node as a Replication Master](using-mariadb-replication-with-mariadb-galera-cluster/using-mariadb-replication-with-mariadb-galera-cluster-using-mariadb-replica.md).


## Replication Filters


Like with [MariaDB replication](../standard-replication/README.md), [replication filters](../standard-replication/replication-filters.md) can be used to filter write sets from being replicated by [Galera Cluster's certification-based replication](about-galera-replication.md). However, they should be used with caution because they may not work as you'd expect.


The following replication filters are honored for [InnoDB](../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/innodb-upgrade-tests/README.md) DML, but not DDL:


* `<code>[binlog_do_db](../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md)</code>`
* `<code>[binlog_ignore_db](../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md)</code>`
* `<code>[replicate_wild_do_table](../standard-replication/replication-and-binary-log-system-variables.md)</code>`
* `<code>[replicate_wild_ignore_table](../standard-replication/replication-and-binary-log-system-variables.md)</code>`


The following replication filters are honored for DML and DDL for tables that use both the [InnoDB](../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/innodb-upgrade-tests/README.md) and [MyISAM](../../../reference/storage-engines/myisam-storage-engine/README.md) storage engines:


* `<code>[replicate_do_table](../standard-replication/replication-and-binary-log-system-variables.md)</code>`
* `<code>[replicate_ignore_table](../standard-replication/replication-and-binary-log-system-variables.md)</code>`


However, it should be kept in mind that if replication filters cause inconsistencies that lead to replication errors, then nodes may abort.


See also [MDEV-421](https://jira.mariadb.org/browse/MDEV-421) and [MDEV-6229](https://jira.mariadb.org/browse/MDEV-6229).


## Network Ports


Galera Cluster needs access to the following ports:


* Standard MariaDB Port (default: 3306) - For MySQL client connections and [State Snapshot Transfers](state-snapshot-transfers-ssts-in-galera-cluster/introduction-to-state-snapshot-transfers-ssts.md) that use the `<code>mysqldump</code>` method. This can be changed by setting `<code>[port](../optimization-and-tuning/system-variables/server-system-variables.md#port)</code>`.
* Galera Replication Port (default: 4567) - For Galera Cluster replication traffic, multicast replication uses both UDP transport and TCP on this port. Can be changed by setting `<code>[wsrep_node_address](galera-cluster-system-variables.md#wsrep_node_address)</code>`.
* Galera Replication Listening Interface (default: `<code>0.0.0.0:4567</code>`) needs to be set using [gmcast.listen_addr](wsrep_provider_options.md#gmcastlisten_addr), either 

  * in [wsrep_provider_options](galera-cluster-system-variables.md#wsrep_provider_options): `<code>wsrep_provider_options='gmcast.listen_addr=tcp://<IP_ADDR>:<PORT>;'</code>`
  * or in [wsrep_cluster_address](galera-cluster-system-variables.md#wsrep_cluster_address)
* IST Port (default: 4568) - For Incremental State Transfers. Can be changed by setting `<code>[ist.recv_addr](https://galeracluster.com/library/documentation/galera-parameters.html#ist-recv-addr)</code>` in `<code>[wsrep_provider_options](galera-cluster-system-variables.md#wsrep_provider_options)</code>`.
* SST Port (default: 4444) - For all [State Snapshot Transfer](state-snapshot-transfers-ssts-in-galera-cluster/introduction-to-state-snapshot-transfers-ssts.md) methods other than `<code>mysqldump</code>`. Can be changed by setting `<code>[wsrep_sst_receive_address](galera-cluster-system-variables.md#wsrep_sst_receive_address)</code>`.


## Mutiple Galera Cluster Instances on One Server


If you want to run multiple Galera Cluster instances on one server, then you can do so by starting each instance with `<code>[mysqld_multi](../../../clients-and-utilities/legacy-clients-and-utilities/mysqld_multi.md)</code>`, or if you are using [systemd](../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/systemd.md), then you can use the relevant [systemd method for interacting with multiple MariaDB instances](../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/systemd.md#interacting-with-multiple-mariadb-server-processes).


You need to ensure that each instance is configured with a different `<code>[datadir](../optimization-and-tuning/system-variables/server-system-variables.md#datadir)</code>`.


You also need to ensure that each instance is configured with different [network ports](#network-ports).

