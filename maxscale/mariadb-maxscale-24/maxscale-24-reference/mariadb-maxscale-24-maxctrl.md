
# MaxCtrl

# MaxCtrl


MaxCtrl is a command line administrative client for MaxScale which uses
the MaxScale REST API for communication. It is intended to be the
replacement software for the legacy MaxAdmin command line client.


By default, the MaxScale REST API listens on port 8989 on the local host. The
default credentials for the REST API are `<code>admin:mariadb</code>`. The users used by the
REST API are the same that are used by the MaxAdmin network interface. This
means that any users created for the MaxAdmin network interface should work with
the MaxScale REST API and MaxCtrl.


For more information about the MaxScale REST API, refer to the
[REST API documentation](../maxscale-24-rest-api/maxscale-24-rest-api-maxscale-rest-api.md) and the
[Configuration Guide](../maxscale-24-getting-started/mariadb-maxscale-24-mariadb-maxscale-configuration-guide.md).


# Commands


* [list](#list)
* [show](#show)
* [set](#set)
* [clear](#clear)
* [drain](#drain)
* [enable](#enable)
* [disable](#disable)
* [create](#create)
* [destroy](#destroy)
* [link](#link)
* [unlink](#unlink)
* [start](#start)
* [stop](#stop)
* [alter](#alter)
* [rotate](#rotate)
* [reload](#reload)
* [call](#call)
* [cluster](#cluster)
* [api](#api)
* [classify](#classify)


## Options


All command accept the following global options.



```
-u, --user      Username to use                    [string] [default: "admin"]
  -p, --password  Password for the user. To input the password manually, give -p
                  as the last argument or use --password=''
                                                   [string] [default: "mariadb"]
  -h, --hosts     List of MaxScale hosts. The hosts must be in HOST:PORT format
                  and each value must be separated by a comma.
                                            [string] [default: "localhost:8989"]
  -t, --timeout   Request timeout in milliseconds      [number] [default: 10000]
  -q, --quiet     Silence all output. Ignored while in interactive mode.
                                                      [boolean] [default: false]
  --tsv           Print tab separated output          [boolean] [default: false]

HTTPS/TLS Options:
  -s, --secure                  Enable HTTPS requests [boolean] [default: false]
  --tls-key                     Path to TLS private key                 [string]
  --tls-passphrase              Password for the TLS private key        [string]
  --tls-cert                    Path to TLS public certificate          [string]
  --tls-ca-cert                 Path to TLS CA certificate              [string]
  -n, --tls-verify-server-cert  Whether to verify server TLS certificates
                                                       [boolean] [default: true]

Options:
  --version  Show version number                                       [boolean]
  --help     Show help                                                 [boolean]

If no commands are given, maxctrl is started in interactive mode. Use `exit` to
exit the interactive mode.
```



## list



```
Usage: list <command>

Commands:
  servers              List servers
  services             List services
  listeners <service>  List listeners of a service
  monitors             List monitors
  sessions             List sessions
  filters              List filters
  modules              List loaded modules
  threads              List threads
  users                List created users
  commands             List module commands
```



### list servers


`<code>Usage: list servers</code>`


List all servers in MaxScale.


| Field | Description |
| --- | --- |
| Field | Description |
| Server | Server name |
| Address | Address where the server listens |
| Port | The port on which the server listens |
| Connections | Current connection count |
| State | Server state |
| GTID | Current value of @@gtid_current_pos |


### list services


`<code>Usage: list services</code>`


List all services and the servers they use.


| Field | Description |
| --- | --- |
| Field | Description |
| Service | Service name |
| Router | Router used by the service |
| Connections | Current connection count |
| Total Connections | Total connection count |
| Servers | Servers that the service uses |


### list listeners


`<code>Usage: list listeners <service></code>`


List listeners for a service.


| Field | Description |
| --- | --- |
| Field | Description |
| Name | Listener name |
| Port | The port where the listener listens |
| Host | The address or socket where the listener listens |
| State | Listener state |


### list monitors


`<code>Usage: list monitors</code>`


List all monitors in MaxScale.


| Field | Description |
| --- | --- |
| Field | Description |
| Monitor | Monitor name |
| State | Monitor state |
| Servers | The servers that this monitor monitors |


### list sessions


`<code>Usage: list sessions</code>`


List all client sessions.


| Field | Description |
| --- | --- |
| Field | Description |
| Id | Session ID |
| User | Username |
| Host | Client host address |
| Connected | Time when the session started |
| Idle | How long the session has been idle, in seconds |
| Service | The service where the session connected |


### list filters


`<code>Usage: list filters</code>`


List all filters in MaxScale.


| Field | Description |
| --- | --- |
| Field | Description |
| Filter | Filter name |
| Service | Services that use the filter |
| Module | The module that the filter uses |


### list modules


`<code>Usage: list modules</code>`


List all currently loaded modules.


| Field | Description |
| --- | --- |
| Field | Description |
| Module | Module name |
| Type | Module type |
| Version | Module version |


### list threads


`<code>Usage: list threads</code>`


List all worker threads.


| Field | Description |
| --- | --- |
| Field | Description |
| Id | Thread ID |
| Current FDs | Current number of managed file descriptors |
| Total FDs | Total number of managed file descriptors |
| Load (1s) | Load percentage over the last second |
| Load (1m) | Load percentage over the last minute |
| Load (1h) | Load percentage over the last hour |


### list users


`<code>Usage: list users</code>`


List network the users that can be used to connect to the MaxScale REST API as
well as enabled local accounts.


| Field | Description |
| --- | --- |
| Field | Description |
| Name | User name |
| Type | User type |
| Privileges | User privileges |


### list commands


`<code>Usage: list commands</code>`


List all available module commands.


| Field | Description |
| --- | --- |
| Field | Description |
| Module | Module name |
| Commands | Available commands |


## show



```
Usage: show <command>

Commands:
  server <server>    Show server
  servers            Show all servers
  service <service>  Show service
  services           Show all services
  monitor <monitor>  Show monitor
  monitors           Show all monitors
  session <session>  Show session
  sessions           Show all sessions
  filter <filter>    Show filter
  filters            Show all filters
  module <module>    Show loaded module
  modules            Show all loaded modules
  maxscale           Show MaxScale information
  thread <thread>    Show thread
  threads            Show all threads
  logging            Show MaxScale logging information
  commands <module>  Show module commands of a module
  qc_cache           Show query classifier cache
  dbusers <service>  Show database users of the service
```



### show server


`<code>Usage: show server <server></code>`


Show detailed information about a server. The `<code>Parameters</code>` field contains the currently configured parameters for this server. See `<code>help alter server</code>` for more details about altering server parameters.


| Field | Description |
| --- | --- |
| Field | Description |
| Server | Server name |
| Address | Address where the server listens |
| Port | The port on which the server listens |
| State | Server state |
| Version | Server version |
| Last Event | The type of the latest event |
| Triggered At | Time when the latest event was triggered at |
| Services | Services that use this server |
| Monitors | Monitors that monitor this server |
| Master ID | The server ID of the master |
| Node ID | The node ID of this server |
| Slave Server IDs | List of slave server IDs |
| Statistics | Server statistics |
| Parameters | Server parameters |


### show servers


`<code>Usage: show servers</code>`


Show detailed information about all servers.


| Field | Description |
| --- | --- |
| Field | Description |
| Server | Server name |
| Address | Address where the server listens |
| Port | The port on which the server listens |
| State | Server state |
| Version | Server version |
| Last Event | The type of the latest event |
| Triggered At | Time when the latest event was triggered at |
| Services | Services that use this server |
| Monitors | Monitors that monitor this server |
| Master ID | The server ID of the master |
| Node ID | The node ID of this server |
| Slave Server IDs | List of slave server IDs |
| Statistics | Server statistics |
| Parameters | Server parameters |


### show service


`<code>Usage: show service <service></code>`


Show detailed information about a service. The `<code>Parameters</code>` field contains the currently configured parameters for this service. See `<code>help alter service</code>` for more details about altering service parameters.


| Field | Description |
| --- | --- |
| Field | Description |
| Service | Service name |
| Router | Router that the service uses |
| State | Service state |
| Started At | When the service was started |
| Current Connections | Current connection count |
| Total Connections | Total connection count |
| Servers | Servers that the service uses |
| Filters | Filters that the service uses |
| Parameters | Service parameter |
| Router Diagnostics | Diagnostics provided by the router module |


### show services


`<code>Usage: show services</code>`


Show detailed information about all services.


| Field | Description |
| --- | --- |
| Field | Description |
| Service | Service name |
| Router | Router that the service uses |
| State | Service state |
| Started At | When the service was started |
| Current Connections | Current connection count |
| Total Connections | Total connection count |
| Servers | Servers that the service uses |
| Filters | Filters that the service uses |
| Parameters | Service parameter |
| Router Diagnostics | Diagnostics provided by the router module |


### show monitor


`<code>Usage: show monitor <monitor></code>`


Show detailed information about a monitor. The `<code>Parameters</code>` field contains the currently configured parameters for this monitor. See `<code>help alter monitor</code>` for more details about altering monitor parameters.


| Field | Description |
| --- | --- |
| Field | Description |
| Monitor | Monitor name |
| State | Monitor state |
| Servers | The servers that this monitor monitors |
| Parameters | Monitor parameters |
| Monitor Diagnostics | Diagnostics provided by the monitor module |


### show monitors


`<code>Usage: show monitors</code>`


Show detailed information about all monitors.


| Field | Description |
| --- | --- |
| Field | Description |
| Monitor | Monitor name |
| State | Monitor state |
| Servers | The servers that this monitor monitors |
| Parameters | Monitor parameters |
| Monitor Diagnostics | Diagnostics provided by the monitor module |


### show session


`<code>Usage: show session <session></code>`


Show detailed information about a single session. The list of sessions can be retrieved with the `<code>list sessions</code>` command. The <session> is the session ID of a particular session.


The `<code>Connections</code>` field lists the servers to which the session is connected and the `<code>Connection IDs</code>` field lists the IDs for those connections.


| Field | Description |
| --- | --- |
| Field | Description |
| Id | Session ID |
| Service | The service where the session connected |
| State | Session state |
| User | Username |
| Host | Client host address |
| Connected | Time when the session started |
| Idle | How long the session has been idle, in seconds |
| Connections | Ordered list of backend connections |
| Connection IDs | Thread IDs for the backend connections |
| Queries | Query history |
| Log | Per-session log messages |


### show sessions


`<code>Usage: show sessions</code>`


Show detailed information about all sessions. See `<code>help show session</code>` for more details.


| Field | Description |
| --- | --- |
| Field | Description |
| Id | Session ID |
| Service | The service where the session connected |
| State | Session state |
| User | Username |
| Host | Client host address |
| Connected | Time when the session started |
| Idle | How long the session has been idle, in seconds |
| Connections | Ordered list of backend connections |
| Connection IDs | Thread IDs for the backend connections |
| Queries | Query history |
| Log | Per-session log messages |


### show filter


`<code>Usage: show filter <filter></code>`


The list of services that use this filter is show in the `<code>Services</code>` field.


| Field | Description |
| --- | --- |
| Field | Description |
| Filter | Filter name |
| Module | The module that the filter uses |
| Services | Services that use the filter |
| Parameters | Filter parameters |


### show filters


`<code>Usage: show filters</code>`


Show detailed information of all filters.


| Field | Description |
| --- | --- |
| Field | Description |
| Filter | Filter name |
| Module | The module that the filter uses |
| Services | Services that use the filter |
| Parameters | Filter parameters |


### show module


`<code>Usage: show module <module></code>`


This command shows all available parameters as well as detailed version information of a loaded module.


| Field | Description |
| --- | --- |
| Field | Description |
| Module | Module name |
| Type | Module type |
| Version | Module version |
| Maturity | Module maturity |
| Description | Short description about the module |
| Parameters | All the parameters that the module accepts |
| Commands | Commands that the module provides |


### show modules


`<code>Usage: show modules</code>`


Displays detailed information about all modules.


| Field | Description |
| --- | --- |
| Field | Description |
| Module | Module name |
| Type | Module type |
| Version | Module version |
| Maturity | Module maturity |
| Description | Short description about the module |
| Parameters | All the parameters that the module accepts |
| Commands | Commands that the module provides |


### show maxscale


`<code>Usage: show maxscale</code>`


See `<code>help alter maxscale</code>` for more details about altering MaxScale parameters.


| Field | Description |
| --- | --- |
| Field | Description |
| Version | MaxScale version |
| Commit | MaxScale commit ID |
| Started At | Time when MaxScale was started |
| Activated At | Time when MaxScale left passive mode |
| Uptime | Time MaxScale has been running |
| Parameters | Global MaxScale parameters |


### show thread


`<code>Usage: show thread <thread></code>`


Show detailed information about a worker thread.


| Field | Description |
| --- | --- |
| Field | Description |
| Id | Thread ID |
| Accepts | Number of TCP accepts done by this thread |
| Reads | Number of EPOLLIN events |
| Writes | Number of EPOLLOUT events |
| Hangups | Number of EPOLLHUP and EPOLLRDUP events |
| Errors | Number of EPOLLERR events |
| Avg event queue length | Average number of events returned by one epoll_wait call |
| Max event queue length | Maximum number of events returned by one epoll_wait call |
| Max exec time | The longest time spent processing events returned by a epoll_wait call |
| Max queue time | The longest time an event had to wait before it was processed |
| Current FDs | Current number of managed file descriptors |
| Total FDs | Total number of managed file descriptors |
| Load (1s) | Load percentage over the last second |
| Load (1m) | Load percentage over the last minute |
| Load (1h) | Load percentage over the last hour |
| QC cache size | Query classifier size |
| QC cache inserts | Number of times a new query was added into the query classification cache |
| QC cache hits | How many times a query classification was found in the query classification cache |
| QC cache misses | How many times a query classification was not found in the query classification cache |
| QC cache evictions | How many times a query classification result was evicted from the query classification cache |


### show threads


`<code>Usage: show threads</code>`


Show detailed information about all worker threads.


| Field | Description |
| --- | --- |
| Field | Description |
| Id | Thread ID |
| Accepts | Number of TCP accepts done by this thread |
| Reads | Number of EPOLLIN events |
| Writes | Number of EPOLLOUT events |
| Hangups | Number of EPOLLHUP and EPOLLRDUP events |
| Errors | Number of EPOLLERR events |
| Avg event queue length | Average number of events returned by one epoll_wait call |
| Max event queue length | Maximum number of events returned by one epoll_wait call |
| Max exec time | The longest time spent processing events returned by a epoll_wait call |
| Max queue time | The longest time an event had to wait before it was processed |
| Current FDs | Current number of managed file descriptors |
| Total FDs | Total number of managed file descriptors |
| Load (1s) | Load percentage over the last second |
| Load (1m) | Load percentage over the last minute |
| Load (1h) | Load percentage over the last hour |
| QC cache size | Query classifier size |
| QC cache inserts | Number of times a new query was added into the query classification cache |
| QC cache hits | How many times a query classification was found in the query classification cache |
| QC cache misses | How many times a query classification was not found in the query classification cache |
| QC cache evictions | How many times a query classification result was evicted from the query classification cache |


### show logging


`<code>Usage: show logging</code>`


See `<code>help alter logging</code>` for more details about altering logging parameters.


| Field | Description |
| --- | --- |
| Field | Description |
| Current Log File | The current log file MaxScale is logging into |
| Enabled Log Levels | List of log levels enabled in MaxScale |
| Parameters | Logging parameters |


### show commands


`<code>Usage: show commands <module></code>`


This command shows the parameters the command expects with the parameter descriptions.


| Field | Description |
| --- | --- |
| Field | Description |
| Command | Command name |
| Parameters | Parameters the command supports |
| Descriptions | Parameter descriptions |


### show qc_cache


`<code>Usage: show qc_cache</code>`


Show contents (statement and hits) of query classifier cache.


### show dbusers


`<code>Usage: show dbusers <service></code>`


Show information about the database users of the service


## set



```
Usage: set <command>

Commands:
  server <server> <state>  Set server state

Set options:
  --force  Forcefully close all connections to the target server
                                                      [boolean] [default: false]
```



### set server


`<code>Usage: set server <server> <state></code>`


If <server> is monitored by a monitor, this command should only be used to set
the server into the `<code>maintenance</code>` state. Any other states will be overridden by
the monitor on the next monitoring interval. To manually control server states,
use the `<code>stop monitor <name></code>` command to stop the monitor before setting the
server states manually.


## clear



```
Usage: clear <command>

Commands:
  server <server> <state>  Clear server state
```



### clear server


`<code>Usage: clear server <server> <state></code>`


This command clears a server state set by the `<code>set server <server> <state></code>`
command


## drain



```
Usage: drain <command>

Commands:
  server <server>  Drain a server of connections

Drain options:
  --drain-timeout  Timeout for the drain operation in seconds. If exceeded, the
                   server is added back to all services without putting it into
                   maintenance mode.                      [number] [default: 90]
```



### drain server


`<code>Usage: drain server <server></code>`


This command drains the server of connections by first removing it from all
services after which it waits until all connections are closed. When all
connections are closed, the server is put into the `<code>maintenance</code>` state and added
back to all the services where it was removed from. To take the server back into
use, execute `<code>clear server <server> maintenance</code>`.


## enable



```
Usage: enable <command>

Commands:
  log-priority <log>  Enable log priority [warning|notice|info|debug]
  account <name>      Activate a Linux user account for administrative use

Enable account options:
  --type  Type of user to create
                         [string] [choices: "admin", "basic"] [default: "basic"]
```



### enable log-priority


`<code>Usage: enable log-priority <log></code>`


The `<code>debug</code>` log priority is only available for debug builds of MaxScale.


### enable account


`<code>Usage: enable account <name></code>`


The Linux user accounts are used by the MaxAdmin UNIX Domain Socket interface


## disable



```
Usage: disable <command>

Commands:
  log-priority <log>  Disable log priority [warning|notice|info|debug]
  account <name>      Disable a Linux user account from administrative use
```



### disable log-priority


`<code>Usage: disable log-priority <log></code>`


The `<code>debug</code>` log priority is only available for debug builds of MaxScale.


### disable account


`<code>Usage: disable account <name></code>`


The Linux user accounts are used by the MaxAdmin UNIX Domain Socket interface


## create



```
Usage: create <command>

Commands:
  server <name> <host|socket> [port]   Create a new server
  monitor <name> <module> [params...]  Create a new monitor
  service <name> <router> <params...>  Create a new service
  filter <name> <module> [params...]   Create a new filter
  listener <service> <name> <port>     Create a new listener
  user <name> <password>               Create a new network user
```



### create server


`<code>Usage: create server <name> <host|socket> [port]</code>`


The created server will not be used by any services or monitors unless the
--services or --monitors options are given. The list of servers a service or a
monitor uses can be altered with the `<code>link</code>` and `<code>unlink</code>` commands. If the
<host|socket> argument is an absolute path, the server will use a local UNIX
domain socket connection. In this case the [port] argument is ignored.


### create monitor


`<code>Usage: create monitor <name> <module> [params...]</code>`


The list of servers given with the --servers option should not contain any
servers that are already monitored by another monitor. The last argument to this
command is a list of key=value parameters given as the monitor parameters.


### create service


`<code>Usage: service <name> <router> <params...></code>`


The last argument to this command is a list of key=value parameters given as the
service parameters. If the --servers or --filters options are used, they must be
defined after the service parameters.


Note that the `<code>user</code>` and `<code>password</code>` parameters must be defined.


### create filter


`<code>Usage: filter <name> <module> [params...]</code>`


The last argument to this command is a list of key=value parameters given as the
filter parameters.


### create listener


`<code>Usage: create listener <service> <name> <port></code>`


The new listener will be taken into use immediately.


### create user


`<code>Usage: create user <name> <password></code>`


The created user can be used with the MaxScale REST API as well as the MaxAdmin
network interface. By default the created user will have read-only privileges.
To make the user an administrative user, use the `<code>--type=admin</code>` option. Basic
users can only perform `<code>list</code>` and `<code>show</code>` commands.


## destroy



```
Usage: destroy <command>

Commands:
  server <name>              Destroy an unused server
  monitor <name>             Destroy an unused monitor
  listener <service> <name>  Destroy an unused listener
  service <name>             Destroy an unused service
  filter <name>              Destroy an unused filter
  user <name>                Remove a network user
```



### destroy server


`<code>Usage: destroy server <name></code>`


The server must be unlinked from all services and monitor before it can be
destroyed.


### destroy monitor


`<code>Usage: destroy monitor <name></code>`


The monitor must be unlinked from all servers before it can be destroyed.


### destroy listener


`<code>Usage: destroy listener <service> <name></code>`


Destroying a listener closes the listening socket, opening it up for reuse.


### destroy service


`<code>Usage: destroy service <name></code>`


The service must be unlinked from all servers and filters. All listeners for the
service must be destroyed before the service itself can be destroyed.


### destroy filter


`<code>Usage: destroy filter <name></code>`


The filter must not be used by any service when it is destroyed.


### destroy user


`<code>Usage: destroy user <name></code>`


The last remaining administrative user cannot be removed. Create a replacement
administrative user before attempting to remove the last administrative user.


## link



```
Usage: link <command>

Commands:
  service <name> <server...>  Link servers to a service
  monitor <name> <server...>  Link servers to a monitor
```



### link service


`<code>Usage: link service <name> <server...></code>`


This command links servers to a service, making them available for any
connections that use the service. Before a server is linked to a service, it
should be linked to a monitor so that the server state is up to date. Newly
linked server are only available to new connections, existing connections will
use the old list of servers.


### link monitor


`<code>Usage: link monitor <name> <server...></code>`


Linking a server to a monitor will add it to the list of servers that are
monitored by that monitor. A server can be monitored by only one monitor at a
time.


## unlink



```
Usage: unlink <command>

Commands:
  service <name> <server...>  Unlink servers from a service
  monitor <name> <server...>  Unlink servers from a monitor
```



### unlink service


`<code>Usage: unlink service <name> <server...></code>`


This command unlinks servers from a service, removing them from the list of
available servers for that service. New connections to the service will not use
the unlinked servers but existing connections can still use the servers.


### unlink monitor


`<code>Usage: unlink monitor <name> <server...></code>`


This command unlinks servers from a monitor, removing them from the list of
monitored servers. The servers will be left in their current state when they are
unlinked from a monitor.


## start



```
Usage: start <command>

Commands:
  service <name>  Start a service
  monitor <name>  Start a monitor
  services        Start all services                         [aliases: maxscale]
```



### start service


`<code>Usage: start service <name></code>`


This starts a service stopped by `<code>stop service <name></code>`


### start monitor


`<code>Usage: start monitor <name></code>`


This starts a monitor stopped by `<code>stop monitor <name></code>`


### start services


`<code>Usage: start [services|maxscale]</code>`


This command will execute the `<code>start service</code>` command for all services in
MaxScale.


## stop



```
Usage: stop <command>

Commands:
  service <name>  Stop a service
  monitor <name>  Stop a monitor
  services        Stop all services                          [aliases: maxscale]
```



### stop service


`<code>Usage: stop service <name></code>`


Stopping a service will prevent all the listeners for that service from
accepting new connections. Existing connections will still be handled normally
until they are closed.


### stop monitor


`<code>Usage: stop monitor <name></code>`


Stopping a monitor will pause the monitoring of the servers. This can be used to
manually control server states with the `<code>set server</code>` command.


### stop services


`<code>Usage: stop [services|maxscale]</code>`


This command will execute the `<code>stop service</code>` command for all services in
MaxScale.


## alter



```
Usage: alter <command>

Commands:
  server <server> <key> <value>             Alter server parameters
  [params...]
  monitor <monitor> <key> <value>           Alter monitor parameters
  [params...]
  service <service> <key> <value>           Alter service parameters
  [params...]
  service-filters <service> [filters...]    Alter filters of a service
  logging <key> <value> [params...]         Alter logging parameters
  maxscale <key> <value> [params...]        Alter MaxScale parameters
  user <name> <password>                    Alter admin user passwords
```



### alter server


`<code>Usage: alter server <server> <key> <value> ...</code>`


To display the server parameters, execute `<code>show server <server></code>`.


### alter [params...]


`<code>Usage: alter <command></code>`


Multiple values can be updated at a time by providing the parameter name
followed by the new value. For example, the following command would change both
the `<code>address</code>` and the `<code>port</code>` parameter of a server:


```
alter server server1 address 127.0.0.1 port 3306
```


All alter commands except `<code>alter user</code>` and `<code>alter service-filters</code>` support
multiple parameters.


### alter monitor


`<code>Usage: alter monitor <monitor> <key> <value> ...</code>`


To display the monitor parameters, execute `<code>show monitor <monitor></code>`


### alter [params...]


`<code>Usage: alter <command></code>`


Multiple values can be updated at a time by providing the parameter name
followed by the new value. For example, the following command would change both
the `<code>address</code>` and the `<code>port</code>` parameter of a server:


```
alter server server1 address 127.0.0.1 port 3306
```


All alter commands except `<code>alter user</code>` and `<code>alter service-filters</code>` support
multiple parameters.


### alter service


`<code>Usage: alter service <service> <key> <value> ...</code>`


To display the service parameters, execute `<code>show service <service></code>`. Some
routers support runtime configuration changes to all parameters. Currently all
readconnroute, readwritesplit and schemarouter parameters can be changed at
runtime. In addition to module specific parameters, the following list of common
service parameters can be altered at runtime:


[
 "user",
 "passwd",
 "enable_root_user",
 "max_connections",
 "connection_timeout",
 "auth_all_servers",
 "optimize_wildcard",
 "strip_db_esc",
 "localhost_match_wildcard_host",
 "max_slave_connections",
 "max_slave_replication_lag",
 "retain_last_statements"
]


### alter [params...]


`<code>Usage: alter <command></code>`


Multiple values can be updated at a time by providing the parameter name
followed by the new value. For example, the following command would change both
the `<code>address</code>` and the `<code>port</code>` parameter of a server:


```
alter server server1 address 127.0.0.1 port 3306
```


All alter commands except `<code>alter user</code>` and `<code>alter service-filters</code>` support
multiple parameters.


### alter service-filters


`<code>Usage: alter service-filters <service> [filters...]</code>`


The order of the filters given as the second parameter will also be the order in
which queries pass through the filter chain. If no filters are given, all
existing filters are removed from the service.


For example, the command `<code>maxctrl alter service filters my-service A B C</code>` will
set the filter chain for the service `<code>my-service</code>` so that A gets the query first
after which it is passed to B and finally to C. This behavior is the same as if
the `<code>filters=A|B|C</code>` parameter was defined for the service.


### alter logging


`<code>Usage: alter logging <key> <value> ...</code>`


To display the logging parameters, execute `<code>show logging</code>`


### alter maxscale


`<code>Usage: alter maxscale <key> <value> ...</code>`


To display the MaxScale parameters, execute `<code>show maxscale</code>`. The following list
of parameters can be altered at runtime:


[
 "auth_connect_timeout",
 "auth_read_timeout",
 "auth_write_timeout",
 "admin_auth",
 "admin_log_auth_failures",
 "passive",
 "ms_timestamp",
 "skip_permission_checks",
 "query_retries",
 "query_retry_timeout",
 "retain_last_statements",
 "dump_last_statements"
]


### alter user


`<code>Usage: alter user <name> <password></code>`


Changes the password for a user. To change the user type, destroy the user and
then create it again.


## rotate



```
Usage: rotate <command>

Commands:
  logs  Rotate log files by closing and reopening the files
```



### rotate logs


`<code>Usage: rotate logs</code>`


This command is intended to be used with the `<code>logrotate</code>` command.


## reload



```
Usage: reload <command>

Commands:
  service <service>  Reloads the database users of this service
```



### reload service


`<code>Usage: reload service <service></code>`


## call



```
Usage: call <command>

Commands:
  command <module> <command> [params...]  Call a module command
```



### call command


`<code>Usage: call command <module> <command> [params...]</code>`


To inspect the list of module commands, execute `<code>list commands</code>`


## cluster



```
Usage: cluster <command>

Commands:
  diff <target>  Show difference between host servers and <target>.
  sync <target>  Synchronize the cluster with target MaxScale server.
```



### cluster diff


`<code>Usage: cluster diff <target></code>`


The list of host servers is controlled with the --hosts option. The target
server should not be in the host list. Value of <target> must be in HOST:PORT
format


### cluster sync


`<code>Usage: cluster sync <target></code>`


This command will alter all MaxScale instances given in the --hosts option to
represent the <target> MaxScale. Value of <target> must be in HOST:PORT format.
Synchronization can be attempted again if a previous attempt failed due to a
network failure or some other ephemeral error. Any other errors require manual
synchronization of the MaxScale configuration files and a restart of the failed
Maxscale.


Note: New objects created by `<code>cluster sync</code>` will have a placeholder value and
must be manually updated. Passwords for existing objects will not be updated by
`<code>cluster sync</code>` and must also be manually updated.


## api



```
Usage: api <command>

Commands:
  get <resource> [path]  Get raw JSON

API options:
  --sum  Calculate sum of API result. Only works for arrays of numbers e.g. `api
         get --sum servers data[].attributes.statistics.connections`.
                                                      [boolean] [default: false]
```



### api get


`<code>Usage: get <resource> [path]</code>`


Perform a raw REST API call. The path definition uses JavaScript syntax to
extract values. For example, the following command extracts all server states as
an array of JSON values: maxctrl api get servers data[].attributes.state


## classify



```
Usage: classify <statement>
```

