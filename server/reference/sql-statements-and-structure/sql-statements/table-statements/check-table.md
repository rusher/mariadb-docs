
# CHECK TABLE

## Syntax


```
CHECK TABLE tbl_name [, tbl_name] ... [option] ...

option = {FOR UPGRADE | QUICK | FAST | MEDIUM | EXTENDED | CHANGED}
```

## Description


`<code>CHECK TABLE</code>` checks a table or tables for errors. `<code>CHECK TABLE</code>` works for
[Archive](../../../storage-engines/archive/README.md), [Aria](../../../storage-engines/s3-storage-engine/aria_s3_copy.md), [CSV](../../../storage-engines/csv/csv-overview.md), [InnoDB](../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/innodb-upgrade-tests/README.md) and [MyISAM](../../../storage-engines/myisam-storage-engine/myisam-system-variables.md) tables. For Aria and MyISAM tables, the
key statistics are updated as well. For CSV, see also [Checking and Repairing CSV Tables](../../../storage-engines/csv/checking-and-repairing-csv-tables.md).


As an alternative, [myisamchk](../../../../clients-and-utilities/myisam-clients-and-utilities/myisamchk-table-information.md) is a commandline tool for checking MyISAM tables when the tables are not being accessed. For Aria tables, there is a similar tool: [aria_chk](../../../../clients-and-utilities/aria-clients-and-utilities/aria_chk.md).


For checking [dynamic columns](../../nosql/dynamic-columns-api.md) integrity, [COLUMN_CHECK()](../../nosql/dynamic-columns-from-mariadb-10.md) can be used.


`<code>CHECK TABLE</code>` can also check views for problems, such as tables
that are referenced in the view definition that no longer exist.


`<code>CHECK TABLE</code>` is also supported for partitioned tables. You can
use `<code class="highlight fixed" style="white-space:pre-wrap">[ALTER TABLE](../data-definition/alter/alter-tablespace.md) ... CHECK PARTITION</code>` 
to check one or more partitions.


The meaning of the different options are as follows - note that this can vary a bit between
storage engines:



|   |   |
| --- | --- |
| FOR UPGRADE | Do a very quick check if the storage format for the table has changed so that one needs to do a REPAIR. This is only needed when one upgrades between major versions of MariaDB or MySQL. This is usually done by [running mariadb-upgrade](../../../../server-management/getting-installing-and-upgrading-mariadb/migrating-to-mariadb/moving-from-mysql/migrating-to-mariadb-from-mysql-obsolete-articles/upgrading-to-mariadb-from-mysql-50-or-older.md). |
| FAST | Only check tables that has not been closed properly or are marked as corrupt. Only supported by the MyISAM and Aria engines. For other engines the table is checked normally |
| CHANGED | Check only tables that has changed since last REPAIR / CHECK. Only supported by the MyISAM and Aria engines. For other engines the table is checked normally. |
| QUICK | Do a fast check. For MyISAM and Aria, this means skipping the check of the delete link chain, which may take some time. |
| MEDIUM | Scan also the data files. Checks integrity between data and index files with checksums. In most cases this should find all possible errors. |
| EXTENDED | Does a full check to verify every possible error. For InnoDB, Aria, and MyISAM, verify for each row that all its keys exists, and for those index keys, they point back to the primary clustered key. This may take a long time on large tables. This option was previously ignored by InnoDB before [MariaDB 10.6.11](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-10-6-11-release-notes.md), [MariaDB 10.7.7](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-7-series/mariadb-10-7-7-release-notes.md), [MariaDB 10.8.6](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-8-series/mariadb-10-8-6-release-notes.md) and [MariaDB 10.9.4](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-9-series/mariadb-10-9-4-release-notes.md). From [MariaDB 11.8](../../../../../release-notes/mariadb-community-server/what-is-mariadb-118.md), also checks for referential integrity. |



For most cases running `<code>CHECK TABLE</code>` without options or `<code>MEDIUM</code>` should be
good enough.


The [Aria](../../../storage-engines/s3-storage-engine/aria_s3_copy.md) storage engine supports [progress reporting](../../../mariadb-internals/using-mariadb-with-your-programs-api/progress-reporting.md) for this statement.


If you want to know if two tables are identical, take a look
at [CHECKSUM TABLE](checksum-table.md).


## InnoDB


If `<code>CHECK TABLE</code>` finds an error in an InnoDB table, MariaDB might shutdown to prevent the error propagation. In this case, the problem will be reported in the error log. Otherwise the table or an index might be marked as corrupted, to prevent use. This does not happen with some minor problems, like a wrong number of entries in a secondary index. Those problems are reported in the output of `<code>CHECK TABLE</code>`.


Each tablespace contains a header with metadata. This header is not checked by this statement.


During the execution of `<code>CHECK TABLE</code>`, other threads may be blocked.


## Examples


```
CHECK TABLE y EXTENDED;
+--------+-------+----------+----------+
| Table  | Op    | Msg_type | Msg_text |
+--------+-------+----------+----------+
| test.y | check | status   | OK       |
+--------+-------+----------+----------+
```

From [MariaDB 11.8](../../../../../release-notes/mariadb-community-server/what-is-mariadb-118.md):


```
CHECK TABLE t1 EXTENDED;
+---------+-------+----------+----------------------------------------------------------------------+
| Table   | Op    | Msg_type | Msg_text                                                             |
+---------+-------+----------+----------------------------------------------------------------------+
| test.t1 | check | Warning  | No suitable key found for foreign key t2_ibfk_1 in table test.t1    |
+---------+-------+----------+----------------------------------------------------------------------+

CHECK TABLE t2 EXTENDED;
+---------+-------+----------+--------------------------------------------------------------------------------------------------+
| Table   | Op    | Msg_type | Msg_text                                                                                         |
+---------+-------+----------+--------------------------------------------------------------------------------------------------+
| test.t2 | check | status   | Cannot add or update a child row: a foreign key constraint fails (Key: t2_ibfk_1, record: '2')  |
| test.t2 | check | status   | Cannot add or update a child row: a foreign key constraint fails (Key: t2_ibfk_1, record: '2')  |
| test.t2 | check | status   | Cannot add or update a child row: a foreign key constraint fails (Key: t2_ibfk_1, record: '3')  |
| test.t2 | check | error    | Corrupt                                                                                          |
+---------+-------+----------+--------------------------------------------------------------------------------------------------+
```
