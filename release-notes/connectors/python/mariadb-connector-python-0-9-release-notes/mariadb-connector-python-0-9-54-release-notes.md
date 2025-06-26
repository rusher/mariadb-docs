# MariaDB Connector/Python 0.9.54-beta Release Notes

The most recent [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release of MariaDB Connector/Python is:[**MariaDB Connector/Python 1.1.12**](../mariadb-connector-python-1-1-release-notes/mariadb-connector-python-1-1-12-release-notes.md)

[Download](https://mariadb.com/downloads/#connectors)[Release Notes](mariadb-connector-python-0-9-54-release-notes.md)[Changelog](../changelogs/mariadb-connector-python-09-changelogs/mariadb-connector-python-0954-changelog.md)[Connector/Python Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-connector-python/README.md)

**Release date:** 18 Feb 2020

This is a [_**beta**_](../../../mariadb-release-criteria.md) release of the MariaDB\
Connector/Python and not intended for production use.

**Do not use&#x20;**_**beta**_**&#x20;releases in production!**

MariaDB Connector/Python enables python programs to access MariaDB and MySQL\
databases, using an API which is compliant with the Python DB API 2.0\
(PEP-249). It is written in C and uses MariaDB Connector/C client library for\
client server communication.

## Notable Updates

* Fixed parameter sequence when creating a xid object
* Added ssl\_capath in connect() method
* [CONPY-40](https://jira.mariadb.org/browse/CONPY-40): ConnectionPool.\_setconfig now accepts only DSN parameters
* [CONPY-35](https://jira.mariadb.org/browse/CONPY-35): Close and reinitialize statement if the cursor was reused with a different SQL statement
* [CONPY-34](https://jira.mariadb.org/browse/CONPY-34): If a python object can't be converted to a corresponding data type, an exception will be raised.
* [CONPY-39](https://jira.mariadb.org/browse/CONPY-39): If no pool\_name was provided, an exception will be raised.
* [CONPY-33](https://jira.mariadb.org/browse/CONPY-33): Segfault when using auto completion in python shell
* [CONPY-37](https://jira.mariadb.org/browse/CONPY-37): Corrected option name: named\_tuple
* [CONPY-36](https://jira.mariadb.org/browse/CONPY-36): connection key word socket was renamed to unix\_socket

## Changelog

For a list of changes made in this release, with links to detailed information\
on each push, see the [changelog](../changelogs/mariadb-connector-python-09-changelogs/mariadb-connector-python-0954-changelog.md).

**Do not use&#x20;**_**beta**_**&#x20;releases in production!**

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
