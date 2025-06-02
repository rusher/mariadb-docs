# Deploy ColumnStore Shared Local Storage Topology

## Overview

This procedure describes the deployment of the ColumnStore Shared Local Storage topology with MariaDB Enterprise Server 10.5, MariaDB Enterprise ColumnStore 5, and MariaDB MaxScale 2.5.

MariaDB Enterprise ColumnStore 5 is a columnar storage engine for MariaDB Enterprise Server 10.5. Enterprise ColumnStore is suitable for Online Analytical Processing (OLAP) workloads.

This procedure has 9 steps, which are executed in sequence.

This procedure represents basic product capability and deploys 3 Enterprise ColumnStore nodes and 1 MaxScale node.

This page provides an overview of the topology, requirements, and deployment procedures.

Please read and understand this procedure before executing.

## Procedure Steps

| Step   | Description                                   |
| ------ | --------------------------------------------- |
| Step 1 | Prepare ColumnStore Nodes                     |
| Step 2 | Configure Shared Local Storage                |
| Step 3 | Install MariaDB Enterprise Server             |
| Step 4 | Start and Configure MariaDB Enterprise Server |
| Step 5 | Test MariaDB Enterprise Server                |
| Step 6 | Install MariaDB MaxScale                      |
| Step 7 | Start and Configure MariaDB MaxScale          |
| Step 8 | Test MariaDB MaxScale                         |
| Step 9 | Import Data                                   |

## Support

Customers can obtain support by submitting a support case.

## Components

The following components are deployed during this procedure:

| Component                                                                    | Function                                                                                                   |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| Component                                                                    | Function                                                                                                   |
| [MariaDB Enterprise Server](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/) | Modern SQL RDBMS with high availability, pluggable storage engines, hot online backups, and audit logging. |
| [MariaDB MaxScale](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/)          | Database proxy that extends the availability, scalability, and security of MariaDB Enterprise Servers      |

## MariaDB Enterprise Server Components

