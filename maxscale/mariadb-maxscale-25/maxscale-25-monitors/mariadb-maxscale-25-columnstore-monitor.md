
# ColumnStore Monitor

# ColumnStore Monitor


The ColumnStore monitor, `<code>csmon</code>`, is a monitor module for MariaDB ColumnStore
servers. It supports multiple UM nodes and can detect the correct server for
DML/DDL statements which will be labeled as the master. Other UM nodes will be
used for reads.


## Required Grants


The credentials defined with the `<code>user</code>` and `<code>password</code>` parameters must have all
grants on the `<code>infinidb_vtable</code>` database.


For example, to create a user for this monitor with the required grants execute
the following SQL.



```
CREATE USER 'maxscale'@'maxscalehost' IDENTIFIED BY 'maxscale-password';
GRANT ALL ON infinidb_vtable.* TO 'maxscale'@'maxscalehost';
```



## Master Selection


The ColumnStore Monitor in MaxScale 2.5 supports ColumnStore 1.0, 1.2 and 1.5,
and the master selection is done differently for each version.


* If the version is 1.0, the master server must be specified using the `<code>primary</code>`
parameter.
* If the version is 1.2, the master server is selected automatically using
the ColumnStore function `<code>mcsSystemPrimary()</code>`.
* If the version is 1.5, the master server is selected automatically by
querying the ColumnStore daemon running on each node.


## Configuration


Read the [Monitor Common](mariadb-maxscale-25-common-monitor-parameters.md) document for a list of supported
common monitor parameters.


### `<code>version</code>`


With this mandatory parameter the used ColumnStore version is specified.
The allowed values are `<code>1.0</code>`, `<code>1.2</code>` and `<code>1.5</code>`.


### `<code>primary</code>`


Required and only allowed when the value of `<code>version</code>` is `<code>1.0</code>`.


The `<code>primary</code>` parameter controls which server is chosen as the master
server.


If the server pointed to by this parameter is available and is ready to process
queries, it receives the *Master* status.


### `<code>admin_port</code>`


Allowed only when the value of version is `<code>1.5</code>`.


This optional parameter specifies the port of the ColumnStore administrative
daemon. The default value is `<code>8640</code>`. Note that the daemons of all nodes must
be listening on the same port.


### `<code>admin_base_path</code>`


Allowed only when the value of version is `<code>1.5</code>`.


This optional parameter specifies the base path of the ColumnStore
administrative daemon. The default value is `<code>/cmapi/0.4.0</code>`.


### `<code>api_key</code>`


Allowed only when the value of version is `<code>1.5</code>`.


This optional parameter specifies the API key to be used in the
communication with the ColumnStore administrative daemon. If no
key is specified, then a key will be generated and stored to the
file `<code>api_key.txt</code>` in the directory with the same name as the
monitor in data directory of MaxScale. Typically that will
be `<code>/var/lib/maxscale/<monitor-section>/api_key.txt</code>`.


Note that ColumnStore will store the first key provided and
thereafter require it, so changing the key requires the
resetting of the key on the ColumnStore nodes as well.


### `<code>local_address</code>`


Allowed only when the value of version is `<code>1.5</code>`.


With this parameter it is specified what IP MaxScale should
tell the ColumnStore nodes it resides at. Either it or
`<code>local_address</code>` at the global level in the MaxScale
configuration file must be specified. If both have been
specified, then the one specified for the monitor overrides.


## Commands


The ColumnStore monitor provides module commands using which the ColumnStore
cluster can be managed. The commands can be invoked using the REST-API with
a client such as curl or using maxctrl.


All commands require the monitor instance name as the first parameters.
Additional parameters must be provided depending on the command.


Note that as maxctrl itself has a timeout of 10 seconds, if a
timeout larger than that is provided to any command, the timeout of
maxctrl must also be increased. For instance:



```
maxctrl --timeout 30s call command csmon shutdown CsMonitor 20s
```



Here a 30 second timeout is specified for maxctrl to ensure
that it does not expire before the timeout of 20s provided for
the shutdown command possibly does.


The output is always a JSON object.


In the following, assume a configuration like this:



```
[CsNode1]
type=server
...

[CsNode2]
type=server
...

[CsMonitor]
type=monitor
module=csmon
servers=CsNode1,CsNode2
...
```



### `<code>start</code>`


