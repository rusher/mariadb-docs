
# Cassandra Status Variables

CassandraSE is no longer actively being developed and has been removed in [MariaDB 10.6](../../../../../release-notes/mariadb-community-server/what-is-mariadb-106.md). See [MDEV-23024](https://jira.mariadb.org/browse/MDEV-23024).




This page documents status variables related to the [Cassandra storage engine](cassandra-storage-engine-issues.md). See [Server Status Variables](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-status-variables.md) for a complete list of status variables that can be viewed with [SHOW STATUS](../../../sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-status.md).


#### `Cassandra_multiget_keys_scanned`


* Description: Number of keys we've made lookups for.
* Scope: Global, Session
* Data Type: `numeric`



#### `Cassandra_multiget_reads`


* Description: Number of read operations.
* Scope: Global, Session
* Data Type: `numeric`



#### `Cassandra_multiget_rows_read`


* Description: Number of rows actually read.
* Scope: Global, Session
* Data Type: `numeric`



#### `Cassandra_network_exceptions`


* Description: Number of network exceptions.
* Scope: Global, Session
* Data Type: `numeric`
* Introduced: `[MariaDB 10.0.3](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-1003-release-notes.md)`



#### `Cassandra_row_insert_batches`


* Description: Number of insert batches performed.
* Scope: Global, Session
* Data Type: `numeric`



#### `Cassandra_row_inserts`


* Description: Number of rows inserted.
* Scope: Global, Session
* Data Type: `numeric`



#### `Cassandra_timeout_exceptions`


* Description: Number of Timeout exceptions we got from Cassandra.
* Scope: Global, Session
* Data Type: `numeric`



#### `Cassandra_unavailable_exceptions`


* Description: Number of Unavailable exceptions we got from Cassandra.
* Scope: Global, Session
* Data Type: `numeric`


