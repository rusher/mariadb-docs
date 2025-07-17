# Connector/Python 1.0.6 Release Notes

{% include "../../../.gitbook/includes/latest-python.md" %}

<a href="https://mariadb.com/downloads/connectors/connectors-data-access/python-connector/" class="button primary">Download</a> <a href="mariadb-connector-python-1-0-6-release-notes.md" class="button secondary">Release Notes</a> <a href="../changelogs/mariadb-connector-python-10-changelogs/mariadb-connector-python-106-changelog.md" class="button secondary">Changelog</a> <a href="https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/connectors-quickstart-guides/connector-python-guide" class="button secondary">Connector/Python Overview</a>

**Release date:** 24 Feb 2021

This is a [_**Stable (GA)**_](../../../community-server/about/release-criteria.md) release of MariaDB Connector/Python.

MariaDB Connector/Python enables python programs to access MariaDB and MySQL databases, using an API which is compliant with the Python DB API 2.0 (PEP-249). It is written in C and uses MariaDB Connector/C client library for client server communication.

## Bugs Fixed

* [CONC-142](https://jira.mariadb.org/browse/CONC-142): Fixed memory leak in connection class (server\_version\_info)
* [CONC-138](https://jira.mariadb.org/browse/CONC-138), [CONC-141](https://jira.mariadb.org/browse/CONC-141): When using binary protocol, convert data to binary object only if the character set is BINARY (63), not if the flag was set and character set is a non binary character set.
* Various build and travis related corrections/fixes.

## Changelog

For a list of changes made in this release, with links to detailed information\
on each push, see the [changelog](../changelogs/mariadb-connector-python-10-changelogs/mariadb-connector-python-106-changelog.md).

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
