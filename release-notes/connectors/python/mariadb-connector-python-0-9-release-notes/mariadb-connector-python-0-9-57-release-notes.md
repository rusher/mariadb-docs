# MariaDB Connector/Python 0.9.57-beta Release Notes

The most recent [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release of MariaDB Connector/Python is:[**MariaDB Connector/Python 1.1.12**](../mariadb-connector-python-1-1-release-notes/mariadb-connector-python-1-1-12-release-notes.md)

[Download](https://mariadb.com/downloads/#connectors)[Release Notes](mariadb-connector-python-0-9-57-release-notes.md)[Changelog](../changelogs/mariadb-connector-python-09-changelogs/mariadb-connector-python-0957-changelog.md)[Connector/Python Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-connector-python/README.md)

**Release date:** 15 Apr 2020

This is a [_**beta**_](../../../mariadb-release-criteria.md) release of the MariaDB\
Connector/Python and not intended for production use.

**Do not use&#x20;**_**beta**_**&#x20;releases in production!**

MariaDB Connector/Python enables python programs to access MariaDB and MySQL\
databases, using an API which is compliant with the Python DB API 2.0\
(PEP-249). It is written in C and uses MariaDB Connector/C client library for\
client server communication.

## Notable Updates

* Build: Posix builds don't link statically against Connector/C anymore.
* [CONPY-53](https://jira.mariadb.org/browse/CONPY-53): Allow empty parameter sequence in execute() method
* [CONPY-56](https://jira.mariadb.org/browse/CONPY-56): Support dictionary option in cursor: Added anoptional boolean parameter 'dictionary' for cursor class. When dictionary parameter was set to true, the fetch operations will return rows from result set as Dict.
* [CONPY-55](https://jira.mariadb.org/browse/CONPY-55): Fixed memory leak when opening/closing cursor.

## Changelog

For a list of changes made in this release, with links to detailed information\
on each push, see the [changelog](../changelogs/mariadb-connector-python-09-changelogs/mariadb-connector-python-0957-changelog.md).

**Do not use&#x20;**_**beta**_**&#x20;releases in production!**

{% @marketo/form formid="4316" formId="4316" %}
