# MariaDB Connector/J 1.5.8 Release Notes

The most recent [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release of [MariaDB Connector/J](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-j/README.md) is:[**MariaDB Connector/J 3.5.3**](../mariadb-connector-j-3-5-release-notes/mariadb-connector-j-3-5-3-release-notes.md)

[Download](https://downloads.mariadb.org/connector-java/1.5.8/)[Release Notes](mariadb-connector-j-158-release-notes.md)[Changelog](../changelogs/mariadb-connector-j-15-changelogs/mariadb-connector-j-158-changelog.md)[Connector/J Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-j/README.md)

**Release date:** 15 Feb 2017

MariaDB Connector/J 1.5.8 is a [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_\
release.

**For an overview of MariaDB Connector/J see the**[**About MariaDB Connector/J**](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-j/README.md) **page**

## Notable Changes

This version is a bug-fix release.

### Bugfix

* [CONJ-424](https://jira.mariadb.org/browse/CONJ-424) : getGeneratedKeys() on table without generated key failed on second execution
* [CONJ-412](https://jira.mariadb.org/browse/CONJ-412) : Metadata take in account tinyInt1isBit in method columnTypeClause
* [CONJ-418](https://jira.mariadb.org/browse/CONJ-418) : ResultSet.last() isLast() afterLast() and isAfterLast() correction when streaming
* [CONJ-415](https://jira.mariadb.org/browse/CONJ-415) : ResultSet.absolute() should not always return true
* [CONJ-392](https://jira.mariadb.org/browse/CONJ-392) : Aurora cluster endpoint detection fails when time\_zone doesn't match system\_time\_zone
* [CONJ-425](https://jira.mariadb.org/browse/CONJ-425) : CallableStatement getObject class according to java.sql.Types value
* [CONJ-426](https://jira.mariadb.org/browse/CONJ-426) : Allow executeBatch to be interrupted
* [CONJ-420](https://jira.mariadb.org/browse/CONJ-420) : High CPU usage against Aurora after 2 hours inactivity

Be notified of new MariaDB Server releases automatically by [subscribing](https://lists.mariadb.org/postorius/lists/announce.lists.mariadb.org/) to the MariaDB Foundation community announce 'at' lists.mariadb.org announcement list (this is a low traffic, announce-only list). MariaDB plc customers will be notified for all new releases, security issues and critical bug fixes for all MariaDB plc products thanks to the Notification Services.

MariaDB may already be included in your favorite OS distribution. More\
information can be found on the[Distributions which Include MariaDB](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/readme-1)\
page.
