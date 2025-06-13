---
layout:
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
---

# Galera Cluster

## Overview

| **Software Version**                                                                                                                  | **Diagram**                                                           | **Features**                                                                                                                                                                                                                                                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <ul><li>Enterprise Server 10.4</li><li>Enterprise Server 10.5</li><li>Enterprise Server 10.6</li><li>Enterprise Server 11.4</li></ul> | ![](../../../.gitbook/assets/es-galera-cluster-topology-no-title.png) | <p><strong>Multi-Primary Cluster Powered by Galera for Transactional/OLTP Workloads</strong></p><ul><li>InnoDB Storage Engine</li><li>Highly available</li><li>Virtually synchronous, certification-based replication</li><li>Automated provisioning of new nodes (IST/SST)</li><li>Scales reads via MaxScale</li><li>Enterprise Server 10.3+, MariaDB Enterprise Cluster (powered by Galera), MaxScale 2.5+</li></ul> |

This procedure describes the deployment of the **Galera Cluster topology** with MariaDB Enterprise Server 11.4 and MariaDB MaxScale 25.01.

MariaDB Enterprise Cluster is powered by Galera.

MariaDB Enterprise Cluster provides read scalability and fault tolerance through virtually synchronous multi-primary certification-based write-set replication (wsrep).

This procedure has 6 steps, which are executed in sequence.

MariaDB products can be deployed in many different topologies to suit specific use cases. Enterprise Cluster can be deployed on its own, or integrated with MariaDB Replication to integrate with other clusters or topologies.

This procedure represents basic product capability with 3 Enterprise Cluster nodes and 1 MaxScale node.

This page provides an overview of the topology, requirements, and deployment procedures.

Please read and understand this procedure before executing.

Procedure Steps

| Step   | Description                          |
| ------ | ------------------------------------ |
| Step 1 | Install MariaDB Enterprise Server    |
| Step 2 | Install MariaDB Enterprise Server    |
| Step 3 | Test MariaDB Enterprise Server       |
| Step 4 | Install MariaDB MaxScale             |
| Step 5 | Start and Configure MariaDB MaxScale |
| Step 6 | Test MariaDB MaxScale                |

## Support

Customers can obtain support by submitting a support case.

## Components

The following components are deployed during this procedure:

| Component                                                                                        | Function                                                                                                   |
| ------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------- |
| [MariaDB Enterprise Server](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/)                     | Modern SQL RDBMS with high availability, pluggable storage engines, hot online backups, and audit logging. |
| [MariaDB MaxScale 25.01](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/mariadb-maxscale-25-01/) | Database proxy that extends the availability, scalability, and security of MariaDB Enterprise Servers      |

### MariaDB Enterprise Server Components

