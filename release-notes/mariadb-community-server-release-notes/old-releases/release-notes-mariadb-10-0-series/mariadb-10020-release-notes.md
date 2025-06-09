# MariaDB 10.0.20 Release Notes

The most recent release in the [MariaDB 10.0](changes-improvements-in-mariadb-10-0.md) series is:[**MariaDB 10.0.38**](mariadb-10038-release-notes.md) [Download Now](https://downloads.mariadb.org/mariadb/10.0.38)

[Download](https://downloads.mariadb.org/mariadb/10.0.20)[Release Notes](mariadb-10020-release-notes.md)[Changelog](../../../changelogs/changelogs-mariadb-100-series/mariadb-10020-changelog.md)[Overview of 10.0](changes-improvements-in-mariadb-10-0.md)

**Release date:** 18 Jun 2015

[MariaDB 10.0](changes-improvements-in-mariadb-10-0.md) is the current stable series of MariaDB. It is an evolution of [MariaDB 5.5](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/aEnK0ZXmUbJzqQrTjFyb/~/changes/311/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5), with several entirely new features not found anywhere else and with\
backported and reimplemented features from MySQL 5.6.

[MariaDB 10.0.20](mariadb-10020-release-notes.md) is a [_**Stable**_](../../../mariadb-release-criteria.md) (_GA_) release.

**For an overview of** [**MariaDB 10.0**](changes-improvements-in-mariadb-10-0.md) **see the**[**What is MariaDB 10.0?**](changes-improvements-in-mariadb-10-0.md) **page.**

Thanks, and enjoy MariaDB!

## Notable changes

* [XtraDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) updated to XtraDB-5.6.24-72.2
* [Innodb](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) updated to InnoDB-5.6.25
* [Performance Schema](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/system-tables/performance-schema) updated to 5.6.25
* [TokuDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/tokudb) updated to TokuDB-7.5.7
* Client command line option `--ssl-verify-server-cert` (and `MYSQL_OPT_SSL_VERIFY_SERVER_CERT` option of the client API) when used together with `--ssl` will ensure that the established connection is SSL-encrypted and the MariaDB server has a valid certificate. This fixes [CVE-2015-3152](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2015-3152).
* Fixes for the following [security vulnerabilities](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/security):
  * [CVE-2015-2582](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2015-2582)
  * [CVE-2015-2620](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2015-2620)
  * [CVE-2015-2643](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2015-2643)
  * [CVE-2015-2648](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2015-2648)
  * [CVE-2015-3152](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2015-3152)
  * [CVE-2015-4752](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2015-4752)
  * [CVE-2015-4864](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2015-4864)

### Platforms

* We're introducing Debian Jessie packages in this version of MariaDB. They are considered experimental at this point.
* We've fixed a bug that caused a segfault on FreeBSD 10.1 x86 ([MDEV-7398](https://jira.mariadb.org/browse/MDEV-7398))

### Changelog

For a complete list of changes made in [MariaDB 10.0.20](mariadb-10020-release-notes.md), with links to detailed\
information on each push, see the [changelog](../../../changelogs/changelogs-mariadb-100-series/mariadb-10020-changelog.md).

Be notified of new MariaDB Server releases automatically by [subscribing](https://lists.mariadb.org/postorius/lists/announce.lists.mariadb.org/) to the MariaDB Foundation community announce 'at' lists.mariadb.org announcement list (this is a low traffic, announce-only list). MariaDB plc customers will be notified for all new releases, security issues and critical bug fixes for all MariaDB plc products thanks to the Notification Services.

MariaDB may already be included in your favorite OS distribution. More\
information can be found on the[Distributions which Include MariaDB](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/readme-1)\
page.

{% @marketo/form formid="4316" formId="4316" %}
