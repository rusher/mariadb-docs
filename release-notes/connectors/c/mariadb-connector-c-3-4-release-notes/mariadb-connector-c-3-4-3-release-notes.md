# Connector/C 3.4.3 Release Notes

The most recent [_**Stable**_](../../../community-server/about/release-criteria.md) _**(GA)**_ release of MariaDB Connector/C is:[**MariaDB Connector/C 3.4.5**](mariadb-connector-c-3-4-5-release-notes.md)

[Download](https://mariadb.com/downloads/connectors)[Release Notes](mariadb-connector-c-3-4-3-release-notes.md)[Changelog](../changelogs/mariadb-connectorc-3-4-changelogs/mariadb-connector-c-3-4-3-changelog.md)[About MariaDB Connector/C](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-c/README.md)

**Release date:** 12 Nov 2024

This is a [_**Stable (GA)**_](../../../community-server/about/release-criteria.md) release of MariaDB\
Connector/C, formerly known as MariaDB Client Library for C.

MariaDB Connector/C 3.4.2 was not released separately but is included in [MariaDB Community Server 11.4.4](../../../community-server/mariadb-11-4-series/mariadb-11-4-4-release-notes.md). MariaDB Connector/C 3.4.3 includes additional bug fixes for the Connector and is included in [MariaDB Community Server 11.6.2](../../../community-server/old-releases/release-notes-mariadb-11-6-rolling-releases/mariadb-11-6-2-release-notes.md), and [11.7.1](../../../community-server/old-releases/mariadb-11-7-rolling-releases/mariadb-11-7-1-release-notes.md).

**For a description of this library see the**[**MariaDB Connector/C**](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c) **page.**

## Notable Changes

* Added option MARIADB\_TLS\_VERIFY\_STATUS to retrieve status of peer certificate validation via mariadb\_get\_infov().
* [CONC-690](https://jira.mariadb.org/browse/CONC-690): Due to required cryptographic functions that are part of the TLS crypto libraries the option WITH\_SSL=OFF (disabling TLS/SSL) is no longer supported and will result in a build error.
* [CONC-724](https://jira.mariadb.org/browse/CONC-724): Added option MARIADB\_OPT\_TLS\_VERIFICATION\_CALLBACK to specify a callback function for peer certificate testing.
* Man pages are no longer stored in github repository. They can be build with cmake option -DWITH\_DOCS=ON (requires pyhon 3 and pandoc).
* If the environment variable MARIADB\_TLS\_DISABLE\_PEER\_VERIFICATION was set, the peer certificate verification will be skipped.
* [CONC-717](https://jira.mariadb.org/browse/CONC-717): Added windows support for the parsec authentication plugin, a new plugin added to MariaDB Server 11.6

## Issues fixed:

* [CONC-712](https://jira.mariadb.org/browse/CONC-712): Skip host name verification on local connections
* [CONC-731](https://jira.mariadb.org/browse/CONC-731): Wrong error message if incorrect fingerprint was specified
* [CONC-732](https://jira.mariadb.org/browse/CONC-732): Always set verification callback function, even if peer certificate validation is disabled (OpenSSL)
* [CONC-735](https://jira.mariadb.org/browse/CONC-735): A reconnect doesn't do node failover when using a connection string with multiple hosts

## Changelog

For a list of changes made in this release, with links to detailed information\
on each push, see the [changelog](../changelogs/mariadb-connectorc-3-4-changelogs/mariadb-connector-c-3-4-3-changelog.md).

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