| Component                                                             | Description                                                                                                                                                                                                                                                                                                                                 |
| --------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Enterprise Cluster](https://app.gitbook.com/s/rBEU9juWLfTDcdwF3Q14/) | MariaDB Enterprise Server leverages the Galera Enterprise 4 wsrep provider plugin • Provides virtually synchronous multi-primary replication for MariaDB Enterprise Server • All nodes can handle both reads and writes • Replicates write-sets to all other nodes in the cluster • Supports data-at-rest encryption of the write-set cache |
| InnoDB                                                                | • General purpose storage engine • ACID-compliant • Performance • Required for Enterprise Cluster                                                                                                                                                                                                                                           |

### MariaDB MaxScale Components

| Component               | Description                                                                                                                                                                                    |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Galera Monitor          | Tracks changes in the state of MariaDB Enterprise Servers operating as Enterprise Cluster nodes.                                                                                               |
| Listener                | Listens for client connections to MaxScale, then passes them to the router service associated with the listener                                                                                |
| Read Connection Router  | Routes connections from the listener to any available Enterprise Cluster node                                                                                                                  |
| Read/Write Split Router | Routes read operations from the listener to any available Enterprise Cluster node, and routes write operations from the listener to a specific server that MaxScale uses as the primary server |
| Server Module           | Connection configuration in MaxScale to an Enterprise Cluster node                                                                                                                             |

## Topology

<figure><img src="../../../.gitbook/assets/es-galera-cluster-topology-no-title.png" alt=""><figcaption></figcaption></figure>

MariaDB Enterprise Cluster topology provides read scalability through certification-based write-set replication (wsrep) that is multi-primary and virtually synchronous.

The Enterprise Cluster topology consists of:

* 1 or more MaxScale nodes
* 3 or more MariaDB Enterprise Servers (ES) configured as Enterprise Cluster nodes

The MaxScale nodes:

* Monitor the health and availability of each Enterprise Cluster node using the Galera Monitor (galeramon)
* Accept client and application connections
* Route queries to the Enterprise Cluster nodes using the Read Connection (readconnroute) or the Read/Write Split (readwritesplit) routers.

The Enterprise Cluster nodes:

* Receive queries from MaxScale
* Store data locally using the InnoDB storage engine
* Perform certification-based virtually synchronous replication to other Enterprise Cluster nodes
* Provide State Snapshot Transfers (SST) to bring MariaDB Enterprise Server nodes into sync with the cluster

## Requirements

These requirements are for the Galera Cluster topology when deployed with MariaDB Enterprise Server and MariaDB MaxScale 25.01.

* [Node Count](./#node-count)
* [Operating System](./#operating-system)

### Node Count

* MaxScale nodes, 1 or more are required.
* Enterprise Cluster nodes, 3 or more are required.

To avoid problems in establishing a quorum in the event of a network partition or outage, MariaDB recommends deploying an odd number of Enterprise Cluster nodes. When using multiple network switches, deploy across an odd number of switches, each with an odd number of nodes. When using multiple data centers, deploy across an odd number of data centers, each with an odd number of switches.

### Operating System

In alignment to the enterprise lifecycle, the Galera Cluster topology with MariaDB Enterprise Server and MariaDB MaxScale 25.01 is provided for:

* AlmaLinux 8 (x86\_64, ARM64)
* AlmaLinux 9 (x86\_64, ARM64)
* Debian 11 (x86\_64, ARM64)
* Debian 12 (x86\_64, ARM64)
* Red Hat Enterprise Linux 8 (x86\_64, ARM64)
* Red Hat Enterprise Linux 9 (x86\_64, PPC64LE, ARM64)
* Red Hat UBI 8 (x86\_64, ARM64)
* Rocky Linux 8 (x86\_64, ARM64)
* Rocky Linux 9 (x86\_64, ARM64)
* SUSE Linux Enterprise Server 15 (x86\_64, ARM64)
* Ubuntu 20.04 LTS (x86\_64, ARM64)
* Ubuntu 22.04 LTS (x86\_64, ARM64)
* Ubuntu 24.04 LTS (x86\_64, ARM64)

## Quick Reference

MariaDB Enterprise Server Configuration Management

| Method             | Description                                                                                                                                                           |
| ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Configuration File | Configuration files (such as /etc/my.cnf) can be used to set system-variables and options. The server must be restarted to apply changes made to configuration files. |
| Command-line       | The server can be started with command-line options that set system-variables and options.                                                                            |
| SQL                | Users can set system-variables that support dynamic changes on-the-fly using the SET statement.                                                                       |

MariaDB Enterprise Server packages are configured to read configuration files from different paths, depending on the operating system. Making custom changes to Enterprise Server default configuration files is not recommended because custom changes may be overwritten by other default configuration files that are loaded later.

To ensure that your custom changes will be read last, create a custom configuration file with the `z-` prefix in one of the include directories.

| Distribution                                                                                                 | Example Configuration File Path                |
| ------------------------------------------------------------------------------------------------------------ | ---------------------------------------------- |
| <ul><li>CentOS</li><li>Red Hat Enterprise Linux (RHEL)</li><li>SUSE Linux Enterprise Server (SLES)</li></ul> | /etc/my.cnf.d/z-custom-mariadb.cnf             |
| <ul><li>Debian</li><li>Ubuntu</li></ul>                                                                      | /etc/mysql/mariadb.conf.d/z-custom-mariadb.cnf |

## MariaDB Enterprise Server Service Management

The `systemctl` command is used to start and stop the MariaDB Enterprise Server service. The `galera_new_cluster and galera_recovery` scripts are used for Enterprise Cluster-specific operations.

| Operation                         | Command                        |
| --------------------------------- | ------------------------------ |
| Start                             | sudo systemctl start mariadb   |
| Stop                              | sudo systemctl stop mariadb    |
| Restart                           | sudo systemctl restart mariadb |
| Enable during startup             | sudo systemctl enable mariadb  |
| Disable during startup            | sudo systemctl disable mariadb |
| Status                            | sudo systemctl status mariadb  |
| Bootstrap a cluster node          | sudo galera\_new\_cluster      |
| Recover a cluster node's position | sudo galera\_recovery          |

For additional information, see "[Starting and Stopping MariaDB](../../../server-management/starting-and-stopping-mariadb/)".

## MariaDB Enterprise Server Logs

MariaDB Enterprise Server produces log data that can be helpful in problem diagnosis.

Log filenames and locations may be overridden in the server configuration. The default location of logs is the data directory. The data directory is specified by the datadir system variable.

| Log                                                                                         | System Variable/Option                                                                                                                                    | Default Filename      |
| ------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------- |
| [MariaDB Error Log](../../../server-management/server-monitoring-logs/error-log.md)         | [log\_error](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#list-of-server-system-variables)             | `<hostname>.err`      |
| [MariaDB Enterprise Audit Log](../../../reference/plugins/mariadb-enterprise-audit.md)      | [server\_audit\_file\_path](../../../reference/plugins/mariadb-audit-plugin/mariadb-audit-plugin-options-and-system-variables.md#server_audit_file_path)  | `server_audit.log`    |
| [Slow Query Log](../../../server-management/server-monitoring-logs/slow-query-log/)         | [slow\_query\_log\_file](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#list-of-server-system-variables) | `<hostname>-slow.log` |
| [General Query Log](../../../server-management/server-monitoring-logs/general-query-log.md) | [general\_log\_file](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#list-of-server-system-variables)     | `<hostname>.log`      |
| [Binary Log](../../../server-management/server-monitoring-logs/binary-log/)                 | [log\_bin](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#log_bin)                                       | `<hostname>-bin`      |

## MaxScale Configuration Management

MaxScale can be configured using several methods. These methods make use of MaxScale's [REST API](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/administrative-tools-for-mariadb-maxscale/administrative-tools-for-mariadb-maxscale-rest-api/).

| Method                                                                                                                                                   | Benefits                                                                                                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [MaxCtrl](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/administrative-tools-for-mariadb-maxscale/administrative-tools-for-mariadb-maxscale-maxctrl/)   | Command-line utility to perform administrative tasks through the REST API. See MaxCtrl Commands.                                                                                                        |
| [MaxGUI](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/administrative-tools-for-mariadb-maxscale/maxgui/)                                               | MaxGUI is a graphical utility that can perform administrative tasks through the REST API.                                                                                                               |
| [REST API](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/administrative-tools-for-mariadb-maxscale/administrative-tools-for-mariadb-maxscale-rest-api/) | The REST API can be used directly. For example, the curl utility could be used to make REST API calls from the command-line. Many programming languages also have libraries to interact with REST APIs. |

The procedure on these pages configures MaxScale using MaxCtrl.

## MaxScale Service Management

The systemctl command is used to start and stop the MaxScale service.>

| Operation              | Command                         |
| ---------------------- | ------------------------------- |
| Start                  | sudo systemctl start maxscale   |
| Stop                   | sudo systemctl stop maxscale    |
| Restart                | sudo systemctl restart maxscale |
| Enable during startup  | sudo systemctl enable maxscale  |
| Disable during startup | sudo systemctl disable maxscale |
| Status                 | sudo systemctl status maxscale  |

For additional information, see "[Starting and Stopping MariaDB](../../../server-management/starting-and-stopping-mariadb/)".

## Next Step

Navigation in the procedure "Deploy Galera Cluster Topology":

Next: Step 1: Install MariaDB Enterprise Server

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>\
\
