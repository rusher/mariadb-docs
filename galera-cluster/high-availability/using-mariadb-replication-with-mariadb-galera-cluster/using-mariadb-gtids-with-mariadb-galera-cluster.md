# Using MariaDB GTIDs with MariaDB Galera Cluster

MariaDB's [global transaction IDs (GTIDs)](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid) are very useful when used with [MariaDB replication](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication), which is primarily what that feature was developed for. [Galera Cluster](https://galeracluster.com/), on the other hand, was developed by Codership for all MySQL and MariaDB variants, and the initial development of the technology pre-dated MariaDB's [GTID](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid) implementation. As a side effect, [MariaDB Galera Cluster](../../../kb/en/galera-cluster/) (at least until [MariaDB 10.5.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-5-series/mariadb-1051-release-notes)) only partially supports MariaDB's [GTID](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid) implementation.

## GTID Support for Write Sets Replicated by Galera Cluster

Galera Cluster has its own [certification-based replication method](../../galera-cluster-quickstart-guides/about-galera-replication.md) that is substantially different from [MariaDB replication](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication). However, it would still be beneficial if [MariaDB Galera Cluster](../../../kb/en/galera-cluster/) was able to associate a Galera Cluster write set with a [GTID](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid) that is globally unique, but that is also consistent for that write set on each cluster node.

Before [MariaDB 10.5.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-5-series/mariadb-1051-release-notes), [MariaDB Galera Cluster](../../../kb/en/galera-cluster/) did not replicate the original [GTID](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid) with the write set except in cases where the transaction was originally applied by a [slave SQL thread](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-threads#slave-sql-thread). Each node independently generated its own [GTID](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid) for each write set in most cases. See [MDEV-20720](https://jira.mariadb.org/browse/MDEV-20720).

### Wsrep GTID Mode

MariaDB supports [wsrep\_gtid\_mode](../../reference/galera-cluster-system-variables.md#wsrep_gtid_mode).

MariaDB has a feature called wsrep GTID mode. When this mode is enabled, MariaDB uses some tricks to try to associate each Galera Cluster write set with a [GTID](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid) that is globally unique, but that is also consistent for that write set on each cluster node. These tricks work in some cases, but [GTIDs](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid) can still become inconsistent among cluster nodes.

#### Enabling Wsrep GTID Mode

Several things need to be configured for wsrep GTID mode to work, such as:

* `[wsrep_gtid_mode=ON](../../reference/galera-cluster-system-variables.md#wsrep_gtid_mode)` needs to be set on all nodes in the cluster.
* `[wsrep_gtid_domain_id](../../reference/galera-cluster-system-variables.md#wsrep_gtid_domain_id)` needs to be set to the same value on all nodes in a given cluster, so that each cluster node uses the same domain when assigning [GTIDs](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid) for Galera Cluster's write sets. When replicating between two clusters, each cluster should have this set to a different value, so that each cluster uses different domains when assigning [GTIDs](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid) for their write sets.
* `[log_slave_updates](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables#log_slave_updates)` needs to be enabled on all nodes in the cluster. See [MDEV-9855](https://jira.mariadb.org/browse/MDEV-9855).
* `[log_bin](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables)` needs to be set to the same path on all nodes in the cluster. See [MDEV-9856](https://jira.mariadb.org/browse/MDEV-9856).

And as an extra safety measure:

* `[gtid_domain_id](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/replication-cluster-multi-master/standard-replication/gtid#gtid_domain_id)` should be set to a different value on all nodes in a given cluster, and each of these values should be different than the configured `[wsrep_gtid_domain_id](../../reference/galera-cluster-system-variables.md#wsrep_gtid_domain_id)` value. This is to prevent a node from using the same domain used for Galera Cluster's write sets when assigning [GTIDs](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid) for non-Galera transactions, such as DDL executed with `[wsrep_sst_method=RSU](../../reference/galera-cluster-system-variables.md#wsrep_sst_method)` set or DML executed with `[wsrep_on=OFF](../../reference/galera-cluster-system-variables.md#wsrep_on)` set.

If you want to avoid writes accidentialy local GTIDS, you can avoid it with`[wsrep_gtid_mode](../../reference/galera-cluster-system-variables.md#wsrep_gtid_mode)` = DISALLOW\_LOCAL\_GTID

In this case you get an error:\
ERROR 4165 (HY000): Galera replication not supported

You can overwrite it temporarily with\
set `[sql_log_bin](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables)` = 0;

For information on setting `[server_id](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables#server_id)`, see [Using MariaDB Replication with MariaDB Galera Cluster: Setting server\_id on Cluster Nodes](using-mariadb-replication-with-mariadb-galera-cluster-using-mariadb-replica.md#setting-server_id-on-cluster-nodes).

#### Known Problems with Wsrep GTID Mode

Until [MariaDB 10.5.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-5-series/mariadb-1051-release-notes), there were known cases where [GTIDs](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid) could become inconsistent across the cluster nodes.

A known issue (fixed in [MariaDB 10.5.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-5-series/mariadb-1051-release-notes)) is:

* Implicitly dropped temporary tables can make GTIDs inconsistent. See [MDEV-14153](https://jira.mariadb.org/browse/MDEV-14153) and [MDEV-20720](https://jira.mariadb.org/browse/MDEV-20720).

This does not necessarily imply that wsrep GTID mode works perfectly in all other situations. If you discover any other issues with it, please [report a bug](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/bug-tracking/reporting-bugs).

### GTIDs for Transactions Applied by Slave Thread

If a Galera Cluster node is also a [replication slave](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-overview), then that node's [slave SQL thread](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-threads#slave-sql-thread) will be applying transactions that it replicates from its replication master. If the node has `[log_slave_updates=ON](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables#log_slave_updates)` set, then each transaction that the [slave SQL thread](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-threads#slave-sql-thread) applies will also generate a Galera Cluster write set that is replicated to the rest of the nodes in the cluster.

In [MariaDB 10.1.30](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-1-series/mariadb-10130-release-notes) and earlier, the node acting as slave would apply the transaction with the original GTID that it received from the master, and the other Galera Cluster nodes would generate their own GTIDs for the transaction when they replicated the write set.

In [MariaDB 10.1.31](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-1-series/mariadb-10131-release-notes) and later, the node acting as slave will include the transaction's original `Gtid_Log_Event` in the replicated write set, so all nodes should associate the write set with its original GTID. See [MDEV-13431](https://jira.mariadb.org/browse/MDEV-13431) about that.

CC BY-SA / Gnu FDL
