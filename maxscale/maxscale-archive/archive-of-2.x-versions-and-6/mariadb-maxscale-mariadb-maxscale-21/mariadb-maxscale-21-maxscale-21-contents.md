# MaxScale 2.1 Contents

### About MariaDB MaxScale

* [About MariaDB MaxScale](about-maxscale-21/mariadb-maxscale-21-about-mariadb-maxscale-21.md)
* [Release Notes](../../archive-of-2x.xx-versions/mariadb-maxscale-21-06/)
* [Changelog](mariadb-maxscale-21-maxscale-21-changelog.md)
* [Limitations](about-maxscale-21/mariadb-maxscale-21-limitations-and-known-issues-within-mariadb-maxscale.md)

### Getting Started

* [MariaDB MaxScale Installation Guide](../../archive-of-2x.xx-versions/mariadb-maxscale-21-06/)
* [Building MariaDB MaxScale from Source Code](maxscale-21-getting-started/mariadb-maxscale-21-building-mariadb-maxscale-from-source-code.md)
* [Configuration Guide](maxscale-21-getting-started/mariadb-maxscale-21-mariadb-maxscale-configuration-usage-scenarios.md)

### Upgrading MariaDB MaxScale

* [Upgrading MariaDB MaxScale from 2.0 to 2.1](../../archive-of-2x.xx-versions/mariadb-maxscale-21-06/)
* [Upgrading MariaDB MaxScale from 1.4 to 2.0](maxscale-21-upgrading/mariadb-maxscale-21-upgrading-mariadb-maxscale-from-14-to-20.md)

### Reference

