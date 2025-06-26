# MariaDB 10.1.10 Release Notes

The most recent release of [MariaDB 10.1](changes-improvements-in-mariadb-10-1.md) is:[**MariaDB 10.1.48**](mariadb-10148-release-notes.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.1.48/)

[Download](https://downloads.mariadb.org/mariadb/10.1.10)[Release Notes](mariadb-10110-release-notes.md)[Changelog](../../changelogs/changelogs-mariadb-101-series/mariadb-10110-changelog.md)[Overview of 10.1](changes-improvements-in-mariadb-10-1.md)

**Release date:** 24 Dec 2015

[MariaDB 10.1](changes-improvements-in-mariadb-10-1.md) is the current stable series of MariaDB. It is an evolution\
of [MariaDB 10.0](../release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md) with several entirely new features not found anywhere else\
and with backported and reimplemented features from MySQL 5.6 and 5.7.

[MariaDB 10.1.10](mariadb-10110-release-notes.md) is a [_**Stable (GA)**_](../../../mariadb-release-criteria.md) release.

**For a complete overview of** [**MariaDB 10.1**](changes-improvements-in-mariadb-10-1.md) **see the**[**What is MariaDB 10.1?**](changes-improvements-in-mariadb-10-1.md) **page.**

Thanks, and enjoy MariaDB!

## Notable Changes

* [Spider](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider) updated to 3.2.37
  * new variable, [spider\_connect\_error\_interval](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider/spider-system-variables)
* [MDEV-7384](https://jira.mariadb.org/browse/MDEV-7384): [mysqlcheck](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/legacy-clients-and-utilities/mysqlcheck) now supports `--persistent` option, when used\
  together with `--analyze` option, it will force[Engine-independent Statistics](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/query-optimizations/statistics-for-optimizing-queries/engine-independent-table-statistics) for\
  this table to be updated.
* [MDEV-9288](https://jira.mariadb.org/browse/MDEV-9288): On POWER8 architecture MariaDB now uses hardware accelerated\
  crc32.
* New variable [innodb\_buffer\_pool\_dump\_pct](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables) specifies the percentage of the [buffer pool](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-buffer-pool) to dump.
* Fixes for the following [security vulnerabilities](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/security):
  * [CVE-2016-0546](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2016-0546)
  * [CVE-2016-0505](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2016-0505)
  * [CVE-2016-0596](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2016-0596)
  * [CVE-2016-0597](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2016-0597)
  * [CVE-2016-0616](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2016-0616)
  * [CVE-2016-0598](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2016-0598)
  * [CVE-2016-0600](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2016-0600)
  * [CVE-2016-0606](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2016-0606)
  * [CVE-2016-0608](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2016-0608)
  * [CVE-2016-0609](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2016-0609)
  * [CVE-2016-0642](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2016-0642)
  * [CVE-2016-0651](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2016-0651)
  * [CVE-2016-2047](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2016-2047): [MDEV-9212](https://jira.mariadb.org/browse/MDEV-9212): Fixed incorrect implementation of the `--ssl-verify-server-cert`\
    option that allowed a malicious attacker (with a capability to perform a\
    man-in-the-middle attack) to replace the server SSL certificate, bypassing\
    the client-side hostname verification. This vulnerability was discovered by\
    Paul Kehrer and Alex Gaynor.

This release includes all bug fixes from [MariaDB 5.5.47](../release-notes-mariadb-5-5-series/mariadb-5547-release-notes.md), [MariaDB 10.0.23](../release-notes-mariadb-10-0-series/mariadb-10023-release-notes.md), and[MariaDB Galera Cluster 10.0.23](../mariadb-galera-cluster-releases/mariadb-galera-100-release-notes/mariadb-galera-cluster-10023-release-notes.md)\
releases.

### SLES 11 Support

Previous builds of [MariaDB 10.1](changes-improvements-in-mariadb-10-1.md) for Suse Linux Enterprise Server (SLES) 11 only\
supported SLES 11 SP3 and SP4. Starting with this release, SLES 11 builds for\
x86\_64 also support SLES 11 SP1 and SP2.

### Deprecated Distributions

As per the [MariaDB Deprecation Policy](../../../mariadb-platform-deprecation-policy.md), this will be the\
last release of [MariaDB 10.1](changes-improvements-in-mariadb-10-1.md) for Fedora 21.

## Changelog

For a complete list of changes made in [MariaDB 10.1.10](mariadb-10110-release-notes.md), with links to detailed\
information on each push, see the [changelog](../../changelogs/changelogs-mariadb-101-series/mariadb-10110-changelog.md).

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
