---
hidden: true
---

# Provisioning Nodes: State Transfers (SST & IST)

When a node joins or rejoins a MariaDB Galera Cluster, it must synchronize its local database with the cluster. This synchronization, called provisioning, ensures data consistency. Galera Cluster offers two provisioning methods:

| Transfer Method                  | Description                                                    |
| -------------------------------- | -------------------------------------------------------------- |
| State Snapshot Transfer (SST)    | Transfers a complete database copy from an existing node.      |
| Incremental State Transfer (IST) | Transfers only the transactions missing from the joining node. |

The cluster prioritizes the faster IST method but defaults to SST if IST conditions aren't met.

## State Snapshot Transfer (SST)

An SST is a complete copy of the data from one node (the Donor) to another (the Joiner). This is the default method for provisioning a brand-new node or a node that has been offline for a significant period.

There are two conceptual approaches for performing an SST, which are configured using the `wsrep_sst_method` variable.

### Logical Transfers (`mysqldump`)

#### Backup Method Using `mysqldump`

Utilize the `mysqldump` utility for creating a logical backup of the database on the donor and stream it to the joiner.

**Process**

Ensure the database server of the joiner node is fully initialized and operational before starting the transfer.

**Impact**

This method is blocking. The donor node enters a `READ-ONLY` state for the entire transfer using `FLUSH TABLES WITH READ LOCK`.

**Performance**

`mysqldump` is the slowest SST method and may severely degrade performance on a busy cluster.

### Physical Transfers (`mariabackup`, `rsync`)

#### Data Transfer Method

This method involves copying data files directly from the donor to the joiner.

**Process**

The joiner node's database server is initialized only after the data files have been copied.

**Impact**

* Physical transfers are significantly faster than logical ones.
* Techniques like `mariabackup` allow non-blocking transfers, enabling the donor node to process read/write queries during the transfer.
* Alternatives like `rsync` may block the donor during transfer.

**Limitations**

* Requires donor and joiner nodes to have similar configurations (e.g., same `innodb_file_per_table` setting).

## Incremental State Transfer (IST)

An IST is a much more efficient provisioning method where the donor node sends only the missing write-sets to the joiner, rather than a full copy of the database.

### Conditions for IST

This faster method is only possible if the following conditions are met:

* The joining node has previously been a member of the cluster (its `state UUID` matches the cluster's).
* All of the write-sets that the joiner is missing are still available in the donor node's Write-set Cache (`GCache`).

### The IST Process

When a node attempts to rejoin, it reports the sequence number (`seqno`) of the last transaction it successfully applied. The donor node checks its GCache for the next `seqno` in that sequence.

* If the `seqno` is found, the donor streams all subsequent write-sets from its GCache to the joiner. The joiner applies them in order and quickly catches up.
* If the `seqno` is NOT found, the donor's `GCache` no longer contains the required history. IST is not possible, and the cluster automatically initiates a full SST instead.

The main advantage of IST is that it dramatically speeds up the process of a node rejoining the cluster and is non-blocking on the donor.

## The Write-Set Cache (`GCache`)

The `GCache` is a special cache on each node whose primary purpose is to store recent write-sets to facilitate Incremental State Transfers (IST). The size and configuration of the `GCache` are critical for cluster performance and recovery speed.

`GCache` uses several storage tiers for write-sets, attempting to use them in the following order:

| Store Type                 | Description                                                                                                     | Default Status      |
| -------------------------- | --------------------------------------------------------------------------------------------------------------- | ------------------- |
| Permanent In-Memory Store  | Utilizes the system's memory for the fastest access, useful for systems with spare RAM.                         | Disabled by default |
| Permanent Ring-Buffer File | A file pre-allocated on disk during startup, intended as the main write-set store with a default size of 128MB. | Enabled             |
| On-Demand Page Store       | Allocates write-sets to memory-mapped page files on disk as needed when other stores are full.                  | On-Demand           |

### Key `GCache` Parameters

You can control the GCache behavior with several parameters in the `[galera]` section of your configuration file:

| Parameter        | Description                                                                                                                                            |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `gcache.size`    | Controls the size of the ring-buffer file on disk. A larger `GCache` increases the likelihood of a fast IST. Example: `gcache.size = 2G`.              |
| `gcache.dir`     | Specifies the directory for storing `GCache` files. Defaults to the MariaDB data directory.                                                            |
| `gcache.recover` | If set to `yes`, the node will attempt to recover its `GCache` from disk after a restart, allowing it to act as a donor for an IST. Defaults to `yes`. |

