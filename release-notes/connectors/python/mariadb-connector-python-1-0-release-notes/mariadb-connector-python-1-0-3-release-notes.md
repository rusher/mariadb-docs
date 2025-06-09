# MariaDB Connector/Python 1.0.3 Release Notes

The most recent [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release of MariaDB Connector/Python is:[**MariaDB Connector/Python 1.1.12**](../mariadb-connector-python-1-1-release-notes/mariadb-connector-python-1-1-12-release-notes.md)

[Download](https://mariadb.com/downloads/#connectors)[Release Notes](mariadb-connector-python-1-0-3-release-notes.md)[Changelog](../changelogs/mariadb-connector-python-10-changelogs/mariadb-connector-python-103-changelog.md)[Connector/Python Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/mariadb-connector-python/README.md)

**Release date:** 7 October 2020

This is a [_**Stable (GA)**_](../../../mariadb-release-criteria.md) release of the MariaDB\
Connector/Python.

MariaDB Connector/Python enables python programs to access MariaDB and MySQL\
databases, using an API which is compliant with the Python DB API 2.0\
(PEP-249). It is written in C and uses MariaDB Connector/C client library for\
client server communication.

## Notable Changes

* [CONPY-117](https://jira.mariadb.org/browse/CONPY-117): Add converter support: The connect() method now accepts an addtional parameter converter which points to a dictionary, containing one or more conversions. A conversion must be specified in the form {FIELD\_TYPE : conversion\_function}

## Bugs Fixed

* [CONPY-119](https://jira.mariadb.org/browse/CONPY-119): Fixed Memory leak with cursor type dictionary
* Check parameters (execute/executemany) for valid subtypes
* [CONPY-118](https://jira.mariadb.org/browse/CONPY-118): Removed statement allocation from cursor initialization function for text protocol
* Don't set unsigned flag if value will fit into unsigned integer (Workaround for [MDEV-23481](https://jira.mariadb.org/browse/MDEV-23481))
* [CONPY-116](https://jira.mariadb.org/browse/CONPY-116): Wrong type reported for MYSQL\_TYPE\_JSON

## Changelog

For a list of changes made in this release, with links to detailed information\
on each push, see the [changelog](../changelogs/mariadb-connector-python-10-changelogs/mariadb-connector-python-103-changelog.md).
