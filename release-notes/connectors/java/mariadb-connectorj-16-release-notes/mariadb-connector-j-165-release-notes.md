# MariaDB Connector/J 1.6.5 Release Notes

The most recent [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release of [MariaDB Connector/J](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-j/README.md) is:[**MariaDB Connector/J 3.5.3**](../mariadb-connector-j-3-5-release-notes/mariadb-connector-j-3-5-3-release-notes.md)

[Download](https://downloads.mariadb.org/connector-java/1.6.5/)[Release Notes](mariadb-connector-j-165-release-notes.md)[Changelog](../changelogs/mariadb-connector-j-16-changelogs/mariadb-connector-j-165-changelog.md)[Connector/J Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-j/README.md)

**Release date:** 26 Sep 2017

MariaDB Connector/J 1.6.5 is a [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_\
release compatible with java 6, 7, 8.

**For an overview of MariaDB Connector/J see the**[**About MariaDB Connector/J**](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-j/README.md) **page**

### Bug

* \[[CONJ-525](https://jira.mariadb.org/browse/CONJ-525)] Batch result-set return array correction when DELETE statement when bulk option is used
* \[[CONJ-526](https://jira.mariadb.org/browse/CONJ-526)] better error message getting metadata information when SQL syntax is wrong
* \[[CONJ-527](https://jira.mariadb.org/browse/CONJ-527)] Resultset.last() return wrong value if resultset has only one result
* \[[CONJ-528](https://jira.mariadb.org/browse/CONJ-528)] Error executing LOAD DATA LOCAL INFILE when file is larger than max\_allowed\_packet

### Misc

* ensuring Connection.isValid(timeout) always respect timeout value

### misc :

* correct typo in error message when setting wrong parameter
* handling connection error when no database is provided
* correcting possible race condition when using Statement/PrepareStatement in multi-thread with fetch size set

Be notified of new MariaDB Server releases automatically by [subscribing](https://lists.mariadb.org/postorius/lists/announce.lists.mariadb.org/) to the MariaDB Foundation community announce 'at' lists.mariadb.org announcement list (this is a low traffic, announce-only list). MariaDB plc customers will be notified for all new releases, security issues and critical bug fixes for all MariaDB plc products thanks to the Notification Services.

MariaDB may already be included in your favorite OS distribution. More\
information can be found on the[Distributions which Include MariaDB](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/readme-1)\
page.

{% @marketo/form formid="4316" formId="4316" %}
