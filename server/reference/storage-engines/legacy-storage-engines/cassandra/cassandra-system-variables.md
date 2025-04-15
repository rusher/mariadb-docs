
# Cassandra System Variables

CassandraSE is no longer actively being developed and has been removed in [MariaDB 10.6](../../../../../release-notes/mariadb-community-server/what-is-mariadb-106.md). See [MDEV-23024](https://jira.mariadb.org/browse/MDEV-23024).



This page documents system variables related to the [Cassandra storage engine](cassandra-storage-engine-issues.md). See [Server System Variables](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md) for a complete list of system variables and instructions on setting them.


#### `<code>cassandra_default_thrift_host</code>`


* Description: Host to connect to, if not specified on per-table basis.
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>string</code>`



#### `<code>cassandra_failure_retries</code>`


* Description: Number of times to retry on timeout/unavailable failures.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>3</code>`
* Valid Values: `<code>1</code>` to `<code>1073741824</code>`



#### `<code>cassandra_insert_batch_size</code>`


* Description: INSERT batch size.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>100</code>`
* Valid Values: `<code>1</code>` to `<code>1073741824</code>`



#### `<code>cassandra_multiget_batch_size</code>`


* Description: Batched Key Access batch size.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>100</code>`
* Valid Values: `<code>1</code>` to `<code>1073741824</code>`



#### `<code>cassandra_read_consistency</code>`


* Description: Consistency to use for reading. See [Datastax's documentation](https://www.datastax.com/documentation/cassandra/2.0/cassandra/dml/dml_config_consistency_c.html) for details.
* Scope: Global, Session
* Default Value: `<code>ONE</code>`
* Valid Values: `<code>ONE</code>`, `<code>TWO</code>`, `<code>THREE</code>`, `<code>ANY</code>`, `<code>ALL</code>`, `<code>QUORUM</code>`, `<code>EACH_QUORUM</code>`, `<code>LOCAL_QUORUM</code>`, `<code>
</code>`



#### `<code>cassandra_rnd_batch_size</code>`


* Description: Full table scan batch size.
* Scope: Global, Session
* Default Value: `<code>10000</code>`
* Valid Values: `<code>1</code>` to `<code>1073741824</code>`



#### `<code>cassandra_write_consistency</code>`


* Description: Consistency to use for writing. See [Datastax's documentation](https://www.datastax.com/documentation/cassandra/2.0/cassandra/dml/dml_config_consistency_c.html) for details.
* Scope: Global, Session
* Default Value: `<code>ONE</code>`
* Valid Values: `<code>ONE</code>`, `<code>TWO</code>`, `<code>THREE</code>`, `<code>ANY</code>`, `<code>ALL</code>`, `<code>QUORUM</code>`, `<code>EACH_QUORUM</code>`, `<code>LOCAL_QUORUM</code>`, `<code>
</code>`


