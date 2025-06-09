# MariaDB 10.3.20 Release Notes

The most recent release of [MariaDB 10.3](what-is-mariadb-103.md) is:[**MariaDB 10.3.39**](mariadb-10-3-39-release-notes.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.3.39/)

Note that this version contains an issue that disabled all events created by a server with a different server\_id. See [MDEV-21758](https://jira.mariadb.org/browse/MDEV-21758) for details.

[Download](https://downloads.mariadb.org/mariadb/10.3.20/)[Release Notes](mariadb-10320-release-notes.md)[Changelog](../../../changelogs/changelogs-mariadb-10-3-series/mariadb-10320-changelog.md)[Overview of 10.3](what-is-mariadb-103.md)

**Release date:** 8 Nov 2019

[MariaDB 10.3](what-is-mariadb-103.md) is the previous stable series of MariaDB, and an evolution of [MariaDB 10.2](../release-notes-mariadb-10-2-series/what-is-mariadb-102.md) with several entirely new features\
not found anywhere else and with backported and reimplemented features from\
MySQL.

[MariaDB 10.3.20](mariadb-10320-release-notes.md) is a [_**Stable (GA)**_](../../../mariadb-release-criteria.md) release.

**For an overview of MariaDB Server 10.3 see the** [**What is MariaDB 10.3?**](what-is-mariadb-103.md) **page.**

Thanks, and enjoy MariaDB!

## Notable Changes

* [MDEV-20987](https://jira.mariadb.org/browse/MDEV-20987): InnoDB fails to start when FTS table has FK relation
* See also the release notes for [MariaDB 10.3.19](mariadb-10319-release-notes.md) for additional items of note
* Fixes for the following [security vulnerabilities](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/security):
  * CVE-\`-\`\`\`

When upgrading from [MariaDB 10.3.8](mariadb-1038-release-notes.md) or earlier to [MariaDB 10.3.9](mariadb-1039-release-notes.md) or higher,\
running `[mysql_upgrade](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/legacy-clients-and-utilities/mysql_upgrade)` is **required** due to changes introduced in[MDEV-14637](https://jira.mariadb.org/browse/MDEV-14637).

## Changelog

For a complete list of changes made in [MariaDB 10.3.20](mariadb-10320-release-notes.md), with links to detailed\
information on each push, see the [changelog](../../../changelogs/changelogs-mariadb-10-3-series/mariadb-10320-changelog.md).

## Contributors

For a full list of contributors to [MariaDB 10.3.20](mariadb-10320-release-notes.md), see the [MariaDB Foundation release announcement](https://mariadb.org/mariadb-10-4-10-10-3-20-10-2-29-and-10-1-43-now-available/).

Be notified of new MariaDB Server releases automatically by [subscribing](https://lists.mariadb.org/postorius/lists/announce.lists.mariadb.org/) to the MariaDB Foundation community announce 'at' lists.mariadb.org announcement list (this is a low traffic, announce-only list). MariaDB plc customers will be notified for all new releases, security issues and critical bug fixes for all MariaDB plc products thanks to the Notification Services.

MariaDB may already be included in your favorite OS distribution. More\
information can be found on the[Distributions which Include MariaDB](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/readme-1)\
page.
