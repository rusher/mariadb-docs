# MariaDB Connector/J 2.6.1 Release Notes

The most recent [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release of [MariaDB Connector/J](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-j/README.md) is:[**MariaDB Connector/J 3.5.3**](../mariadb-connector-j-3-5-release-notes/mariadb-connector-j-3-5-3-release-notes.md)

[Download](https://mariadb.com/downloads/#connectors)[Release Notes](mariadb-connector-j-261-release-notes.md)[Changelog](../changelogs/mariadb-connector-j-26-changelogs/mariadb-connector-j-261-changelog.md)[Connector/J Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-j/README.md)

**Release date:** 23 Jun 2020

MariaDB Connector/J 2.6.1 is a [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release.

**For an overview of MariaDB Connector/J see the**[**About MariaDB Connector/J**](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-j/README.md) **page**

## Notable Updates

* [CONJ-781](https://jira.mariadb.org/browse/CONJ-781) - DatabaseMetaData.supportsMultipleResultSets() now return correctly true.
* [CONJ-791](https://jira.mariadb.org/browse/CONJ-791) - Using CallableStatement.getTimestamp() can't get data correctly
* [CONJ-705](https://jira.mariadb.org/browse/CONJ-705) - ParameterMetadata now return parameterCount() even if no information
* [CONJ-775](https://jira.mariadb.org/browse/CONJ-775) - avoid a NPE for malformed "jdbc:mariadb:/" connection string.
* [CONJ-776](https://jira.mariadb.org/browse/CONJ-776) - Temporal Data Tables are not listed in metadata
* [CONJ-785](https://jira.mariadb.org/browse/CONJ-785) - corrected escape sequence for multiple backslash escape
* [CONJ-786](https://jira.mariadb.org/browse/CONJ-786) - Connection.setReadOnly(true ) with option `assureReadOnly` now force read only connection even for mono server\*
* [CONJ-795](https://jira.mariadb.org/browse/CONJ-795) - permit resultset.getRow() for TYPE\_FORWARD\_ONLY when streaming
* [CONJ-797](https://jira.mariadb.org/browse/CONJ-797) - Connector set UTF8mb4 equivalent in case of server configured with UTF8mb3 collation
* [CONJ-800](https://jira.mariadb.org/browse/CONJ-800) - implement Statement setEscapeProcessing to avoid escape
* [CONJ-801](https://jira.mariadb.org/browse/CONJ-801) - possible race condition using resultset getter using label
* [CONJ-778](https://jira.mariadb.org/browse/CONJ-778) - Missing import org.osgi.service.jdbc in Import-Package clause of the OSGi manifest
* [CONJ-779](https://jira.mariadb.org/browse/CONJ-779) - Logic error in stop() method of OSGi bundle activator
* [CONJ-780](https://jira.mariadb.org/browse/CONJ-780) - Logic error in implementation of OSGi DataSourceFactory (MariaDbDataSourceFactory)
* [CONJ-788](https://jira.mariadb.org/browse/CONJ-788) - resultset metadata always indicate that column is writable even if not
* [CONJ-789](https://jira.mariadb.org/browse/CONJ-789) - ensure connection reference removal on (prepared)Statement close
* [CONJ-782](https://jira.mariadb.org/browse/CONJ-782) - SkySQL testing

## Changelog

For a complete list of changes made in MariaDB Connector/J 2.6.1, with links to detailed\
information on each push, see the [changelog](../changelogs/mariadb-connector-j-26-changelogs/mariadb-connector-j-261-changelog.md).

Be notified of new MariaDB Server releases automatically by [subscribing](https://lists.mariadb.org/postorius/lists/announce.lists.mariadb.org/) to the MariaDB Foundation community announce 'at' lists.mariadb.org announcement list (this is a low traffic, announce-only list). MariaDB plc customers will be notified for all new releases, security issues and critical bug fixes for all MariaDB plc products thanks to the Notification Services.

MariaDB may already be included in your favorite OS distribution. More\
information can be found on the[Distributions which Include MariaDB](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/readme-1)\
page.
