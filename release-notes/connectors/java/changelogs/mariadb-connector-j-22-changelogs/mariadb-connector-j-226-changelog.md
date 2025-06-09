# MariaDB Connector/J 2.2.6 Changelog

The most recent [_**Stable**_](../../../../mariadb-release-criteria.md) _**(GA)**_ release of [MariaDB Connector/J](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-j/README.md) is:[**MariaDB Connector/J 3.5.3**](../../mariadb-connector-j-3-5-release-notes/mariadb-connector-j-3-5-3-release-notes.md)

[Download](https://downloads.mariadb.org/connector-java/2.2.6/)[Release Notes](../../mariadb-connectorj-22-release-notes/mariadb-connector-j-226-release-notes.md)[Changelog](mariadb-connector-j-226-changelog.md)[Connector/J Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-j/README.md)

**Release date:** 19 Jul 2018

For the highlights of this release, see the[release notes](../../mariadb-connectorj-22-release-notes/mariadb-connector-j-226-release-notes.md).

The revision number links will take you to the revision's page on GitHub. On[GitHub](https://github.com/MariaDB/mariadb-connector-j) you can view more\
details of the revision and view diffs of the code modified in that revision.

* [Revision #1e2c912c](https://github.com/mariadb-corporation/mariadb-connector-j/commit/1e2c912c) - Bump 2.2.6 version
* [Revision #b626e026](https://github.com/mariadb-corporation/mariadb-connector-j/commit/b626e026) - \[[CONJ-384](https://jira.mariadb.org/browse/CONJ-384)] add option "useAffectedRow" test and documentation
* [Revision #91be0a9f](https://github.com/mariadb-corporation/mariadb-connector-j/commit/91be0a9f) - \[misc] remove test not stable for aurora
* [Revision #32fdd7f0](https://github.com/mariadb-corporation/mariadb-connector-j/commit/32fdd7f0) - \[misc] change appveyor to last recent MariaDB released version
* [Revision #a7e50a9b](https://github.com/mariadb-corporation/mariadb-connector-j/commit/a7e50a9b) - \[misc] add testing with java oraclejdk-ea allowed to fail, since not fully reliable
* [Revision #e0e946e3](https://github.com/mariadb-corporation/mariadb-connector-j/commit/e0e946e3) - \[misc] travis test correction: work even if Travis secure environment variables are not accessible (in Pull request)
* [Revision #ff9926c3](https://github.com/mariadb-corporation/mariadb-connector-j/commit/ff9926c3) - \[[CONJ-624](https://jira.mariadb.org/browse/CONJ-624)] MariaDbPoolDataSource possible NPE on configuration getter
* [Revision #d4fcfbeb](https://github.com/mariadb-corporation/mariadb-connector-j/commit/d4fcfbeb) - [CONJ-623](https://jira.mariadb.org/browse/CONJ-623) / Increase connection logging when Primary node connection fails
* [Revision #803825eb](https://github.com/mariadb-corporation/mariadb-connector-j/commit/803825eb) - \[[CONJ-622](https://jira.mariadb.org/browse/CONJ-622)] The option connectTimeout takes in account DriverManager getLoginTimeout() va
* [Revision #78736434](https://github.com/mariadb-corporation/mariadb-connector-j/commit/78736434) - \[[CONJ-621](https://jira.mariadb.org/browse/CONJ-621)] escaping when having curly bracket in table field name (backtick)
* [Revision #db8da1f4](https://github.com/mariadb-corporation/mariadb-connector-j/commit/db8da1f4) - \[misc] better unexcepected character when malformed String (wrong surrogate)
* [Revision #7db9cbb4](https://github.com/mariadb-corporation/mariadb-connector-j/commit/7db9cbb4) - \[misc] testing correction when testSingleHost is false
* [Revision #8a4877ed](https://github.com/mariadb-corporation/mariadb-connector-j/commit/8a4877ed) - \[[CONJ-618](https://jira.mariadb.org/browse/CONJ-618)] Client prepared statement parsing double slash as comment error
* [Revision #b24e66b0](https://github.com/mariadb-corporation/mariadb-connector-j/commit/b24e66b0) - fixed formatting
* [Revision #eac3d315](https://github.com/mariadb-corporation/mariadb-connector-j/commit/eac3d315) - Update MariaDbPoolDataSource.java
* [Revision #e9e8acc4](https://github.com/mariadb-corporation/mariadb-connector-j/commit/e9e8acc4) - \[[CONJ-618](https://jira.mariadb.org/browse/CONJ-618)] Client preparestatement parsing error on escaped ' / " in query (not parameters)
* [Revision #f5587acc](https://github.com/mariadb-corporation/mariadb-connector-j/commit/f5587acc) - \[misc] removing one test for aurora
* [Revision #80695d9b](https://github.com/mariadb-corporation/mariadb-connector-j/commit/80695d9b) - \[misc] add oracle java 10 and ea to travis
* [Revision #caad0f16](https://github.com/mariadb-corporation/mariadb-connector-j/commit/caad0f16) - update README java 6-7 to last version 1.7.4
* [Revision #bc8fe422](https://github.com/mariadb-corporation/mariadb-connector-j/commit/bc8fe422) - change README to last version 2.2.5
* [Revision #96c722e2](https://github.com/mariadb-corporation/mariadb-connector-j/commit/96c722e2) - \[misc] documentation format correction

Be notified of new MariaDB Server releases automatically by [subscribing](https://lists.mariadb.org/postorius/lists/announce.lists.mariadb.org/) to the MariaDB Foundation community announce 'at' lists.mariadb.org announcement list (this is a low traffic, announce-only list). MariaDB plc customers will be notified for all new releases, security issues and critical bug fixes for all MariaDB plc products thanks to the Notification Services.

MariaDB may already be included in your favorite OS distribution. More\
information can be found on the[Distributions which Include MariaDB](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/readme-1)\
page.

{% @marketo/form formid="4316" formId="4316" %}
