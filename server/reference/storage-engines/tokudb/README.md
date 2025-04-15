
# TokuDB

TokuDB has been deprecated by its upstream maintainer. It is disabled from [MariaDB 10.5](../../../../release-notes/mariadb-community-server/what-is-mariadb-105.md) and has been been removed in [MariaDB 10.6](../../../../release-notes/mariadb-community-server/what-is-mariadb-106.md) - [MDEV-19780](https://jira.mariadb.org/browse/MDEV-19780). We recommend [MyRocks](../myrocks/myrocks-in-mariadb-102-vs-mariadb-103.md) as a long-term migration path.


The TokuDB storage engine is for use in high-performance and write-intensive environments, offering increased compression and better performance.


It is available in an open-source version, included with 64-bit MariaDB (but not enabled by default), and an Enterprise edition available from Tokutek.


Official TokuDB Product Specs and Manuals are available on the Percona website. See:


* [TokuDB Documentation](https://www.percona.com/doc/percona-tokudb/index.html)


TokuDB is available on the following distributions:



| Distribution | Introduced |
| --- | --- |
| Distribution | Introduced |
| CentOS 6 64-bit and newer | [MariaDB 5.5.36](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/mariadb-5536-release-notes.md) and [MariaDB 10.0.9](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-1009-release-notes.md) |
| Debian 7 "wheezy"64-bit and newer | [MariaDB 5.5.33](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/mariadb-5533-release-notes.md) and [MariaDB 10.0.5](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-1005-release-notes.md) |
| Fedora 19 64-bit and newer | [MariaDB 5.5.33](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/mariadb-5533-release-notes.md) and [MariaDB 10.0.5](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-1005-release-notes.md) |
| openSUSE 13.1 64-bit and newer | [MariaDB 5.5.41](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/mariadb-5541-release-notes.md) and [MariaDB 10.0.15](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-10015-release-notes.md) |
| Red Hat 6 64-bit and newer | [MariaDB 5.5.36](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/mariadb-5536-release-notes.md) and [MariaDB 10.0.9](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-1009-release-notes.md) |
| Ubuntu 12.10 "quantal" 64-bit and newer | [MariaDB 5.5.33](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/mariadb-5533-release-notes.md) and [MariaDB 10.0.5](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-1005-release-notes.md) |




Note that the default value of [tokudb_pk_insert_mode](tokudb-system-variables.md#tokudb_pk_insert_mode) will prevent row-based replication from working. To use RBR, change the value of this variable.


### Versions of the TokuDB plugin included in MariaDB



| TokuDB Version | Introduced | Maturity |
| --- | --- | --- |
| TokuDB Version | Introduced | Maturity |
| TokuDB from [Percona Server 5.6.49-89.0](https://www.percona.com/doc/percona-server/5.6/release-notes/Percona-Server-5.6.49-89.0.html) | [MariaDB 10.1.46](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10146-release-notes.md) | Stable |
| TokuDB from [Percona Server 5.6.46-86.2](https://www.percona.com/doc/percona-server/5.6/release-notes/Percona-Server-5.6.46-86.2.html) | [MariaDB 10.1.44](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10144-release-notes.md) | Stable |
| TokuDB from [Percona Server 5.6.43-84.3](https://www.percona.com/doc/percona-server/5.6/release-notes/Percona-Server-5.6.43-84.3.html) | [MariaDB 10.1.39](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10139-release-notes.md) | Stable |
| TokuDB from [Percona Server 5.6.42-84.2](https://www.percona.com/doc/percona-server/5.6/release-notes/Percona-Server-5.6.42-84.2.html) | [MariaDB 10.0.38](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-10038-release-notes.md) | Stable |
| TokuDB from [Percona Server 5.6.41-84.1](https://www.percona.com/doc/percona-server/5.6/release-notes/Percona-Server-5.6.41-84.1.html) | [MariaDB 10.1.36](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10136-release-notes.md), [MariaDB 10.0.37](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-10037-release-notes.md) | Stable |
| TokuDB from [Percona Server 5.6.39-83.1](https://www.percona.com/doc/percona-server/5.6/release-notes/Percona-Server-5.6.39-82.1.html) | [MariaDB 10.0.35](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-10035-release-notes.md) | Stable |
| TokuDB from [Percona Server 5.6.38-83.0](https://www.percona.com/doc/percona-server/5.6/release-notes/Percona-Server-5.6.38-83.0.html) | [MariaDB 10.1.31](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10131-release-notes.md), [MariaDB 10.0.34](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-10034-release-notes.md) | Stable |
| TokuDB from [Percona Server 5.6.37-82.2](https://www.percona.com/doc/percona-server/5.6/release-notes/Percona-Server-5.6.37-82.2.html) | [MariaDB 10.2.9](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1029-release-notes.md), [MariaDB 10.1.27](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10127-release-notes.md), [MariaDB 10.0.33](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-10033-release-notes.md) | Stable |
| TokuDB from [Percona Server 5.6.36-82.1](https://www.percona.com/doc/percona-server/5.6/release-notes/Percona-Server-5.6.36-82.1.html) | [MariaDB 10.2.8](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1028-release-notes.md), [MariaDB 10.1.26](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10126-release-notes.md), [MariaDB 10.0.32](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-10032-release-notes.md) | Stable |
| TokuDB from [Percona Server 5.6.36-82.0](https://www.percona.com/doc/percona-server/5.6/release-notes/Percona-Server-5.6.36-82.0.html) | [MariaDB 10.2.7](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1027-release-notes.md), [MariaDB 10.1.24](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10124-release-notes.md), [MariaDB 10.0.31](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-10031-release-notes.md) | Stable |
| TokuDB from [Percona Server 5.6.35-80.0](https://www.percona.com/doc/percona-server/5.6/release-notes/Percona-Server-5.6.35-80.0.html) | [MariaDB 10.2.5](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1025-release-notes.md), [MariaDB 10.1.22](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10122-release-notes.md), [MariaDB 10.0.30](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-10030-release-notes.md) | Stable |
| TokuDB from [Percona Server 5.6.34-79.1](https://www.percona.com/doc/percona-server/5.6/release-notes/Percona-Server-5.6.34-79.1.html) | [MariaDB 10.1.20](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10120-release-notes.md), [MariaDB 10.0.29](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-10029-release-notes.md) | Stable |
| TokuDB from [Percona Server 5.6.33-79.0](https://www.percona.com/doc/percona-server/5.6/release-notes/Percona-Server-5.6.33-79.0.html) | [MariaDB 10.1.19](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10119-release-notes.md), [MariaDB 10.0.28](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-10028-release-notes.md) | Stable |
| TokuDB from [Percona Server 5.6.32-78.1](https://www.percona.com/doc/percona-server/5.6/release-notes/Percona-Server-5.6.32-78.1.html) | [MariaDB 10.1.18](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10118-release-notes.md) | Stable |
| TokuDB from [Percona Server 5.6.31-77.0](https://www.percona.com/doc/percona-server/5.6/release-notes/Percona-Server-5.6.31-77.0.html) | [MariaDB 10.1.17](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10117-release-notes.md), [MariaDB 10.0.27](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-10027-release-notes.md) | Stable |
| TokuDB from [Percona Server 5.6.30-76.3](https://www.percona.com/doc/percona-server/5.6/release-notes/Percona-Server-5.6.30-76.3.html) | [MariaDB 10.1.15](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10115-release-notes.md), [MariaDB 10.0.26](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-10026-release-notes.md) | Stable |
| TokuDB from [Percona Server 5.6.26-74.0](https://www.percona.com/doc/percona-server/5.6/release-notes/Percona-Server-5.6.30-76.3.html) [[1](#_note-0)] | [MariaDB 10.0.23](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-10023-release-notes.md) | Stable |
| [TokuDB 7.5.7](https://docs.tokutek.com/tokudb/tokudb-release-notes.html#tokudb-7-5-7) | [MariaDB 10.0.20](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-10020-release-notes.md), [MariaDB 5.5.44](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/mariadb-5544-release-notes.md) | Stable |
| [TokuDB 7.5.6](https://docs.tokutek.com/tokudb/tokudb-release-notes.html#tokudb-7-5-6) | [MariaDB 10.1.5](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-5-release-notes.md), [MariaDB 10.0.18](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-10018-release-notes.md), [MariaDB 5.5.43](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/mariadb-5543-release-notes.md) | Stable |
| [TokuDB 7.5.5](https://docs.tokutek.com/tokudb/tokudb-release-notes.html#tokudb-7-5-5) | [MariaDB 10.1.3](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-3-release-notes.md), [MariaDB 10.0.17](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-10017-release-notes.md), [MariaDB 5.5.42](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/mariadb-5542-release-notes.md) | Stable |
| [TokuDB 7.5.4](https://docs.tokutek.com/tokudb/tokudb-release-notes.html#tokudb-7-5-4) | [MariaDB 10.0.16](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-10016-release-notes.md) | Stable |
| [TokuDB 7.5.3](https://docs.tokutek.com/tokudb/tokudb-release-notes.html#tokudb-7-5-3) | [MariaDB 10.1.2](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-2-release-notes.md), [MariaDB 10.0.15](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-10015-release-notes.md), [MariaDB 5.5.41](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/mariadb-5541-release-notes.md) | Stable |
| [TokuDB 7.5.0](https://docs.tokutek.com/tokudb/tokudb-release-notes.html#tokudb-7-5-0) | [MariaDB 10.0.14](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-10014-release-notes.md), [MariaDB 5.5.40](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/mariadb-5540-release-notes.md) | Stable |
| [TokuDB 7.1.7](https://docs.tokutek.com/tokudb/tokudb-release-notes.html#tokudb-7-1-7) | [MariaDB 10.0.13](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-10013-release-notes.md), [MariaDB 5.5.39](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/mariadb-5539-release-notes.md) | Stable |
| [TokuDB 7.1.6](https://docs.tokutek.com/tokudb/tokudb-release-notes.html#tokudb-7-1-6) | [MariaDB 10.0.11](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-10011-release-notes.md), [MariaDB 5.5.38](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/mariadb-5538-release-notes.md) | Stable |
| [TokuDB 7.1.5](https://docs.tokutek.com/tokudb/tokudb-release-notes.html#tokudbv-7-1-5) | [MariaDB 10.0.10](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-10010-release-notes.md), [MariaDB 5.5.37](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/mariadb-5537-release-notes.md) | Stable |
| [TokuDB 7.1.0](https://docs.tokutek.com/tokudb/tokudb-release-notes.html#tokudb-7-1-0) | [MariaDB 5.5.34](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/mariadb-5534-release-notes.md) | Stable |
| [TokuDB 7.0.4](https://docs.tokutek.com/tokudb/tokudb-release-notes.html#tokudb-7-0-4) | [MariaDB 10.0.5](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-1005-release-notes.md), [MariaDB 5.5.33](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/mariadb-5533-release-notes.md) | Stable |



The version of TokuDB in your local MariaDB is available by querying the [tokudb_version](tokudb-system-variables.md) status variable. For example:


```
SHOW VARIABLES LIKE 'tokudb_version';
```

In the MariaDB binary tarballs, only the ones labeled "glibc_214" have TokuDB.


1. [↑](#_ref-0) with this version, TokuDB now follows the version numbering of Percona XtraDB


More information about TokuDB in MariaDB can be found on the following pages:

