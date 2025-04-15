
# MaxScale 25.01 Optimistic Transaction Execution Filter

# Optimistic Transaction Execution Filter


The `<code>optimistictrx</code>` filter implements optimistic transaction execution. The
filter is designed for a use-case where most of the transactions are read-only
and writes happen rarely but each set of read-only statements is still grouped
into a read-write transaction (i.e. `<code>START TRANSACTION</code>`, `<code>BEGIN</code>` or
`<code>SET autocommit=0</code>`).


This filter will replace the `<code>BEGIN</code>` and `<code>START TRANSACTION</code>` SQL commands with
`<code>START TRANSACTION READ ONLY</code>`. If the transaction is fully read-only, the
transaction completes normally. However, if a write happens in the middle of a
transaction, the filter issues a `<code>ROLLBACK</code>` command and then replays the
read-only part of the transaction, including the original `<code>BEGIN</code>` statement. If
the results of the replayed read-only part of the transaction is identical to
the one that was returned to the client, the transaction proceeds normally. If
the result checksum does not match, the connection is closed to prevent a write
with the wrong transaction state from happening.


# Configuration


To add the filter to a service, define an instance of the filter and then add it
to a service's `<code>filters</code>` list:



```
[OptimisticTrx]
type=filter
module=optimistictrx

[MyService]
...
filters=OptimisticTrx
```



This can also be done at runtime with:



```
maxctrl create filter OptimisticTrx optimistictrx
maxctrl alter service-filter MyService OptimisticTrx
```

