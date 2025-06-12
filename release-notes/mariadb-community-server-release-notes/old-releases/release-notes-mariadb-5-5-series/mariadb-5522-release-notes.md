# MariaDB 5.5.22 Release Notes

The most recent release in the [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5) series is:[**MariaDB 5.5.68**](mariadb-5568-release-notes.md) [Download Now](https://downloads.mariadb.org/mariadb/5.5.68/)

[Download](https://downloads.askmonty.org/mariadb/5.5.22) |**Release Notes** |[Changelog](../../../changelogs/changelogs-mariadb-55-series/mariadb-5522-changelog.md) |[Overview of 5.5](broken-reference)

**Release date:** 29 Mar 2012

[MariaDB 5.5.22](mariadb-5522-release-notes.md) is a [_**Release Candidate**_](../../../mariadb-release-criteria.md) _**(RC)**_\
release. In general this means that there are no known serious bugs, except for\
those marked as feature requests, that no bugs were fixed since last release\
that caused a notable code changes, and that we believe the code is ready for\
general usage (based on bug inflow), but we want more testing before calling it\
stable. This is the third release of the [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5) series.

**For a description of** [**MariaDB 5.5**](broken-reference) **see the**[**What is MariaDB 5.5**](broken-reference) **page.**

For a list of changes made in [MariaDB 5.5.22](mariadb-5522-release-notes.md)-rc, with links to detailed\
information on each push, see the[MariaDB 5.5.22 Changelog](../../../changelogs/changelogs-mariadb-55-series/mariadb-5522-changelog.md).

In most respects [MariaDB](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/mariadb/README.md) will work exactly as MySQL: all commands,\
interfaces, libraries and APIs that exist in MySQL also exist in MariaDB.

**Note:** _There are no RPM packages of_ [_MariaDB 5.5.22_](mariadb-5522-release-notes.md) _available at this time._

## Security Fixes

This release includes fixes for the following security vulnerabilities:

* [CVE-2012-1703](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2012-1703)
* [CVE-2012-1688](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2012-1688)
* [CVE-2012-1690](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2012-1690)
* [CVE-2012-1697](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2012-1697)

## Includes MySQL 5.5.22

This version of MariaDB includes MySQL 5.5.22. See [Changes in MySQL 5.5.22](https://dev.mysql.com/doc/refman/5.5/en/news-5-5-22.html) for what changed between this and previous MySQL versions.

## Dynamic replication variables

The variables `replicate_do_*`, `replicate_ignore_*`, and`replicate_wild_*` have been made dynamic, so they can be changed without\
requiring a server restart.

See [Dynamic Replication Variables](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-filters) for more\
information.

## SQL level error logging

The SQL\_ERROR\_LOG plugin implemented to allow logging of sql errors.

See [SQL\_ERROR\_LOG](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/server-monitoring-logs/sql-error-log-plugin) for more information.

Be notified of new MariaDB Server releases automatically by [subscribing](https://lists.mariadb.org/postorius/lists/announce.lists.mariadb.org/) to the MariaDB Foundation community announce 'at' lists.mariadb.org announcement list (this is a low traffic, announce-only list). MariaDB plc customers will be notified for all new releases, security issues and critical bug fixes for all MariaDB plc products thanks to the Notification Services.

MariaDB may already be included in your favorite OS distribution. More\
information can be found on the[Distributions which Include MariaDB](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/readme-1)\
page.

{% @marketo/form formid="4316" formId="4316" %}
