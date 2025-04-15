
# MaxScale 24.08 Beta Contents

# Contents


## About MariaDB MaxScale


* [About MariaDB MaxScale](mariadb-maxscale-24-08-beta-about/mariadb-maxscale-2408-maxscale-2408-beta-about-mariadb-maxscale.md)
* [Changelog](mariadb-maxscale-2408-maxscale-2408-beta-changelog.md)
* [Limitations](mariadb-maxscale-24-08-beta-about/mariadb-maxscale-2408-maxscale-2408-beta-limitations-and-known-issues-within-mariadb-maxscale.md)


## Getting Started


* [MariaDB MaxScale Installation Guide](mariadb-maxscale-24-08-beta-getting-started/mariadb-maxscale-2408-maxscale-2408-beta-mariadb-maxscale-installation-guide.md)
* [Building MariaDB MaxScale from Source Code](mariadb-maxscale-24-08-beta-getting-started/mariadb-maxscale-2408-maxscale-2408-beta-building-mariadb-maxscale-from-source-code.md)
* [Configuration Guide](mariadb-maxscale-24-08-beta-getting-started/mariadb-maxscale-2408-maxscale-2408-beta-mariadb-maxscale-configuration-guide.md)
* [MaxGUI](mariadb-maxscale-24-08-beta-getting-started/mariadb-maxscale-2408-maxscale-2408-beta-mariadb-maxscale-maxgui-guide.md)


## Upgrading MariaDB MaxScale


* [Upgrading MaxScale](mariadb-maxscale-24-08-beta-upgrading/mariadb-maxscale-2408-maxscale-2408-beta-upgrading-mariadb-maxscale.md)


## Reference


* [MaxCtrl - Command Line Admin Interface](mariadb-maxscale-24-08-beta-reference/mariadb-maxscale-2408-maxscale-2408-beta-maxctrl.md)
* [MaxScale REST API](mariadb-maxscale-24-08-beta-rest-api/mariadb-maxscale-2408-maxscale-2408-beta-rest-api.md)
* [Module Commands](mariadb-maxscale-24-08-beta-reference/mariadb-maxscale-2408-maxscale-2408-beta-module-commands.md)
* [Routing Hints](mariadb-maxscale-24-08-beta-reference/mariadb-maxscale-2408-maxscale-2408-beta-hint-syntax.md)


## Tutorials


The main tutorial for MariaDB MaxScale consist of setting up MariaDB MaxScale for the environment you are using with either a connection-based or a read/write-based configuration.


* [MariaDB MaxScale Tutorial](mariadb-maxscale-24-08-beta-tutorials/mariadb-maxscale-2408-maxscale-2408-beta-setting-up-mariadb-maxscale.md)


These tutorials are for specific use cases and module combinations.


* [Administration Tutorial](mariadb-maxscale-24-08-beta-tutorials/mariadb-maxscale-2408-maxscale-2408-beta-mariadb-maxscale-administration-tutorial.md)
* [Avro Router Tutorial](mariadb-maxscale-24-08-beta-tutorials/mariadb-maxscale-2408-maxscale-2408-beta-avrorouter-tutorial.md)
* [Connection Routing Tutorial](mariadb-maxscale-24-08-beta-tutorials/mariadb-maxscale-2408-maxscale-2408-beta-connection-routing-with-mariadb-maxscale.md)
* [Filter Tutorial](mariadb-maxscale-24-08-beta-tutorials/mariadb-maxscale-2408-maxscale-2408-beta-filters.md)
* [MariaDB Monitor Failover Tutorial](mariadb-maxscale-24-08-beta-tutorials/mariadb-maxscale-2408-maxscale-2408-beta-automatic-failover-with-mariadb-monitor.md)
* [Read Write Splitting Tutorial](mariadb-maxscale-24-08-beta-tutorials/mariadb-maxscale-2408-maxscale-2408-beta-read-write-splitting-with-mariadb-maxscale.md)
* [Simple Schema Sharding Tutorial](mariadb-maxscale-24-08-beta-tutorials/mariadb-maxscale-2408-maxscale-2408-beta-schemarouter-simple-sharding-with-two-servers.md)


