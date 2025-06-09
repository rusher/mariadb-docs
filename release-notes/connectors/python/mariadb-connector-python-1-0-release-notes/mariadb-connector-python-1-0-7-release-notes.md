# MariaDB Connector/Python 1.0.7 Release Notes

The most recent [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release of MariaDB Connector/Python is:[**MariaDB Connector/Python 1.1.12**](../mariadb-connector-python-1-1-release-notes/mariadb-connector-python-1-1-12-release-notes.md)

[Download](https://mariadb.com/downloads/#connectors)[Release Notes](mariadb-connector-python-1-0-7-release-notes.md)[Changelog](../changelogs/mariadb-connector-python-10-changelogs/mariadb-connector-python-107-changelog.md)[Connector/Python Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/mariadb-connector-python/README.md)

**Release date:** 8 Jun 2021

This is a [_**Stable (GA)**_](../../../mariadb-release-criteria.md) release of the MariaDB\
Connector/Python.

MariaDB Connector/Python enables python programs to access MariaDB and MySQL\
databases, using an API which is compliant with the Python DB API 2.0\
(PEP-249). It is written in C and uses MariaDB Connector/C client library for\
client server communication.

## Bugs Fixed

* [CONPY-155](https://jira.mariadb.org/browse/CONPY-155): fixed crash in get\_server\_version method of connection class
* [CONPY-144](https://jira.mariadb.org/browse/CONPY-144): fixed crash in connection pool
* [CONPY-150](https://jira.mariadb.org/browse/CONPY-150): convert invalid date types (day, month or year=0) to NULL

## Changelog

For a list of changes made in this release, with links to detailed information\
on each push, see the [changelog](../changelogs/mariadb-connector-python-10-changelogs/mariadb-connector-python-107-changelog.md).
