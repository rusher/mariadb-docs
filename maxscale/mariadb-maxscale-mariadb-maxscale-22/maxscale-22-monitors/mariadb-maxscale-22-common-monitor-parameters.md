
# MaxScale 2.2 Common Monitor Parameters

# Common Monitor Parameters


This document lists optional parameters that all current monitors support.


## Parameters


### `<code>user</code>`


Username used by the monitor to connect to the backend servers. If a server defines
the `<code>monitoruser</code>` parameter, that value will be used instead.


### `<code>password</code>`


Password for the user defined with the `<code>user</code>` parameter. If a server defines
the `<code>monitorpw</code>` parameter, that value will be used instead.


### `<code>monitor_interval</code>`


This is the time the monitor waits between each cycle of monitoring. The default
value of 2000 milliseconds (2 seconds) should be lowered if you want a faster
response to changes in the server states. The value is defined in milliseconds
and the smallest possible value is 100 milliseconds.


The default value of *monitor_interval* was updated from 10000 milliseconds to
2000 milliseconds in MaxScale 2.2.0.



```
monitor_interval=2500
```



### `<code>backend_connect_timeout</code>`


This parameter controls the timeout for connecting to a monitored server. It is
in seconds and the minimum value is 1 second. The default value for this
parameter is 3 seconds.



```
backend_connect_timeout=6
```



### `<code>backend_write_timeout</code>`


This parameter controls the timeout for writing to a monitored server. It is in
seconds and the minimum value is 1 second. The default value for this parameter
is 3 seconds.



```
backend_write_timeout=4
```



### `<code>backend_read_timeout</code>`


This parameter controls the timeout for reading from a monitored server. It is
in seconds and the minimum value is 1 second. The default value for this
parameter is 3 seconds.



```
backend_read_timeout=2
```



### `<code>backend_connect_attempts</code>`


This parameter defines the maximum times a backend connection is attempted every
monitoring loop. The default is 1. Every attempt may take up to
`<code>backend_connect_timeout</code>` seconds to perform. If none of the attempts are
successful, the backend is considered to be unreachable and down.



```
backend_connect_attempts=3
```



### `<code>script</code>`


This command will be executed when a server changes its state. The parameter should be an absolute path to a command or the command should be in the executable path. The user which is used to run MaxScale should have execution rights to the file itself and the directory it resides in.



```
script=/home/user/myscript.sh initiator=$INITIATOR event=$EVENT live_nodes=$NODELIST
```



The following substitutions will be made to the parameter value:


* `<code>$INITIATOR</code>` will be replaced with the IP and port of the server who initiated the event
* `<code>$EVENT</code>` will be replaced with the name of the event
* `<code>$LIST</code>` will be replaced with a list of server IPs and ports
* `<code>$NODELIST</code>` will be replaced with a list of server IPs and ports that are running
* `<code>$SLAVELIST</code>` will be replaced with a list of server IPs and ports that are slaves
* `<code>$MASTERLIST</code>` will be replaced with a list of server IPs and ports that are masters
* `<code>$SYNCEDLIST</code>` will be replaced with a list of server IPs and ports that are synced Galera nodes
* `<code>$PARENT</code>` will be replaced with the IP and port of the parent node of the server who initiated
 the event. For master-slave setups, this will be the master if the initiating server is a slave.
* `<code>$CHILDREN</code>` will be replaced with the IPs and ports of the child nodes of the server who initiated
 the event. For master-slave setups, this will be a list of slave servers if the initiating server is a master.


The expanded variable value can be an empty string if no servers match the
variable's requirements. For example, if no masters are available `<code>$MASTERLIST</code>`
will expand into an empty string.


For example, the previous example will be executed as:



```
/home/user/myscript.sh initiator=[192.168.0.10]:3306 event=master_down live_nodes=[192.168.0.201]:3306,[192.168.0.121]:3306
```



Any output by the executed script will be logged into the MaxScale log. Each
outputted line will be logged as a separate log message.


The log level on which the messages are logged depends on the format of the
messages. If the first word in the output line is one of `<code>alert:</code>`, `<code>error:</code>`,
`<code>warning:</code>`, `<code>notice:</code>`, `<code>info:</code>` or `<code>debug:</code>`, the message will be logged on the
corresponding level. If the message is not prefixed with one of the keywords,
the message will be logged on the notice level. Whitespace before, after or
inbetween the keyword and the colon is ignored and the matching is
case-insensitive.


### `<code>script_timeout</code>`


The timeout for the executed script in seconds. The default value is 90
seconds.


If the script execution exceeds the configured timeout, it is stopped by sending
a SIGTERM signal to it. If the process does not stop, a SIGKILL signal will be
sent to it once the execution time is greater than twice the configured timeout.


### `<code>events</code>`


A list of event names which cause the script to be executed. If this option is not defined, all events cause the script to be executed. The list must contain a comma separated list of event names.



```
events=master_down,slave_down
```



## Script events


Here is a table of all possible event types and their descriptions that the monitors can be called with.


| Event Name | Description |
| --- | --- |
| Event Name | Description |
| master_down | A Master server has gone down |
| master_up | A Master server has come up |
| slave_down | A Slave server has gone down |
| slave_up | A Slave server has come up |
| server_down | A server with no assigned role has gone down |
| server_up | A server with no assigned role has come up |
| ndb_down | A MySQL Cluster node has gone down |
| ndb_up | A MySQL Cluster node has come up |
| lost_master | A server lost Master status |
| lost_slave | A server lost Slave status |
| lost_ndb | A MySQL Cluster node lost node membership |
| new_master | A new Master was detected |
| new_slave | A new Slave was detected |
| new_ndb | A new MySQL Cluster node was found |


### `<code>journal_max_age</code>`


The maximum journal file age in seconds. The default value is 28800 seconds.


When the monitor starts, it reads any stored journal files. If the journal file
is older than the value of *journal_max_age*, it will be removed and the monitor
starts with no prior knowledge of the servers.


## Monitor Crash Safety


Starting with MaxScale 2.2.0, the monitor modules keep an on-disk journal of the
latest server states. This change makes the monitors crash-safe when options
that introduce states are used. It also allows the monitors to retain stateful
information when MaxScale is restarted.


For MySQL monitor, options that introduce states into the monitoring process are
the `<code>detect_stale_master</code>` and `<code>detect_stale_slave</code>` options, both of which are
enabled by default. Galeramon has the `<code>disable_master_failback</code>` parameter which
introduces a state.


The default location for the server state journal is in
`<code>/var/lib/maxscale/<monitor name>/monitor.dat</code>` where `<code><monitor name></code>` is the
name of the monitor section in the configuration file. If MaxScale crashes or is
shut down in an uncontrolled fashion, the journal will be read when MaxScale is
started. To skip the recovery process, manually delete the journal file before
starting MaxScale.
