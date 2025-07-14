# MariaDB 10.3.7 Release Notes

The most recent release of [MariaDB 10.3](what-is-mariadb-103.md) is:[**MariaDB 10.3.39**](mariadb-10-3-39-release-notes.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.3.39/)

[Download](https://downloads.mariadb.org/mariadb/10.3.7)[Release Notes](mariadb-1037-release-notes.md)[Changelog](../../changelogs/changelogs-mariadb-10-3-series/mariadb-1037-changelog.md)[Overview of 10.3](what-is-mariadb-103.md)

**Release date:** 25 May 2018

[MariaDB 10.3](what-is-mariadb-103.md) is an evolution\
of [MariaDB 10.2](../release-notes-mariadb-10-2-series/what-is-mariadb-102.md) with several entirely new features not found anywhere else\
and with backported and reimplemented features from MySQL.

[MariaDB 10.3.7](mariadb-1037-release-notes.md) is a [_**Stable (GA)**_](../../../mariadb-release-criteria.md) release.

**For an overview of MariaDB Server 10.3 see the**[**What is MariaDB 10.3?**](what-is-mariadb-103.md) **page or watch the webinar recording,** [**What's new in MariaDB TX 3.0**](https://go.mariadb.com/mariadbtx3.0_webinar_registration-LP.html?utm_source=kb\&utm_campaign=mariadbtx-ondemand-webinar_kb-release-notes)**.**

Thanks, and enjoy MariaDB!

## Notable Changes

Notable changes of this release include:

* [MyRocks Storage Engine](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/myrocks) is now [Stable (GA)](../../../mariadb-release-criteria.md)
* [Spider Storage Engine](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider) is now [Stable (GA)](../../../mariadb-release-criteria.md)
* Two new [ALTER TABLE ... ALGORITHM](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table#algorithm) options, INSTANT and NOCOPY, which allow operations that would require any data files to be modified, or that would require rebuilding the clustered index respectively, to be refused rather than potentially perform slowly, as well as other ALTER TABLE improvements. ([MDEV-13134](https://jira.mariadb.org/browse/MDEV-13134), [MDEV-14168](https://jira.mariadb.org/browse/MDEV-14168))
* The embedded server library now supports SSL when connecting to remote servers.
* New system variable [secure\_timestamp](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/server-system-variables#secure_timestamp) for restricting the direct setting of a session timestamp ([MDEV-15923](https://jira.mariadb.org/browse/MDEV-15923))
* New status variables [feature\_json](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/server-status-variables#feature_json) for monitoring JSON functionality usage and [feature\_system\_versioning](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/server-status-variables#feature_system_versioning) for [system versioning](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/temporal-tables/system-versioned-tables).
* [mysqldump](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/legacy-clients-and-utilities/mysqldump) `--ignore-database` option ([MDEV-13336](https://jira.mariadb.org/browse/MDEV-13336))
* Remove InnoDB 5.7 version number from [MariaDB 10.3](what-is-mariadb-103.md) onwards ([MDEV-16172](https://jira.mariadb.org/browse/MDEV-16172))
* Fixes for instant ADD COLUMN ([MDEV-14906](https://jira.mariadb.org/browse/MDEV-14906), [MDEV-15060](https://jira.mariadb.org/browse/MDEV-15060), [MDEV-15871](https://jira.mariadb.org/browse/MDEV-15871), [MDEV-16065](https://jira.mariadb.org/browse/MDEV-16065))
* Various performance fixes and code cleanup, including clean up InnoDB parameter validation ([MDEV-12218](https://jira.mariadb.org/browse/MDEV-12218))
* Fixed hangs on shutdown ([MDEV-13779](https://jira.mariadb.org/browse/MDEV-13779)) and EXPORT ([MDEV-13987](https://jira.mariadb.org/browse/MDEV-13987))
* As per the [MariaDB Deprecation Policy](../../../mariadb-platform-deprecation-policy.md), this will be the last release of [MariaDB 10.3](what-is-mariadb-103.md) for Debian 7 Wheezy and Fedora 26

For a complete list of changes made in [MariaDB 10.3.7](mariadb-1037-release-notes.md), with links to detailed\
information on each push, see the [changelog](../../changelogs/changelogs-mariadb-10-3-series/mariadb-1037-changelog.md).

## Contributors

For a full list of contributors to [MariaDB 10.3.7](mariadb-1037-release-notes.md), see the [MariaDB Foundation release announcement](https://mariadb.org/mariadb-10-3-7-now-available/).

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
