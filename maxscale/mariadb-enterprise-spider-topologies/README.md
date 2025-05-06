
# MariaDB Enterprise Spider Topologies


# Overview


MariaDB Enterprise Spider supports multiple topologies. Several options are described below. MariaDB Enterprise Spider can be deployed in other topologies. The topologies on this page are representative of basic product capabilities.


For additional information, choose an Enterprise Spider topology:



| Topology | Diagram | Use Cases |
| --- | --- | --- |
| Topology | Diagram | Use Cases |
| Spider Federated | ![spider-federated](../.gitbook/assets/mariadb-enterprise-spider-topologies/+image/spider-federated.png "spider-federated") | • Read from and write to tables on remote ES nodes • Migrate tables from remote ES node • Query tables on remote ES node • JOIN local tables with tables on remote ES node • ES 10.3+ |
| Spider Sharded | ![spider-sharded](../.gitbook/assets/mariadb-enterprise-spider-topologies/+image/spider-sharded.png "spider-sharded") | • Shard tables for horizontal scalability • Consolidate tables from remote ES nodes into one "virtual" table • Partition a large table across multiple remote ES nodes • Use regular partitioning syntax to define shards • ES 10.3+ |
| Spider ODBC | ![spider-federated-odbc](../.gitbook/assets/mariadb-enterprise-spider-topologies/+image/spider-federated-odbc.png "spider-federated-odbc") | • Read from and write to tables on ODBC Data Sources • Migrate data from an ODBC Data Source • Query data from an ODBC Data Source • JOIN local tables with data from an ODBC Data Source • ES 10.5+ |


