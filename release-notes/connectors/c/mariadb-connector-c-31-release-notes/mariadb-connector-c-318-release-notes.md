# MariaDB Connector/C 3.1.8 Release Notes

The most recent [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release of MariaDB Connector/C is:[**MariaDB Connector/C 3.4.5**](../mariadb-connector-c-3-4-release-notes/mariadb-connector-c-3-4-5-release-notes.md)

[Download](https://mariadb.com/downloads/#connectors)[Release Notes](mariadb-connector-c-318-release-notes.md)[Changelog](../changelogs/mariadb-connector-c-31-changelogs/mariadb-connector-c-318-changelog.md)[About MariaDB Connector/C](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-c/README.md)

**Release date:** 14 May 2020

This is a [_**Stable (GA)**_](../../../mariadb-release-criteria.md) release of the MariaDB\
Connector/C, formerly known as MariaDB Client Library for C.

**For a description of this library see the**[**MariaDB Connector/C**](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c) **page.**

## Notable Changes

* Included in [MariaDB 10.5.3](../../../mariadb-community-server-release-notes/mariadb-10-5-series/mariadb-1053-release-notes.md), [MariaDB 10.4.13](../../../mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/mariadb-10413-release-notes.md), [MariaDB 10.3.23](../../../mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-10323-release-notes.md), and [MariaDB 10.2.32](../../../mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-10232-release-notes.md)
* In this version we've moved to providing binaries for several different Linux distributions instead of just a pair of "generic" Linux binaries (a 32-bit and a 64-bit). If you want to continue using the generic binaries, they are still present and listed as "Ubuntu 14.04 32-bit" and "Ubuntu 14.04 64-bit" on the downloads page
* [CONC-304](https://jira.mariadb.org/browse/CONC-304): Rename the static library to `libmariadb.a` and other `libmariadb` files in a consistent manner
* [CONC-441](https://jira.mariadb.org/browse/CONC-441): Default user name for C/C is wrong if login user is different from effective user
* [CONC-449](https://jira.mariadb.org/browse/CONC-449): Check `$MARIADB_HOME/my.cnf` in addition to `$MYSQL_HOME/my.cnf`
* [CONC-457](https://jira.mariadb.org/browse/CONC-457): `mysql_list_processes` crashes in `unpack_fields`
* [CONC-458](https://jira.mariadb.org/browse/CONC-458): `mysql_get_timeout_value` crashes when used improperly
* [CONC-464](https://jira.mariadb.org/browse/CONC-464): Fix static build for auth\_gssapi\_client plugin
* Fixes for the following [security vulnerabilities](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/security):
  * [CVE-2020-2752](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-2752)
  * [CVE-2020-13249](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-13249)

## Changelog

For a list of changes made in this release, with links to detailed information\
on each push, see the [changelog](../changelogs/mariadb-connector-c-31-changelogs/mariadb-connector-c-318-changelog.md).

Be notified of new MariaDB Server releases automatically by [subscribing](https://lists.mariadb.org/postorius/lists/announce.lists.mariadb.org/) to the MariaDB Foundation community announce 'at' lists.mariadb.org announcement list (this is a low traffic, announce-only list). MariaDB plc customers will be notified for all new releases, security issues and critical bug fixes for all MariaDB plc products thanks to the Notification Services.

MariaDB may already be included in your favorite OS distribution. More\
information can be found on the[Distributions which Include MariaDB](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/readme-1)\
page.
