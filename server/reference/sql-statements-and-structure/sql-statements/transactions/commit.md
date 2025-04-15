
# COMMIT

The `<code>COMMIT</code>` statement ends a transaction, saving any changes to the data so that they become visible to subsequent transactions. Also, [unlocks metadata](metadata-locking.md) changed by current transaction. If [autocommit](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#autocommit) is set to 1, an implicit commit is performed after each statement. Otherwise, all transactions which don't end with an explicit `<code>COMMIT</code>` are implicitly rollbacked and the changes are lost. The `<code>[ROLLBACK](rollback.md)</code>` statement can be used to do this explicitly.


The required syntax for the `<code>COMMIT</code>` statement is as follows:


```
COMMIT [WORK] [AND [NO] CHAIN] [[NO] RELEASE]
```

`<code>COMMIT</code>` is the more important transaction terminator, as well as the more interesting one. The basic form of the `<code>COMMIT</code>` statement is simply the keyword `<code>COMMIT</code>` (the keyword `<code>WORK</code>` is simply noise and can be omitted without changing the effect).


The optional `<code>AND CHAIN</code>` clause is a convenience for initiating a new transaction as soon as the old transaction terminates. If `<code>AND CHAIN</code>` is specified, then there is effectively nothing between the old and new transactions, although they remain separate. The characteristics of the new transaction will be the same as the characteristics of the old one — that is, the new transaction will have the same access mode, isolation level and diagnostics area size (we'll discuss all of these shortly) as the transaction just terminated.


`<code>RELEASE</code>` tells the server to disconnect the client immediately after the current transaction.


There are `<code>NO RELEASE</code>` and `<code>AND NO CHAIN</code>` options. By default, commits do not `<code>RELEASE</code>` or `<code>CHAIN</code>`, but it's possible to change this default behavior with the [completion_type](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#completion_type) server system variable. In this case, the `<code>AND NO CHAIN</code>` and `<code>NO RELEASE</code>` options override the server default.


## See Also


* [autocommit](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#autocommit) - server system variable that determines whether statements are automatically committed.
* [completion_type](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#completion_type) - server system variable that determines whether COMMIT's are standard, COMMIT AND CHAIN or COMMIT RELEASE.
* [SQL statements that cause an implicit commit](sql-statements-that-cause-an-implicit-commit.md)

