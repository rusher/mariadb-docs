# MariaDB Server

Created by Egor Ustinov, last modified on Sep 24, 2025

This dashboard provides a unified view of a database topology. It combines topology information, system health, replication or cluster metrics, and query performance in one place. Administrators can use it to monitor availability, troubleshoot issues, and optimize performance.

***

## Topology Overview

Summarizes the overall topology, showing which servers are active, their versions, and how they are organized.

* Name — Displays the name of the MariaDB topology currently being monitored.
* Project — Shows the associated project or environment label.
* Primary/Replica — A table with:
  * Instance: Server hostname.
  * Type: Instance role.
  * Seconds behind primary: Replication delay value.
  * Status: Availability of the node.
* Topology Info — Count of nodes grouped by type (e.g., server, MaxScale).
* MariaDB Server Uptime by Instance — Uptime in seconds for each server instance.

***

## System Metrics

Monitors server resource usage to detect bottlenecks in CPU, memory, network, and storage.

* CPU Utilisation — Line graph of CPU usage percentage per instance.
* Memory Usage — Percentage of used memory per instance (excluding cache/buffers).
* Network Traffic — Time-series of receive and transmit throughput per instance (bits per second).
* Filesystems Info — Table with filesystem type, mount point, capacity, and instance.
* Disk Used Space Utilisation — Graph of percentage disk space used per mount point.
* Disk IOPS — Reads and writes per second per storage device.

***

## Replication / Cluster Metrics

Provides insight into replication and cluster-related activity, including binary log usage, commit rates, and delay measurements.

* Binlog Size — Current binary log size per instance.
* Binlog Throughput — Bytes written to binary logs per second.
* Binlog Commits — Rate of commit operations recorded in binary logs.
* Replication Lag — Replication delay value reported in seconds.
* Replication Status (table) — Consolidated view of replication health per instance. Fields include:
  * Slave\_connections — Number of replication I/O connections (channels) this server has established to its upstream source.
  * Retried\_transactions — Cumulative count of replicated transactions retried after transient errors (e.g., deadlocks).
  * Slave\_IO\_Running / Slave\_SQL\_Running — Flags showing whether the I/O thread is fetching events and whether the SQL thread is applying them.
  * Last\_Errno / Last\_IO\_Errno / Last\_SQL\_Errno — Most recent numeric error codes reported by replication overall, the I/O thread, and the SQL thread.
  * Read\_Master\_Log\_Pos / Relay\_Log\_Pos — Current read position in the source’s binary log and the last executed position in the local relay log.

***

## Query Metrics

Focuses on query execution and workload behavior, highlighting concurrency, throughput, and inefficiencies.

* Current Threads Running — Number of threads actively executing queries.
* Questions (QPS) — Queries per second executed on each instance.
* Slow Queries — Rate of queries exceeding `long_query_time`.
* Created Tmp Disk Tables — On-disk temporary tables created per second.

***

## Connections

This section provides visibility into how clients connect to the server and whether connection limits or failures are occurring.

* Number of Connections — Current number of active client connections (`Threads_connected`).
* Connection Utilization — Share of connections in use compared to the configured maximum (`Threads_connected / max_connections`).
* % of Aborted Connections — Percentage of connection attempts that failed or were aborted (`aborted_connects / connections`).

***

## Range Metrics

Highlights query access patterns where range operations or scans are used.

* Select Range Scan — Number of `SELECT` operations performing range scans.
* Select Full Range Join — Number of queries that performed a full range join, which indicates a join operation that scanned ranges in both tables. This often reflects suboptimal indexing or join conditions.
* Select Range Check — Number of `SELECT` operations requiring range checks.

***

## InnoDB Metrics

Shows activity within the InnoDB storage engine.

* InnoDB Read/Writes — Shows the rate of physical read and write operations performed by InnoDB (per second). Reads reflect data being fetched from disk; writes reflect pages flushed or inserted to disk.
* InnoDB Buffer Pool Reads — Shows logical reads served from the InnoDB buffer pool vs. pages that had to be evicted or read ahead. Helps identify buffer pool efficiency.
* InnoDB Row Lock — Tracks the number of row lock waits occurring in InnoDB. High values may indicate contention on hot rows or poor indexing.
* InnoDB Checkpoint Age — Displays the size of uncheckpointed redo log data (in bytes). A large checkpoint age can signal risk of longer crash recovery times.
* InnoDB Log Writes — Number of write operations to the InnoDB redo log per second. Indicates how much redo logging activity is happening due to transactions.
* InnoDB History List Length — Tracks the length of the undo log history list. Growth in this metric often points to long-running transactions preventing purge.
* Deadlocks — Number of deadlocks detected by InnoDB. Each deadlock is a situation where two or more transactions block each other, requiring one to be rolled back.

***

## Processlist

Shows information about active sessions and thread states collected from `information_schema.processlist`.

* Processlist Count — Table view showing:
  * Instance: Database node.
  * Client: Client host connected.
  * Value: Number of processes/threads from that client.

***

## Attachments

&#x20;[image-20250922-145525.png](broken-reference) (image/png)\
&#x20;[image-20250922-151811.png](broken-reference) (image/png)\
&#x20;[image-20250922-151856.png](broken-reference) (image/png)\
&#x20;[image-20250922-152006.png](broken-reference) (image/png)\
&#x20;[image-20250922-152032.png](broken-reference) (image/png)\
&#x20;[image-20250922-152056.png](broken-reference) (image/png)\
&#x20;[image-20250922-152350.png](broken-reference) (image/png)\
&#x20;[image-20250922-152527.png](broken-reference) (image/png)

Document generated by Confluence on Oct 13, 2025 16:28

[Atlassian](http://www.atlassian.com/)
