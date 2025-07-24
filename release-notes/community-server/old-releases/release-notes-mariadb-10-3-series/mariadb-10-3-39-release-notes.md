# MariaDB 10.3.39 Release Notes

[Download](https://downloads.mariadb.org/mariadb/10.3.39/)[Release Notes](mariadb-10-3-39-release-notes.md)[Changelog](../../changelogs/changelogs-mariadb-10-3-series/mariadb-10-3-39-changelog.md)[Overview of 10.3](what-is-mariadb-103.md)

**Release date:** 10 May 2023

[MariaDB 10.3](what-is-mariadb-103.md) is the previous stable series of MariaDB, supported until May 2023, and an evolution of [MariaDB 10.2](../release-notes-mariadb-10-2-series/what-is-mariadb-102.md) with several entirely new features not found anywhere else and\
with backported and reimplemented features from MySQL.

[MariaDB 10.3.39](mariadb-10-3-39-release-notes.md) is a [_**Stable (GA)**_](../../about/release-criteria.md) release.

[MariaDB 10.3.39](mariadb-10-3-39-release-notes.md) is the last release of the [MariaDB 10.3](what-is-mariadb-103.md) release series.

**For an overview of MariaDB Server 10.3 see the** [**What is MariaDB 10.3?**](what-is-mariadb-103.md) **page.**

Thanks, and enjoy MariaDB!

## Notable Items

* As per the [MariaDB Maintenance Policy](https://mariadb.org/about/#maintenance-policy), this will be the final release of [MariaDB 10.3](what-is-mariadb-103.md)

### Replication

* Fixed a deadlock on parallel slave involving full image Write event on the sequence engine ([MDEV-29621](https://jira.mariadb.org/browse/MDEV-29621))

### Docker

* Add replication setup to containers contributed by Md Sahil ([MDEV-29762](https://jira.mariadb.org/browse/MDEV-29762))

When upgrading from [MariaDB 10.3.8](mariadb-1038-release-notes.md) or earlier to [MariaDB 10.3.9](mariadb-1039-release-notes.md) or higher,\
running [mysql\_upgrade](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/legacy-clients-and-utilities/mysql_upgrade) is **required** due to changes introduced in[MDEV-14637](https://jira.mariadb.org/browse/MDEV-14637).

### Security

* Fixes for the following [security vulnerabilities](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/security):
  * [CVE-2022-47015](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-47015)

## Changelog

For a complete list of changes made in [MariaDB 10.3.39](mariadb-10-3-39-release-notes.md), with links to detailed\
information on each push, see the [changelog](../../changelogs/changelogs-mariadb-10-3-series/mariadb-10-3-39-changelog.md).

## Contributors

For a full list of contributors to [MariaDB 10.3.39](mariadb-10-3-39-release-notes.md), see the [MariaDB Foundation release announcement](https://mariadb.org/mariadb-10-11-3-10-10-4-10-9-6-10-8-8-10-6-13-10-5-20-10-4-29-and-10-3-39-now-available/).

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
