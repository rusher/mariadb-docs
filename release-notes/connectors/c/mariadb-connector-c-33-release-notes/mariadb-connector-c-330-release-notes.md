# Connector/C 3.3.0.rc1 Release Notes

The most recent [_**Stable**_](../../../community-server/about/release-criteria.md) _**(GA)**_ release of MariaDB Connector/C is:[**MariaDB Connector/C 3.4.5**](../mariadb-connector-c-3-4-release-notes/mariadb-connector-c-3-4-5-release-notes.md)

[Download](https://mariadb.com/downloads/#connectors)[Release Notes](mariadb-connector-c-330-release-notes.md)[Changelog](../changelogs/mariadb-connector-c-33-changelogs/mariadb-connector-c-330-changelog.md)[About MariaDB Connector/C](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-c/README.md)

**Release date:** 15 Feb 2022

This is a [_**RC**_](../../../community-server/about/release-criteria.md) release of MariaDB\
Connector/C, formerly known as MariaDB Client Library for C.

**For a description of this library see the**[**MariaDB Connector/C**](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c) **page.**

**Do not use non-stable (non-GA) releases in production!**

## New features

#### Restrict authentication plugins ([CONC-544](https://jira.mariadb.org/browse/CONC-544))

Added new option MARIADB\_OPT\_RESTRICTED\_AUTH (and corresponding "restricted-auth" option for configuration files) which specifies on or more comma spearated authentication plugins which are allowed for authenication.

If the server asks for an authentication plugin not listed in this option the connect attempt will fail with error CR\_PLUGIN\_NOT\_ALLOWED.

### ZStandard compresion support

Zstd compression is now supported for connections to a MySQL Server 8.0 or newer.\
Compression algorithms are now provided via plugins. If the Zstd compression plugin is not part of a downloaded package it means, that zstd is not installed by default on this platform. In this case you have to install the zstd libraries and include files and build the plugin from source.

#### Support for semi synchronous replication ([CONC-470](https://jira.mariadb.org/browse/CONC-470))

Beside already supported asynchronous replication the replication/binlog API now supports semi synchronous replication.

#### Failover capabilities ([CONC-365](https://jira.mariadb.org/browse/CONC-365))

host parameter of mysql\_real\_connect (and corresponding configuration settings MYSQL\_OPT\_HOST for mysql\_options() api call and host key in configuration files) now accepts to specify multiple hosts and ports.

When establishing a connection, the list of specified hosts is run through until a connection can be established. If no connection can be established to any of the specified hosts, an error is returned.

#### MARIADB\_CONNECTION\_BYTES\_READ and MARIADB\_CONNECTION\_BYTES\_SENT

mariadb\_get\_infov now supports options MARIADB\_CONNECTION\_BYTES\_READ and MARIADB\_CONNECTION\_BYTES\_SENT to obtain the bytes sent or read to/from database server.

#### Connection string support ([CONC-247](https://jira.mariadb.org/browse/CONC-247))

A connection string contains key/value pairs, separated by a semicolon as used in ODBC. Supported keys are all configuration options which can be used in MariaDB configuration files. For a complete list check[config\_files#configuration-options](https://github.com/mariadb-corporation/mariadb-connector-c/wiki/config_files#configuration-options).

The connection string must contain at least one semicolon, otherwise it wil be interpreted as hostname. Unknown or invalid keys will be ignored.

To connect via connection string, the following methods might be used:

* by specifing connection option in configuration file:
* by using mariadb\_connect() macro
* by passing connection string in host parameter to mysql\_real\_connect

## Bugs fixed

* [CONC-467](https://jira.mariadb.org/browse/CONC-467): rotate as first event isn't handled correctly (replication/binlog api)

## Changelog

For a list of changes made in this release, with links to detailed information\
on each push, see the [changelog](../changelogs/mariadb-connector-c-33-changelogs/mariadb-connector-c-330-changelog.md).

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
