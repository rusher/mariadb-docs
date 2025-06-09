# MariaDB Connector/J 2.1.2 Release Notes

[Download](https://downloads.mariadb.org/connector-java/2.1.2/)[Release Notes](mariadb-connector-j-212-release-notes.md)[Changelog](../changelogs/mariadb-connector-j-21-changelogs/mariadb-connector-j-212-changelog.md)[Connector/J Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-j/README.md)

**Release date:** 26 Sep 2017

MariaDB Connector/J 2.1.2 is a [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_\
release.

**For an overview of MariaDB Connector/J see the**[**About MariaDB Connector/J**](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-j/README.md) **page**

### Bug

* \[[CONJ-525](https://jira.mariadb.org/browse/CONJ-525)] Batch result-set return array correction when DELETE statement when bulk option is used
* \[[CONJ-526](https://jira.mariadb.org/browse/CONJ-526)] better error message getting metadata information when SQL syntax is wrong
* \[[CONJ-527](https://jira.mariadb.org/browse/CONJ-527)] Resultset.last() return wrong value if resultset has only one result
* \[[CONJ-528](https://jira.mariadb.org/browse/CONJ-528)] Error executing LOAD DATA LOCAL INFILE when file is larger than max\_allowed\_packet

### Misc

* ensuring Connection.isValid(timeout) always respect timeout value

Be notified of new MariaDB Server releases automatically by [subscribing](https://lists.mariadb.org/postorius/lists/announce.lists.mariadb.org/) to the MariaDB Foundation community announce 'at' lists.mariadb.org announcement list (this is a low traffic, announce-only list). MariaDB plc customers will be notified for all new releases, security issues and critical bug fixes for all MariaDB plc products thanks to the Notification Services.

MariaDB may already be included in your favorite OS distribution. More\
information can be found on the[Distributions which Include MariaDB](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/readme-1)\
page.
