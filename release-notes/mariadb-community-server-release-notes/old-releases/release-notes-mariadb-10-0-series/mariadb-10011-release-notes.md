# MariaDB 10.0.11 Release Notes

The most recent release in the [MariaDB 10.0](changes-improvements-in-mariadb-10-0.md) series is:[**MariaDB 10.0.38**](mariadb-10038-release-notes.md) [Download Now](https://downloads.mariadb.org/mariadb/10.0.38)

[Download](https://downloads.mariadb.org/mariadb/10.0.11)[Release Notes](mariadb-10011-release-notes.md)[Changelog](../../changelogs/changelogs-mariadb-100-series/mariadb-10011-changelog.md)[Overview of 10.0](changes-improvements-in-mariadb-10-0.md)

**Release date:** 12 May 2014

[MariaDB 10.0](changes-improvements-in-mariadb-10-0.md) is the current stable series of MariaDB. It is an evolution of [MariaDB 5.5](../release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5.md) with several entirely new features not found anywhere else and\
with backported and reimplemented features from MySQL 5.6.

[MariaDB 10.0.11](mariadb-10011-release-notes.md) is a [_**Stable**_](../../../mariadb-release-criteria.md) (_GA_) release.

**For an overview of** [**MariaDB 10.0**](changes-improvements-in-mariadb-10-0.md) **see the**[**What is MariaDB 10.0?**](changes-improvements-in-mariadb-10-0.md) **page.**

Thanks, and enjoy MariaDB!

## Notable changes

[MariaDB 10.0.11](mariadb-10011-release-notes.md) is primarily a bug-fix release.

Notable changes of this release include:

* Fixes for the following security vulnerabilities:
  * [CVE-2014-2436](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-2436)
  * [CVE-2014-2440](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-2440)
  * [CVE-2014-2430](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-2430)
  * [CVE-2014-2431](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-2431)
  * [CVE-2019-2481](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-2481)
  * [CVE-2021-2032](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-2032)
* Updated [TokuDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/storage-engines/tokudb) engine to version 7.1.6
* Updated [Spider](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/storage-engines/spider) storage engine to version 3.2
* Updated [XtraDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/storage-engines/innodb) storage engine to version 5.6.17-65.0
* Updated [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/storage-engines/innodb) storage engine to version 5.6.17
* Updated [performance\_schema](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/system-tables/performance-schema) to version 5.6.17
* Updated [Connect](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/storage-engines/connect), and [OQGraph](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/storage-engines/oqgraph-storage-engine) engines.
* Online [ALTER TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table) works for partitioned tables
* New system variable [default\_regex\_flags](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/server-system-variables#default_regex_flags). To make MariaDB [RLIKE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/string-functions/regular-expressions-functions/regexp) operator behave in a non-standard but backward compatible way use

```sql
SET @@default_regex_flags='DOTALL';
```

For a complete list of changes made in [MariaDB 10.0.11](mariadb-10011-release-notes.md), with links to detailed\
information on each push, see the [changelog](../../changelogs/changelogs-mariadb-100-series/mariadb-10011-changelog.md).

## Ubuntu 12.10 and Mint 14

As per the [MariaDB Deprecation Policy](../../../mariadb-platform-deprecation-policy.md), this will be the last release of [MariaDB 10.0](changes-improvements-in-mariadb-10-0.md) for both Ubuntu 12.10 "Quantal" and Mint 14 "Nadia".

Be notified of new MariaDB Server releases automatically by [subscribing](https://lists.mariadb.org/postorius/lists/announce.lists.mariadb.org/) to the MariaDB Foundation community announce 'at' lists.mariadb.org announcement list (this is a low traffic, announce-only list). MariaDB plc customers will be notified for all new releases, security issues and critical bug fixes for all MariaDB plc products thanks to the Notification Services.

MariaDB may already be included in your favorite OS distribution. More\
information can be found on the[Distributions which Include MariaDB](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/distributions-including-mariadb)\
page.

{% @marketo/form formid="4316" formId="4316" %}
