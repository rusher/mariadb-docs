# MariaDB 10.11.4 Release Notes

The most recent release of [MariaDB 10.11](what-is-mariadb-1011.md) is:[**MariaDB 10.11.11**](mariadb-10-11-11-release-notes.md) Stable (GA) [Download Now](https://mariadb.com/downloads/)[_Alternate download from mariadb.org_](https://downloads.mariadb.org/mariadb/10.11.11/)

[Download 10.11.4](https://downloads.mariadb.org/mariadb/10.11.4/)[Release Notes](mariadb-10-11-4-release-notes.md)[Changelog](../../changelogs/changelogs-mariadb-10-11-series/mariadb-10-11-4-changelog.md)[Overview of 10.11](what-is-mariadb-1011.md)

**Release date:** 7 Jun 2023

[MariaDB 10.11](what-is-mariadb-1011.md) is the current long term maintenance development series of MariaDB, [maintained until](https://mariadb.org/about/#maintenance-policy) February 2028. It is an evolution of [MariaDB 10.10](../old-releases/release-notes-mariadb-10-10-series/what-is-mariadb-1010.md) with several entirely new features.

[MariaDB 10.11.4](mariadb-10-11-4-release-notes.md) is a [_**Stable (GA)**_](../../mariadb-release-criteria.md) release.

**For an overview of** [**MariaDB 10.11**](what-is-mariadb-1011.md) **see the**[**What is MariaDB 10.11?**](what-is-mariadb-1011.md) **page.**

Thanks, and enjoy MariaDB!

## Notable Items

### InnoDB

* Server crashes in st\_join\_table::choose\_best\_splitting ([MDEV-31403](https://jira.mariadb.org/browse/MDEV-31403))
* Crash with condition pushable into derived and containing outer reference ([MDEV-31240](https://jira.mariadb.org/browse/MDEV-31240))
* InnoDB does not free UNDO after the fix of [MDEV-30671](https://jira.mariadb.org/browse/MDEV-30671) ([MDEV-31234](https://jira.mariadb.org/browse/MDEV-31234))
* InnoDB hang fixes ([MDEV-31158](https://jira.mariadb.org/browse/MDEV-31158), [MDEV-31343](https://jira.mariadb.org/browse/MDEV-31343), [MDEV-31350](https://jira.mariadb.org/browse/MDEV-31350))
* [Innodb\_buffer\_pool\_read\_requests](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/innodb-status-variables#innodb_buffer_pool_read_requests) is not updated correctly ([MDEV-31309](https://jira.mariadb.org/browse/MDEV-31309))
* InnoDB monitor trx\_rseg\_history\_len was accidentally disabled by default ([MDEV-31308](https://jira.mariadb.org/browse/MDEV-31308))
* Revert "[MDEV-30473](https://jira.mariadb.org/browse/MDEV-30473) : Do not allow GET\_LOCK() / RELEASE\_LOCK() in cluster"

### Optimizer

* Crash with condition pushable into derived and containing outer reference ([MDEV-31403](https://jira.mariadb.org/browse/MDEV-31403) [MDEV-31240](https://jira.mariadb.org/browse/MDEV-31240))
* Crash with [EXPLAIN EXTENDED](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/analyze-and-explain-statements/explain) for multi-table update of system table ([MDEV-31224](https://jira.mariadb.org/browse/MDEV-31224))

### Security

* Fixes for the following [security vulnerabilities](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/security):
  * CVE-`-``#`

## Changelog

For a complete list of changes made in [MariaDB 10.11.4](mariadb-10-11-4-release-notes.md), with links to detailed\
information on each push, see the [changelog](../../changelogs/changelogs-mariadb-10-11-series/mariadb-10-11-4-changelog.md).

## Contributors

For a full list of contributors to [MariaDB 10.11.4](mariadb-10-11-4-release-notes.md), see the [MariaDB Foundation release announcement](https://mariadb.org/mariadb-10-11-4-10-10-5-10-9-7-10-6-14-10-5-21-10-4-30-now-available/).

Be notified of new MariaDB Server releases automatically by [subscribing](https://lists.mariadb.org/postorius/lists/announce.lists.mariadb.org/) to the MariaDB Foundation community announce 'at' lists.mariadb.org announcement list (this is a low traffic, announce-only list). MariaDB plc customers will be notified for all new releases, security issues and critical bug fixes for all MariaDB plc products thanks to the Notification Services.

MariaDB may already be included in your favorite OS distribution. More\
information can be found on the[Distributions which Include MariaDB](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/readme-1)\
page.

{% @marketo/form formid="4316" formId="4316" %}
