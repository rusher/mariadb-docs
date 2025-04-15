
# MASTER_POS_WAIT

## Syntax


```
MASTER_POS_WAIT(log_name,log_pos[,timeout,["connection_name"]])
```

## Description


This function is useful in [replication](../../../administrative-sql-statements/replication-statements/README.md) for controlling primary/replica synchronization. It blocks until the replica has read and applied all updates up to the specified position (`<code>log_name,log_pos</code>`) in the primary log. The return value is the number of log events the replica had to wait for to advance to the specified position. The function returns NULL if
the replica SQL thread is not started, the replica's primary information is not
initialized, the arguments are incorrect, or an error occurs. It returns -1 if
the timeout has been exceeded. If the replica SQL thread stops while
 `<code class="highlight fixed" style="white-space:pre-wrap">MASTER_POS_WAIT()</code>` is waiting, the function returns NULL. If
the replica is past the specified position, the function returns immediately.


If a `<code>timeout</code>` value is specified, `<code class="highlight fixed" style="white-space:pre-wrap">MASTER_POS_WAIT()</code>` stops
waiting when `<code>timeout</code>` seconds have elapsed. `<code>timeout</code>` must be greater than 0; a
zero or negative `<code>timeout</code>` means no `<code>timeout</code>`.


The `<code class="highlight fixed" style="white-space:pre-wrap">connection_name</code>` is used when you are using [multi-source-replication](../../../../../../server-usage/replication-cluster-multi-master/standard-replication/multi-source-replication.md). If you don't specify it, it's set to the value of the [default_master_connection](../../../../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md) system variable.


Statements using the MASTER_POS_WAIT() function are not [safe for statement-based replication](../../../../../../server-usage/replication-cluster-multi-master/standard-replication/unsafe-statements-for-statement-based-replication.md).

