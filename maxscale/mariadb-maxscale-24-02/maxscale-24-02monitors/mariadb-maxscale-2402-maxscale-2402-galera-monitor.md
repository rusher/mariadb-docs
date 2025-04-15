
# MaxScale 24.02 Galera Monitor

# Galera Monitor




* [Galera Monitor](#galera-monitor)

  * [Overview](#overview)

    * [WSREP Variables and Their Effects](#wsrep-variables-and-their-effects)
    * [Galera clusters and replicas replicating from it](#galera-clusters-and-replicas-replicating-from-it)
  * [Required Grants](#required-grants)
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
sync with the rest of the cluster. It can also assign primary and replica roles
inside MaxScale, allowing Galera clusters to be used with modules designed for
traditional primary-replica clusters.


By default, the Galera Monitor will choose the node with the lowest
`<code>wsrep_local_index</code>` value as the primary. This will mean that two MaxScales
running on different servers will choose the same server as the primary.


### WSREP Variables and Their Effects


The following WSREP variables are inspected by galeramon to see whether a node is
usable. If the node is not usable, it loses the `<code>Master</code>` and `<code>Slave</code>` labels and
will be in the `<code>Running</code>` state.


* If `<code>wsrep_ready=0</code>`, the WSREP system is not yet ready and the Galera node
 cannot accept queries.
* If `<code>wsrep_desync=1</code>` is set, the node is desynced and is not participating in
 the Galera replication.
* If `<code>wsrep_reject_queries=[ALL|ALL_KILL]</code>` is set, queries are refused and the
 node is unusable.
* With `<code>wsrep_sst_donor_rejects_queries=1</code>`, donor nodes reject
 queries. Galeramon treats this the same as if `<code>wsrep_reject_queries=ALL</code>` was
 set.
* If `<code>wsrep_local_state</code>` is not 4 (or 2 with `<code>available_when_donor=true</code>`), the
 node is not in the correct state and is not used.


### Galera clusters and replicas replicating from it


MaxScale 2.4.0 added support for replicas replicating off of Galera nodes. If a
non-Galera server monitored by galeramon is replicating from a Galera node also
monitored by galeramon, it will be assigned the `<code>Slave, Running</code>` status as long
as the replication works. This allows read-scaleout with Galera servers without
increasing the size of the Galera cluster.


## Required Grants


The Galera Monitor requires the `<code>REPLICA MONITOR</code>` grant to work:



```
CREATE USER 'maxscale'@'maxscalehost' IDENTIFIED BY 'maxscale-password';
GRANT REPLICA MONITOR ON *.* TO 'maxscale-user'@'maxscalehost';
```



With MariaDB Server 10.4 and earlier, `<code>REPLICATION CLIENT</code>` is required instead.



```
GRANT REPLICATION CLIENT ON *.* TO 'maxscale-user'@'maxscalehost';
```



If `<code>set_donor_nodes</code>` is configured, the `<code>SUPER</code>` grant is required:



```
GRANT SUPER ON *.* TO 'maxscale'@'maxscalehost';
```



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
[Monitor Common](mariadb-maxscale-2402-maxscale-2402-common-monitor-parameters.md) document.


## Galera Monitor optional parameters


These are optional parameters specific to the Galera Monitor.


### `<code>disable_master_failback</code>`


* Type: boolean
* Default: false
* Dynamic: Yes


If a node marked as primary inside MaxScale happens to fail and the primary
status is assigned to another node MaxScale will normally return the primary
status to the original node after it comes back up. With this option enabled, if
the primary status is assigned to a new node it will not be reassigned to the
original node for as long as the new primary node is running. In this case the
`<code>Master Stickiness</code>` status bit is set which will be visible in the
`<code>maxctrl list servers</code>` output.


### `<code>available_when_donor</code>`


* Type: boolean
* Default: false
* Dynamic: Yes


This option allows Galera nodes to be used normally when they are donors in an
SST operation when the SST method is non-blocking
(e.g. `<code>wsrep_sst_method=mariabackup</code>`).


Normally when an SST is performed, both participating nodes lose their `<code>Synced</code>`,
`<code>Master</code>` or `<code>Slave</code>` statuses. When this option is enabled, the donor is treated as
if it was a normal member of the cluster (i.e. `<code>wsrep_local_state = 4</code>`). This is
especially useful if the cluster drops down to one node and an SST is required
to increase the cluster size.


The current list of non-blocking SST
methods are `<code>xtrabackup</code>`, `<code>xtrabackup-v2</code>` and `<code>mariabackup</code>`. Read the
[wsrep_sst_method](../../../server/server-usage/replication-cluster-multi-master/galera-cluster/galera-cluster-system-variables.md)
documentation for more details.


### `<code>disable_master_role_setting</code>`


* Type: boolean
* Default: false
* Dynamic: Yes


This disables the assignment of primary and replica roles to the Galera cluster
nodes. If this option is enabled, Synced is the only status assigned by this
monitor.


### `<code>use_priority</code>`


* Type: boolean
* Default: false
* Dynamic: Yes


Enable interaction with server priorities. This will allow the monitor to
deterministically pick the write node for the monitored Galera cluster and will
allow for controlled node replacement.


### `<code>root_node_as_master</code>`


* Type: boolean
* Default: false
* Dynamic: Yes


This option controls whether the write primary Galera node requires a
*wsrep_local_index* value of 0. This option was introduced in MaxScale 2.1.0 and
it is disabled by default in versions 2.1.5 and newer. In versions 2.1.4 and
older, the option was enabled by default.


A Galera cluster will always have a node which has a *wsrep_local_index* value
of 0. Based on this information, multiple MaxScale instances can always pick the
same node for writes.


If the `<code>root_node_as_master</code>` option is disabled for galeramon, the node with the
lowest index will always be chosen as the primary. If it is enabled, only the
node with a a *wsrep_local_index* value of 0 can be chosen as the primary.


This parameter can work with `<code>disable_master_failback</code>` but using them together
is not advisable: the intention of `<code>root_node_as_master</code>` is to make sure that
all MaxScale instances that are configured to use the same Galera cluster will
send writes to the same node. If `<code>disable_master_failback</code>` is enabled, this is
no longer true if the Galera cluster reorganizes itself in a way that a
different node gets the node index 0, writes would still be going to the old
node that previously had the node index 0. A restart of one of the MaxScales or
a new MaxScale joining the cluster will cause writes to be sent to the wrong
node, thus resulting in an increasing the rate of deadlock errors and
sub-optimal performance.


### `<code>set_donor_nodes</code>`


* Type: boolean
* Default: false
* Dynamic: Yes


This option controls whether the global variable *wsrep_sst_donor* should be set
in each cluster node with *slave' status*.
The variable contains a list of replica servers, automatically sorted, with
possible primary candidates at its end.


The sorting is based either on *wsrep_local_index* or node server *priority*
depending on the value of *use_priority* option.
If no server has *priority* defined the sorting switches to *wsrep_local_index*.
Node names are collected by fetching the result of the variable *wsrep_node_name*.


Example of variable being set in all replica nodes, assuming three nodes:



```
SET GLOBAL wsrep_sst_donor = "galera001,galera000"
```



**Note**:
in order to set the global variable *wsrep_sst_donor*, proper privileges are
required for the monitor user that connects to cluster nodes.
This option is disabled by default and was introduced in MaxScale 2.1.0.


## Interaction with Server Priorities


If the `<code>use_priority</code>` option is set and a server is configured with the
`<code>priority=<int></code>` parameter, galeramon will use that as the basis on which the
primary node is chosen. This requires the `<code>disable_master_role_setting</code>` to be
undefined or disabled. The server with the lowest positive value of *priority*
will be chosen as the primary node when a replacement Galera node is promoted to
a primary server inside MaxScale. If all candidate servers have the same
priority, the order of the servers in the `<code>servers</code>` parameter dictates which is
chosen as the primary.


Nodes with a negative value (*priority* < 0) will never be chosen as the
primary. This allows you to mark some servers as permanent replicas by assigning a
non-positive value into *priority*. Nodes with the default priority of 0 are
only selected if no nodes with higher priority are present and the normal node
selection rules apply to them (i.e. selection is based on `<code>wsrep_local_index</code>`).


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
priority=-1
```



In this example `<code>node-1</code>` is always used as the primary if available. If `<code>node-1</code>`
is not available, then the next node with the highest priority rank is used. In
this case it would be `<code>node-3</code>`. If both `<code>node-1</code>` and `<code>node-3</code>` were down, then
`<code>node-2</code>` would be used. Because `<code>node-4</code>` has a value of -1 in *priority*, it
will never be the primary. Nodes without *priority* parameter are considered as
having a priority of 0 and will be used only if all nodes with a positive
*priority* value are not available.


With priority ranks you can control the order in which MaxScale chooses the
primary node. This will allow for a controlled failure and replacement of nodes.
