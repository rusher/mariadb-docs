# MariaDB Galera Cluster

Created by Egor Ustinov, last modified on Oct 13, 2025

The MariaDB Galera Cluster dashboard mirrors most sections from the [MariaDB Server](broken-reference) dashboard extending it with **Galera Metrics** section and the **Galera Nodes** table. Use this dashboard when you need Galera-specific cluster health alongside the familiar server views.

***

## Galera Metrics

* **Flow Control Pause %** – Percent of time a node is paused by Galera flow control (backpressure).
* **Flow Control Messages Sent** – “Slow-down” signals sent per second when a node is under pressure.
* **Replication Queue Depth Received** – Size of the receive/apply queue; growth indicates apply lag.
* **Write Conflicts** – Certification conflicts per second (failed concurrent writes on hot rows).
* **Max Galera Replication Latency (s)** – Maximum observed replication/EVS latency per node.
* **Transactions** – Per-node throughput: transactions **received** from peers and/or **replicated** out.
* **Writeset Traffic** – Bytes/s of Galera writesets per node (inbound vs outbound).

### Galera Nodes

Per-node status summary with short state logic:

* **Instance / Status** — Is the server up? (Based on `mariadb_up`)
* **Accept Queries** — Can this node take client traffic right now? (Based on `wsrep_ready`)
* **Local State** — Where is the node in the Galera lifecycle? (Based on `wsrep_local_state`)
* **Flow Control** — Is this node throttling or being throttled? (If any `wsrep_flow_control_*` rate is **> 0** over the interval → **ON**, otherwise **OFF**)
* **Cluster Status** — Is the node in the **Primary** component? (Based on `wsrep_cluster_status`)
* **Connected** — Is the node linked to the group? (Based on `wsrep_connected`)

## Attachments

* &#x20;[image-20251013-152743.png](broken-reference) (image/png)
* &#x20;[image-20251013-152748.png](broken-reference) (image/png)
* &#x20;[image-20251013-152832.png](broken-reference) (image/png)
* &#x20;[image-20251013-161037.png](broken-reference) (image/png)
* &#x20;[image-20251013-161107.png](broken-reference) (image/png)

[Atlassian](http://www.atlassian.com/)
