# MariaDB Connector/J 1.7.6 Release Notes

{% include "../../../.gitbook/includes/latest-java.md" %}

[Download](https://downloads.mariadb.org/connector-java/1.7.6/)[Release Notes](mariadb-connector-j-176-release-notes.md)[Changelog](../changelogs/1.7/mariadb-connector-j-176-changelog.md)[Connector/J Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-j/README.md)

**Release date:** 10 Dec 2020

MariaDB Connector/J 1.7.6 is a [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_\
release.

**For an overview of MariaDB Connector/J see the**[**About MariaDB Connector/J**](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-j/README.md) **page**

Reporting correction/contribution to java 7 supported version

## Bugs Fixed

* [CONJ-682](https://jira.mariadb.org/browse/CONJ-682) : When receiving an RST during connection validation, the pool will end up throwing a connection timeout exception in place of reusing another connection.
* [CONJ-522](https://jira.mariadb.org/browse/CONJ-522) : When using multiple pools and a pool is closed, it closes a global executor used by all pools. This occurs even if there are still other pools open.
* [CONJ-750](https://jira.mariadb.org/browse/CONJ-750) : protocol error when not setting database, indicating null authentication plugin
* [CONJ-639](https://jira.mariadb.org/browse/CONJ-639) : enabledSslProtocolSuites does not include TLSv1.2 by default

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
