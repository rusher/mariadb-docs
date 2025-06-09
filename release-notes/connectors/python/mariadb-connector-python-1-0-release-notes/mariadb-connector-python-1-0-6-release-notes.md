# MariaDB Connector/Python 1.0.6 Release Notes

The most recent [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release of MariaDB Connector/Python is:[**MariaDB Connector/Python 1.1.12**](../mariadb-connector-python-1-1-release-notes/mariadb-connector-python-1-1-12-release-notes.md)

[Download](https://mariadb.com/downloads/#connectors)[Release Notes](mariadb-connector-python-1-0-6-release-notes.md)[Changelog](../changelogs/mariadb-connector-python-10-changelogs/mariadb-connector-python-106-changelog.md)[Connector/Python Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/mariadb-connector-python/README.md)

**Release date:** 24 Feb 2021

This is a [_**Stable (GA)**_](../../../mariadb-release-criteria.md) release of the MariaDB\
Connector/Python.

MariaDB Connector/Python enables python programs to access MariaDB and MySQL\
databases, using an API which is compliant with the Python DB API 2.0\
(PEP-249). It is written in C and uses MariaDB Connector/C client library for\
client server communication.

## Bugs Fixed

* [CONC-142](https://jira.mariadb.org/browse/CONC-142): Fixed memory leak in connection class (server\_version\_info)
* [CONC-138](https://jira.mariadb.org/browse/CONC-138), [CONC-141](https://jira.mariadb.org/browse/CONC-141): When using binary protocol, convert data to binary object only if the character set is BINARY (63), not if the flag was set and character set is a non binary character set.
* Various build and travis related corrections/fixes.

## Changelog

For a list of changes made in this release, with links to detailed information\
on each push, see the [changelog](../changelogs/mariadb-connector-python-10-changelogs/mariadb-connector-python-106-changelog.md).
