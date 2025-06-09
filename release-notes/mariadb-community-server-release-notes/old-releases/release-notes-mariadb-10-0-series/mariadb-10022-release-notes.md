# MariaDB 10.0.22 Release Notes

The most recent release in the [MariaDB 10.0](changes-improvements-in-mariadb-10-0.md) series is:[**MariaDB 10.0.38**](mariadb-10038-release-notes.md) [Download Now](https://downloads.mariadb.org/mariadb/10.0.38)

[Download](https://downloads.mariadb.org/mariadb/10.0.22)[Release Notes](mariadb-10022-release-notes.md)[Changelog](../../../changelogs/changelogs-mariadb-100-series/mariadb-10022-changelog.md)[Overview of 10.0](changes-improvements-in-mariadb-10-0.md)

**Release date:** 29 Oct 2015

[MariaDB 10.0](changes-improvements-in-mariadb-10-0.md) is a previous stable series of MariaDB. It is an evolution of [MariaDB 5.5](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/aEnK0ZXmUbJzqQrTjFyb/~/changes/311/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5) with several entirely new features not found anywhere else and with\
backported and reimplemented features from MySQL 5.6.

[MariaDB 10.0.22](mariadb-10022-release-notes.md) is a [_**Stable**_](../../../mariadb-release-criteria.md) (_GA_) release.

**For an overview of** [**MariaDB 10.0**](changes-improvements-in-mariadb-10-0.md) **see the**[**What is MariaDB 10.0?**](changes-improvements-in-mariadb-10-0.md) **page.**

Thanks, and enjoy MariaDB!

## Notable changes

* [XtraDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) updated to XtraDB-5.6.26-74.0
* [Innodb](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) updated to InnoDB-5.6.27
* [Performance Schema](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/system-tables/performance-schema) updated to 5.6.27
* Slave started with [--binlog-format=STATEMENT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables) can replicate from master with any type of [--binlog-format](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables).
* Replication from MySQL 5.6 with GTID, binlog\_rows\_query\_log\_events and ignorable events now works. In this case MariaDB will remove the MySQL GTIDs and other unneeded events and instead adds its own [GTIDs](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid).
* The [mysql.event table](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/system-tables/the-mysql-database-tables/mysql-event-table) is upgraded live; no need to restart the server to use events if the event table has changed ([MariaDB 10.0.22](mariadb-10022-release-notes.md) and [MariaDB 10.1.9](../release-notes-mariadb-10-1-series/mariadb-10-1-9-release-notes.md)).
* Setting the [event\_scheduler](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/server-system-variables#event_scheduler) system variable will also try to reload the [mysql.event table](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/system-tables/the-mysql-database-tables/mysql-event-table) if it was not properly loaded at startup.
* Slaves now apply any events they get from the master, regardless of the [binary log format](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/server-monitoring-logs/binary-log/binary-log-formats). The [binlog\_format](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables) system variable only applies to normal (not replicated) updates.
* Fixes for the following [security vulnerabilities](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/security):
  * [CVE-2015-4802](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2015-4802)
  * [CVE-2015-4807](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2015-4807)
  * [CVE-2015-4815](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2015-4815)
  * [CVE-2015-4826](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2015-4826)
  * [CVE-2015-4830](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2015-4830)
  * [CVE-2015-4836](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2015-4836)
  * [CVE-2015-4858](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2015-4858)
  * [CVE-2015-4861](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2015-4861)
  * [CVE-2015-4870](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2015-4870)
  * [CVE-2015-4913](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2015-4913)
  * [CVE-2015-4792](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2015-4792)
  * [CVE-2015-7744](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2015-7744)
  * [CVE-2016-0610](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2016-0610)
  * [CVE-2016-3471](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2016-3471)

### Deprecated Distributions

As per the [MariaDB Deprecation Policy](../../../mariadb-platform-deprecation-policy.md), this will be the last release of [MariaDB 10.0](changes-improvements-in-mariadb-10-0.md) for Ubuntu 14.10 "Utopic" and Fedora 20.

### Changelog

For a complete list of changes made in [MariaDB 10.0.22](mariadb-10022-release-notes.md), with links to detailed\
information on each push, see the [changelog](../../../changelogs/changelogs-mariadb-100-series/mariadb-10022-changelog.md).

Be notified of new MariaDB Server releases automatically by [subscribing](https://lists.mariadb.org/postorius/lists/announce.lists.mariadb.org/) to the MariaDB Foundation community announce 'at' lists.mariadb.org announcement list (this is a low traffic, announce-only list). MariaDB plc customers will be notified for all new releases, security issues and critical bug fixes for all MariaDB plc products thanks to the Notification Services.

MariaDB may already be included in your favorite OS distribution. More\
information can be found on the [Distributions which Include MariaDB](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/readme-1)\
page.
