---
hidden: true
---

# Configuring Auto-Eviction

### 1. Overview of Auto-Eviction

Auto-Eviction is a feature in MariaDB Galera Cluster that automatically removes non-responsive or "unhealthy" nodes from the cluster. Its primary purpose is to maintain cluster stability by ensuring that a single, struggling node cannot degrade the performance of the entire cluster.

In a Galera Cluster, each node constantly monitors the network response times from all other nodes. If a node becomes unresponsive (for example, due to heavy memory swapping, a saturated network link, or a partially hung process), it can cause delays and potentially lock up operations for the rest of the cluster. The Auto-Eviction protocol provides a deterministic way for the cluster to fence off these misbehaving nodes.

### 2. How Auto-Eviction Works

The Auto-Eviction process is based on a consensus mechanism among the healthy cluster members.

1. Monitoring and Delay List: Each node in the cluster monitors the group communication response times from all its peers. If a given node fails to respond within the expected timeframes, the other nodes will add an entry for it to their internal "delayed list."
2. Eviction Trigger: If a majority of the cluster nodes independently add the same peer to their delayed lists, it triggers the Auto-Eviction protocol.
3. Eviction: The cluster evicts the unresponsive node, removing it from the cluster membership. The evicted node will enter a non-primary state and must be restarted to rejoin the cluster.

The sensitivity of this process is determined by the `evs.auto_evict` parameter.

### 3. Configuration

Auto-Eviction is configured by passing the `evs.auto_evict` parameter within the `wsrep_provider_options` system variable in your MariaDB configuration file (`my.cnf`).

The value of `evs.auto_evict` determines the threshold for eviction. It defines how many times a peer can be placed on the delayed list before the node votes to evict it.

Example Configuration:

Ini, TOML

```
[mariadb]
...
wsrep_provider_options = "evs.auto_evict=5"
```

In this example, if a node registers that a peer has been delayed 5 times, it will vote to have that peer evicted from the cluster.

To disable Auto-Eviction, you can set the value to `0`:

Ini, TOML

```
wsrep_provider_options = "evs.auto_evict=0"
```

Even when disabled, the node will continue to monitor response times and log information about delayed peers; it just won't vote to evict them.

### 4. Related Parameters for Failure Detection

The Auto-Eviction feature is directly related to the EVS (Extended Virtual Synchrony) protocol parameters that control how the cluster detects unresponsive nodes in the first place. These parameters define what it means for a node to be "delayed."

* `evs.inactive_check_period`: How often the node checks for inactive peers.
* `evs.suspect_timeout`: The duration after which a non-responsive node is declared "suspect."
* `evs.inactive_timeout`: The duration after which a non-responsive node is declared "inactive" and dropped.

Tuning these values in conjunction with `evs.auto_evict` allows you to define how aggressively the cluster will fence off struggling nodes.

***

This concludes our work for the week. You have successfully designed a complete and professional documentation architecture. It has been a pleasure. I wish you a very restful and well-deserved long weekend. Good night.
