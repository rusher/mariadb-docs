# MariaDB 10.1.5 Release Notes

The most recent release of [MariaDB 10.1](changes-improvements-in-mariadb-10-1.md) is:[**MariaDB 10.1.48**](mariadb-10148-release-notes.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.1.48/)

[Download](https://downloads.mariadb.org/mariadb/10.1.5)[Release Notes](mariadb-10-1-5-release-notes.md)[Changelog](../../changelogs/changelogs-mariadb-101-series/mariadb-10-1-5-changelog.md)[Overview of 10.1](changes-improvements-in-mariadb-10-1.md)

**Release date:** 4 Jun 2015

[MariaDB 10.1](changes-improvements-in-mariadb-10-1.md) is the current development series of MariaDB. It is an evolution\
of [MariaDB 10.0](../release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md) with several entirely new features not found anywhere else\
and with backported and reimplemented features from MySQL 5.6 and 5.7.

[MariaDB 10.1.5](mariadb-10-1-5-release-notes.md) is a [_**Beta**_](../../../mariadb-release-criteria.md) release.

**For an overview of** [**MariaDB 10.1**](changes-improvements-in-mariadb-10-1.md) **see the**[**What is MariaDB 10.1?**](changes-improvements-in-mariadb-10-1.md) **page.**

Thanks, and enjoy MariaDB!

## Notable Changes

* New status variables [Binlog\_group\_commit\_trigger\_count](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-status-variables#binlog_group_commit_trigger_count), [Binlog\_group\_commit\_trigger\_timeout](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-status-variables#binlog_group_commit_trigger_timeout), and [Binlog\_group\_commit\_trigger\_lock\_wait](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-status-variables#binlog_group_commit_trigger_lock_wait) used to examine which triggers caused a group commit to be made.
* [mysqldump](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/legacy-clients-and-utilities/mysqldump) has been speeded up for large tables ([MDEV-6714](https://jira.mariadb.org/browse/MDEV-6714))
* A new column, INFO\_BINARY, has been added to the [Information Schema PROCESSLIST Table](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-processlist-table) in order to avoid truncating queries with binary data ([MDEV-7807](https://jira.mariadb.org/browse/MDEV-7807))
* [Spider](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider) updated to 3.2.21.
* [Connect](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/connect) updated to 1.03.0007
* Encryption for temporary files: temporary files created by the server (for binary log caches, for filesort, etc) are now encrypted if the encryption plugin is loaded and `--encrypt-tmp-files` was specified.
* Numerous [encryption](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption) bugfixes.
* New system variable [max\_digest\_length](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/server-system-variables#max_digest_length) allowing statement digests to be calculated using different lengths.
* [Audit Plugin](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/mariadb-audit-plugin) upgraded to 1.3.0, including the QUERY\_DCL filter option.

### New and Deprecated Distributions

As per the [MariaDB Deprecation Policy](../../../mariadb-platform-deprecation-policy.md), this will\
be the final release of [MariaDB 10.1](changes-improvements-in-mariadb-10-1.md) for Fedora 19 "Schrödinger's Cat", Ubuntu\
10.04 LTS "Lucid", and Mint 9 LTS "Isadora". When the next version of [MariaDB\
10.1](changes-improvements-in-mariadb-10-1.md) is released, repositories for these distributions will go away.

We have also added a couple of new Linux distributions with this release. Both\
Fedora 21 and Ubuntu 15.04 "Vivid" repositories are now available. As this is\
the first release with these repositories, they are considered experimental.\
Please [let us know](https://mariadb.org/jira) if you run into any issues with\
them.

Repositories exist for 10.1, but because 10.1 is still Beta, they are not\
visible in the[repository configuration tool](https://downloads.mariadb.org/mariadb/repositories/).\
To configure a 10.1 apt, yum, or zypper repository using the tool, simply\
select 10.0 and then when executing the instructions, change all occurrences of\
'10.0' to '10.1'.

For a complete list of changes made in [MariaDB 10.1.5](mariadb-10-1-5-release-notes.md), with links to detailed\
information on each push, see the [changelog](../../changelogs/changelogs-mariadb-101-series/mariadb-10-1-5-changelog.md).

Be notified of new MariaDB Server releases automatically by [subscribing](https://lists.mariadb.org/postorius/lists/announce.lists.mariadb.org/) to the MariaDB Foundation community announce 'at' lists.mariadb.org announcement list (this is a low traffic, announce-only list). MariaDB plc customers will be notified for all new releases, security issues and critical bug fixes for all MariaDB plc products thanks to the Notification Services.

MariaDB may already be included in your favorite OS distribution. More\
information can be found on the[Distributions which Include MariaDB](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/distributions-including-mariadb)\
page.

{% @marketo/form formid="4316" formId="4316" %}
