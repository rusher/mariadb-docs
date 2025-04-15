
# RabbitMQ Consumer Client

# RabbitMQ Consumer Client


## Overview


This utility tool is used to read messages from a RabbitMQ broker sent by the [RabbitMQ Filter](mariadb-maxscale-20-rabbitmq-filter.md) and forward these messages into an SQL database as queries.


## Command Line Arguments


The **RabbitMQ Consumer Client** only has one command line argument.


| Command | Argument |
| --- | --- |
| Command | Argument |
| -c | Path to the folder containing the configuration file |


## Installation


To install the RabbitMQ Consumer Client you ca either use the provided packages or you can compile it from source code. The source code is included as a part of the MariaDB MaxScale source code and can be found in the `<code>rabbitmq_consumer</code>` folder.


## Building from source


This program requires the librabbitmq and libmysqlclient libraries.


* [librabbitmq-c](https://github.com/alanxz/rabbitmq-c)
* [MariaDB Client Library for C 2.0 Series](../../../connectors/mariadb-connector-cpp/mariadb-connector-cpp-sample-application.md)


Building with CMake:



```
cmake .
```



Variables to pass for CMake:


Path to headers -DCMAKE_INCLUDE_PATH=<path to="" headers="">
Path to libraries -DCMAKE_LIBRARY_PATH=<path to="" libraries="">
Install prefix -DCMAKE_INSTALL_PREFIX=<prefix>


Separate multiple folders with colons, for example:



```
path1:path2:path3
```



After running CMake run `<code>make</code>` to build the binaries and `<code>make package</code>` to build RPMs.


To build without CMake, use the provided makefile and update the
include and library directories 'in buildvars.inc'


## Configuration


The consumer client requires that the `<code>consumer.cnf</code>` configuration file is either be present in the `<code>etc</code>` folder of the installation directory or in the folder specified by the `<code>-c</code>` argument.


The source broker, the destination database and the message log file can be configured into the separate `<code>consumer.cnf</code>` file.


| Option | Description |
| --- | --- |
| Option | Description |
| hostname | Hostname of the RabbitMQ server |
| port | Port of the RabbitMQ server |
| vhost | Virtual host location of the RabbitMQ server |
| user | Username for the RabbitMQ server |
| passwd | Password for the RabbitMQ server |
| queue | Queue to consume from |
| dbserver | Hostname of the SQL server |
| dbport | Port of the SQL server |
| dbname | Name of the SQL database to use |
| dbuser | Database username |
| dbpasswd | Database password |
| logfile | Message log filename |