Here are tutorials on monitoring and managing MariaDB MaxScale in cluster environments.


* [REST API Tutorial](mariadb-maxscale-24-08-beta-tutorials/mariadb-maxscale-2408-maxscale-2408-beta-rest-api-tutorial.md)


## Routers


The routing module is the core of a MariaDB MaxScale service. The router documentation
contains all module specific configuration options and detailed explanations
of their use.


* [Avrorouter](mariadb-maxscale-24-08-beta-routers/mariadb-maxscale-2408-maxscale-2408-beta-avrorouter.md)
* [Binlogrouter](mariadb-maxscale-24-08-beta-routers/mariadb-maxscale-2408-maxscale-2408-beta-binlogrouter.md)
* [Cat](mariadb-maxscale-24-08-beta-routers/mariadb-maxscale-2408-maxscale-2408-beta-cat.md)
* [HintRouter](mariadb-maxscale-24-08-beta-routers/mariadb-maxscale-2408-maxscale-2408-beta-hintrouter.md)
* [KafkaCDC](mariadb-maxscale-24-08-beta-routers/mariadb-maxscale-2408-maxscale-2408-beta-kafkacdc.md)
* [KafkaImporter](mariadb-maxscale-24-08-beta-routers/mariadb-maxscale-2408-maxscale-2408-beta-kafkaimporter.md)
* [MirrorRouter](mariadb-maxscale-24-08-beta-routers/mariadb-maxscale-2408-maxscale-2408-beta-mirror.md)
* [Read Connection Router](mariadb-maxscale-24-08-beta-routers/mariadb-maxscale-2408-maxscale-2408-beta-readconnroute.md)
* [Read Write Split](mariadb-maxscale-24-08-beta-routers/mariadb-maxscale-2408-maxscale-2408-beta-readwritesplit.md)
* [Schemarouter](mariadb-maxscale-24-08-beta-routers/mariadb-maxscale-2408-maxscale-2408-beta-schemarouter.md)
* [SmartRouter](mariadb-maxscale-24-08-beta-routers/mariadb-maxscale-2408-maxscale-2408-beta-smartrouter.md)


The following routers are only available in MaxScale Enterprise.


* [Diff](mariadb-maxscale-24-08-beta-routers/mariadb-maxscale-2408-maxscale-2408-beta-diff-router-for-comparing-servers.md)


## Filters


Here are detailed documents about the filters MariaDB MaxScale offers. They contain configuration guides and example use cases. Before reading these, you should have read the filter tutorial so that you know how they work and how to configure them.


