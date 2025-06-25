# MariaDB 10.6.5 Release Notes

The most recent release of [MariaDB 10.6](what-is-mariadb-106.md) is:[**MariaDB 10.6.21**](mariadb-10-6-21-release-notes.md) Stable (GA) [Download Now](https://mariadb.com/downloads/)[_Alternate download from mariadb.org_](https://downloads.mariadb.org/mariadb/10.6.21/)

[Download 10.6.5](https://downloads.mariadb.org/mariadb/10.6.5)[Release Notes](mariadb-1065-release-notes.md)[Changelog](../changelogs/changelogs-mariadb-106-series/mariadb-1065-changelog.md)[Overview of 10.6](what-is-mariadb-106.md)

**Release date:** 8 Nov 2021

[MariaDB 10.6](what-is-mariadb-106.md) is the current stable series of MariaDB. It is an evolution\
of [MariaDB 10.5](../mariadb-10-5-series/what-is-mariadb-105.md) with several entirely new features.

[MariaDB 10.6.5](mariadb-1065-release-notes.md) is a [_**Stable (GA)**_](../../mariadb-release-criteria.md) release.

**For an overview of** [**MariaDB 10.6**](what-is-mariadb-106.md) **see the**[**What is MariaDB 10.6?**](what-is-mariadb-106.md) **page.**

Thanks, and enjoy MariaDB!

## Notable Items

### InnoDB

* Linux after kernel version 5.10 has a io-uring regression causing a write to storage to be lost, or not acknowledged. As such [innodb\_use\_native\_aio](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_use_native_aio) will default to 0 (off) until 5.16. If [innodb\_use\_native\_aio](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_use_native_aio) is enabled in your configuration, a warning will be logged, however it will continue with the io-uring enabled, potentially resulting in a hang, or an assertion later. The long term support kernel 5.14.14 we haven't observed failures, and 5.15.0-rc7 failures have been observed, though less frequently. If you have [innodb\_use\_native\_aio](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_use_native_aio) explicitly enabled, and are using watch out for a lack of InnoDB updates followed by a 10 minute timeout. See [MDEV-26674](https://jira.mariadb.org/browse/MDEV-26674) for details.
* `ALTER TABLE…IMPORT TABLESPACE` fixes ([MDEV-18543](https://jira.mariadb.org/browse/MDEV-18543), [MDEV-20931](https://jira.mariadb.org/browse/MDEV-20931), [MDEV-26131](https://jira.mariadb.org/browse/MDEV-26131), [MDEV-26621](https://jira.mariadb.org/browse/MDEV-26621))
* `innodb_undo_log_truncate` fixes ([MDEV-26445](https://jira.mariadb.org/browse/MDEV-26445), [MDEV-26450](https://jira.mariadb.org/browse/MDEV-26450), [MDEV-26672](https://jira.mariadb.org/browse/MDEV-26672), [MDEV-26864](https://jira.mariadb.org/browse/MDEV-26864))
* Page I/O performance fixes ([MDEV-25215](https://jira.mariadb.org/browse/MDEV-25215), [MDEV-26547](https://jira.mariadb.org/browse/MDEV-26547), [MDEV-26626](https://jira.mariadb.org/browse/MDEV-26626), [MDEV-26819](https://jira.mariadb.org/browse/MDEV-26819))
* Replication timeouts with `XA PREPARE` ([MDEV-26682](https://jira.mariadb.org/browse/MDEV-26682))
* Improved DDL and data dictionary ([MDEV-25919](https://jira.mariadb.org/browse/MDEV-25919))
* Performance fixes ([MDEV-26356](https://jira.mariadb.org/browse/MDEV-26356), [MDEV-26467](https://jira.mariadb.org/browse/MDEV-26467), [MDEV-26826](https://jira.mariadb.org/browse/MDEV-26826))

### Replication

* Memory hogging on slave by ROW event applier is eliminated ([MDEV-26712](https://jira.mariadb.org/browse/MDEV-26712))
* `mysql --binary-mode` now properly handles `\\0` in data ([MDEV-25444](https://jira.mariadb.org/browse/MDEV-25444))
* Fixes race condition between `SHOW BINARY LOGS` and `RESET MASTER` ([MDEV-20215](https://jira.mariadb.org/browse/MDEV-20215))
* Missed statement rollback in case transaction drops or create temporary table is corrected ([MDEV-26833](https://jira.mariadb.org/browse/MDEV-26833))

### Audit Plugin

* The `QUERY_DDL` [server\_audit\_events](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/mariadb-audit-plugin/mariadb-audit-plugin-options-and-system-variables#server_audit_events) setting now logs `CREATE/DROP [PROCEDURE / FUNCTION / USER]` statements. See [MariaDB Audit Plugin - Log Settings](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/mariadb-audit-plugin/mariadb-audit-plugin-log-settings). ([MDEV-23457](https://jira.mariadb.org/browse/MDEV-23457))

### Packaging & Misc

* Session tracking flag in OK\_PACKET ([MDEV-26868](https://jira.mariadb.org/browse/MDEV-26868))
* Some views force server (and mysqldump) to generate invalid SQL for their definitions ([MDEV-26299](https://jira.mariadb.org/browse/MDEV-26299))

### Security

* Fixes for the following [security vulnerabilities](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/security):
  * [CVE-2021-46667](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-46667)
  * [CVE-2021-46662](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-46662)
  * [CVE-2022-27385](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27385)
  * [CVE-2022-27385](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27385)
  * [CVE-2022-31624](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-31624)

## Changelog

For a complete list of changes and bugfixes made in [MariaDB 10.6.5](mariadb-1065-release-notes.md), with links to detailed\
information on each push, see the [changelog](../changelogs/changelogs-mariadb-106-series/mariadb-1065-changelog.md).

## Contributors

For a full list of contributors to [MariaDB 10.6.5](mariadb-1065-release-notes.md), see the [MariaDB Foundation release announcement](https://mariadb.org/mariadb-10-7-1-rc-and-mariadb-10-6-5-10-5-13-10-4-22-10-3-32-and-10-2-41-now-available/).

Be notified of new MariaDB Server releases automatically by [subscribing](https://lists.mariadb.org/postorius/lists/announce.lists.mariadb.org/) to the MariaDB Foundation community announce 'at' lists.mariadb.org announcement list (this is a low traffic, announce-only list). MariaDB plc customers will be notified for all new releases, security issues and critical bug fixes for all MariaDB plc products thanks to the Notification Services.

MariaDB may already be included in your favorite OS distribution. More\
information can be found on the[Distributions which Include MariaDB](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/distributions-including-mariadb)\
page.

{% @marketo/form formid="4316" formId="4316" %}
