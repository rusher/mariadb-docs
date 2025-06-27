---
hidden: true
---

# MariaDB Connector/J 3.5.4 Release Notes

<a href="https://mariadb.com/downloads/connectors/connectors-data-access/java8-connector" class="button primary">Download</a>  <a href="mariadb-connector-j-3-5-4-release-notes.md" class="button secondary">Release Notes</a>  <a href="../changelogs/mariadb-connector-j-3-5-changelogs/mariadb-connector-j-3-5-4-changelog.md" class="button secondary">Changelog</a>  <a href="https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-j/about-mariadb-connector-j" class="button secondary">Connector/J Overview</a>

**Release date:** ?? Jun 2025

MariaDB Connector/J 3.5.4 is a [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release.

{% hint style="info" %}
**For an overview of MariaDB Connector/J see the** [**About MariaDB Connector/J**](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-j/about-mariadb-connector-j) **page**
{% endhint %}

## Notable Changes

* Added caching option for loadCodecs results to improve performance ([CONJ-1261](https://jira.mariadb.org/browse/CONJ-1261))
  * Added new option [`cachedCodecs`](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-j/about-mariadb-connector-j#cachedCodecs)

## Bugs Fixed

* Fixed incorrect type definitions in DatabaseMetaData.getTypeInfo() ([CONJ-1234](https://jira.mariadb.org/browse/CONJ-1234))
* Resolved potential race condition that could cause NullPointerException ([CONJ-1247](https://jira.mariadb.org/browse/CONJ-1247)) 
* avoids redundant queries for CallableStatement.getParameterMetaData() ([CONJ-1250](https://jira.mariadb.org/browse/CONJ-1250))
* Fixed SSL configuration issue where zero SSL settings only functioned without explicit SSL configuration ([CONJ-1251](https://jira.mariadb.org/browse/CONJ-1251))
* Resolved GSSAPI authentication error when server exchanges begin with 0x01 byte ([CONJ-1252](https://jira.mariadb.org/browse/CONJ-1252))
* Corrected DatabaseMetadata.getTypeInfo() returning incorrect values for AUTO_INCREMENT, FIXED_PREC_SCALE, and CASE_SENSITIVE fields ([CONJ-1254](https://jira.mariadb.org/browse/CONJ-1254))
* Fixed getString method on BIT(1) fields to properly honor transformedBitIsBoolean configuration ([CONJ-1255](https://jira.mariadb.org/browse/CONJ-1255))
* Enhanced metadata compatibility with MariaDB version 12.0 ([CONJ-1259](https://jira.mariadb.org/browse/CONJ-1259))
* Improved performance of DatabaseMetaData.getExportedKeys method ([CONJ-1260](https://jira.mariadb.org/browse/CONJ-1260))
  * Added new option [`metaExportedKeys`](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-j/about-mariadb-connector-j#metaExportedKeys)`
* Fixed issue to ensure correct catalog name is returned ([CONJ-1256](https://jira.mariadb.org/browse/CONJ-1256))

## Changelog

For a complete list of changes made in MariaDB Connector/J 3.5.4, with links to detailed\
information on each push, see the [changelog](../changelogs/mariadb-connector-j-3-5-changelogs/mariadb-connector-j-3-5-4-changelog.md).

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