| Component                                                                         | Description                                                                                                                                                                                                               |
| --------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Component                                                                         | Description                                                                                                                                                                                                               |
| [MariaDB Enterprise ColumnStore](https://app.gitbook.com/s/rBEU9juWLfTDcdwF3Q14/) | • Columnar storage engine • Highly available • Optimized for Online Analytical Processing (OLAP) workloads • Scalable query execution • Cluster Management API (CMAPI) provides a REST API for multi-node administration. |

## MariaDB MaxScale Components

| Component               | Description                                                                                                                                                                                        |
| ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Component               | Description                                                                                                                                                                                        |
| Listener                | Listens for client connections to MaxScale then passes them to the router service                                                                                                                  |
| MariaDB Monitor         | Tracks changes in the state of MariaDB Enterprise Servers.                                                                                                                                         |
| Read Connection Router  | Routes connections from the listener to any available Enterprise ColumnStore node                                                                                                                  |
| Read/Write Split Router | Routes read operations from the listener to any available Enterprise ColumnStore node, and routes write operations from the listener to a specific server that MaxScale uses as the primary server |
| Server Module           | Connection configuration in MaxScale to an Enterprise ColumnStore node                                                                                                                             |

## Topology

The MariaDB Enterprise ColumnStore topology with Object Storage delivers production analytics with high availability, fault tolerance, and limitless data storage by leveraging S3-compatible storage.

The topology consists of:

* One or more MaxScale nodes
* An odd number of ColumnStore nodes (minimum of 3) running ES, Enterprise ColumnStore, and CMAPI

The MaxScale nodes:

* Monitor the health and availability of each ColumnStore node using the MariaDB Monitor (mariadbmon)
* Accept client and application connections
* Route queries to ColumnStore nodes using the Read/Write Split Router (readwritesplit)

The ColumnStore nodes:

* Receive queries from MaxScale
* Execute queries
  * Use [shared local storage](https://app.gitbook.com/s/rBEU9juWLfTDcdwF3Q14/architecture/columnstore-storage-architecture#shared-local-storage) for the [Storage Manager directory](https://app.gitbook.com/s/rBEU9juWLfTDcdwF3Q14/architecture/columnstore-storage-architecture#storage-manager-directory)

## Requirements

These requirements are for the ColumnStore Object Storage topology when deployed with MariaDB Enterprise Server 10.5, MariaDB Enterprise ColumnStore 5, and MariaDB MaxScale 2.5.

* Node Count
* Operating System
* Minimum Hardware Requirements
* Recommended Hardware Requirements
* Storage Requirements
* S3-Compatible Object Storage Requirements
* Preferred Object Storage Providers: Cloud
* Preferred Object Storage Providers: Hardware
* Shared Local Storage Directories
* Shared Local Storage Options
* Recommended Storage Options

## Node Count

* MaxScale nodes, 1 or more are required.
* Enterprise ColumnStore nodes, 3 or more are required for high availability. You should always have an odd number of nodes in a multi-node ColumnStore deployment to avoid split brain scenarios.

## Operating System

In alignment to the enterprise lifecycle, the ColumnStore Object Storage topology with MariaDB Enterprise Server 10.5, MariaDB Enterprise ColumnStore 5, and MariaDB MaxScale 2.5 is provided for:

* CentOS Linux 7 (x86\_64)
* Debian 10 (x86\_64)
* Red Hat Enterprise Linux 7 (x86\_64)
* Red Hat Enterprise Linux 8 (x86\_64)
* Ubuntu 18.04 LTS (x86\_64)
* Ubuntu 20.04 LTS (x86\_64)

## Minimum Hardware Requirements

MariaDB Enterprise ColumnStore's minimum hardware requirements are not intended for production environments, but the minimum hardware requirements can be appropriate for development and test environments. For production environments, see the recommended hardware requirements instead.

The minimum hardware requirements are:

| Component                   | CPU      | Memory |
| --------------------------- | -------- | ------ |
| Component                   | CPU      | Memory |
| MaxScale node               | 4+ cores | 4+ GB  |
| Enterprise ColumnStore node | 4+ cores | 4+ GB  |

MariaDB Enterprise ColumnStore will refuse to start if the system has less than 3 GB of memory.

If Enterprise ColumnStore is started on a system with less memory, the following error message will be written to the ColumnStore system log called crit.log:

```
Apr 30 21:54:35 a1ebc96a2519 PrimProc[1004]: 35.668435 |0|0|0| C 28 CAL0000: Error total memory available is less than 3GB.
```

And the following error message will be raised to the client:

```
ERROR 1815 (HY000): Internal error: System is not ready yet. Please try again.
```

## Recommended Hardware Requirements

MariaDB Enterprise ColumnStore's recommended hardware requirements are intended for production analytics.

The recommended hardware requirements are:

| Component                   | CPU       | Memory  |
| --------------------------- | --------- | ------- |
| Component                   | CPU       | Memory  |
| MaxScale node               | 8+ cores  | 16+ GB  |
| Enterprise ColumnStore node | 64+ cores | 128+ GB |

## Storage Requirements

The ColumnStore Object Storage topology requires the following storage types:

| Storage Type                                                                                                                              | Description                                                                                                                                                                                                                                      |
| ----------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Storage Type                                                                                                                              | Description                                                                                                                                                                                                                                      |
| [Shared Local Storage](https://app.gitbook.com/s/rBEU9juWLfTDcdwF3Q14/architecture/columnstore-storage-architecture#shared-local-storage) | The ColumnStore Object Storage topology uses shared local storage for the [Storage Manager directory](https://app.gitbook.com/s/rBEU9juWLfTDcdwF3Q14/architecture/columnstore-storage-architecture#storage-manager-directory) to store metadata. |

## Shared Local Storage Directories

The ColumnStore Object Storage topology uses shared local storage for the Storage Manager directory to store metadata.

The Storage Manager directory is located at the following path by default:

* `/var/lib/columnstore/storagemanager`

## Shared Local Storage Options

The most common shared local storage options for the ColumnStore Object Storage topology are:

| Shared Local Storage                   | Common Usage | Description                                                                                                                                                                                                                                                                                                                                                                                     |
| -------------------------------------- | ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Shared Local Storage                   | Common Usage | Description                                                                                                                                                                                                                                                                                                                                                                                     |
| EBS (Elastic Block Store) Multi-Attach | AWS          | • EBS is a high-performance block-storage service for AWS (Amazon Web Services). • EBS Multi-Attach allows an EBS volume to be attached to multiple instances in AWS. Only clustered file systems, such as GFS2, are supported. • For deployments in AWS, EBS Multi-Attach is a recommended option for the Storage Manager directory, and Amazon S3 storage is the recommended option for data. |
| EFS (Elastic File System)              | AWS          | • EFS is a scalable, elastic, cloud-native NFS file system for AWS (Amazon Web Services). • For deployments in AWS, EFS is a recommended option for the Storage Manager directory, and Amazon S3 storage is the recommended option for data. EFS is a scalable, elastic, cloud-native NFS file system for AWS (Amazon Web Services).                                                            |
| Filestore                              | GCP          | • Filestore is high-performance, fully managed storage for GCP (Google Cloud Platform). • For deployments in GCP, Filestore is the recommended option for the Storage Manager directory, and Google Object Storage (S3-compatible) is the recommended option for data.                                                                                                                          |
| GlusterFS                              | On-premises  | • GlusterFS is a distributed file system. • GlusterFS supports replication and failover.                                                                                                                                                                                                                                                                                                        |
| NFS (Network File System)              | On-premises  | • NFS is a distributed file system. • If NFS is used, the storage should be mounted with the sync option to ensure that each node flushes its changes immediately. • For on-premises deployments, NFS is the recommended option for the Storage Manager directory, and any S3-compatible storage is the recommended option for data.                                                            |

## Enterprise ColumnStore Management with CMAPI

Enterprise ColumnStore's CMAPI (Cluster Management API) is a REST API that can be used to manage a multi-node Enterprise ColumnStore cluster.

Many tools are capable of interacting with REST APIs. For example, the curl utility could be used to make REST API calls from the command-line.

Many programming languages also have libraries for interacting with REST APIs.

The examples below show how to use the CMAPI with curl.

### URL Endpoint Format for REST API

```
https://{server}:{port}/cmapi/{version}/{route}/{command}
```

For example:

* [shutdown](https://mcs1:8640/cmapi/0.4.0/cluster/shutdown)
* [start](https://mcs1:8640/cmapi/0.4.0/cluster/start)
* [status](https://mcs1:8640/cmapi/0.4.0/cluster/status)

### Required Request Headers

* `'x-api-key'`: '93816fa66cc2d8c224e62275bd4f248234dd4947b68d4af2b29671dd7d5532dd'
* `'Content-Type'`: 'application/json'

x-api-key can be set to any value of your choice during the first call to the server. Subsequent connections will require this same key.

### Get Status

```
$ curl -k -s https://mcs1:8640/cmapi/0.4.0/cluster/status \
      --header 'Content-Type:application/json' \
      --header 'x-api-key:93816fa66cc2d8c224e62275bd4f248234dd4947b68d4af2b29671dd7d5532dd' \
      | jq .
```

### Start Cluster

```
$ curl -k -s -X PUT https://mcs1:8640/cmapi/0.4.0/cluster/start \
      --header 'Content-Type:application/json' \
      --header 'x-api-key:93816fa66cc2d8c224e62275bd4f248234dd4947b68d4af2b29671dd7d5532dd' \
      --data '{"timeout":20}' \
      | jq .
```

### Stop Cluster

```
$ curl -k -s -X PUT https://mcs1:8640/cmapi/0.4.0/cluster/shutdown \
      --header 'Content-Type:application/json' \
      --header 'x-api-key:93816fa66cc2d8c224e62275bd4f248234dd4947b68d4af2b29671dd7d5532dd' \
      --data '{"timeout":20}' \
      | jq .
```

### Add Node

```
$ curl -k -s -X PUT https://mcs1:8640/cmapi/0.4.0/cluster/node \
      --header 'Content-Type:application/json' \
      --header 'x-api-key:93816fa66cc2d8c224e62275bd4f248234dd4947b68d4af2b29671dd7d5532dd' \
      --data '{"timeout":20, "node": "192.0.2.2"}' \
      | jq .
```

### Remove Node

```
$ curl -k -s -X DELETE https://mcs1:8640/cmapi/0.4.0/cluster/node \
      --header 'Content-Type:application/json' \
      --header 'x-api-key:93816fa66cc2d8c224e62275bd4f248234dd4947b68d4af2b29671dd7d5532dd' \
      --data '{"timeout":20, "node": "192.0.2.2"}' \
      | jq .
```

## Quick Reference

### MariaDB Enterprise Server Configuration Management

| Method             | Description                                                                                                                                                           |
| ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Method             | Description                                                                                                                                                           |
| Configuration File | Configuration files (such as /etc/my.cnf) can be used to set system-variables and options. The server must be restarted to apply changes made to configuration files. |
| Command-line       | The server can be started with command-line options that set system-variables and options.                                                                            |
| SQL                | Users can set system-variables that support dynamic changes on-the-fly using the SET statement.                                                                       |

MariaDB Enterprise Server packages are configured to read configuration files from different paths, depending on the operating system. Making custom changes to Enterprise Server default configuration files is not recommended because custom changes may be overwritten by other default configuration files that are loaded later.

To ensure that your custom changes will be read last, create a custom configuration file with the z- prefix in one of the include directories.

| Distribution                               | Example Configuration File Path                |
| ------------------------------------------ | ---------------------------------------------- |
| Distribution                               | Example Configuration File Path                |
| • CentOS • Red Hat Enterprise Linux (RHEL) | /etc/my.cnf.d/z-custom-mariadb.cnf             |
| • Debian • Ubuntu                          | /etc/mysql/mariadb.conf.d/z-custom-mariadb.cnf |

## MariaDB Enterprise Server Service Management

The systemctl command is used to start and stop the MariaDB Enterprise Server service.

| Operation              | Command                        |
| ---------------------- | ------------------------------ |
| Operation              | Command                        |
| Start                  | sudo systemctl start mariadb   |
| Stop                   | sudo systemctl stop mariadb    |
| Restart                | sudo systemctl restart mariadb |
| Enable during startup  | sudo systemctl enable mariadb  |
| Disable during startup | sudo systemctl disable mariadb |
| Status                 | sudo systemctl status mariadb  |

For additional information, see "Start and Stop Services".

## MariaDB Enterprise Server Logs

MariaDB Enterprise Server produces log data that can be helpful in problem diagnosis.

Log filenames and locations may be overridden in the server configuration. The default location of logs is the data directory. The data directory is specified by the datadir system variable.

| Log                          | System Variable/Option    | Default Filename  |
| ---------------------------- | ------------------------- | ----------------- |
| Log                          | System Variable/Option    | Default Filename  |
| MariaDB Error Log            | log\_error                | .err              |
| MariaDB Enterprise Audit Log | server\_audit\_file\_path | server\_audit.log |
| Slow Query Log               | slow\_query\_log\_file    | -slow.log         |
| General Query Log            | general\_log\_file        | .log              |
| Binary Log                   | log\_bin                  | -bin              |

## Enterprise ColumnStore Service Management

The systemctl command is used to start and stop the ColumnStore service.

| Operation              | Command                                    |
| ---------------------- | ------------------------------------------ |
| Operation              | Command                                    |
| Start                  | sudo systemctl start mariadb-columnstore   |
| Stop                   | sudo systemctl stop mariadb-columnstore    |
| Restart                | sudo systemctl restart mariadb-columnstore |
| Enable during startup  | sudo systemctl enable mariadb-columnstore  |
| Disable during startup | sudo systemctl disable mariadb-columnstore |
| Status                 | sudo systemctl status mariadb-columnstore  |

In the ColumnStore Object Storage topology, the mariadb-columnstore service should not be enabled. The CMAPI service restarts Enterprise ColumnStore as needed, so it does not need to start automatically upon reboot.

## Enterprise ColumnStore CMAPI Service Management

The systemctl command is used to start and stop the CMAPI service.

| Operation              | Command                                          |
| ---------------------- | ------------------------------------------------ |
| Operation              | Command                                          |
| Start                  | sudo systemctl start mariadb-columnstore-cmapi   |
| Stop                   | sudo systemctl stop mariadb-columnstore-cmapi    |
| Restart                | sudo systemctl restart mariadb-columnstore-cmapi |
| Enable during startup  | sudo systemctl enable mariadb-columnstore-cmapi  |
| Disable during startup | sudo systemctl disable mariadb-columnstore-cmapi |
| Status                 | sudo systemctl status mariadb-columnstore-cmapi  |

For additional information on endpoints, see "CMAPI".

## MaxScale Configuration Management

MaxScale can be configured using several methods. These methods make use of MaxScale's [REST API](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/administrative-tools-for-mariadb-maxscale/administrative-tools-for-mariadb-maxscale-rest-api/).

| Method                                                                                                                                                   | Benefits                                                                                                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Method                                                                                                                                                   | Benefits                                                                                                                                                                                                |
| [MaxCtrl](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/administrative-tools-for-mariadb-maxscale/administrative-tools-for-mariadb-maxscale-maxctrl/)   | Command-line utility to perform administrative tasks through the REST API. See MaxCtrl Commands.                                                                                                        |
| [MaxGUI](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/administrative-tools-for-mariadb-maxscale/maxgui/)                                               | MaxGUI is a graphical utility that can perform administrative tasks through the REST API.                                                                                                               |
| [REST API](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/administrative-tools-for-mariadb-maxscale/administrative-tools-for-mariadb-maxscale-rest-api/) | The REST API can be used directly. For example, the curl utility could be used to make REST API calls from the command-line. Many programming languages also have libraries to interact with REST APIs. |

The procedure on these pages configures MaxScale using MaxCtrl.

## MaxScale Service Management

The systemctl command is used to start and stop the MaxScale service.>

| Operation              | Command                         |
| ---------------------- | ------------------------------- |
| Operation              | Command                         |
| Start                  | sudo systemctl start maxscale   |
| Stop                   | sudo systemctl stop maxscale    |
| Restart                | sudo systemctl restart maxscale |
| Enable during startup  | sudo systemctl enable maxscale  |
| Disable during startup | sudo systemctl disable maxscale |
| Status                 | sudo systemctl status maxscale  |

For additional information, see "Start and Stop Services".

## Next Step

Navigation in the procedure Shared Local Storage topology

Next: Step 1: Prepare ColumnStore Nodes.

Copyright © 2025 MariaDB
