# MariaDB Connector/Python 0.9.58 beta Changelog

The most recent [_**Stable**_](../../../../mariadb-release-criteria.md) _**(GA)**_ release of MariaDB Connector/Python is:[**MariaDB Connector/Python 1.1.12**](../../mariadb-connector-python-1-1-release-notes/mariadb-connector-python-1-1-12-release-notes.md)

[Download](https://mariadb.com/downloads/#connectors)[Release Notes](../../mariadb-connector-python-0-9-release-notes/mariadb-connector-python-0-9-58-release-notes.md)[Changelog](mariadb-connector-python-0958-changelog.md)[Connector/Python Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/mariadb-connector-python/README.md)

**Release date:** 6 May 2020

For the highlights of this release, see the[release notes](../../mariadb-connector-python-0-9-release-notes/mariadb-connector-python-0-9-58-release-notes.md).

**Do not use&#x20;**_**beta**_**&#x20;releases in production!**

The revision number links will take you to the revision's page on GitHub. On[GitHub](https://github.com/MariaDB/mariadb-connector-python/) you can view more\
details of the revision and view diffs of the code modified in that revision.

* [Revision #5334dde](https://github.com/mariadb-corporation/mariadb-connector-python/commit/5334dde)\
  2020-05-06 05:23:09 +0200
  * Fixed typo
* [Revision #87684a1](https://github.com/mariadb-corporation/mariadb-connector-python/commit/87684a1)\
  2020-05-05 22:41:36 +0200
  * Fix for [CONPY-62](https://jira.mariadb.org/browse/CONPY-62): Decimal values returned as strings when passing in paramaters
* [Revision #d35d172](https://github.com/mariadb-corporation/mariadb-connector-python/commit/d35d172)\
  2020-05-05 08:25:35 +0200
  * Fix for [CONPY-61](https://jira.mariadb.org/browse/CONPY-61): `executemany()` doesn't allow inserting optional entries
* [Revision #3028132](https://github.com/mariadb-corporation/mariadb-connector-python/commit/3028132)\
  2020-04-23 22:19:03 +0200
  * Fix for [CONPY-59](https://jira.mariadb.org/browse/CONPY-59): Cursor fetchall with error
* [Revision #59c7771](https://github.com/mariadb-corporation/mariadb-connector-python/commit/59c7771)\
  2020-04-19 14:59:54 +0200
  * Fix for [CONPY-58](https://jira.mariadb.org/browse/CONPY-58): Parameter Error when using `paramstyle PYFORMAT`
* [Revision #6cb5227](https://github.com/mariadb-corporation/mariadb-connector-python/commit/6cb5227)\
  2020-04-15 11:45:04 +0200
  * Bump version number
