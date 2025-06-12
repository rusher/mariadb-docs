# Understanding MaxScale's Read/Write Split Router

MaxScale's [Read/Write Split Router (readwritesplit)](../../../mariadb-maxscale-23-02/mariadb-maxscale-23-02-routers/mariadb-maxscale-2302-readwritesplit.md) performs query-based load balancing. For each client connected to MaxScale, it opens up connections to multiple back-end database servers. When the client sends a write query to MaxScale, it routes the query to the connection opened with the primary server. When the client sends a read query to MaxScale, it routes the query to a connection opened with one of the replicas.

## What Does the Read/Write Split Router Support?

The [Read/Write Split Router (readwritesplit)](../../../mariadb-maxscale-23-02/mariadb-maxscale-23-02-routers/mariadb-maxscale-2302-readwritesplit.md) supports:

* [MariaDB replication](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication) deployments
* [Galera Cluster](../../../../../en/mariadb-galera-cluster-quickstart/) deployments
* [Multi-Node Enterprise ColumnStore](../../../../../en/mariadb-columnstore/) deployments

## When to Use the Read/Write Split Router?

The [Read/Write Split Router (readwritesplit)](../../../mariadb-maxscale-23-02/mariadb-maxscale-23-02-routers/mariadb-maxscale-2302-readwritesplit.md) allows you to:

* Perform query-based load balancing.
* Route client connections to multiple servers simultaneously.
* Route write queries to primary and read queries to replicas.
* Automatically reconnect clients to the new primary after failover or switchover.
* Automatically replay transactions on the new primary after failover or switchover.
* Automatically retry failed queries.
* Enforce causal reads to avoid reading stale data caused by slave lag.

## Deploying Read/Write Split Router

* [Deploy ColumnStore Object Storage Topology](https://mariadb.com/kb/en/deploy-columnstore-object-storage-topology-with-mariadb-server/)
* [Deploy ColumnStore Shared Local Storage Topology](https://mariadb.com/kb/en/columnstore-shared-local-storage/)
* [Deploy Galera Cluster Topology](https://mariadb.com/kb/en/topologies-galera-cluster/)
* [Deploy Primary/Replica Topology](https://mariadb.com/kb/en/deploy-primaryreplica-topology-with-enterprise-server/)
* Deploy Xpand Topology
* write-split-router-usageDeploy MaxScale with MariaDB Monitor and Read/Write Split Router
* [Deploy MaxScale with Galera Monitor and Read/Write Split Router](../../mariadb-maxscale-2106-maxscale-21-06-monitors/maxscale-mariadb-monitor-usage/maxscale-mariadb-monitor-usage-galera-monitor.md)

Copyright © 2025 MariaDB

{% @marketo/form formId="4316" %}
