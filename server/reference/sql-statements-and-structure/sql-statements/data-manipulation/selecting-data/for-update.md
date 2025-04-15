
# FOR UPDATE

InnoDB supports row-level locking. Selected rows can be locked using [LOCK IN SHARE MODE](lock-in-share-mode.md) or FOR UPDATE. In both cases, a lock is acquired on the rows read by the query, and it will be released when the current transaction is committed.


The `<code>FOR UPDATE</code>` clause of [SELECT](../../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/benchmarks-and-long-running-tests/benchmark-results/select-random-ranges-and-select-random-point.md) applies only when [autocommit](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#autocommit) is set to 0 or the `<code>SELECT</code>` is enclosed in a transaction. A lock is acquired on the rows, and other transactions are prevented from writing the rows, acquire locks, and from reading them (unless their isolation level is `<code>[READ UNCOMMITTED](../../transactions/set-transaction.md)</code>`).


If `<code>autocommit</code>` is set to 1, the [LOCK IN SHARE MODE](lock-in-share-mode.md) and `<code>FOR UPDATE</code>` clauses have no effect in InnoDB. For non-transactional storage engines like MyISAM and ARIA, a table level lock will be taken even if autocommit is set to 1.


If the isolation level is set to [SERIALIZABLE](../../transactions/set-transaction.md), all plain `<code>SELECT</code>` statements are converted to `<code>SELECT ... LOCK IN SHARE MODE</code>`.


## Example


```
SELECT * FROM trans WHERE period=2001 FOR UPDATE;
```

## See Also


* [SELECT](../../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/benchmarks-and-long-running-tests/benchmark-results/select-random-ranges-and-select-random-point.md)
* [LOCK IN SHARE MODE](lock-in-share-mode.md)
* [InnoDB Lock Modes](../../../../storage-engines/innodb/innodb-lock-modes.md)

