# Connector/J 1.5.4 Release Notes

{% include "../../../.gitbook/includes/latest-java.md" %}

[Download](https://downloads.mariadb.org/connector-java/1.5.4/)[Release Notes](mariadb-connector-j-154-release-notes.md)[Changelog](../changelogs/1.5/mariadb-connector-j-154-changelog.md)[Connector/J Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-j/README.md)

**Release date:** 13 Oct 2016

MariaDB Connector/J 1.5.4 is a [_**Stable**_](../../../community-server/about/release-criteria.md) _**(GA)**_\
release.

**For an overview of MariaDB Connector/J see the**[**About MariaDB Connector/J**](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-j/README.md) **page**

## Notable Changes

This version is a bug-fix release.

* [CONJ-363](https://jira.mariadb.org/browse/CONJ-363) : Connection.getClientInfo implementation correction to follow JDBC rules
* [CONJ-361](https://jira.mariadb.org/browse/CONJ-361) : PrepareStatement setString() with empty string correction.
* [CONJ-360](https://jira.mariadb.org/browse/CONJ-360) : replacing ManagementFactory.getRuntimeMXBean() that cause Connection timeout issue due to DNS lookup depending on environment
* [CONJ-359](https://jira.mariadb.org/browse/CONJ-359) : Metadata getColumns(...) resultSet doesnt have "IS\_GENERATEDCOLUMN" info

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
