# MariaDB Connector/Python 1.1.12 Release Notes

[Download](https://mariadb.com/downloads/connectors/connectors-data-access/python-connector/)[Release Notes](mariadb-connector-python-1-1-12-release-notes.md)[Changelog](../changelogs/mariadb-connector-python-11-changelogs/mariadb-connector-python-1-1-12-changelog.md)[Connector/Python Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-connector-python/README.md)

**Release date:** 24 Feb 2025

This is a [_**stable**_](../../../mariadb-release-criteria.md) release of the MariaDB\
Connector/Python.

**For a description of this library see the**[**MariaDB Connector/Python documentation**](https://mariadb-corporation.github.io/mariadb-connector-python/index.html) **.**

MariaDB Connector/Python enables python programs to access MariaDB and MySQL databases, using an API which is compliant with the Python DB API 2.0 (PEP-249). It is written in C and uses MariaDB Connector/C client library for client server communication.

## Notable changes

* [CONPY-299](https://jira.mariadb.org/browse/CONPY-299): Added support for VECTOR: Vectors can be directly used in parameters as float arrays without using tobytes() method or SQL Function Vec\_FromText()

## Bug fixes

* [CONPY-295](https://jira.mariadb.org/browse/CONPY-295): Fix unsigned check when using executemany() method
* [CONPY-300](https://jira.mariadb.org/browse/CONPY-300): Documentation fix (ConnectionPool)
* [CONPY-302](https://jira.mariadb.org/browse/CONPY-302): Fix segfault when using threads()
* Fixed exception type for ER\_BAD\_FIELD\_ERROR (now OperationalError instead of ProgrammingError)

## Installation

MariaDB Connector/Python 1.1.12 can be obtained from central python repository:

```bash
pip3 install mariadb
```

or to upgrade to the most recent version

```bash
pip3 install --upgrade mariadb
```

## Changelog

For a list of changes made in this release, with links to detailed information\
on each push, see the [changelog](../changelogs/mariadb-connector-python-11-changelogs/mariadb-connector-python-1-1-12-changelog.md).

## Links:

* [Documentation](https://mariadb-corporation.github.io/mariadb-connector-python/index.htmli)
* [Bug tracker](https://jira.mariadb.org)
* Sources are hosted on [Github](https://github.com/mariadb-corporation/mariadb-connector-python)
