# MariaDB Connector/Python 1.1.11 Release Notes

The most recent [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release of MariaDB Connector/Python is:[**MariaDB Connector/Python 1.1.12**](mariadb-connector-python-1-1-12-release-notes.md)

[Download](https://mariadb.com/downloads/connectors/connectors-data-access/python-connector/)[Release Notes](mariadb-connector-python-1-1-11-release-notes.md)[Changelog](../changelogs/mariadb-connector-python-11-changelogs/mariadb-connector-python-1-1-11-changelog.md)[Connector/Python Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/mariadb-connector-python/README.md)

**Release date:** 15 Nov 2024

This is a [_**stable**_](../../../mariadb-release-criteria.md) release of the MariaDB\
Connector/Python.

**For a description of this library see the**[**MariaDB Connector/Python documentation**](https://mariadb-corporation.github.io/mariadb-connector-python/index.html) **.**

MariaDB Connector/Python enables python programs to access MariaDB and MySQL databases, using an API which is compliant with the Python DB API 2.0 (PEP-249). It is written in C and uses MariaDB Connector/C client library for client server communication.

## Notable changes

* Added new property tls\_peer\_cert\_info which returns peer certificate information (TLS connections only).
* Added support for Python 3.13
* Removed Python 3.8 builds
* Binary packages for Windows are now built with Connector/C 3.4.3

## Bug fixes

* Build fixes for MariaDB Connector/C 3.4.x
* [CONPY-289](https://jira.mariadb.org/browse/CONPY-289): BIGINT out of range on bulk insert
* [CONPY-293](https://jira.mariadb.org/browse/CONPY-293): Fix gcc warnings
* [CONPY-283](https://jira.mariadb.org/browse/CONPY-283): Incorrect result format after cursor.scroll()

## Installation

MariaDB Connector/Python 1.1.11 can be obtained from central python repository:

```bash
pip3 install mariadb
```

or to upgrade to the most recent version

```bash
pip3 install --upgrade mariadb
```

## Changelog

For a list of changes made in this release, with links to detailed information\
on each push, see the [changelog](../changelogs/mariadb-connector-python-11-changelogs/mariadb-connector-python-1-1-11-changelog.md).

## Links:

* [Documentation](https://mariadb-corporation.github.io/mariadb-connector-python/index.htmli)
* [Bug tracker](https://jira.mariadb.org)
* Sources are hosted on [Github](https://github.com/mariadb-corporation/mariadb-connector-python)

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
