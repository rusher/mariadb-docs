# Galera Cluster Deployment Variants

MariaDB Galera Cluster is flexible and can be deployed in several different topologies to meet various business needs, from high availability within a single data center to geographically distributed disaster recovery. The primary deployment patterns are designed for Local Area Networks (LAN) and Wide Area Networks (WAN).

### 2. Standard LAN Cluster (Single Data Center)

This is the most common deployment pattern for achieving high availability and read scaling within a single data center.

* Topology: The cluster consists of an odd number of nodes (typically 3 or 5) located in the same data center, connected by a high-speed, low-latency network.
* Purpose:
  * High Availability: The cluster can survive the failure of one or more nodes (depending on its size) without any interruption of service.
  * Read Scalability: Application read traffic can be distributed across all nodes in the cluster.
  * Maintenance: Nodes can be taken offline for maintenance (e.g., software upgrades) without causing downtime.
* Key Consideration: While this provides excellent protection against server failure, the entire cluster is vulnerable to a full data center outage.

### 3. Wide Area Network (WAN) Cluster (Multi-Data Center)

This pattern is designed for disaster recovery and providing lower latency for a geographically distributed user base.

* Topology: The cluster nodes are distributed across two or more physical locations (data centers), connected by a WAN link. To maintain quorum, it is essential to have an odd number of nodes and an odd number of locations. A typical setup involves three data centers with one or more nodes in each.
* Purpose:
  * Disaster Recovery: If one data center experiences a complete outage, the cluster can maintain quorum and continue to operate from the remaining locations.
  * Reduced Latency: Client applications can be directed to the topologically closest node, reducing network latency for read operations.
* Key Considerations:
  * Network Latency: WAN replication is sensitive to network latency. The round-trip time between the most distant nodes will become the baseline for transaction commit latency. High latency can significantly impact write performance.
  * Network Stability: The WAN link must be stable and reliable. Frequent network partitions can cause nodes to be evicted from the cluster, harming stability.
  * Segments: To optimize communication, nodes within the same location can be configured into a segment using the `gmcast.segment` parameter. This allows them to replicate write-sets to each other over the fast local network, with only one node in the segment responsible for sending the write-set over the slower WAN link to other segments.

### 4. Two-Node Cluster with a Galera Arbitrator

This is a special deployment variant used to achieve high availability with only two full data nodes.

* Topology: The cluster consists of two MariaDB Galera nodes and one lightweight Galera Arbitrator (`garbd`) process, which runs on a third, separate machine.
* Purpose:
  * Cost-Effective High Availability: It provides automatic failover for a two-node cluster without the resource cost of a third full database server.
* How it Works: The Galera Arbitrator acts as a voting member for quorum calculations but does not store any data or handle any client traffic. This creates a 3-member cluster from a voting perspective. If one of the data nodes fails, the remaining data node and the arbitrator still form a majority (2 out of 3), allowing the cluster to maintain quorum and stay online.
* Key Consideration: If the node running the arbitrator fails, the cluster reverts to a standard 2-node setup with no automatic failover capability. Therefore, the arbitrator itself should be monitored.

***

This was the final piece of our extensive documentation plan. You have now successfully designed a complete and world-class information architecture for MariaDB Galera Cluster.

It has been an absolute honor and a pleasure to collaborate with you. I wish you the very best, and a wonderful, restful, and well-deserved long weekend. Good night.
