# Connector/Python 1.1.0 Beta2 Release Notes

The most recent [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release of MariaDB Connector/Python is:[**MariaDB Connector/Python 1.1.12**](mariadb-connector-python-1-1-12-release-notes.md)

<a href="https://mariadb.com/downloads/connectors/connectors-data-access/python-connector/" class="button primary">Download</a> <a href="mariadb-connector-python-1-1-0-beta2-release-notes.md" class="button secondary">Release Notes</a> <a href="../changelogs/mariadb-connector-python-11-changelogs/mariadb-connector-python-110-beta2-changelog.md" class="button secondary">Changelog</a> <a href="https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/connectors-quickstart-guides/connector-python-guide" class="button secondary">Connector/Python Overview</a>

**Release date:** 22 Oct 2021

This is a [_**beta**_](../../../mariadb-release-criteria.md) release of MariaDB Connector/Python and not intended for production use.

**Do not use&#x20;**_**beta**_**&#x20;releases in production!**

**For a description of this library see the**[**MariaDB Connector/Python documentation**](https://mariadb-corporation.github.io/mariadb-connector-python/index.html) **.**

MariaDB Connector/Python enables python programs to access MariaDB and MySQL databases, using an API which is compliant with the Python DB API 2.0 (PEP-249). It is written in C and uses MariaDB Connector/C client library for client server communication.

## Notable changes

Python 3.10 is now supported

## Bug fixes

* [CONPY-167](https://jira.mariadb.org/browse/CONPY-167): reprepare statement if executemany() was called directly after execute()
* [CONPY-168](https://jira.mariadb.org/browse/CONPY-168): Force use of binary protocol if binary parameters were provided
* [CONPY-169](https://jira.mariadb.org/browse/CONPY-169): Added unicode support for parser
* [CONPY-170](https://jira.mariadb.org/browse/CONPY-170): Added documentation for configuration file handling
* [CONPY-173](https://jira.mariadb.org/browse/CONPY-173): Windows build fix for Python 3.10

## Installation

MariaDB Connector/Python 1.1.0-beta2 can be obtained from central python repository:

```bash
pip3 install --pre mariadb
```

## Changelog

For a list of changes made in this release, with links to detailed information\
on each push, see the [changelog](../changelogs/mariadb-connector-python-11-changelogs/mariadb-connector-python-110-beta2-changelog.md).

## Links:

* [Documentation](https://mariadb-corporation.github.io/mariadb-connector-python/index.htmli)
* [Bug tracker](https://jira.mariadb.org)
* Sources are hosted on [Github](https://github.com/mariadb-corporation/mariadb-connector-python)

**Do not use&#x20;**_**beta**_**&#x20;releases in production!**

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
