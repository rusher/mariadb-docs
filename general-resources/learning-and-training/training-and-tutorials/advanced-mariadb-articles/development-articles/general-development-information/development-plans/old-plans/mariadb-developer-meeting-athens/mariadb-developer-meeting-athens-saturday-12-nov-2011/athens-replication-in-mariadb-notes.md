
# Athens - Replication in MariaDB - notes

**Note:** This page is obsolete. The information is old, outdated, or otherwise currently incorrect. We are keeping the page for historical reasons only. **Do not** rely on the information in this article.



Overview of Replication in MariaDB: [Replication](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/replication-cluster-multi-master/)


## In [MariaDB 5.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-3-series/changes-improvements-in-mariadb-5-3):


* Group Commit for the binary log.

  * [Mark Callaghan from Facebook did some benchmarks:](https://www.facebook.com/note.php?note_id=10150211546215933)
  * The Facebook patch and the implementation in [MariaDB 5.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-3-series/changes-improvements-in-mariadb-5-3) are two different solutions to the same problem. The latest Facebook patch is close to the performance in MariaDB, but MariaDB is still faster.
  * [Benchmarking thread scheduling in group commit, part 2](https://kristiannielsen.livejournal.com/15739.html)


* Enhancements for START TRANSACTION WITH CONSISTENT SNAPSHOT

  * Is actually consistent now ...
  * non-blocking slave privisioning


* Annotation of row-based replication events with the original SQL statement

  * A separate, but very similar, implementation is in 5.6


* Row-based replication for tables with no primary key


* PBXT consistent commit ordering


* Binlog Event Checksums (backport from MySQL 5.6


## To be in [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5)


* `@@do_not_replicate`


## Additional:


* Fixing `rpl_transaction_enabled` in case we crash and rollback during XA


## Misc:


* This preview also includes a small change to make mysqlbinlog omit redundatn use statements around BEGIN, SACEPOINT, COMMIT, and ROLLBACK events when reading MySQL 5.0 binlogs.
* The preview included a feature `--innodb-release-locks-early`. However we decided to omit this feature from future MariaDB releases because of a fundamental design bug, [Bug #798213](https://bugs.launchpad.net/bugs/798213)