* [MaxAdmin - Admin Interface](maxscale-21-reference/mariadb-maxscale-21-maxadmin-admin-interface.md)
* [Routing Hints](maxscale-21-reference/mariadb-maxscale-21-hint-syntax.md)
* [MaxBinlogCheck](../mariadb-maxscale-mariadb-maxscale-22/maxscale-22-reference/mariadb-maxscale-22-maxbinlogcheck-the-mariadb-binlog-check-utility.md)
* [MaxScale REST API](https://mariadb.com/kb/en/mariadb-maxscale-21-rest-api-design-document/)
* [Module Commands](../mariadb-maxscale-mariadb-maxscale-22/maxscale-22-reference/mariadb-maxscale-22-module-commands.md)

### Tutorials

The main tutorial for MariaDB MaxScale consist of setting up MariaDB MaxScale for the environment you are using with either a connection-based or a read/write-based configuration.

* [MariaDB MaxScale Tutorial](maxscale-21-tutorials/mariadb-maxscale-21-setting-up-mariadb-maxscale.md)

These tutorials are for specific use cases and module combinations.

* [Administration Tutorial](maxscale-21-tutorials/mariadb-maxscale-21-mariadb-maxscale-administration-tutorial.md)
* [Avro Router Tutorial](maxscale-21-tutorials/mariadb-maxscale-21-avrorouter-tutorial.md)
* [Filter Tutorial](https://mariadb.com/kb/en/maxscale-21-tutorials-filters/)
* [Galera Cluster Connection Routing Tutorial](maxscale-21-tutorials/mariadb-maxscale-21-connection-routing-with-galera-cluster.md)
* [Galera Gluster Read Write Splitting Tutorial](maxscale-21-tutorials/mariadb-maxscale-21-readwrite-splitting-with-galera-cluster.md)
* [MySQL Cluster Setup](maxscale-21-tutorials/mariadb-maxscale-21-mysql-cluster-setup-and-mariadb-maxscale-configuration.md)
* [MariaDB Replication Connection Routing Tutorial](maxscale-21-tutorials/mariadb-maxscale-21-connection-routing-with-mysql-replication.md)
* [MariaDB Replication Read Write Splitting Tutorial](maxscale-21-tutorials/mariadb-maxscale-21-readwrite-splitting-with-mysql-replication.md)
* [MariaDB MaxScale Information Schema Tutorial](maxscale-21-tutorials/mariadb-maxscale-21-maxinfo-plugin.md)
* [Notification Service](../../archive-of-2x.xx-versions/mariadb-maxscale-21-06/)
* [RabbitMQ and Tee Filter Data Archiving Tutorial](maxscale-21-tutorials/mariadb-maxscale-21-data-archiving-with-mqfilter-and-tee-filters.md)
* [RabbitMQ Setup and MariaDB MaxScale Integration Tutorial](maxscale-21-tutorials/mariadb-maxscale-21-rabbit-mq-setup-and-mariadb-maxscale-integration.md)
* [Replication Proxy with the Binlog Router Tutorial](maxscale-21-tutorials/mariadb-maxscale-21-mariadb-maxscale-as-a-binlog-server.md)
* [Simple Schema Sharding Tutorial](maxscale-21-tutorials/mariadb-maxscale-21-simple-sharding-with-two-servers.md)

Here are tutorials on monitoring and managing MariaDB MaxScale in cluster environments.

* [Nagios Plugins for MariaDB MaxScale Tutorial](maxscale-21-tutorials/mariadb-maxscale-21-mariadb-maxscale-nagios-plugins-for-nagios-351.md)

### Routers

The routing module is the core of a MariaDB MaxScale service. The router documentation\
contains all module specific configuration options and detailed explanations\
of their use.

* [Avrorouter](maxscale-21-routers/mariadb-maxscale-21-avrorouter.md)
* [Binlogrouter](maxscale-21-routers/mariadb-maxscale-21-binlogrouter.md)
* [Read Connection Router](maxscale-21-routers/mariadb-maxscale-21-readconnroute.md)
* [Read Write Split](maxscale-21-routers/mariadb-maxscale-21-readwritesplit.md)
* [Schemarouter](maxscale-21-routers/mariadb-maxscale-21-schemarouter-router.md)

There are also two diagnostic routing modules. The CLI is for MaxAdmin and\
the Debug CLI client for Telnet.

* [CLI](maxscale-21-routers/mariadb-maxscale-21-maxscale-21-cli.md)

### Filters

Here are detailed documents about the filters MariaDB MaxScale offers. They contain configuration guides and example use cases. Before reading these, you should have read the filter tutorial so that you know how they work and how to configure them.

* [Cache](maxscale-21-filters/mariadb-maxscale-21-maxscale-21-cache.md)
* [Consistent Critical Read Filter](maxscale-21-filters/mariadb-maxscale-21-consistent-critical-read-filter.md)
* [Database Firewall Filter](maxscale-21-filters/mariadb-maxscale-21-database-firewall-filter.md)
* [Insert Stream Filter](../mariadb-maxscale-mariadb-maxscale-23/maxscale-23-filters/mariadb-maxscale-23-insert-stream-filter.md)
* [Luafilter](maxscale-21-filters/mariadb-maxscale-21-lua-filter.md)
* [Masking Filter](maxscale-21-filters/mariadb-maxscale-21-masking.md)
* [Maxrows Filter](maxscale-21-filters/mariadb-maxscale-21-maxrows.md)
* [Named Server Filter](maxscale-21-filters/mariadb-maxscale-21-named-server-filter.md)
* [Query Log All](maxscale-21-filters/mariadb-maxscale-21-query-log-all-filter.md)
* [RabbitMQ Filter](maxscale-21-filters/mariadb-maxscale-21-rabbitmq-filter.md)
* [Regex Filter](maxscale-21-filters/mariadb-maxscale-21-regex-filter.md)
* [Tee Filter](maxscale-21-filters/mariadb-maxscale-21-tee-filter.md)
* [Top N Filter](maxscale-21-filters/mariadb-maxscale-21-top-filter.md)
* [Transaction Performance Monitoring Filter](../../archive-of-2x.xx-versions/mariadb-maxscale-21-06/)

### Monitors

Common options for all monitor modules.

* [Monitor Common](../../archive-of-2x.xx-versions/mariadb-maxscale-21-06/)

Module specific documentation.

* [Aurora Monitor](../mariadb-maxscale-mariadb-maxscale-22/maxscale-22-monitors/mariadb-maxscale-22-aurora-monitor.md)
* [Galera Monitor](maxscale-21-monitors/mariadb-maxscale-21-galera-monitor.md)
* [Multi-Master Monitor](../mariadb-maxscale-mariadb-maxscale-22/maxscale-22-monitors/mariadb-maxscale-22-multi-master-monitor.md)
* [MySQL Monitor](maxscale-21-monitors/mariadb-maxscale-21-mysql-monitor.md)
* [MySQL Cluster Monitor](maxscale-21-monitors/mariadb-maxscale-21-ndb-cluster-monitor.md)

### Protocols

Documentation for MaxScale protocol modules.

* [Change Data Capture (CDC) Protocol](maxscale-21-protocols/mariadb-maxscale-21-change-data-capture-cdc-protocol.md)
* [Change Data Capture (CDC) Users](maxscale-21-protocols/mariadb-maxscale-21-change-data-capture-cdc-users.md)

### Authenticators

A short description of the authentication module type can be found in the[Authentication Modules](maxscale-21-authenticators/mariadb-maxscale-21-authentication-modules-in-maxscale.md)\
document.

* [MySQL Authenticator](../mariadb-maxscale-mariadb-maxscale-22/maxscale-22-authenticators/mariadb-maxscale-22-mysql-authenticator.md)
* [GSSAPI Authenticator](maxscale-21-authenticators/mariadb-maxscale-21-gssapi-client-authenticator.md)

### Utilities

* [RabbitMQ Consumer Client](maxscale-21-filters/mariadb-maxscale-21-rabbitmq-consumer-client.md)

### Design Documents

* [DCB States (to be replaced in StarUML)](https://mariadb.com/kb/en/Design-Documents/DCB-States.pdf)
* [Schema Sharding Router Technical Documentation](maxscale-21-design-documents/mariadb-maxscale-21-schemarouter-router-technical-overview.md)
* [Plugin development guide](maxscale-21-design-documents/mariadb-maxscale-21-mariadb-maxscale-plugin-development-guide.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
