# MariaDB Connector/Python 0.9.58-beta Release Notes

The most recent [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release of MariaDB Connector/Python is:[**MariaDB Connector/Python 1.1.12**](../mariadb-connector-python-1-1-release-notes/mariadb-connector-python-1-1-12-release-notes.md)

[Download](https://mariadb.com/downloads/#connectors)[Release Notes](mariadb-connector-python-0-9-58-release-notes.md)[Changelog](../changelogs/mariadb-connector-python-09-changelogs/mariadb-connector-python-0958-changelog.md)[Connector/Python Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/mariadb-connector-python/README.md)

**Release date:** 6 May 2020

This is a [_**beta**_](../../../mariadb-release-criteria.md) release of the MariaDB\
Connector/Python and not intended for production use.

**Do not use&#x20;**_**beta**_**&#x20;releases in production!**

MariaDB Connector/Python enables python programs to access MariaDB and MySQL\
databases, using an API which is compliant with the Python DB API 2.0\
(PEP-249). It is written in C and uses MariaDB Connector/C client library for\
client server communication.

## Notable Updates

* [CONPY-62](https://jira.mariadb.org/browse/CONPY-62): When using binary protocol (which is forced when using a placeholder), the type NEW\_DECIMAL was ignored and internally converted as string instead of Decimal
* [CONPY-61](https://jira.mariadb.org/browse/CONPY-61): Fixed bug in execute\_many when using NULL values or indicator variables
* [CONPY-59](https://jira.mariadb.org/browse/CONPY-59): Fixed bug when converting invalid date "0000-00-00". Instead of raising an exception it will be converted to None value.
* [CONPY-58](https://jira.mariadb.org/browse/CONPY-58): Fixed parameter error when using paramstype PyFormat.

## Changelog

For a list of changes made in this release, with links to detailed information\
on each push, see the [changelog](../changelogs/mariadb-connector-python-09-changelogs/mariadb-connector-python-0958-changelog.md).

**Do not use&#x20;**_**beta**_**&#x20;releases in production!**

{% @marketo/form formid="4316" formId="4316" %}
