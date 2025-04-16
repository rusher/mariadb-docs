
# Spider Storage Engine Core Concepts


A typical Spider deployment has a shared-nothing clustered architecture. The system works with any inexpensive hardware, and with a minimum of specific requirements for hardware or software. It consists of a set of computers, with one or more MariaDB processes known as nodes.


The nodes that store the data will be designed as `<code>Backend Nodes</code>`, and can be any MariaDB, MySQL, Oracle server instances using any storage engine available inside the backend.


The `<code>Spider Proxy Nodes</code>` are instances running at least MariaDB 10. `<code>Spider Proxy Nodes</code>` are used to declare per table attachment to the backend nodes. In addition `<code>Spider Proxy Nodes</code>` can be setup to enable the tables to be split and mirrored to multiple `<code>Backend Nodes</code>`.


## Spider Common Usage


![Spider3](../../../.gitbook/assets/spider-storage-engine-core-concepts/+image/Spider3.png "Spider3")
![Spider4](../../../.gitbook/assets/spider-storage-engine-core-concepts/+image/Spider4.png "Spider4")


In the default high availability setup #Spider Nodes

# produce SQL errors when a backend server is not responding. Per table monitoring can be setup to enable availability in case of unresponsive backends `<code>monotoring_bg_kind=1</code>` or `<code>monotoring_bg_kind=2</code>`. The Monitoring Spider Nodes will be inter-connected with usage of the system table `<code>mysql.link_mon_servers</code>` to manage network partitioning. Better known as split brain, an even number of `<code>Spider Monitor Nodes</code>` should be setup to allow a consensus based on the majority. Rather a single separated shared `<code>Monitoring Node</code>` instance or a minimum set of 3 `<code>Spider Nodes</code>`. More information can be found [here](https://fr.slideshare.net/Kentoku/spider-ha-20100922dtt7).



##### MariaDB starting with [10.7.5](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-7-series/mariadb-1075-release-notes.md)
Spider's high availability feature has been deprecated ([MDEV-28479](https://jira.mariadb.org/browse/MDEV-28479)), and will be deleted. Please use other high availability solutions like [replication](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/README.md) or [galera-cluster](../../../server-usage/replication-cluster-multi-master/galera-cluster/galera-cluster-status-variables.md).


## Spider Storage Engine Federation


Spider is a pluggable Storage Engine, acting as a proxy between the optimizer and the remote backends. When the optimizer requests multiple calls to the storage engine, Spider enforces consistency using the 2 phase commit protocol to the backends and by creating transactions on the backends to preserve atomic operations for a single SQL execution. 
Preserving atomic operation during execution is used at multiple levels in the architecture. For the regular optimizer plan, it refers to `<code>multiple split reads</code>` and for concurrent partition scans, it will refer to `<code>semi transactions</code>`.


Costly queries can be more efficient when it is possible to fully push down part of the execution plan on each backend and reduce the result afterwards. Spider enables such execution with some direct execution shortcuts.


![Spider1](../../../.gitbook/assets/spider-storage-engine-core-concepts/+image/Spider1.png "Spider1")


## Spider Threading Model


Spider uses the per partitions and per table model to concurrently access the remote backend nodes. For memory workload that property can be used to define multiple partitions on a single remote backend node to better adapt the concurrency to available CPUs in the hardware.


![Spider2](../../../.gitbook/assets/spider-storage-engine-core-concepts/+image/Spider2.png "Spider2")


Spider maintains an internal dictionary of Table and Index statistics based on separated threads. The statistics are pulled per default on a time line basis and refer to `<code>crd</code>` for cardinality and `<code>sts</code>` for table status.


## Spider Memory Model


Spider stores resultsets into memory, but [spider_quick_mode](spider-system-variables.md)=3 stores resultsets into internal temporary tables if the resultsets are larger than quick_table_size.

