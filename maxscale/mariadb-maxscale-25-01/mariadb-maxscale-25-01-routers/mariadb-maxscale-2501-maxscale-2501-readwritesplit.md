
# MaxScale 25.01 Readwritesplit

# Readwritesplit


This document provides a short overview of the **readwritesplit** router module
and its intended use case scenarios. It also displays all router configuration
parameters with their descriptions. A list of current limitations of the module
is included and use examples are provided.




* [Readwritesplit](#readwritesplit)

  * [Overview](#overview)
  * [Interaction with servers in Maintenance and Draining state](#interaction-with-servers-in-maintenance-and-draining-state)
  * [Configuration](#configuration)
  * [Settings](#settings)

    * [max_slave_connections](#max_slave_connections)

      * [Behavior of max_slave_connections=0](#behavior-of-max_slave_connections0)
    * [slave_connections](#slave_connections)
    * [max_replication_lag](#max_replication_lag)
    * [use_sql_variables_in](#use_sql_variables_in)
    * [master_reconnection](#master_reconnection)
    * [slave_selection_criteria](#slave_selection_criteria)
    * [master_accept_reads](#master_accept_reads)
    * [strict_multi_stmt](#strict_multi_stmt)
    * [strict_sp_calls](#strict_sp_calls)
    * [strict_tmp_tables](#strict_tmp_tables)
    * [master_failure_mode](#master_failure_mode)
    * [retry_failed_reads](#retry_failed_reads)
    * [delayed_retry](#delayed_retry)
    * [delayed_retry_timeout](#delayed_retry_timeout)
    * [transaction_replay](#transaction_replay)
    * [transaction_replay_max_size](#transaction_replay_max_size)
    * [transaction_replay_attempts](#transaction_replay_attempts)
    * [transaction_replay_timeout](#transaction_replay_timeout)
    * [transaction_replay_retry_on_deadlock](#transaction_replay_retry_on_deadlock)
    * [transaction_replay_safe_commit](#transaction_replay_safe_commit)
    * [transaction_replay_retry_on_mismatch](#transaction_replay_retry_on_mismatch)
    * [transaction_replay_checksum](#transaction_replay_checksum)
    * [optimistic_trx](#optimistic_trx)
    * [causal_reads](#causal_reads)

      * [Implementation of causal_reads](#implementation-of-causal_reads)

        * [Normal SQL](#normal-sql)
        * [Prepared Statements](#prepared-statements)
      * [Limitations of Causal Reads](#limitations-of-causal-reads)
    * [causal_reads_timeout](#causal_reads_timeout)
    * [lazy_connect](#lazy_connect)
    * [reuse_prepared_statements](#reuse_prepared_statements)
  * [Router Diagnostics](#router-diagnostics)
  * [Server Ranks](#server-ranks)
  * [Routing hints](#routing-hints)

    * [Known Limitations of Routing Hints](#known-limitations-of-routing-hints)
  * [Module Commands](#module-commands)

    * [reset-gtid](#reset-gtid)
  * [Examples](#examples)
  * [Readwritesplit routing decisions](#readwritesplit-routing-decisions)

    * [Routing to Primary](#routing-to-primary)

      * [Transaction Isolation Level Tracking](#transaction-isolation-level-tracking)
    * [Routing to Replicas](#routing-to-replicas)
    * [Routing to every session backend](#routing-to-every-session-backend)
    * [Routing to previous target](#routing-to-previous-target)
  * [Limitations](#limitations)

    * [Prepared Statement Limitations](#prepared-statement-limitations)
    * [Transaction Replay Limitations](#transaction-replay-limitations)

      * [Limitations in Session State Modifications](#limitations-in-session-state-modifications)
      * [Limitations in Service-to-Service Routing](#limitations-in-service-to-service-routing)
      * [Limitations in multi-statement handling](#limitations-in-multi-statement-handling)
      * [Limitations in client session handling](#limitations-in-client-session-handling)




## Overview


The **readwritesplit** router is designed to increase the read-only processing
capability of a cluster while maintaining consistency. This is achieved by
splitting the query load into read and write queries. Read queries, which do not
modify data, are spread across multiple nodes while all write queries will be
sent to a single node.


The router is designed to be used with a traditional Primary-Replica replication
cluster. It automatically detects changes in the primary server and will use the
current primary server of the cluster. With a Galera cluster, one can achieve a
resilient setup and easy primary failover by using one of the Galera nodes as a
Write-Primary node, where all write queries are routed, and spreading the read
load over all the nodes.


## Interaction with servers in `<code>Maintenance</code>` and `<code>Draining</code>` state


When a server that readwritesplit uses is put into maintenance mode, any ongoing
requests are allowed to finish before the connection is closed. If the server
that is put into maintenance mode is a primary, open transaction are allowed to
complete before the connection is closed. Note that this means neither idle
session nor long-running transactions will be closed by readwritesplit. To
forcefully close the connections, use the following command:



```
maxctrl set server <server> maintenance --force
```



If a server is put into the `<code>Draining</code>` state while a connection is open, the
connection will be used normally. Whenever a new connection needs to be created,
whether that be due to a network error or when a new session being opened, only
servers that are neither `<code>Draining</code>` nor `<code>Drained</code>` will be used.


## Configuration


Readwritesplit router-specific settings are specified in the configuration file
of MariaDB MaxScale in its specific section. The section can be freely named but
the name is used later as a reference in a listener section.


For more details about the standard service parameters, refer to the
[Configuration Guide](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md).


Starting with 2.3, all router parameters can be configured at runtime. Use
`<code>maxctrl alter service</code>` to modify them. The changed configuration will only be
taken into use by new sessions.


## Settings


### `<code>max_slave_connections</code>`


* Type: integer
* Mandatory: No
* Dynamic: Yes
* Default: 255


`<code>max_slave_connections</code>` sets the maximum number of replicas a router session uses
at any moment. The default is to use at most 255 replica connections per client
connection. In older versions the default was to use all available replicas with
no limit.


For MaxScale 2.5.12 and newer, the minimum value is 0.


For MaxScale versions 2.5.11 and older, the minimum value is 1. These versions
suffer from a bug ([MXS-3536](https://jira.mariadb.org/browse/MXS-3536)) that
causes the parameter to accept any values but only function when a value greater
than one was given.


Starting with MaxScale 2.5.0, the use of percentage values in
`<code>max_slave_connections</code>` is deprecated. The support for percentages will be
removed in a future release.


For example, if you have configured MaxScale with one primary and three replicas
and set `<code>max_slave_connections=2</code>`, for each client connection a connection to
the primary and two replica connections would be opened. The read query load
balancing is then done between these two replicas and writes are sent to the
primary.


By tuning this parameter, you can control how dynamic the load balancing is at
the cost of extra created connections. With a lower value of
`<code>max_slave_connections</code>`, less connections per session are created and the set of
possible replica servers is smaller. With a higher value in
`<code>max_slave_connections</code>`, more connections are created which requires more
resources but load balancing will almost always give the best single query
response time and performance. Longer sessions are less affected by a high
`<code>max_slave_connections</code>` as the relative cost of opening a connection is lower.


#### Behavior of `<code>max_slave_connections=0</code>`


When readwritesplit is configured with `<code>max_slave_connections=0</code>`, readwritesplit
will behave slightly differently in that it will route all reads to the current
master server. This is a convenient way to force all of the traffic to go to a
single node while still being able to leverage the replay and reconnection
features of readwritesplit.


In this mode, the behavior of `<code>master_failure_mode=fail_on_write</code>` also changes
slightly. If the current `<code>Master</code>` server fails and a read is done when there's
no other `<code>Master</code>` server available, the connection will be closed. This is done
to prevent an extra slave connection from being opened that would not be closed
if a new `<code>Master</code>` server would arrive.


### `<code>slave_connections</code>`


* Type: integer
* Mandatory: No
* Dynamic: Yes
* Default: 255


This parameter controls how many replica connections each new session starts
with. The default value is 255 which is the same as the default value of
`<code>max_slave_connections</code>`.


In contrast to `<code>max_slave_connections</code>`, `<code>slave_connections</code>` serves as a
soft limit on how many replica connections are created. The number of replica
connections can exceed `<code>slave_connections</code>` if the load balancing algorithm
finds an unconnected replica server better than all other replicas.


Setting this parameter to 1 allows faster connection creation and improved
resource usage due to the smaller amount of initial backend
connections. It is recommended to use `<code>slave_connections=1</code>` when the
lifetime of the client connections is short.


### `<code>max_replication_lag</code>`


* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: 0s


**NOTE** Up until 23.02, this parameter was called `<code>max_slave_replication_lag</code>`,
which has been deprecated but still works as an alias for `<code>max_replication_lag</code>`.


Specify how many seconds a replica is allowed to be behind the primary. The lag of
a replica must be less than the configured value in order for it to be used for
routing. If set to `<code>0s</code>` (the default value), the feature is disabled.


The replica lag must be less than `<code>max_replication_lag</code>`. This means that it
is possible to define, with `<code>max_replication_lag=1s</code>`, that all replicas must
be up to date in order for them to be used for routing.


Note that this feature does not guarantee that writes done on the primary are
visible for reads done on the replica. This is mainly due to the method of
replication lag measurement. For a feature that guarantees this, refer to
[causal_reads](#causal_reads).


The lag is specified as documented
[here](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md). Note that since
the granularity of the lag is seconds, a lag specified in milliseconds will be
rejected, even if the duration is longer than a second.


The Readwritesplit-router does not detect the replication lag itself. A monitor
such as the MariaDB-monitor for a Primary-Replica cluster is required. This option
only affects Primary-Replica clusters. Galera clusters do not have a concept of
replica lag even if the application of write sets might have lag. When a server is
disqualified from routing because of replication lag, a warning is logged. Similarly,
when the server has caught up enough to be a valid routing target, another warning
is logged. These messages are only logged when a query is being routed and the
replication state changes.


Starting with MaxScale versions 23.08.7, 24.02.3 and 25.01.1, readwritesplit
will discard connections to any servers that have excessive replication lag. The
connection will be discarded if a server is lagging behind by more than twice
the amount of `<code>max_replication_lag</code>` and the server is behind by more than 300
seconds (`<code>replication lag > MAX(300, 2 * max_replication_lag)</code>`).


### `<code>use_sql_variables_in</code>`


* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `<code>master</code>`, `<code>all</code>`
* Default: `<code>all</code>`


This parameter controls how `<code>SELECT</code>` statements that use SQL user variables are
handled. Here is an example of such a query that uses it to return an increasing
row number for a resultset:



```
SET @rownum := 0;
SELECT @rownum := @rownum + 1 AS rownum, user, host FROM mysql.user;
```



By default MaxScale will route both the `<code>SET</code>` and `<code>SELECT</code>` statements to all
nodes. Any future reads of the user variables can also be performed on any node.


The possible values for this parameter are:


* `<code>all</code>` (default)
* Modifications to user variables inside `<code>SELECT</code>` statements as well as reads
 of user variables are routed to all servers.
Versions before MaxScale 22.08 returned an error if a user variable was
modified inside of a `<code>SELECT</code>` statement when `<code>use_sql_variables_in=all</code>` was
used. MaxScale 22.08 will instead route the query to all servers and discard
the extra results.
* `<code>master</code>`
* Modifications to user variables inside `<code>SELECT</code>` statements as well as reads
 of user variables are routed to the primary server. This forces more of the
 traffic onto the primary server but it reduces the amount of data that is
 discarded for any `<code>SELECT</code>` statement that also modifies a user
 variable. With this mode, the state of user variables is not deterministic
 if they are modified inside of a `<code>SELECT</code>` statement. `<code>SET</code>` statements that
 modify user variables are still routed to all servers.


DML statements, such as `<code>INSERT</code>`, `<code>UPDATE</code>` or `<code>DELETE</code>`, that modify SQL user
variables are still treated as writes and are only routed to the primary
server. For example, after the following query the value of `<code>@myid</code>` is no longer
the same on all servers and the `<code>SELECT</code>` statement can return different values
depending where it ends up being executed:



```
SET @myid := 0;
INSERT INTO test.t1 VALUES (@myid := @myid + 1);
SELECT @myid; -- Might return 1 or 0
```



### `<code>master_reconnection</code>`


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: true (>= MaxScale 24.02), false(<= MaxScale 23.08)


Allow the primary server to change mid-session. This feature requires that
`<code>disable_sescmd_history</code>` is not used.


Starting with MaxScale 24.02, if `<code>disable_sescmd_history</code>` is enabled,
`<code>master_reconnection</code>` will be automatically disabled.


When a readwritesplit session starts, it will pick a primary server as the
current primary server of that session. When `<code>master_reconnection</code>` is disabled,
when this primary server is lost or changes to another server, the connection
will be closed.


When `<code>master_reconnection</code>` is enabled, readwritesplit can sometimes recover a
lost connection to the primary server. This largely depends on the value of
`<code>master_failure_mode</code>`.


With `<code>master_failure_mode=fail_instantly</code>`, the primary server is only allowed to
change to another server. This change must happen without a loss of the primary
server.


With `<code>master_failure_mode=fail_on_write</code>`, the loss of the primary server is no
longer a fatal error: if a replacement primary server appears before any write
queries are received, readwritesplit will transparently reconnect to the new
primary server.


In both cases the change in the primary server can only take place if
`<code>prune_sescmd_history</code>` is enabled or `<code>max_sescmd_history</code>` has not yet
been exceeded and the session does not have an open transaction.


The recommended configuration is to use `<code>master_reconnection=true</code>` and
`<code>master_failure_mode=fail_on_write</code>`. This provides improved fault tolerance
without any risk to the consistency of the database.


### `<code>slave_selection_criteria</code>`


* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `<code>least_current_operations</code>`, `<code>adaptive_routing</code>`, `<code>least_behind_master</code>`, `<code>least_router_connections</code>`, `<code>least_global_connections</code>`
* Default: `<code>least_current_operations</code>`


This option controls how the readwritesplit router chooses the replicas it
connects to and how the load balancing is done. The default behavior is to route
read queries to the replica server with the lowest amount of ongoing queries i.e.
`<code>least_current_operations</code>`.


The option syntax:



```
slave_selection_criteria=<criteria>
```



Where `<code><criteria></code>` is one of the following values.


* `<code>least_current_operations</code>` (default), the replica with least active operations
* `<code>adaptive_routing</code>`, based on server average response times.
* `<code>least_behind_master</code>`, the replica with smallest replication lag
* `<code>least_global_connections</code>`, the replica with least connections from MariaDB MaxScale
* `<code>least_router_connections</code>`, the replica with least connections from this service


`<code>least_current_operations</code>` uses the current number of active operations
(i.e. SQL queries) as the load balancing metric and it optimizes for maximal
query throughput. Each query gets routed to the server with the least active
operations which results in faster servers processing more traffic.


`<code>adaptive_routing</code>` uses the server response time and current estimated server
load as the load balancing metric. The server that is estimated to finish an
additional query first is chosen. A modified average response time for each
server is continuously updated to allow slow servers at least some traffic and
quickly react to changes in server load conditions. This selection criteria is
designed for heterogeneous clusters: servers of differing hardware, differing
network distances, or when other loads are running on the servers (including a
backup). If the servers are queried by other clients than MaxScale, the load
caused by them is indirectly taken into account.


`<code>least_behind_master</code>` uses the measured replication lag as the load balancing
metric. This means that servers that are more up-to-date are favored which
increases the likelihood of the data being read being up-to-date. However, this
is not as effective as `<code>causal_reads</code>` would be as there's no guarantee that
writes done by the same connection will be routed to a server that has
replicated those changes. The recommended approach is to use
`<code>LEAST_CURRENT_OPERATIONS</code>` or `<code>ADAPTIVE_ROUTING</code>` in combination with
`<code>causal_reads</code>`


**NOTE**: `<code>least_global_connections</code>` and `<code>least_router_connections</code>` should not
be used, they are legacy options that exist only for backwards
compatibility. Using them will result in skewed load balancing as the algorithm
uses a metric that's too coarse (number of connections) to load balance
something that's finer (individual SQL queries).


The `<code>least_global_connections</code>` and `<code>least_router_connections</code>` use the
connections from MariaDB MaxScale to the server, not the amount of connections
reported by the server itself.


Starting with MaxScale versions 2.5.29, 6.4.11, 22.08.9, 23.02.5 and 23.08.1,
lowercase versions of the values are also accepted. For example,
`<code>slave_selection_criteria=LEAST_CURRENT_OPERATIONS</code>` and
`<code>slave_selection_criteria=least_current_operations</code>` are both accepted as valid
values.


Starting with MaxScale 23.08.1, the legacy uppercase values have been
deprecated. All runtime modifications of the parameter will now be persisted in
lowercase. The uppercase values are still accepted but will be removed in a
future MaxScale release.


### `<code>master_accept_reads</code>`


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: false


Enables the primary server to be used for reads. This is a useful option to
enable if you are using a small number of servers and wish to use the primary
for reads as well and the load on it does not reduce the write throughput of the
cluster.


By default, no reads are sent to the primary as long as there is a valid replica
server available. If no replicas are available, reads are sent to the primary
regardless of the value of `<code>master_accept_reads</code>`.



```
# Use the primary for reads
master_accept_reads=true
```



### `<code>strict_multi_stmt</code>`


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: false


When a client executes a multi-statement query, it will be treated as if it were
a DML statement and routed to the primary. If the option is enabled, all queries
after a multi-statement query will be routed to the primary to guarantee a
consistent session state.


If the feature is disabled, queries are routed normally after a multi-statement
query.


**Warning:** Enable the strict mode only if you know that the clients will send
 statements that cause inconsistencies in the session state.



```
# Enable strict multi-statement mode
strict_multi_stmt=true
```



### `<code>strict_sp_calls</code>`


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: false


Similar to `<code>strict_multi_stmt</code>`, this option allows all queries after a CALL
operation on a stored procedure to be routed to the primary.


All warnings and restrictions that apply to `<code>strict_multi_stmt</code>` also apply to
`<code>strict_sp_calls</code>`.


### `<code>strict_tmp_tables</code>`


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: true (>= MaxScale 24.02), false (<= MaxScale 23.08)


When `<code>strict_tmp_tables</code>` is disabled, all temporary tables are lost when a
reconnection of the primary node occurs. This means that if a reconnection to
the primary takes place, temporary tables might appear to disappear in the
middle of a connection.


When `<code>strict_tmp_tables</code>` is enabled, reconnections are prevented as long as a
temporary tables exist. In this case if the primary node is lost and temporary
table exist, the session is closed. If a session creates temporary tables but
does not drop them, this behavior will effectively disable reconnections until
the session is closed.


### `<code>master_failure_mode</code>`


* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `<code>fail_instantly</code>`, `<code>fail_on_write</code>`, `<code>error_on_write</code>`
* Default: `<code>fail_on_write</code>` (MaxScale 23.08: `<code>fail_instantly</code>`)


This option controls how the failure of a primary server is handled.


The following table describes the values for this option and how they treat the
loss of a primary server.


| Value | Description |
| --- | --- |
| Value | Description |
| fail_instantly | When the failure of the primary server is detected, the connection will be closed immediately. |
| fail_on_write | The client connection is closed if a write query is received when no primary is available. |
| error_on_write | If no primary is available and a write query is received, an error is returned stating that the connection is in read-only mode. |


These also apply to new sessions created after the primary has failed. This means
that in `<code>fail_on_write</code>` or `<code>error_on_write</code>` mode, connections are accepted as
long as replica servers are available.


When configured with `<code>fail_on_write</code>` or `<code>error_on_write</code>`, sessions that are idle
will not be closed even if all backend connections for that session have
failed. This is done in the hopes that before the next query from the idle
session arrives, a reconnection to one of the replicas is made. However, this can
leave idle connections around unless the client application actively closes
them. To prevent this, use the
[connection_timeout](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
parameter.


**Note:** If `<code>master_failure_mode</code>` is set to `<code>error_on_write</code>` and the connection
to the primary is lost, by default, clients will not be able to execute write
queries without reconnecting to MariaDB MaxScale once a new primary is
available. If [master_reconnection](#master_reconnection) is enabled, the
session can recover if one of the replicas is promoted as the primary.


### `<code>retry_failed_reads</code>`


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: true


This option controls whether autocommit selects are retried in case of failure.


When a simple autocommit select is being executed outside of a transaction and
the replica server where the query is being executed fails, readwritesplit can
retry the read on a replacement server. This makes the failure of a replica
transparent to the client.


If a part of the result was already delivered to the client, the query will not
be retried. The retrying of queries with partially delivered results is only
possible when `<code>transaction_replay</code>` is enabled.


### `<code>delayed_retry</code>`


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: false


Retry queries over a period of time.


When this feature is enabled, a failure to route a query due to a connection
problem will not immediately result in an error. The routing of the query is
delayed until either a valid candidate server is available or the retry timeout
is reached. If a candidate server becomes available before the timeout is
reached, the query is routed normally and no connection error is returned. If no
candidates are found and the timeout is exceeded, the router returns to normal
behavior and returns an error.


When combined with the `<code>master_reconnection</code>` parameter, failures of writes done
outside of transactions can be hidden from the client connection. This allows a
primary to be replaced while writes are being sent.


Starting with MaxScale 21.06.18, 22.08.15, 23.02.12, 23.08.8, 24.02.4 and
25.01.1, `<code>delayed_retry</code>` will no longer attempt to retry a query if it was
already sent to the database. If a query is received while a valid target server
is not available, the execution of the query is delayed until a valid target is
found or the delayed retry timeout is hit. If a query was already sent, it will
not be replayed to prevent duplicate execution of statements.


In older versions of MaxScale, duplicate execution of a statement can occur if
the connection to the server is lost or the server crashes but the server comes
back up before the timeout for the retrying is exceeded. At this point, if the
server managed to read the client's statement, it will be executed. For this
reason, it is recommended to only enable `<code>delayed_retry</code>` for older versions of
MaxScale when the possibility of duplicate statement execution is an acceptable
risk.


### `<code>delayed_retry_timeout</code>`


* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: 10s


The duration to wait until an error is returned to the client when
`<code>delayed_retry</code>` is enabled.


The timeout is specified as documented
[here](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md). If no explicit unit
is provided, the value is interpreted as seconds in MaxScale 2.4. In subsequent
versions a value without a unit may be rejected. Note that since the granularity
of the timeout is seconds, a timeout specified in milliseconds will be rejected,
even if the duration is longer than a second.


### `<code>transaction_replay</code>`


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: false


Replay interrupted transactions.


Enabling this parameter enables both `<code>delayed_retry</code>` and `<code>master_reconnection</code>`
and sets `<code>master_failure_mode</code>` to `<code>fail_on_write</code>`, thereby overriding any
configured values for these parameters.


When the server where the transaction is in progress fails, readwritesplit can
migrate the transaction to a replacement server. This can completely hide the
failure of a primary node without any visible effects to the client.


If no replacement node becomes available, the client connection is closed.


To control how long a transaction replay can take, use
`<code>transaction_replay_timeout</code>`.


Please refer to the
[Transaction Replay Limitations](#transaction-replay-limitations) section for
a more detailed explanation of what should and should not be done with
transaction replay.


### `<code>transaction_replay_max_size</code>`


* Type: [size](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: 1 MiB


The limit on transaction size for transaction replay in bytes. Any transaction
that exceeds this limit will not be replayed. The default value is 1 MiB. This
limit applies at a session level which means that the total peak memory
consumption can be `<code>transaction_replay_max_size</code>` times the number of client
connections.


The amount of memory needed to store a particular transaction will be slightly
larger than the length in bytes of the SQL used in the transaction. If the limit
is ever exceeded, a message will be logged at the info level.


The number of times that this limit has been exceeded is shown in
`<code>maxctrl show service</code>` as `<code>trx_max_size_exceeded</code>`.


Read [the configuration guide](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
for more details on size type parameters in MaxScale.


### `<code>transaction_replay_attempts</code>`


* Type: integer
* Mandatory: No
* Dynamic: Yes
* Default: 5


The upper limit on how many times a transaction replay is attempted before
giving up.


A transaction replay failure can happen if the server where the transaction is
being replayed fails while the replay is in progress. In practice this parameter
controls how many server and network failures a single transaction replay
tolerates. If a transaction is replayed successfully, the counter for failed
attempts is reset.


### `<code>transaction_replay_timeout</code>`


* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: 30s (>= MaxScale 24.02), 0s (<= MaxScale 23.08)


The time how long transactions are attempted for. To explicitly disable this
feature, set the value to 0 seconds.


The timeout is
[a duration type](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
and the value must include a unit for the duration.


When `<code>transaction_replay_timeout</code>` is enabled, the time a transaction replay can
take is controlled solely by this parameter. This is a more convenient and
predictable method of controlling how long a transaction replay can be attempted
before the connection is closed.


If `<code>delayed_retry_timeout</code>` is less than `<code>transaction_replay_timeout</code>`, it is set
to the same value.


Without `<code>transaction_replay_timeout</code>` the time how long a transaction can be
retried is controlled by `<code>delayed_retry_timeout</code>` and
`<code>transaction_replay_attempts</code>`. This can result in a maximum replay time limit of
`<code>delayed_retry_timeout</code>` multiplied by `<code>transaction_replay_attempts</code>`, by default
this is 50 seconds. The minimum replay time limit can be as low as
`<code>transaction_replay_attempts</code>` seconds (5 seconds by default) in cases where the
connection fails after it was created. Usually this happens due to problems like
the max_connections limit being hit on the database server.


`<code>transaction_replay_timeout</code>` is the recommended method of controlling the
timeouts for transaction replay and is by default set to 30 seconds in MaxScale
24.02.


### `<code>transaction_replay_retry_on_deadlock</code>`


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: false


Enable automatic retrying of transactions that end up in a deadlock.


If this feature is enabled and a transaction returns a deadlock error
(e.g. `<code>SQLSTATE 40001: Deadlock found when trying to get lock; try restarting transaction</code>`),
the transaction is automatically retried. If the retrying of the transaction
results in another deadlock error, it is retried until it either succeeds or a
transaction checksum error is encountered.


### `<code>transaction_replay_safe_commit</code>`


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: true


If a transaction is ending and the `<code>COMMIT</code>` statement at the end of it is
interrupted, there is a risk of duplicating the transaction if it is
replayed. This parameter prevents the retrying of transactions that are about to
commit.


This parameter was added in MaxScale 23.08.0 and is enabled by default. The
older version of MaxScale always attempted to replay the transaction even if
there was a risk of duplicating the transaction.


In MaxScale 25.01.0, this parameter also disabled the replaying of individual
DML statements that `<code>delayed_retry</code>` enabled. The result of this was that only
statements done inside of an explicit transactions or with autocommit disabled
were replayed and writes done with autocommit enabled were never replayed.


In MaxScale 25.01.1 and newer versions, where `<code>delayed_retry no longer attempts
to retry a query if it was already sent to the database, write queries outside
of transactions are delayed if no valid target is found but they are never
retried. Thus</code>`transaction_replay_safe_commit`<code>again only affects how the</code>`COMMIT` of a transaction is handled.


If the data that is about to be modified is read before it is modified and it is
locked in an appropriate manner (e.g. with `<code>SELECT ... FOR UPDATE</code>` or with the
`<code>SERIALIZABLE</code>` isolation level), it is safe to replay a transaction that was
about to commit. This is because the checksum of the transaction will mismatch
if the original transaction ended up committing on the server. Disabling this
feature can enable more robust delivery of transactions but it requires that the
SQL is correctly formed and compatible with this behavior.


### `<code>transaction_replay_retry_on_mismatch</code>`


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: false


Retry transactions that end in checksum mismatch.


When enabled, any replayed transactions that end with a checksum mismatch are
retried until they either succeeds or one of the transaction replay limits is
reached (`<code>delayed_retry_timeout</code>`, `<code>transaction_replay_timeout</code>` or
`<code>transaction_replay_attempts</code>`).


### `<code>transaction_replay_checksum</code>`


* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `<code>full</code>`, `<code>result_only</code>`, `<code>no_insert_id</code>`
* Default: `<code>full</code>`


Selects which transaction checksum method is used to verify the result of the
replayed transaction.


Note that only `<code>transaction_replay_checksum=full</code>` is guaranteed to retain the
consistency of the replayed transaction.


Possible values are:


* `<code>full</code>` (default)
* All responses from the server are included in the checksum. This retains the
 full consistency guarantee of the replayed transaction as it must match
 exactly the one that was already returned to the client.
* `<code>result_only</code>`
* Only resultsets and errors are included in the checksum. OK packets
 (i.e. successful queries that do not return results) are ignored. This mode
 is intended to be used in cases where the extra information (auto-generated
 ID, warnings etc.) returned in the OK packet is not used by the
 application.
This mode is safe to use only if the auto-generated ID is not actually used
by any following queries. An example of such behavior would be a transaction
that ends with an `<code>INSERT</code>` into a table with an `<code>AUTO_INCREMENT</code>` field.
* `<code>no_insert_id</code>`
* The same as `<code>result_only</code>` but results from queries that use
 `<code>LAST_INSERT_ID()</code>` are also ignored. This mode is safe to use only if the
 result of the query is not used by any subsequent statement in the
 transaction.


### `<code>optimistic_trx</code>`


This feature has been moved into the
[OptimisticTrx](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-optimistic-transaction-execution-filter.md) filter in MaxScale 25.01 and the
parameter has been removed from readwritesplit.


### `<code>causal_reads</code>`


* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `<code>none</code>`, `<code>local</code>`, `<code>global</code>`, `<code>fast</code>`, `<code>fast_global</code>`, `<code>universal</code>`, `<code>fast_universal</code>`
* Default: `<code>none</code>`


Enable causal reads. This feature requires MariaDB 10.2.16 or newer to function.


If a client connection modifies the database and `<code>causal_reads</code>` is enabled, any
subsequent reads performed on replica servers will be done in a manner that
prevents replication lag from affecting the results.


The following table contains a comparison of the modes. Read the
[implementation of causal_reads](#implementation-of-causal_reads) for more
information on what a sync consists of and why minimizing the number of them is
important.


| Mode | Level of Causality | Latency |
| --- | --- | --- |
| Mode | Level of Causality | Latency |
| local | Session | Low, one sync per write. |
| fast | Session | None, no sync at all. |
| global | Service | Medium, one sync per read. |
| fast_global | Service | None, no sync at all. |
| universal | Cluster | High, one sync per read plus a roundtrip to the primary. |
| fast_universal | Cluster | Low, one roundtrip to the primary. |


The `<code>fast</code>`, `<code>fast_global</code>` and `<code>fast_universal</code>` modes should only be used when
low latency is more important than proper distribution of reads. These modes
should only be used when the workload is mostly read-only with only occasional
writes. If used with a mixed or a write-heavy workload, the traffic will end up
being routed almost exclusively to the primary server.


**Note:** This feature also enables multi-statement execution of SQL in the
 protocol. This is equivalent to using `<code>allowMultiQueries=true</code>` in
 [Connector/J](../../../connectors/mariadb-connector-j/about-mariadb-connector-j.md#allowmultiqueries)
 or using `<code>CLIENT_MULTI_STATEMENTS</code>` and `<code>CLIENT_MULTI_RESULTS</code>` in the
 Connector/C. The *Implementation of causal_reads* section explains why this is
 necessary.


The possible values for this parameter are:


* `<code>none</code>` (default)
* Read causality is disabled.
* `<code>local</code>`
* Writes are locally visible. Writes are guaranteed to be visible only to the
 connection that does it. Unrelated modifications done by other connections
 are not visible. This mode improves read scalability at the cost of latency
 and reduces the overall load placed on the primary server without breaking
 causality guarantees.
* `<code>global</code>`
* Writes are globally visible. If one connection writes a value, all
 connections to the same service will see it. In general this mode is slower
 than the `<code>local</code>` mode due to the extra synchronization it has to do. This
 guarantees global happens-before ordering of reads when all transactions are
 inside a single GTID domain.This mode gives similar benefits as the `<code>local</code>`
 mode in that it improves read scalability at the cost of latency.
With MaxScale versions 2.5.14 and older, multi-domain use of causal_reads
could cause non-causal reads to occur. Starting with MaxScale 2.5.15, this
was fixed and all the GTID coordinates are passed alongside all requests
which makes multi-domain GTIDs safe to use. However, this does mean that the
GTID coordinates will never be reset: if replication is reset and GTID
coordinates go "backwards", readwritesplit will not consider these as being
newer than the ones already stored. To reset the stored GTID coordinates in
readwritesplit, MaxScale must be restarted.
MaxScale 6.4.11 added the new `<code>reset-gtid</code>` module command to
readwritesplit. This allows the global GTID state used by
`<code>causal_reads=global</code>` to be reset without having to restart MaxScale.
* `<code>fast</code>`
* This mode is similar to the `<code>local</code>` mode where it will only affect the
 connection that does the write but where the `<code>local</code>` mode waits for a replica
 server to catch up, the `<code>fast</code>` mode will only use servers that are known to
 have replicated the write. This means that if no replica has replicated the
 write, the primary where the write was done will be used. The value of
 `<code>causal_reads_timeout</code>` is ignored in this mode. Currently the replication
 state is only updated by the mariadbmon monitor whenever the servers are
 monitored. This means that a smaller `<code>monitor_interval</code>` provides faster
 replication state updates and possibly better overall usage of servers.
This mode is the inverse of the `<code>local</code>` mode in the sense that it improves
read latency at the cost of read scalability while still retaining the
causality guarantees for reads. This functionality can also be considered an
improved version of the functionality that the
[CCRFilter](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-consistent-critical-read-filter.md) module provides.
* `<code>fast_global</code>`
* This mode is identical to the `<code>fast</code>` mode except that it uses the global
 GTID instead of the session local one. This is similar to how `<code>local</code>` and
 `<code>global</code>` modes differ from each other. The value of `<code>causal_reads_timeout</code>`
 is ignored in this mode. Currently the replication state is only updated by
 the mariadbmon monitor whenever the servers are monitored. This means that a
 smaller `<code>monitor_interval</code>` provides faster replication state updates and
 possibly better overall usage of servers.
* `<code>universal</code>`
* The universal mode guarantees that all SELECT statements always see the
 latest observable transaction state on a database cluster. The basis of this
 is the `<code>@@gtid_current_pos</code>` variable which is read from the current primary
 server before each read. This guarantees that if a transaction was visible
 at the time the read is received by readwritesplit, the transaction is
 guaranteed to be complete on the replica server where the read is done.
This mode is the most consistent of all the modes. It provides consistency
regardless of where a write originated from but it comes at the cost of
increased latency. For every read, a round trip to the current primary server
is done. This means that the latency of any given SELECT statement increases
by roughly twice the network latency between MaxScale and the database
cluster. In addition, an extra SELECT statement is always executed on the
primary which places some load on the server.
* `<code>fast_universal</code>`
* A mix of `<code>fast</code>` and `<code>universal</code>`. This mode that guarantees that all SELECT
 statements always see the latest observable transaction state but unlike the
 `<code>universal</code>` mode that waits on the server to catch up, this mode behaves
 like `<code>fast</code>` and routes the query to the current primary if no replicas are
 available that have caught up.
This mode provides the same consistency guarantees of `<code>universal</code>` with a
constant latency overhead of one extra roundtrip. However, this also puts
the most load on the primary node as even a moderate write load can cause
the GTIDs of replicas to lag too far behind.


Before MaxScale 2.5.0, the `<code>causal_reads</code>` parameter was a boolean
parameter. False values translated to `<code>none</code>` and true values translated to
`<code>local</code>`. The use of boolean parameters is deprecated but still accepted in
MaxScale 2.5.0.


#### Implementation of `<code>causal_reads</code>`


This feature is based on the `<code>MASTER_GTID_WAIT</code>` function and the tracking of
server-side status variables. By tracking the latest GTID that each statement
generates, readwritesplit can then perform a synchronization operation with the
help of the `<code>MASTER_GTID_WAIT</code>` function.


If the replica has not caught up to the primary within the configured time, as
specified by [causal_reads_timeout](#causal_reads_timeout), it will
be retried on the primary.


The exception to this rule is the `<code>fast</code>` mode which does not do any
synchronization at all. This can be done as any reads that would go to
out-of-date servers will be re-routed to the current primary.


##### Normal SQL


A practical example can be given by the following set of SQL commands executed
with `<code>autocommit=1</code>`.



```
INSERT INTO test.t1 (id) VALUES (1);
SELECT * FROM test.t1 WHERE id = 1;
```



As the statements are not executed inside a transaction, from the load balancer's
point of view, the latter statement can be routed to a replica server. The problem
with this is that if the value that was inserted on the primary has not yet
replicated to the server where the SELECT statement is being performed, it can
appear as if the value we just inserted is not there.


By prefixing these types of SELECT statements with a command that guarantees
consistent results for the reads, read scalability can be improved without
sacrificing consistency.


The set of example SQL above will be translated by MaxScale into the following
statements.



```
INSERT INTO test.t1 (id) VALUES (1);

-- These are executed as one multi-query
SET @maxscale_secret_variable=(
    SELECT CASE
           WHEN MASTER_GTID_WAIT('0-3000-8', 10) = 0 THEN 1
           ELSE (SELECT 1 FROM INFORMATION_SCHEMA.ENGINES)
    END); SELECT * FROM test.t1 WHERE id = 1;
```



The `<code>SET</code>` command will synchronize the replica to a certain logical point in the
replication stream (see
[MASTER_GTID_WAIT](../../../server/reference/sql-statements-and-structure/sql-statements/built-in-functions/secondary-functions/miscellaneous-functions/master_gtid_wait.md) for more
details). If the synchronization fails, the query will not run and it will be
retried on the server where the transaction was originally done.


##### Prepared Statements


Binary protocol prepared statements are handled in a different manner. Instead
of adding the synchronization SQL into the original SQL query, it is sent as a
separate packet before the prepared statement is executed.


We'll use the same example SQL but use a binary protocol prepared statement for
the SELECT:



```
COM_QUERY:         INSERT INTO test.t1 (id) VALUES (1);
COM_STMT_PREPARE:  SELECT * FROM test.t1 WHERE id = ?;
COM_STMT_EXECUTE:  ? = 123
```



The SQL that MaxScale executes will be the following:



```
COM_QUERY:         INSERT INTO test.t1 (id) VALUES (1);
COM_STMT_PREPARE:  SELECT * FROM test.t1 WHERE id = ?;
COM_QUERY:         IF (MASTER_GTID_WAIT('0-3000-8', 10) <> 0) THEN KILL (SELECT CONNECTION_ID()); END IF
COM_STMT_EXECUTE:  ? = 123
```



Both the synchronization query and the execution of the prepared statement are
sent at the same time. This is done to remove the need to wait for the result of
the synchronization query before routing the execution of the prepared
statement. This keeps the performance of causal_reads for prepared statements
the same as it is for normal SQL queries.


As a result of this, each time the synchronization query times out, the
connection will be killed by the `<code>KILL</code>` statement and readwritesplit will retry
the query on the primary. This is done to prevent the execution of the prepared
statement that follows the synchronization query from being processed by the
MariaDB server.


It is recommend that the session command history is enabled whenever prepared
statements are used with `<code>causal_reads</code>`. This allows new connections to be
created whenever a causal read times out.


A failed causal read inside of a read-only transaction started with
`<code>START TRANSACTION READ ONLY</code>` will return the following error:



```
Error:    1792
SQLSTATE: 25006
Message:  Causal read timed out while in a read-only transaction, cannot retry command.
```



Older versions of MaxScale attempted to retry the command on the current primary
server which would cause the connection to be closed and a warning to be logged.


#### Limitations of Causal Reads


* Starting with MaxScale 24.02.5, the fast modes `<code>fast</code>`, `<code>fast_global</code>` and
 `<code>fast_universal</code>` work with Galera clusters. In older versions, none of the
 `<code>causal_reads</code>` modes worked with Galera. The non-fast modes that rely on the
 [MASTER_GTID_WAIT](../../../server/reference/sql-statements-and-structure/sql-statements/built-in-functions/secondary-functions/miscellaneous-functions/master_gtid_wait.md)
 function still do not work with Galera. This is because Galera does not
 implement a mechanism that allows a client to wait for a particular GTID.
* If the combination of the original SQL statement and the modifications
 added to it by readwritesplit exceed the maximum packet size (16777213 bytes),
 the causal read will not be attempted and a non-causal read is done instead.
 This applies only to text protocol queries as the binary protocol queries use
 a different synchronization mechanism.
* SQL like `<code>INSERT ... RETURNING</code>` that commits a transaction and returns a
 resultset will only work with causal reads if the connector supports the
 DEPRECATE_EOF protocol feature. The following table contains a list of MariaDB
 connectors and whether they support the protocol feature.


| Connector | Supported | Version |
| --- | --- | --- |
| Connector | Supported | Version |
| Connector/J | Yes | 3.5.2 |
| Connector/Node.js | Yes | 3.4.0 |
| Connector/R2DBC | Yes | 1.3.0 |
| Connector/C | No | 3.4.4 |
| Connector/C++ | No | 1.1.5 |
| Connector/ODBC | No | 3.2.5 |


### `<code>causal_reads_timeout</code>`


* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: 10s


The timeout for the replica synchronization done by `<code>causal_reads</code>`.


The timeout is specified as documented
[here](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md). If no explicit unit
is provided, the value is interpreted as seconds in MaxScale 2.4. In subsequent
versions a value without a unit may be rejected. Note that since the granularity
of the timeout is seconds, a timeout specified in milliseconds will be rejected,
even if the duration is longer than a second.


### `<code>lazy_connect</code>`


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: false


Lazy connection creation causes connections to backend servers to be opened only
when they are needed. This reduces the load that is placed on the backend
servers when the client connections are short.


Normally readwritesplit opens as many connections as it can when the session is
first opened. This makes the execution of the first query faster when all
available connections are already created. When `<code>lazy_connect</code>` is enabled, this
initial connection creation is skipped. If the client executes only read
queries, no connection to the primary is made. If only write queries are made,
only the primary connection is used.


In MaxScale 23.08.2, if a [session command](#routing-to-every-session-backend)
is received as the first command, the default behavior is to execute it on a
replica. If [master_accept_reads](#master_accept_reads) is enabled, the query is
executed on the primary server, if one is available. In practice this means that
workloads which are mostly reads with infrequent writes should disable
`<code>master_accept_reads</code>` if they also use `<code>lazy_connect</code>`.


Older versions of MaxScale always tried to execute all session commands on the
primary node if one was available.


### `<code>reuse_prepared_statements</code>`


This feature has been moved into the [PsReuse](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-psreuse.md) filter in
MaxScale 25.01 and the parameter has been removed from readwritesplit.


## Router Diagnostics


The `<code>router_diagnostics</code>` output for a readwritesplit service contains the
following fields.


* `<code>queries</code>`: Number of queries executed through this service.
* `<code>route_master</code>`: Number of writes routed to primary.
* `<code>route_slave</code>`: Number of reads routed to replicas.
* `<code>route_all</code>`: Number of session commands routed to all servers.
* `<code>rw_transactions</code>`: Number of explicit read-write transactions.
* `<code>ro_transactions</code>`: Number of explicit read-only transactions.
* `<code>replayed_transactions</code>`: Number of replayed transactions.
* `<code>server_query_statistics</code>`: Statistics for each configured and used server consisting of the following fields.
* `<code>id</code>`: Name of the server
* `<code>total</code>`: Total number of queries.
* `<code>read</code>`: Total number of reads.
* `<code>write</code>`: Total number of writes.
* `<code>avg_sess_duration</code>`: Average duration of a client session to this server.
* `<code>avg_sess_active_pct</code>`: Average percentage of time client sessions were active. 0% means connections were opened but never used.
* `<code>avg_selects_per_session</code>`: Average number of selects per session.


## Server Ranks


The general rule with server ranks is that primary servers will be used before
secondary servers. Readwritesplit is an exception to this rule. The following
rules govern how readwritesplit behaves with servers that have different ranks.


* Sessions will use the current primary server as long as possible. This means
 that sessions with a secondary primary will not use the main primary as long
 as the secondary primary is available.
* All replica connections will use the same rank as the primary connection. Any
 stale connections with a different rank than the primary will be discarded.
* If no primary connection is available and `<code>master_reconnection</code>` is enabled, a
 connection to the best primary is created. If the new primary has a different
 priority than existing connections have, the connections with a different rank
 will be discarded.
* If open connections exist, these will be used for routing. This means that if
 the primary is lost but the session still has replica servers with the same rank,
 they will remain in use.
* If no open connections exist, the servers with the best rank will used.


## Routing hints


The readwritesplit router supports routing hints. For a detailed guide on hint
syntax and functionality, please read [this](../mariadb-maxscale-25-01-reference/mariadb-maxscale-2501-maxscale-2501-hint-syntax.md)
document.


**Note**: Routing hints will always have the highest priority when a routing
decision is made. This means that it is possible to cause inconsistencies in
the session state and the actual data in the database by adding routing hints
to DDL/DML statements which are then directed to replica servers. Only use routing
hints when you are sure that they can cause no harm.


An exception to this rule is `<code>transaction_replay</code>`: when it is enabled, all
routing hints inside transaction are ignored. This is done to prevent changes
done inside a re-playable transaction from affecting servers outside of the
transaction. This behavior was added in MaxScale 6.1.4. Older versions allowed
routing hints to override the transaction logic.


### Known Limitations of Routing Hints


* If a `<code>SELECT</code>` statement with a `<code>maxscale route to slave</code>` hint is received
 while autocommit is disabled, the query will be routed to a replica server. This
 causes some metadata locks to be acquired on the database in question which
 will block DDL statements on the server until either the connection is closed
 or autocommit is enabled again.


## Module Commands


The readwritesplit router implements the following module commands.


### `<code>reset-gtid</code>`


The command resets the global GTID state in the router. It can be used with
`<code>causal_reads=global</code>` to reset the state. This can be useful when the cluster is
reverted to an earlier state and the GTIDs recorded in MaxScale are no longer
valid.


The first and only argument to the command is the router name. For example, to
reset the GTID state of a readwritesplit named `<code>My-RW-Router</code>`, the following
MaxCtrl command should be used:



```
maxctrl call command readwritesplit reset-gtid My-RW-Router
```



## Examples


Examples of the readwritesplit router in use can be found in the
[Tutorials](https://mariadb.com/kb/Tutorials) folder.


## Readwritesplit routing decisions


Here is a small explanation which shows what kinds of queries are routed to
which type of server.


### Routing to Primary


Routing to primary is important for data consistency and because majority of
writes are written to binlog and thus become replicated to replicas.


The following operations are routed to primary:


* DML statements (`<code>INSERT</code>`, `<code>UPDATE</code>`, `<code>DELETE</code>` etc.)
* DDL statements (`<code>DROP</code>`, `<code>CREATE</code>`, `<code>ALTER</code>` etc.)
* All statements within an open read-write transaction
* Stored procedure calls
* User-defined function calls
* Queries that use sequences (`<code>NEXT VALUE FOR seq</code>`, `<code>NEXTVAL(seq)</code>` or `<code>seq.nextval</code>`)
* Statements that use any of the following functions:
* `<code>LAST_INSERT_ID()</code>`
* `<code>GET_LOCK()</code>`
* `<code>RELEASE_LOCK()</code>`
* `<code>IS_USED_LOCK()</code>`
* `<code>IS_FREE_LOCK()</code>`
* Statements that use any of the following variables:
* `<code>@@last_insert_id</code>`
* `<code>@@identity</code>`


In addition to these, if the **readwritesplit** service is configured with the
`<code>max_replication_lag</code>` parameter, and if all replicas suffer from too much
replication lag, then statements will be routed to the primary. (There might be
other similar configuration parameters in the future which limit the number of
statements that will be routed to replicas.)


#### Transaction Isolation Level Tracking


If either `<code>session_track_transaction_info=CHARACTERISTICS</code>` or
`<code>session_track_system_variables=tx_isolation</code>` is configured for the MariaDB
server, readwritesplit will track the transaction isolation level and lock the
session to the primary when the isolation level is set to serializable. This
retains the correctness of the isolation level which can otherwise cause
problems.


Starting with MaxScale 23.08, once the transaction isolation level is set to
something other than `<code>SERIALIZABLE</code>`, the session is no longer locked to the
primary and returns to its normal state. Older versions of MaxScale remain
locked to the primary even if the session goes out of the `<code>SERIALIZABLE</code>`
isolation level.


### Routing to Replicas


The ability to route some statements to replicas is important because it also
decreases the load targeted to *primary*. Moreover, it is possible to have multiple
replicas to share the load in contrast to single primary.


Queries which can be routed to replicas must be auto committed and belong to one
of the following group:


* Read-only statements (i.e. `<code>SELECT</code>`) that only use read-only built-in functions
* All statements within an explicit read-only transaction (`<code>START TRANSACTION READ ONLY</code>`)
* `<code>SHOW</code>` statements except `<code>SHOW MASTER STATUS</code>`


The list of supported built-in functions can be found
[here](https://github.com/mariadb-corporation/MaxScale/blob/23.02/query_classifier/qc_sqlite/builtin_functions.cc).


### Routing to every session backend


A third class of statements includes those which modify session data, such as
session system variables, user-defined variables, the default database, etc. We
call them session commands, and they must be replicated as they affect the
future results of read and write operations. They must be executed on all
servers that could execute statements on behalf of this client.


Session commands include for example:


* Commands that modify the session state (`<code>SET</code>`, `<code>USE</code>`, `<code>CHANGE USER</code>`)
* Text protocol `<code>PREPARE</code>` statements
* Binary protocol prepared statements
* Other miscellaneous commands (COM_QUIT, COM_PING etc.)


**NOTE**: if variable assignment is embedded in a write statement it is routed
to *primary* only. For example, `<code>INSERT INTO t1 values(@myvar:=5, 7)</code>` would be
routed to *primary* only.


The router stores all of the executed session commands so that in case of a
replica failure, a replacement replica can be chosen and the session command history
can be repeated on that new replica. This means that the router stores each
executed session command for the duration of the session. Applications that use
long-running sessions might cause MariaDB MaxScale to consume a growing amount
of memory unless the sessions are closed. This can be solved by adjusting the
value of `<code>max_sescmd_history</code>`.


### Routing to previous target


In the following cases, a query is routed to the same server where the previous
query was executed. If no previous target is found, the query is routed to the
current primary.


* If a query uses the `<code>FOUND_ROWS()</code>` function, it will be routed to the server
 where the last query was executed. This is done with the assumption that a
 query with `<code>SQL_CALC_FOUND_ROWS</code>` was previously executed.
* COM_STMT_FETCH_ROWS will always be routed to the same server where the
 COM_STMT_EXECUTE was routed.


## Limitations


Read queries are routed to the primary server in the following situations:


* Query is executed inside an open read-write transaction
* Statement includes a stored procedure or an UDF call
* If there are multiple statements inside one query e.g.
 `<code>INSERT INTO ... ; SELECT LAST_INSERT_ID();</code>`


### Prepared Statement Limitations


If a prepared statement targets a temporary table on the primary, the replica
servers will fail to execute it. This will cause all replica connections to be
closed (MXS-1816).


### Transaction Replay Limitations


When transaction replay is enabled, readwritesplit calculates a checksum of the
server responses for each transaction. This is used to determine whether a
replayed transaction was identical to the original transaction. Starting with
MaxScale 23.08, a 128-bit xxHash checksum is stored for each statement that is
in the transaction. Older versions of MaxScale used a single 160-bit SHA1
checksum for the whole transaction.


If the results from the replacement server are not identical when the
transaction is replayed, the client connection is closed. This means that any
transaction with a server specific result (e.g. `<code>NOW()</code>`, `<code>@@server_id</code>`) cannot
be replayed successfully but it will still be attempted.


If a transaction reads data before updating it, the rows should be locked by
using `<code>SELECT ... FOR UPDATE</code>`. This will prevent overlapping transactions when
multiple transactions are being replayed that modify the same set of rows.


If the connection to the server where the transaction is being executed is
lost when the final `<code>COMMIT</code>` is being executed, it is impossible to know
whether the transaction was successfully committed. This means that there
is a possibility for duplicate transaction execution which can result in
data duplication in certain cases.


In MaxScale 23.08, the `<code>transaction_replay_safe_commit</code>` variable controls
whether a replay is attempted or not whenever a `<code>COMMIT</code>` is interrupted. By
default the transaction will not be replayed. Older versions of MaxScale always
replayed the transaction.


Data duplication can happen if the transaction consists of the following
statement types:


* INSERT of rows into a table that does not have an auto-increment primary key
* A "blind update" of one or more rows e.g. `<code>UPDATE t SET c = c + 1 WHERE id = 123</code>`
* A "blind delete" e.g. `<code>DELETE FROM t LIMIT 100</code>`


This is not an exhaustive list and any operations that do not check the row
contents before performing the operation on them might face this problem.


In all cases the problem of duplicate transaction execution can be avoided by
including a `<code>SELECT ... FOR UPDATE</code>` in the statement. This will guarantee that
in the case that the transaction fails when it is being committed, the row is
only modified if it matches the expected contents.


Similarly, a connection loss during `<code>COMMIT</code>` can also result in transaction
replay failure. This happens due to the same reason as duplicate transaction
execution but the retried transaction will not be committed. This can be
considered a success case as the transaction replay detected that the results of
the two transactions are different. In these cases readwritesplit will abort the
transaction and close the client connection.


Statements that result in an implicit commit do not reset the transaction when
transaction_replay is enabled. This means that if the transaction is replayed,
the transaction will be committed twice due to the implicit commit being
present. The exception to this are the transaction management statements such as
`<code>BEGIN</code>` and `<code>START TRANSACTION</code>`: they are detected and will cause the
transaction to be correctly reset.


In older versions of MaxScale, if a connection to a server is lost while a
statement is being executed and the result was partially delivered to the
client, readwritesplit would immediately close the session without attempting to
replay the failing statement. Starting with MaxScale 23.08, this limitation no
longer applies if the statement was done inside of a transaction and
`<code>transaction_replay</code>` is enabled
([MXS-4549](https://jira.mariadb.org/browse/MXS-4549)).


If the connection to the server where a transaction is being executed is lost
while a `<code>ROLLBACK</code>` is being executed, readwritesplit will still attempt to
replay the transaction in the hopes that the real response can be delivered to
the client. However, this does mean that it is possible that a rolled back
transaction which gets replayed ends up with a conflict and is reported as a
replay failure when in reality a rolled back transaction could be safely
ignored.


#### Limitations in Session State Modifications


Any changes to the session state (e.g. autocommit state, SQL mode) done inside a
transaction will remain in effect even if the connection to the server where the
transaction is being executed fails. When readwritesplit creates a new
connection to a server to replay the transaction, it will first restore the
session state by executing all session commands that were executed. This means
that if the session state is changed mid-transaction in a way that affects the
results, transaction replay will fail.


The following partial transaction demonstrates the problem by using
[SQL_MODE](../../../server/server-management/variables-and-modes/sql-mode.md) inside a transaction.



```
SET SQL_MODE='';            -- A session command
BEGIN;
SELECT "hello world";       -- Returns the string "hello world"
SET SQL_MODE='ANSI_QUOTES'; -- A session command
SELECT 'hello world';       -- Returns the string "hello world"
```



If this transaction has to be replayed the actual SQL that gets executed is the
following.



```
SET SQL_MODE='';            -- Replayed session command
SET SQL_MODE='ANSI_QUOTES'; -- Replayed session command
BEGIN;
SELECT "hello world";       -- Returns an error
SELECT 'hello world';       -- Returns the string "hello world"
```



First the session state is restored by executing all commands that changed the
state after which the actual transaction is replayed. Due to the fact that the
SQL_MODE was changed mid-transaction, one of the queries will now return an
error instead of the result we expected leading to a transaction replay failure.


#### Limitations in Service-to-Service Routing


In a service-to-service configuration (i.e. a service using another service in
its `<code>targets</code>` list ), if the topmost service starts a transaction, all
lower-level readwritesplit services will also behave as if a transaction is
open. If a connection to a backend database fails during this, it can result in
unnecessary transaction replays which in turn can end up with checksum
conflicts. The recommended approach is to not use any commands inside a
transaction that would be routed to more than one node.


#### Limitations in multi-statement handling


When a multi-statement query is executed through the readwritesplit router, it
will always be routed to the primary. See
[strict_multi_stmt](mariadb-maxscale-2501-maxscale-2501-readwritesplit.md) for more
details.


If the multi-statement query creates a temporary table, it will not be
detected and reads to this table can be routed to replica servers. To
prevent this, always execute the temporary table creation as an individual
statement.


#### Limitations in client session handling


Some of the queries that a client sends are routed to all backends instead of
just to one. These queries include `<code>USE <db name></code>` and `<code>SET autocommit=0</code>`, among
many others. Readwritesplit sends a copy of these queries to each backend server
and forwards the primary's reply to the client. Below is a list of MySQL commands
which are classified as session commands.



```
COM_INIT_DB (USE <db name> creates this)
COM_CHANGE_USER
COM_STMT_CLOSE
COM_STMT_SEND_LONG_DATA
COM_STMT_RESET
COM_STMT_PREPARE
COM_QUIT (no response, session is closed)
COM_REFRESH
COM_DEBUG
COM_PING
SQLCOM_CHANGE_DB (USE ... statements)
SQLCOM_DEALLOCATE_PREPARE
SQLCOM_PREPARE
SQLCOM_SET_OPTION
SELECT ..INTO variable|OUTFILE|DUMPFILE
SET autocommit=1|0
```



Prior to MaxScale 2.3.0, session commands that were 2²⁴ - 1 bytes or longer were
not supported and caused the session to be closed.


There is a possibility for misbehavior. If `<code>USE mytable</code>` is executed in one of
the replicas and fails, it may be due to replication lag rather than the database
not existing. Thus, the same command may produce different result in different
backend servers. The replicas which fail to execute a session command will be
dropped from the active list of replicas for this session to guarantee a
consistent session state across all the servers used by the session. In
addition, the server will not be used again for routing for the duration of the
session.


The above-mentioned behavior for user variables can be partially controlled with
the configuration parameter `<code>use_sql_variables_in</code>`:



```
use_sql_variables_in=[master|all] (default: all)
```



**WARNING**


If a SELECT query modifies a user variable when the `<code>use_sql_variables_in</code>`
parameter is set to `<code>all</code>`, it will not be routed and the client will receive an
error. A log message is written into the log further explaining the reason for
the error. Here is an example use of a SELECT query which modifies a user
variable and how MariaDB MaxScale responds to it.



```
MySQL [(none)]> set @id=1;
Query OK, 0 rows affected (0.00 sec)

MySQL [(none)]> SELECT @id := @id + 1 FROM test.t1;
ERROR 1064 (42000): Routing query to backend failed. See the error log for further details.
```



Allow user variable modification in SELECT queries by setting
`<code>use_sql_variables_in=master</code>`. This will route all queries that use user
variables to the primary.
