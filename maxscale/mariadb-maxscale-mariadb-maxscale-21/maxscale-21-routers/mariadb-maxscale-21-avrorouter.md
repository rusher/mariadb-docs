
# Avrorouter

# Avrorouter


The avrorouter is a MariaDB 10.0 binary log to Avro file converter. It consumes
binary logs from a local directory and transforms them into a set of Avro files.
These files can then be queried by clients for various purposes.


This router is intended to be used in tandem with the [Binlog Server](mariadb-maxscale-21-binlogrouter.md).
The Binlog Server can connect to a master server and request binlog records. These
records can then consumed by the avrorouter directly from the binlog cache of
the Binlog Server. This allows MariaDB MaxScale to automatically transform binlog events
on the master to local Avro format files.


![](../../.gitbook/assets/mariadb-corporation/MaxScale/2.1.17/Documentation/Routers/images/Binlog-Avro.png.png)


The avrorouter can also consume binary logs straight from the master. This will
remove the need to configure the Binlog Server but it will increase the disk space
requirement on the master server by at least a factor of two.


The converted Avro files can be requested with the CDC protocol. This protocol
should be used to communicate with the avrorouter and currently it is the only
supported protocol. The clients can request either Avro or JSON format data
streams from a database table.


# Configuration


For information about common service parameters, refer to the
[Configuration Guide](../maxscale-21-getting-started/mariadb-maxscale-21-mariadb-maxscale-configuration-usage-scenarios.md).


## Router Parameters


### `<code>source</code>`


The source for the binary logs. This is an optional parameter.


The value of this parameter should be the name of a Binlog Server service.
The *filestem* and *binlogdir* parameters of this service will be read from
the router_options and they will be used as the source for the binary logs. This
removes the need to manually enter the right *binlogdir* and *filestem* options
for the avrorouter.


Here is an example of two services. The first service (`<code>replication-router</code>`) is
responsible for downloading the binary logs from the master and the second service
(`<code>avro-router</code>`) will convert the binary logs into Avro format files and store them
in `<code>/var/lib/mysql</code>`.



```
[replication-router]
type=service
router=binlogrouter
router_options=server-id=4000,binlogdir=/var/lib/mysql,filestem=binlog
user=maxuser
passwd=maxpwd

[avro-router]
type=service
router=avrorouter
source=replication-router
```



**Note:** Since the 2.1 version of MaxScale, all of the router options can also
be defined as parameters.



```
[replication-router]
type=service
router=binlogrouter
router_options=server-id=4000,binlogdir=/var/lib/mysql,filestem=binlog
user=maxuser
passwd=maxpwd

[avro-router]
type=service
router=avrorouter
binlogdir=/var/lib/mysql
filestem=binlog
avrodir=/var/lib/maxscale
```



## Router Options


The avrorouter is configured with a comma-separated list of key-value pairs.
Currently the router has one mandatory parameter, `<code>binlogdir</code>`. If no `<code>source</code>`
parameter is defined, binlogdir needs to be manually defined in the router
options. The following options should be given as a value to the
`<code>router_options</code>` parameter.


### General Options


These options control various file locations and names.


#### `<code>binlogdir</code>`


The location of the binary log files. This is the first mandatory parameter
and it defines where the module will read binlog files from. Read access to
this directory is required.


If used in conjunction with the Binlog Server, the value of this option should
be the same for both the Binlog Server and the avrorouter if the `<code>source</code>` parameter
is not used.


#### `<code>avrodir</code>`


The location where the Avro files are stored. This is the second mandatory
parameter and it governs where the converted files are stored. This directory
will be used to store the Avro files, plain-text Avro schemas and other files
needed by the avrorouter. The user running MariaDB MaxScale will need both read and
write access to this directory.


