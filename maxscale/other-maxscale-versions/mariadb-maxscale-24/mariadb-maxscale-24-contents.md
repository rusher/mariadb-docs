
# MaxScale 2.4 Contents

# Contents


## About MariaDB MaxScale


* [About MariaDB MaxScale](about-maxscale-24/mariadb-maxscale-24-about-mariadb-maxscale.md)
* [Changelog](mariadb-maxscale-24-changelog.md)
* [Limitations](about-maxscale-24/mariadb-maxscale-24-limitations-and-known-issues-within-mariadb-maxscale.md)


## Getting Started


* [MariaDB MaxScale Installation Guide](maxscale-24-getting-started/mariadb-maxscale-24-mariadb-maxscale-installation-guide.md)
* [Building MariaDB MaxScale from Source Code](maxscale-24-getting-started/mariadb-maxscale-24-building-mariadb-maxscale-from-source-code.md)
* [Configuration Guide](maxscale-24-getting-started/mariadb-maxscale-24-mariadb-maxscale-configuration-guide.md)


## Upgrading MariaDB MaxScale


* [Upgrading MariaDB MaxScale from 2.3 to 2.4](maxscale-24-upgrading/mariadb-maxscale-24-upgrading-mariadb-maxscale-from-23-to-24.md)
* [Upgrading MariaDB MaxScale from 2.2 to 2.3](maxscale-24-upgrading/mariadb-maxscale-24-upgrading-mariadb-maxscale-from-22-to-23.md)
* [Upgrading MariaDB MaxScale from 2.1 to 2.2](maxscale-24-upgrading/mariadb-maxscale-24-upgrading-mariadb-maxscale-from-21-to-22.md)
* [Upgrading MariaDB MaxScale from 2.0 to 2.1](maxscale-24-upgrading/mariadb-maxscale-24-upgrading-mariadb-maxscale-from-20-to-21.md)
* [Upgrading MariaDB MaxScale from 1.4 to 2.0](maxscale-24-upgrading/mariadb-maxscale-24-upgrading-mariadb-maxscale-from-14-to-20.md)


## Reference


* [MaxCtrl - Command Line Admin Interface](maxscale-24-reference/mariadb-maxscale-24-maxctrl.md)
* [MaxAdmin - Legacy Admin Interface](maxscale-24-reference/mariadb-maxscale-24-maxadmin-admin-interface.md)
* [Routing Hints](maxscale-24-reference/mariadb-maxscale-24-hint-syntax.md)
* [MaxBinlogCheck](maxscale-24-reference/mariadb-maxscale-24-maxbinlogcheck-the-mariadb-binlog-check-utility.md)
* [MaxScale REST API](maxscale-24-rest-api/maxscale-24-rest-api-maxscale-rest-api.md)
* [Module Commands](maxscale-24-reference/mariadb-maxscale-24-module-commands.md)


## Tutorials


The main tutorial for MariaDB MaxScale consist of setting up MariaDB MaxScale for the environment you are using with either a connection-based or a read/write-based configuration.


* [MariaDB MaxScale Tutorial](maxscale-24-tutorials/mariadb-maxscale-24-setting-up-mariadb-maxscale.md)


These tutorials are for specific use cases and module combinations.


* [Connection Routing Tutorial](maxscale-24-tutorials/mariadb-maxscale-24-connection-routing-with-mariadb-maxscale.md)
* [Read Write Splitting Tutorial](maxscale-24-tutorials/mariadb-maxscale-24-read-write-splitting-with-mariadb-maxscale.md)
* [Administration Tutorial](maxscale-24-tutorials/mariadb-maxscale-24-mariadb-maxscale-administration-tutorial.md)
* [Avro Router Tutorial](maxscale-24-tutorials/mariadb-maxscale-24-avrorouter-tutorial.md)
* [MariaDB Monitor Failover Tutorial](maxscale-24-tutorials/mariadb-maxscale-24-automatic-failover-with-mariadb-monitor.md)
* [MariaDB MaxScale Information Schema Tutorial](maxscale-24-tutorials/mariadb-maxscale-24-maxinfo-plugin.md)
* [Replication Proxy with the Binlog Router Tutorial](maxscale-24-tutorials/mariadb-maxscale-24-mariadb-maxscale-as-a-binlog-server.md)
* [Simple Schema Sharding Tutorial](maxscale-24-tutorials/mariadb-maxscale-24-simple-sharding-with-two-servers.md)
* [Filter Tutorial](maxscale-24-tutorials/9077.md)
* [RabbitMQ and Tee Filter Data Archiving Tutorial](maxscale-24-tutorials/mariadb-maxscale-24-data-archiving-with-mqfilter-and-tee-filters.md)
* [RabbitMQ Setup and MariaDB MaxScale Integration Tutorial](maxscale-24-tutorials/mariadb-maxscale-24-rabbit-mq-setup-and-mariadb-maxscale-integration.md)
* [Xpand Monitor Tutorial](maxscale-24-tutorials/mariadb-maxscale-24-configuring-the-xpand-monitor.md)
* [MaxScale Xpand Tutorial](maxscale-24-tutorials/mariadb-maxscale-24-maxscale-and-xpand-tutorial.md)


Here are tutorials on monitoring and managing MariaDB MaxScale in cluster environments.


