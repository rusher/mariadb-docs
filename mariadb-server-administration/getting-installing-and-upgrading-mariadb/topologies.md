---
description: A page imported from the MariaDB Enterprise documentation.
---

# Topologies

### Overview <a href="#overview_h2" id="overview_h2"></a>

Procedures are provided to download, install, set-up, configure, and test MariaDB products.

[Upgrade](https://mariadb.com/docs/server/service-management/upgrades/) instructions are also available.

MariaDB products can be deployed in many different topologies. The topologies on this page are representative. MariaDB products can be deployed to form other topologies, leverage advanced product capabilities, or combine the capabilities of multiple topologies.

### Transactional (OLTP)

| Topology                                                                                                                    | **Diagram**                                                                                                                                                                         | **Features**                                                                                                                                                                                                                                                                                                                                                                                                             |
| --------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| <ul><li><a href="https://mariadb.com/docs/server/deploy/topologies/primary-replica/">Primary/Replica Topology</a></li></ul> | [![Primary/Replica Topology](https://mariadb.com/docs/_images/es-primary-replica-topology-no-title.png)](https://mariadb.com/docs/_images/es-primary-replica-topology-no-title.png) | <ul><li><strong>MariaDB Replication</strong></li><li>Highly available</li><li>Asynchronous or semi-synchronous replication</li><li>Automatic failover via MaxScale</li><li>Manual provisioning of new nodes from backup</li><li>Scales reads via MaxScale</li><li>Enterprise Server 10.3+, MaxScale 2.5+</li></ul>                                                                                                       |
| <ul><li><a href="https://mariadb.com/docs/server/deploy/topologies/galera-cluster/">Galera Cluster Topology</a></li></ul>   | [![Galera Cluster Topology](https://mariadb.com/docs/_images/es-galera-cluster-topology-no-title.png)](https://mariadb.com/docs/_images/es-galera-cluster-topology-no-title.png)    | <ul><li><strong>Multi-Primary Cluster Powered by Galera for Transactional/OLTP Workloads</strong></li><li>InnoDB Storage Engine</li><li>Highly available</li><li>Virtually synchronous, certification-based replication</li><li>Automated provisioning of new nodes (IST/SST)</li><li>Scales reads via MaxScale</li><li>Enterprise Server 10.3+, MariaDB Enterprise Cluster (powered by Galera), MaxScale 2.5+</li></ul> |

### Analytical (OLAP, Data Warehousing, DSS)

| Topology                                                                                                                                                      | **Diagram**                                                                                                                                                                                          | **Features**                                                                                                                                                                                                                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <ul><li><a href="https://mariadb.com/docs/server/deploy/topologies/columnstore-object-storage/">ColumnStore Object Storage Topology</a></li></ul>             | [![ColumnStore Object Storage Topology](https://mariadb.com/docs/_images/es-columnstore-topology-s3-no-title.png)](https://mariadb.com/docs/_images/es-columnstore-topology-s3-no-title.png)         | <ul><li><strong>Columnar storage engine with S3-compatible object storage</strong></li><li>Highly available</li><li>Automatic failover via MaxScale and CMAPI</li><li>Scales reads via MaxScale</li><li>Bulk data import</li><li>Enterprise Server 10.5, Enterprise ColumnStore 5, MaxScale 2.5</li><li>Enterprise Server 10.6, Enterprise ColumnStore 23.02, MaxScale 22.08</li></ul> |
| <ul><li><a href="https://mariadb.com/docs/server/deploy/topologies/columnstore-shared-local-storage/">ColumnStore Shared Local Storage Topology</a></li></ul> | [![ColumnStore Shared Local Storage Topology](https://mariadb.com/docs/_images/es-columnstore-topology-nfs-no-title.png)](https://mariadb.com/docs/_images/es-columnstore-topology-nfs-no-title.png) | <ul><li><strong>Columnar storage engine with shared local storage</strong></li><li>Highly available</li><li>Automatic failover via MaxScale and CMAPI</li><li>Scales reads via MaxScale</li><li>Bulk data import</li><li>Enterprise Server 10.5, Enterprise ColumnStore 5, MaxScale 2.5</li><li>Enterprise Server 10.6, Enterprise ColumnStore 23.02, MaxScale 22.08</li></ul>         |

### Hybrid Workloads

| Topology                                                                                                          | **Diagram**                                                                                                                                                                      | **Features**                                                                                                                                                                                                                                                                                                                                                                          |
| ----------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <ul><li><a href="https://mariadb.com/docs/server/deploy/topologies/columnstore-htap/">HTAP Topology</a></li></ul> | [![HTAP Topology](https://mariadb.com/docs/_images/es-columnstore-htap-topology-s3-no-title.png)](https://mariadb.com/docs/_images/es-columnstore-htap-topology-s3-no-title.png) | <ul><li><strong>Single-stack hybrid transactional/analytical workloads</strong></li><li>ColumnStore for analytics with scalable S3-compatible object storage</li><li>InnoDB for transactions</li><li>Cross-engine JOINs</li><li>Enterprise Server 10.5, Enterprise ColumnStore 5, MaxScale 2.5</li><li>Enterprise Server 10.6, Enterprise ColumnStore 23.02, MaxScale 22.08</li></ul> |

### Spider Topologies

| Topology                                                                                                                      | **Diagram**                                                                                                                                                                                            | **Features**                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ----------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <ul><li><a href="https://mariadb.com/docs/server/deploy/topologies/spider-federated/">Spider Federated Topology</a></li></ul> | [![Spider Federated Topology](https://mariadb.com/docs/_images/es-spider-federated-mariadb-topology-no-title.png)](https://mariadb.com/docs/_images/es-spider-federated-mariadb-topology-no-title.png) | <ul><li><strong>Read from and write to tables on remote ES nodes</strong></li><li>Spider Node uses Spider storage engine for Federated Spider Tables</li><li>Federated Spider Table is a "virtual" table</li><li>Spider uses MariaDB foreign data wrapper to query Data Table on Data Node</li><li>Data Node uses non-Spider storage engine for Data Tables</li><li>Supports transactions</li><li>Enterprise Server 10.3+, Enterprise Spider</li></ul>                     |
| <ul><li><a href="https://mariadb.com/docs/server/deploy/topologies/spider-sharded/">Spider Sharded Topology</a></li></ul>     | [![Spider Sharded Topology](https://mariadb.com/docs/_images/es-spider-sharded-mariadb-topology-no-title.png)](https://mariadb.com/docs/_images/es-spider-sharded-mariadb-topology-no-title.png)       | <ul><li><strong>Shard tables for horizontal scalability</strong></li><li>Spider Node uses Spider storage engine for Sharded Spider Tables</li><li>Sharded Spider Table is a partitioned "virtual" table</li><li>Spider uses MariaDB foreign data wrapper to query Data Tables on Data Nodes for each partition</li><li>Data Node uses non-Spider storage engine for Data Tables</li><li>Supports transactions</li><li>Enterprise Server 10.3+, Enterprise Spider</li></ul> |

### Single Node Topologies

#### MariaDB Community Server

* [MariaDB Community Server 10.5](https://mariadb.com/docs/server/deploy/topologies/single-node/community-server-10-5/)
* [MariaDB Community Server 10.6](https://mariadb.com/docs/server/deploy/topologies/single-node/community-server-10-6/)

#### MariaDB Community Server with ColumnStore

* [MariaDB Community Server with ColumnStore 5](https://mariadb.com/docs/server/deploy/topologies/single-node/community-columnstore-cs10-5/)
* [MariaDB Community Server with ColumnStore 6](https://mariadb.com/docs/server/deploy/topologies/single-node/community-columnstore-cs10-6/)

#### MariaDB Enterprise ColumnStore with Local Storage

* [MariaDB Enterprise ColumnStore 5 with Local Storage](https://mariadb.com/docs/server/deploy/topologies/single-node/enterprise-columnstore-es10-5-local/)
* [MariaDB Enterprise ColumnStore 22.08 with Local Storage](https://mariadb.com/docs/server/deploy/topologies/single-node/enterprise-columnstore-es10-6-local/)
* [MariaDB Enterprise ColumnStore 23.10 with Local Storage](https://mariadb.com/docs/server/deploy/topologies/single-node/enterprise-columnstore-es11-4-local/)

For high availability and scalability, instead see "[ColumnStore Shared Local Storage Topology](https://mariadb.com/docs/server/deploy/topologies/columnstore-shared-local-storage/)".

#### MariaDB Enterprise ColumnStore with Object Storage

* [MariaDB Enterprise ColumnStore 5 with Object Storage](https://mariadb.com/docs/server/deploy/topologies/single-node/enterprise-columnstore-es10-5-object/)
* [MariaDB Enterprise ColumnStore 22.08 with Object Storage](https://mariadb.com/docs/server/deploy/topologies/single-node/enterprise-columnstore-es10-6-object/)
* [MariaDB Enterprise ColumnStore 23.10 with Object Storage](https://mariadb.com/docs/server/deploy/topologies/single-node/enterprise-columnstore-es11-4-object/)

For high availability and scalability, instead see "[ColumnStore Object Storage Topology](https://mariadb.com/docs/server/deploy/topologies/columnstore-object-storage/)".

#### MariaDB Enterprise Server

* [MariaDB Enterprise Server 10.2](https://mariadb.com/docs/server/deploy/topologies/single-node/enterprise-server-10-2/)
* [MariaDB Enterprise Server 10.3](https://mariadb.com/docs/server/deploy/topologies/single-node/enterprise-server-10-3/)
* [MariaDB Enterprise Server 10.4](https://mariadb.com/docs/server/deploy/topologies/single-node/enterprise-server-10-4/)
* [MariaDB Enterprise Server 10.5](https://mariadb.com/docs/server/deploy/topologies/single-node/enterprise-server-10-5/)
* [MariaDB Enterprise Server 10.6](https://mariadb.com/docs/server/deploy/topologies/single-node/enterprise-server-10-6/)
* [MariaDB Enterprise Server 11.4](https://mariadb.com/docs/server/deploy/topologies/single-node/enterprise-server-11-4/)

### Deployment Practices

* [Best Practices](https://mariadb.com/docs/server/deploy/best-practices/)
* [Customer Download Token](https://mariadb.com/docs/server/deploy/token/)
* [Supply Chain Security](https://mariadb.com/docs/server/security/supply-chain/#Validating_Sums_and_Signatures)

### Deployment Methods

* [Deploy from Binary Tarball](https://mariadb.com/docs/server/deploy/deployment-methods/bintar/)
* [Deploy from Package Tarball](https://mariadb.com/docs/server/deploy/deployment-methods/package-tarball/)
* [Deploy from Repository (APT, YUM, ZYpp)](https://mariadb.com/docs/server/deploy/deployment-methods/repo/)
* [Deploy from Repository Mirror](https://mariadb.com/docs/server/deploy/deployment-methods/repo-mirror/)
* [Deploy with Docker](https://mariadb.com/docs/server/deploy/deployment-methods/docker/)
* [Deploy in the cloud on MariaDB SkySQL DBaaS](https://mariadb.com/docs/server/deploy/deployment-methods/skysql/)

### Support

* [Obtaining support from MariaDB Corporation](https://mariadb.com/docs/server/support/)
* [Compatibility](https://mariadb.com/docs/server/deploy/compatibility/)
