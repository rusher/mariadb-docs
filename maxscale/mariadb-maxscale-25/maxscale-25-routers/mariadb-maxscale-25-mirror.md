
# Mirror

# Mirror


*Note:* This module is a part of the experimental module package,
 `<code>maxscale-experimental</code>`.




* [Mirror](#mirror)

  * [Overview](#overview)
  * [Configuration Parameters](#configuration-parameters)

    * [main](#main)
    * [exporter](#exporter)
    * [file](#file)
    * [kafka_broker](#kafka_broker)
    * [kafka_topic](#kafka_topic)
  * [Example Configuration](#example-configuration)
  * [Limitations](#limitations)




## Overview


The `<code>mirror</code>` router is designed for data consistency and database behavior
verification during system upgrades. It allows statement duplication to multiple
servers in a manner similar to that of the
[Tee filter](../maxscale-25-filters/mariadb-maxscale-25-tee-filter.md) with exporting of collected query metrics.


For each executed query the router exports a JSON object that describes the
query results and has the following fields:


| Key | Description |
| --- | --- |
| Key | Description |
| query | The executed SQL if an SQL statement was executed |
| command | The SQL command |
| session | The connection ID of the session that executed the query |
| query_id | Query sequence number, starts from 1 |
| results | Array of query result objects |


The objects in the `<code>results</code>` array describe an individual query result and have
the following fields:


| Key | Description |
| --- | --- |
| Key | Description |
| target | The target where the query was executed |
| checksum | The CRC32 checksum of the result |
| rows | Number of returned rows |
| warnings | Number of returned warnings |
| duration | Query duration in milliseconds |
| type | Result type, one of ok, error or resultset |


## Configuration Parameters


### `<code>main</code>`


The main target from which results are returned to the client. This is a
mandatory parameter and must define one of the targets configured in the
`<code>targets</code>` parameter of the service.


If the connection to the main target cannot be created or is lost mid-session,
the client connection will be closed. Connection failures to other targets are
not fatal errors and any open connections to them will be closed. The router
does not create new connections after the initial connections are created.


### `<code>exporter</code>`


The exporter where the data is exported. This is a mandatory parameter. Possible
values are:


* `<code>log</code>`
* Exports metrics to MaxScale log on INFO level. No configuration parameters.
* `<code>file</code>`
* Exports metrics to a file. Configured with the [file](#file) parameter.
* `<code>kafka</code>`
* Exports metrics to a Kafka broker. Configured with the
 [kafka_broker](#kafka_broker) and [kafka_topic](#kafka_topic)
 parameters.


### `<code>file</code>`


The output file where the metrics will be written. The file must be writable by
the user that is running MaxScale, usually the `<code>maxscale</code>` user.


When the `<code>file</code>` parameter is altered at runtime, the old file is closed before
the new file is opened. This makes it a convenient way of rotating the file
where the metrics are exported. Note that the file name alteration must change
the value for it to take effect.


This is a mandatory parameter when configured with `<code>exporter=file</code>`.


### `<code>kafka_broker</code>`


The Kafka broker list. Must be given as a comma-separated list of broker hosts
with optional ports in `<code>host:port</code>` format.


This is a mandatory parameter when configured with `<code>exporter=kafka</code>`.


### `<code>kafka_topic</code>`


The kafka topic where the metrics are sent.


This is a mandatory parameter when configured with `<code>exporter=kafka</code>`.


## Example Configuration



```
[server1]
type=server
address=127.0.0.1
port=3000

[server2]
type=server
address=127.0.0.1
port=3001

[MariaDB-Monitor]
type=monitor
module=mariadbmon
servers=server1,server2
user=maxuser
password=maxpwd
monitor_interval=2000

[Mirror-Router]
type=service
router=mirror
user=maxuser
password=maxpwd
targets=server1,server2
main=server1
exporter=file
file=/tmp/Mirror-Router.log

[Mirror-Listener]
type=listener
protocol=mariadbclient
service=Mirror-Router
port=3306
```



## Limitations


* Broken network connections are not recreated.
* Prepared statements are not supported.
* Contents of non-SQL statements are not added to the exported metrics.
* Data synchronization in dynamic environments (e.g. when replication is in use)
 is not guaranteed. This means that result mismatches can be reported when the
 data is only eventually consistent.
