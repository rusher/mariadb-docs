# MariaDB Connector/C 3.1.2 Changelog

The most recent [_**Stable**_](../../../../mariadb-release-criteria.md) _**(GA)**_ release of MariaDB Connector/C is:[**MariaDB Connector/C 3.4.5**](../../mariadb-connector-c-3-4-release-notes/mariadb-connector-c-3-4-5-release-notes.md)

[Download](https://mariadb.com/downloads/#connectors)[Release Notes](../../mariadb-connector-c-31-release-notes/mariadb-connector-c-312-release-notes.md)[Changelog](mariadb-connector-c-312-changelog.md)[About MariaDB Connector/C](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-c/README.md)

**Release date:** 19 Jun 2019

For the highlights of this release, see the[release notes](../../mariadb-connector-c-31-release-notes/mariadb-connector-c-312-release-notes.md).

The revision number links will take you to the revision's page on GitHub. On[GitHub](https://github.com/MariaDB/mariadb-connector-c/) you can view more\
details of the revision and view diffs of the code modified in that revision.

* [Revision #c098613](https://github.com/mariadb-corporation/mariadb-connector-c/commit/c098613)\
  2019-06-14 13:48:31 +0200
  * Moved rpl\_api test to manual tests, since there is an endless loop for now without timeout.
* [Revision #b4a95c3](https://github.com/mariadb-corporation/mariadb-connector-c/commit/b4a95c3)\
  2019-06-14 13:36:27 +0200
  * Merge commit [Revision #5dd2ba5d0b35951ea1d5905c6482eb3debff09b8](https://github.com/mariadb-corporation/mariadb-connector-c/commit/5dd2ba5d0b35951ea1d5905c6482eb3debff09b8) into 3.1
* [Revision #5dd2ba5](https://github.com/mariadb-corporation/mariadb-connector-c/commit/5dd2ba5)\
  2019-06-14 13:33:34 +0200
  * Fix for [CONC-383](https://jira.mariadb.org/browse/CONC-383): client plugins can't be loaded due to missing prefix
* [Revision #8983406](https://github.com/mariadb-corporation/mariadb-connector-c/commit/8983406)\
  2019-06-14 13:36:07 +0200
  * Merge commit [Revision #d4a0a384459e3a6645ad4df46db18a5d2dd4c780](https://github.com/mariadb-corporation/mariadb-connector-c/commit/d4a0a384459e3a6645ad4df46db18a5d2dd4c780) into 3.1
* [Revision #d4a0a38](https://github.com/mariadb-corporation/mariadb-connector-c/commit/d4a0a38)\
  2019-06-14 08:47:21 +0200
  * Better test of warnings during prepare.
* [Revision #78e857e](https://github.com/mariadb-corporation/mariadb-connector-c/commit/78e857e)\
  2019-06-03 11:03:57 +0200
  * Removed unused call to QueryContextAttributes with connection info.
* [Revision #d95dec8](https://github.com/mariadb-corporation/mariadb-connector-c/commit/d95dec8)\
  2019-06-08 09:05:04 +0200
  * Move NORMAL priority at the end of priority string, otherwise possible version specifications will not work.
* [Revision #cd90aa4](https://github.com/mariadb-corporation/mariadb-connector-c/commit/cd90aa4)\
  2019-06-06 15:39:47 -0400
  * bump the VERSION
