
# XA Transactions


## Overview


The MariaDB XA implementation is based on the X/Open CAE document Distributed Transaction Processing: The XA Specification. This document is published by The Open Group and available at [c193.htm](https://www.opengroup.org/public/pubs/catalog/c193.htm).


XA transactions are designed to allow distributed transactions, where a transaction manager (the application) controls a transaction which involves multiple resources. Such resources are usually DBMSs, but could be resources of any type. The whole set of required transactional operations is called a global transaction. Each subset of operations which involve a single resource is called a local transaction. XA used a 2-phases commit (2PC). With the first commit, the transaction manager tells each resource to prepare an effective commit, and waits for a confirm message. The changes are not still made effective at this point. If any of the resources encountered an error, the transaction manager will rollback the global transaction. If all resources communicate that the first commit is successful, the transaction manager can require a second commit, which makes the changes effective.


In MariaDB, XA transactions can only be used with storage engines that support them. At least [InnoDB](../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/innodb-upgrade-tests/README.md), [TokuDB](../../../storage-engines/tokudb/tokudb-resources.md), [SPIDER](../../../storage-engines/spider/spider-functions/spider_copy_tables.md) and [MyRocks](../../../storage-engines/myrocks/myrocks-in-mariadb-102-vs-mariadb-103.md) support them. XA transactions are always supported.


Like regular transactions, XA transactions create [metadata locks](metadata-locking.md) on accessed tables.


XA transactions require [REPEATABLE READ](set-transaction.md#repeatable-read) as a minimum isolation level. However, distributed transactions should always use [SERIALIZABLE](set-transaction.md#serializable).


Trying to start more than one XA transaction at the same time produces a 1400 error ([SQLSTATE](../../../../server-usage/programming-customizing-mariadb/programmatic-compound-statements/programmatic-compound-statements-diagnostics/sqlstate.md) 'XAE09'). The same error is produced when attempting to start an XA transaction while a regular transaction is in effect. Trying to start a regular transaction while an XA transaction is in effect produces a 1399 error ([SQLSTATE](../../../../server-usage/programming-customizing-mariadb/programmatic-compound-statements/programmatic-compound-statements-diagnostics/sqlstate.md) 'XAE07').


The [statements that cause an implicit COMMIT](sql-statements-that-cause-an-implicit-commit.md) for regular transactions produce a 1400 error ([SQLSTATE](../../../../server-usage/programming-customizing-mariadb/programmatic-compound-statements/programmatic-compound-statements-diagnostics/sqlstate.md) 'XAE09') if a XA transaction is in effect.


## Internal XA vs External XA


XA transactions are an overloaded term in MariaDB. If a [storage engine](../../../../../general-resources/learning-and-training/video-presentations-and-screencasts/storage-engines-and-plugins-videos.md) is XA-capable, it can mean one or both of these:


* It supports MariaDB's internal two-phase commit API. This is transparent to the user. Sometimes this is called "internal XA", since MariaDB's internal [transaction coordinator log](../../../../server-management/server-monitoring-logs/transaction-coordinator-log/transaction-coordinator-log-overview.md) can handle coordinating these transactions.


* It supports XA transactions, with the `<code>XA START</code>`, `<code>XA PREPARE</code>`, `<code>XA COMMIT</code>`, etc. statements. Sometimes this is called "external XA", since it requires the use of an external transaction coordinator to use this feature properly.


## Transaction Coordinator Log


If you have two or more XA-capable storage engines enabled, then a transaction coordinator log must be available.


There are currently two implementations of the transaction coordinator log:


* Binary log-based transaction coordinator log
* Memory-mapped file-based transaction coordinator log


If the [binary log](../../../storage-engines/innodb/binary-log-group-commit-and-innodb-flushing-performance.md) is enabled on a server, then the server will use the binary log-based transaction coordinator log. Otherwise, it will use the memory-mapped file-based transaction coordinator log.


See [Transaction Coordinator Log](../../../../server-management/server-monitoring-logs/transaction-coordinator-log/transaction-coordinator-log-overview.md) for more information.


## Syntax


```
XA {START|BEGIN} xid [JOIN|RESUME]

XA END xid [SUSPEND [FOR MIGRATE]]

XA PREPARE xid

XA COMMIT xid [ONE PHASE]

XA ROLLBACK xid

XA RECOVER [FORMAT=['RAW'|'SQL']]

xid: gtrid [, bqual [, formatID ]]
```

The interface to XA transactions is a set of SQL statements starting with `<code>XA</code>`. Each statement changes a transaction's state, determining which actions it can perform. A transaction which does not exist is in the `<code>NON-EXISTING</code>` state.


When trying to execute an operation which is not allowed for the transaction's current state, an error is produced:


```
XA COMMIT 'test' ONE PHASE;
ERROR 1399 (XAE07): XAER_RMFAIL: The command cannot be executed when global transaction is in the  ACTIVE state

XA COMMIT 'test2';
ERROR 1399 (XAE07): XAER_RMFAIL: The command cannot be executed when global transaction is in the  NON-EXISTING state
```

### XA START


```
XA {START|BEGIN} xid [JOIN|RESUME]
```

`<code>XA START</code>` (or `<code>BEGIN</code>`) starts a transaction and defines its `<code>xid</code>` (a transaction identifier). The new transaction will be in `<code>ACTIVE</code>` state.


The `<code>xid</code>` can have 3 components, though only the first one is mandatory. `<code>gtrid</code>` is a quoted string representing a global transaction identifier. `<code>bqual</code>` is a quoted string representing a local transaction identifier. `<code>formatID</code>` is an unsigned integer indicating the format used for the first two components; if not specified, defaults to 1. MariaDB does not interpret in any way these components, and only uses them to identify a transaction. `<code>xid</code>`s of transactions in effect must be unique.


Using the `<code>JOIN</code>` or `<code>RESUME</code>` keywords will currently cause an error to be returned.


```
MariaDB [test]> XA START 'test' RESUME;
ERROR 1398 (XAE05): XAER_INVAL: Invalid arguments (or unsupported command)
MariaDB [test]> XA START 'test' JOIN;
ERROR 1398 (XAE05): XAER_INVAL: Invalid arguments (or unsupported command)
```

An exception to this is that `<code>XA START xid RESUME</code>` will resume the transaction if the `<code>xid</code>` is the same as the previous `<code>xid</code>` used in `<code>XA END xid</code>`. This simply undoes the `<code>XA END</code>` and moves it from the `<code>IDLE</code>` state back into `<code>ACTIVE</code>`.


```
XA START 'test';
INSERT INTO t VALUES (1,2);
XA END 'test';
XA START 'test' RESUME; -- This reverts the XA END and continues the transaction
INSERT INTO t VALUES (3,4);
XA END 'test';
XA PREPARE 'test';
XA COMMIT 'test';
```

### XA END


```
XA END xid [SUSPEND [FOR MIGRATE]]
```

`<code>XA END</code>` declares that the specified `<code>ACTIVE</code>` transaction is finished and it changes its state to `<code>IDLE</code>`. `<code>SUSPEND [FOR MIGRATE]</code>` has no effect.


### XA PREPARE


```
XA PREPARE xid
```

`<code>XA PREPARE</code>` prepares an `<code>IDLE</code>` transaction for commit, changing its state to `<code>PREPARED</code>`. Prepared transactions are stored persistently and will survive disconnects and server crashes, and must be explicitly committed or rolled back.



##### MariaDB until [10.5](../../../../../release-notes/mariadb-community-server/what-is-mariadb-105.md)
Before [MariaDB 10.5](../../../../../release-notes/mariadb-community-server/what-is-mariadb-105.md), prepared transactions were automatically rolled back on client disconnect, but were not rolled back if the server was crashed or killed. This violated XA guarantees and could have caused inconsistent data, if the transaction in question was already irrevocably committed in another XA participant.


### XA COMMIT


```
XA COMMIT xid [ONE PHASE]
```

`<code>XA COMMIT</code>` definitely commits and terminates a transaction which has already been `<code>PREPARED</code>`. If the `<code>ONE PHASE</code>` clause is specified, this statements performs a 1-phase commit on an `<code>IDLE</code>` transaction.


### XA ROLLBACK


```
XA ROLLBACK xid
```

`<code>XA ROLLBACK</code>` rolls back and terminates an `<code>IDLE</code>` or `<code>PREPARED</code>` transaction.


### XA RECOVER


```
XA RECOVER [FORMAT=['RAW'|'SQL']]
```

The `<code>XA RECOVER</code>` statement shows information about all transactions which are in the `<code>PREPARED</code>` state. It does not matter which connection created the transaction: if it has been `<code>PREPARED</code>`, it appears. But this does not mean that a connection can commit or rollback a transaction which was started by another connection. Note that transactions using a 1-phase commit are never in the `<code>PREPARED</code>` state, so they cannot be shown by `<code>XA RECOVER</code>`.


`<code>XA RECOVER</code>` produces four columns:


```
XA RECOVER;
+----------+--------------+--------------+------+
| formatID | gtrid_length | bqual_length | data |
+----------+--------------+--------------+------+
|        1 |            4 |            0 | test |
+----------+--------------+--------------+------+
```

You can use `<code>XA RECOVER FORMAT='SQL'</code>` to get the data in a human readable
form that can be directly copy-pasted into `<code>XA COMMIT</code>` or `<code>XA ROLLBACK</code>`. This is particularly useful for binary `<code>xid</code>` generated by some transaction coordinators.


`<code>formatID</code>` is the `<code>formatID</code>` part of `<code>xid</code>`.


`<code>data</code>` are the `<code>gtrid</code>` and `<code>bqual</code>` parts of `<code>xid</code>`, concatenated.


`<code>gtrid_length</code>` and `<code>bqual_length</code>` are the lengths of `<code>gtrid</code>` and `<code>bqual</code>`, respectevely.


## Examples


2-phases commit:


```
XA START 'test';

INSERT INTO t VALUES (1,2);

XA END 'test';

XA PREPARE 'test';

XA COMMIT 'test';
```

1-phase commit:


```
XA START 'test';

INSERT INTO t VALUES (1,2);

XA END 'test';

XA COMMIT 'test' ONE PHASE;
```

Human-readable:


```
xa start '12\r34\t67\v78', 'abc\ndef', 3;

insert t1 values (40);

xa end '12\r34\t67\v78', 'abc\ndef', 3;

xa prepare '12\r34\t67\v78', 'abc\ndef', 3;

xa recover format='RAW';
+----------+--------------+--------------+--------------------+
| formatID | gtrid_length | bqual_length | data               |
+----------+--------------+--------------+--------------------+
34      67v78abc       11 |            7 | 12
def |
+----------+--------------+--------------+--------------------+

xa recover format='SQL';
+----------+--------------+--------------+-----------------------------------------------+
| formatID | gtrid_length | bqual_length | data                                          |
+----------+--------------+--------------+-----------------------------------------------+
|        3 |           11 |            7 | X'31320d3334093637763738',X'6162630a646566',3 |
+----------+--------------+--------------+-----------------------------------------------+

xa rollback X'31320d3334093637763738',X'6162630a646566',3;
```

## Known Issues


### MariaDB Galera Cluster


[MariaDB Galera Cluster](../../../../server-usage/replication-cluster-multi-master/galera-cluster/galera-cluster-status-variables.md) does not support XA transactions.


However, [MariaDB Galera Cluster](../../../../server-usage/replication-cluster-multi-master/galera-cluster/galera-cluster-status-variables.md) builds include a built-in plugin called `<code>wsrep</code>`. Consequently, these [MariaDB Galera Cluster](../../../../server-usage/replication-cluster-multi-master/galera-cluster/galera-cluster-status-variables.md) builds have multiple XA-capable storage engines by default, even if the only "real" storage engine that supports external [XA transactions](xa-transactions.md) enabled on these builds by default is [InnoDB](../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/innodb-upgrade-tests/README.md). Therefore, when using one these builds MariaDB would be forced to use a [transaction coordinator log](../../../../server-management/server-monitoring-logs/transaction-coordinator-log/transaction-coordinator-log-overview.md) by default, which could have performance implications.


See [Transaction Coordinator Log Overview: MariaDB Galera Cluster](../../../../server-management/server-monitoring-logs/transaction-coordinator-log/transaction-coordinator-log-overview.md#mariadb-galera-cluster) for more information.


### Incompatibility with XA behaviour


From [MariaDB 10.5](../../../../../release-notes/mariadb-community-server/what-is-mariadb-105.md), `<code>XA PREPARE</code>`
persists the XA transaction following the XA Specification. If an existing
application relies on the previous behavior, upgrading to 10.5 or later can
leave XA transactions in the PREPAREd state indefinitely after disconnect,
causing such applications to no longer function correctly.


As a work-around, the variable
[legacy_xa_rollback_at_disconnect](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#legacy_xa_rollback_at_disconnect)
can be set to TRUE to re-enable the old behavior and roll back XA
transactions in the PREPAREd state at disconnect. This is non-standard
behaviour, and is not recommended for new applications. If
rollback-at-disconnect is desired, it is better to use a normal (non-XA) transaction.

