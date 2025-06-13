---
icon: briefcase-arrow-right
layout:
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: false
---

# Galera Use Cases

MariaDB Galera Cluster ensures high availability and disaster recovery through synchronous multi-master replication. It's ideal for active-active setups, providing strong consistency and automatic failover, perfect for critical applications needing continuous uptime.

Common use cases for Galera replication include:

| Read Master      | WAN Clustering                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Read Master      | Traditional MariaDB master-slave topology, but with Galera all "slave" nodes are capable masters at all times - it is just the application that treats them as slaves. Galera replication can guarantee zero slave lag for such installations and, due to parallel slave applying, much better throughput for the cluster.                                                                                                               |
| WAN Clustering   | Synchronous replication works fine over the WAN network. There will be a delay, which is proportional to the network round trip time (RTT), but it only affects the commit operation.                                                                                                                                                                                                                                                    |
| Disaster Recover | Disaster recovery is a sub-class of WAN replication. Here one data center is passive and only receives replication events, but does not process any client transactions. Such a remote data center will be up to date at all times and no data loss can happen. During recovery, the spare site is just nominated as primary and application can continue as normal with a minimal fail over delay.                                      |
| Latency Eraser   | With WAN replication topology, cluster nodes can be located close to clients. Therefore all read & write operations will be super fast with the local node connection. The RTT related delay will be experienced only at commit time, and even then it can be generally accepted by end user, usually the kill-joy for end user experiences is the slow browsing response time, and read operations are as fast as they possibly can be. |

## See Also

* [What is MariaDB Galera Cluster?](galera-cluster-quickstart-guides/mariadb-galera-cluster-guide.md)
* [About Galera Replication](galera-cluster-quickstart-guides/about-galera-replication.md)
* [Codership: Using Galera Cluster](https://codership.com/content/using-galera-cluster)
* [Getting Started with MariaDB/Galera Cluster](galera-management/getting-started-with-mariadb-galera-cluster.md)
* [MariaDB Galera Cluster and M/S replication](https://www.youtube.com/watch?v=Nd0nvltLPdQ) (video)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
