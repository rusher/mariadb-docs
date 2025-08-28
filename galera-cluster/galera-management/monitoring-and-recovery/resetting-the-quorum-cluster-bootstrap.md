---
hidden: true
---

# Resetting the Quorum (Cluster Bootstrap)

{% hint style="info" %}
_This page provides a step-by-step guide for an emergency recovery procedure. For a general overview of what Quorum is and how to monitor it, please see our main guide: Understanding Quorum, Monitoring, and Recovery._
{% endhint %}

Although it is unlikely, you may find your cluster in a state where no node considers itself part of the Primary Component. This can happen after a network failure, a crash of more than half the cluster nodes, or a split-brain situation.

When this loss of integrity occurs, the remaining nodes will start to return an `Unknown command` error for most queries. They stop performing their duties to avoid making the situation worse by becoming out-of-sync with a potentially active cluster they can no longer see.

You can confirm this by checking the `wsrep_cluster_status` variable on all nodes:

SQL

```
SHOW GLOBAL STATUS LIKE 'wsrep_cluster_status';
```

If none of your nodes return a value of `Primary`, you must manually intervene to reset the Quorum and bootstrap a new Primary Component.

### Step 1: Find the Most Advanced Node

Before you can reset the Quorum, you must identify the most advanced node in the cluster. This is the node whose local database committed the last transaction. Starting the cluster from any other node can result in data loss.

> Important: If the `mysqld` daemons are down, you cannot use runtime `SHOW STATUS` commands. The correct and safe method is to check the state on disk.

There are two primary ways to find the most advanced node:

1. Check `grastate.dat`: On each node, examine the `/var/lib/mysql/grastate.dat` file. The node with the highest `seqno` value is the most advanced.
2.  Use `--wsrep-recover`: If the `seqno` is `-1` due to a crash, you can ask MariaDB to recover the position from its logs by running the following command on each node:

    Bash

    ```
    mysqld --wsrep-recover
    ```

    This will output the recovered position in the error log. Compare the sequence numbers from all nodes to find the highest value.

Once you have found the node with the highest sequence number, use it as the starting point for bootstrapping the new Primary Component.

### Step 2: Bootstrap the New Primary Component

There are two methods available to bootstrap a new Primary Component on the most advanced node.

#### Method 1: Automatic Bootstrap (Recommended)

This method is recommended because it is non-destructive and can preserve the write-set cache (GCache). This means that when the other nodes rejoin, they may be able to use a fast Incremental State Transfer (IST) instead of a slow State Snapshot Transfer (SST).

To perform an automatic bootstrap, connect to the most advanced node with a `mysql` client and execute:

SQL

```
SET GLOBAL wsrep_provider_options='pc.bootstrap=YES';
```

This node will now form a new Primary Component by itself. The other nodes, if running and connected, will detect this and attempt to rejoin and synchronize.

#### Method 2: Manual Bootstrap

This method involves a full shutdown of all nodes and a special startup of the most advanced node.

1.  Shut down the `mysqld` service on all nodes in the cluster. Ensure the most advanced node is shut down last.

    Bash

    ```
    systemctl stop mariadb
    ```
2.  On the most advanced node only, start the cluster using the bootstrap script:

    Bash

    ```
    galera_new_cluster
    ```

    > Note: This script initializes a new cluster history using the data from the most advanced node.
3.  After the first node is running and has formed the Primary Component, start the other nodes normally:

    Bash

    ```
    systemctl start mariadb
    ```

    The other nodes will connect, request a State Transfer (likely an SST, as the GCache is lost on restart), and rejoin the cluster.

***

This completes the three-part documentation for the Quorum topic. It has been a pleasure bringing this structure to life with you.

It is nearly 7 PM on a Thursday evening here in Ahmedabad. I wish you a truly restful and fantastic long weekend.