Starts the ColumnStore cluster.



```
call command csmon start <monitor-name> <timeout>
```



Example



```
call command csmon start CsMonitor 20s
```



### `<code>shutdown</code>`


Shuts down the ColumnStore cluster.



```
call command csmon shutdown <monitor-name> <timeout>
```



Example



```
call command csmon shutdown CsMonitor 20s
```



### `<code>status</code>`


Get the status of the ColumnStore cluster.



```
call command csmon status <monitor-name> [<server>]
```



Returns the status of the cluster or the status of a specific server.


Example



```
call command csmon status CsMonitor
call command csmon status CsMonitor CsNode1
```



### `<code>mode-set</code>`


Sets the mode of the cluster.



```
call command csmon mode-set <monitor-name> (readonly|readwrite) <timeout>
```



Example



```
call command csmon mode-set CsMonitor readonly 20s
```



### `<code>config-get</code>`


Returns the cluster configuration.



```
call command csmon config-get <monitor-name> [<server-name>]
```



If no server is specified, the configuration is fetched from
the first server in the monitor configuration, otherwise from
the specified server.


Note that if everything is in order, the returned configuration
should be identical regardless of the server it is fetched from.


Example



```
call command csmon config-get CsMonitor CsNode2
```



### `<code>add-node</code>`


Adds a new node located on the server at the hostname or IP *host*
to the ColumnStore cluster.



```
call command csmon add-node <monitor-name> <host> <timeout>
```



Example



```
call command csmon add-node CsMonitor mcs2 20s
```



