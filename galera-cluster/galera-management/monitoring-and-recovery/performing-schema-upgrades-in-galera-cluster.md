---
hidden: true
---

# Performing Schema Upgrades in Galera Cluster

Performing schema changes (i.e., Data Definition Language or DDL statements like `ALTER TABLE`, `CREATE INDEX`) in a MariaDB Galera Cluster requires special handling. Because Galera is a multi-primary cluster where all nodes must remain in sync, a schema change on one node must be safely replicated to all other nodes without causing inconsistencies or blocking the entire cluster for an extended period.

MariaDB Galera Cluster provides two methods for handling schema upgrades:

* Total Order Isolation (TOI): This is the default and safest method. The DDL statement is replicated to all nodes, and each node waits for all preceding transactions to complete before executing the change. This blocks the entire cluster for the duration of the schema change.
* Rolling Schema Upgrade (RSU): This is a more advanced, non-blocking method. The DDL statement is executed only on the local node where it is run. The administrator then applies the change manually to the other nodes one by one, allowing the cluster to remain online and available.

The method used is controlled by the `wsrep_OSU_method` session variable.

### 2. Total Order Isolation (TOI)

Total Order Isolation is the default method for schema upgrades (`wsrep_OSU_method = 'TOI'`). It ensures maximum data consistency by treating the DDL statement like any other transaction that must be applied in the same order on all nodes.

#### How TOI Works

1. You execute a DDL statement (e.g., `ALTER TABLE...`) on any node in the cluster.
2. The statement is replicated to all other nodes.
3. On every node, the cluster waits for all transactions that were in progress _before_ the `ALTER` statement to finish.
4. Once the node is caught up, it executes the DDL statement.
5. After the DDL statement completes, the node can begin processing new transactions again.

#### Advantages of TOI

* Simplicity and Safety: It is the easiest and safest method. It guarantees that the schema is identical on all nodes at all times.
* Consistency: There is no risk of data drifting or replication errors due to schema mismatches.

#### Disadvantages of TOI

* Blocking Operation: The primary drawback is that the DDL statement blocks the entire cluster. No node can process any write transactions while the schema change is running. For a large table that takes a long time to alter, this can result in significant application downtime.

#### When to Use TOI

TOI is the recommended method for:

* Schema changes that are known to be very fast.
* Environments where a short period of cluster-wide write unavailability is acceptable.
* Situations where schema consistency is the absolute highest priority.

### 3. Rolling Schema Upgrade (RSU)

Rolling Schema Upgrade is a non-blocking method (`wsrep_OSU_method = 'RSU'`) that allows you to perform schema changes without taking the entire cluster offline.

#### How RSU Works

The RSU method tells the cluster to not replicate the DDL statement. The change is only applied to the local node where you execute the command. It is then the administrator's responsibility to apply the same change to the other nodes one by one.

The typical procedure is as follows:

1.  Set the RSU Method: On the first node, change the OSU method for your current session:

    SQL

    ```
    SET SESSION wsrep_OSU_method = 'RSU';
    ```
2. Remove the Node from Rotation: Take the node out of your load balancer's pool so it no longer receives application traffic.
3. Apply the Schema Change: Execute the DDL statement (e.g., `ALTER TABLE...`) on this isolated node.
4. Return the Node to Rotation: Once the `ALTER` is complete, add the node back to the load balancer's pool.
5. Repeat for All Nodes: Repeat steps 1-4 on every other node in the cluster, one at a time, until all nodes have the updated schema.

#### Advantages of RSU

* High Availability: The cluster remains online and available to serve traffic throughout the entire process, as you only ever take one node out of rotation at a time.
* No Cluster-Wide Blocking: Application writes can continue on the active nodes.

#### Disadvantages of RSU

* Complexity and Risk: The process is manual and more complex, which introduces a higher risk of human error.
* Temporary Inconsistency: For the duration of the upgrade, your cluster will have a mixed schema, where some nodes have the old schema and others have the new one. This can cause replication errors if a transaction that relies on the new schema is sent to a node that has not yet been upgraded.

#### When to Use RSU

RSU is the best method for:

* Applying long-running schema changes to large tables where cluster downtime is not acceptable.
* Environments where high availability is the top priority.

It requires careful planning and a good understanding of your application's queries to ensure that no replication errors occur during the upgrade process.
