# MariaDB Connector/J 1.4.1 Changelog

The most recent [_**Stable**_](../../../../mariadb-release-criteria.md) _**(GA)**_ release of [MariaDB Connector/J](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-j/README.md) is:[**MariaDB Connector/J 3.5.3**](../../mariadb-connector-j-3-5-release-notes/mariadb-connector-j-3-5-3-release-notes.md)

[Download](https://downloads.mariadb.org/connector-java/1.4.1/)[Release Notes](../../mariadb-connector-j-14-release-notes/mariadb-connector-j-141-release-notes.md)[Changelog](mariadb-connector-j-141-changelog.md)[Connector/J Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-j/README.md)

**Release date:** 11 Apr 2016

For the highlights of this release, see the[release notes](../../mariadb-connector-j-14-release-notes/mariadb-connector-j-141-release-notes.md).

The revision number links will take you to the revision's page on GitHub. On[GitHub](https://github.com/MariaDB/mariadb-connector-j) you can view more details of the revision and view diffs of the code modified in that revision.

* [Revision #651af72](https://github.com/mariadb-corporation/mariadb-connector-j/commit/651af72)
  * when option rewriteBatchedStatements is set to true, correction of packet separation when query size > max\_allow\_packet
* [Revision #ae64162](https://github.com/mariadb-corporation/mariadb-connector-j/commit/ae64162)
  * correction when using prepareStatement without parameters and option rewriteBatchedStatements to true
* [Revision #171b1ab](https://github.com/mariadb-corporation/mariadb-connector-j/commit/171b1ab)
  * \[[CONJ-270](https://jira.mariadb.org/browse/CONJ-270)] permit 65535 parameters to server preparedStatement
* [Revision #41bd470](https://github.com/mariadb-corporation/mariadb-connector-j/commit/41bd470)
  * \[268] update license header
* [Revision #9e36595](https://github.com/mariadb-corporation/mariadb-connector-j/commit/9e36595)
  * \[misc] correction on callableStatement with output parameter if resulset size > 16mb
* [Revision #c1b9006](https://github.com/mariadb-corporation/mariadb-connector-j/commit/c1b9006)
  * \[misc] performance improvement : reuse buffer for reading result and using System.arraycopy
* [Revision #2d1d4e3](https://github.com/mariadb-corporation/mariadb-connector-j/commit/2d1d4e3)
  * \[CON-274] connection to permit connection to mysql 5.1 db using password

{% @marketo/form formid="4316" formId="4316" %}
