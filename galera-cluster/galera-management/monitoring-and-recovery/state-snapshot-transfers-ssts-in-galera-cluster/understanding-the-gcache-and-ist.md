---
hidden: true
---

# Understanding the GCache and IST

{% hint style="info" %}
This page provides a deep-dive into Incremental State Transfer (IST), the preferred method for a node to synchronize with the cluster. For information on the fallback mechanism, see the guide on State Snapshot Transfers (SSTs).
{% endhint %}

## Incremental State Transfer (IST)?

An Incremental State Transfer (IST) is the fast and efficient process where a joining node receives only the missing transactions it needs to catch up with the cluster, rather than receiving a full copy of the entire database.

This is the preferred provisioning method because it is:

* Fast: Transferring only the missing changes is significantly faster than copying the entire dataset.
* Non-Blocking: The donor node can continue to serve read and write traffic while an IST is in progress.

### Conditions for IST

IST is an automatic process, but it is only possible if the following conditions are met:

* The joining node has previously been a member of the cluster (its `state UUID` matches the cluster's).
* All of the write-sets that the joiner is missing are still available in the donor node's Write-set Cache (GCache).

If these conditions are not met, the cluster automatically falls back to performing a full State Snapshot Transfer (SST).

## The Write-Set Cache (GCache)

The GCache is a special cache on each node whose primary purpose is to store recent write-sets specifically to facilitate Incremental State Transfers. The size and configuration of the GCache are therefore critical for the cluster's recovery speed and high availability.

### How the GCache Enables IST

When a node attempts to rejoin the cluster, it reports the sequence number (`seqno`) of the last transaction it successfully applied. The potential donor node then checks its GCache for the very next `seqno` in that sequence.

* If the `seqno` is found in the GCache: The donor has the necessary history. It streams all subsequent write-sets from its GCache to the joiner. The joiner applies them in order and quickly becomes `Synced`.
* If the `seqno` is NOT found in the GCache: The node was disconnected for too long, and the required history has been purged from the cache. IST is not possible, and an SST is initiated.

### Configuring the GCache

You can control the GCache behavior with several parameters in the `[galera]` section of your configuration file (`my.cnf`).

* `gcache.size`: This is the most important parameter for IST. It controls the size of the on-disk ring-buffer file (e.g., `gcache.size = 2G`). A larger GCache can hold more history, increasing the likelihood that a disconnected node can use a fast IST instead of a slow SST.
* `gcache.dir`: Specifies the directory where the GCache files are stored. It is a best practice to place the GCache on your fastest available storage (e.g., an SSD or NVMe drive).
* `gcache.recover`: Enabled by default in modern Galera versions, this allows a node to recover its GCache from disk after a restart, enabling it to immediately serve as a donor for an IST.

