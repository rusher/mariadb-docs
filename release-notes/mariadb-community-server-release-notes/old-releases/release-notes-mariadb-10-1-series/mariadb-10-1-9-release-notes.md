# MariaDB 10.1.9 Release Notes

The most recent release of [MariaDB 10.1](changes-improvements-in-mariadb-10-1.md) is:[**MariaDB 10.1.48**](mariadb-10148-release-notes.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.1.48/)

[Download](https://downloads.mariadb.org/mariadb/10.1.9)[Release Notes](mariadb-10-1-9-release-notes.md)[Changelog](../../../changelogs/changelogs-mariadb-101-series/mariadb-10-1-9-changelog.md)[Overview of 10.1](changes-improvements-in-mariadb-10-1.md)

**Release date:** 23 Nov 2015

[MariaDB 10.1](changes-improvements-in-mariadb-10-1.md) is the current stable series of MariaDB. It is an evolution\
of [MariaDB 10.0](../release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md) with several entirely new features not found anywhere else\
and with backported and reimplemented features from MySQL 5.6 and 5.7.

[MariaDB 10.1.9](mariadb-10-1-9-release-notes.md) is a [_**Stable (GA)**_](../../../mariadb-release-criteria.md) release.

**For a complete overview of** [**MariaDB 10.1**](changes-improvements-in-mariadb-10-1.md) **see the**[**What is MariaDB 10.1?**](changes-improvements-in-mariadb-10-1.md) **page.**

Thanks, and enjoy MariaDB!

## Notable Changes

* [CONNECT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/connect) engine updated to version 1.04.0003.
  * numerous new [JSON User Defined Functions](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/connect/connect-table-types/connect-json-table-type#json-user-defined-functions).
* The [SHOW SLAVE STATUS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-replica-status) field, `seconds_behind_master`, is now, with [parallel replication](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/parallel-replication), only updated after transactions commit.
* Includes all bug fixes from [MariaDB 5.5.46](../release-notes-mariadb-5-5-series/mariadb-5546-release-notes.md), [MariaDB 10.0.22](../release-notes-mariadb-10-0-series/mariadb-10022-release-notes.md), and [MariaDB Galera Cluster 10.0.22](../mariadb-galera-cluster-releases/mariadb-galera-100-release-notes/mariadb-galera-cluster-10-0-22-release-notes.md) releases.
* Fixes for the following [security vulnerabilities](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/security):
  * [CVE-2015-7744](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2015-7744)
  * [CVE-2016-0610](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2016-0610)
  * [CVE-2016-3471](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2016-3471)

For a complete list of changes made in [MariaDB 10.1.9](mariadb-10-1-9-release-notes.md), with links to detailed\
information on each push, see the [changelog](../../../changelogs/changelogs-mariadb-101-series/mariadb-10-1-9-changelog.md).

Be notified of new MariaDB Server releases automatically by [subscribing](https://lists.mariadb.org/postorius/lists/announce.lists.mariadb.org/) to the MariaDB Foundation community announce 'at' lists.mariadb.org announcement list (this is a low traffic, announce-only list). MariaDB plc customers will be notified for all new releases, security issues and critical bug fixes for all MariaDB plc products thanks to the Notification Services.

MariaDB may already be included in your favorite OS distribution. More\
information can be found on the[Distributions which Include MariaDB](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/readme-1)\
page.

{% @marketo/form formid="4316" formId="4316" %}
