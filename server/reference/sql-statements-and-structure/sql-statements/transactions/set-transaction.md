
# SET TRANSACTION

## Syntax


```
SET [GLOBAL | SESSION] TRANSACTION
    transaction_property [, transaction_property] ...

transaction_property:
    ISOLATION LEVEL level
  | READ WRITE
  | READ ONLY

level:
     REPEATABLE READ
   | READ COMMITTED
   | READ UNCOMMITTED
   | SERIALIZABLE
```


## Description


This statement sets the transaction isolation level or the transaction access mode globally, for the current session, or for the next transaction:


* With the `GLOBAL` keyword, the statement sets the default
 transaction level globally for all subsequent sessions. Existing sessions are
 unaffected.
* With the `SESSION` keyword, the statement sets the default
 transaction level for all subsequent transactions performed within the
 current session.
* Without any `SESSION` or `GLOBAL` keyword,
 the statement sets the isolation level for only the next (not started) transaction
 performed within the current session. After that it reverts to using the session value.


A change to the global default isolation level requires the 
`[SUPER](../account-management-sql-commands/grant.md)` privilege. Any session is free to change its
session isolation level (even in the middle of a transaction), or the isolation
level for its next transaction.


### Isolation Level


To set the global default isolation level at server startup, use the
[--transaction-isolation=level](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#tx_isolation) option on the command line or in an option file. Values of level for this option use dashes
rather than spaces, so the allowable values are [READ_UNCOMMITTED](#read-uncommitted),
[READ-COMMITTED](#read-committed), [REPEATABLE-READ](#repeatable-read), or
[SERIALIZABLE](#serializable). For example, to set the default isolation
level to `REPEATABLE READ`, use these lines in the [mariadb]
section of an option file:


```
[mariadb]
transaction-isolation = REPEATABLE-READ
```

To determine the global and session transaction isolation levels at
runtime, check the value of the [tx_isolation](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#tx_isolation) system variable (note that the variable has been renamed [transaction_isolation](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#transaction_isolation) from [MariaDB 11.1.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-1-series/mariadb-11-1-1-release-notes), to match the option, and the old name deprecated).


```
SELECT @@GLOBAL.tx_isolation, @@tx_isolation;
```

From [MariaDB 11.1.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-1-series/mariadb-11-1-1-release-notes):


```
SELECT @@GLOBAL.transaction_isolation, @@transaction_isolation;
```

InnoDB supports each of the translation isolation levels described here
using different locking strategies. The default level is 
`REPEATABLE READ`. For additional information about InnoDB
record-level locks and how it uses them to execute various types of statements,
see [InnoDB Lock Modes](../../../storage-engines/innodb/innodb-lock-modes.md),
and [innodb-locks-set.html](https://dev.mysql.com/doc/refman/en/innodb-locks-set.html).


### Isolation Levels


The following sections describe how MariaDB supports the different transaction levels.


#### READ UNCOMMITTED


`SELECT` statements are performed in a non-locking fashion,
but a possible earlier version of a row might be used. Thus, using this
isolation level, such reads are not consistent. This is also called a "dirty
read." Otherwise, this isolation level works like 
`READ COMMITTED`.


#### READ COMMITTED


A somewhat Oracle-like isolation level with respect to consistent
(non-locking) reads: Each consistent read, even within the same
transaction, sets and reads its own fresh snapshot. See
[innodb-consistent-read.html](https://dev.mysql.com/doc/refman/en/innodb-consistent-read.html).


For locking reads (`SELECT` with `FOR UPDATE`
or `LOCK IN SHARE MODE`), InnoDB locks only index records, not
the gaps before them, and thus allows the free insertion of new records next to
locked records. For `UPDATE` and `DELETE`
statements, locking depends on whether the statement uses a unique index with a
unique search condition (such as `WHERE id = 100`), or a
range-type search condition (such as `WHERE id > 100`). For a
unique index with a unique search condition, InnoDB locks only the index record
found, not the gap before it. For range-type searches, InnoDB locks the index
range scanned, using gap locks or next-key (gap plus index-record) locks to
block insertions by other sessions into the gaps covered by the range. This is
necessary because "phantom rows" must be blocked for MariaDB replication and
recovery to work.


**Note:** If the `READ COMMITTED` isolation
level is used or the [innodb_locks_unsafe_for_binlog](../../../storage-engines/innodb/innodb-system-variables.md#innodb_locks_unsafe_for_binlog) system variable is enabled,
there is no InnoDB gap locking except for [foreign-key](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/optimization-and-indexes/foreign-keys.md) constraint checking and
duplicate-key checking. Also, record locks for non-matching rows are released
after MariaDB has evaluated the `WHERE` condition.If you use `READ COMMITTED` or enable innodb_locks_unsafe_for_binlog, you must use row-based binary logging.


#### REPEATABLE READ


This is the default isolation level for InnoDB. For consistent reads,
there is an important difference from the `READ COMMITTED`
isolation level: All consistent reads within the same transaction read the
snapshot established by the first read. This convention means that if you issue
several plain (non-locking) `SELECT` statements within the
same transaction, these `SELECT` statements are consistent
also with respect to each other. See
[innodb-consistent-read.html](https://dev.mysql.com/doc/refman/en/innodb-consistent-read.html).


For locking reads (SELECT with FOR UPDATE or LOCK IN SHARE MODE),
UPDATE, and DELETE statements, locking depends on whether the
statement uses a unique index with a unique search condition, or a
range-type search condition. Prior to [MariaDB 10.3.38](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-10-3-38-release-notes), [MariaDB 10.4.28](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/mariadb-10-4-28-release-notes), [MariaDB 10.5.19](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-5-series/mariadb-10-5-19-release-notes), [MariaDB 10.6.12](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-6-series/mariadb-10-6-12-release-notes), [MariaDB 10.7.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-7-series/mariadb-10-7-8-release-notes), [MariaDB 10.8.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-8-series/mariadb-10-8-7-release-notes), [MariaDB 10.9.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-9-series/mariadb-10-9-5-release-notes), [MariaDB 10.10.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-10-series/mariadb-10-10-3-release-notes), [MariaDB 10.11.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-11-series/mariadb-10-11-2-release-notes) and [MariaDB 11.0.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-0-series/mariadb-11-0-0-release-notes), for a unique index with a unique search condition, InnoDB locks only the index record found, not the gap
before it. From these versions, MariaDB no longer relaxes the gap locking for unique indexes.


For other search conditions, InnoDB locks the index range scanned, using gap locks or next-key (gap plus index-record) locks to block insertions by other sessions into the gaps covered by the range.


This is the minimum isolation level for non-distributed [XA transactions](xa-transactions.md).


#### SERIALIZABLE


This level is like REPEATABLE READ, but InnoDB implicitly converts all
plain SELECT statements to [SELECT ... LOCK IN SHARE MODE](../data-manipulation/selecting-data/select.md#lock-in-share-mode-and-for-update-clauses) if [autocommit](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#autocommit)
is disabled. If autocommit is enabled, the SELECT is its own
transaction. It therefore is known to be read only and can be
serialized if performed as a consistent (non-locking) read and need
not block for other transactions. (This means that to force a plain
SELECT to block if other transactions have modified the selected rows,
you should disable autocommit.)


Distributed [XA transactions](xa-transactions.md) should always use this isolation level.


#### innodb_snapshop_isolation


If the [innodb_snapshot_isolation](../../../storage-engines/innodb/innodb-system-variables.md#innodb_snapshot_isolation) system variable is not set to ON, strictly-speaking anything other than READ UNCOMMITTED is not clearly defined. [innodb_snapshot_isolation](../../../storage-engines/innodb/innodb-system-variables.md#innodb_snapshot_isolation) was introduced in [MariaDB 10.6.18](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-6-series/mariadb-10-6-18-release-notes), [MariaDB 10.11.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-11-series/mariadb-10-11-8-release-notes), [MariaDB 11.0.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-0-series/mariadb-11-0-6-release-notes), [MariaDB 11.1.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-1-series/mariadb-11-1-5-release-notes), [MariaDB 11.2.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-2-series/mariadb-11-2-4-release-notes), [MariaDB 11.4.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-11-4-series/mariadb-11-4-2-release-notes) to address this, but defaults to `OFF` for backwards compatibility. Setting to `ON` will result in attempts to acquire a lock on a record that does not exist in the current read view raising an error, and the transaction being rolled back.


### Access Mode


The access mode specifies whether the transaction is allowed to write data or not. By default, transactions are in `READ WRITE` mode (see the [tx_read_only](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#tx_read_only) system variable). `READ ONLY` mode allows the storage engine to apply optimizations that cannot be used for transactions which write data. Note that unlike the global [read_only](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#read_only) mode, [READ_ONLY ADMIN](../account-management-sql-commands/grant.md#read_only-admin) (and [SUPER](../account-management-sql-commands/grant.md#super) before [MariaDB 10.11.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-11-series/mariadb-10-11-0-release-notes)) privilege doesn't allow writes and DDL statements on temporary tables are not allowed either.


It is not permitted to specify both `READ WRITE` and `READ ONLY` in the same statement.


`READ WRITE` and `READ ONLY` can also be specified in the [START TRANSACTION](start-transaction.md) statement, in which case the specified mode is only valid for one transaction.


## Examples


```
SET GLOBAL TRANSACTION ISOLATION LEVEL SERIALIZABLE;
```

Attempting to set the isolation level within an existing transaction without specifying `GLOBAL` or `SESSION`.


```
START TRANSACTION;

SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;
ERROR 1568 (25001): Transaction characteristics can't be changed while a transaction is in progress
```


GPLv2 fill_help_tables.sql

