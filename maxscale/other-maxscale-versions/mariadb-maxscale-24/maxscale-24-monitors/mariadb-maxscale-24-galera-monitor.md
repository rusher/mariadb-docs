
# Galera Monitor

# Galera Monitor




* [Galera Monitor](#galera-monitor)

  * [Overview](#overview)

    * [Galera clusters and slaves replicating from it](#galera-clusters-and-slaves-replicating-from-it)
  * [Configuration](#configuration)
  * [Common Monitor Parameters](#common-monitor-parameters)
  * [Galera Monitor optional parameters](#galera-monitor-optional-parameters)

    * [disable_master_failback](#disable_master_failback)
    * [available_when_donor](#available_when_donor)
    * [disable_master_role_setting](#disable_master_role_setting)
    * [use_priority](#use_priority)
    * [root_node_as_master](#root_node_as_master)
    * [set_donor_nodes](#set_donor_nodes)
  * [Interaction with Server Priorities](#interaction-with-server-priorities)




## Overview


The Galera Monitor is a monitoring module for MaxScale that monitors a Galera
cluster. It detects whether nodes are a part of the cluster and if they are in
sync with the rest of the cluster. It can also assign master and slave roles
inside MaxScale, allowing Galera clusters to be used with modules designed for
traditional master-slave clusters.


By default, the Galera Monitor will choose the node with the lowest
`wsrep_local_index` value as the master. This will mean that two MaxScales
running on different servers will choose the same server as the master.


### Galera clusters and slaves replicating from it


MaxScale 2.4.0 added support for slaves replicating off of Galera nodes. If a
non-Galera server monitored by galeramon is replicating from a Galera node also
monitored by galeramon, it will be assigned the `Slave, Running` status as long
as the replication works. This allows read-scaleout with Galera servers without
increasing the size of the Galera cluster.


## Configuration


A minimal configuration for a monitor requires a set of servers for monitoring
and a username and a password to connect to these servers. The user requires the
REPLICATION CLIENT privilege to successfully monitor the state of the servers.



```
[Galera-Monitor]
type=monitor
module=galeramon
servers=server1,server2,server3
user=myuser
password=mypwd
```



## Common Monitor Parameters


For a list of optional parameters that all monitors support, read the
[Monitor Common](mariadb-maxscale-24-common-monitor-parameters.md) document.


## Galera Monitor optional parameters


These are optional parameters specific to the Galera Monitor.


### `disable_master_failback`


If a node marked as master inside MaxScale happens to fail and the master status
is assigned to another node MaxScale will normally return the master status to
the original node after it comes back up. With this option enabled, if the
master status is assigned to a new node it will not be reassigned to the
original node for as long as the new master node is running.



```
disable_master_failback=true
```



### `available_when_donor`


This option allows Galera nodes to be used normally when they are donors in an
SST operation when the SST method is non-blocking
(e.g. `wsrep_sst_method=mariabackup`).


Normally when an SST is performed, both participating nodes lose their Synced,
Master or Slave statuses. When this option is enabled, the donor is treated as
if it was a normal member of the cluster (i.e. `wsrep_local_state = 4`). This is
especially useful if the cluster drops down to one node and an SST is required
to increase the cluster size.


The current list of non-blocking SST
methods are `xtrabackup`, `xtrabackup-v2` and `mariabackup`. Read the
[wsrep_sst_method](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables)
documentation for more details.



```
available_when_donor=true
```



### `disable_master_role_setting`


This disables the assignment of master and slave roles to the Galera cluster
nodes. If this option is enabled, Synced is the only status assigned by this
monitor.



```
disable_master_role_setting=true
```



### `use_priority`


Enable interaction with server priorities. This will allow the monitor to
deterministically pick the write node for the monitored Galera cluster and will
allow for controlled node replacement.



```
use_priority=true
```



### `root_node_as_master`


This option controls whether the write master Galera node requires a
*wsrep_local_index* value of 0. This option was introduced in MaxScale 2.1.0 and
it is disabled by default in versions 2.1.5 and newer. In versions 2.1.4 and
older, the option was enabled by default.


A Galera cluster will always have a node which has a *wsrep_local_index* value
of 0. Based on this information, multiple MaxScale instances can always pick the
same node for writes.


If the `root_node_as_master` option is disabled for galeramon, the node with the
lowest index will always be chosen as the master. If it is enabled, only the
node with a a *wsrep_local_index* value of 0 can be chosen as the master.


### `set_donor_nodes`


This option controls whether the global variable *wsrep_sst_donor* should be set
in each cluster node with *slave' status*.
The variable contains a list of slave servers, automatically sorted, with
possible master candidates at its end.


The sorting is based either on *wsrep_local_index* or node server *priority*
depending on the value of *use_priority* option.
If no server has *priority* defined the sorting switches to *wsrep_local_index*.
Node names are collected by fetching the result of the variable *wsrep_node_name*.


Example of variable being set in all slave nodes, assuming three nodes:



```
SET GLOBAL wsrep_sst_donor = "galera001,galera000"
```



**Note**:
in order to set the global variable *wsrep_sst_donor*, proper privileges are
required for the monitor user that connects to cluster nodes.
This option is disabled by default and was introduced in MaxScale 2.1.0.



```
set_donor_nodes=true
```



## Interaction with Server Priorities


If the `use_priority` option is set and a server is configured with the
`priority=<int>` parameter, galeramon will use that as the basis on which the
master node is chosen. This requires the `disable_master_role_setting` to be
undefined or disabled. The server with the lowest positive value of *priority*
will be chosen as the master node when a replacement Galera node is promoted to
a master server inside MaxScale. If all candidate servers have the same
priority, the order of the servers in the `servers` parameter dictates which is
chosen as the master.


Nodes with a non-positive value (*priority* <= 0) will never be chosen as the
master. This allows you to mark some servers as permanent slaves by assigning a
non-positive value into *priority*.


Here is an example.



```
[node-1]
type=server
address=192.168.122.101
port=3306
priority=1

[node-2]
type=server
address=192.168.122.102
port=3306
priority=3

[node-3]
type=server
address=192.168.122.103
port=3306
priority=2

[node-4]
type=server
address=192.168.122.104
port=3306
priority=0
```



In this example `node-1` is always used as the master if available. If `node-1`
is not available, then the next node with the highest priority rank is used. In
this case it would be `node-3`. If both `node-1` and `node-3` were down, then
`node-2` would be used. Because `node-4` has a value of 0 in *priority*, it will
never be the master. Nodes without *priority* parameter are considered as
having the lowest priority rank and will be used only if all nodes
with *priority* parameter are not available.


With priority ranks you can control the order in which MaxScale chooses the
master node. This will allow for a controlled failure and replacement of nodes.


CC BY-SA / Gnu FDL


{% @marketo/form formId="4316" %}
