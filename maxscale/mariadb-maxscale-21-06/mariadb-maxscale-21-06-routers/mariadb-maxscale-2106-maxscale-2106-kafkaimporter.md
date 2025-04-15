
# MaxScale 21.06 KafkaImporter

# KafkaImporter




* [KafkaImporter](#kafkaimporter)

  * [Overview](#overview)

    * [Required Grants](#required-grants)
  * [Parameters](#parameters)

    * [bootstrap_servers](#bootstrap_servers)
    * [topics](#topics)
    * [batch_size](#batch_size)
    * [kafka_sasl_mechanism](#kafka_sasl_mechanism)
    * [kafka_sasl_user](#kafka_sasl_user)
    * [kafka_sasl_password](#kafka_sasl_password)
    * [kafka_ssl](#kafka_ssl)
    * [kafka_ssl_ca](#kafka_ssl_ca)
    * [kafka_ssl_cert](#kafka_ssl_cert)
    * [kafka_ssl_key](#kafka_ssl_key)
    * [table_name_in](#table_name_in)
    * [timeout](#timeout)
  * [Limitations](#limitations)




## Overview


The KafkaImporter module reads messages from Kafka and streams them into a
MariaDB server. The messages are inserted into a table designated by either the
topic name or the message key (see [table_name_in](#table_name_in) for
details). The table will be automatically created with the following SQL:



```
CREATE TABLE IF NOT EXISTS my_table (
  data LONGTEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  id VARCHAR(1024) AS (JSON_EXTRACT(data, '$._id')) UNIQUE KEY,
  CONSTRAINT data_is_json CHECK(JSON_VALID(data))
);
```



The payload of the message is inserted into the `<code>data</code>` field from which the `<code>id</code>`
field is calculated. The payload must be a valid JSON object and it must either
contain a unique `<code>_id</code>` field or it must not exist or the value must be a JSON
null. This is similar to the MongoDB document format where the `<code>_id</code>` field is
the primary key of the document collection.


If a message is read from Kafka and the insertion into the table fails due to a
violation of one of the constraints, the message is ignored. Similarly, messages
with duplicate `<code>_id</code>` value are also ignored: this is done to avoid inserting the
same document multiple times whenever the connection to either Kafka or MariaDB
is lost.


The limitations on the data can be removed by either creating the table before
the KafkaImporter is started, in which case the `<code>CREATE TABLE IF NOT EXISTS</code>`
does nothing, or by altering the structure of the existing table. The minimum
requirement that must be met is that the table contains the `<code>data</code>` field to
which string values can be inserted into.


The database server where the data is inserted is chosen from the set of servers
available to the service. The first server labeled as the Master with the best
rank will be chosen. This means that a monitor must be configured for the
MariaDB server where the data is to be inserted.


In MaxScale versions 21.06.18, 22.08.15, 23.02.12, 23.08.8, 24.02.4 and 24.08.2
the `<code>_id</code>` field is not required to be present. Older versions of MaxScale used
the following SQL where the `<code>_id</code>` field was mandatory:



```
CREATE TABLE IF NOT EXISTS my_table (
  data LONGTEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  id VARCHAR(1024) AS (JSON_EXTRACT(data, '$._id')) UNIQUE KEY,
  CONSTRAINT data_is_json CHECK(JSON_VALID(data)),
  CONSTRAINT id_is_not_null CHECK(JSON_EXTRACT(data, '$._id') IS NOT NULL)
);
```



### Required Grants


The user defined by the `<code>user</code>` parameter of the service must have `<code>INSERT</code>` and
`<code>CREATE</code>` privileges on all tables that are created.


## Parameters


### `<code>bootstrap_servers</code>`


* Type: string
* Mandatory: Yes
* Dynamic: Yes


The list of Kafka brokers as a CSV list in `<code>host:port</code>` format.


### `<code>topics</code>`


* Type: stringlist
* Mandatory: Yes
* Dynamic: Yes


The comma separated list of topics to subscribe to.


### `<code>batch_size</code>`


* Type: count
* Mandatory: No
* Dynamic: Yes
* Default: `<code>100</code>`


Maximum number of uncommitted records. The KafkaImporter will buffer records
into batches and commit them once either enough records are gathered (controlled
by this parameter) or when the KafkaImporter goes idle. Any uncommitted records
will be read again if a reconnection to either Kafka or MariaDB occurs.


### `<code>kafka_sasl_mechanism</code>`


* Type: [enum](../mariadb-maxscale-21-06-getting-started/mariadb-maxscale-2106-maxscale-2106-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `<code>PLAIN</code>`, `<code>SCRAM-SHA-256</code>`, `<code>SCRAM-SHA-512</code>`
* Default: `<code>PLAIN</code>`


SASL mechanism to use. The Kafka broker must be configured with the same
authentication scheme.


### `<code>kafka_sasl_user</code>`


* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `<code>""</code>`


SASL username used for authentication. If this parameter is defined,
`<code>kafka_sasl_password</code>` must also be provided.


### `<code>kafka_sasl_password</code>`


* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `<code>""</code>`


SASL password for the user. If this parameter is defined, `<code>kafka_sasl_user</code>` must
also be provided.


### `<code>kafka_ssl</code>`


* Type: [boolean](../mariadb-maxscale-21-06-getting-started/mariadb-maxscale-2106-maxscale-2106-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `<code>false</code>`


Enable SSL for Kafka connections.


### `<code>kafka_ssl_ca</code>`


* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: `<code>""</code>`


SSL Certificate Authority file in PEM format. If this parameter is not
defined, the system default CA certificate is used.


### `<code>kafka_ssl_cert</code>`


* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: `<code>""</code>`


SSL public certificate file in PEM format. If this parameter is defined,
`<code>kafka_ssl_key</code>` must also be provided.


### `<code>kafka_ssl_key</code>`


* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: `<code>""</code>`


SSL private key file in PEM format. If this parameter is defined,
`<code>kafka_ssl_cert</code>` must also be provided.


### `<code>table_name_in</code>`


* Type: [enum](../mariadb-maxscale-21-06-getting-started/mariadb-maxscale-2106-maxscale-2106-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `<code>topic</code>`, `<code>key</code>`
* Default: `<code>topic</code>`


The Kafka message part that is used to locate the table to insert the data into.


Enumeration Values:


* `<code>topic</code>`: The topic named is used as the fully qualified table name.
* `<code>key</code>`: The message key is used as the fully qualified table name. If the Kafka
 message does not have a key, the message is ignored.


For example, all messages with a fully qualified table name of `<code>my_db.my_table</code>`
will be inserted into the table `<code>my_table</code>` located in the `<code>my_db</code>` database. If
the table or database names have special characters that must be escaped to make
them valid identifiers, the name must also contain those escape characters. For
example, to insert into a table named `<code>my table</code>` in the database `<code>my database</code>`,
the name would be:



```
`my database`.`my table`
```



### `<code>timeout</code>`


* Type: [duration](../mariadb-maxscale-21-06-getting-started/mariadb-maxscale-2106-maxscale-2106-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `<code>5000ms</code>`


Timeout for both Kafka and MariaDB network communication.


## Limitations


* The backend servers used by this service must be MariaDB version 10.2 or
 newer.
