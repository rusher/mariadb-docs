# MariaDB Connector/J 2.1.1 Release Notes

[Download](https://downloads.mariadb.org/connector-java/2.1.1/)[Release Notes](mariadb-connector-j-211-release-notes.md)[Changelog](../changelogs/mariadb-connector-j-21-changelogs/mariadb-connector-j-211-changelog.md)[Connector/J Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-j/README.md)

**Release date:** 6 Sep 2017

MariaDB Connector/J 2.1.1 is a [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_\
release.

**For an overview of MariaDB Connector/J see the**[**About MariaDB Connector/J**](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-j/README.md) **page**

### Bug

* \[[CONJ-519](https://jira.mariadb.org/browse/CONJ-519)] Updatable result-set possible NPE when same field is repeated.
* \[[CONJ-514](https://jira.mariadb.org/browse/CONJ-514)] ResultSet method wasNull() always return true after a call on a "null-date" field binary protocol handling
* \[[CONJ-516](https://jira.mariadb.org/browse/CONJ-516)] Permit using updatable result-set when fetching
* \[[CONJ-511](https://jira.mariadb.org/browse/CONJ-511)] Add legacy SSL certificate Hostname verification with CN even when SAN are set
* \[[CONJ-515](https://jira.mariadb.org/browse/CONJ-515)] Improve MariaDB driver stability in case JNA errors

### Misc

* correct typo in error message when setting wrong parameter
* add trace to HostnameVerifier implementation
* handling connection error when no database is provided

Be notified of new MariaDB Server releases automatically by [subscribing](https://lists.mariadb.org/postorius/lists/announce.lists.mariadb.org/) to the MariaDB Foundation community announce 'at' lists.mariadb.org announcement list (this is a low traffic, announce-only list). MariaDB plc customers will be notified for all new releases, security issues and critical bug fixes for all MariaDB plc products thanks to the Notification Services.

MariaDB may already be included in your favorite OS distribution. More\
information can be found on the[Distributions which Include MariaDB](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/readme-1)\
page.
