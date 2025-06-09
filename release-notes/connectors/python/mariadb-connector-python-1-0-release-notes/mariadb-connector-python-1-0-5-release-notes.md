# MariaDB Connector/Python 1.0.5 Release Notes

The most recent [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release of MariaDB Connector/Python is:[**MariaDB Connector/Python 1.1.12**](../mariadb-connector-python-1-1-release-notes/mariadb-connector-python-1-1-12-release-notes.md)

[Download](https://mariadb.com/downloads/#connectors)[Release Notes](mariadb-connector-python-1-0-5-release-notes.md)[Changelog](../changelogs/mariadb-connector-python-10-changelogs/mariadb-connector-python-105-changelog.md)[Connector/Python Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/mariadb-connector-python/README.md)

**Release date:** 25 November 2020

This is a [_**Stable (GA)**_](../../../mariadb-release-criteria.md) release of the MariaDB\
Connector/Python.

MariaDB Connector/Python enables python programs to access MariaDB and MySQL\
databases, using an API which is compliant with the Python DB API 2.0\
(PEP-249). It is written in C and uses MariaDB Connector/C client library for\
client server communication.

## Notable changes:

* [CONPY-127](https://jira.mariadb.org/browse/CONPY-127): When establishing a new database connection the connect method now also supports `None` values instead of strings only.
* [CONPY-128](https://jira.mariadb.org/browse/CONPY-128): Added connection attribute `server_version_info` and (for compatibility) `get_server_version()` method. Both return a tuple, describing the version number of connected server in following format: (`MAJOR_VERSION, MINOR_VERSION, PATCH_VERSION`)
* [CONPY-133](https://jira.mariadb.org/browse/CONPY-133): The internal parser now supports the full [MariaDB comment syntax](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/comment-syntax)

## Bugs Fixed

* [CONPY-126](https://jira.mariadb.org/browse/CONPY-126): Fixed memory leak in connection object
* [CONPY-130](https://jira.mariadb.org/browse/CONPY-130): Fixed DeprecationWarning: builtin type Row has no module attribute
* [CONPY-131](https://jira.mariadb.org/browse/CONPY-131): Fixed crash type\_traverse() called for non-heap type Row (Python 3.6 only)
* [CONPY-132](https://jira.mariadb.org/browse/CONPY-132): Fixed memory leak in connection pool

## Changelog

For a list of changes made in this release, with links to detailed information\
on each push, see the [changelog](../changelogs/mariadb-connector-python-10-changelogs/mariadb-connector-python-105-changelog.md).