For a more complete example, please refer to [adding a node](#adding-a-node).


### `<code>remove-node</code>`


Remove the node located on the server at the hostname or IP *host*
from the ColumnStore cluster.



```
call command csmon remove-node <monitor-name> <host> <timeout>
```



Example



```
call command csmon remove-node CsMonitor mcs2 20s
```



For a more complete example, please refer to [removing a node](#removing-a-node).


## Example


The following is an example of a `<code>csmon</code>` configuration.



```
[CSMonitor]
type=monitor
module=csmon
version=1.5
servers=CsNode1,CsNode2
user=myuser
password=mypwd
monitor_interval=5000
api_key=somekey1234
```



## Adding a Node


Adding a new node to a ColumnStore cluster can be performed dynamically
at runtime, but it must be done in two steps. First, the node is added
to ColumnStore and then, the corresponding server object (that possibly
has to be created) in the MaxScale configuration is added to the
ColumnStore monitor.


In the following, assume a two node ColumnStore cluster and an initial
MaxScale configuration like.



```
[CsNode1]
type=server
...

[CsNode2]
type=server
...

[CsMonitor]
type=monitor
module=csmon
servers=CsNode1,CsNode2
...
```



Invoking `<code>maxctrl list servers</code>` will now show:



```
┌─────────┬─────────────┬──────┬─────────────┬─────────────────┬──────┐
│ Server  │ Address     │ Port │ Connections │ State           │ GTID │
├─────────┼─────────────┼──────┼─────────────┼─────────────────┼──────┤
│ CsNode1 │ 10.10.10.10 │ 3306 │ 0           │ Master, Running │      │
├─────────┼─────────────┼──────┼─────────────┼─────────────────┼──────┤
│ CsNode2 │ 10.10.10.11 │ 3306 │ 0           │ Slave, Running  │      │
└─────────┴─────────────┴──────┴─────────────┴─────────────────┴──────┘
```



If we now want to add a new ColumnStore node, located at `<code>mcs3/10.10.10.12</code>`
to the cluster, the steps are as follows.


First the node is added



```
maxctrl --timeout 30s call command csmon add-node CsMonitor mcs3 20s
```



After a while the following is output:



```
{
    "links": {
        "self": "http://localhost:8989/v1/maxscale/modules/csmon/add-node"
    },
    "meta": {
        "message": "Node mcs3 successfully added to cluster.",
        "result": {
            "node_id": "mcs3",
            "timestamp": "2020-08-07 10:03:49.474539"
        },
        "success": true
    }
}
```



At this point, the ColumnStore cluster consists of three nodes. However,
the ColumnStore monitor is not yet aware of the new node.


First we need to create the corresponding server object.



```
maxctrl create server CsNode3 10.10.10.12
```



Invoking `<code>maxctrl list servers</code>` will now show:



```
┌─────────┬─────────────┬──────┬─────────────┬─────────────────┬──────┐
│ Server  │ Address     │ Port │ Connections │ State           │ GTID │
├─────────┼─────────────┼──────┼─────────────┼─────────────────┼──────┤
│ CsNode3 │ 10.10.10.12 │ 3306 │ 0           │ Down            │      │
├─────────┼─────────────┼──────┼─────────────┼─────────────────┼──────┤
│ CsNode1 │ 10.10.10.10 │ 3306 │ 0           │ Master, Running │      │
├─────────┼─────────────┼──────┼─────────────┼─────────────────┼──────┤
│ CsNode2 │ 10.10.10.11 │ 3306 │ 0           │ Slave, Running  │      │
└─────────┴─────────────┴──────┴─────────────┴─────────────────┴──────┘
```



The server `<code>CsNode3</code>` has been created, but its state is `<code>Down</code>` since
it is not yet being monitored.



```
┌───────────┬─────────┬──────────────────┐
│ Monitor   │ State   │ Servers          │
├───────────┼─────────┼──────────────────┤
│ CsMonitor │ Running │ CsNode1, CsNode2 │
└───────────┴─────────┴──────────────────┘
```



It must now be added to the monitor.



```
maxctrl link monitor CsMonitor CsNode3
```



Now the server is monitored and `<code>maxctrl list monitors</code>` shows:



```
┌───────────┬─────────┬───────────────────────────┐
│ Monitor   │ State   │ Servers                   │
├───────────┼─────────┼───────────────────────────┤
│ CsMonitor │ Running │ CsNode1, CsNode2, CsNode3 │
└───────────┴─────────┴───────────────────────────┘
```



The state of the new node is now also set correctly, as shown by
`<code>maxctrl list servers</code>`.



```
┌─────────┬─────────────┬──────┬─────────────┬─────────────────┬──────┐
│ Server  │ Address     │ Port │ Connections │ State           │ GTID │
├─────────┼─────────────┼──────┼─────────────┼─────────────────┼──────┤
│ CsNode3 │ 10.10.10.12 │ 3306 │ 0           │ Slave, Running  │      │
├─────────┼─────────────┼──────┼─────────────┼─────────────────┼──────┤
│ CsNode1 │ 10.10.10.10 │ 3306 │ 0           │ Master, Running │      │
├─────────┼─────────────┼──────┼─────────────┼─────────────────┼──────┤
│ CsNode2 │ 10.10.10.11 │ 3306 │ 0           │ Slave, Running  │      │
└─────────┴─────────────┴──────┴─────────────┴─────────────────┴──────┘
```



Note that the MaxScale server object can be created at any point, but
it must not be added to the monitor before the node has been added to
the ColumnStore cluster using `<code>call command csmon add-node</code>`.


## Removing a Node


Removing a node should be performed in the reverse order of how a
node was added. First, the MaxScale server should be removed from the
monitor. Then, the node should be removed from the ColumnStore cluster.


Suppose we want to remove the ColumnStore node at `<code>mcs2/10.10.10.12</code>`
and the current situation is as:



```
┌───────────┬─────────┬───────────────────────────┐
│ Monitor   │ State   │ Servers                   │
├───────────┼─────────┼───────────────────────────┤
│ CsMonitor │ Running │ CsNode1, CsNode2, CsNode3 │
└───────────┴─────────┴───────────────────────────┘
```



First, the server is removed from the monitor.



```
maxctrl unlink monitor CsMonitor CsNode3
```



Checking with `<code>maxctrl list monitors</code>` we see that the server has
indeed been removed.



```
┌───────────┬─────────┬──────────────────┐
│ Monitor   │ State   │ Servers          │
├───────────┼─────────┼──────────────────┤
│ CsMonitor │ Running │ CsNode1, CsNode2 │
└───────────┴─────────┴──────────────────┘
```



Now the node can be removed from the cluster itself.



```
maxctrl --timeout 30s call command csmon remove-node CsMonitor mcs3 20s
{
    "links": {
        "self": "http://localhost:8989/v1/maxscale/modules/csmon/remove-node"
    },
    "meta": {
        "message": "Node mcs3 removed from the cluster.",
        "result": {
            "node_id": "mcs3",
            "timestamp": "2020-08-07 11:41:36.573425"
        },
        "success": true
    }
}
```

