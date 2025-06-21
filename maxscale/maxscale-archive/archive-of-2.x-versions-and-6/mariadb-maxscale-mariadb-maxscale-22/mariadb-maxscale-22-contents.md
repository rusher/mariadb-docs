# MaxScale 2.2 Contents

### About MariaDB MaxScale

* [About MariaDB MaxScale](about-maxscale-22/mariadb-maxscale-22-about-mariadb-maxscale.md)
* [Changelog](../../archive-of-2x.xx-versions/mariadb-maxscale-21-06/)
* [Limitations](about-maxscale-22/mariadb-maxscale-22-limitations-and-known-issues-within-mariadb-maxscale.md)

### Getting Started

* [MariaDB MaxScale Installation Guide](maxscale-22-getting-started/mariadb-maxscale-22-mariadb-maxscale-installation-guide.md)
* [Building MariaDB MaxScale from Source Code](../mariadb-maxscale-mariadb-maxscale-23/maxscale-23-getting-started/mariadb-maxscale-23-building-mariadb-maxscale-from-source-code.md)
* [Configuration Guide](maxscale-22-getting-started/mariadb-maxscale-22-mariadb-maxscale-configuration-usage-scenarios.md)

### Upgrading MariaDB MaxScale

* [Upgrading MariaDB MaxScale from 2.1 to 2.2](../../archive-of-2x.xx-versions/mariadb-maxscale-21-06/)
* [Upgrading MariaDB MaxScale from 2.0 to 2.1](maxscale-22-upgrading/mariadb-maxscale-22-upgrading-mariadb-maxscale-from-20-to-21.md)
* [Upgrading MariaDB MaxScale from 1.4 to 2.0](maxscale-22-upgrading/mariadb-maxscale-22-upgrading-mariadb-maxscale-from-14-to-20.md)

### Reference

* [MaxAdmin - Admin Interface](maxscale-22-reference/mariadb-maxscale-22-maxadmin-admin-interface.md)
* [Routing Hints](maxscale-22-reference/mariadb-maxscale-22-hint-syntax.md)
* [MaxBinlogCheck](../../archive-of-2x.xx-versions/mariadb-maxscale-21-06/)
* [MaxScale REST API](../../archive-of-2x.xx-versions/mariadb-maxscale-21-06/)
* [Module Commands](../mariadb-maxscale-mariadb-maxscale-21/maxscale-21-reference/mariadb-maxscale-21-module-commands.md)

### Tutorials

The main tutorial for MariaDB MaxScale consist of setting up MariaDB MaxScale for the environment you are using with either a connection-based or a read/write-based configuration.

* [MariaDB MaxScale Tutorial](maxscale-22-tutorials/mariadb-maxscale-22-setting-up-mariadb-maxscale.md)

These tutorials are for specific use cases and module combinations.

* [Connection Routing Tutorial](maxscale-22-tutorials/mariadb-maxscale-22-connection-routing-with-mariadb-maxscale.md)
* [Read Write Splitting Tutorial](../../archive-of-2x.xx-versions/mariadb-maxscale-21-06/)
* [Administration Tutorial](../mariadb-maxscale-mariadb-maxscale-23/maxscale-tutorials/mariadb-maxscale-23-mariadb-maxscale-administration-tutorial.md)
* [Avro Router Tutorial](maxscale-22-tutorials/mariadb-maxscale-22-avrorouter-tutorial.md)
* [MariaDB Monitor Failover Tutorial](../../archive-of-2x.xx-versions/mariadb-maxscale-21-06/)
* [MariaDB MaxScale Information Schema Tutorial](maxscale-22-tutorials/mariadb-maxscale-22-maxinfo-plugin.md)
* [Replication Proxy with the Binlog Router Tutorial](maxscale-22-tutorials/mariadb-maxscale-22-mariadb-maxscale-as-a-binlog-server.md)
* [Simple Schema Sharding Tutorial](maxscale-22-tutorials/mariadb-maxscale-22-simple-sharding-with-two-servers.md)
* [Filter Tutorial](maxscale-22-tutorials/7122.md)
* [MySQL Cluster Setup](maxscale-22-tutorials/mariadb-maxscale-22-mysql-cluster-setup-and-mariadb-maxscale-configuration.md)
* [RabbitMQ and Tee Filter Data Archiving Tutorial](maxscale-22-tutorials/mariadb-maxscale-22-data-archiving-with-mqfilter-and-tee-filters.md)
* [RabbitMQ Setup and MariaDB MaxScale Integration Tutorial](maxscale-22-tutorials/mariadb-maxscale-22-rabbit-mq-setup-and-mariadb-maxscale-integration.md)

Here are tutorials on monitoring and managing MariaDB MaxScale in cluster environments.

* [Nagios Plugins for MariaDB MaxScale Tutorial](maxscale-22-tutorials/mariadb-maxscale-22-mariadb-maxscale-nagios-plugins-for-nagios-351.md)

### Routers

