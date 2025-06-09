# MariaDB Connector/J 3.0.6 Changelog

The most recent [_**Stable**_](../../../../mariadb-release-criteria.md) _**(GA)**_ release of [MariaDB Connector/J](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-j/README.md) is:[**MariaDB Connector/J 3.5.3**](../../mariadb-connector-j-3-5-release-notes/mariadb-connector-j-3-5-3-release-notes.md)

[Download](https://mariadb.com/downloads/#connectors)[Release Notes](../../mariadb-connector-j-3-0-release-notes/mariadb-connector-j-306-release-notes.md)[Changelog](mariadb-connector-j-306-changelog.md)[Connector/J Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-j/README.md)

**Release date:** 29 Jun 2022

For the highlights of this release, see the[release notes](../../mariadb-connector-j-3-0-release-notes/mariadb-connector-j-306-release-notes.md).

The revision number links will take you to the revision's page on GitHub. On[GitHub](https://github.com/MariaDB/mariadb-connector-j) you can view more\
details of the revision and view diffs of the code modified in that revision.

* [Revision #8b32329c](https://github.com/mariadb-corporation/mariadb-connector-j/commit/8b32329c) - bump 3.0.6 version
* [Revision #17e60c88](https://github.com/mariadb-corporation/mariadb-connector-j/commit/17e60c88) - \[[CONJ-985](https://jira.mariadb.org/browse/CONJ-985)] ResultSet.getObject() returns ByteSet instead of byte\[] for BIT(x>1) and not Boolean for BIT(1)
* [Revision #8033c1f7](https://github.com/mariadb-corporation/mariadb-connector-j/commit/8033c1f7) - \[[CONJ-979](https://jira.mariadb.org/browse/CONJ-979)] tinyint(1) support \* getObject now return Boolean \* metadata correction returning Boolean/Integer
* [Revision #f97b2e9e](https://github.com/mariadb-corporation/mariadb-connector-j/commit/f97b2e9e) - \[[CONJ-980](https://jira.mariadb.org/browse/CONJ-980)] supporting java.util.Date Parameter
* [Revision #e6fa71d1](https://github.com/mariadb-corporation/mariadb-connector-j/commit/e6fa71d1) - \[[CONJ-953](https://jira.mariadb.org/browse/CONJ-953)] PreparedStatement.getGeneratedKeys() returns rows when no keys are generated in insert
* [Revision #b06d9586](https://github.com/mariadb-corporation/mariadb-connector-j/commit/b06d9586) - \[[CONJ-984](https://jira.mariadb.org/browse/CONJ-984)] Permit executing an initial command with new option `initSql`
* [Revision #f42d29ac](https://github.com/mariadb-corporation/mariadb-connector-j/commit/f42d29ac) - \[misc] adding gradle file to gitignore
* [Revision #6785db4c](https://github.com/mariadb-corporation/mariadb-connector-j/commit/6785db4c) - \[[CONJ-976](https://jira.mariadb.org/browse/CONJ-976)] statement batch correction
* [Revision #e3fd97f4](https://github.com/mariadb-corporation/mariadb-connector-j/commit/e3fd97f4) - \[[CONJ-975](https://jira.mariadb.org/browse/CONJ-975)] ArrayIndexOutOfBoundsException using Resultset.getTime() on '00:00:00' Time value using binary protocol
* [Revision #e6a29d0b](https://github.com/mariadb-corporation/mariadb-connector-j/commit/e6a29d0b) - \[[CONJ-976](https://jira.mariadb.org/browse/CONJ-976)] permit pipelining for batching even when `allowLocalInfile` option is enable
* [Revision #de7ca6fa](https://github.com/mariadb-corporation/mariadb-connector-j/commit/de7ca6fa) - Merge branch 'master' into develop
* [Revision #47d20367](https://github.com/mariadb-corporation/mariadb-connector-j/commit/47d20367) - Merge tag '3.0.5' into develop
