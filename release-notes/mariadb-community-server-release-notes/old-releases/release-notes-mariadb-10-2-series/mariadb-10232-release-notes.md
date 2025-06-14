# MariaDB 10.2.32 Release Notes

The most recent release of [MariaDB 10.2](what-is-mariadb-102.md) is:[**MariaDB 10.2.44**](mariadb-10244-release-notes.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.2.44/)

[Download](https://downloads.mariadb.org/mariadb/10.2.32/)[Release Notes](mariadb-10232-release-notes.md)[Changelog](../../../changelogs/changelogs-mariadb-102-series/mariadb-10232-changelog.md)[Overview of 10.2](what-is-mariadb-102.md)

**Release date:** 12 May 2020

[MariaDB 10.2](what-is-mariadb-102.md) is a previous stable series of MariaDB. It is an evolution\
of [MariaDB 10.1](../release-notes-mariadb-10-1-series/changes-improvements-in-mariadb-10-1.md) with several entirely new features not found anywhere else\
and with backported and reimplemented features from MySQL 5.6 and 5.7.

[MariaDB 10.2.32](mariadb-10232-release-notes.md) is a [_**Stable (GA)**_](../../../mariadb-release-criteria.md) release.

**For an overview of** [**MariaDB 10.2**](what-is-mariadb-102.md) **see the**[**What is MariaDB 10.2?**](what-is-mariadb-102.md) **page.**

Thanks, and enjoy MariaDB!

## Notable Changes

### Events

* Fixed issue that, from [MariaDB 10.2.28](mariadb-10228-release-notes.md), disabled all [events](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/triggers-events/event-scheduler/events) created by a server with a different `server_id`. Note that the fix does not re-enable affected events. ([MDEV-21758](https://jira.mariadb.org/browse/MDEV-21758))

### Other

* [HeidiSQL](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/graphical-and-enhanced-clients/heidisql) updated to 11.0 ([MDEV-22032](https://jira.mariadb.org/browse/MDEV-22032))
* Mariabackup does not honor ignore\_db\_dirs from server config ([MDEV-19347](https://jira.mariadb.org/browse/MDEV-19347))
* Mariabackup `--ftwrl-wait-timeout` never times out on explicit lock ([MDEV-20230](https://jira.mariadb.org/browse/MDEV-20230))
* FULLTEXT INDEX, Assertion \`\`!table->fts->in\_queue`' failed in` fts\_optimize\_remove\_table\` ([MDEV-21550](https://jira.mariadb.org/browse/MDEV-21550))
* Wrong estimate of affected BLOB columns in update of PRIMARY KEY ([MDEV-22384](https://jira.mariadb.org/browse/MDEV-22384))
* Duplicate key value is silently truncated to 64 characters in `print_keydup_error` ([MDEV-20604](https://jira.mariadb.org/browse/MDEV-20604))
* Session tracking returns incorrectly long tracking data ([MDEV-22504](https://jira.mariadb.org/browse/MDEV-22504))
* Add `pam_user_map.so` file to binary tarball package ([MDEV-21913](https://jira.mariadb.org/browse/MDEV-21913))
* Running out of file descriptors and eventual crash ([MDEV-18027](https://jira.mariadb.org/browse/MDEV-18027))
* mysql\_upgrade is made aware of the upstream slave tables to issue warnings when that takes place ([MDEV-10047](https://jira.mariadb.org/browse/MDEV-10047))
* Corruption for `SET GLOBAL innodb_` string variables ([MDEV-22393](https://jira.mariadb.org/browse/MDEV-22393))
* wsrep performance optimization ([MDEV-7962](https://jira.mariadb.org/browse/MDEV-7962))
* [mysqldump](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/legacy-clients-and-utilities/mysqldump) parameter, `--ignore-table-data`, added ([MDEV-22037](https://jira.mariadb.org/browse/MDEV-22037))
* Server can fail while replicating conditional comments (Bug#28388217)
* [Galera wsrep library](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/what-is-mariadb-galera-cluster/README.md) updated to 25.3.29
* Added the `xml-report` option to [mysql-test-run](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/testing-tools/mariadb-test/mariadb-test-run-pl-options) ([MDEV-22176](https://jira.mariadb.org/browse/MDEV-22176))
* As per the [MariaDB Deprecation Policy](../../../mariadb-platform-deprecation-policy.md), this will be the last release of [MariaDB 10.2](what-is-mariadb-102.md) for Debian 8 "Jessie"
* Fixes for the following [security vulnerabilities](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/security):
  * [CVE-2020-2752](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-2752)
  * [CVE-2020-2812](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-2812)
  * [CVE-2020-2814](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-2814)
  * [CVE-2020-2760](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-2760)
  * [CVE-2020-13249](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-13249)

Upgrading from 10.2 versions earlier than 10.2.17 is **highly recommended**\
for all [**Galera**](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/galera/README.md) users due to bug [MDEV-12837](https://jira.mariadb.org/browse/MDEV-12837) which caused serious stability\
issues with earlier versions. See the bug issue page for more information.\
When upgrading from [MariaDB 10.2.16](mariadb-10216-release-notes.md) or earlier to [MariaDB 10.2.17](mariadb-10217-release-notes.md) or higher,\
running [mysql\_upgrade](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/legacy-clients-and-utilities/mysql_upgrade) is **required** due to changes introduced in [MDEV-14637](https://jira.mariadb.org/browse/MDEV-14637).

## Changelog

For a complete list of changes made in [MariaDB 10.2.32](mariadb-10232-release-notes.md) with links to detailed\
information on each push, see the [changelog](../../../changelogs/changelogs-mariadb-102-series/mariadb-10232-changelog.md).

## Contributors

For a full list of contributors to [MariaDB 10.2.32](mariadb-10232-release-notes.md), see the [MariaDB Foundation release announcement](https://mariadb.org/mariadb-10-4-13-10-3-23-10-2-32-10-1-45-and-5-5-68-now-available).\
Thanks, and enjoy MariaDB!

Be notified of new MariaDB Server releases automatically by [subscribing](https://lists.mariadb.org/postorius/lists/announce.lists.mariadb.org/) to the MariaDB Foundation community announce 'at' lists.mariadb.org announcement list (this is a low traffic, announce-only list). MariaDB plc customers will be notified for all new releases, security issues and critical bug fixes for all MariaDB plc products thanks to the Notification Services.

MariaDB may already be included in your favorite OS distribution. More\
information can be found on the[Distributions which Include MariaDB](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/distributions-including-mariadb)\
page.

{% @marketo/form formid="4316" formId="4316" %}
