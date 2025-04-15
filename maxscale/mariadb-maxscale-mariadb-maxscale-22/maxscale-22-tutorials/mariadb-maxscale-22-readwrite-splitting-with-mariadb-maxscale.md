
# Read/Write Splitting with MariaDB MaxScale

# Read/Write Splitting with MariaDB MaxScale


The object of this tutorial is to have a system that appears to the client as a
single database. MariaDB MaxScale will split the statements such that write
statements will be sent to the current master server in the replication cluster
and read statements will be balanced across the rest of the servers.


## Setting up MariaDB MaxScale


The first part of this tutorial is covered in [MariaDB MaxScale Tutorial](mariadb-maxscale-22-setting-up-mariadb-maxscale.md).
Please read it and follow the instructions for setting up MariaDB MaxScale with
the type of cluster you want to use.


Once you have MariaDB MaxScale installed and the database users created, we can
create the configuration file for MariaDB MaxScale.


## Creating Your MariaDB MaxScale Configuration


MariaDB MaxScale reads its configuration from `<code>/etc/maxscale.cnf</code>`. A template
configuration is provided with the MaxScale installation.


A global `<code>[maxscale]</code>` section is included in every MariaDB MaxScale
configuration file; this is used to set the values of various global parameters,
perhaps the most important of these is the number of threads that MariaDB
MaxScale will use to handle client requests. To automatically configure the
thread count, use the `<code>threads=auto</code>` parameter.



```
[maxscale]
threads=auto
```



## Configuring Servers


Read the [Configuring Servers](../../mariadb-maxscale-21-06/README.md) mini-tutorial to see how
the servers are configured.


## Configuring the Monitor


The next step is the configuration of the monitor. This depends on the type of
cluster you use with MaxScale.


For master-slave clusters read the
[Configuring MariaDB Monitor](../../mariadb-maxscale-21-06/README.md)
tutorial. If you are using a Galera cluster, read the
[Configuring Galera Monitor](../../mariadb-maxscale-21-06/README.md)
tutorial instead.


## Configuring the Service


After configuring the servers and the monitor, we create a Read/Write Splitter
service configuration. Create the following section in your configuration
file. The section name is the names of the service and should be meaningful to
the administrator. For this tutorial, we use the `<code>Splitter-Service</code>` name for our
service.



```
[Splitter-Service]
type=service
router=readwritesplit
servers=dbserv1, dbserv2, dbserv3
user=maxscale
password=maxscale_pw
```



The router module we use for this service is `<code>readwritesplit</code>`.


The services must be provided with the list of servers where queries
will be routed to. The server names given here are the names of server sections
in the configuration file (to be defined later) and not the physical hostnames
or addresses of the servers.


The final part of the service configuration is the `<code>user</code>` and `<code>password</code>`
parameters that define the credentials that the service will use to populate the
user authentication data. These users were created at the start of the
[MaxScale Tutorial](mariadb-maxscale-22-setting-up-mariadb-maxscale.md).


**Note:** For increased security [encrypt your passwords in the configuration file](../../mariadb-maxscale-21-06/README.md).


## Configuring the Listener


In order to allow network connections to the services, we must associate network
ports with the services. This is done by creating a separate listener section in
the configuration file. A service may have multiple listeners but for this
tutorial we will only need one.



```
[Splitter-Listener]
type=listener
service=Splitter-Service
protocol=MariaDBClient
port=3306
```



The `<code>service</code>` parameter tells to which service the listener connects to. For the
`<code>Splitter-Listener</code>` we set it to `<code>Splitter-Service</code>`.


A listener must also define the protocol module it will use for the incoming
network protocol (must be the `<code>MariaDBClient</code>` protocol for all database
listeners) as well as the the network port to listen on.


Additionally, the `<code>address</code>` parameter may be given if the listener is required
to bind to a particular network interface when the host machine has multiple
network interfaces. The default behavior is to listen on all network interfaces
(the IPv6 address `<code>::</code>`).


## Configuring the Administrative Interface


The MaxAdmin configuration is described in the
[Configuring MaxAdmin](../../mariadb-maxscale-21-06/README.md) document.


## Starting MariaDB MaxScale


Upon completion of the configuration process MariaDB MaxScale is ready to be
started for the first time. For newer systems that use systemd, use the *systemctl* command.



```
sudo systemctl start maxscale
```



For older SysV systems, use the *service* command.



```
sudo service maxscale start
```



If MaxScale fails to start, check the error log in
`<code>/var/log/maxscale/maxscale.log</code>` to see if any errors are detected in the
configuration file. The `<code>maxadmin</code>` command may be used to confirm that MariaDB
MaxScale is running and the services, listeners and servers have been correctly
configured.



```
% sudo maxadmin list services

Services.
--------------------------+-------------------+--------+----------------+-------------------
Service Name              | Router Module     | #Users | Total Sessions | Backend databases
--------------------------+-------------------+--------+----------------+-------------------
Splitter-Service          | readwritesplit    |      1 |              1 | dbserv1, dbserv2, dbserv3
CLI                       | cli               |      2 |              3 |
--------------------------+-------------------+--------+----------------+-------------------

% sudo maxadmin list servers

Servers.
-------------------+-----------------+-------+-------------+--------------------
Server             | Address         | Port  | Connections | Status
-------------------+-----------------+-------+-------------+--------------------
dbserv1            | 192.168.2.1     |  3306 |           0 | Running, Slave
dbserv2            | 192.168.2.2     |  3306 |           0 | Running, Master
dbserv3            | 192.168.2.3     |  3306 |           0 | Running, Slave
-------------------+-----------------+-------+-------------+--------------------

% sudo maxadmin list listeners

Listeners.
---------------------+---------------------+--------------------+-----------------+-------+--------
Name                 | Service Name        | Protocol Module    | Address         | Port  | State
---------------------+---------------------+--------------------+-----------------+-------+--------
Splitter-Listener    | Splitter-Service    | MariaDBClient      | *               |  3306 | Running
CLI-Listener         | CLI                 | maxscaled          | default         |     0 | Running
---------------------+---------------------+--------------------+-----------------+-------+--------
```



MariaDB MaxScale is now ready to start accepting client connections and routing
them to the cluster. More options may be found in the
[Configuration Guide](../maxscale-22-getting-started/mariadb-maxscale-22-mariadb-maxscale-configuration-usage-scenarios.md)
and in the [readwritesplit module documentation](../maxscale-22-routers/mariadb-maxscale-22-readwritesplit.md).


More detail on the use of `<code>maxadmin</code>` can be found in the
[MaxAdmin](../maxscale-22-reference/mariadb-maxscale-22-maxadmin-admin-interface.md) document.
