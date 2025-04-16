
# Avrorouter

# Avrorouter


The avrorouter is a MariaDB 10.0 binary log to Avro file converter. It consumes
binary logs from a local directory and transforms them into a set of Avro files.
These files can then be queried by clients for various purposes.


This router is intended to be used in tandem with the
[Binlog Server](mariadb-maxscale-25-binlogrouter-24.md).
The Binlog Server can connect to a master server and request binlog records.
These records can then consumed by the avrorouter directly from the binlog cache
of the Binlog Server. This allows MariaDB MaxScale to automatically transform
binlog events on the master to local Avro format files.


![](../../.gitbook/assets/mariadb-corporation/MaxScale/2.5.29/Documentation/Routers/images/Binlog-Avro.png.png)


The avrorouter can also consume binary logs straight from the master. This will
remove the need to configure the Binlog Server but it will increase the disk space
requirement on the master server by at least a factor of two.


The converted Avro files can be requested with the CDC protocol. This protocol
should be used to communicate with the avrorouter and currently it is the only
supported protocol. The clients can request either Avro or JSON format data
streams from a database table.




* [Avrorouter](#avrorouter)

  * [Direct Replication Mode](#direct-replication-mode)
  * [Configuration](#configuration)

    * [Router Parameters](#router-parameters)

      * [gtid_start_pos](#gtid_start_pos)
      * [server_id](#server_id)
      * [source](#source)
      * [codec](#codec)
      * [match and exclude](#match-and-exclude)
      * [binlogdir](#binlogdir)
      * [avrodir](#avrodir)

        * [filestem](#filestem)
      * [start_index](#start_index)

        * [Example configuration](#example-configuration)
      * [Avro File Related Parameters](#avro-file-related-parameters)

        * [group_trx](#group_trx)
        * [group_rows](#group_rows)
        * [block_size](#block_size)
  * [Module commands](#module-commands)

    * [avrorouter::convert SERVICE {start | stop}](#avrorouterconvert-service-start-stop)
    * [avrorouter::purge SERVICE](#avrorouterpurge-service)
  * [Files Created by the Avrorouter](#files-created-by-the-avrorouter)
  * [Resetting the Conversion Process](#resetting-the-conversion-process)
  * [Stopping the Avrorouter](#stopping-the-avrorouter)
  * [Example Client](#example-client)
  * [Avro Schema Generator](#avro-schema-generator)

    * [Simple Schema Generator](#simple-schema-generator)
    * [Python Schema Generator](#python-schema-generator)
    * [Go Schema Generator](#go-schema-generator)
  * [Examples](#examples)
  * [Building Avrorouter](#building-avrorouter)
  * [Router Diagnostics](#router-diagnostics)
  * [Limitations](#limitations)




## Direct Replication Mode


MaxScale 2.4.0 added a direct replication mode that connects the avrorouter
directly to a MariaDB server. This mode is an improvement over the binlogrouter
based replication as it provides a more space-efficient and faster conversion
process. This is the recommended method of using the avrorouter as it is faster,
more efficient and less prone to errors caused by missing DDL events.


To enable the direct replication mode, add either the `<code>servers</code>` or the `<code>cluster</code>`
parameter to the avrorouter service. The avrorouter will then use one of the
servers as the replication source.


Here is a minimal avrorouter direct replication configuration:



```
[maxscale]
threads=auto

[server1]
type=server
address=127.0.0.1
port=3306
protocol=MariaDBBackend

[cdc-service]
type=service
router=avrorouter
servers=server1
user=maxuser
password=maxpwd

[cdc-listener]
type=listener
service=cdc-service
protocol=CDC
port=4001
```



In direct replication mode, the avrorouter stores the latest replicated GTID in
the `<code>last_gtid.txt</code>` file located in the `<code>avrodir</code>` (defaults to
`<code>/var/lib/maxscale</code>`). To reset the replication process, stop MaxScale and remove
the file.


Additionally, the avrorouter will attempt to automatically create any missing
schema files for tables that have data events for them but the DDL for those
tables is not contained in the binlogs.


## Configuration


For information about common service parameters, refer to the
[Configuration Guide](../maxscale-25-getting-started/mariadb-maxscale-25-mariadb-maxscale-configuration-guide.md).


### Router Parameters


#### `<code>gtid_start_pos</code>`


The GTID where avrorouter starts the replication from in direct replication
mode. The parameter value must be in the MariaDB GTID format e.g. 0-1-123 where
the first number is the replication domain, the second the server_id value of
the server and the last is the GTID sequence number.


This parameter has no effect in the traditional mode. If this parameter is
defined, the replication will start from the implicit GTID that the master first
serves.


#### `<code>server_id</code>`


The
[server_id](../../../server/server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md#server_id)
used when replicating from the master in direct replication mode. The default
value is 1234.


#### `<code>source</code>`


**Note:** This parameter has been removed in MaxScale 2.5.0 due to changes in
 the binlogrouter. The direct replication mode is the recommended mode
 of operation. Using the binlogrouter is less efficient and more
 cumbersome to both configure and manage than the direct replication
 mode.


#### `<code>codec</code>`


The compression codec to use. By default, the avrorouter does not use compression.


This parameter takes one of the following two values; *null* or
*deflate*. These are the mandatory compression algorithms required by the
Avro specification. For more information about the compression types,
refer to the [Avro specification](https://avro.apache.org/docs/current/spec.html#Required+Codecs).


#### `<code>match</code>` and `<code>exclude</code>`


These [regular expression settings](../maxscale-25-getting-started/mariadb-maxscale-25-mariadb-maxscale-configuration-guide.md#standard-regular-expression-settings-for-filters)
filter events for processing depending on table names. Avrorouter does not support the
*options*-parameter for regular expressions.


To prevent excessive matching of similarly named tables, surround each table
name with the `<code>^</code>` and `<code>$</code>` tokens. For example, to match the `<code>test.clients</code>` table
but not `<code>test.clients_old</code>` table use `<code>match=^test[.]clients$</code>`. For multiple
tables, surround each table in parentheses and add a pipe character between
them: `<code>match=(^test[.]t1$)|(^test[.]t2$)</code>`.


#### `<code>binlogdir</code>`


The location of the binary log files. This is the first mandatory parameter
and it defines where the module will read binlog files from. Read access to
this directory is required.


If used in conjunction with the binlogrouter, the value of this option should be
the same for both the binlogrouter and the avrorouter.


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


##### `<code>filestem</code>`


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


##### Example configuration



```
[replication-router]
type=service
router=binlogrouter
router_options=server-id=4000,binlogdir=/var/lib/mysql,filestem=binlog
user=maxuser
password=maxpwd

[avro-router]
type=service
router=avrorouter
binlogdir=/var/lib/mysql
filestem=binlog
avrodir=/var/lib/maxscale
```



#### Avro File Related Parameters


These options control how large the Avro file data blocks can get.
Increasing or lowering the block size could have a positive effect
depending on your use case. For more information about the Avro file
format and how it organizes data, refer to the
[Avro documentation](https://avro.apache.org/docs/current/).


The avrorouter will flush a block and start a new one when either `<code>group_trx</code>`
transactions or `<code>group_rows</code>` row events have been processed. Changing these
options will also allow more frequent updates to stored data but this
will cause a small increase in file size and search times.


It is highly recommended to keep the block sizes relatively large to allow
larger chunks of memory to be flushed to disk at one time. This will make
the conversion process noticeably faster.


##### `<code>group_trx</code>`


Controls the number of transactions that are grouped into a single Avro
data block. The default value is 1 transaction.


##### `<code>group_rows</code>`


Controls the number of row events that are grouped into a single Avro
data block. The default value is 1000 row events.


##### `<code>block_size</code>`


The Avro data block size in bytes. The default is 16 kilobytes. Increase this
value if individual events in the binary logs are very large. The value is a
size type parameter which means that it can also be defined with an SI suffix.
Refer to the [Configuration Guide](../maxscale-25-getting-started/mariadb-maxscale-25-mariadb-maxscale-configuration-guide.md)
for more details about size type parameters and how to use them.


## Module commands


Read [Module Commands](../maxscale-25-reference/mariadb-maxscale-25-module-commands.md) documentation for
details about module commands.


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


## Files Created by the Avrorouter


The avrorouter creates two files in the location pointed by *avrodir*:
*avro.index* and *avro-conversion.ini*. The *avro.index* file is used to store
the locations of the GTIDs in the .avro files. The *avro-conversion.ini* contains
the last converted position and GTID in the binlogs. If you need to reset the
conversion process, delete these two files and restart MaxScale.


## Resetting the Conversion Process


To reset the binlog conversion process, issue the `<code>purge</code>` module command by
executing it via MaxCtrl and stop MaxScale. If manually created schema files
were used, they need to be recreated once MaxScale is stopped. After stopping
MaxScale and optionally creating the schema files, the conversion process can be
started by starting MaxScale.


## Stopping the Avrorouter


The safest way to stop the avrorouter when used with the binlogrouter is to
follow the following steps:


* Issue `<code>STOP SLAVE</code>` on the binlogrouter
* Wait for the avrorouter to process all files
* Stop MaxScale with `<code>systemctl stop maxscale</code>`


This guarantees that the conversion process halts at a known good position in
the latest binlog file.


## Example Client


The avrorouter comes with an example client program, *cdc.py*, written in Python 3.
This client can connect to a MaxScale configured with the CDC protocol and the
avrorouter.


Before using this client, you will need to install the Python 3 interpreter and
add users to the service with the *cdc_users.py* script. Fore more details about
the user creation, please refer to the [CDC Protocol](../maxscale-25-protocols/mariadb-maxscale-25-change-data-capture-cdc-protocol.md)
and [CDC Users](../maxscale-25-protocols/mariadb-maxscale-25-change-data-capture-cdc-users.md) documentation.


Read the output of `<code>cdc.py --help</code>` for a full list of supported options
and a short usage description of the client program.


## Avro Schema Generator


The avrorouter needs to have access to the CREATE TABLE statement for all tables
for which there are data events in the binary logs. If the CREATE TABLE
statements for the tables aren't present in the current binary logs, the schema
files must be created.


In the direct replication mode, avrorouter will automatically create the missing
schema files by connecting to the database and executing a `<code>SHOW CREATE TABLE</code>`
statement. If a connection cannot be made or the service user lacks the
permission, an error will be logged and the data events for that table will not
be processed.


For the legacy binlog mode, the files must be generated with a schema file
generator. There are currently two methods to generate the .avsc schema files.


### Simple Schema Generator


The `<code>cdc_one_schema.py</code>` generates a schema file for a single table by reading a
tab separated list of field and type names from the standard input. This is the
recommended schema generation tool as it does not directly communicate with the
database thus making it more flexible.


The only requirement to run the script is that a Python interpreter is
installed.


To use this script, pipe the output of the `<code>mysql</code>` command line into the
`<code>cdc_one_schema.py</code>` script:



```
mysql -ss -u <user> -p -h <host> -P <port> -e 'DESCRIBE `<database>`.`<table>`'|./cdc_one_schema.py <database> <table>
```



Replace the `<code><user></code>`, `<code><host></code>`, `<code><port></code>`, `<code><database></code>` and `<code><table></code>` with
appropriate values and run the command. Note that the `<code>-ss</code>` parameter is
mandatory as that will generate the tab separated output instead of the default
pretty-printed output.


An .avsc file named after the database and table name will be generated in the
current working directory. Copy this file to the location pointed by the
`<code>avrodir</code>` parameter of the avrorouter.


Alternatively, you can also copy the output of the `<code>mysql</code>` command to a file and
feed it into the script if you cannot execute the SQL command directly:



```
# On the database server
mysql -ss -u <user> -p -h <host> -P <port> -e 'DESCRIBE `<database>`.`<table>`' > schema.tsv
# On the MaxScale server
./cdc_one_schema.py <database> <table> < schema.tsv
```



If you want to use a specific Python interpreter instead of the one found in the
search path, you can modify the first line of the script from `<code>#!/usr/bin/env
python</code>` to `<code>#!/path/to/python</code>` where `<code>/path/to/python</code>` is the absolute path to
the Python interpreter (both Python 2 and Python 3 can be used).


### Python Schema Generator



```
usage: cdc_schema.py [--help] [-h HOST] [-P PORT] [-u USER] [-p PASSWORD] DATABASE
```



The *cdc_schema.py* executable is installed as a part of MaxScale. This is a
Python 3 script that generates Avro schema files from an existing database.


The script will generate the .avsc schema files into the current directory. Run
the script for all required databases copy the generated .avsc files to the
directory where the avrorouter stores the .avro files (the value of `<code>avrodir</code>`).


### Go Schema Generator


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


## Examples


The [Avrorouter Tutorial](../maxscale-25-tutorials/mariadb-maxscale-25-avrorouter-tutorial.md) shows you how
the Avrorouter works with the Binlog Server to convert binlogs from a master server
into easy to process Avro data.


Here is a simple configuration example which reads binary logs locally from
`<code>/var/lib/mysql/</code>` and stores them as Avro files in `<code>/var/lib/maxscale/avro/</code>`.
The service has one listener listening on port 4001 for CDC protocol clients.



```
[avro-converter]
type=service
router=avrorouter
user=myuser
password=mypasswd
router_options=binlogdir=/var/lib/mysql/,
        filestem=binlog,
        avrodir=/var/lib/maxscale/avro/

[avro-listener]
type=listener
service=avro-converter
protocol=CDC
port=4001
```



Here is an example how you can query for data in JSON format using the *cdc.py*
Python script. It queries the table *test.mytable* for all change records.



```
cdc.py --user=myuser --password=mypasswd --host=127.0.0.1 --port=4001 test.mytable
```



You can then combine it with the *cdc_kafka_producer.py* to publish these change
records to a Kafka broker.



```
cdc.py --user=myuser --password=mypasswd --host=127.0.0.1 --port=4001 test.mytable |
cdc_kafka_producer.py --kafka-broker 127.0.0.1:9092 --kafka-topic test.mytable
```



For more information on how to use these scripts, see the output of `<code>cdc.py -h</code>`
and `<code>cdc_kafka_producer.py -h</code>`.


## Building Avrorouter


To build the avrorouter from source, you will need the
[Avro C](https://avro.apache.org/docs/current/api/c/) library, liblzma,
[the Jansson library](https://www.digip.org/jansson/) and sqlite3 development
headers. When configuring MaxScale with CMake, you will need to add
`<code>-DBUILD_CDC=Y</code>` to build the CDC module set.


The Avro C library needs to be build with position independent code enabled. You
can do this by adding the following flags to the CMake invocation when
configuring the Avro C library.



```
-DCMAKE_C_FLAGS=-fPIC -DCMAKE_CXX_FLAGS=-fPIC
```



For more details about building MaxScale from source, please refer to the
[Building MaxScale from Source Code](../maxscale-25-getting-started/mariadb-maxscale-25-building-mariadb-maxscale-from-source-code.md)
document.


## Router Diagnostics


The `<code>router_diagnostics</code>` output for an avrorouter service contains the following
fields.


* `<code>infofile</code>`: File where the avrorouter stores the conversion process state.
* `<code>avrodir</code>`: Directory where avro files are stored
* `<code>binlogdir</code>`: Directory where binlog files are read from
* `<code>binlog_name</code>`: Current binlog name
* `<code>binlog_pos</code>`: Current binlog position
* `<code>gtid</code>`: Current GTID
* `<code>gtid_timestamp</code>`: Current GTID timestamp
* `<code>gtid_event_number</code>`: Current GTID event number


## Limitations


The avrorouter does not support the following data types, conversions or SQL statements:


* BIT
* Fields CAST from integer types to string types
* [CREATE TABLE ... AS SELECT statements](../../../server/reference/sql-statements-and-structure/vectors/create-table-with-vectors.md)


The avrorouter does not do any crash recovery. This means that the avro files
need to be removed or truncated to valid block lengths before starting the
avrorouter.
