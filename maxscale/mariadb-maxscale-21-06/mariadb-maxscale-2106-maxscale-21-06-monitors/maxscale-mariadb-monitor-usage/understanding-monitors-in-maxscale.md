
# Understanding Monitors in MaxScale


# Overview


In MariaDB MaxScale, monitors perform the following tasks:


* Deciding whether a server is up or down.
* Deciding whether a server is the primary server or a replica server.
* Performing automatic failover when the primary server fails (for certain kinds of deployments).


# Monitors Supported by MaxScale


MaxScale supports different monitors for different kinds of deployments:



| Deployment Type | Monitor |
| --- | --- |
| Deployment Type | Monitor |
| [MariaDB Replication](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/replication-cluster-multi-master/standard-replication/) | [MariaDB Monitor (mariadbmon)](maxscale-mariadb-monitor-usage-mariadb-monitor/understanding-maxscales-mariadb-monitor.md) |
| [Galera Cluster](/en/mariadb-galera-cluster-quickstart/) | [Galera Monitor (galeramon)](maxscale-mariadb-monitor-usage-galera-monitor/README.md#understanding-maxscales-galera-monitor) |
| [Multi-Node Enterprise ColumnStore](/en/mariadb-columnstore/) | [MariaDB Monitor (mariadbmon)](https://mariadb.com/kb/en/mariadb-maxscale-2208-mariadb-monitor/) |
| [ColumnStore 1.2](https://mariadb.com/kb/en/columnstore-storage-engine/) | [ColumnStore Monitor (csmon)](https://mariadb.com/kb/en/mariadb-maxscale-2208-columnstore-monitor/) |
| Xpand | [Xpand Monitor (xpandmon)](/en/mariadb-maxscale-2208-xpand-monitor/) |
| Amazon Aurora | [Aurora Monitor (auroramon)](https://mariadb.com/kb/en/mariadb-maxscale-2208-aurora-monitor/) |




Copyright © 2025 MariaDB