* [Binlog Filter](mariadb-maxscale-24-08-beta-filters/mariadb-maxscale-2408-maxscale-2408-beta-binlog-filter.md)
* [Cache](mariadb-maxscale-24-08-beta-filters/mariadb-maxscale-2408-maxscale-2408-beta-cache.md)
* [Comment Filter](mariadb-maxscale-24-08-beta-filters/mariadb-maxscale-2408-maxscale-2408-beta-comment-filter.md)
* [Consistent Critical Read Filter](mariadb-maxscale-24-08-beta-filters/mariadb-maxscale-2408-maxscale-2408-beta-consistent-critical-read-filter.md)
* [Hint Filter](mariadb-maxscale-24-08-beta-filters/mariadb-maxscale-2408-maxscale-2408-beta-hintfilter.md)
* [LDIFilter](mariadb-maxscale-24-08-beta-filters/mariadb-maxscale-2408-maxscale-2408-beta-ldi-filter.md)
* [Luafilter](mariadb-maxscale-24-08-beta-filters/mariadb-maxscale-2408-maxscale-2408-beta-lua-filter.md)
* [Masking Filter](mariadb-maxscale-24-08-beta-filters/mariadb-maxscale-2408-maxscale-2408-beta-masking.md)
* [Maxrows Filter](mariadb-maxscale-24-08-beta-filters/mariadb-maxscale-2408-maxscale-2408-beta-maxrows.md)
* [Named Server Filter](mariadb-maxscale-24-08-beta-filters/mariadb-maxscale-2408-maxscale-2408-beta-named-server-filter.md)
* [Prepared Statement Reuse Filter](mariadb-maxscale-24-08-beta-filters/mariadb-maxscale-2408-maxscale-2408-beta-psreuse.md)
* [Optimistic Transaction Execution Filter](mariadb-maxscale-24-08-beta-filters/mariadb-maxscale-2408-maxscale-2408-beta-optimistic-transaction-execution-filter.md)
* [Query Log All](mariadb-maxscale-24-08-beta-filters/mariadb-maxscale-2408-maxscale-2408-beta-query-log-all-filter.md)
* [Regex Filter](mariadb-maxscale-24-08-beta-filters/mariadb-maxscale-2408-maxscale-2408-beta-regex-filter.md)
* [Rewrite Filter](mariadb-maxscale-24-08-beta-filters/mariadb-maxscale-2408-maxscale-2408-beta-rewrite-filter.md)
* [Tee Filter](mariadb-maxscale-24-08-beta-filters/mariadb-maxscale-2408-maxscale-2408-beta-tee-filter.md)
* [Throttle Filter](mariadb-maxscale-24-08-beta-filters/mariadb-maxscale-2408-maxscale-2408-beta-throttle.md)
* [Top N Filter](mariadb-maxscale-24-08-beta-filters/mariadb-maxscale-2408-maxscale-2408-beta-top-filter.md)
* [Transaction Performance Monitoring Filter](mariadb-maxscale-24-08-beta-filters/mariadb-maxscale-2408-maxscale-2408-beta-transaction-performance-monitoring-filter.md)


The following filters are only available in MaxScale Enterprise.


* [Wcar](mariadb-maxscale-24-08-beta-filters/mariadb-maxscale-2408-maxscale-2408-beta-wcar-workload-capture-and-replay.md)


## Monitors


Common options for all monitor modules.


* [Monitor Common](mariadb-maxscale-2408-beta-maxscale-24-08-beta-monitors/mariadb-maxscale-2408-maxscale-2408-beta-common-monitor-parameters.md)


Module specific documentation.


* [Galera Monitor](mariadb-maxscale-2408-beta-maxscale-24-08-beta-monitors/mariadb-maxscale-2408-maxscale-2408-beta-galera-monitor.md)
* [MariaDB Monitor](mariadb-maxscale-2408-beta-maxscale-24-08-beta-monitors/mariadb-maxscale-2408-maxscale-2408-beta-mariadb-monitor.md)


## Protocols


Documentation for MaxScale protocol modules.


* [MariaDB](mariadb-maxscale-24-08-beta-protocols/mariadb-maxscale-2408-maxscale-2408-beta-mariadb-protocol-module.md)
* [Change Data Capture (CDC) Protocol](mariadb-maxscale-24-08-beta-protocols/mariadb-maxscale-2408-maxscale-2408-beta-change-data-capture-cdc-protocol.md)
* [Change Data Capture (CDC) Users](mariadb-maxscale-24-08-beta-protocols/mariadb-maxscale-2408-maxscale-2408-beta-change-data-capture-cdc-users.md)
* [NoSQL](mariadb-maxscale-24-08-beta-protocols/mariadb-maxscale-2408-maxscale-2408-beta-nosql-protocol-module.md)


The MaxScale CDC Connector provides a C++ API for consuming data from a CDC system.


* [CDC Connector](mariadb-maxscale-24-08-beta-connectors/mariadb-maxscale-2408-maxscale-2408-beta-maxscale-cdc-connector.md)


## Authenticators


A short description of the authentication module type can be found in the
[Authentication Modules](mariadb-maxscale-24-08-beta-authenticators/mariadb-maxscale-2408-maxscale-2408-beta-authentication-modules.md)
document.


* [MySQL Authenticator](mariadb-maxscale-24-08-beta-authenticators/mariadb-maxscale-2408-maxscale-2408-beta-mariadbmysql-authenticator.md)
* [GSSAPI Authenticator](mariadb-maxscale-24-08-beta-authenticators/mariadb-maxscale-2408-maxscale-2408-beta-gssapi-client-authenticator.md)
