# Using MariaDB GTIDs with MariaDB Galera Cluster

MariaDB's [global transaction IDs (GTIDs)](../../../../clients-and-utilities/server-client-software/client-libraries/clientserver-protocol/replication-protocol/gtid_event.md) are very useful when used with [MariaDB replication](/kb/en/high-availability-performance-tuning-mariadb-replication/), which is primarily what that feature was developed for. [Galera Cluster](http://galeracluster.com/), on the other hand, was developed by Codership for all MySQL and MariaDB variants, and the initial development of the technology pre-dated MariaDB's [GTID](../../../../clients-and-utilities/server-client-software/client-libraries/clientserver-protocol/replication-protocol/gtid_event.md) implementation. As a side effect, [MariaDB Galera Cluster](../galera-cluster-status-variables.md) (at least until [MariaDB 10.5.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/release-notes-mariadb-105-series/mariadb-1051-release-notes)) only partially supports MariaDB's [GTID](../../../../clients-and-utilities/server-client-software/client-libraries/clientserver-protocol/replication-protocol/gtid_event.md) implementation.

#

# GTID Support for Write Sets Replicated by Galera Cluster

Galera Cluster has its own [certification-based replication method](../about-galera-replication.md) that is substantially different from [MariaDB replication](/kb/en/high-availability-performance-tuning-mariadb-replication/). However, it would still be beneficial if [MariaDB Galera Cluster](../galera-cluster-status-variables.md) was able to associate a Galera Cluster write set with a [GTID](../../../../clients-and-utilities/server-client-software/client-libraries/clientserver-protocol/replication-protocol/gtid_event.md) that is globally unique, but that is also consistent for that write set on each cluster node.

