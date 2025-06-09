# MariaDB Connector/Python 1.0.10 Release Notes

The most recent [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release of MariaDB Connector/Python is:[**MariaDB Connector/Python 1.1.12**](../mariadb-connector-python-1-1-release-notes/mariadb-connector-python-1-1-12-release-notes.md)

[Download](https://mariadb.com/downloads/connectors/connectors-data-access/python-connector/)[Release Notes](mariadb-connector-python-1-0-10-release-notes.md)[Changelog](../changelogs/mariadb-connector-python-10-changelogs/mariadb-connector-python-1010-changelog.md)[Connector/Python Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-connector-python/README.md)

**Release date:** 18 Feb 2022

This is a [_**Stable (GA)**_](../../../mariadb-release-criteria.md) release of the MariaDB\
Connector/Python.

MariaDB Connector/Python enables python programs to access MariaDB and MySQL\
databases, using an API which is compliant with the Python DB API 2.0\
(PEP-249). It is written in C and uses MariaDB Connector/C client library for\
client server communication.

## Bugs Fixed

* [CONPY-193](https://jira.mariadb.org/browse/CONPY-193): Fixed fallback for bulk execution (executemany) when connected to non MariaDB database servers.
* [CONPY-188](https://jira.mariadb.org/browse/CONPY-188): If a connection or cursor is closed, an exception is returned whether a method or property of a closed object is called

## Changelog

For a list of changes made in this release, with links to detailed information\
on each push, see the [changelog](../changelogs/mariadb-connector-python-10-changelogs/mariadb-connector-python-1010-changelog.md).
