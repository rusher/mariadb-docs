# MariaDB 10.1.28 Release Notes

The most recent release of [MariaDB 10.1](changes-improvements-in-mariadb-10-1.md) is:[**MariaDB 10.1.48**](mariadb-10148-release-notes.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.1.48/)

[Download](https://downloads.mariadb.org/mariadb/10.1.28)[Release Notes](mariadb-10128-release-notes.md)[Changelog](../../../changelogs/changelogs-mariadb-101-series/mariadb-10128-changelog.md)[Overview of 10.1](changes-improvements-in-mariadb-10-1.md)

**Release date:** 28 Sep 2017

[MariaDB 10.1](changes-improvements-in-mariadb-10-1.md) is the previous stable series of MariaDB. It is an evolution\
of [MariaDB 10.0](../release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md) with several entirely new features not found anywhere else\
and with backported and reimplemented features from MySQL 5.6 and 5.7.

[MariaDB 10.1.28](mariadb-10128-release-notes.md) will be a [_**Stable (GA)**_](../../../mariadb-release-criteria.md) release.

**For an overview of** [**MariaDB 10.1**](changes-improvements-in-mariadb-10-1.md) **see the**[**What is MariaDB 10.1?**](changes-improvements-in-mariadb-10-1.md) **page.**

Thanks, and enjoy MariaDB!

## Notable Changes

### Updates

* [XtraDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) updated to 5.6.37-82.2
* [TokuDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/tokudb) updated to 5.6.37-82.2

### Bug Fixes

* [MDEV-13787](https://jira.mariadb.org/browse/MDEV-13787): Crash in persistent stats wsrep\_on (thd=0x0)
* [MDEV-13899](https://jira.mariadb.org/browse/MDEV-13899): IMPORT TABLESPACE may corrupt ROW\_FORMAT=REDUNDANT tables
* [MDEV-13488](https://jira.mariadb.org/browse/MDEV-13488): InnoDB writes CRYPT\_INFO even though encryption is not enabled (fixes upgrades from 5.5 to 10.1)
* [MDEV-13437](https://jira.mariadb.org/browse/MDEV-13437): InnoDB fails to return error for XA COMMIT or XA ROLLBACK in read-only mode
* [MDEV-13637](https://jira.mariadb.org/browse/MDEV-13637): InnoDB change buffer housekeeping can cause redo log overrun and possibly deadlocks
* [MDEV-12988](https://jira.mariadb.org/browse/MDEV-12988): Mariabackup fails if innodb\_undo\_tablespaces>0
* [MDEV-13471](https://jira.mariadb.org/browse/MDEV-13471): Test failure on innodb.log\_file\_size,4k (fixes Galera when using innodb\_page\_size=4k)
* [MDEV-13814](https://jira.mariadb.org/browse/MDEV-13814): Extra logging when innodb\_log\_archive=ON (XtraDB only)
* [MDEV-13807](https://jira.mariadb.org/browse/MDEV-13807): mariabackup --apply-log-only does generate redo log by performing rollback and possibly other tasks
* [MDEV-13684](https://jira.mariadb.org/browse/MDEV-13684): InnoDB race condition between fil\_crypt\_thread and btr\_scrub\_init

### Encryption

* Temporary files created by merge sort and row log are encrypted if [innodb\_encrypt\_log](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables) is set to `1`, regardless of whether the table encrypted or not ([MDEV-12634](https://jira.mariadb.org/browse/MDEV-12634)).

### Security Fixes

* Fixes for the following [security vulnerabilities](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/security):
  * CVE-\`-\`\`\`

## Notes

For a complete list of changes made in [MariaDB 10.1.28](mariadb-10128-release-notes.md), with links to detailed\
information on each push, see the [changelog](../../../changelogs/changelogs-mariadb-101-series/mariadb-10128-changelog.md).

A file format compatibility bug that was introduced in [MariaDB 10.1.0](mariadb-10-1-0-release-notes.md) was fixed in [MariaDB 10.1.21](mariadb-10121-release-notes.md).\
Using [page\_compression](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-page-compression) or non-default [innodb\_page\_size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables) created files that were incompatible with [MariaDB 10.0](../release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md) or MySQL 5.6. [MariaDB 10.1.21](mariadb-10121-release-notes.md) and higher will convert affected files from earlier [MariaDB 10.1](changes-improvements-in-mariadb-10-1.md) releases to a compatible format.**This prevents a downgrade to earlier** [**MariaDB 10.1**](changes-improvements-in-mariadb-10-1.md) **versions.**[See the commit for details.](https://github.com/MariaDB/server/commit/ab1e6fefd869242d962cb91a006f37bb9ad534a7)

Be notified of new MariaDB Server releases automatically by [subscribing](https://lists.mariadb.org/postorius/lists/announce.lists.mariadb.org/) to the MariaDB Foundation community announce 'at' lists.mariadb.org announcement list (this is a low traffic, announce-only list). MariaDB plc customers will be notified for all new releases, security issues and critical bug fixes for all MariaDB plc products thanks to the Notification Services.

MariaDB may already be included in your favorite OS distribution. More\
information can be found on the[Distributions which Include MariaDB](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/readme-1)\
page.

{% @marketo/form formid="4316" formId="4316" %}
