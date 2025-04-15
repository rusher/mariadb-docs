
# ColumnStore System Operations

 
1. [System status "System status"](#system-status) 

  1. [Viewing system status "Viewing system status"](#viewing-system-status)
  1. [Simple external monitoring script "Simple external monitoring script"](#simple-external-monitoring-script)
  1. [Viewing process status "Viewing process status"](#viewing-process-status)
1. [System operations "System operations"](#system-operations) 

  1. [Stopping the system "Stopping the system"](#stopping-the-system)
  1. [Starting the system or modules "Starting the system or modules"](#starting-the-system-or-modules)
  1. [Restarting the system "Restarting the system"](#restarting-the-system)
  1. [Shutting down the system "Shutting down the system"](#shutting-down-the-system)
  1. [Disabling system modules "Disabling system modules"](#disabling-system-modules)
  1. [Enabling System Modules "Enabling System Modules"](#enabling-system-modules)
  1. [Switch Parent OAM Module "Switch Parent OAM Module"](#switch-parent-oam-module)
1. [System configuraiton "System configuraiton"](#system-configuraiton) 

  1. [Viewing network configuration "Viewing network configuration"](#viewing-network-configuration)
  1. [Viewing module configuration "Viewing module configuration"](#viewing-module-configuration)





## System status


### Viewing system status


The system status shows the status of the system and all equipped servers. 
To view the system status, use the *getSystemStatus* command in [mcsadmin](columnstore-administrative-console.md), or simply use [mcsadmin](columnstore-administrative-console.md) *getSystemStatus* from the operating system prompt.


Example:


```
# mcsadmin getSystemStatus
getsystemstatus   Sat Jun 11 01:01:22 2016

System columnstore-1

System and Module statuses

Component     Status                       Last Status Change
------------  --------------------------   ------------------------
System        ACTIVE                       Fri Jun 10 01:50:46 2016

Module pm1    ACTIVE                       Fri Jun 10 01:50:43 2016
```

The table below shows the available system and server statuses.



| Status | Definition |
| --- | --- |
| Status | Definition |
| Active | The system, server, or Network Interface Card (NIC) is available to process database requests |
| Auto Disabled | Disabled as a result of a server failure. |
| Auto Init | Auto initialization mode during a fault recovery. |
| Auto Offline | The system or server is offline due to a fault. |
| Busy_Init | The module/system is performing an initialization task at startup time before going to the ACTIVE state. |
| Degraded | The server is active, but the performance is degraded. A server is degraded when a NIC is not working. |
| Down | Communication failure. |
| Failed | A stop/start/restart request for the system or a server failed. |
| Initial | Initial state after a system reboot or install and before any action is taken. |
| Man Disabled | Disabled as a result of executing the altersystem-disableModule command. |
| Man Init | Manual initialization mode during a start or restart command. |
| Man Offline | The system or server was taken offline with the stop or shutdown command. |
| Up | Successfully communicating. |



When all servers are active, then the system status is active. If one or more servers are Man Offline and the others are active, the system is Man Offline. All equipped servers must be active before the system is shown as active.


### Simple external monitoring script


The following starter / reference shell script will wrap an mcsadmin call and produce output / return codes matching the nagios plugin specification. Most monitoring tools can easily integrate this and it typically requires configuring an agent on a columnstore node to periodically invoke this to determine current status.


```
#!/bin/bash
MCS_DIR="/usr/local/mariadb/columnstore"

# capture getSystemStatus and remove first 9 lines and blank lines to just have status table contents
STATUS=$($MCS_DIR/bin/mcsadmin getSystemStatus | tail -n +9  | sed '/^$/d' )
# grab system status line
SYSTEM_STATUS=$(echo "$STATUS" | grep 'System' | awk '{ printf $2; }')
# combine module status lines
MODULE_STATUS=$(echo "$STATUS" | grep 'Module' | awk '{ printf $2 ":" $3 " "; }')

# if system status is ACTIVE, then all good otherwise consider critical failure
if [ "$SYSTEM_STATUS" == "ACTIVE" ]
then
  echo "OK - system: $SYSTEM_STATUS, modules: $MODULE_STATUS"
  exit 0
else
  echo "CRITICAL - system: $SYSTEM_STATUS, modules: $MODULE_STATUS"
  exit 2
fi
```

### Viewing process status


To view the process status, use the *getProcessStatus* command in [mcsadmin](columnstore-administrative-console.md), or simply use [mcsadmin](columnstore-administrative-console.md) *getProcessStatus* from the operating system prompt.
The table below shows the available system and server statuses.


Example:


```
[myusr@srv1 ~]# mcsadmin getProcessStatus
getprocessstatus   Sat Jun 11 00:59:09 2016

MariaDB Columnstore Process statuses

Process             Module    Status            Last Status Change        Process ID
------------------  ------    ---------------   ------------------------  ----------
ProcessMonitor      pm1       ACTIVE            Fri Jun 10 01:50:04 2016        2487
ProcessManager      pm1       ACTIVE            Fri Jun 10 01:50:10 2016        2673
SNMPTrapDaemon      pm1       ACTIVE            Fri Jun 10 01:50:16 2016        3534
DBRMControllerNode  pm1       ACTIVE            Fri Jun 10 01:50:20 2016        3585
ServerMonitor       pm1       ACTIVE            Fri Jun 10 01:50:22 2016        3625
DBRMWorkerNode      pm1       ACTIVE            Fri Jun 10 01:50:22 2016        3665
DecomSvr            pm1       ACTIVE            Fri Jun 10 01:50:26 2016        3742
PrimProc            pm1       ACTIVE            Fri Jun 10 01:50:28 2016        3770
ExeMgr              pm1       ACTIVE            Fri Jun 10 01:50:32 2016        3844
WriteEngineServer   pm1       ACTIVE            Fri Jun 10 01:50:36 2016        3934
DDLProc             pm1       ACTIVE            Fri Jun 10 01:50:40 2016        3991
DMLProc             pm1       ACTIVE            Fri Jun 10 01:50:45 2016        4058
mysqld              pm1       ACTIVE            Fri Jun 10 01:50:22 2016        2975
```

The table below shows the supported process states.



| Status | Definition |
| --- | --- |
| Status | Definition |
| Active | The process is fully functional. |
| Auto Init | Auto initialization mode during a fault recovery |
| Auto Offline | The process is offline due to a fault. |
| Busy Init | The process is performing an initialization task at startup time before going to the ACTIVE state. |
| Failed | A stop/start/restart request for a process failed. |
| Hot Standby | The process is functional in a standby/ready state in case a failover occurs. |
| Initial | State after a system reboot or install and before any action is taken |
| Man Init | Manual initialization mode during a start or restart command |
| Man Offline | The process was taken offline with the stop or shutdown command. |
| Standby Init | Manual initialization mode during a start or restart command of a Hot Standby process. |



## System operations


### Stopping the system


To stop the system, use the *stopSystem* command in [mcsadmin](columnstore-administrative-console.md), or simply use [mcsadmin](columnstore-administrative-console.md) *stopSystem* from the operating system prompt.


Stopping the system stops the storage engine database processes. The process that supports the Management Console and System Alarms remains active.


### Starting the system or modules


To start the system, use the *startSystem* command in [mcsadmin](columnstore-administrative-console.md), or simply use [mcsadmin](columnstore-administrative-console.md) *startSystem* from the operating system prompt


### Restarting the system


To restart the system, use the *restartSystem* command in [mcsadmin](columnstore-administrative-console.md), or simply use [mcsadmin](columnstore-administrative-console.md) *restartSystem* from the operating system prompt


### Shutting down the system


To shut down the system completely including storage engine database processes as well as the process that supports management console and system alarms, use the *shutdownSystem* command in [mcsadmin](columnstore-administrative-console.md), or simply use [mcsadmin](columnstore-administrative-console.md) *shutdownSystem* from the operating system prompt


### Disabling system modules


A System Module can be disabled when the system is ACTIVE or OFFLINE. To disable a module, use the *alterSystem-disableModule module_id* command in [mcsadmin](columnstore-administrative-console.md), or simply use [mcsadmin](columnstore-administrative-console.md) *alterSystem-disableModule module_id* from the operating system prompt.


Example:


```
mcsadmin alterSystem-disablemodule PM2, PM3
```

The modules PM2 and PM3 will be stopped and disabled.


_Note_: Disabling a module may result in data loss if the data is local to the [PM](../../columnstore-architecture/columnstore-performance-module.md). If the data is SAN mounted, the dbroots would need to be moved to other PMs. Please see “Moving DBRoots” of this guide for more information on moving DBRoots.


### Enabling System Modules


To enable a module, use the *alterSystem-enableModule module_id* command in [mcsadmin](columnstore-administrative-console.md), or simply use [mcsadmin](columnstore-administrative-console.md) *alterSystem-enableModule module_id* from the operating system prompt.


Example:


```
mcsadmin alterSystem-enablemodule PM2, PM3
```

The modules PM2 and PM3 will be enabled and started.


### Switch Parent OAM Module


Parent OAM Module is the Performance Module that monitors the overall system including all the [UM](../../columnstore-architecture/columnstore-user-module.md) and [PM](../../columnstore-architecture/columnstore-performance-module.md) nodes and their status, as well as handles PM node failover. In a running system with more than 1 PM node there will be 2 Parent OAM Modules - an Active Parent and a Standby Parent.


To switch a module to the Standby Parent, use *switchParentOAMModule* in [mcsadmin](columnstore-administrative-console.md), or simply use [mcsadmin](columnstore-administrative-console.md) *switchParentOAMModule* from the operating system prompt.
The Standby Parent OAM Module will become active.


To switch a module to a specific module:
use *switchParentOAMModule module_id* on [mcsadmin](columnstore-administrative-console.md), or simply use [mcsadmin](columnstore-administrative-console.md) *switchParentOAMModule module_id* from the operating system prompt.


Example:


```
switchParentOAMModule pm3
```

The Performance-Module 3 will become the active Parent OAM Module


## System configuraiton


### Viewing network configuration


To view the network configuration of all nodes and their statuses use *getSystemNetworkConfig* on [mcsadmin](columnstore-administrative-console.md), or simply use [mcsadmin](columnstore-administrative-console.md) *getSystemNetworkConfig* from the operating system prompt.


Example:


```
[myusr@srv1 ~]mcsadmin getSystemNetworkConfig

getsystemnetworkconfig   Sat Jun 11 01:34:55 2016
System Network Configuration
Module Name    Module Description            NIC ID    Host Name     IP Address          Status        
-----------    -------------------------     ------    ---------     ---------------     ------------  
pm1            Performance Module #1            1      localhost     127.0.0.1           UP
```

### Viewing module configuration


To view the module configuration of all nodes and their statuses use *getModuleConfig* on [mcsadmin](columnstore-administrative-console.md), or simply use [mcsadmin](columnstore-administrative-console.md) *getModuleConfig* from the operating system prompt.


```
[myusr@srv1 ~]mcsadmin getModuleConfig
getmoduleconfig   Sat Jun 11 01:51:37 2016
Module Name Configuration

Module 'um1' Configuration information
ModuleType = um
ModuleDesc = User Module #1
ModuleIPAdd NIC ID 1 = 10.100.7.80
ModuleHostName NIC ID 1 = srvhst2
ModuleIPAdd NIC ID 2 = 10.100.107.81
ModuleHostName NIC ID 2 = srvhst2b

Module 'pm1' Configuration information
ModuleType = pm
ModuleDesc = Performance Module #1
ModuleIPAdd NIC ID 1 = 10.100.7.10
ModuleHostName NIC ID 1 = srvhst1
DBRootIDs assigned  = 1
```
