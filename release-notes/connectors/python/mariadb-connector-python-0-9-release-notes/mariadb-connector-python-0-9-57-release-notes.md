# Connector/Python 0.9.57-beta Release Notes

{% include "../../../.gitbook/includes/latest-python.md" %}

<a href="https://mariadb.com/downloads/connectors/connectors-data-access/python-connector/" class="button primary">Download</a> <a href="mariadb-connector-python-0-9-57-release-notes.md" class="button secondary">Release Notes</a> <a href="../changelogs/mariadb-connector-python-09-changelogs/mariadb-connector-python-0957-changelog.md" class="button secondary">Changelog</a> <a href="https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/connectors-quickstart-guides/connector-python-guide" class="button secondary">Connector/Python Overview</a>

**Release date:** 15 Apr 2020

This is a [_**beta**_](../../../mariadb-release-criteria.md) release of MariaDB Connector/Python and not intended for production use.

{% hint style="danger" %}
**Do not use&#x20;**_**beta**_**&#x20;releases in production!**
{% endhint %}

MariaDB Connector/Python enables python programs to access MariaDB and MySQL databases, using an API which is compliant with the Python DB API 2.0 (PEP-249). It is written in C and uses MariaDB Connector/C client library for client server communication.

## Notable Updates

* Build: Posix builds don't link statically against Connector/C anymore.
* [CONPY-53](https://jira.mariadb.org/browse/CONPY-53): Allow empty parameter sequence in execute() method
* [CONPY-56](https://jira.mariadb.org/browse/CONPY-56): Support dictionary option in cursor: Added anoptional boolean parameter 'dictionary' for cursor class. When dictionary parameter was set to true, the fetch operations will return rows from result set as Dict.
* [CONPY-55](https://jira.mariadb.org/browse/CONPY-55): Fixed memory leak when opening/closing cursor.

## Changelog

For a list of changes made in this release, with links to detailed information\
on each push, see the [changelog](../changelogs/mariadb-connector-python-09-changelogs/mariadb-connector-python-0957-changelog.md).

**Do not use&#x20;**_**beta**_**&#x20;releases in production!**

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
