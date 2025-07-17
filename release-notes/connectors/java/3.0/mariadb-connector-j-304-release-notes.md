# Connector/J 3.0.4 Release Notes

{% include "../../../.gitbook/includes/latest-java.md" %}

[Download](https://mariadb.com/downloads/#connectors)[Release Notes](mariadb-connector-j-304-release-notes.md)[Changelog](../changelogs/3.0/mariadb-connector-j-304-changelog.md)[Connector/J Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-j/README.md)

**Release date:** 25 Mar 2022

MariaDB Connector/J 3.0.4 is a [_**Stable**_](../../../community-server/about/release-criteria.md) _**(GA)**_ release.

**For an overview of MariaDB Connector/J see the**[**About MariaDB Connector/J**](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-j/README.md) **page**

### Bugs Fixed

* [CONJ-921](https://jira.mariadb.org/browse/CONJ-921) DatabaseMetadata#getTables throws a syntax error if a NULL value is used for tableNamePattern
* [CONJ-922](https://jira.mariadb.org/browse/CONJ-922) A DECIMAL overflow for long/int/short is not throwing an exception
* [CONJ-924](https://jira.mariadb.org/browse/CONJ-924) A NULL value returned for a column can result in java.lang.IllegalArgumentException: Unexpected data type NULL
* [CONJ-926](https://jira.mariadb.org/browse/CONJ-926) The authentication is restricted to the methods 'mysql\_native\_password,client\_ed25519,auth\_gssapi\_client' instead of allowing all supported methods, if the option restrictedAuth is not set (default NULL).
* [CONJ-923](https://jira.mariadb.org/browse/CONJ-923) 32 bit value returned instead of a 64 bit value for generated id / updated rows
* [CONJ-933](https://jira.mariadb.org/browse/CONJ-933) When the load-balancing HA mode is used a host is not used anymore after a connection failed, even if a connection would be possible again.
* [CONJ-935](https://jira.mariadb.org/browse/CONJ-935) Connection.getMetaData() returns values of type MariaDbClob instead of the expected type String
* [CONJ-937](https://jira.mariadb.org/browse/CONJ-937) metadata.getColumnTypeName() returns the values with a wrong types
* [CONJ-934](https://jira.mariadb.org/browse/CONJ-934) A connection fails if the password is set before the username for MariaDbDataSource
* [CONJ-932](https://jira.mariadb.org/browse/CONJ-932) The login packet has non-standard length information for the attributes, which can result in issues when using wireshark.
* [CONJ-945](https://jira.mariadb.org/browse/CONJ-945) When using failover the definition of retriesAllDown is ignored when trying to reconnect
* [CONJ-940](https://jira.mariadb.org/browse/CONJ-940) Updates of rows is not possible for storage engines which do not provide the metadata information for primary columns

### Install and Upgrade

* [CONJ-925](https://jira.mariadb.org/browse/CONJ-925) missing OSGI metadata is missing

## Changelog

For a complete list of changes made in MariaDB Connector/J 3.0.4, with links to detailed\
information on each push, see the [changelog](../changelogs/3.0/mariadb-connector-j-304-changelog.md).

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