The avrorouter will also use the *avrodir* to store various internal
files. These files are named *avro.index* and *avro-conversion.ini*. By default,
the default data directory, */var/lib/maxscale/*, is used. Before version 2.1 of
MaxScale, the value of *binlogdir* was used as the default value for *avrodir*.


#### `<code>filestem</code>`


The base name of the binlog files. The default value is "mysql-bin". The binlog
files are assumed to follow the naming schema *<filestem>.<n>* where *<n>* is
the binlog number and *<filestem>* is the value of this router option.


For example, with the following router option:



```
filestem=mybin,binlogdir=/var/lib/mysql/binlogs/
```



The first binlog file the avrorouter would look for is `<code>/var/lib/mysql/binlogs/mybin.000001</code>`.


#### `<code>start_index</code>`


The starting index number of the binlog file. The default value is 1.
For the binlog *mysql-bin.000001* the index would be 1, for *mysql-bin.000005*
the index would be 5.


If you need to start from a binlog file other than 1, you need to set the value
of this option to the correct index. The avrorouter will always start from the
beginning of the binary log file.


### Avro file options


These options control how large the Avro file data blocks can get.
Increasing or lowering the block size could have a positive effect
depending on your use case. For more information about the Avro file
format and how it organizes data, refer to the [Avro documentation](https://avro.apache.org/docs/current/).


The avrorouter will flush a block and start a new one when either `<code>group_trx</code>`
transactions or `<code>group_rows</code>` row events have been processed. Changing these
options will also allow more frequent updates to stored data but this
will cause a small increase in file size and search times.


It is highly recommended to keep the block sizes relatively large to allow
larger chunks of memory to be flushed to disk at one time. This will make
the conversion process noticeably faster.


#### `<code>group_trx</code>`


Controls the number of transactions that are grouped into a single Avro
data block. The default value is 1 transaction.


#### `<code>group_rows</code>`


Controls the number of row events that are grouped into a single Avro
data block. The default value is 1000 row events.


#### `<code>block_size</code>`


The Avro data block size in bytes. The default is 16 kilobytes. Increase this
value if individual events in the binary logs are very large.


## Module commands


Read [Module Commands](../maxscale-21-reference/mariadb-maxscale-21-module-commands.md) documentation for details about module commands.


The avrorouter supports the following module commands.


### `<code>avrorouter::convert SERVICE {start | stop}</code>`


Start or stop the binary log to Avro conversion. The first parameter is the name
of the service to stop and the second parameter tells whether to start the
conversion process or to stop it.


### `<code>avrorouter::purge SERVICE</code>`


This command will delete all files created by the avrorouter. This includes all
.avsc schema files and .avro data files as well as the internal state tracking
files. Use this to completely reset the conversion process.


**Note:** Once the command has completed, MaxScale must be restarted to restart
the conversion process. Issuing a `<code>convert start</code>` command **will not work**.


**WARNING:** You will lose any and all converted data when this command is
 executed.


# Files Created by the Avrorouter


The avrorouter creates two files in the location pointed by *avrodir*:
*avro.index* and *avro-conversion.ini*. The *avro.index* file is used to store
the locations of the GTIDs in the .avro files. The *avro-conversion.ini* contains
the last converted position and GTID in the binlogs. If you need to reset the
conversion process, delete these two files and restart MaxScale.


# Resetting the Conversion Process


To reset the binlog conversion process, issue the `<code>purge</code>` module command by
executing it via MaxAdmin and stop MaxScale. If manually created schema files
were used, they need to be recreated once MaxScale is stopped. After stopping
MaxScale and optionally creating the schema files, the conversion process can be
started by starting MaxScale.


# Example Client


The avrorouter comes with an example client program, *cdc.py*, written in Python 3.
This client can connect to a MaxScale configured with the CDC protocol and the
avrorouter.


Before using this client, you will need to install the Python 3 interpreter and
add users to the service with the *cdc_users.py* script. Fore more details about
the user creation, please refer to the [CDC Protocol](../maxscale-21-protocols/mariadb-maxscale-21-change-data-capture-cdc-protocol.md)
and [CDC Users](../maxscale-21-protocols/mariadb-maxscale-21-change-data-capture-cdc-users.md) documentation.


Read the output of `<code>cdc.py --help</code>` for a full list of supported options
and a short usage description of the client program.


# Avro Schema Generator


If the CREATE TABLE statements for the tables aren't present in the current
binary logs, the schema files must be generated with a schema file
generator. There are currently two methods to generate the .avsc schema files.


## Python Schema Generator



```
usage: cdc_schema.py [--help] [-h HOST] [-P PORT] [-u USER] [-p PASSWORD] DATABASE
```



The *cdc_schema.py* executable is installed as a part of MaxScale. This is a
Python 3 script that generates Avro schema files from an existing database.


The script will generate the .avsc schema files into the current directory. Run
the script for all required databases copy the generated .avsc files to the
directory where the avrorouter stores the .avro files (the value of `<code>avrodir</code>`).


## Go Schema Generator


The *cdc_schema.go* example Go program is provided with MaxScale. This file
can be used to create Avro schemas for the avrorouter by connecting to a
database and reading the table definitions. You can find the file in MaxScale's
share directory in `<code>/usr/share/maxscale/</code>`.


You'll need to install the Go compiler and run `<code>go get</code>` to resolve Go
dependencies before you can use the *cdc_schema* program. After resolving the
dependencies you can run the program with `<code>go run cdc_schema.go</code>`. The program
will create .avsc files in the current directory. These files should be moved
to the location pointed by the *avrodir* option of the avrorouter if they are
to be used by the router itself.


Read the output of `<code>go run cdc_schema.go -help</code>` for more information on how
to run the program.


# Examples


The [Avrorouter Tutorial](../maxscale-21-tutorials/mariadb-maxscale-21-avrorouter-tutorial.md) shows you how
the Avrorouter works with the Binlog Server to convert binlogs from a master server
into easy to process Avro data.


Here is a simple configuration example which reads binary logs locally from `<code>/var/lib/mysql/</code>`
and stores them as Avro files in `<code>/var/lib/maxscale/avro/</code>`. The service has one listener
listening on port 4001 for CDC protocol clients.



```
[avro-converter]
type=service
router=avrorouter
router_options=binlogdir=/var/lib/mysql/,
        filestem=binlog,
        avrodir=/var/lib/maxscale/avro/

[avro-listener]
type=listener
service=avro-converter
protocol=CDC
port=4001
```



Here is an example how you can query for data in JSON format using the *cdc.py* Python script.
It queries the table *test.mytable* for all change records.



```
cdc.py --user=myuser --password=mypasswd --host=127.0.0.1 --port=4001 test.mytable
```



You can then combine it with the *cdc_kafka_producer.py* to publish these change records to a Kafka broker.



```
cdc.py --user=myuser --password=mypasswd --host=127.0.0.1 --port=4001 test.mytable | cdc_kafka_producer.py --kafka-broker 127.0.0.1:9092 --kafka-topic test.mytable
```



For more information on how to use these scripts, see the output of `<code>cdc.py -h</code>` and `<code>cdc_kafka_producer.py -h</code>`.


# Building Avrorouter


To build the avrorouter from source, you will need the [Avro C](https://avro.apache.org/docs/current/api/c/)
library, liblzma, [the Jansson library](https://www.digip.org/jansson/) and sqlite3 development headers. When
configuring MaxScale with CMake, you will need to add `<code>-DBUILD_CDC=Y</code>` to build the CDC module set.


The Avro C library needs to be build with position independent code enabled. You can do this by
adding the following flags to the CMake invocation when configuring the Avro C library.



```
-DCMAKE_C_FLAGS=-fPIC -DCMAKE_CXX_FLAGS=-fPIC
```



For more details about building MaxScale from source, please refer to the
[Building MaxScale from Source Code](../maxscale-21-getting-started/mariadb-maxscale-21-building-mariadb-maxscale-from-source-code.md) document.