The routing module is the core of a MariaDB MaxScale service. The router documentation\
contains all module specific configuration options and detailed explanations\
of their use.

* [Avrorouter](maxscale-22-routers/mariadb-maxscale-22-avrorouter.md)
* [Binlogrouter](../../archive-of-2x.xx-versions/mariadb-maxscale-21-06/)
* [HintRouter](../../archive-of-2x.xx-versions/mariadb-maxscale-21-06/)
* [Read Connection Router](maxscale-22-routers/mariadb-maxscale-22-readconnroute.md)
* [Read Write Split](maxscale-22-routers/mariadb-maxscale-22-readwritesplit.md)
* [Schemarouter](maxscale-22-routers/mariadb-maxscale-22-schemarouter-router.md)

There are also two diagnostic routing modules. The CLI is for MaxAdmin and\
the Debug CLI client for Telnet.

* [CLI](../../archive-of-2x.xx-versions/mariadb-maxscale-21-06/)

### Filters

Here are detailed documents about the filters MariaDB MaxScale offers. They contain configuration guides and example use cases. Before reading these, you should have read the filter tutorial so that you know how they work and how to configure them.

* [Cache](../../archive-of-2x.xx-versions/mariadb-maxscale-21-06/)
* [Consistent Critical Read Filter](maxscale-22-filters/mariadb-maxscale-22-consistent-critical-read-filter.md)
* [Database Firewall Filter](maxscale-22-filters/mariadb-maxscale-22-database-firewall-filter.md)
* [Insert Stream Filter](maxscale-22-filters/mariadb-maxscale-22-insert-stream-filter.md)
* [Luafilter](maxscale-22-filters/mariadb-maxscale-22-lua-filter.md)
* [Masking Filter](maxscale-22-filters/mariadb-maxscale-22-masking.md)
* [Maxrows Filter](maxscale-22-filters/mariadb-maxscale-22-maxrows.md)
* [Named Server Filter](maxscale-22-filters/mariadb-maxscale-22-named-server-filter.md)
* [Query Log All](maxscale-22-filters/mariadb-maxscale-22-query-log-all-filter.md)
* [Hint Filter](../../archive-of-2x.xx-versions/mariadb-maxscale-21-06/)
* [RabbitMQ Filter](maxscale-22-filters/mariadb-maxscale-22-rabbitmq-filter.md)
* [Regex Filter](maxscale-22-filters/mariadb-maxscale-22-regex-filter.md)
* [Tee Filter](maxscale-22-filters/mariadb-maxscale-22-tee-filter.md)
* [Top N Filter](maxscale-22-filters/mariadb-maxscale-22-top-filter.md)
* [Transaction Performance Monitoring Filter](maxscale-22-filters/mariadb-maxscale-22-transaction-performance-monitoring-filter.md)

### Monitors

Common options for all monitor modules.

* [Monitor Common](../../archive-of-2x.xx-versions/mariadb-maxscale-21-06/)

Module specific documentation.

* [Aurora Monitor](../mariadb-maxscale-mariadb-maxscale-21/maxscale-21-monitors/mariadb-maxscale-21-aurora-monitor.md)
* [Galera Monitor](maxscale-22-monitors/mariadb-maxscale-22-galera-monitor.md)
* [Multi-Master Monitor](../mariadb-maxscale-mariadb-maxscale-21/maxscale-21-monitors/mariadb-maxscale-21-multi-master-monitor.md)
* [MariaDB Monitor](../../archive-of-2x.xx-versions/mariadb-maxscale-21-06/)
* [MySQL Cluster Monitor](../mariadb-maxscale-14/maxscale-14-monitors/ndb-cluster-monitor.md)

### Protocols

Documentation for MaxScale protocol modules.

* [Change Data Capture (CDC) Protocol](../../archive-of-2x.xx-versions/mariadb-maxscale-21-06/)
* [Change Data Capture (CDC) Users](maxscale-22-protocols/mariadb-maxscale-22-change-data-capture-cdc-users.md)

The MaxScale CDC Connector provides a C++ API for consuming data from a CDC system.

* [CDC Connector](../../archive-of-2x.xx-versions/mariadb-maxscale-21-06/)

### Authenticators

A short description of the authentication module type can be found in the[Authentication Modules](maxscale-22-authenticators/mariadb-maxscale-22-authentication-modules-in-maxscale.md)\
document.

* [MySQL Authenticator](../mariadb-maxscale-mariadb-maxscale-21/maxscale-21-authenticators/mariadb-maxscale-21-mysql-authenticator.md)
* [GSSAPI Authenticator](maxscale-22-authenticators/mariadb-maxscale-22-gssapi-client-authenticator.md)

### Utilities

* [RabbitMQ Consumer Client](maxscale-22-filters/mariadb-maxscale-22-rabbitmq-consumer-client.md)

### Design Documents

* [Plugin development guide](maxscale-22-design-documents/mariadb-maxscale-22-mariadb-maxscale-plugin-development-guide.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
