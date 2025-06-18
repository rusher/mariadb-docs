# MaxScale 2.3 Contents

### About MariaDB MaxScale

* [About MariaDB MaxScale](about-maxscale-23/mariadb-maxscale-23-about-mariadb-maxscale.md)
* [Changelog](../mariadb-maxscale-21-06/)
* [Limitations](about-maxscale-23/mariadb-maxscale-23-limitations-and-known-issues-within-mariadb-maxscale.md)

### Getting Started

* [MariaDB MaxScale Installation Guide](maxscale-23-getting-started/mariadb-maxscale-23-mariadb-maxscale-installation-guide.md)
* [Building MariaDB MaxScale from Source Code](../mariadb-maxscale-mariadb-maxscale-22/maxscale-22-getting-started/mariadb-maxscale-22-building-mariadb-maxscale-from-source-code.md)
* [Configuration Guide](../mariadb-maxscale-21-06/)

### Upgrading MariaDB MaxScale

* [Upgrading MariaDB MaxScale from 2.2 to 2.3](../mariadb-maxscale-21-06/)
* [Upgrading MariaDB MaxScale from 2.1 to 2.2](../mariadb-maxscale-mariadb-maxscale-22/maxscale-22-upgrading/mariadb-maxscale-22-upgrading-mariadb-maxscale-from-21-to-22.md)
* [Upgrading MariaDB MaxScale from 2.0 to 2.1](maxscale-23-upgrading/mariadb-maxscale-23-upgrading-mariadb-maxscale-from-20-to-21.md)
* [Upgrading MariaDB MaxScale from 1.4 to 2.0](../mariadb-maxscale-14/mariadb-maxscale-14-upgrading-maxscale/upgrading-mariadb-maxscale-from-14-to-20.md)

### Reference

* [MaxAdmin - Admin Interface](maxscale-23-reference/mariadb-maxscale-23-maxadmin-admin-interface.md)
* [Routing Hints](maxscale-23-reference/mariadb-maxscale-23-hint-syntax.md)
* [MaxBinlogCheck](maxscale-23-reference/mariadb-maxscale-23-maxbinlogcheck-the-mariadb-binlog-check-utility.md)
* [MaxScale REST API](maxscale-23-rest-api/maxscale-2-3-rest-api.md)
* [Module Commands](maxscale-23-reference/mariadb-maxscale-23-module-commands.md)

### Tutorials

The main tutorial for MariaDB MaxScale consist of setting up MariaDB MaxScale for the environment you are using with either a connection-based or a read/write-based configuration.

* [MariaDB MaxScale Tutorial](../mariadb-maxscale-21-06/)

These tutorials are for specific use cases and module combinations.

