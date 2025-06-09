# MariaDB Connector/J 1.3.6 Changelog

The most recent [_**Stable**_](../../../../mariadb-release-criteria.md) _**(GA)**_ release of [MariaDB Connector/J](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-j/README.md) is:[**MariaDB Connector/J 3.5.3**](../../mariadb-connector-j-3-5-release-notes/mariadb-connector-j-3-5-3-release-notes.md)

[Download](https://downloads.mariadb.org/connector-java/1.3.6/)[Release Notes](../../mariadb-connectorj-13-release-notes/mariadb-connector-j-136-release-notes.md)[Changelog](mariadb-connector-j-136-changelog.md)[Connector/J Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-j/README.md)

**Release date:** 29 Feb 2016

For the highlights of this release, see the[release notes](../../mariadb-connectorj-13-release-notes/mariadb-connector-j-136-release-notes.md).

The revision number links will take you to the revision's page on GitHub. On[GitHub](https://github.com/MariaDB/mariadb-connector-j) you can view more details of the revision and view diffs of the code modified in that revision.

* [CONJ-252](https://jira.mariadb.org/browse/CONJ-252) : Correction of charset parameter on Statement.setCharacterStream() and setClob. [Revision #012b8c3](https://github.com/mariadb-corporation/mariadb-connector-j/commit/012b8c3) 2016-02-19
* [CONJ-253](https://jira.mariadb.org/browse/CONJ-253) : Protocol encoding correction for binary field. [Revision #123f02a](https://github.com/mariadb-corporation/mariadb-connector-j/commit/123f02a) 2016-02-20
* [CONJ-254](https://jira.mariadb.org/browse/CONJ-254) : Correction of error in boolean when using scala anorm string interpolation. [Revision #16ad037](https://github.com/mariadb-corporation/mariadb-connector-j/commit/16ad037) 2016-02-19
* [CONJ-255](https://jira.mariadb.org/browse/CONJ-255) : getBoolean() improvement (for field not normally considered as boolean). [Revision #16ad037](https://github.com/mariadb-corporation/mariadb-connector-j/commit/16ad037) 2016-02-19
* [CONJ-258](https://jira.mariadb.org/browse/CONJ-258) : correction of possible race condition on statement.close().. [Revision #161f581](https://github.com/mariadb-corporation/mariadb-connector-j/commit/161f581) 2016-02-21

**Misc**

* using default utf8mb4 (4 bit UTF8) charset in exchanges. [Revision #ac52bb9](https://github.com/mariadb-corporation/mariadb-connector-j/commit/ac52bb9) 2016-02-20, [Revision #34a91cb](https://github.com/mariadb-corporation/mariadb-connector-j/commit/34a91cb) 2016-02-20
* binary data Time correction. [Revision #da00357](https://github.com/mariadb-corporation/mariadb-connector-j/commit/da00357) 2016-02-20
