# MariaDB Connector/Python 1.0.4 Release Notes

The most recent [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release of MariaDB Connector/Python is:[**MariaDB Connector/Python 1.1.12**](../mariadb-connector-python-1-1-release-notes/mariadb-connector-python-1-1-12-release-notes.md)

[Download](https://mariadb.com/downloads/#connectors)[Release Notes](mariadb-connector-python-1-0-4-release-notes.md)[Changelog](../changelogs/mariadb-connector-python-10-changelogs/mariadb-connector-python-104-changelog.md)[Connector/Python Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/mariadb-connector-python/README.md)

**Release date:** 20 October 2020

This is a [_**Stable (GA)**_](../../../mariadb-release-criteria.md) release of the MariaDB\
Connector/Python.

MariaDB Connector/Python enables python programs to access MariaDB and MySQL\
databases, using an API which is compliant with the Python DB API 2.0\
(PEP-249). It is written in C and uses MariaDB Connector/C client library for\
client server communication.

## Notable Changes

Python 3.9 wheel packages for Windows are now available on pypi.org

## Bugs Fixed

* [CONPY-123](https://jira.mariadb.org/browse/CONPY-123): Free pending resultsets when closing cursor
* [CONPY-124](https://jira.mariadb.org/browse/CONPY-124): Fix build when using Connector/C < 3.1.8
* [CONPY-125](https://jira.mariadb.org/browse/CONPY-125): Build fix: replaced obsolete ULONG\_LONG\_MAX definitions

## Changelog

For a list of changes made in this release, with links to detailed information\
on each push, see the [changelog](../changelogs/mariadb-connector-python-10-changelogs/mariadb-connector-python-104-changelog.md).