* [REST API Tutorial](maxscale-24-tutorials/mariadb-maxscale-24-rest-api-tutorial.md)


## Routers


The routing module is the core of a MariaDB MaxScale service. The router documentation
contains all module specific configuration options and detailed explanations
of their use.


* [Avrorouter](maxscale-24-routers/mariadb-maxscale-24-avrorouter.md)
* [Binlogrouter](maxscale-24-routers/mariadb-maxscale-24-binlogrouter.md)
* [Cat](maxscale-24-routers/mariadb-maxscale-24-cat.md)
* [HintRouter](maxscale-24-routers/mariadb-maxscale-24-hintrouter.md)
* [Read Connection Router](maxscale-24-routers/mariadb-maxscale-24-readconnroute.md)
* [Read Write Split](maxscale-24-routers/mariadb-maxscale-24-readwritesplit.md)
* [Schemarouter](maxscale-24-routers/mariadb-maxscale-24-schemarouter.md)
* [SmartRouter](maxscale-24-routers/mariadb-maxscale-24-smartrouter.md)


The legacy diagnostic routing module MaxAdmin has been deprecated: avoid using
it.


* [CLI](maxscale-24-routers/mariadb-maxscale-24-cli.md)


## Filters


Here are detailed documents about the filters MariaDB MaxScale offers. They contain configuration guides and example use cases. Before reading these, you should have read the filter tutorial so that you know how they work and how to configure them.


* [Cache](maxscale-24-filters/mariadb-maxscale-24-cache.md)
* [Consistent Critical Read Filter](maxscale-24-filters/mariadb-maxscale-24-consistent-critical-read-filter.md)
* [Database Firewall Filter](maxscale-24-filters/mariadb-maxscale-24-database-firewall-filter.md)
* [Insert Stream Filter](maxscale-24-filters/mariadb-maxscale-24-insert-stream-filter.md)
* [Luafilter](maxscale-24-filters/mariadb-maxscale-24-lua-filter.md)
* [Masking Filter](maxscale-24-filters/mariadb-maxscale-24-masking.md)
* [Maxrows Filter](maxscale-24-filters/mariadb-maxscale-24-maxrows.md)
* [Named Server Filter](maxscale-24-filters/mariadb-maxscale-24-named-server-filter.md)
* [Query Log All](maxscale-24-filters/mariadb-maxscale-24-query-log-all-filter.md)
* [Hint Filter](maxscale-24-filters/mariadb-maxscale-24-hintfilter.md)
* [RabbitMQ Filter](maxscale-24-filters/mariadb-maxscale-24-rabbitmq-filter.md)
* [Regex Filter](maxscale-24-filters/mariadb-maxscale-24-regex-filter.md)
* [Tee Filter](maxscale-24-filters/mariadb-maxscale-24-tee-filter.md)
* [Throttle Filter](maxscale-24-filters/mariadb-maxscale-24-throttle.md)
* [Top N Filter](maxscale-24-filters/mariadb-maxscale-24-top-filter.md)
* [Transaction Performance Monitoring Filter](maxscale-24-filters/mariadb-maxscale-24-transaction-performance-monitoring-filter.md)
* [Binlog Filter](maxscale-24-filters/mariadb-maxscale-24-binlog-filter.md)


## Monitors


Common options for all monitor modules.


* [Monitor Common](maxscale-24-monitors/mariadb-maxscale-24-common-monitor-parameters.md)


Module specific documentation.


* [MariaDB Monitor](maxscale-24-monitors/mariadb-maxscale-24-mariadb-monitor.md)
* [Galera Monitor](maxscale-24-monitors/mariadb-maxscale-24-galera-monitor.md)
* [ColumnStore Monitor](maxscale-24-monitors/mariadb-maxscale-24-columnstore-monitor.md)
* [Aurora Monitor](maxscale-24-monitors/mariadb-maxscale-24-aurora-monitor.md)
* [Xpand Monitor](maxscale-24-monitors/mariadb-maxscale-24-xpand-monitor.md)


## Protocols


Documentation for MaxScale protocol modules.


* [Change Data Capture (CDC) Protocol](maxscale-24-protocols/mariadb-maxscale-24-change-data-capture-cdc-protocol.md)
* [Change Data Capture (CDC) Users](maxscale-24-protocols/mariadb-maxscale-24-change-data-capture-cdc-users.md)


The MaxScale CDC Connector provides a C++ API for consuming data from a CDC system.


* [CDC Connector](maxscale-24-connectors/mariadb-maxscale-24-maxscale-cdc-connector.md)


## Authenticators


A short description of the authentication module type can be found in the
[Authentication Modules](maxscale-24-authenticators/mariadb-maxscale-24-authentication-modules-in-maxscale.md)
document.


* [MySQL Authenticator](maxscale-24-authenticators/mariadb-maxscale-24-mysql-authenticator.md)
* [GSSAPI Authenticator](maxscale-24-authenticators/mariadb-maxscale-24-gssapi-client-authenticator.md)


## Utilities


* [RabbitMQ Consumer Client](maxscale-24-filters/mariadb-maxscale-24-rabbitmq-consumer-client.md)


## Design Documents


* [Plugin development guide](https://mariadb.com/kb/en/mariadb-maxscale-24-mariadb-maxscale-plugin-development-guide/)


CC BY-SA / Gnu FDL


{% @marketo/form formId="4316" %}
