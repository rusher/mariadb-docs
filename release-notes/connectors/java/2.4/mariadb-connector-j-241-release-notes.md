# Connector/J 2.4.1 Release Notes

{% include "../../../.gitbook/includes/latest-java.md" %}

[Download](https://downloads.mariadb.com/Connectors/java/connector-java-2.4.1/)[Release Notes](mariadb-connector-j-241-release-notes.md)[Changelog](../changelogs/2.4/mariadb-connector-j-241-changelog.md)[Connector/J Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-j/README.md)

**Release date:** 18 Mar 2019

MariaDB Connector/J 2.4.1 is a [_**Stable**_](../../../community-server/about/release-criteria.md) _**(GA)**_\
release.

**For an overview of MariaDB Connector/J see the**[**About MariaDB Connector/J**](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-j/README.md) **page**

### Evolutions

* \[misc] enabled running of 'SHOW ENGINE INNODB STATUS' for error code 1213 (@mtykhenko)
* \[misc] reduce mutex using select @@innodb\_read\_only for aurora (@matsuzayaws)

### Bugs

* \[misc] updating checkstyle version dependency
* \[misc] permit using SSL on localsocket
* \[misc] java PID using java 9 ProcessHandle if existing, relying on JNA if present
* [CONJ-687](https://jira.mariadb.org/browse/CONJ-687): addition of option "useMysqlMetadata" to permit MySQL meta compatibility
* [CONJ-682](https://jira.mariadb.org/browse/CONJ-682): internal pool correction: when receiving an RST during connection validation, the pool will end up throwing connection timeout exception in place of reusing another connection.

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
