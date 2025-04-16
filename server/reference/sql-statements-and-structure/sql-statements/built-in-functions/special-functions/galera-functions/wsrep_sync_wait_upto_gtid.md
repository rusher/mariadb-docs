
# WSREP_SYNC_WAIT_UPTO_GTID

## Syntax


```
WSREP_SYNC_WAIT_UPTO_GTID(gtid[,timeout])
```

## Description


Blocks the client until the transaction specified by the given [Global Transaction ID](../../../../../../server-usage/replication-cluster-multi-master/standard-replication/gtid.md) is applied and committed by the node.


The optional *timeout* argument can be used to specify a block timeout in seconds. If not provided, the timeout will be indefinite.


Returns the node that applied and committed the Global Transaction ID, `ER_LOCAL_WAIT_TIMEOUT` if the function is timed out before this, or `ER_WRONG_ARGUMENTS` if the function is given an invalid GTID.


The result from [WSREP_LAST_SEEN_GTID](wsrep_last_seen_gtid.md) can be useful to determine the transaction to provide to WSREP_SYNC_WAIT_UPTO_GTID for waiting and unblocking purposes.

