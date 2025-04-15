
# MaxScale and Clustrix Tutorial

# MaxScale and Clustrix Tutorial


Since version 2.4, MaxScale has built-in support for Clustrix. This
tutorial explains how to setup MaxScale in front of a Clustrix
cluster.


There is no Clustrix specific router, but both the
[readconnroute](../maxscale-24-routers/mariadb-maxscale-24-readconnroute.md) and
the [readwritesplit](../maxscale-24-routers/mariadb-maxscale-24-readwritesplit.md) routers can be
used.


## Clustrix and Readconnroute


With *readconnroute* you get simple connection based routing, where
each new connection is created (by default) to the Clustrix node with
the least amount of existing connections. That is, with readconnroute
the behaviour will be very similar to the behaviour when
[HAProxy](https://www.haproxy.org) is used as the Clustrix load
balancer.


### Bootstrap servers


The Clustrix monitor is capable of autonomously figuring out the cluster
configuration, but in order to get going there must be at least one
*server*-section referring to a node in the Clustrix cluster.



```
[Bootstrap-1]
type=server
address=IP-OF-NODE
port=3306
protocol=MySQLBackend
```



That server defintion will be used by the monitor in order to connect
to the Clustrix cluster. There can be more than one such "bootstrap"
definition to cater for the case that the node used as a bootstrap
server is down when MaxScale starts.


**NOTE** These bootstrap servers should *only* be referred to from the
 Clustrix monitor configuration, but *never* from a service.


### Monitor


In the Clustrix monitor section, the bootstrap servers are referred to
in the same way as "ordinary" servers are referred to in other monitors.



```
[Clustrix]
type=monitor
module=clustrixmon
servers=Bootstrap-1
user=USER
password=PASSWORD
```



The bootstrap servers are only used for connecting to the Clustrix
cluster; thereafter the Clustrix monitor will dynamically find out the
cluster configuration.


The discovered cluster configuration will be stored (the ips and ports
of the Clustrix nodes) and upon subsequent restarts the Clustrix
monitor will use that information if the bootstrap servers happen to
be unavailable.


With the configuration above `<code>maxctrl list servers</code>` might output
the following:



```
┌───────────────────┬──────────────┬──────┬─────────────┬─────────────────┬──────┐
│ Server            │ Address      │ Port │ Connections │ State           │ GTID │
├───────────────────┼──────────────┼──────┼─────────────┼─────────────────┼──────┤
│ @@Clustrix:node-7 │ 10.2.224.102 │ 3306 │ 0           │ Master, Running │      │
├───────────────────┼──────────────┼──────┼─────────────┼─────────────────┼──────┤
│ @@Clustrix:node-8 │ 10.2.224.103 │ 3306 │ 0           │ Master, Running │      │
├───────────────────┼──────────────┼──────┼─────────────┼─────────────────┼──────┤
│ @@Clustrix:node-6 │ 10.2.224.101 │ 3306 │ 0           │ Master, Running │      │
├───────────────────┼──────────────┼──────┼─────────────┼─────────────────┼──────┤
│ Bootstrap-1       │ 10.2.224.101 │ 3306 │ 0           │ Master, Running │      │
└───────────────────┴──────────────┴──────┴─────────────┴─────────────────┴──────┘
```



All servers whose name start with `<code>@@</code>` have been detected dynamically.


Note that the address `<code>10.2.224.101</code>` appears twice; once for
`<code>Bootstrap-1</code>` and another time for `<code>@@Clustrix:node-6</code>`. The Clustrix
monitor will create a dynamic server instance for *all* nodes in the
Clustrix cluster; also for the ones used in bootstrap server sections.


### Service


The service is specified as follows:



```
[Clustrix-Service]
type=service
router=readconnroute
user=USER
password=PASSWORD
cluster=Clustrix
```



Note that the service does *not* list any specific servers, but
instead refers, using the argument `<code>cluster</code>`, to the Clustrix monitor.


In practice this means that the service will use the servers of the
monitor named `<code>Clustrix</code>` and in the case of a Clustrix monitor those
servers will be the ones that the monitor has detected
dynamically. That is, when setup like this, the service will
automatically adjust to any changes taking place in the Clustrix
cluster.


**NOTE** There is no need to specify any `<code>router_options</code>`, but the
default `<code>router_options=running</code>` provides the desired behaviour.
In particular do **not** specify `<code>router_options=master</code>` as that will
cause only a *single* node to be used.


### Listener


To complete the configuration, a listener must be specified.



```
[Clustrix-Service-Listener]
type=listener
service=Clustrix-Service
protocol=MariaDBClient
port=4008
```



## Clustrix and Readwritesplit


The primary purpose of the router *readwritesplit* is to split
statements between one master and multiple slaves. In the case of
Clustrix, all servers will be masters, but *readwritesplit* may still
be the right choise.


Namely, as *readwritesplit* is transaction aware and capable of
replaying transactions, it can be used for hiding certain events
taking place in Clustrix from the clients that use it.


For instance, whenever a node is removed from or added to a Clustrix
cluster there will be a *group change*, which is visible to a client
as a transaction rollback. However, if *readwritesplit* is used and
transaction replay is enabled, then MaxScale may be able to hide the
group change so that the client only detects a slight delay.


Apart from the service section, the configuration when using
*readwritesplit* is identical to the *readconnroute* configuration
described above.


### Service


The service is specified as follows:



```
[Clustrix-Service]
type=service
router=readwritesplit
user=maxscale
password=maxscale
cluster=Clustrix
transaction_replay=true
slave_selection_criteria=LEAST_GLOBAL_CONNECTIONS
```



With this configuration, subject to the boundary conditions of
transaction replaying, a client will neither notice group change
events nor the disappearance of the very node the client is connected
to. In that latter case, MaxScale will simply connect to another node
and replay the current transaction (if one is active). For detailed
information about the transaction replay functionality, please refer
to the *readwritesplit*
[documentation](../maxscale-24-routers/mariadb-maxscale-24-readwritesplit.md#transaction_replay).


**NOTE** It is vital to have
`<code>slave_selection_criteria=LEAST_GLOBAL_CONNECTIONS</code>`, as otherwise
connections will **not** be distributed evenly across all Clustrix
nodes.


As a rule of thumb, use *readwritesplit* if it is important that
changes taking place in the cluster configuration are hidden from the
applications, otherwise use *readconnroute*.
