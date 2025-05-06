
# WSREP_LAST_SEEN_GTID

## Syntax


```
WSREP_LAST_SEEN_GTID()
```

## Description


Returns the [Global Transaction ID](../../../../../../server-usage/replication-cluster-multi-master/standard-replication/gtid.md) of the most recent write transaction observed by the client.


The result can be useful to determine the transaction to provide to [WSREP_SYNC_WAIT_UPTO_GTID](wsrep_sync_wait_upto_gtid.md) for waiting and unblocking purposes.


CC BY-SA / Gnu FDL

