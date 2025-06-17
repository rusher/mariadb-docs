# MariaDB 10.6.2 Release Notes

The most recent release of [MariaDB 10.6](what-is-mariadb-106.md) is:[**MariaDB 10.6.21**](mariadb-10-6-21-release-notes.md) Stable (GA) [Download Now](https://mariadb.com/downloads/)[_Alternate download from mariadb.org_](https://downloads.mariadb.org/mariadb/10.6.21/)

[Download 10.6.2](https://downloads.mariadb.org/mariadb/10.6.2/)[Release Notes](mariadb-1062-release-notes.md)[Changelog](../../changelogs/changelogs-mariadb-106-series/mariadb-1062-changelog.md)[Overview of 10.6](what-is-mariadb-106.md)

**Release date:** 18 Jun 2021

[MariaDB 10.6](what-is-mariadb-106.md) is the current development series of MariaDB. It is an evolution\
of [MariaDB 10.5](../mariadb-10-5-series/what-is-mariadb-105.md) with several entirely new features.

[MariaDB 10.6.2](mariadb-1062-release-notes.md) is a [_**Release Candidate (RC)**_](../../mariadb-release-criteria.md) release.

**Do not use non-stable (non-GA) releases in production!**

**For an overview of** [**MariaDB 10.6**](what-is-mariadb-106.md) **see the**[**What is MariaDB 10.6?**](what-is-mariadb-106.md) **page.**

[Register now for our MariaDB Community Server 10.6 webinar to be held 2021-06-29](https://go.mariadb.com/21Q3-WBN-GLBL-OSSG-Community-Server-10.6-2021-06-22_Registration-LP.html?utm_source=KB) and be one of the first to see the biggest features coming in MariaDB Community Server 10.6, with an exclusive opportunity to have your questions answered by MariaDB engineering and product leads.

Thanks, and enjoy MariaDB!

## Notable Changes

### InnoDB

* When [innodb\_adaptive\_hash\_index=OFF](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_adaptive_hash_index) (the default), the following counters (which reflect btr\_cur\_n\_non\_sea) will no longer be updated ([MDEV-25882](https://jira.mariadb.org/browse/MDEV-25882)):
  * adaptive\_hash\_index in [INFORMATION\_SCHEMA.INNODB\_METRICS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb_metrics-table)
  * [Innodb\_adaptive\_hash\_non\_hash\_searches](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/innodb-status-variables#innodb_adaptive_hash_non_hash_searches) in [INFORMATION\_SCHEMA.GLOBAL\_STATUS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-global_status-and-session_status-tables)

### Replication

* [Semisync](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/semisynchronous-replication) replica recovery is introduced. [rpl-semi-sync-slave-enabled = ON](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/semisynchronous-replication#rpl_semi_sync_slave_enabled) server executes a special recovery branch to guarantee its consistency with a primary server ([MDEV-21117](https://jira.mariadb.org/browse/MDEV-21117))

### General

* Error messages now use "MariaDB" instead of "MySQL" ([MDEV-22189](https://jira.mariadb.org/browse/MDEV-22189))
* Implement `FLUSH TABLES tbl_name [, tbl_name] ... WITH READ LOCK` for views ([MDEV-15888](https://jira.mariadb.org/browse/MDEV-15888))
* All statements can be prepared, except `[PREPARE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/prepared-statements/prepare-statement)`, `[EXECUTE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/prepared-statements/execute-statement)`, and `[DEALLOCATE / DROP PREPARE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/prepared-statements/deallocate-drop-prepare)` ([MDEV-16708](https://jira.mariadb.org/browse/MDEV-16708))

## Changelog

For a complete list of changes and bugfixes made in [MariaDB 10.6.2](mariadb-1062-release-notes.md), with links to detailed\
information on each push, see the [changelog](../../changelogs/changelogs-mariadb-106-series/mariadb-1062-changelog.md).

## Contributors

For a full list of contributors to [MariaDB 10.6.2](mariadb-1062-release-notes.md), see the [MariaDB Foundation release announcement](https://mariadb.org/mariadb-10-6-2-now-available/).

**Do not use non-stable (non-GA) releases in production!**

Be notified of new MariaDB Server releases automatically by [subscribing](https://lists.mariadb.org/postorius/lists/announce.lists.mariadb.org/) to the MariaDB Foundation community announce 'at' lists.mariadb.org announcement list (this is a low traffic, announce-only list). MariaDB plc customers will be notified for all new releases, security issues and critical bug fixes for all MariaDB plc products thanks to the Notification Services.

MariaDB may already be included in your favorite OS distribution. More\
information can be found on the[Distributions which Include MariaDB](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/distributions-including-mariadb)\
page.

{% @marketo/form formid="4316" formId="4316" %}
