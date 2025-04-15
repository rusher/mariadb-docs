
# MaxScale 21.06 KafkaCDC

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
    * [match](#match)
    * [exclude](#exclude)
    * [cooperative_replication](#cooperative_replication)
    * [read_gtid_from_kafka](#read_gtid_from_kafka)
    * [kafka_ssl](#kafka_ssl)
    * [kafka_ssl_ca](#kafka_ssl_ca)
    * [kafka_ssl_cert](#kafka_ssl_cert)
    * [kafka_ssl_key](#kafka_ssl_key)
    * [kafka_sasl_user](#kafka_sasl_user)
    * [kafka_sasl_password](#kafka_sasl_password)
    * [kafka_sasl_mechanism](#kafka_sasl_mechanism)
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


* In order for `<code>kafkacdc</code>` to work, the binary logging on the source server must
 be configured to use row-based replication and the row image must be set to
 full by configuring `<code>binlog_format=ROW</code>` and `<code>binlog_row_image=FULL</code>`.
* The `<code>servers</code>` parameter defines the set of servers where the data is
 replicated from. The replication will be done from the first master server
 that is found.
* The `<code>user</code>` and `<code>password</code>` of the service will be used to connect to the
 master. This user requires the `<code>REPLICATION SLAVE</code>` grant.
* The KafkaCDC service must not be configured to use listeners. If a listener is
 configured, all attempts to start a session will fail.


## Parameters


### `<code>bootstrap_servers</code>`


* Type: string
* Mandatory: Yes
* Dynamic: No


The list of Kafka brokers to use in `<code>host:port</code>` format. Multiple values
can be separated with commas. This is a mandatory parameter.


### `<code>topic</code>`


* Type: string
* Mandatory: Yes
* Dynamic: No


The Kafka topic where the replicated events will be sent. This is a
mandatory parameter.


### `<code>enable_idempotence</code>`


* Type: [boolean](../mariadb-maxscale-21-06-getting-started/mariadb-maxscale-2106-maxscale-2106-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `<code>false</code>`


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


* Type: [duration](../mariadb-maxscale-21-06-getting-started/mariadb-maxscale-2106-maxscale-2106-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `<code>10s</code>`


The connection and read timeout for the replication stream.


### `<code>gtid</code>`


* Type: string
* Mandatory: No
* Dynamic: No
* Default: `<code>""</code>`


The initial GTID position from where the replication is started. By default the
replication is started from the beginning. The value of this parameter is only
used if no previously replicated events with GTID positions can be retrieved
from Kafka.


Once the replication has started and a GTID position has been recorded, this
parameter will be ignored. To reset the recorded GTID position, delete the
`<code>current_gtid.txt</code>` file located in `<code>/var/lib/maxscale/<SERVICE>/</code>` where
`<code><SERVICE></code>` is the name of the KafkaCDC service.


### `<code>server_id</code>`


* Type: number
* Mandatory: No
* Dynamic: No
* Default: `<code>1234</code>`


The
[server_id](../../../server/server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md#server_id)
used when replicating from the master in direct replication mode. The default
value is 1234. This parameter was added in MaxScale 2.5.7.


### `<code>match</code>`


* Type: [regex](../mariadb-maxscale-21-06-getting-started/mariadb-maxscale-2106-maxscale-2106-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `<code>""</code>`


Only include data from tables that match this pattern.


For example, if configured with `<code>match=accounts[.].*</code>`, only data from the
`<code>accounts</code>` database is sent to Kafka.


The pattern is matched against the combined database and table name separated by
a period. This means that the event for the table `<code>t1</code>` in the `<code>test</code>` database
would appear as `<code>test.t1</code>`. The behavior is the same even if the database or the
table name contains a period. This means that an event for the `<code>test.table</code>`
table in the `<code>my.data</code>` database would appear as `<code>my.data.test.table</code>`.


Here is an example configuration that only sends events for tables from the
`<code>db1</code>` database. The `<code>accounts</code>` and `<code>users</code>` tables in the `<code>db1</code>` database are
filtered out using the `<code>exclude</code>` parameter.



```
[Kafka-CDC]
type=service
router=kafkacdc
servers=server1
user=maxuser
password=maxpwd
bootstrap_servers=127.0.0.1:9092
topic=my-cdc-topic
match=db1[.]
exclude=db1[.](accounts|users)
```



### `<code>exclude</code>`


* Type: [regex](../mariadb-maxscale-21-06-getting-started/mariadb-maxscale-2106-maxscale-2106-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `<code>""</code>`


Exclude data from tables that match this pattern.


For example, if configured with `<code>exclude=mydb[.].*</code>`, all data from the tables in
the `<code>mydb</code>` database is not sent to Kafka.


The pattern matching works the same way for both of the `<code>exclude</code>` and `<code>match</code>`
parameters. See [match](#match) for an explanation on how the patterns are
matched against the database and table names.


### `<code>cooperative_replication</code>`


* Type: [boolean](../mariadb-maxscale-21-06-getting-started/mariadb-maxscale-2106-maxscale-2106-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `<code>false</code>`


Controls whether multiple instances cooperatively replicate from the same
cluster. This is a boolean parameter and is disabled by default. It was added in
MaxScale 6.0.


When this parameter is enabled and the monitor pointed to by the `<code>cluster</code>`
parameter supports cooperative monitoring (currently only `<code>mariadbmon</code>`), the
replication is only active if the monitor owns the cluster it is monitoring.


Whenever an instance that does not own the cluster gains ownership of the
cluster, the replication will continue from the latest GTID that was delivered
to Kafka.


This means that multiple MaxScale instances can replicate from the same set of
servers and the event is only processed once. This feature does not provide
exactly-once semantics for the Kafka event delivery. However, it does provide
high-availability for the `<code>kafkacdc</code>` instances which allows automated failover
between multiple MaxScale instances.


### `<code>read_gtid_from_kafka</code>`


* Type: [boolean](../mariadb-maxscale-21-06-getting-started/mariadb-maxscale-2106-maxscale-2106-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `<code>true</code>`


On startup, the latest GTID is by default read from the Kafka cluster. This
makes it possible to recover the replication position stored by another
MaxScale. Sometimes this is not desirable and the GTID should only be read from
the local file or started anew. Examples of these are when the GTIDs are reset
or the replication topology has changed.


### `<code>kafka_ssl</code>`


* Type: [boolean](../mariadb-maxscale-21-06-getting-started/mariadb-maxscale-2106-maxscale-2106-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `<code>false</code>`


Enable SSL for Kafka connections. This is a boolean parameter and is disabled by
default.


### `<code>kafka_ssl_ca</code>`


* Type: path
* Mandatory: No
* Dynamic: No
* Default: `<code>""</code>`


Path to the certificate authority file in PEM format. If this is not provided,
the default system certificates will be used.


### `<code>kafka_ssl_cert</code>`


* Type: path
* Mandatory: No
* Dynamic: No
* Default: `<code>""</code>`


Path to the public certificate in PEM format.


The client must provide a certificate if the Kafka server performs authentication
of the client certificates. This feature is enabled by default in Kafka and is
controlled by
[ssl.endpoint.identification.algorithm](https://kafka.apache.org/documentation/#brokerconfigs_ssl.endpoint.identification.algorithm).


If `<code>kafka_ssl_cert</code>` is provided, `<code>kafka_ssl_key</code>` must also be provided.


### `<code>kafka_ssl_key</code>`


* Type: path
* Mandatory: No
* Dynamic: No
* Default: `<code>""</code>`


Path to the private key in PEM format.


If `<code>kafka_ssl_key</code>` is provided, `<code>kafka_ssl_cert</code>` must also be provided.


### `<code>kafka_sasl_user</code>`


* Type: string
* Mandatory: No
* Dynamic: No
* Default: `<code>""</code>`


Username for SASL authentication.


If `<code>kafka_sasl_user</code>` is provided, `<code>kafka_sasl_password</code>` must also be provided.


### `<code>kafka_sasl_password</code>`


* Type: string
* Mandatory: No
* Dynamic: No
* Default: `<code>""</code>`


Password for SASL authentication.


If `<code>kafka_sasl_password</code>` is provided, `<code>kafka_sasl_user</code>` must also be provided.


### `<code>kafka_sasl_mechanism</code>`


* Type: [enum](../mariadb-maxscale-21-06-getting-started/mariadb-maxscale-2106-maxscale-2106-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Values: `<code>PLAIN</code>`, `<code>SCRAM-SHA-256</code>`, `<code>SCRAM-SHA-512</code>`
* Default: `<code>PLAIN</code>`


The SASL mechanism used. The default value is `<code>PLAIN</code>` which uses plaintext
authentication. It is recommended to enable SSL whenever plaintext
authentication is used.


Allowed values are:


* `<code>PLAIN</code>`
* `<code>SCRAM-SHA-256</code>`
* `<code>SCRAM-SHA-512</code>`


The value that should be used depends on the SASL mechanism used by the
Kafka broker.


## Example Configuration


The following configuration defines the minimal setup for streaming replication
events from MariaDB into Kafka as JSON:



```
# The server we're replicating from
[server1]
type=server
address=127.0.0.1
port=3306

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
