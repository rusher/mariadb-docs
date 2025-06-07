# Spider Storage Engine Overview

## Overview

MariaDB Enterprise Spider is a storage engine for MariaDB Enterprise Server that supports table federation, table sharding, and ODBC data sources.

MariaDB Enterprise Spider creates "virtual" Spider Tables on a Spider Node that clients and applications can query as if they were regular tables. For Federated Spider Tables and Sharded Spider Tables, the Enterprise Spider storage engine uses a MariaDB foreign data wrapper to query a Data Table on one or more Data Nodes. For ODBC Spider Tables, the Enterprise Spider storage engine uses an ODBC foreign data wrapper to query an ODBC Data Source.

## Benefits

MariaDB Enterprise Spider:

* Supports a MariaDB foreign data wrapper. The MariaDB foreign data wrapper can be used to replace the older Federated and FederatedX storage engines.
* Supports an ODBC foreign data wrapper in MariaDB Enterprise Server 10.5 and later. ODBC foreign data wrapper is beta maturity.

The maturity can be confirmed by querying the [information\_schema.SPIDER\_WRAPPER\_PROTOCOLS](../../../../reference/storage-engines/spider/information-schema-spider_wrapper_protocols-table.md) table.

| ES Versions | Spider Version                |
| ----------- | ----------------------------- |
| ES Versions | Spider Version                |
| ES 10.5     | MariaDB Enterprise Spider 3.4 |

## Available Platforms

* AlmaLinux 8 (x86\_64, ARM64)
* AlmaLinux 9 (x86\_64, ARM64)
* CentOS Linux 7 (x86\_64)
* CentOS Linux 8 (x86\_64, ARM64)
* Debian 9 (x86\_64, ARM64)
* Debian 10 (x86\_64, ARM64)
* Debian 11 (x86\_64, ARM64)
* Debian 12 (x86\_64, ARM64)
* Microsoft Windows (x86\_64)
* Red Hat Enterprise Linux 7 (x86\_64)
* Red Hat Enterprise Linux 8 (x86\_64, ARM64)
* Red Hat UBI 8 (x86\_64, ARM64)
* Rocky Linux 8 (x86\_64, packages, Red, Linux, Hat, Enterprise, ARM64, 8)
* SUSE Linux Enterprise Server 12 (x86\_64, ARM64)
* SUSE Linux Enterprise Server 15 (x86\_64, ARM64)
* Ubuntu 18.04 LTS (x86\_64, ARM64)
* Ubuntu 20.04 LTS (x86\_64, ARM64)
* Ubuntu 22.04 LTS (x86\_64, ARM64)
* Ubuntu 24.04 LTS (x86\_64, ARM64)

## Topologies

MariaDB Enterprise Spider supports multiple topologies. Several options are described below. MariaDB Enterprise Spider can be deployed in other topologies. The topologies on this page are representative of basic product capabilities.

For additional information, choose an Enterprise Spider topology:

| Topology                                                                                                                                                                   | Diagram                                                                                                                   | Use Cases                                                                                                                                                                                                         |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Topology                                                                                                                                                                   | Diagram                                                                                                                   | Use Cases                                                                                                                                                                                                         |
| [Spider Federated](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/maxscale-architecture/mariadb-enterprise-spider-topologies/federated-mariadb-enterprise-spider-topology) | ![spider-federated](../../../../.gitbook/assets/spider-storage-engine-introduction/+image/spider-federated.png)           | Read from and write to tables on remote ES nodes Migrate tables from remote ES node Query tables on remote ES node JOIN local tables with tables on remote ES node                                                |
| [Spider Sharded](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/maxscale-architecture/mariadb-enterprise-spider-topologies/sharded-mariadb-enterprise-spider-topology)     | ![spider-sharded](../../../../.gitbook/assets/spider-storage-engine-introduction/+image/spider-sharded.png)               | Shard tables for horizontal scalability Consolidate tables from remote ES nodes into one "virtual" table Partition a large table across multiple remote ES nodes Use regular partitioning syntax to define shards |
| [Spider ODBC](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/maxscale-architecture/mariadb-enterprise-spider-topologies/odbc-mariadb-enterprise-spider-topology)           | ![spider-federated-odbc](../../../../.gitbook/assets/spider-storage-engine-introduction/+image/spider-federated-odbc.png) | Read from and write to tables on ODBC Data Sources Migrate data from an ODBC Data Source Query data from an ODBC Data Source JOIN local tables with data from an ODBC Data Source ES 10.5+                        |

## Deployment Instructions

