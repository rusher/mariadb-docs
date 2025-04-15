
# Galera Monitor

# Galera Monitor


## Overview


The Galera Monitor is a monitoring module for MaxScale that monitors a Galera cluster. It detects whether nodes are a part of the cluster and if they are in sync with the rest of the cluster. It can also assign master and slave roles inside MaxScale, allowing Galera clusters to be used with modules designed for traditional master-slave clusters.


By default, the Galera Monitor will choose the node with the lowest `<code>wsrep_local_index</code>`
value as the master. This will mean that two MaxScales running on different
servers will choose the same server as the master.


## Configuration


A minimal configuration for a monitor requires a set of servers for monitoring and a username and a password to connect to these servers. The user requires the REPLICATION CLIENT privilege to successfully monitor the state of the servers.



```
[Galera Monitor]
type=monitor
module=galeramon
servers=server1,server2,server3
user=myuser
passwd=mypwd
```



## Common Monitor Parameters


For a list of optional parameters that all monitors support, read the [Monitor Common](../../mariadb-maxscale-21-06/README.md) document.


## Galera Monitor optional parameters


These are optional parameters specific to the Galera Monitor.


### `<code>disable_master_failback</code>`


If a node marked as master inside MaxScale happens to fail and the master status is assigned to another node MaxScale will normally return the master status to the original node after it comes back up. With this option enabled, if the master status is assigned to a new node it will not be reassigned to the original node for as long as the new master node is running.



```
disable_master_failback=true
```



### `<code>available_when_donor</code>`


This option only has an effect if there is a single Galera node being backed up an XtraBackup instance. This causes the initial node to go into Donor state which would normally prevent if from being marked as a valid server inside MaxScale. If this option is enabled, a single node in Donor state where the method is XtraBackup will be kept in Synced state.



```
available_when_donor=true
```



### `<code>disable_master_role_setting</code>`


This disables the assignment of master and slave roles to the Galera cluster nodes. If this option is enabled, Synced is the only status assigned by this monitor.



```
disable_master_role_setting=true
```



### `<code>use_priority</code>`


Enable interaction with server priorities. This will allow the monitor to deterministically pick the write node for the monitored Galera cluster and will allow for controlled node replacement.



```
use_priority=true
```



### `<code>root_node_as_master</code>`


This option controls whether the write master Galera node requires a
*wsrep_local_index* value of 0. This option was introduced in MaxScale 2.1.0 and
it is disabled by default in versions 2.1.5 and newer. In versions 2.1.4 and
older, the option was enabled by default.


A Galera cluster will always have a node which has a *wsrep_local_index* value
of 0. Based on this information, multiple MaxScale instances can always pick the
same node for writes.


If the `<code>root_node_as_master</code>` option is disabled for galeramon, the node with the
lowest index will always be chosen as the master. If it is enabled, only the
node with a a *wsrep_local_index* value of 0 can be chosen as the master.


### `<code>set_donor_nodes</code>`


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


If the `<code>use_priority</code>` option is set and a server is configured with the
`<code>priority=<int></code>` parameter, galeramon will use that as the basis on which the
master node is chosen. This requires the `<code>disable_master_role_setting</code>` to be
undefined or disabled. The server with the lowest positive value of *priority*
will be chosen as the master node when a replacement Galera node is promoted to
a master server inside MaxScale.


Nodes with a non-positive value (*priority* <= 0) will never be chosen as the master. This allows
you to mark some servers as permanent slaves by assigning a non-positive value
into *priority*.


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



In this example `<code>node-1</code>` is always used as the master if available. If `<code>node-1</code>`
is not available, then the next node with the highest priority rank is used. In
this case it would be `<code>node-3</code>`. If both `<code>node-1</code>` and `<code>node-3</code>` were down, then
`<code>node-2</code>` would be used. Because `<code>node-4</code>` has a value of 0 in *priority*, it will
never be the master. Nodes without *priority* parameter are considered as
having the lowest priority rank and will be used only if all nodes
with *priority* parameter are not available.


With priority ranks you can control the order in which MaxScale chooses the
master node. This will allow for a controlled failure and replacement of nodes.
