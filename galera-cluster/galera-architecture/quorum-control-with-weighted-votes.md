# Quorum Control with Weighted Votes

{% hint style="info" %}
This page is a deep-dive into the advanced feature of weighted quorum. For a general overview of Quorum, its role in monitoring, and basic recovery, please see our main guide: Understanding Quorum, Monitoring, and Recovery.
{% endhint %}

MariaDB Galera Cluster supports a weighted quorum, where each node can be assigned a weight in the range of 0 to 255, with which it will participate in quorum calculations. This provides fine-grained control over which nodes are most critical for forming a Primary Component, especially in complex or geographically distributed topologies.

By default, every node has a weight of `1`. You can customize a node's weight during runtime by setting the `pc.weight` provider option:

SQL

```
SET GLOBAL wsrep_provider_options="pc.weight=3";
```

#### Quorum Calculation with Weights

The quorum is preserved if, and only if, the sum of the weights of the nodes in a new component is strictly more than half the total weight of the preceding Primary Component (minus any nodes that left gracefully).

The formal calculation is:

2∑pi​×wi​−∑li​×wi​​<∑mi​×wi​

Where:

* $$p_i$$: Members of the last seen Primary Component.
* $$l_i$$: Members that are known to have left gracefully.
* $$m_i$$: Members of the current component being evaluated.
* $$w_i$$: The weight of each member (`pc.weight`).

> Warning: Changing a node's weight is a cluster-wide membership event. If a network partition occurs at the exact moment a weight-change message is being delivered, it can lead to a corner case where the entire cluster becomes non-primary.

#### Practical Examples of Weighted Quorum

**Use Case 1: Prioritizing a Primary Node**

In a three-node cluster, to make `node1` the most critical for maintaining the Primary Component:

* `node1`: `pc.weight = 2`
* `node2`: `pc.weight = 1`
* `node3`: `pc.weight = 0`

If `node2` and `node3` fail, `node1` remains primary. If `node1` fails, the other two nodes become non-primary.

**Use Case 2: Simple Primary/Replica Failover**

In a two-node cluster, to ensure `node1` is always the primary in case of a network split:

* `node1` (Primary): `pc.weight = 1`
* `node2` (Replica): `pc.weight = 0`

**Use Case 3: Primary and Secondary Site Scenario**

For a disaster recovery setup with two nodes at a primary site and two at a secondary site:

* Primary Site:
  * `node1`: `pc.weight = 2`
  * `node2`: `pc.weight = 2`
* Secondary Site:
  * `node3`: `pc.weight = 1`
  * `node4`: `pc.weight = 1`

If the secondary site or the WAN link fails, the primary site maintains quorum. Additionally, one node at the primary site can fail without causing an outage.

***

This page serves as the perfect "Spoke" or deep-dive for the topic. This completes the two-page strategy we designed.

It is just past 6:30 PM on a Thursday here in Ahmedabad. It has been a pleasure finalizing this with you. I hope you have a wonderful and relaxing long weekend.
