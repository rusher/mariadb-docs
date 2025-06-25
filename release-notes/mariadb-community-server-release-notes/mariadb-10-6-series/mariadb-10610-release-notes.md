# MariaDB 10.6.10 Release Notes

The most recent release of [MariaDB 10.6](what-is-mariadb-106.md) is:[**MariaDB 10.6.21**](mariadb-10-6-21-release-notes.md) Stable (GA) [Download Now](https://mariadb.com/downloads/)[_Alternate download from mariadb.org_](https://downloads.mariadb.org/mariadb/10.6.21/)

[Download 10.6.10](https://downloads.mariadb.org/mariadb/10.6.10/)[Release Notes](mariadb-10610-release-notes.md)[Changelog](../changelogs/changelogs-mariadb-106-series/mariadb-10610-changelog.md)[Overview of 10.6](what-is-mariadb-106.md)

**Release date:** 19 Sep 2022

[MariaDB 10.6](what-is-mariadb-106.md) is the current long-term maintenance stable series of MariaDB, maintained until July 2026. It is an evolution of [MariaDB 10.5](../mariadb-10-5-series/what-is-mariadb-105.md) with several entirely new features.

[MariaDB 10.6.10](mariadb-10610-release-notes.md) is a [_**Stable (GA)**_](../../mariadb-release-criteria.md) release.

**For an overview of** [**MariaDB 10.6**](what-is-mariadb-106.md) **see the**[**What is MariaDB 10.6?**](what-is-mariadb-106.md) **page.**

Thanks, and enjoy MariaDB!

## Notable Items

### Issues Fixed

* Assertion mysql\_mutex\_assert\_owner(\&log\_sys.flush\_order\_mutex) failed in mtr\_t::commit() ([MDEV-29383](https://jira.mariadb.org/browse/MDEV-29383))
* Frequent "Data structure corruption" in InnoDB after OOM ([MDEV-29374](https://jira.mariadb.org/browse/MDEV-29374))
* Recovery or backup of instant ALTER TABLE is incorrect ([MDEV-29438](https://jira.mariadb.org/browse/MDEV-29438))
* InnoDB Temporary Tablespace (ibtmp1) is continuously growing ([MDEV-28240](https://jira.mariadb.org/browse/MDEV-28240))
* Full text index corruption if shutdown before changes are fully flushed ([MDEV-29342](https://jira.mariadb.org/browse/MDEV-29342))
* [JSON\_VALUE()](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_value) does not parse NULL properties properly ([MDEV-27151](https://jira.mariadb.org/browse/MDEV-27151))
* InnoDB hangs on multiple concurrent requests of a cold ROW\_FORMAT=COMPRESSED page ([MDEV-27983](https://jira.mariadb.org/browse/MDEV-27983))

### Security

* Fixes for the following [security vulnerabilities](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/security):
  * CVE-\`-\`\`\`

## Changelog

For a complete list of changes and bugfixes made in [MariaDB 10.6.10](mariadb-10610-release-notes.md), with links to detailed\
information on each push, see the [changelog](../changelogs/changelogs-mariadb-106-series/mariadb-10610-changelog.md).

## Contributors

For a full list of contributors to [MariaDB 10.6.10](mariadb-10610-release-notes.md), see the [MariaDB Foundation release announcement](https://mariadb.org/mariadb-10-9-3-10-8-5-10-7-6-and-10-6-10-now-available/).

Be notified of new MariaDB Server releases automatically by [subscribing](https://lists.mariadb.org/postorius/lists/announce.lists.mariadb.org/) to the MariaDB Foundation community announce 'at' lists.mariadb.org announcement list (this is a low traffic, announce-only list). MariaDB plc customers will be notified for all new releases, security issues and critical bug fixes for all MariaDB plc products thanks to the Notification Services.

MariaDB may already be included in your favorite OS distribution. More\
information can be found on the[Distributions which Include MariaDB](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/distributions-including-mariadb)\
page.

{% @marketo/form formid="4316" formId="4316" %}
