
# Configuring the Xpand Monitor

# Configuring the Xpand Monitor


This document describes how to configure the Xpand monitor for use
with a Xpand cluster.


## Configuring the Monitor


Contrary to the other monitors of MaxScale, the Xpand monitor will
autonomously figure out the cluster configuration and for each Xpand
node create the corresponding MaxScale server object.


In order to do that, a *sufficient* number of "bootstrap" server instances
must be specified in the MaxScale configuration file for the Xpand
monitor to start with. One server instance is in principle sufficient, but
if the corresponding node happens to be down when MaxScale starts, the
monitor will not be able to function.



```
[Bootstrap1]
type=server
address=10.2.224.101
port=3306
protocol=mariadbbackend

[Bootstrap2]
type=server
address=10.2.224.102
port=3306
protocol=mariadbbackend
```



The server configuration is identical with that of any other server, but since
these servers are *only* used for bootstrapping the Xpand monitor it is
adviceable to use names that clearly will identify them as such.


The actual Xpand monitor configuration looks as follows:



```
[Xpand]
type=monitor
module=xpandmon
servers=Bootstrap1, Bootstrap2
user=monitor_user
password=monitor_password
monitor_interval=2000
cluster_monitor_interval=60000
```



The mandatory parameters are the object type, the monitor module to use, the
list of servers to use for bootstrapping and the username and password to use
when connecting to the servers.


The `<code>monitor_interval</code>` parameter specifies how frequently the monitor should
ping the health check port of each server and the `<code>cluster_monitor_interval</code>`
specifies how frequently the monitor should do a complete cluster check, that
is, access the `<code>system</code>` tables of the Cluster for checking the Cluster
configuration. The default values are `<code>2000</code>` and `<code>60000</code>`, that is, 2 seconds
and 1 minute, respectively.


For each detected Xpand node a corresponding MaxScale server object will be
created, whose name is `<code>@@<Monitor-Name>:node-<id>, where _Monitor-Name_
is the name of the monitor, in this example</code>`Xpand` and *id* is the node id
of the Xpand node. So, with a cluster of three nodes, the created servers
might be named like.



```
@@Xpand:node-2`
@@Xpand:node-3`
@@Xpand:node-7`
```



Note that as these are created at runtime and may disappear at any moment,
depending on changes happening in and made to the Xpand cluster, they
should never be referred to directly from service configurations. Instead,
services should refer to the monitor, as shown in the following:



```
[MyService]
type=service
router=readconnroute
user=service_user
password=service_password
cluster=Xpand
```



Instead of listing the servers of the service explicitly using the `<code>servers</code>`
parameter as usually is the case, the service refers to the Xpand monitor
using the `<code>cluster</code>` parameter. This will cause the service to use the Xpand
nodes that the Xpand monitor discovers at runtime.


For additional details, please consult the monitor
[documentation](../maxscale-25-monitors/mariadb-maxscale-25-xpand-monitor.md).
