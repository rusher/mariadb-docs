---
hidden: true
---

# MariaDB 11.8.3 Release Notes

{% include "../../.gitbook/includes/unreleased-11-8.md" %}

<!--
<a href="https://mariadb.com/downloads" class="button primary">Download</a> <a href="mariadb-11.8.3-release-notes.md" class="button secondary">Release Notes</a> <a href="../changelogs/changelogs-mariadb-11-8-series/mariadb-11.8.3-changelog.md" class="button secondary">Changelog</a> <a href="what-is-mariadb-118.md" class="button secondary">Overview of 11.8</a>

[<sup>_Alternate download from mariadb.org_</sup>](https://downloads.mariadb.org/mariadb/11.8.3/)

**Release date:** ?
-->

MariaDB 11.8.3 is a [_**Stable (GA)**_](../about/release-criteria.md) release. It is an evolution of [MariaDB 11.7](../old-releases/mariadb-11-7-rolling-releases/what-is-mariadb-117.md) with several entirely new features.

[MariaDB 11.8](what-is-mariadb-118.md) is a [long-term release](https://mariadb.org/11-8-is-lts/).

{% hint style="success" %}
**For an overview of MariaDB 11.8 see the** [**MariaDB 11.8 Changes and Improvements**](what-is-mariadb-118.md) **page.**
{% endhint %}

Thanks, and enjoy MariaDB!

## Notable Items

### Storage Engines

#### InnoDB

* After SET GLOBAL innodb\_buffer\_pool\_size was aborted while attempting to shrink the buffer pool, executing SET GLOBAL innodb\_adaptive\_hash\_index=ON could lead to corruption of the adaptive hash index. (MDEV-36863)
* Fatal InnoDB error: Unknown error Temp file write failure (MDEV-36017)
* When innodb\_buffer\_pool\_size is being shrunk while there are no data pages cached, InnoDB could hang or crash. (MDEV-37263)
* After a successful shrinking of innodb\_buffer\_pool\_size, there will be no message about it in the server error log.
  * After a failed shrinking of innodb\_buffer\_pool\_size, the adaptive hash index will not be re-enabled if innodb\_adaptive\_hash\_index was ON when SET GLOBAL innodb\_buffer\_pool\_size=... started to execute. (MDEV-36868)
* AUTO\_INCREMENT leads to non-serializable on results (MDEV-36330)
* Vector index was corrupted if one statement was rolled back (e.g. insert violating a unique constraint) in the middle of a larger transaction. (MDEV-37068)

#### Aria

* Assertion when adding FK to MyISAM/Aria table with a vector index (MDEV-37022)


### Data Definition - Alter Table

* Adding (with ALTER TABLE) a UNIQUE constraint that is USING HASH to a table with foreign keys could've caused the table to become corrupted. (MDEV-36852)
* DROP DEFAULT makes SHOW CREATE non-idempotent (MDEV-29001)

### Partitioning

* Server crashes in do\_mark\_index\_columns instead of ER\_DUP\_ENTRY on partitioned table (MDEV-36817)
* A replica would crash while replicating UPDATE and DELETE DML statements that target a table which previously had a partition that was converted to a separate table via ALTER TABLE .. CONVERT PARTITION .. TO TABLE. For example, if the command looked like ALTER TABLE t1 CONVERT PARTITION p1 TO TABLE t\_new; the replica would crash when trying to update/deleterows in table t1 after running the command. (MDEV-36906)

### Data Definition - Create Table

* CREATE OR REPLACE with self-referencing CHECK hangs forever, cannot be killed (MDEV-29155)

### Server

* Segfault on INTERSECT ALL with UNION in Oracle mode (MDEV-25158)
* In certain cases privileges on sequences were too restrictive, for example, SELECT on a table might've erroneously required INSERT privilege on a sequences (MDEV-36870)


### mariabackup

* This commit fixes a bug where Aria tables are used in (master-\>slave1-\>slave2) and a backup is taken on slave2. In this case it is possible that the replication position in the backup, stored in mysql.gtid\_slave\_pos, will be wrong. This will lead to replication errors if one is trying to use the backup as a new slave. (MDEV-36143)
* Maria-backup would crash during the 'maria\_recovery' part. This could happen if server was doing repair or creating indexes while the
backup was running. (MDEV-36860)

### Optimizer

* MariaDB server crash when a query includes a derived table containing unnamed column. (MDEV-24588)
* Crash in add\_keyuses\_for\_splitting() when joining with a derived table (MDEV-30711)
* Split Materialized code: last\_refills is never set in 11.0+ (MDEV-36323)
* Don't generate index\_merge plans, if a column is present in both Secondary Key and Primary Key indexes and either of the indexes include it with DESC order (as the scan itself is not a ROR scan). (MDEV-36410)
* Incorrect handling of null values on join conditions. (MDEV-37057)

### JSON

* Starting from 10.11.12, Incorrect handling of UTF-8 characters (and other character sets requiring more than a single byte representation) in the minimum/maximum positions of a table during the execution of ANALYZE TABLE tbl PERSISTENT FOR ALL resulted in an endless loop consuming more memory and prevented the server from terminating. (MDEV-36765)

### Galera

* galera\_3nodes.inconsistency\_shutdown test occasionally hangs (MDEV-36968)
* The galera RPM wasn't buildable on Fedora 41 or later because of changes rpmbuild. The build script has been changed to be compatible with newer rpmbuild behaviour. (MDEV-35108)

### Replication

* semi sync makes the master unresponsive when a replica is stopped (MDEV-36934)
* parallel slave ALTER-SEQUNCE attempted to binlog out-of-order (MDEV-35570)

### Stored routines

* Crash when calling stored function in FOR loop argument (MDEV-26115)

### Authentication and Privilege System

* ALTER TABLE require ALTER privilege on sequence from DEFAULT value expression (MDEV-36280)

### Locking

* Deadlock does not rollback transaction fully (MDEV-36959)

### Data Manipulation - Insert

* UNIQUE constraint that was USING HASH and UNIQUE constrant WITHOUT OVERLAPS could be violated under heavy load in READ COMMITTED transaction isolation mode. (MDEV-37199)

### Character Sets

* Fresh MariaDB 11.4 installation gives errors when configuring utf8 (MDEV-36815)

### Plugin - AWS key management

* aws\_key\_management compilation was previously broken, is now fixed. plugin can be compiled again. As before, -DNOT\_FOR\_DISTRIBUTION=ON  is necessary to build it. (MDEV-30831)

### Packaging

* mariadb systemd mult-instance service was changed to not attempt changes to the permissions on its pam helper server. This prevented unconstructive behaviour and errors in the systemd journal when starting the mariadb@.service. (MDEV-36738)

### Docker

* The new parameter innodb\_linux\_aio controls which Linux implementation to use for innodb\_use\_native\_aio=ON.
  * innodb\_linux\_aio=auto is equivalent to innodb\_linux\_aio=io\_uring when it is available, and falling back to innodb\_linux\_aio=aio when not.
  * Previously, only one implementation (libaio or io\_uring) was available. Currently, if io\_uring is disabled in the environment, we will fall back to the older libaio interface. (MDEV-36234)

### Sequences

* Remove the error codes added to 10.11 by the MDEV-36032 patch (MDEV-36856)

### XA

* DML committed within XA transaction block after deadlock error and implicit rollback (MDEV-37141)

## Changelog

For a complete list of changes made in MariaDB 11.8.3, with links to detailed information on each push, see the [changelog](../changelogs/changelogs-mariadb-11-8-series/mariadb-11.8.3-changelog.md).

{% include "../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}
<!-- This page is licensed: CC BY-SA / Gnu FDL -->

{% @marketo/form formid="4316" formId="4316" %}
