# MariaDB Connector/Python 1.0.1 Release Notes

The most recent [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release of MariaDB Connector/Python is:[**MariaDB Connector/Python 1.1.12**](../mariadb-connector-python-1-1-release-notes/mariadb-connector-python-1-1-12-release-notes.md)

[Download](https://mariadb.com/downloads/#connectors)[Release Notes](mariadb-connector-python-1-0-1-release-notes.md)[Changelog](../changelogs/mariadb-connector-python-10-changelogs/mariadb-connector-python-101-changelog.md)[Connector/Python Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/mariadb-connector-python/README.md)

**Release date:** 18 August 2020

This is a [_**Stable (GA)**_](../../../mariadb-release-criteria.md) release of the MariaDB\
Connector/Python.

MariaDB Connector/Python enables python programs to access MariaDB and MySQL\
databases, using an API which is compliant with the Python DB API 2.0\
(PEP-249). It is written in C and uses MariaDB Connector/C client library for\
client server communication.

## Notable Updates

* [CONPY-107](https://jira.mariadb.org/browse/CONPY-107): Negative time values are now converted to datetime.timedelta
* [CONPY-106](https://jira.mariadb.org/browse/CONPY-106): Exception types are choosen now by error number instead of SQL state.
* [CONPY-105](https://jira.mariadb.org/browse/CONPY-105): Changed behavior of rowcount and lastrowid to be conformant with PEP-249
* [CONPY-102](https://jira.mariadb.org/browse/CONPY-102): Autocommit is set OFF by default. Added an option autocommit for connect() method.
* [CONPY-101](https://jira.mariadb.org/browse/CONPY-101): Fixed negative reference count in cursor.callproc()
* [CONPY-100](https://jira.mariadb.org/browse/CONPY-100): Added binary option for cursor, which allows to use binary protocol without passing parameters
* [CONPY-99](https://jira.mariadb.org/browse/CONPY-99): Fixed memory leak in fetchall()
* [CONPY-98](https://jira.mariadb.org/browse/CONPY-98): CAST AS BINARY doesn't return binary object
* [CONPY-95](https://jira.mariadb.org/browse/CONPY-95): Added support for MYSQL\_TYPE\_BIT
* [CONPY-94](https://jira.mariadb.org/browse/CONPY-94): Added missing support for subtypes of Python Classes
* [CONPY-93](https://jira.mariadb.org/browse/CONPY-93): Python memory allocation without holding the GIL
* [CONPY-85](https://jira.mariadb.org/browse/CONPY-85): Fixed version checking of Connector/C in setup routine
* [CONPY-83](https://jira.mariadb.org/browse/CONPY-83): Added missing reference incrementing in ConnectionPool
* [CONPY-82](https://jira.mariadb.org/browse/CONPY-82): Unlock mutex, if the attempt to add a new connection to connection pool fails

## Changelog

For a list of changes made in this release, with links to detailed information\
on each push, see the [changelog](../changelogs/mariadb-connector-python-10-changelogs/mariadb-connector-python-101-changelog.md).
