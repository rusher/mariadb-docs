# MariaDB Connector/J 1.4.1 Release Notes

{% include "../../../.gitbook/includes/latest-java.md" %}

[Download](https://downloads.mariadb.org/connector-java/1.4.1/)[Release Notes](mariadb-connector-j-141-release-notes.md)[Changelog](../changelogs/1.4/mariadb-connector-j-141-changelog.md)[Connector/J Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-j/README.md)

**Release date:** 11 Apr 2016

**An issue was reported as a "Blocker" in this version. Please use the corrected version 1.4.3.**\
Issue resolution in MariaDB is visible through the corresponding ticket in MariaDB’s tracking system (JIRA): [CONJ-284](https://jira.mariadb.org/browse/CONJ-284)

**For a description of MariaDB Connector/J see the**[**About MariaDB Connector/J**](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-j/README.md) **page**

## Notable Changes

This version is a bugfix release.

* [CONJ-274](https://jira.mariadb.org/browse/CONJ-274) correction to permit connections to MySQL 5.1 server
* [CONJ-273](https://jira.mariadb.org/browse/CONJ-273) correction when using prepareStatement without parameters and option rewriteBatchedStatements to true
* [CONJ-270](https://jira.mariadb.org/browse/CONJ-270) permit 65535 parameters to server preparedStatement
* [CONJ-268](https://jira.mariadb.org/browse/CONJ-268) update license header
* when the option rewriteBatchedStatements is set to true, correction of packet separation when query size > max\_allow\_packet
* performance improvement for select result

## Changelog

For a list of all changes made in this release, with links to detailed\
information on each push, see the[changelog](../changelogs/1.4/mariadb-connector-j-141-changelog.md).

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
