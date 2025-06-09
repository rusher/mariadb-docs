# MariaDB Connector/Python 0.9.56 beta Release Notes

The most recent [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release of MariaDB Connector/Python is:[**MariaDB Connector/Python 1.1.12**](../mariadb-connector-python-1-1-release-notes/mariadb-connector-python-1-1-12-release-notes.md)

[Download](https://mariadb.com/downloads/#connectors)[Release Notes](mariadb-connector-python-0-9-56-release-notes.md)[Changelog](../changelogs/mariadb-connector-python-09-changelogs/mariadb-connector-python-0956-changelog.md)[Connector/Python Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/mariadb-connector-python/README.md)

**Release date:** 6 Apr 2020

This is a [_**beta**_](../../../mariadb-release-criteria.md) release of the MariaDB\
Connector/Python and not intended for production use.

**Do not use&#x20;**_**beta**_**&#x20;releases in production!**

MariaDB Connector/Python enables python programs to access MariaDB and MySQL\
databases, using an API which is compliant with the Python DB API 2.0\
(PEP-249). It is written in C and uses MariaDB Connector/C client library for\
client server communication.

## Notable Updates

* [CONPY-46](https://jira.mariadb.org/browse/CONPY-46): Implemented `__enter__()` and `__exit__()` methods for with statement (PEP-343). These methods are available now for connection and cursor class.
* [CONPY-47](https://jira.mariadb.org/browse/CONPY-47): When sending parameters PyBool\_Type wasn't supported. In case a boolean type (True/False) will be provided as a parameter, it will be converted to a tinyint (MYSQL\_TYPE\_TINY).
* [CONPY-48](https://jira.mariadb.org/browse/CONPY-48): Accept List of parameters for execute() method
* [CONPY-49](https://jira.mariadb.org/browse/CONPY-49): Added support for Decimal type
  * When retrieving data with column type MYSQL\_TYPE\_NEWDECIMAL Connector/Python now loads the decimal module and converts data from string into Pythons decimal.Decimal type.
  * Wnen sending a decimal.Decimal parameter, value will be converted to string and send with type MYSQL\_TYPE\_NEWDECIMAL to server.
* [CONPY-51](https://jira.mariadb.org/browse/CONPY-51): Store field\_count internelly for buffered cursors to prevent overriding/clearing the value by connection methods which directly send commands to database server.
* [CONPY-52](https://jira.mariadb.org/browse/CONPY-52): Fixed double free of resultset.

## Changelog

For a list of changes made in this release, with links to detailed information\
on each push, see the [changelog](../changelogs/mariadb-connector-python-09-changelogs/mariadb-connector-python-0956-changelog.md).

**Do not use&#x20;**_**beta**_**&#x20;releases in production!**

{% @marketo/form formid="4316" formId="4316" %}
