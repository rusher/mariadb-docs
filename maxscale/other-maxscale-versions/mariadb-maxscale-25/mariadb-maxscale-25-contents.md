# MaxScale 2.5 Contents

### About MariaDB MaxScale

* [About MariaDB MaxScale](about-maxscale-25/mariadb-maxscale-25-about-mariadb-maxscale.md)
* [Changelog](mariadb-maxscale-25-changelog.md)
* [Limitations](about-maxscale-25/mariadb-maxscale-25-limitations-and-known-issues-within-mariadb-maxscale.md)

### Getting Started

* [MariaDB MaxScale Installation Guide](maxscale-25-getting-started/mariadb-maxscale-25-mariadb-maxscale-installation-guide.md)
* [Building MariaDB MaxScale from Source Code](maxscale-25-getting-started/mariadb-maxscale-25-building-mariadb-maxscale-from-source-code.md)
* [Configuration Guide](maxscale-25-getting-started/mariadb-maxscale-25-mariadb-maxscale-configuration-guide.md)
* [MaxGUI](maxscale-25-getting-started/mariadb-maxscale-25-mariadb-maxscale-maxgui-guide.md)

### Upgrading MariaDB MaxScale

* [Upgrading MariaDB MaxScale from 2.4 to 2.5](maxscale-25-upgrading/mariadb-maxscale-25-upgrading-mariadb-maxscale-from-24-to-25.md)
* [Upgrading MariaDB MaxScale from 2.3 to 2.4](maxscale-25-upgrading/mariadb-maxscale-25-upgrading-mariadb-maxscale-from-23-to-24.md)
* [Upgrading MariaDB MaxScale from 2.2 to 2.3](maxscale-25-upgrading/mariadb-maxscale-25-upgrading-mariadb-maxscale-from-22-to-23.md)
* [Upgrading MariaDB MaxScale from 2.1 to 2.2](maxscale-25-upgrading/mariadb-maxscale-25-upgrading-mariadb-maxscale-from-21-to-22.md)
* [Upgrading MariaDB MaxScale from 2.0 to 2.1](maxscale-25-upgrading/mariadb-maxscale-25-upgrading-mariadb-maxscale-from-20-to-21.md)
* [Upgrading MariaDB MaxScale from 1.4 to 2.0](maxscale-25-upgrading/mariadb-maxscale-25-upgrading-mariadb-maxscale-from-14-to-20.md)

### Reference

* [MaxCtrl - Command Line Admin Interface](maxscale-25-reference/mariadb-maxscale-25-maxctrl.md)
* [MaxScale REST API](maxscale-25-rest-api/mariadb-maxscale-25-rest-api.md)
* [Module Commands](maxscale-25-reference/mariadb-maxscale-25-module-commands.md)
* [Routing Hints](maxscale-25-reference/mariadb-maxscale-25-hint-syntax.md)

### Tutorials

The main tutorial for MariaDB MaxScale consist of setting up MariaDB MaxScale for the environment you are using with either a connection-based or a read/write-based configuration.

* [MariaDB MaxScale Tutorial](maxscale-25-tutorials/mariadb-maxscale-25-setting-up-mariadb-maxscale.md)

These tutorials are for specific use cases and module combinations.

* [Administration Tutorial](maxscale-25-tutorials/mariadb-maxscale-25-mariadb-maxscale-administration-tutorial.md)
* [Avro Router Tutorial](maxscale-25-tutorials/mariadb-maxscale-25-avrorouter-tutorial.md)
* [Connection Routing Tutorial](maxscale-25-tutorials/mariadb-maxscale-25-connection-routing-with-mariadb-maxscale.md)
* [Filter Tutorial](maxscale-25-tutorials/mariadb-maxscale-25-filters.md)
* [MariaDB Monitor Failover Tutorial](maxscale-25-tutorials/mariadb-maxscale-25-automatic-failover-with-mariadb-monitor.md)
* [Read Write Splitting Tutorial](maxscale-25-tutorials/mariadb-maxscale-25-read-write-splitting-with-mariadb-maxscale.md)
* [Simple Schema Sharding Tutorial](maxscale-25-tutorials/mariadb-maxscale-25-simple-sharding-with-two-servers.md)
* [Xpand Monitor Tutorial](maxscale-25-tutorials/mariadb-maxscale-25-configuring-the-xpand-monitor.md)
* [Xpand Usage Tutorial](maxscale-25-tutorials/mariadb-maxscale-25-maxscale-and-xpand-tutorial.md)

Here are tutorials on monitoring and managing MariaDB MaxScale in cluster environments.

* [REST API Tutorial](maxscale-25-tutorials/mariadb-maxscale-25-rest-api-tutorial.md)

### Routers

The routing module is the core of a MariaDB MaxScale service. The router documentation\
contains all module specific configuration options and detailed explanations\
of their use.

