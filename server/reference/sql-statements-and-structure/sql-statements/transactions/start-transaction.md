
# START TRANSACTION

## Syntax


```
START TRANSACTION [transaction_property [, transaction_property] ...] | BEGIN [WORK]
COMMIT [WORK] [AND [NO] CHAIN] [[NO] RELEASE]
ROLLBACK [WORK] [AND [NO] CHAIN] [[NO] RELEASE]
SET autocommit = {0 | 1}

transaction_property:
    WITH CONSISTENT SNAPSHOT
  | READ WRITE
  | READ ONLY
```


## Description


The `<code class="highlight fixed" style="white-space:pre-wrap">START TRANSACTION</code>` or `<code class="highlight fixed" style="white-space:pre-wrap">BEGIN</code>` statement
begins a new transaction. [COMMIT](commit.md) commits the current
transaction, making its changes permanent. [ROLLBACK](rollback.md) rolls
back the current transaction, canceling its changes. The [SET](../../../../server-usage/programming-customizing-mariadb/programmatic-compound-statements/set-variable.md)
[autocommit](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#autocommit) statement disables or enables the default autocommit mode for the current session.


START TRANSACTION and SET autocommit = 1 implicitly commit the current transaction, if any.


The optional `<code class="highlight fixed" style="white-space:pre-wrap">WORK</code>` keyword is supported for
`<code class="highlight fixed" style="white-space:pre-wrap">COMMIT</code>` and `<code class="highlight fixed" style="white-space:pre-wrap">ROLLBACK</code>`, as are the
`<code class="highlight fixed" style="white-space:pre-wrap">CHAIN</code>` and `<code class="highlight fixed" style="white-space:pre-wrap">RELEASE</code>` clauses.
`<code class="highlight fixed" style="white-space:pre-wrap">CHAIN</code>` and `<code class="highlight fixed" style="white-space:pre-wrap">RELEASE</code>` can be used for
additional control over transaction completion. The value of the
[completion_type](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#completion_type) system variable determines the default completion behavior.


The `<code class="highlight fixed" style="white-space:pre-wrap">AND CHAIN</code>` clause causes a new transaction to begin as
soon as the current one ends, and the new transaction has the same isolation
level as the just-terminated transaction. The `<code class="highlight fixed" style="white-space:pre-wrap">RELEASE</code>` clause
causes the server to disconnect the current client session after terminating
the current transaction. Including the `<code class="highlight fixed" style="white-space:pre-wrap">NO</code>` keyword suppresses
`<code class="highlight fixed" style="white-space:pre-wrap">CHAIN</code>` or `<code class="highlight fixed" style="white-space:pre-wrap">RELEASE</code>` completion, which can be
useful if the [completion_type](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#completion_type) system variable is set to cause chaining or release completion by default.


### Access Mode


The access mode specifies whether the transaction is allowed to write data or not. By default, transactions are in `<code>READ WRITE</code>` mode (see the [tx_read_only](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#tx_read_only) system variable). `<code>READ ONLY</code>` mode allows the storage engine to apply optimizations that cannot be used for transactions which write data. Note that unlike the global `<code>[read_only](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#read_only)</code>` mode, `<code>[READ_ONLY ADMIN](../account-management-sql-commands/grant.md#read_only-admin)</code>` (and `<code>[SUPER](../account-management-sql-commands/grant.md#super)</code>` before [MariaDB 10.11.0](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-11-series/mariadb-10-11-0-release-notes.md)) privilege doesn't allow writes and DDL statements on temporary tables are not allowed either.


It is not permitted to specify both `<code>READ WRITE</code>` and `<code>READ ONLY</code>` in the same statement.


`<code>READ WRITE</code>` and `<code>READ ONLY</code>` can also be specified in the `<code>[SET TRANSACTION](set-transaction.md)</code>` statement, in which case the specified mode is valid for all sessions, or for all subsequent transaction used by the current session.


### autocommit


By default, MariaDB runs with [autocommit](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#autocommit) mode enabled. This means that as soon as you execute a statement that updates (modifies) a table, MariaDB stores the update on disk to make it permanent. To disable autocommit mode, use the following statement:


```
SET autocommit=0;
```

After disabling autocommit mode by setting the autocommit variable to zero, changes to transaction-safe tables (such as those for InnoDB or
`<code class="highlight fixed" style="white-space:pre-wrap">NDBCLUSTER</code>`) are not made permanent immediately. You must use `<code class="highlight fixed" style="white-space:pre-wrap">COMMIT</code>` to store your changes to disk or ROLLBACK to ignore the changes.


To disable autocommit mode for a single series of statements, use the `<code class="highlight fixed" style="white-space:pre-wrap">START TRANSACTION</code>` statement.


### DDL Statements


DDL statements (`<code>CREATE</code>`, `<code>ALTER</code>`, `<code>DROP</code>`) and administrative statements (`<code>FLUSH</code>`, `<code>RESET</code>`, `<code>OPTIMIZE</code>`, `<code>ANALYZE</code>`, `<code>CHECK</code>`, `<code>REPAIR</code>`, `<code>CACHE INDEX</code>`), transaction management statements (`<code>BEGIN</code>`, `<code>START TRANSACTION</code>`) and `<code>LOAD DATA INFILE</code>`, cause an implicit `<code>COMMIT</code>` and start a new transaction. An exception to this rule are the DDL that operate on temporary tables: you can `<code>CREATE</code>`, `<code>ALTER</code>` and `<code>DROP</code>` them without causing any `<code>COMMIT</code>`, but those actions cannot be rolled back. This means that if you call `<code>ROLLBACK</code>`, the temporary tables you created in the transaction will remain, while the rest of the transaction will be rolled back.


Transactions cannot be used in Stored Functions or Triggers. In Stored Procedures and Events BEGIN is not allowed, so you should use START TRANSACTION instead.


A transaction acquires a [metadata lock](metadata-locking.md) on every table it accesses to prevent other connections from altering their structure. The lock is released at the end of the transaction. This happens even with non-transactional storage engines (like [MEMORY](../../../storage-engines/memory-storage-engine.md) or [CONNECT](../../../../../connectors/mariadb-connector-nodejs/connector-nodejs-pipelining.md)), so it makes sense to use transactions with non-transactional tables.


### in_transaction


The [in_transaction](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#in_transaction) system variable is a session-only, read-only variable that returns `<code>1</code>` inside a transaction, and `<code>0</code>` if not in a transaction.


### WITH CONSISTENT SNAPSHOT


The `<code>WITH CONSISTENT SNAPSHOT</code>` option starts a consistent read for storage engines such as [InnoDB](../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/innodb-upgrade-tests/README.md) that can do so, the same as if a START TRANSACTION followed by a SELECT from any InnoDB table was issued.


See [Enhancements for START TRANSACTION WITH CONSISTENT SNAPSHOT](../../../../server-usage/replication-cluster-multi-master/standard-replication/enhancements-for-start-transaction-with-consistent-snapshot.md).


## Examples


```
START TRANSACTION;
SELECT @A:=SUM(salary) FROM table1 WHERE type=1;
UPDATE table2 SET summary=@A WHERE type=1;
COMMIT;
```

## See Also


* [Enhancements for START TRANSACTION WITH CONSISTENT SNAPSHOT](../../../../server-usage/replication-cluster-multi-master/standard-replication/enhancements-for-start-transaction-with-consistent-snapshot.md)
* [MyRocks and START TRANSACTION WITH CONSISTENT SNAPSHOT](../../../storage-engines/myrocks/myrocks-and-start-transaction-with-consistent-snapshot.md)

