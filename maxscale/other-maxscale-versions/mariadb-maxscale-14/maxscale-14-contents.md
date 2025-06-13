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

# MaxScale 1.4 Contents

[Search page for MaxScale Documentation](https://mariadb-corporation.github.io/MaxScale/Search/)

## Contents

### About MaxScale

* [About MaxScale](about-maxscale-14/)
* [MaxScale 1.4.3 Release Notes](maxscale-14-release-notes/mariadb-maxscale-143-release-notes.md)
* [Changelog](../mariadb-maxscale-21-06/)
* [Limitations](about-maxscale-14/limitations-and-known-issues-within-maxscale.md)
* [COPYRIGHT](about-maxscale-14/copyrightmd.md)
* [LICENSE](about-maxscale-14/licensemd.md)

### Getting Started

* [MariaDB MaxScale Installation Guide](maxscale-14-getting-started/mariadb-maxscale-installation-guide.md)
* [Building MaxScale from Source Code](maxscale-14-getting-started/building-maxscale-from-source-code.md)
* [Configuration Guide](maxscale-14-getting-started/maxscale-configuration-usage-scenarios.md)

### Upgrading MaxScale

* [Upgrading MaxScale from 1.3 to 1.4](mariadb-maxscale-14-upgrading-maxscale/upgrading-maxscale-from-13-to-14.md)
* [Upgrading MaxScale from 1.2 to 1.3](mariadb-maxscale-14-upgrading-maxscale/upgrading-maxscale-from-12-to-13.md)
* [Upgrading MaxScale from 1.1.1 to 1.2](mariadb-maxscale-14-upgrading-maxscale/5379.md)
* [Upgrading MaxScale from 1.0.5 to 1.1.0](mariadb-maxscale-14-upgrading-maxscale/5380.md)

### Reference

* [MaxAdmin](maxscale-14-reference/maxadmin.md)
* [How Errors are Handled in MaxScale](maxscale-14-reference/how-errors-are-handled-in-maxscale.md)
* [Debug and Diagnostic Support](maxscale-14-reference/maxscale-change-history.md)
* [Routing Hints](maxscale-14-reference/maxscale-hint-syntax.md)
* [MaxBinlogCheck](maxscale-14-reference/maxbinlogcheck.md)
* [MaxScale and SSL](maxscale-14-reference/maxscale-and-ssl.md)

### Tutorials

The main tutorial for MaxScale consist of setting up MaxScale for the environment you are using with either a connection-based or a read/write-based configuration.

* [MaxScale Tutorial](maxscale-14-tutorials/setting-up-maxscale.md)

These tutorials are for specific use cases and module combinations.

* [Administration Tutorial](maxscale-14-tutorials/maxscale-administration-tutorial.md)
* [Filter Tutorial](maxscale-14-tutorials/tutorials-maxscale-filters.md)
* [MaxScale Information Schema Tutorial](maxscale-14-tutorials/maxinfo-plugin.md)
* [MySQL Cluster Setup](maxscale-14-tutorials/mysql-cluster-setup-and-maxscale-configuration.md)
* [Replication Proxy with the Binlog Router Tutorial](maxscale-14-tutorials/maxscale-as-a-replication-proxy.md)
* [RabbitMQ Setup and MaxScale Integration Tutorial](maxscale-14-tutorials/rabbit-mq-setup-and-maxscale-integration.md)
* [RabbitMQ and Tee Filter Data Archiving Tutorial](maxscale-14-tutorials/data-archiving-with-mqfilter-and-tee-filters.md)
* [Simple Schema Sharding Tutorial](maxscale-14-tutorials/maxscale-simple-sharding-with-two-servers.md)

Here are tutorials on monitoring and managing MaxScale in cluster environments.

* [Nagios Plugins for MaxScale Tutorial](maxscale-14-tutorials/maxscale-nagios-plugins-for-nagios-351.md)

### Routers

The routing module is the core of a MaxScale service. The router documentation\
contains all module specific configuration options and detailed explanations\
of their use.

* [Read Write Split](maxscale-14-routers/readwritesplit.md)
* [Read Connection Router](maxscale-14-routers/maxscale-readconnroute.md)
* [Schemarouter](maxscale-14-routers/maxscale-routers-schemarouter-router.md)
* [Binlogrouter](maxscale-14-routers/binlogrouter.md)

There are also two diagnostic routing modules. The CLI is for MaxAdmin and\
the Debug CLI client for Telnet.

* [CLI](../../maxscale-management/maxscale-troubleshooting.md)
* [Debug CLI](maxscale-14-routers/debug-cli.md)

### Filters

Here are detailed documents about the filters MaxScale offers. They contain configuration guides and example use cases. Before reading these, you should have read the filter tutorial so that you know how they work and how to configure them.

* [Query Log All](maxscale-14-filters/maxscale-query-log-all-filter.md)
* [Regex Filter](maxscale-14-filters/maxscale-regex-filter-overview.md)
* [Tee Filter](maxscale-14-filters/maxscale-tee-filter-overview.md)
* [Top N Filter](maxscale-14-filters/maxscale-top-filter-overview.md)
* [Database Firewall Filter](maxscale-14-filters/maxscale-database-firewall-filter.md)
* [RabbitMQ Filter](maxscale-14-filters/maxscale-rabbitmq-filter.md)
* [Named Server Filter](maxscale-14-filters/maxscale-named-server-filter-overview.md)

### Monitors

Common options for all monitor modules.

* [Monitor Common](../mariadb-maxscale-21-06/)

Module specific documentation.

* [MySQL Monitor](maxscale-14-monitors/mysql-monitor.md)
* [Galera Monitor](maxscale-14-monitors/maxscale-galera-monitor.md)
* [Multi-Master Monitor](maxscale-14-monitors/multi-master-monitor.md)
* [MySQL Cluster Monitor](../mariadb-maxscale-mariadb-maxscale-21/maxscale-21-monitors/mariadb-maxscale-21-ndb-cluster-monitor.md)

### Utilities

* [RabbitMQ Consumer Client](maxscale-14-filters/maxscale-rabbitmq-consumer-client.md)

### Design Documents

* [Core Objects Design (in development)](https://mariadb-corporation.github.io/MaxScale/Design-Documents/core-objects-html-docs)
* [Binlog Router Design (in development)](https://mariadb-corporation.github.io/MaxScale/Design-Documents/binlog-router-html-docs)
* [DCB States (to be replaced in StarUML)](../../mariadb-maxscale-14/Design-Documents/DCB-States.pdf)
* [Schema Sharding Router Technical Documentation](maxscale-design-documents/schemarouter-router-technical-overview.md)

### Earlier Release Notes

* [MaxScale 1.4.0 Release Notes](maxscale-14-release-notes/mariadb-maxscale-140-beta-release-notes.md)
* [MaxScale 1.3.0 Release Notes](maxscale-14-release-notes/mariadb-maxscale-13-release-notes.md)
* [MaxScale 1.2.0 Release Notes](maxscale-14-release-notes/mariadb-maxscale-12-release-notes.md)
* [MaxScale 1.1.1 Release Notes](maxscale-14-release-notes/mariadb-maxscale-111-release-notes.md)
* [MaxScale 1.1.0 Release Notes](maxscale-14-release-notes/maxscale-11-release-notes.md)
* [MaxScale 1.0.3 Release Notes](maxscale-14-release-notes/maxscale-103-ga-new-features.md)
* [MaxScale 1.0.1 Release Notes](maxscale-14-release-notes/maxscale-101-beta-new-features.md)
* [MaxScale 1.0 Release Notes](maxscale-14-release-notes/maxscale-10-beta-new-features.md)
* [MaxScale 0.7 Release Notes](maxscale-14-release-notes/maxscale-07-alpha-new-features.md)
* [MaxScale 0.6 Release Notes](maxscale-14-release-notes/maxscale-bug-fixes.md)
* [MaxScale 0.5 Release Notes](maxscale-14-release-notes/maxscale-05-alpha-new-features.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
