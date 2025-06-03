# Topologies

MariaDB products can be deployed in many different topologies. The topologies described in this section are representative. MariaDB products can be deployed to form other topologies, leverage advanced product capabilities, or combine the capabilities of multiple topologies.

Topologies are the arrangement of nodes and links to achieve a purpose. This documentation describes a few of the many topologies that can be deployed using MariaDB database products.

We group topologies by workload (transactional, analytical, hybrid) and technologies (Enterprise Spider). Single-node topologies are listed separately.

To help you select the correct topology:

* Each topology is named and this name is used consistently throughout the documentation.
* A thumbnail diagram provides a small-scale summary of the topology's architecture.
* Finally, we provide a list of the benefits of the topology.

Although multiple topologies are listed on this page, the listed topologies are not the only options. MariaDB products are flexible, configurable, and extensible, so it possible to deploy different topologies that combine the capabilities of multiple topologies listed on this page. The topologies listed on this page are primarily intended to be representative of the most commonly requested use cases.

## Transactional (OLTP)

<table><thead><tr><th valign="top">Topology</th><th>Diagram</th><th>Features</th></tr></thead><tbody><tr><td valign="top">Primary/Replica Topology</td><td><img src="../../.gitbook/assets/es-primary-replica-topology-no-title.png" alt=""></td><td><p><strong>MariaDB Replication</strong></p><ul><li>Highly available</li><li>Asynchronous or semi-synchronous replication</li><li>Automatic failover via MaxScale</li><li>Manual provisioning of new nodes from backup</li><li>Scales reads via MaxScale</li><li>Enterprise Server 10.3+, MaxScale 2.5+</li></ul></td></tr><tr><td valign="top"><a href="galera-cluster/">Galera Cluster Topology</a></td><td><img src="../../.gitbook/assets/es-galera-cluster-topology-no-title.png" alt=""></td><td><p><strong>Galera Cluster Topology Multi-Primary Cluster Powered by Galera for Transactional/OLTP Workloads</strong></p><ul><li>InnoDB Storage Engine</li><li>Highly available</li><li>Virtually synchronous, certification-based replication</li><li>Automated provisioning of new nodes (IST/SST)</li><li>Scales reads via MaxScale Enterprise Server 10.3+, MariaDB Enterprise Cluster (powered by Galera), MaxScale 2.5+</li></ul></td></tr></tbody></table>

### Analytical (OLAP, Data Warehousing, DSS)

<table><thead><tr><th valign="top">Topology</th><th>Diagram</th><th>Features</th></tr></thead><tbody><tr><td valign="top"><a href="columnstore-object-storage/">ColumnStore Object Storage Topology</a></td><td><img src="../../.gitbook/assets/es-columnstore-topology-s3-no-title.png" alt=""></td><td><p><strong>Columnar storage engine with S3-compatible object storage</strong></p><ul><li>Highly available</li><li>Automatic failover via MaxScale and CMAPI</li><li>Scales reads via MaxScale</li><li>Bulk data import</li><li>Enterprise Server 10.5, Enterprise ColumnStore 5, MaxScale 2.5</li><li>Enterprise Server 10.6, Enterprise ColumnStore 23.02, MaxScale 22.08</li></ul></td></tr><tr><td valign="top"><a href="columnstore-shared-local-storage/">ColumnStore Shared Local Storage Topology</a></td><td><img src="../../.gitbook/assets/es-columnstore-topology-nfs-no-title.png" alt=""></td><td><p><strong>Columnar storage engine with shared local storage</strong></p><ul><li>Highly available</li><li>Automatic failover via MaxScale and CMAPI</li><li>Scales reads via MaxScale</li><li>Bulk data import</li><li>Enterprise Server 10.5, Enterprise ColumnStore 5, MaxScale 2.5</li><li>Enterprise Server 10.6, Enterprise ColumnStore 23.02, MaxScale 22.08</li></ul></td></tr></tbody></table>

## Hybrid Workloads

<table><thead><tr><th valign="top">Topology</th><th>Diagram</th><th>Features</th></tr></thead><tbody><tr><td valign="top"><a href="htap/">HTAP Topology</a></td><td><img src="../../.gitbook/assets/es-columnstore-htap-topology-s3-no-title.png" alt=""></td><td><ul><li>Single-stack hybrid transactional/analytical workloads</li><li>ColumnStore for analytics with scalable S3-compatible object storage</li><li>InnoDB for transactions• Cross-engine JOINs</li><li>Enterprise Server 10.5, Enterprise ColumnStore 5, MaxScale 2.5</li><li>Enterprise Server 10.6, Enterprise ColumnStore 23.02, MaxScale 22.08</li></ul></td></tr></tbody></table>

## Spider Topologies

<table><thead><tr><th valign="top">Topology</th><th>Diagram</th><th>Features</th></tr></thead><tbody><tr><td valign="top">Spider Federated Topology</td><td><img src="../../.gitbook/assets/es-spider-federated-mariadb-topology-no-title.png" alt=""></td><td><ul><li>Read from and write to tables on remote ES nodes</li><li>Spider Node uses Spider storage engine for Federated Spider Tables</li><li>Federated Spider Table is a "virtual" table• Spider uses MariaDB foreign data wrapper to query Data Table on Data Node</li><li>Data Node uses non-Spider storage engine for Data Tables</li><li>Supports transactions</li><li>Enterprise Server 10.3+, Enterprise Spider</li></ul></td></tr><tr><td valign="top">Spider Sharded Topology</td><td><img src="../../.gitbook/assets/es-spider-sharded-mariadb-topology-no-title.png" alt=""></td><td><ul><li>Shard tables for horizontal scalability</li><li>Spider Node uses Spider storage engine for Sharded Spider Tables</li><li>Sharded Spider Table is a partitioned "virtual" table</li><li>Spider uses MariaDB foreign data wrapper to query Data Tables on Data Nodes for each partition</li><li>Data Node uses non-Spider storage engine for Data Tables</li><li>Supports transactions</li><li>Enterprise Server 10.3+, Enterprise Spider</li></ul></td></tr></tbody></table>

Copyright © 2025 MariaDB
