# MariaDB 10.4.9 Release Notes

The most recent release of [MariaDB 10.4](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/broken-reference/README.md) is:[**MariaDB 10.4.34**](mariadb-10-4-34-release-notes.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.4.34/)

After an upgrade MariaDB Server can crash if InnoDB tables exist with a `FULLTEXT INDEX` and a `FOREIGN KEY` constraint attached to them. We got reports that the crash already will be encountered on startup, but a crash is also possible at a later stage. See [MDEV-20987](https://jira.mariadb.org/browse/MDEV-20987) for more details.**Do not download or use this release.**

[Download](https://mariadb.com/downloads/)[Release Notes](mariadb-1049-release-notes.md)[Changelog](../../changelogs/changelogs-mariadb-10-4-series/mariadb-1049-changelog.md)[Overview of 10.4](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/broken-reference/README.md)

[_Alternate download from mariadb.org_](https://downloads.mariadb.org/mariadb/10.4.9/)

**Release date:** 5 Nov 2019

[MariaDB 10.4](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/broken-reference/README.md) is the current _stable_ series of MariaDB. It is an evolution\
of [MariaDB 10.3](../release-notes-mariadb-10-3-series/what-is-mariadb-103.md) with several entirely new features not found anywhere else\
and with backported and reimplemented features from MySQL.

[MariaDB 10.4.9](mariadb-1049-release-notes.md) will be a [_**Stable (GA)**_](../../../mariadb-release-criteria.md) release.

**For an overview of** [**MariaDB 10.4**](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/broken-reference/README.md) **see the**[**What is MariaDB 10.4?**](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/broken-reference/README.md) **page.**

Thanks, and enjoy MariaDB!

## Notable Changes

Notable changes of this release include:

* [MDEV-20864](https://jira.mariadb.org/browse/MDEV-20864): Debug-only option [innodb\_change\_buffer\_dump](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_change_buffer_dump) for dumping the contents of the InnoDB change buffer to the server error log at startup.
* mariadb-backup:
  * [MDEV-18438](https://jira.mariadb.org/browse/MDEV-18438): mbstream recreates xtrabackup\_info on same directory as backup file
  * [MDEV-20703](https://jira.mariadb.org/browse/MDEV-20703): mariabackup creates binlog files in server binlog directory on --prepare --export step
* FULLTEXT INDEX:
  * [MDEV-19647](https://jira.mariadb.org/browse/MDEV-19647): Server hangs after dropping full text indexes and restart
  * [MDEV-19529](https://jira.mariadb.org/browse/MDEV-19529): InnoDB hang on `DROP FULLTEXT INDEX`
  * [MDEV-19073](https://jira.mariadb.org/browse/MDEV-19073): FTS row mismatch after crash recovery
  * [MDEV-20621](https://jira.mariadb.org/browse/MDEV-20621): FULLTEXT INDEX activity causes InnoDB hang
* [MDEV-20927](https://jira.mariadb.org/browse/MDEV-20927): Duplicate key with auto increment
* ALTER TABLE:
  * [MDEV-20799](https://jira.mariadb.org/browse/MDEV-20799): DROP Virtual Column crash
  * [MDEV-20852](https://jira.mariadb.org/browse/MDEV-20852): BtrBulk is unnecessarily holding `dict_index_t::lock`
* System-Versioned Tables:
  * [MDEV-16210](https://jira.mariadb.org/browse/MDEV-16210): FK constraints on versioned tables use historical rows, which may cause constraint violation
  * [MDEV-20812](https://jira.mariadb.org/browse/MDEV-20812): Unexpected `ER_ROW_IS_REFERENCED_2` or server crash in `row_ins_foreign_report_err` upon DELETE from versioned table with FK
* [MDEV-20117](https://jira.mariadb.org/browse/MDEV-20117): corruption after instant DROP/reorder COLUMN
* [Galera wsrep library](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/what-is-mariadb-galera-cluster/README.md) updated to 26.4.3
* Packages for Ubuntu 19.10 Eoan have been added in this release
* Fixes for the following [security vulnerabilities](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/security):
  * [CVE-2019-2974](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-2974)
  * [CVE-2019-2938](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-2938)
  * [CVE-2020-2780](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-2780)
  * [CVE-2021-2144](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-2144)

## Changelog

For a complete list of changes made in [MariaDB 10.4.9](mariadb-1049-release-notes.md), with links to detailed\
information on each push, see the [changelog](../../changelogs/changelogs-mariadb-10-4-series/mariadb-1049-changelog.md).

## Contributors

For a full list of contributors to [MariaDB 10.4.9](mariadb-1049-release-notes.md), see the [MariaDB Foundation release announcement](https://mariadb.org/mariadb-10-4-9-10-3-19-and-10-2-28-10-1-42-and-5-5-66-now-available/).

Be notified of new MariaDB Server releases automatically by [subscribing](https://lists.mariadb.org/postorius/lists/announce.lists.mariadb.org/) to the MariaDB Foundation community announce 'at' lists.mariadb.org announcement list (this is a low traffic, announce-only list). MariaDB plc customers will be notified for all new releases, security issues and critical bug fixes for all MariaDB plc products thanks to the Notification Services.

MariaDB may already be included in your favorite OS distribution. More\
information can be found on the[Distributions which Include MariaDB](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/distributions-including-mariadb)\
page.

{% @marketo/form formid="4316" formId="4316" %}