To deploy the Enterprise Spider storage engine with MariaDB Enterprise Server, choose an Enterprise Spider topology and an ES version:

| Topology                                                                                                                                                                                                                                                                                                        | Diagram                                                                                                         | Use Cases                                                                                                                                                                                                                                                                                                                                                        |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Topology                                                                                                                                                                                                                                                                                                        | Diagram                                                                                                         | Use Cases                                                                                                                                                                                                                                                                                                                                                        |
| [Enterprise Server 10.5](../../../../../en/mariadb-server-releases-mariadb-enterprise-server-10-5/) [Enterprise Server 10.6](https://mariadb.com/kb/en/mariadb-server-releases-mariadb-enterprise-server-10-6/) [Enterprise Server 11.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/enterprise-server/11-4) | ![spider-federated](../../../../.gitbook/assets/spider-storage-engine-introduction/+image/spider-federated.png) | _Read from and write to tables on remote ES nodes_ Spider Node uses Spider storage engine for Federated Spider Tables Federated Spider Table is a "virtual" table Spider uses MariaDB foreign data wrapper to query Data Table on Data Node Data Node uses non-Spider storage engine for Data Tables Supports transactions, Enterprise Spider                    |
| [Enterprise Server 10.5](../../../../../en/mariadb-server-releases-mariadb-enterprise-server-10-5/) [Enterprise Server 10.6](../../../../../en/mariadb-server-releases-mariadb-enterprise-server-10-6/) [Enterprise Server 11.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/enterprise-server/11-4)         | ![spider-sharded](../../../../.gitbook/assets/spider-storage-engine-introduction/+image/spider-sharded.png)     | _Shard tables for horizontal scalability_ Spider Node uses Spider storage engine for Sharded Spider Tables Sharded Spider Table is a partitioned "virtual" table Spider uses MariaDB foreign data wrapper to query Data Tables on Data Nodes for each partition Data Node uses non-Spider storage engine for Data Tables Supports transactions Enterprise Spider |

## Term Definitions

| Term                | Definition                                                                                                                                                                                                                                                                                                                                                                                        |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Term                | Definition                                                                                                                                                                                                                                                                                                                                                                                        |
| Data Node           | A Data Node is a MariaDB Enterprise Server node that contains one or more Data Tables.                                                                                                                                                                                                                                                                                                            |
| Data Table          | A Data Table stores data for a Spider Table. When a Spider Table is queried, the Enterprise Spider storage engine uses the MariaDB foreign data wrapper to read from and write to the Data Table on a Data Node. The Data Table must be created on the Data Node with the same structure as the Spider Table. The Data Table must use a non-Spider storage engine, such as InnoDB or ColumnStore. |
| ODBC Data Source    | An ODBC Data Source relies on an ODBC Driver and an ODBC Driver Manager to query an external data source.                                                                                                                                                                                                                                                                                         |
| ODBC Driver         | An ODBC Driver is a library that integrates with a ODBC Driver Manager to query an external data source.                                                                                                                                                                                                                                                                                          |
| ODBC Driver Manager | An ODBC Driver Manager allows applications to use ODBC Drivers.                                                                                                                                                                                                                                                                                                                                   |
| Spider Node         | A Spider Node is a MariaDB Enterprise Server node that contains one or more Spider Tables.                                                                                                                                                                                                                                                                                                        |
| Spider Table        | A Spider Table is a virtual table that does not store data. When a Spider Table is queried, the Enterprise Spider storage engine uses foreign data wrappers to read from and write to Data Tables on Data Nodes or ODBC Data Sources.                                                                                                                                                             |

## Resources

### ES Information Schema Reference

* [SPIDER\_ALLOC\_MEM](../../../../reference/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-spider_alloc_mem-table.md)
* [SPIDER\_WRAPPER\_PROTOCOLS](../../../../reference/storage-engines/spider/information-schema-spider_wrapper_protocols-table.md)

### ES Plugin Reference

* [SPIDER](../../../../reference/storage-engines/spider/)

### ES SQL Statement Reference

* [ALTER SERVER](../../../../reference/sql-statements/data-definition/alter/alter-server.md)
* [CREATE SERVER](../../../../reference/sql-statements/data-definition/create/create-server.md)
* [DROP SERVER](../../../../reference/sql-statements/data-definition/drop/drop-server.md)

### ES System Table Reference

* spider\_link\_failed\_log
* spider\_link\_mon\_servers
* spider\_table\_crd
* spider\_table\_position\_for\_recovery
* spider\_tables
* spider\_table\_sts
* spider\_xa\_failed\_log
* spider\_xa\_member
* spider\_xa
