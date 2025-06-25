# MariaDB 10.0.30 Release Notes

The most recent release in the [MariaDB 10.0](changes-improvements-in-mariadb-10-0.md) series is:[**MariaDB 10.0.38**](mariadb-10038-release-notes.md) [Download Now](https://downloads.mariadb.org/mariadb/10.0.38)

[Download](https://downloads.mariadb.org/mariadb/10.0.30)[Release Notes](mariadb-10030-release-notes.md)[Changelog](../../changelogs/changelogs-mariadb-100-series/mariadb-10030-changelog.md)[Overview of 10.0](changes-improvements-in-mariadb-10-0.md)

**Release date:** 8 Mar 2017

[MariaDB 10.0](changes-improvements-in-mariadb-10-0.md) is a previous stable series of MariaDB. It is an evolution of [MariaDB 5.5](../release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5.md) with several entirely new features not found anywhere else and with\
backported and reimplemented features from MySQL 5.6.

This is a [_**Stable**_](../../../mariadb-release-criteria.md) (_GA_) release.

**For an overview of** [**MariaDB 10.0**](changes-improvements-in-mariadb-10-0.md) **see the**[**What is MariaDB 10.0?**](changes-improvements-in-mariadb-10-0.md) **page.**

Thanks, and enjoy MariaDB!

## Notable changes

* [XtraDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) updated to 5.6.35-80.0
* [TokuDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/tokudb) updated to 5.6.35-80.0
* [PCRE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/string-functions/regular-expressions-functions/pcre) updated to 8.40
* [MDEV-11027](https://jira.mariadb.org/browse/MDEV-11027): better InnoDB crash recovery progress reporting
* [MDEV-11520](https://jira.mariadb.org/browse/MDEV-11520): improvements to how InnoDB data files are extended
* Improvements to InnoDB startup/shutdown to make it more robust
* [MDEV-11233](https://jira.mariadb.org/browse/MDEV-11233): fix for FULLTEXT index crash
* [MDEV-6143](https://jira.mariadb.org/browse/MDEV-6143): MariaDB Linux binary tarballs will now always untar to directories that match their filename
* As per the [MariaDB Deprecation Policy](../../../mariadb-platform-deprecation-policy.md), this will be the last release of [MariaDB 10.0](changes-improvements-in-mariadb-10-0.md) for Fedora 23, CentOS 5, RHEL 5, and openSUSE 13
* Fixes for the following [security vulnerabilities](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/security):
  * [CVE-2017-3313](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-3313)
  * [CVE-2017-3302](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-3302)

## Changelog

For a complete list of changes made in [MariaDB 10.0.30](mariadb-10030-release-notes.md), with links to detailed\
information on each push, see the [changelog](../../changelogs/changelogs-mariadb-100-series/mariadb-10030-changelog.md).

Be notified of new MariaDB Server releases automatically by [subscribing](https://lists.mariadb.org/postorius/lists/announce.lists.mariadb.org/) to the MariaDB Foundation community announce 'at' lists.mariadb.org announcement list (this is a low traffic, announce-only list). MariaDB plc customers will be notified for all new releases, security issues and critical bug fixes for all MariaDB plc products thanks to the Notification Services.

MariaDB may already be included in your favorite OS distribution. More\
information can be found on the[Distributions which Include MariaDB](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/distributions-including-mariadb)\
page.

{% @marketo/form formid="4316" formId="4316" %}
