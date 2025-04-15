
# KafkaCDC

# KafkaCDC




* [KafkaCDC](#kafkacdc)

  * [Overview](#overview)
  * [Configuration](#configuration)
  * [Parameters](#parameters)

    * [bootstrap_servers](#bootstrap_servers)
    * [topic](#topic)
    * [enable_idempotence](#enable_idempotence)
    * [timeout](#timeout)
    * [gtid](#gtid)

      * [server_id](#server_id)
  * [Example Configuration](#example-configuration)
  * [Limitations](#limitations)




## Overview


The KafkaCDC module reads data changes in MariaDB via replication and converts
them into JSON objects that are then streamed to a Kafka broker.


DDL events (`<code>CREATE TABLE</code>`, `<code>ALTER TABLE</code>`) are streamed as JSON objects in the
following format (example created by `<code>CREATE TABLE test.t1(id INT)</code>`):



```
{
  "namespace": "MaxScaleChangeDataSchema.avro",
  "type": "record",
  "name": "ChangeRecord",
  "table": "t2",              // name of the table
  "database": "test",         // the database the table is in
  "version": 1,               // schema version, incremented when the table format changes
  "gtid": "0-3000-14",        // GTID that created the current version of the table
  "fields": [
    {
      "name": "domain",       // First part of the GTID
      "type": "int"
    },
    {
      "name": "server_id",    // Second part of the GTID
      "type": "int"
    },
    {
      "name": "sequence",     // Third part of the GTID
      "type": "int"
    },
    {
      "name": "event_number", // Sequence number of the event inside the GTID
      "type": "int"
    },
    {
      "name": "timestamp",    // UNIX timestamp when the event was created
      "type": "int"
    },
    {
      "name": "event_type",   // Event type
      "type": {
        "type": "enum",
        "name": "EVENT_TYPES",
        "symbols": [
          "insert",           // The row that was inserted
          "update_before",    // The row before it was updated
          "update_after",     // The row after it was updated
          "delete"            // The row that was deleted
        ]
      }
    },
    {
      "name": "id",           // Field name
      "type": [
        "null",
        "long"
      ],
      "real_type": "int",     // Field type
      "length": -1,           // Field length, if found
      "unsigned": false       // Whether the field is unsigned
    }
  ]
}
```



The `<code>domain</code>`, `<code>server_id</code>` and `<code>sequence</code>` fields contain the GTID that this event
belongs to. The `<code>event_number</code>` field is the sequence number of events inside the
transaction starting from 1. The `<code>timestamp</code>` field is the UNIX timestamp when
the event occurred. The `<code>event_type</code>` field contains the type of the event, one
of:


* `<code>insert</code>`: the event is the data that was added to MariaDB
* `<code>delete</code>`: the event is the data that was removed from MariaDB
* `<code>update_before</code>`: the event contains the data before an update statement modified it
* `<code>update_after</code>`: the event contains the data after an update statement modified it


All remaining fields contains data from the table. In the example event this
would be the fields `<code>id</code>` and `<code>data</code>`.


DML events (`<code>INSERT</code>`, `<code>UPDATE</code>`, `<code>DELETE</code>`) are streamed as JSON objects that
follow the format specified in the DDL event. The objects are in the following
format (example created by `<code>INSERT INTO test.t1 VALUES (1)</code>`):



```
{
  "domain": 0,
  "server_id": 3000,
  "sequence": 20,
  "event_number": 1,
  "timestamp": 1580485945,
  "event_type": "insert",
  "id": 1,
  "table_name": "t2",
  "table_schema": "test"
}
```



The `<code>table_name</code>` and `<code>table_schema</code>` fields were added in MaxScale 2.5.3. These
contain the table name and schema the event targets.


The router stores table metadata in the MaxScale data directory. The
default value is `<code>/var/lib/maxscale/<service name></code>`. If data for a table
is replicated before a DDL event for it is replicated, the CREATE TABLE
will be queried from the master server.


During shutdown, the Kafka event queue is flushed. This can take up to 60
seconds if the network is slow or there are network problems.


## Configuration


The `<code>servers</code>` parameter defines the set of servers where the data is replicated
from. The replication will be done from the first master server that is found.


The `<code>user</code>` and `<code>password</code>` of the service will be used to connect to the
master. This user requires the REPLICATION SLAVE grant.


The KafkaCDC service must not be configured to use listeners. If a listener is
configured, all attempts to start a session will fail.


## Parameters


### `<code>bootstrap_servers</code>`


The list of Kafka brokers to use in `<code>host:port</code>` format. Multiple values
can be separated with commas. This is a mandatory parameter.


### `<code>topic</code>`


The Kafka topic where the replicated events will be sent. This is a
mandatory parameter.


### `<code>enable_idempotence</code>`


Enable idempotent producer mode. This feature requires Kafka version 0.11 or
newer to work and is disabled by default.


When enabled, the Kafka producer enters a strict mode which avoids event
duplication due to broker outages or other network errors. In HA scenarios where
there are more than two MaxScale instances, event duplication can still happen
as there is no synchronization between the MaxScale instances.


The Kafka C library,
[librdkafka](https://github.com/edenhill/librdkafka/blob/master/CONFIGURATION),
describes the parameter as follows:



When set to true, the producer will ensure that messages are successfully
produced exactly once and in the original produce order. The following
configuration properties are adjusted automatically (if not modified by the
user) when idempotence is enabled: max.in.flight.requests.per.connection=5 (must
be less than or equal to 5), retries=INT32_MAX (must be greater than 0),
acks=all, queuing.strategy=fifo.



### `<code>timeout</code>`


The connection and read timeout for the replication stream. The default
value is 10 seconds.


### `<code>gtid</code>`


The initial GTID position from where the replication is started. By default the
replication is started from the beginning. The value of this parameter is only
used if no previously replicated events with GTID positions can be retrieved
from Kafka.


#### `<code>server_id</code>`


The
[server_id](../../../server/server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md#server_id)
used when replicating from the master in direct replication mode. The default
value is 1234. This parameter was added in MaxScale 2.5.7.


## Example Configuration


The following configuration defines the minimal setup for streaming replication
events from MariaDB into Kafka as JSON:



```
# The server we're replicating from
[server1]
type=server
address=127.0.0.1
port=3306
protocol=MariaDBBackend

# The monitor for the server
[MariaDB-Monitor]
type=monitor
module=mariadbmon
servers=server1
user=maxuser
password=maxpwd
monitor_interval=5000

# The MariaDB-to-Kafka CDC service
[Kafka-CDC]
type=service
router=kafkacdc
servers=server1
user=maxuser
password=maxpwd
bootstrap_servers=127.0.0.1:9092
topic=my-cdc-topic
```



## Limitations


* The KafkaCDC module provides at-least-once semantics for the generated
 events. This means that each replication event is delivered to kafka at least
 once but there can be duplicate events in case of failures.
* Authentication to Kafka is not currently supported.
