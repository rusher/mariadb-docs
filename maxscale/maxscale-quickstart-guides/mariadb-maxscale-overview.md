# MariaDB MaxScale Overview

## Overview

MariaDB MaxScale is an advanced proxy, router, and load balancer:

* MaxScale performs automated failover for MariaDB replication. When the primary server fails, MaxScale promotes a replica to be the new primary and redirects the remaining replicas to it.
* MaxScale's ReadWriteSplit router performs query-based load balancing. ReadWriteSplit routes each write statement to the current primary server and load balances read statements by routing them to the replica servers.
* MaxScale's ReadConnRoute router performs connection-based load balancing. ReadConnRoute routes each connection to a single primary or replica node, depending on configuration.
* MaxScale can import data from Kafka and export data into Kafka. MaxScale's KafkaCDC router streams data from MariaDB database products to a Kafka broker. MaxScale's KafkaImporter router streams data from Kafka to MariaDB database products.
* MaxScale provides built-in mechanisms to perform server maintenance without disrupting applications or clients. Servers can be set to maintenance mode using the command-line interface with MaxCtrl, a web browser with MaxGUI, or REST API.
* MaxScale's Cache filter can improve SELECT performance by caching and reusing results.
* Security and traffic controls for database connections and queries can be implemented with MaxScale. MaxScale's QLAfilter can be used to create an audit trail by logging all queries. MaxScale's RegexFilter can also perform audit logging or protect against SQL injection by matching queries against a regular expression and performing various actions on the query, such as logging it, modifying it, or routing it to a specific server.

MariaDB MaxScale can be deployed in the cloud or on-premises.

## Scheduled Releases

MariaDB MaxScale follows the MariaDB Enterprise release schedule, which can be found here.

## Latest Software Releases

| Release Series | Latest Release Date | Latest Release                                                                                                                                                                                             |
| -------------- | ------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Release Series | Latest Release Date | Latest Release                                                                                                                                                                                             |
| 24.02          | 2024-12-09          | [MariaDB MaxScale 24.02.4](../other-maxscale-versions/mariadb-maxscale-24-02/maxscale-24-02release-notes/mariadb-maxscale-2402-maxscale-2402-mariadb-maxscale-24022-release-notes-2024-06-03.md)           |
| 23.08          | 2024-12-09          | [MariaDB MaxScale 23.08.8](https://mariadb.com/kb/en/mariadb-maxscale-2308-maxscale-2308-mariadb-maxscale-23085-release-notes-2024-03-11/)                                                                 |
| 23.02          | 2024-12-09          | [MariaDB MaxScale 23.02.12](../other-maxscale-versions/mariadb-maxscale-23-02/mariadb-maxscale-23-02-release-notes/mariadb-maxscale-2302-maxscale-2302-mariadb-maxscale-23029-release-notes-2024-03-11.md) |
| 22.08          | 2024-12-09          | [MariaDB MaxScale 22.08.15](https://mariadb.com/kb/en/mariadb-maxscale-2208-mariadb-maxscale-220812-release-notes-2024-03-11/)                                                                             |
| 6              | 2024-03-11          | [MariaDB MaxScale 6.4.15](../other-maxscale-versions/mariadb-maxscale-21-06/)                                                                                                                              |
| 2.5            | 2023-10-25          | [MariaDB MaxScale 2.5.29](../other-maxscale-versions/mariadb-maxscale-25/maxscale-25-release-notes/mariadb-maxscale-25-mariadb-maxscale-2529-release-notes-2023-10-25.md)                                  |
| 2.4            | 2022-01-10          | [MariaDB MaxScale 2.4.19](../other-maxscale-versions/mariadb-maxscale-24/maxscale-24-release-notes/mariadb-maxscale-24-mariadb-maxscale-2419-release-notes-2022-01-10.md)                                  |

## Available Documentation

### Deployment

* [Deploy ColumnStore Object Storage Topology](https://mariadb.com/kb/en/Deploy_ColumnStore_Object_Storage_Topology)
* [Deploy ColumnStore Shared Local Storage Topology](https://mariadb.com/kb/en/Deploy_ColumnStore_Shared_Local_Storage_Topology)
* [Deploy Galera Cluster Topology](https://mariadb.com/kb/en/Deploy_Galera_Cluster_Topology)
* [Deploy Primary/Replica Topology](https://mariadb.com/kb/en/Deploy_Primary/Replica_Topology)
* [Deploy Xpand Topology](https://mariadb.com/kb/en/Deploy_Xpand_Topology)

### Service Management

* [Administrative Tools for MariaDB MaxScale](https://mariadb.com/kb/en/Administrative_Tools_for_MariaDB_MaxScale)

### Connect and Query

* [Connect and Query](https://mariadb.com/kb/en/Connect_and_Query)

### Security

* [Authentication with MariaDB MaxScale](../maxscale-security/mariadb-maxscale-authentication/)
* [Data-in-Transit Encryption for MariaDB MaxScale](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption)
* [Enabling TLS for MaxScale's REST API](https://mariadb.com/kb/en/Enabling_TLS_for_MaxScale's_REST_API)
* [Enabling TLS on MaxScale](https://mariadb.com/kb/en/Enabling_TLS_on_MaxScale)

### Architecture

* [MariaDB MaxScale Architecture](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/migrating-to-mariadb/migrating-to-mariadb-from-sql-server/understanding-mariadb-architecture)

### What's New

* See the [MariaDB MaxScale 24.02 Changelog](../other-maxscale-versions/mariadb-maxscale-24-02/mariadb-maxscale-2402-maxscale-2402-changelog.md) for a list of what's new in MaxScale 24.02 and prior versions.

Copyright © 2025 MariaDB

{% @marketo/form formId="4316" %}
