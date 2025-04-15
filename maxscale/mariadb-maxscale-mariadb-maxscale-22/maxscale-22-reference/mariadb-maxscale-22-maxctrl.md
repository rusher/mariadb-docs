
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
[REST API documentation](../../mariadb-maxscale-21-06/README.md) and the
[Configuration Guide](../maxscale-22-getting-started/mariadb-maxscale-22-mariadb-maxscale-configuration-usage-scenarios.md).


# Commands


* [list](#list)
* [show](#show)
* [set](#set)
* [clear](#clear)
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
* [call](#call)
* [cluster](#cluster)
* [api](#api)


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
  -q, --quiet     Silence all output                  [boolean] [default: false]
  --tsv           Print tab separated output          [boolean] [default: false]

HTTPS/TLS Options:
  -s, --secure              Enable HTTPS requests     [boolean] [default: false]
  --tls-key                 Path to TLS private key                     [string]
  --tls-cert                Path to TLS public certificate              [string]
  --tls-ca-cert             Path to TLS CA certificate                  [string]
  --tls-verify-server-cert  Whether to verify server TLS certificates
                                                       [boolean] [default: true]

Options:
  --version         Show version number                                [boolean]
  --tls-passphrase  Password for the TLS private key                    [string]
  --help            Show help                                          [boolean]
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
  users                List created network users
  commands             List module commands
```



### list servers


`<code>Usage: list servers</code>`


List all servers in MaxScale.


### list services


`<code>Usage: list services</code>`


List all services and the servers they use.


### list listeners


`<code>Usage: list listeners <service></code>`


List listeners for a service.


### list monitors


`<code>Usage: list monitors</code>`


List all monitors in MaxScale.


### list sessions


`<code>Usage: list sessions</code>`


List all client sessions.


### list filters


`<code>Usage: list filters</code>`


List all filters in MaxScale.


### list modules


`<code>Usage: list modules</code>`


List all currently loaded modules.


### list users


`<code>Usage: list users</code>`


List the users that can be used to connect to the MaxScale REST API.


### list commands


`<code>Usage: list commands</code>`


List all available module commands.


## show



```
Usage: show <command>

Commands:
  server <server>    Show server
  service <service>  Show service
  monitor <monitor>  Show monitor
  session <session>  Show session
  filter <filter>    Show filter
  module <module>    Show loaded module
  maxscale           Show MaxScale information
  logging            Show MaxScale logging information
  commands <module>  Show module commands of a module
```



### show server


`<code>Usage: show server <server></code>`


Show detailed information about a server. The `<code>Parameters</code>` field contains the
currently configured parameters for this server. See `<code>help alter server</code>` for
more details about altering server parameters.


### show service


`<code>Usage: show service <service></code>`


Show detailed information about a service. The `<code>Parameters</code>` field contains the
currently configured parameters for this service. See `<code>help alter service</code>` for
more details about altering service parameters.


### show monitor


`<code>Usage: show monitor <monitor></code>`


Show detailed information about a monitor. The `<code>Parameters</code>` field contains the
currently configured parameters for this monitor. See `<code>help alter monitor</code>` for
more details about altering monitor parameters.


### show session


`<code>Usage: show session <session></code>`


Show detailed information about a single session. The list of sessions can be
retrieved with the `<code>list sessions</code>` command. The <session> is the session ID of a
particular session.


### show filter


`<code>Usage: show filter <filter></code>`


The list of services that use this filter is show in the `<code>Services</code>` field.


### show module


`<code>Usage: show module <module></code>`


This command shows all available parameters as well as detailed version
information of a loaded module.


### show maxscale


`<code>Usage: show maxscale</code>`


See `<code>help alter maxscale</code>` for more details about altering MaxScale parameters.


### show logging


`<code>Usage: show logging</code>`


See `<code>help alter logging</code>` for more details about altering logging parameters.


### show commands


`<code>Usage: show commands <module></code>`


This command shows the parameters the command expects with the parameter
descriptions.


## set



```
Usage: set <command>

Commands:
  server <server> <state>  Set server state
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
  server <name> <host> <port>       Create a new server
  monitor <name> <module>           Create a new monitor
  listener <service> <name> <port>  Create a new listener
  user <name> <password>            Create a new network user

Common create options:
  --protocol               Protocol module name                         [string]
  --authenticator          Authenticator module name                    [string]
  --authenticator-options  Option string for the authenticator          [string]
  --tls-key                Path to TLS key                              [string]
  --tls-cert               Path to TLS certificate                      [string]
  --tls-ca-cert            Path to TLS CA certificate                   [string]
  --tls-version            TLS version to use                           [string]
  --tls-cert-verify-depth  TLS certificate verification depth           [string]

Create server options:
  --services  Link the created server to these services                  [array]
  --monitors  Link the created server to these monitors                  [array]

Create monitor options:
  --servers           Link the created monitor to these servers          [array]
  --monitor-user      Username for the monitor user                     [string]
  --monitor-password  Password for the monitor user                     [string]

Create listener options:
  --interface  Interface to listen on                   [string] [default: "::"]

Create user options:
  --type  Type of user to create
                         [string] [choices: "admin", "basic"] [default: "basic"]
```



### create server


`<code>Usage: create server <name> <host> <port></code>`


The created server will not be used by any services or monitors unless the
--services or --monitors options are given. The list of servers a service or a
monitor uses can be altered with the `<code>link</code>` and `<code>unlink</code>` commands.


### create monitor


`<code>Usage: create monitor <name> <module></code>`


The list of servers given with the --servers option should not contain any
servers that are already monitored by another monitor.


### create listener


`<code>Usage: create listener <service> <name> <port></code>`


The new listener will be taken into use immediately.


### create user


`<code>Usage: create user <name> <password></code>`


The created user can be used with the MaxScale REST API as well as the MaxAdmin
network interface. By default the created user will have read-only privileges.
To make the user an administrative user, use the `<code>--type=admin</code>` option.


## destroy



```
Usage: destroy <command>

Commands:
  server <name>              Destroy an unused server
  monitor <name>             Destroy an unused monitor
  listener <service> <name>  Destroy an unused listener
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


Destroying a monitor causes it to be removed on the next restart. Destroying a
listener at runtime stops it from accepting new connections but it will still be
bound to the listening socket. This means that new listeners cannot be created
to replace destroyed listeners without restarting MaxScale.


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
  maxscale        Start MaxScale by starting all services
```



### start service


`<code>Usage: start service <name></code>`


This starts a service stopped by `<code>stop service <name></code>`


### start monitor


`<code>Usage: start monitor <name></code>`


This starts a monitor stopped by `<code>stop monitor <name></code>`


### start maxscale


`<code>Usage: start maxscale</code>`


This command will execute the `<code>start service</code>` command for all services in
MaxScale.


## stop



```
Usage: stop <command>

Commands:
  service <name>  Stop a service
  monitor <name>  Stop a monitor
  maxscale        Stop MaxScale by stopping all services
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


### stop maxscale


`<code>Usage: stop maxscale</code>`


This command will execute the `<code>stop service</code>` command for all services in
MaxScale.


## alter



```
Usage: alter <command>

Commands:
  server <server> <key> <value>    Alter server parameters
  monitor <monitor> <key> <value>  Alter monitor parameters
  service <service> <key> <value>  Alter service parameters
  logging <key> <value>            Alter logging parameters
  maxscale <key> <value>           Alter MaxScale parameters
```



### alter server


`<code>Usage: alter server <server> <key> <value></code>`


To display the server parameters, execute `<code>show server <server></code>`


### alter monitor


`<code>Usage: alter monitor <monitor> <key> <value></code>`


To display the monitor parameters, execute `<code>show monitor <monitor></code>`


### alter service


`<code>Usage: alter service <service> <key> <value></code>`


To display the service parameters, execute `<code>show service <service></code>`. The
following list of parameters can be altered at runtime:


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
 "max_slave_replication_lag"
]


### alter logging


`<code>Usage: alter logging <key> <value></code>`


To display the logging parameters, execute `<code>show logging</code>`


### alter maxscale


`<code>Usage: alter maxscale <key> <value></code>`


To display the MaxScale parameters, execute `<code>show maxscale</code>`. The following list
of parameters can be altered at runtime:


[
 "auth_connect_timeout",
 "auth_read_timeout",
 "auth_write_timeout",
 "admin_auth",
 "admin_log_auth_failures",
 "passive"
]


## rotate



```
Usage: rotate <command>

Commands:
  logs  Rotate log files by closing and reopening the files
```



### rotate logs


`<code>Usage: rotate logs</code>`


This command is intended to be used with the `<code>logrotate</code>` command.


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
represent the <target> MaxScale. If the synchronization of a MaxScale instance
fails, it will be disabled by executing the `<code>stop maxscale</code>` command on that
instance. Synchronization can be attempted again if a previous attempt failed
due to a network failure or some other ephemeral error. Any other errors require
manual synchronization of the MaxScale configuration files and a restart of the
failed Maxscale.


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
