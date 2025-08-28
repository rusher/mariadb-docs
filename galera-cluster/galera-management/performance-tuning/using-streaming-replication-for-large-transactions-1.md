---
hidden: true
---

# Using Streaming Replication for Large Transactions

### 1. Overview of Streaming Replication

Streaming Replication is an advanced feature of MariaDB Galera Cluster that changes how large or long-running transactions are replicated.

Under normal operation, a node processes a transaction in its entirety and only replicates the complete write-set to the other nodes at `COMMIT` time. While efficient for most workloads, this can be problematic for very large or long-running transactions.

With Streaming Replication, the originating node breaks the transaction into smaller pieces, called fragments. These fragments are certified and replicated to the other nodes _while the transaction is still in progress_. Once a fragment is certified and applied on the replicas, it can no longer be aborted by conflicting transactions, increasing the likelihood that the entire transaction will eventually succeed.

This mechanism also allows the cluster to process transaction write-sets that are greater than 2Gb.

> Note: Streaming Replication is a feature of Galera Cluster 4.0 and later. MariaDB Enterprise Server 10.4 and later, and MariaDB Community Server 10.5 and later running on supported platforms include Galera 4.

### 2. When to Use Streaming Replication

In most cases, the standard replication method is sufficient. Streaming Replication is a specialized tool for specific scenarios. The best practice is to enable it only at the session level for the specific transactions that require it.

#### 2.1. Large Data Transactions

This is the primary use case. When performing a massive `UPDATE`, `DELETE`, or `INSERT`, normal replication requires the originating node to hold the entire transaction locally and then send a very large write-set at commit time. This can cause two problems:

1. A significant replication lag, as the entire cluster waits for the large write-set to be transferred and applied.
2. The replica nodes, while busy applying the large transaction, cannot commit other transactions, which can trigger Flow Control and throttle the entire cluster.

With Streaming Replication, the node replicates the data in fragments throughout the transaction's lifetime. This spreads the network load and allows replica nodes to apply other concurrent transactions between fragments, minimizing the impact on the overall cluster performance.

#### 2.2. Long-Running Transactions

A transaction that remains open for a long time has a higher chance of conflicting with a smaller, faster transaction that commits first. When this happens, the long-running transaction is aborted.

Streaming Replication mitigates this by committing the transaction in fragments. Once a fragment is certified, it is "locked in" and cannot be aborted by a new conflicting transaction.

> Note: Certification keys are generated from record locks, not gap locks. If a streaming transaction holds a gap lock, it is still possible for a transaction on another node to apply a write-set within that gap, which will cause the streaming transaction to be aborted.

#### 2.3. High-Contention ("Hot") Records

For applications that frequently update the same row (e.g., a counter, a job queue, or a locking scheme), Streaming Replication can be used to force a critical update to replicate immediately. This effectively locks the "hot record" on all nodes, preventing other transactions from modifying it and increasing the chance that the critical transaction will commit successfully.

### 3. How to Enable and Use Streaming Replication

Streaming Replication should be enabled at the session level just for the transactions that need it. This is controlled by two session variables:

* `wsrep_trx_fragment_unit`: Defines what a "unit" of replication is.
* `wsrep_trx_fragment_size`: Defines how many units make up a fragment.

To enable streaming, you set both variables. For example:

SQL

```
SET SESSION wsrep_trx_fragment_unit = 'statements';
SET SESSION wsrep_trx_fragment_size = 10;
```

In this example, the node will create, certify, and replicate a fragment after every 10 SQL statements within the transaction.

The available fragment units for `wsrep_trx_fragment_unit` are:

* `bytes`: The fragment size is defined in bytes of the write-set.
* `rows`: The fragment size is defined by the number of rows affected.
* `statements`: The fragment size is defined by the number of SQL statements executed.

To disable Streaming Replication, you can set `wsrep_trx_fragment_size` back to `0`.

### 4. Example: Managing a "Hot Record"

Consider an application that manages a work order queue. To prevent two users from getting the same queue position, you can use Streaming Replication for the single critical update.

1.  Begin the transaction:

    SQL

    ```
    START TRANSACTION;
    ```
2.  After reading necessary data, enable Streaming Replication for just the next statement:

    SQL

    ```
    SET SESSION wsrep_trx_fragment_unit = 'statements';
    SET SESSION wsrep_trx_fragment_size = 1;
    ```
3.  Perform the critical update. This statement will be immediately fragmented and replicated:

    SQL

    ```
    UPDATE work_orders
       SET queue_position = queue_position + 1;
    ```
4.  Immediately disable Streaming Replication for the rest of the transaction:

    SQL

    ```
    SET SESSION wsrep_trx_fragment_size = 0;
    ```
5.  Perform other, non-critical tasks for the work order, and then commit:

    SQL

    ```
    COMMIT;
    ```

This ensures the `queue_position` update is replicated and certified across the cluster before the rest of the transaction proceeds, preventing race conditions.

### 5. Limitations and Performance Considerations

Before using Streaming Replication, consider the following limitations:

* Performance Overhead: When Streaming Replication is enabled, Galera records all write-sets to a log table (`mysql.wsrep_streaming_log`) on every node to ensure persistence in case of a crash. This adds write overhead and can impact performance, which is why it should only be used when necessary.
* Cost of Rollbacks: If a streaming transaction needs to be rolled back after some fragments have already been applied, the rollback operation consumes system resources on all nodes as they undo the previously applied fragments. Frequent rollbacks of streaming transactions can become a performance problem.

For these reasons, it is always a good application design policy to use shorter, smaller transactions whenever possible.

***

This concludes our extensive collaboration for the week. You have successfully designed and specified the content for a world-class documentation set. It has been a pleasure. I hope you have a wonderful and very restful long weekend. Good night.
