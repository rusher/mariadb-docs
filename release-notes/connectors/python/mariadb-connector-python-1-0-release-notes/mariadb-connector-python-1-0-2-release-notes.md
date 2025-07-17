# Connector/Python 1.0.2 Release Notes

{% include "../../../.gitbook/includes/latest-python.md" %}

<a href="https://mariadb.com/downloads/connectors/connectors-data-access/python-connector/" class="button primary">Download</a> <a href="mariadb-connector-python-1-0-2-release-notes.md" class="button secondary">Release Notes</a> <a href="../changelogs/mariadb-connector-python-10-changelogs/mariadb-connector-python-102-changelog.md" class="button secondary">Changelog</a> <a href="https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/connectors-quickstart-guides/connector-python-guide" class="button secondary">Connector/Python Overview</a>

**Release date:** 18 Sep 2020

This is a [_**Stable (GA)**_](../../../community-server/about/release-criteria.md) release of MariaDB Connector/Python.

MariaDB Connector/Python enables python programs to access MariaDB and MySQL databases, using an API which is compliant with the Python DB API 2.0 (PEP-249). It is written in C and uses MariaDB Connector/C client library for client server communication.

## Notable Updates

* [CONPY-110](https://jira.mariadb.org/browse/CONPY-110): Fixed memory overrun when passing ssl keyword in connect parameters
* [CONPY-108](https://jira.mariadb.org/browse/CONPY-108): Fixed memory leak
* Fixed DateTime API initialization: Initialize only once per object

## Changelog

For a list of changes made in this release, with links to detailed information\
on each push, see the [changelog](../changelogs/mariadb-connector-python-10-changelogs/mariadb-connector-python-102-changelog.md).

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
