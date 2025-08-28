---
hidden: true
---

# Understanding Quorum, Monitoring, and Recovery

Quorum is essential for maintaining data consistency in a MariaDB Galera Cluster by safeguarding against network partitions or node failures. It ensures that the cluster processes database queries and transactions only when a majority of nodes are operational, healthy, and in communication.

This majority group is known as the Primary Component. Nodes not in this group switch to a non-primary state, halting queries and entering a read-only "safe mode" to prevent data discrepancies.

The primary function of Quorum is to avoid "split-brain" scenarios. A split-brain occurs when network partitions lead to parts of the cluster operating independently and accepting writes, resulting in conflicting data. By ensuring only the partition with a majority of nodes becomes the Primary Component, Quorum effectively prevents these inconsistencies.

### Quorum Calculation

Quorum is achieved when more than 50% of the total nodes in the last known membership are in communication.

* Odd Number of Nodes (Recommended): In a 3-node cluster, a majority is 2. The cluster can tolerate the failure of 1 node and remain operational. In a 5-node cluster, a majority is 3, and it can tolerate 2 node failures. This is the ideal and most resilient configuration.
* Even Number of Nodes: In a 2-node cluster, a majority is also 2. If one node fails, the remaining node represents only 50% of the cluster, which is not a majority. It will lose Quorum and stop functioning. This is why a 2-node cluster has no fault tolerance without an external voting member.

### The Galera Arbitrator (`garbd`)

The Galera Arbitrator (`garbd`) is the standard solution for clusters with an even number of nodes. It is a lightweight, stateless daemon that can be run on a separate, minimal server.

`garbd` acts as a voting member in the cluster without being a full database node. It participates in Quorum calculations, effectively turning an even-numbered cluster into an odd-numbered one. For example, in a 2-node cluster, adding `garbd` makes the total number of voting members 3. If one database node fails, the remaining database node and `garbd` still form a majority (2 out of 3), allowing the cluster to maintain Quorum and stay online.

### Understanding and Recovering from a Split-Brain

A split-brain occurs when a network partition divides the cluster and no resulting group of nodes has a majority. The most common cause is a 4-node or 6-node cluster being split into two equal-sized halves.

By design, Galera's quorum mechanism prevents data corruption in this scenario. Both halves of the cluster will fail to achieve a majority, and all nodes will enter a non-Primary state, refusing to serve queries.

If you need to restore service before the network issue is fixed, you must manually intervene:

1. Choose ONE side of the partition to become the new Primary Component.
2.  On a single node within that chosen group, execute the following command to force it to bootstrap a new component:

    SQL

    ```
    SET GLOBAL wsrep_provider_options='pc.bootstrap=true';
    ```
3. The nodes in this group will now form a new Primary Component and become operational. When network connectivity is restored, the nodes from the other partition will automatically detect this Primary Component and rejoin the cluster.

> Warning: Never execute the bootstrap command on both sides of a partition. This will create two independent, active clusters with diverging data, leading to severe data inconsistency that is very difficult to repair.

### 5. Advanced Quorum Control

As a more advanced alternative to `garbd` for fine-grained control, nodes can also be assigned a specific voting weight.

> _For a detailed guide on this feature, see our advanced page: Configuring Advanced Quorum with Weighted Votes (`pc.weight`)._

### 6. Monitoring Quorum and Cluster Membership

You can check the health of the cluster and its Quorum status at any time by querying the following status variables. These should be run on all nodes to ensure you get a consistent picture.

*   `wsrep_cluster_status`: The most important variable for Quorum.

    * Healthy Value: `Primary`
    * Unhealthy Value: Any other value (e.g., `non-Primary`, `Disconnected`) means the node is not part of a functional cluster component that has Quorum.

    SQL

    ```
    SHOW GLOBAL STATUS LIKE 'wsrep_cluster_status';
    ```
* `wsrep_cluster_size`: Shows the number of nodes in the component this node is currently connected to.
  * Healthy Value: Should match the number of nodes you expect in your cluster.
  *   SQL

      ```
        SHOW GLOBAL STATUS LIKE 'wsrep_cluster_size';
      ```
*   `wsrep_cluster_conf_id` and `wsrep_cluster_state_uuid`: These are identifiers for the cluster membership group.

    * Healthy Value: The values for both variables must be identical on every single node in the cluster.
    * Unhealthy Value: If any node reports a different value, it means it has been partitioned from the Primary Component.

    SQL

    ```
    SHOW GLOBAL STATUS LIKE 'wsrep_cluster_conf_id';
    SHOW GLOBAL STATUS LIKE 'wsrep_cluster_state_uuid';
    ```

### 7. Recovering from a Full Cluster Shutdown

If the entire cluster shuts down or fails in a way that Quorum is lost on all nodes, you must manually bootstrap the cluster to re-establish a Primary Component.

1. Stop all remaining MariaDB nodes in the cluster to ensure a clean start.
2. Identify the most advanced node. This is the node that contains the most recent data. You can find this by checking the `seqno` value in the `/var/lib/mysql/grastate.dat` file on each node. The node with the highest `seqno` is the most advanced.
3.  Bootstrap the Primary Component from the most advanced node. You can do this by using a dedicated bootstrap script:

    Bash

    ```
    galera_new_cluster
    ```
4. Start the other nodes normally. They will detect the new Primary Component and rejoin the cluster.