* [Avrorouter](maxscale-25-routers/mariadb-maxscale-25-avrorouter.md)
* [Binlogrouter](maxscale-25-routers/mariadb-maxscale-25-binlogrouter.md)
* [Cat](maxscale-25-routers/mariadb-maxscale-25-cat.md)
* [HintRouter](maxscale-25-routers/mariadb-maxscale-25-hintrouter.md)
* [KafkaCDC](maxscale-25-routers/mariadb-maxscale-25-kafkacdc.md)
* [MirrorRouter](maxscale-25-routers/mariadb-maxscale-25-mirror.md)
* [Read Connection Router](maxscale-25-routers/mariadb-maxscale-25-readconnroute.md)
* [Read Write Split](maxscale-25-routers/mariadb-maxscale-25-readwritesplit.md)
* [Schemarouter](maxscale-25-routers/mariadb-maxscale-25-schemarouter.md)
* [SmartRouter](maxscale-25-routers/mariadb-maxscale-25-smartrouter.md)

### Filters

Here are detailed documents about the filters MariaDB MaxScale offers. They contain configuration guides and example use cases. Before reading these, you should have read the filter tutorial so that you know how they work and how to configure them.

* [Binlog Filter](maxscale-25-filters/mariadb-maxscale-25-binlog-filter.md)
* [Cache](maxscale-25-filters/mariadb-maxscale-25-cache.md)
* [Consistent Critical Read Filter](maxscale-25-filters/mariadb-maxscale-25-consistent-critical-read-filter.md)
* [Database Firewall Filter](maxscale-25-filters/mariadb-maxscale-25-database-firewall-filter.md)
* [Hint Filter](maxscale-25-filters/mariadb-maxscale-25-hintfilter.md)
* [Insert Stream Filter](maxscale-25-filters/mariadb-maxscale-25-insert-stream-filter.md)
* [Luafilter](maxscale-25-filters/mariadb-maxscale-25-lua-filter.md)
* [Masking Filter](maxscale-25-filters/mariadb-maxscale-25-masking.md)
* [Maxrows Filter](maxscale-25-filters/mariadb-maxscale-25-maxrows.md)
* [Named Server Filter](maxscale-25-filters/mariadb-maxscale-25-named-server-filter.md)
* [Query Log All](maxscale-25-filters/mariadb-maxscale-25-query-log-all-filter.md)
* [Regex Filter](maxscale-25-filters/mariadb-maxscale-25-regex-filter.md)
* [Tee Filter](maxscale-25-filters/mariadb-maxscale-25-tee-filter.md)
* [Throttle Filter](maxscale-25-filters/mariadb-maxscale-25-throttle.md)
* [Top N Filter](maxscale-25-filters/mariadb-maxscale-25-top-filter.md)
* [Transaction Performance Monitoring Filter](maxscale-25-filters/mariadb-maxscale-25-transaction-performance-monitoring-filter.md)

### Monitors

Common options for all monitor modules.

* [Monitor Common](maxscale-25-monitors/mariadb-maxscale-25-common-monitor-parameters.md)

Module specific documentation.

* [Aurora Monitor](maxscale-25-monitors/mariadb-maxscale-25-aurora-monitor.md)
* [ColumnStore Monitor](maxscale-25-monitors/mariadb-maxscale-25-columnstore-monitor.md)
* [Galera Monitor](maxscale-25-monitors/mariadb-maxscale-25-galera-monitor.md)
* [MariaDB Monitor](maxscale-25-monitors/mariadb-maxscale-25-mariadb-monitor.md)
* [Xpand Monitor](maxscale-25-monitors/mariadb-maxscale-25-xpand-monitor.md)

### Protocols

Documentation for MaxScale protocol modules.

* [Change Data Capture (CDC) Protocol](maxscale-25-protocols/mariadb-maxscale-25-change-data-capture-cdc-protocol.md)
* [Change Data Capture (CDC) Users](maxscale-25-protocols/mariadb-maxscale-25-change-data-capture-cdc-users.md)

The MaxScale CDC Connector provides a C++ API for consuming data from a CDC system.

* [CDC Connector](maxscale-25-connectors/mariadb-maxscale-25-maxscale-cdc-connector.md)

### Authenticators

A short description of the authentication module type can be found in the[Authentication Modules](maxscale-25-authenticators/mariadb-maxscale-25-authentication-modules.md)\
document.

* [MySQL Authenticator](maxscale-25-authenticators/mariadb-maxscale-25-mysql-authenticator.md)
* [GSSAPI Authenticator](maxscale-25-authenticators/mariadb-maxscale-25-gssapi-client-authenticator.md)

### Design Documents

* [Plugin development guide](https://mariadb.com/kb/en/mariadb-maxscale-25-mariadb-maxscale-plugin-development-guide/)

CC BY-SA / Gnu FDL

{% @marketo/form formId="4316" %}
