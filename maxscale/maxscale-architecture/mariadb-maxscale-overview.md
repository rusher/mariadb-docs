---
description: >-
  Get an overview of MariaDB MaxScale. This section introduces its core
  functionalities, including intelligent routing, load balancing, and high
  availability, for managing and optimizing deployment.
---

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

| Release Series | Latest Release Date | Latest Release                                                                                                                                                                                       |
| -------------- | ------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Release Series | Latest Release Date | Latest Release                                                                                                                                                                                       |
| 24.02          | 2024-12-09          | [MariaDB MaxScale 24.02.4](../maxscale-versions/mariadb-maxscale-24-02/maxscale-24-02release-notes/mariadb-maxscale-2402-maxscale-2402-mariadb-maxscale-24022-release-notes-2024-06-03.md)           |
| 23.08          | 2024-12-09          | MariaDB MaxScale 23.08.8                                                                                                                                                                             |
| 23.02          | 2024-12-09          | [MariaDB MaxScale 23.02.12](../maxscale-versions/mariadb-maxscale-23-02/mariadb-maxscale-23-02-release-notes/mariadb-maxscale-2302-maxscale-2302-mariadb-maxscale-23029-release-notes-2024-03-11.md) |
| 22.08          | 2024-12-09          | MariaDB MaxScale 22.08.15                                                                                                                                                                            |
| 6              | 2024-03-11          | [MariaDB MaxScale 6.4.15](../maxscale-versions/mariadb-maxscale-21-06/)                                                                                                                              |
| 2.5            | 2023-10-25          | [MariaDB MaxScale 2.5.29](../maxscale-versions/mariadb-maxscale-25/maxscale-25-release-notes/mariadb-maxscale-25-mariadb-maxscale-2529-release-notes-2023-10-25.md)                                  |
| 2.4            | 2022-01-10          | [MariaDB MaxScale 2.4.19](../maxscale-versions/mariadb-maxscale-24/maxscale-24-release-notes/mariadb-maxscale-24-mariadb-maxscale-2419-release-notes-2022-01-10.md)                                  |

## Available Documentation

### Security

* [Authentication with MariaDB MaxScale](../maxscale-security/mariadb-maxscale-authentication/)
* [Data-in-Transit Encryption for MariaDB MaxScale](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption)

### Architecture

* [MariaDB MaxScale Architecture](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/migrating-to-mariadb/migrating-to-mariadb-from-sql-server/understanding-mariadb-architecture)

### What's New

* See the [MariaDB MaxScale 24.02 Changelog](../maxscale-versions/mariadb-maxscale-24-02/mariadb-maxscale-2402-maxscale-2402-changelog.md) for a list of what's new in MaxScale 24.02 and prior versions.

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
