# Understanding MaxScale's Read/Write Split Router

MaxScale's [Read/Write Split Router (readwritesplit)](../../reference/maxscale-routers/maxscale-readwritesplit.md) performs query-based load balancing. For each client connected to MaxScale, it opens up connections to multiple back-end database servers. When the client sends a write query to MaxScale, it routes the query to the connection opened with the primary server. When the client sends a read query to MaxScale, it routes the query to a connection opened with one of the replicas.

## What Does the Read/Write Split Router Support?

The [Read/Write Split Router (readwritesplit)](../../reference/maxscale-routers/maxscale-readwritesplit.md) supports:

* [MariaDB replication](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication) deployments
* [Galera Cluster](https://github.com/mariadb-corporation/docs-server/blob/test/en/mariadb-galera-cluster-quickstart/README.md) deployments
* [Multi-Node Enterprise ColumnStore](https://github.com/mariadb-corporation/docs-server/blob/test/en/mariadb-columnstore/README.md) deployments

## When to Use the Read/Write Split Router?

The [Read/Write Split Router (readwritesplit)](../../reference/maxscale-routers/maxscale-readwritesplit.md) allows you to:

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

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
