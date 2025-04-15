
# CHECKSUM TABLE

## Syntax


```
CHECKSUM TABLE tbl_name [, tbl_name] ... [ QUICK | EXTENDED ]
```


## Description


`<code class="fixed" style="white-space:pre-wrap">CHECKSUM TABLE</code>` reports a table checksum. This is very
useful if you want to know if two tables are the same (for example on a master
and slave).


With `<code class="fixed" style="white-space:pre-wrap">QUICK</code>`, the live table checksum is reported if it is
available, or `<code class="fixed" style="white-space:pre-wrap">NULL</code>` otherwise. This is very fast. A live
checksum is enabled by specifying the `<code class="fixed" style="white-space:pre-wrap">CHECKSUM=1</code>` table
option when you [create the table](../../vectors/create-table-with-vectors.md); currently, this is supported
only for [Aria](../../../storage-engines/s3-storage-engine/aria_s3_copy.md) and [MyISAM](../../../storage-engines/myisam-storage-engine/myisam-system-variables.md) tables.


With `<code class="fixed" style="white-space:pre-wrap">EXTENDED</code>`, the entire table is read row by row and the
checksum is calculated. This can be very slow for large tables.


If neither `<code class="fixed" style="white-space:pre-wrap">QUICK</code>` nor `<code class="fixed" style="white-space:pre-wrap">EXTENDED</code>` is
specified, MariaDB returns a live checksum if the table storage engine supports
it and scans the table otherwise.


`<code>CHECKSUM TABLE</code>` requires the [SELECT privilege](../account-management-sql-commands/grant.md#table-privileges) for the table.


For a nonexistent table, `<code class="fixed" style="white-space:pre-wrap">CHECKSUM TABLE</code>` returns
`<code class="fixed" style="white-space:pre-wrap">NULL</code>` and generates a warning.


The table row format affects the checksum value. If the row format changes, the checksum will change. This means that when a table created with a MariaDB/MySQL version is upgraded to another version, the checksum value will probably change.


Two identical tables should always match to the same checksum value; however, also for non-identical tables there is a very slight chance that they will return the same value as the hashing algorithm is not completely collision-free.


## Identical Tables


Identical tables mean that the CREATE statement is identical and that the following variable, which affects the storage formats, was the same when the tables were created:


* [mysql56-temporal-format](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#mysql56_temporal_format)


## Differences Between MariaDB and MySQL


`<code class="fixed" style="white-space:pre-wrap">CHECKSUM TABLE</code>` may give a different result as MariaDB doesn't
ignore `<code class="fixed" style="white-space:pre-wrap">NULL</code>`s in the columns as MySQL 5.1 does (Later MySQL
versions should calculate checksums the same way as MariaDB). You can get the
'old style' checksum in MariaDB by starting [mariadbd](../../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd.md) with the
[--old](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#old) option (deprecated from [MariaDB 10.9](../../../../../release-notes/mariadb-community-server/what-is-mariadb-109.md)) or setting [old_mode](../../../../server-management/variables-and-modes/old-mode.md) to [COMPAT_5_1_CHECKSUM](../../../../server-management/variables-and-modes/old-mode.md#compat_5_1_checksum) (from [MariaDB 10.9](../../../../../release-notes/mariadb-community-server/what-is-mariadb-109.md)) . Note however that that the MyISAM and Aria storage engines in MariaDB are using the new checksum internally, so if you are
using this old mode, the `<code class="fixed" style="white-space:pre-wrap">CHECKSUM</code>` command will be
slower as it needs to calculate the checksum row by row.