* [Connection Routing Tutorial](maxscale-tutorials/mariadb-maxscale-23-connection-routing-with-mariadb-maxscale.md)
* [Read Write Splitting Tutorial](maxscale-tutorials/mariadb-maxscale-23-readwrite-splitting-with-mariadb-maxscale.md)
* [Administration Tutorial](../mariadb-maxscale-mariadb-maxscale-22/maxscale-22-tutorials/mariadb-maxscale-22-mariadb-maxscale-administration-tutorial.md)
* [Avro Router Tutorial](maxscale-tutorials/mariadb-maxscale-23-avrorouter-tutorial.md)
* [MaxScale Failover with Keepalived and MaxCtrl](https://mariadb.com/kb/en/)
* [MariaDB Monitor Failover Tutorial](maxscale-tutorials/mariadb-maxscale-23-automatic-failover-with-mariadb-monitor.md)
* [MariaDB MaxScale Information Schema Tutorial](maxscale-tutorials/mariadb-maxscale-23-maxinfo-plugin.md)
* [Replication Proxy with the Binlog Router Tutorial](maxscale-tutorials/mariadb-maxscale-23-mariadb-maxscale-as-a-binlog-server.md)
* [Simple Schema Sharding Tutorial](maxscale-tutorials/mariadb-maxscale-23-simple-sharding-with-two-servers.md)
* [Filter Tutorial](maxscale-tutorials/8077.md)
* [MySQL Cluster Setup](maxscale-tutorials/mariadb-maxscale-23-mysql-cluster-setup-and-mariadb-maxscale-configuration.md)
* [RabbitMQ and Tee Filter Data Archiving Tutorial](maxscale-tutorials/mariadb-maxscale-23-data-archiving-with-mqfilter-and-tee-filters.md)
* [RabbitMQ Setup and MariaDB MaxScale Integration Tutorial](maxscale-tutorials/mariadb-maxscale-23-rabbit-mq-setup-and-mariadb-maxscale-integration.md)

Here are tutorials on monitoring and managing MariaDB MaxScale in cluster environments.

* [MariaDB MaxScale HA with Lsyncd](https://mariadb.com/kb/en/)
* [Nagios Plugins for MariaDB MaxScale Tutorial](maxscale-tutorials/mariadb-maxscale-23-mariadb-maxscale-nagios-plugins-for-nagios-351.md)
* [REST API Tutorial](../mariadb-maxscale-21-06/)

### Routers

The routing module is the core of a MariaDB MaxScale service. The router documentation\
contains all module specific configuration options and detailed explanations\
of their use.

* [Avrorouter](maxscale-23-routers/mariadb-maxscale-23-avrorouter.md)
* [Binlogrouter](maxscale-23-routers/mariadb-maxscale-23-binlogrouter.md)
* [HintRouter](maxscale-23-routers/mariadb-maxscale-23-hintrouter.md)
* [Read Connection Router](maxscale-23-routers/mariadb-maxscale-23-readconnroute.md)
* [Read Write Split](maxscale-23-routers/mariadb-maxscale-23-readwritesplit.md)
* [Schemarouter](maxscale-23-routers/mariadb-maxscale-23-schemarouter-router.md)
* [Cat](../mariadb-maxscale-21-06/)

There are also two diagnostic routing modules. The CLI is for MaxAdmin and\
the Debug CLI client for Telnet.

* [CLI](maxscale-23-routers/mariadb-maxscale-23-cli.md)

### Filters

Here are detailed documents about the filters MariaDB MaxScale offers. They contain configuration guides and example use cases. Before reading these, you should have read the filter tutorial so that you know how they work and how to configure them.

* [Cache](maxscale-23-filters/mariadb-maxscale-23-cache.md)
* [Consistent Critical Read Filter](maxscale-23-filters/mariadb-maxscale-23-consistent-critical-read-filter.md)
* [Database Firewall Filter](maxscale-23-filters/mariadb-maxscale-23-database-firewall-filter.md)
* [Insert Stream Filter](../mariadb-maxscale-mariadb-maxscale-21/maxscale-21-filters/mariadb-maxscale-21-insert-stream-filter.md)
* [Luafilter](maxscale-23-filters/mariadb-maxscale-23-lua-filter.md)
* [Masking Filter](maxscale-23-filters/mariadb-maxscale-23-masking.md)
* [Maxrows Filter](maxscale-23-filters/mariadb-maxscale-23-maxrows.md)
* [Named Server Filter](maxscale-23-filters/mariadb-maxscale-23-named-server-filter.md)
* [Query Log All](maxscale-23-filters/mariadb-maxscale-23-query-log-all-filter.md)
* [Hint Filter](maxscale-23-filters/mariadb-maxscale-23-hintfilter.md)
* [RabbitMQ Filter](maxscale-23-filters/mariadb-maxscale-23-rabbitmq-filter.md)
* [Regex Filter](maxscale-23-filters/mariadb-maxscale-23-regex-filter.md)
* [Tee Filter](maxscale-23-filters/mariadb-maxscale-23-tee-filter.md)
* [Throttle Filter](../mariadb-maxscale-21-06/)
* [Top N Filter](maxscale-23-filters/mariadb-maxscale-23-top-filter.md)
* [Transaction Performance Monitoring Filter](maxscale-23-filters/mariadb-maxscale-23-transaction-performance-monitoring-filter.md)
* [Binlog Filter](../mariadb-maxscale-21-06/)

### Monitors

Common options for all monitor modules.

* [Monitor Common](maxscale-23-monitors/mariadb-maxscale-23-common-monitor-parameters.md)

Module specific documentation.

* [MariaDB Monitor](maxscale-23-monitors/mariadb-maxscale-23-mariadb-monitor.md)
* [Galera Monitor](maxscale-23-monitors/mariadb-maxscale-23-galera-monitor.md)
* [ColumnStore Monitor](../mariadb-maxscale-21-06/)
* [Aurora Monitor](maxscale-23-monitors/mariadb-maxscale-23-aurora-monitor.md)

Legacy monitors that have been deprecated.

* [Multi-Master Monitor](maxscale-23-monitors/mariadb-maxscale-23-multi-master-monitor.md)
* [MySQL Cluster Monitor](maxscale-23-monitors/mariadb-maxscale-23-ndb-cluster-monitor.md)

### Protocols

Documentation for MaxScale protocol modules.

* [Change Data Capture (CDC) Protocol](maxscale-23-protocols/mariadb-maxscale-23-change-data-capture-cdc-protocol.md)
* [Change Data Capture (CDC) Users](maxscale-23-protocols/mariadb-maxscale-23-change-data-capture-cdc-users.md)

The MaxScale CDC Connector provides a C++ API for consuming data from a CDC system.

* [CDC Connector](maxscale-23-connectors/mariadb-maxscale-23-maxscale-cdc-connector.md)

### Authenticators

A short description of the authentication module type can be found in the[Authentication Modules](maxscale-23-authenticators/mariadb-maxscale-23-authentication-modules-in-maxscale.md)\
document.

* [MySQL Authenticator](maxscale-23-authenticators/mariadb-maxscale-23-mysql-authenticator.md)
* [GSSAPI Authenticator](../mariadb-maxscale-21-06/)

### Utilities

* [RabbitMQ Consumer Client](maxscale-23-filters/mariadb-maxscale-23-rabbitmq-consumer-client.md)

### Design Documents

* [Plugin development guide](https://mariadb.com/kb/en/mariadb-maxscale-23-mariadb-maxscale-plugin-development-guide/)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