Before [MariaDB 10.5.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/release-notes-mariadb-105-series/mariadb-1051-release-notes), [MariaDB Galera Cluster](../galera-cluster-status-variables.md) did not replicate the original [GTID](../../../../clients-and-utilities/server-client-software/client-libraries/clientserver-protocol/replication-protocol/gtid_event.md) with the write set except in cases where the transaction was originally applied by a [slave SQL thread](../../standard-replication/replication-threads.md#slave-sql-thread). Each node independently generated its own [GTID](../../../../clients-and-utilities/server-client-software/client-libraries/clientserver-protocol/replication-protocol/gtid_event.md) for each write set in most cases. See [MDEV-20720](https://jira.mariadb.org/browse/MDEV-20720).

#

## Wsrep GTID Mode

MariaDB supports [wsrep_gtid_mode](../galera-cluster-system-variables.md#wsrep_gtid_mode).

MariaDB has a feature called wsrep GTID mode. When this mode is enabled, MariaDB uses some tricks to try to associate each Galera Cluster write set with a [GTID](../../../../clients-and-utilities/server-client-software/client-libraries/clientserver-protocol/replication-protocol/gtid_event.md) that is globally unique, but that is also consistent for that write set on each cluster node. These tricks work in some cases, but [GTIDs](../../../../clients-and-utilities/server-client-software/client-libraries/clientserver-protocol/replication-protocol/gtid_event.md) can still become inconsistent among cluster nodes.

#

### Enabling Wsrep GTID Mode

Several things need to be configured for wsrep GTID mode to work, such as:

* `[wsrep_gtid_mode=ON](../galera-cluster-system-variables.md#wsrep_gtid_mode)` needs to be set on all nodes in the cluster.

* `[wsrep_gtid_domain_id](../galera-cluster-system-variables.md#wsrep_gtid_domain_id)` needs to be set to the same value on all nodes in a given cluster, so that each cluster node uses the same domain when assigning [GTIDs](../../../../clients-and-utilities/server-client-software/client-libraries/clientserver-protocol/replication-protocol/gtid_event.md) for Galera Cluster's write sets. When replicating between two clusters, each cluster should have this set to a different value, so that each cluster uses different domains when assigning [GTIDs](../../../../clients-and-utilities/server-client-software/client-libraries/clientserver-protocol/replication-protocol/gtid_event.md) for their write sets.

* `[log_slave_updates](../../standard-replication/replication-and-binary-log-system-variables.md#log_slave_updates)` needs to be enabled on all nodes in the cluster. See [MDEV-9855](https://jira.mariadb.org/browse/MDEV-9855).

* `[log_bin](/kb/en/replication-and-binary-log-server-system-variables/#log_bin)` needs to be set to the same path on all nodes in the cluster. See [MDEV-9856](https://jira.mariadb.org/browse/MDEV-9856).

And as an extra safety measure:

* `[gtid_domain_id](../../../../clients-and-utilities/server-client-software/client-libraries/clientserver-protocol/replication-protocol/gtid_event.md#gtid_domain_id)` should be set to a different value on all nodes in a given cluster, and each of these values should be different than the configured `[wsrep_gtid_domain_id](../galera-cluster-system-variables.md#wsrep_gtid_domain_id)` value. This is to prevent a node from using the same domain used for Galera Cluster's write sets when assigning [GTIDs](../../../../clients-and-utilities/server-client-software/client-libraries/clientserver-protocol/replication-protocol/gtid_event.md) for non-Galera transactions, such as DDL executed with `[wsrep_sst_method=RSU](../galera-cluster-system-variables.md#wsrep_sst_method)` set or DML executed with `[wsrep_on=OFF](../galera-cluster-system-variables.md#wsrep_on)` set.

If you want to avoid writes accidentialy local GTIDS, you can avoid it with 
`[wsrep_gtid_mode](../galera-cluster-system-variables.md#wsrep_gtid_mode)` = DISALLOW_LOCAL_GTID

In this case you get an error:
ERROR 4165 (HY000): Galera replication not supported

You can overwrite it temporarily with
set `[sql_log_bin](/kb/en/replication-and-binary-log-server-system-variables/#sql_log_bin)` = 0;

For information on setting `[server_id](../../standard-replication/replication-and-binary-log-system-variables.md#server_id)`, see [Using MariaDB Replication with MariaDB Galera Cluster: Setting server_id on Cluster Nodes](using-mariadb-replication-with-mariadb-galera-cluster-using-mariadb-replica.md#setting-server_id-on-cluster-nodes).

#

### Known Problems with Wsrep GTID Mode

Until [MariaDB 10.5.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/release-notes-mariadb-105-series/mariadb-1051-release-notes), there were known cases where [GTIDs](../../../../clients-and-utilities/server-client-software/client-libraries/clientserver-protocol/replication-protocol/gtid_event.md) could become inconsistent across the cluster nodes.

A known issue (fixed in [MariaDB 10.5.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/release-notes-mariadb-105-series/mariadb-1051-release-notes)) is:

* Implicitly dropped temporary tables can make GTIDs inconsistent. See [MDEV-14153](https://jira.mariadb.org/browse/MDEV-14153) and [MDEV-20720](https://jira.mariadb.org/browse/MDEV-20720).

This does not necessarily imply that wsrep GTID mode works perfectly in all other situations. If you discover any other issues with it, please [report a bug](/kb/en/mariadb-community-bug-reporting/#reporting-a-bug).

#

## GTIDs for Transactions Applied by Slave Thread

If a Galera Cluster node is also a [replication slave](../../standard-replication/replication-overview.md), then that node's [slave SQL thread](../../standard-replication/replication-threads.md#slave-sql-thread) will be applying transactions that it replicates from its replication master. If the node has `[log_slave_updates=ON](../../standard-replication/replication-and-binary-log-system-variables.md#log_slave_updates)` set, then each transaction that the [slave SQL thread](../../standard-replication/replication-threads.md#slave-sql-thread) applies will also generate a Galera Cluster write set that is replicated to the rest of the nodes in the cluster.

In [MariaDB 10.1.30](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/release-notes-mariadb-101-series/mariadb-10130-release-notes) and earlier, the node acting as slave would apply the transaction with the original GTID that it received from the master, and the other Galera Cluster nodes would generate their own GTIDs for the transaction when they replicated the write set.

In [MariaDB 10.1.31](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/release-notes-mariadb-101-series/mariadb-10131-release-notes) and later, the node acting as slave will include the transaction's original `Gtid_Log_Event` in the replicated write set, so all nodes should associate the write set with its original GTID. See [MDEV-13431](https://jira.mariadb.org/browse/MDEV-13431) about that.