# MariaDB Connector/Python 1.1.0 RC1 Release Notes

The most recent [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release of MariaDB Connector/Python is:[**MariaDB Connector/Python 1.1.12**](mariadb-connector-python-1-1-12-release-notes.md)

[Download](https://mariadb.com/downloads/#connectors)[Release Notes](mariadb-connector-python-1-1-0-rc1-release-notes.md)[Changelog](../changelogs/mariadb-connector-python-11-changelogs/mariadb-connector-python-110-rc1-changelog.md)[Connector/Python Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/mariadb-connector-python/README.md)

**Release date:** 7 Apr 2022

This is an [_**rc**_](../../../mariadb-release-criteria.md) release of the MariaDB\
Connector/Python.

**Do not use non-stable (non-GA) releases in production!**

**For a description of this library see the**[**MariaDB Connector/Python documentation**](https://mariadb-corporation.github.io/mariadb-connector-python/index.html) **.**

MariaDB Connector/Python enables python programs to access MariaDB and MySQL databases, using an API which is compliant with the Python DB API 2.0 (PEP-249). It is written in C and uses MariaDB Connector/C client library for client server communication.

## Notable changes

* [CONPY-44](https://jira.mariadb.org/browse/CONPY-44): Added support for simple failover (Requires MariaDB Connector/C 3.3)
* [CONPY-184](https://jira.mariadb.org/browse/CONPY-184): Display status of objects in string representation (cursor, connection, pool)

## Bug fixes

* [CONPY-88](https://jira.mariadb.org/browse/CONPY-88): Get additional information in fieldinfo: cursor->description() now contains 3 additional elements: table\_name, orginal column name and original table name
* [CONPY-187](https://jira.mariadb.org/browse/CONPY-187): Fixed wrong detection of bulk capabilities
* [CONPY-188](https://jira.mariadb.org/browse/CONPY-188): If a connection or cursor is closed, an exception is returned whether a method or property of a closed object is called
* [CONPY-189](https://jira.mariadb.org/browse/CONPY-189): Fixed build with Visual Studio 2022
* [CONPY-178](https://jira.mariadb.org/browse/CONPY-178): If a cursor was not properly cleared (all results weren't fetched) the clear\_result routine has to free result sets only if field\_count > 0
* [CONPY-175](https://jira.mariadb.org/browse/CONPY-175): Allocate heap memory for string escaping

## Installation

MariaDB Connector/Python 1.1.0-rc1 can be obtained from central python repository:

```bash
pip3 install --pre mariadb
```

## Changelog

For a list of changes made in this release, with links to detailed information\
on each push, see the [changelog](https://mariadb.com/kb/en/mariadb-connector-python-110-tc1-changelog).

## Links:

* [Documentation](https://mariadb-corporation.github.io/mariadb-connector-python/index.htmli)
* [Bug tracker](https://jira.mariadb.org)
* Sources are hosted on [Github](https://github.com/mariadb-corporation/mariadb-connector-python)

**Do not use non-stable (non-GA) releases in production!**

{% @marketo/form formid="4316" formId="4316" %}
