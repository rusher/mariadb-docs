# Using MariaDB Replication with MariaDB Galera Cluster

[MariaDB replication](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication) and [MariaDB Galera Cluster](https://github.com/mariadb-corporation/docs-server/blob/test/kb/en/galera-cluster/README.md) can be used together. However, there are some things that have to be taken into account.

## Tutorials

If you want to use [MariaDB replication](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication) and [MariaDB Galera Cluster](https://github.com/mariadb-corporation/docs-server/blob/test/kb/en/galera-cluster/README.md) together, then the following tutorials may be useful:

* [Configuring MariaDB Replication between MariaDB Galera Cluster and MariaDB Server](https://github.com/mariadb-corporation/docs-server/blob/test/kb/en/using-mariadb-replication-with-mariadb-galera-cluster-configuring-mariadb-r/README.md)
* [Configuring MariaDB Replication between Two MariaDB Galera Clusters](configuring-mariadb-replication-between-two-mariadb-galera-clusters.md)

## Configuring a Cluster Node as a Replication Master

If a Galera Cluster node is also a [replication master](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-overview), then some additional configuration may be needed.

Like with [MariaDB replication](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication), write sets that are received by a node with [Galera Cluster's certification-based replication](../../readme/about-galera-replication.md) are not written to the [binary log](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/server-monitoring-logs/binary-log) by default.

If the node is a replication master, then its replication slaves only replicate transactions which are in the binary log, so this means that the transactions that correspond to Galera Cluster write-sets would not be replicated by any replication slaves by default. If you would like a node to write its replicated write sets to the [binary log](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/server-monitoring-logs/binary-log), then you will have to set `[log_slave_updates=ON](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables#log_slave_updates)`. If the node has any replication slaves, then this would also allow those slaves to replicate the transactions that corresponded to those write sets.

See [Configuring MariaDB Galera Cluster: Writing Replicated Write Sets to the Binary Log](../../galera-management/configuring-mariadb-galera-cluster.md#writing-replicated-write-sets-to-the-binary-log) for more information.

## Configuring a Cluster Node as a Replication Slave

If a Galera Cluster node is also a [replication slave](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-overview), then some additional configuration may be needed.

If the node is a replication slave, then the node's [slave SQL thread](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-threads#slave-sql-thread) will be applying transactions that it replicates from its replication master. Transactions applied by the slave SQL thread will only generate Galera Cluster write-sets if the node has `[log_slave_updates=ON](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables#log_slave_updates)` set. Therefore, in order to replicate these transactions to the rest of the nodes in the cluster, `[log_slave_updates=ON](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables#log_slave_updates)` must be set.

If the node is a replication slave, then it is probably also a good idea to enable `[wsrep_restart_slave](../../reference/galera-cluster-system-variables.md#wsrep_restart_slave)`. When this is enabled, the node will restart its [slave threads](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-threads#threads-on-the-slave) whenever it rejoins the cluster.

## Replication Filters

Both [MariaDB replication](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication) and [MariaDB Galera Cluster](https://github.com/mariadb-corporation/docs-server/blob/test/kb/en/galera-cluster/README.md) support [replication filters](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-filters), so extra caution must be taken when using all of these features together. See [Configuring MariaDB Galera Cluster: Replication Filters](../../galera-management/configuring-mariadb-galera-cluster.md#replication-filters) for more details on how MariaDB Galera Cluster interprets replication filters.

## Setting server\_id on Cluster Nodes

### Setting the Same server\_id on Each Cluster Node

It is most common to set `[server_id](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables#server_id)` to the same value on each node in a given cluster. Since [MariaDB Galera Cluster](https://github.com/mariadb-corporation/docs-server/blob/test/kb/en/galera-cluster/README.md) uses a [virtually synchronous certification-based replication](../../readme/about-galera-replication.md), all nodes should have the same data, so in a logical sense, a cluster can be considered in many cases a single logical server for purposes related to [MariaDB replication](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication). The [binary logs](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/server-monitoring-logs/binary-log) of each cluster node might even contain roughly the same transactions and [GTIDs](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid) if `[log_slave_updates=ON](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables#log_slave_updates)` is set and if [wsrep GTID mode](using-mariadb-gtids-with-mariadb-galera-cluster.md#wsrep-gtid-mode) is enabled and if non-Galera transactions are not being executed on any nodes.

### Setting a Different server\_id on Each Cluster Node

There are cases when it might make sense to set a different `[server_id](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables#server_id)` value on each node in a given cluster. For example, if `[log_slave_updates=OFF](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables#log_slave_updates)` is set and if another cluster or a standard MariaDB Server is using [multi-source replication](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/multi-source-replication) to replicate transactions from each cluster node individually, then it would be required to set a different `[server_id](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables#server_id)` value on each node for this to work.

Keep in mind that if replication is set up in a scenario where each cluster node has a different `[server_id](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables#server_id)` value, and if the replication topology is set up in such a way that a cluster node can replicate the same transactions through Galera and through MariaDB replication, then you may need to configure the cluster node to ignore these transactions when setting up MariaDB replication. You can do so by setting `[IGNORE_SERVER_IDS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/change-master-to#ignore_server_ids)` to the server IDs of all nodes in the same cluster when executing `[CHANGE MASTER TO](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/change-master-to)`. For example, this might be required when circular replication is set up between two separate clusters, and each cluster node as a different `[server_id](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables#server_id)` value, and each cluster has `[log_slave_updates=ON](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables#log_slave_updates)` set.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
