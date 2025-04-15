
# MaxScale 21.06 Common Monitor Parameters

# Common Monitor Parameters


This document settings supported by all monitors. These should be defined
in the monitor section of the configuration file.




* [Common Monitor Parameters](#common-monitor-parameters)

  * [Parameters](#parameters)

    * [module](#module)
    * [user](#user)
    * [password](#password)
    * [servers](#servers)
    * [monitor_interval](#monitor_interval)
    * [backend_connect_timeout](#backend_connect_timeout)
    * [backend_write_timeout](#backend_write_timeout)
    * [backend_read_timeout](#backend_read_timeout)
    * [backend_connect_attempts](#backend_connect_attempts)
    * [disk_space_threshold](#disk_space_threshold)
    * [disk_space_check_interval](#disk_space_check_interval)
    * [script](#script)
    * [script_timeout](#script_timeout)
    * [events](#events)
    * [journal_max_age](#journal_max_age)
  * [Monitor Crash Safety](#monitor-crash-safety)
  * [Script example](#script-example)




## Parameters


### `<code>module</code>`


* Type: string
* Mandatory: Yes
* Dynamic: No


The monitor module this monitor should use. Typically `<code>mariadbmon</code>` or
`<code>galeramon</code>`.


### `<code>user</code>`


* Type: string
* Mandatory: Yes
* Dynamic: Yes


Username used by the monitor to connect to the backend servers. If a server defines
the `<code>monitoruser</code>` parameter, that value will be used instead.


### `<code>password</code>`


* Type: string
* Mandatory: Yes
* Dynamic: Yes


Password for the user defined with the `<code>user</code>` parameter. If a server defines
the `<code>monitorpw</code>` parameter, that value will be used instead.


**Note:** In older versions of MaxScale this parameter was called `<code>passwd</code>`. The
 use of `<code>passwd</code>` was deprecated in MaxScale 2.3.0.


### `<code>servers</code>`


* Type: string
* Mandatory: Yes
* Dynamic: Yes


A comma-separated list of servers the monitor should monitor.



```
servers=MyServer1,MyServer2
```



### `<code>monitor_interval</code>`


* Type: [duration](../mariadb-maxscale-21-06-getting-started/mariadb-maxscale-2106-maxscale-2106-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `<code>2s</code>`


Defines how often the monitor updates the status of the servers. Choose a lower
value if servers should be queried more often. The smallest possible value is
100 milliseconds. If querying the servers takes longer than `<code>monitor_interval</code>`,
the effective update rate is reduced.



```
monitor_interval=2s
```



The interval is specified as documented
[here](../mariadb-maxscale-21-06-getting-started/mariadb-maxscale-2106-maxscale-2106-mariadb-maxscale-configuration-guide.md). If no explicit unit
is provided, the value is interpreted as milliseconds in MaxScale 2.4. In subsequent
versions a value without a unit may be rejected.


### `<code>backend_connect_timeout</code>`


* Type: [duration](../mariadb-maxscale-21-06-getting-started/mariadb-maxscale-2106-maxscale-2106-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `<code>3s</code>`


This parameter controls the timeout for connecting to a monitored server.
The interval is specified as documented
[here](../mariadb-maxscale-21-06-getting-started/mariadb-maxscale-2106-maxscale-2106-mariadb-maxscale-configuration-guide.md). If no explicit unit
is provided, the value is interpreted as seconds in MaxScale 2.4. In subsequent
versions a value without a unit may be rejected. Note that since the granularity
of the timeout is seconds, a timeout specified in milliseconds will be rejected,
even if the duration is longer than a second. The minimum value is 1 second.



```
backend_connect_timeout=3s
```



### `<code>backend_write_timeout</code>`


* Type: [duration](../mariadb-maxscale-21-06-getting-started/mariadb-maxscale-2106-maxscale-2106-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `<code>3s</code>`


This parameter controls the timeout for writing to a monitored server.
The timeout is specified as documented
[here](../mariadb-maxscale-21-06-getting-started/mariadb-maxscale-2106-maxscale-2106-mariadb-maxscale-configuration-guide.md). If no explicit unit
is provided, the value is interpreted as seconds in MaxScale 2.4. In subsequent
versions a value without a unit may be rejected. Note that since the granularity
of the timeout is seconds, a timeout specified in milliseconds will be rejected,
even if the duration is longer than a second. The minimum value is 1 seconds.



```
backend_write_timeout=3s
```



### `<code>backend_read_timeout</code>`


* Type: [duration](../mariadb-maxscale-21-06-getting-started/mariadb-maxscale-2106-maxscale-2106-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `<code>3s</code>`


This parameter controls the timeout for reading from a monitored server.
The timeout is specified as documented
[here](../mariadb-maxscale-21-06-getting-started/mariadb-maxscale-2106-maxscale-2106-mariadb-maxscale-configuration-guide.md). If no explicit unit
is provided, the value is interpreted as seconds in MaxScale 2.4. In subsequent
versions a value without a unit may be rejected. Note that since the granularity
of the timeout is seconds, a timeout specified in milliseconds will be rejected,
even if the duration is longer than a second. The minimum value is 1 second.



```
backend_read_timeout=3s
```



### `<code>backend_connect_attempts</code>`


* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `<code>1</code>`


This parameter defines the maximum times a backend connection is attempted every
monitoring loop. Every attempt may take up to `<code>backend_connect_timeout</code>` seconds
to perform. If none of the attempts are successful, the backend is considered to
be unreachable and down.



```
backend_connect_attempts=1
```



### `<code>disk_space_threshold</code>`


* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None


This parameter duplicates the `<code>disk_space_threshold</code>`
[server parameter](../mariadb-maxscale-21-06-getting-started/mariadb-maxscale-2106-maxscale-2106-mariadb-maxscale-configuration-guide.md).
If the parameter has *not* been specified for a server, then the one specified
for the monitor is applied.


**NOTE**: Since MariaDB 10.4.7, MariaDB 10.3.17 and MariaDB 10.2.26, the
information will be available *only* if the monitor user has the `<code>FILE</code>`
privilege.


That is, if the disk configuration is the same on all servers monitored by
the monitor, it is sufficient (and more convenient) to specify the disk
space threshold in the monitor section, but if the disk configuration is
different on all or some servers, then the disk space threshold can be
specified individually for each server.


For example, suppose `<code>server1</code>`, `<code>server2</code>` and `<code>server3</code>` are identical
in all respects. In that case we can specify `<code>disk_space_threshold</code>`
in the monitor.



```
[server1]
type=server
...

[server2]
type=server
...

[server3]
type=server
...

[monitor]
type=monitor
servers=server1,server2,server3
disk_space_threshold=/data:80
...
```



However, if the servers are heterogeneous with the disk used for the
data directory mounted on different paths, then the disk space threshold
must be specified separately for each server.



```
[server1]
type=server
disk_space_threshold=/data:80
...

[server2]
type=server
disk_space_threshold=/Data:80
...

[server3]
type=server
disk_space_threshold=/DBData:80
...

[monitor]
type=monitor
servers=server1,server2,server3
...
```



If *most* of the servers have the data directory disk mounted on
the same path, then the disk space threshold can be specified on
the monitor and separately on the server with a different setup.



```
[server1]
type=server
disk_space_threshold=/DbData:80
...

[server2]
type=server
...

[server3]
type=server
...

[monitor]
type=monitor
servers=server1,server2,server3
disk_space_threshold=/data:80
...
```



Above, `<code>server1</code>` has the disk used for the data directory mounted
at `<code>/DbData</code>` while both `<code>server2</code>` and `<code>server3</code>` have it mounted on
`<code>/data</code>` and thus the setting in the monitor covers them both.


### `<code>disk_space_check_interval</code>`


* Type: [duration](../mariadb-maxscale-21-06-getting-started/mariadb-maxscale-2106-maxscale-2106-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `<code>0s</code>`


With this parameter it can be specified the minimum amount of time
between disk space checks. The interval is specified as documented
[here](../mariadb-maxscale-21-06-getting-started/mariadb-maxscale-2106-maxscale-2106-mariadb-maxscale-configuration-guide.md). If no explicit unit
is provided, the value is interpreted as milliseconds in MaxScale 2.4. In subsequent
versions a value without a unit may be rejected.
The default value is 0, which means that by default the disk space
will not be checked.


Note that as the checking is made as part of the regular monitor interval
cycle, the disk space check interval is affected by the value of
`<code>monitor_interval</code>`. In particular, even if the value of
`<code>disk_space_check_interval</code>` is smaller than that of `<code>monitor_interval</code>`,
the checking will still take place at `<code>monitor_interval</code>` intervals.


### `<code>script</code>`


* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None


This command will be executed on a server state change. The parameter should
be an absolute path to a command or the command should be in the executable
path. The user running MaxScale should have execution rights to the file itself
and the directory it resides in. The script may have placeholders which
MaxScale will substitute with useful information when launching the script.


The placeholders and their substitution results are:


* `<code>$INITIATOR</code>` -> IP and port of the server which initiated the event
* `<code>$EVENT</code>` -> event description, e.g. "server_up"
* `<code>$LIST</code>` -> list of IPs and ports of all servers
* `<code>$NODELIST</code>` -> list of IPs and ports of all running servers
* `<code>$SLAVELIST</code>` -> list of IPs and ports of all slave servers
* `<code>$MASTERLIST</code>` -> list of IPs and ports of all master servers
* `<code>$SYNCEDLIST</code>` -> list of IPs and ports of all synced Galera nodes
* `<code>$PARENT</code>` -> IP and port of the parent of the server which initiated the event.
For master-slave setups, this will be the master if the initiating server is a
slave.
* `<code>$CHILDREN</code>` -> list of IPs and ports of the child nodes of the server who
initiated the event. For master-slave setups, this will be a list of slave
servers if the initiating server is a master.


The expanded variable value can be an empty string if no servers match the
variable's requirements. For example, if no masters are available `<code>$MASTERLIST</code>`
will expand into an empty string. The list-type substitutions will only contain
servers monitored by the current monitor.



```
script=/home/user/myscript.sh initiator=$INITIATOR event=$EVENT live_nodes=$NODELIST
```



The above script could be executed as:



```
/home/user/myscript.sh initiator=[192.168.0.10]:3306 event=master_down live_nodes=[192.168.0.201]:3306,[192.168.0.121]:3306
```



See section [Script example](#script-example) below for an example script.


Any output by the executed script will be logged into the MaxScale log. Each
outputted line will be logged as a separate log message.


The log level on which the messages are logged depends on the format of the
messages. If the first word in the output line is one of `<code>alert:</code>`, `<code>error:</code>`,
`<code>warning:</code>`, `<code>notice:</code>`, `<code>info:</code>` or `<code>debug:</code>`, the message will be logged on the
corresponding level. If the message is not prefixed with one of the keywords,
the message will be logged on the notice level. Whitespace before, after or
between the keyword and the colon is ignored and the matching is
case-insensitive.


Currently, the script must not execute any of the following MaxCtrl
calls as they cause a deadlock:


* `<code>alter monitor</code>` to the monitor executing the script
* `<code>stop monitor</code>` to the monitor executing the script
* `<code>call command</code>` to a MariaDB-Monitor that is executing the script


### `<code>script_timeout</code>`


* Type: [duration](../mariadb-maxscale-21-06-getting-started/mariadb-maxscale-2106-maxscale-2106-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `<code>90s</code>`


The timeout for the executed script. The interval is specified as documented
[here](../mariadb-maxscale-21-06-getting-started/mariadb-maxscale-2106-maxscale-2106-mariadb-maxscale-configuration-guide.md). If no explicit unit
is provided, the value is interpreted as seconds in MaxScale 2.4. In subsequent
versions a value without a unit may be rejected. Note that since the granularity
of the timeout is seconds, a timeout specified in milliseconds will be rejected,
even if the duration is longer than a second.


If the script execution exceeds the configured timeout, it is stopped by sending
a SIGTERM signal to it. If the process does not stop, a SIGKILL signal will be
sent to it once the execution time is greater than twice the configured timeout.


### `<code>events</code>`


* Type: enum
* Mandatory: No
* Dynamic: Yes
* Values: `<code>master_down</code>`, `<code>master_up</code>`, `<code>slave_down</code>`, `<code>slave_up</code>`, `<code>server_down</code>`, `<code>server_up</code>`, `<code>lost_master</code>`, `<code>lost_slave</code>`, `<code>new_master</code>`, `<code>new_slave</code>`
* Default: All events


A list of event names which cause the script to be executed. If this option is
not defined, all events cause the script to be executed. The list must contain a
comma separated list of event names.



```
events=master_down,slave_down
```



The following table contains all the possible event types and their
descriptions.


| Event Name | Description |
| --- | --- |
| Event Name | Description |
| master_down | A Master server has gone down |
| master_up | A Master server has come up |
| slave_down | A Slave server has gone down |
| slave_up | A Slave server has come up |
| server_down | A server with no assigned role has gone down |
| server_up | A server with no assigned role has come up |
| lost_master | A server lost Master status |
| lost_slave | A server lost Slave status |
| new_master | A new Master was detected |
| new_slave | A new Slave was detected |


### `<code>journal_max_age</code>`


* Type: [duration](../mariadb-maxscale-21-06-getting-started/mariadb-maxscale-2106-maxscale-2106-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `<code>28800s</code>`


The maximum journal file age. The interval is specified as documented
[here](../mariadb-maxscale-21-06-getting-started/mariadb-maxscale-2106-maxscale-2106-mariadb-maxscale-configuration-guide.md). If no explicit unit
is provided, the value is interpreted as seconds in MaxScale 2.4. In subsequent
versions a value without a unit may be rejected. Note that since the granularity
of the max age is seconds, a max age specified in milliseconds will be rejected,
even if the duration is longer than a second.


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


## Script example


Below is an example monitor configuration which launches a script with all
supported substitutions. The example script reads the results and prints it to
file and sends it as email.



```
[MyMonitor]
type=monitor
module=mariadbmon
servers=C1N1,C1N2,C1N3
user=maxscale
password=password
monitor_interval=10000
script=/path/to/maxscale_monitor_alert_script.sh --initiator=$INITIATOR --parent=$PARENT --children=$CHILDREN --event=$EVENT --node_list=$NODELIST --list=$LIST --master_list=$MASTERLIST --slave_list=$SLAVELIST --synced_list=$SYNCEDLIST
```



File "maxscale_monitor_alert_script.sh":


|   |   |
| --- | --- |
| 1
 2
 3
 4
 5
 6
 7
 8
 9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57 | #!/usr/bin/env bash

initiator=""
parent=""
children=""
event=""
node_list=""
list=""
master_list=""
slave_list=""
synced_list=""

process_arguments()
{
 while [ "$1" != "" ]; do
 if [[ "$1" =~ ^--initiator=.* ]]; then
 initiator=${1#'--initiator='}
 elif [[ "$1" =~ ^--parent.* ]]; then
 parent=${1#'--parent='}
 elif [[ "$1" =~ ^--children.* ]]; then
 children=${1#'--children='}
 elif [[ "$1" =~ ^--event.* ]]; then
 event=${1#'--event='}
 elif [[ "$1" =~ ^--node_list.* ]]; then
 node_list=${1#'--node_list='}
 elif [[ "$1" =~ ^--list.* ]]; then
 list=${1#'--list='}
 elif [[ "$1" =~ ^--master_list.* ]]; then
 master_list=${1#'--master_list='}
 elif [[ "$1" =~ ^--slave_list.* ]]; then
 slave_list=${1#'--slave_list='}
 elif [[ "$1" =~ ^--synced_list.* ]]; then
 synced_list=${1#'--synced_list='}
 fi
 shift
 done
}

process_arguments $@
read -r -d '' MESSAGE << EOM
A server has changed state. The following information was provided:

Initiator: $initiator
Parent: $parent
Children: $children
Event: $event
Node list: $node_list
List: $list
Master list: $master_list
Slave list: $slave_list
Synced list: $synced_list
EOM

# print message to file

echo "$MESSAGE" > /path/to/script_output.txt
# email the message

echo "$MESSAGE" | mail -s "MaxScale received $event event for initiator $initiator." mariadb_admin@domain.com |
