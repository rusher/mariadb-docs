
# Clustrix Monitor

# Clustrix Monitor


## Overview


The Clustrix Monitor is a monitor that monitors a Clustrix cluster. It is
capable of detecting the cluster setup and creating corresponding server
instances within MaxScale.


## Configuration


A minimal configuration for a monitor requires one server in the Clustrix
cluster, and a username and a password to connect to the server. Note that
by default the Clustrix monitor will only use that server in order to
dynamically find out the configuration of the cluster; after startup it
will completely rely upon information obtained at runtime. To change the
default behaviour, please see the parameter
[dynamic_node_detection](#dynamic_node_detection).


To ensure that the Clustrix monitor will be able to start, it is adviseable
to provide *more* than one server to cater for the case that not all nodes
are always up when MaxScale starts.



```
[TheClustrixMonitor]
type=monitor
module=clustrixmon
servers=server1,server2,server3
user=myuser
password=mypwd
```



## Dynamic Servers


The server objects the Clustrix monitor creates for each detected
Clustrix node will be named like



```
@@<name-of-clustrix-monitor>:node-<id>
```



where `<code><name-of-clustrix-monitor></code>` is the name of the Clustrix monitor
instance, as defined in the MaxScale configuration file, and `<code><id></code>` is the
id of the Clustrix node.


For instance, with the Clustrix monitor defined as above and a Clustrix
cluster consisting of 3 nodes whose ids are `<code>1</code>`, `<code>2</code>` and `<code>3</code>` respectively,
the names of the created server objects will be:



```
@@TheClustrixMonitor:node-1
@@TheClustrixMonitor:node-2
@@TheClustrixMonitor:node-3
```



### Grants


Note that the monitor user *must* have `<code>SELECT</code>` grant on the following tables:


* `<code>system.nodeinfo</code>`
* `<code>system.membership</code>`
* `<code>system.softfailed_nodes</code>`


You can give the necessary grants using the following commands:



```
GRANT SELECT ON system.membership TO 'myuser'@'%';
    GRANT SELECT ON system.nodeinfo TO 'myuser'@'%';
    GRANT SELECT ON system.softfailed_nodes TO 'myuser'@'%';
```



Further, if you want be able to *softfail* and *unsoftfail* a node via MaxScale,
then the monitor user must have `<code>SUPER</code>` privileges, which can be granted like:



```
GRANT SUPER ON *.* TO 'myuser'@'%';
```



The user name must be changed to the one actually being used.


## Common Monitor Parameters


For a list of optional parameters that all monitors support, read the
[Monitor Common](mariadb-maxscale-25-common-monitor-parameters.md) document.


## Clustrix Monitor optional parameters


These are optional parameters specific to the Clustrix Monitor.


### `<code>cluster_monitor_interval</code>`


Defines, in milliseconds, how often the monitor checks the state of the
entire cluster. The default value is 60000 (1 minute), which should not
be lowered as that may have an adverse effect on the Cluster itself.



```
cluster_monitor_interval=120000ms
```



The interval is specified as documented
[here](../maxscale-25-getting-started/mariadb-maxscale-25-mariadb-maxscale-configuration-guide.md#durations). If no explicit unit
is provided, the value is interpreted as milliseconds in MaxScale 2.4. In subsequent
versions a value without a unit may be rejected.


### `<code>health_check_threshold</code>`


Defines how many times the health check may fail before the monitor
considers a particular node to be down. The default value is 2.



```
health_check_threshold=3
```



### `<code>dynamic_node_detection</code>`


By default, the Clustrix monitor will only use the bootstrap nodes
in order to connect to the Clustrix cluster and then find out the
cluster configuration dynamically at runtime.


That behaviour can be turned off with this optional parameter, in
which case all Clustrix nodes must manually be defined as shown below.



```
[Node-1]
type=server
address=192.168.121.77
port=3306
...

[Node-2]
...

[Node-3]
...

[Clustrix-Monitor]
type=monitor
module=clustrixmon
servers=Node-1, Node-2, Node-3
dynamic_node_detection=false
```



The default value of `<code>dynamic_node_detection</code>` is `<code>true</code>`.


See also [health_check_port](#health_check_port).


### `<code>health_check_port</code>`


With this optional parameter it can be specified what health check
port to use, if `<code>dynamic_node_detection</code>` has been disabled.



```
health_check_port=4711
```



The default value is `<code>3581</code>`.


Note that this parameter is *ignored* unless `<code>dynamic_node_detection</code>`
is `<code>false</code>`. Note also that the port must be the same for all nodes.


## Commands


The Clustrix monitor supports the following module commands.


### `<code>softfail</code>`


With the `<code>softfail</code>` module command, a node can be *softfailed* via
MaxScale. The command requires as argument the name of the Clustrix
monitor instance (as defined in the configuration file) and the name
of the node to be softfailed.


For instance, with a configuration file like



```
[TheClustrixMonitor]
type=monitor
module=clustrixmon
...
```



then the node whose server name is `<code>@@TheClustrixMonitor:node-1</code>` can
be softfailed like



```
$ maxctrl call command clustrixmon softfail TheClustrixMonitor @@TheClustrixMonitor:node-1
```



If the softfailing of a node is successfully initiated, then the status
of the corresponding MaxScale server object will be set to `<code>Draining</code>`,
which will prevent new connections from being created to the node.


When the number of connections through MaxScale to the node has dropped
to 0, its state will change to `<code>Drained</code>`. Note that the state `<code>Drained</code>`
only tells that there are no connections to the node, not what the state
of the softfailing operation is.


### `<code>unsoftfail</code>`


With the `<code>unsoftfail</code>` module command, a node can be *unsoftfailed* via
MaxScale. The command requires as argument the name of the Clustrix
monitor instance (as defined in the configuration file) and the name
of the node to be unsoftfailed.


With a setup similar to the `<code>softfail</code>` case, a node can be unsoftfailed
like:



```
$ maxctrl call command clustrixmon unsoftfail TheClustrixMonitor @@TheClustrixMonitor:node-1
```



If a node is successfully softfailed, then a `<code>Draining</code>` status of
the corresponding MaxScale server object will be cleared.


## SOFTFAILed nodes


During the cluster check, which is performed once per
`<code>cluster_monitor_interval</code>`, the monitor will also check whether any
nodes are being softfailed. The status of the corresponding server
object of a node being softfailed will be set to `<code>Draining</code>`,
which will prevent new connections from being created to that node.


When the number of connections through MaxScale to the node has dropped
to 0, its state will change to `<code>Drained</code>`. Note that the state `<code>Drained</code>`
only tells that there are no connections to the node, not what the state
of the softfailing operation is.


If a node that was softfailed is UNSOFTFAILed then the `<code>Draining</code>`
status will be cleared.


If the softfailing and unsoftfailing is initiated using the `<code>softfail</code>`
and `<code>unsoftfail</code>` commands of the Clustrix monitor, then there will be
no delay between the softfailing or unsoftfailing being initated and the
`<code>Draining</code>` status being turned on/off.
