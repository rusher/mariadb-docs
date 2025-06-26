# MariaDB 10.2.11 Release Notes

The most recent release of [MariaDB 10.2](what-is-mariadb-102.md) is:[**MariaDB 10.2.44**](mariadb-10244-release-notes.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.2.44/)

[Download](https://downloads.mariadb.org/mariadb/10.2.11)[Release Notes](mariadb-10211-release-notes.md)[Changelog](../../changelogs/changelogs-mariadb-102-series/mariadb-10211-changelog.md)[Overview of 10.2](what-is-mariadb-102.md)

**Release date:** 28 Nov 2017

[MariaDB 10.2](what-is-mariadb-102.md) is the current stable series of MariaDB. It is an evolution\
of [MariaDB 10.1](../release-notes-mariadb-10-1-series/changes-improvements-in-mariadb-10-1.md) with several entirely new features not found anywhere else\
and with backported and reimplemented features from MySQL 5.6 and 5.7.

[MariaDB 10.2.11](mariadb-10211-release-notes.md) is a [_**Stable (GA)**_](../../../mariadb-release-criteria.md) release.

**For an overview of** [**MariaDB 10.2**](what-is-mariadb-102.md) **see the**[**What is MariaDB 10.2?**](what-is-mariadb-102.md) **page.**

Thanks, and enjoy MariaDB!

## Notable Changes

### InnoDB

* [MDEV-13206](https://jira.mariadb.org/browse/MDEV-13206) INSERT ON DUPLICATE KEY UPDATE foreign key fail
* Support CRC32 SSE2 implementation under Windows
* [MDEV-13795](https://jira.mariadb.org/browse/MDEV-13795)/[MDEV-14332](https://jira.mariadb.org/browse/MDEV-14332) Corruption during online table-rebuilding ALTER when VIRTUAL columns exist
* [MDEV-13328](https://jira.mariadb.org/browse/MDEV-13328) ALTER TABLE…DISCARD TABLESPACE takes a lot of time
* [MDEV-14140](https://jira.mariadb.org/browse/MDEV-14140) IMPORT TABLESPACE must not go beyond FSP\_FREE\_LIMIT
* [MDEV-14244](https://jira.mariadb.org/browse/MDEV-14244) [MariaDB 10.2.10](mariadb-10210-release-notes.md) fails to run on Debian Stretch with ext3 and O\_DIRECT
* [MDEV-14219](https://jira.mariadb.org/browse/MDEV-14219) Allow online table rebuild when encryption or compression parameters change

### [MariaDB Backup](broken-reference)

* [MDEV-14499](https://jira.mariadb.org/browse/MDEV-14499) mariadb-backup 10.2 fails to back up a multi-file InnoDB system tablespace
* [MDEV-14447](https://jira.mariadb.org/browse/MDEV-14447) mariadb-backup incremental incorrectly extends system tablespace for multi-file innodb\_data\_file\_path
* [MDEV-13560](https://jira.mariadb.org/browse/MDEV-13560) Copy all innodb undo tablespaces from the backup directory to destination

### Other

* [Mroonga](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/mroonga) updated to 7.07.
* As per the [MariaDB Deprecation Policy](../../../mariadb-platform-deprecation-policy.md), this will be the last release of [MariaDB 10.2](what-is-mariadb-102.md) for RHEL 7.2 and CentOS 7.2. Starting with the next 10.2 release we will be building MariaDB for CentOS 7 and RHEL 7 on version 7.3.
* [Repositories](https://downloads.mariadb.org/mariadb/repositories/) for Ubuntu 17.10 Artful added

### Security Fixes

* Fixes for the following [security vulnerabilities](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/security):
  * CVE-\`-\`\`\`

## Notes

For a complete list of changes made in [MariaDB 10.2.11](mariadb-10211-release-notes.md), with links to detailed\
information on each push, see the [changelog](../../changelogs/changelogs-mariadb-102-series/mariadb-10211-changelog.md).

{% include "https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/~/reusable/vX1KAy0t1XuYJaGsK28T/" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
