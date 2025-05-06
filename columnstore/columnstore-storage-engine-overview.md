
# ColumnStore Storage Engine Overview


# Overview


[MariaDB Enterprise ColumnStore](/en/mariadb-columnstore/) integrates with MariaDB Enterprise Server using the ColumnStore storage engine plugin. The ColumnStore storage engine plugin enables MariaDB Enterprise Server to interact with ColumnStore tables.


For deployment instructions and available documentation, see "[MariaDB Enterprise ColumnStore](/en/mariadb-columnstore/)".


Feature Summary
The ColumnStore storage engine has the following features:



| Feature | Detail | Resources |
| --- | --- | --- |
| Feature | Detail | Resources |
| Storage Engine | ColumnStore |  |
| Availability | ES 10.5+, CS 10.5+ | [MariaDB Enterprise Server](/en/mariadb-enterprise-server/) |
| Workload Optimization | OLAP and Hybrid | [OLAP Workloads](https://mariadb.com/kb/en/mariadb-enterprise-columnstore-storage-architecture/#olap-workloads) [Hybrid Workloads](https://mariadb.com/kb/en/mariadb-enterprise-columnstore-storage-architecture/#hybrid-workloads) |
| Table Orientation | Columnar | [Columnar Storage Engine](https://mariadb.com/kb/en/mariadb-enterprise-columnstore-storage-architecture/#overview) |
| ACID-compliant | Yes |  |
| Indexes | Unnecessary | [Extent Elimination](columnstore-architecture/mariadb-enterprise-columnstore-query-evaluation.md#extent-elimination) |
| Compression | Yes | [Compression](https://mariadb.com/kb/en/mariadb-enterprise-columnstore-storage-architecture/#compression) |
| High Availability (HA) | Yes | [High Availability and Failover](https://mariadb.com/kb/en/columnstore-architecture-from-enterprise-docs/#high-availability-and-failover) |
| Main Memory Caching | Yes |  |
| Transaction Logging | Yes | [Version Buffer](https://mariadb.com/kb/en/mariadb-enterprise-columnstore-storage-architecture/#version-buffer) |
| Garbage Collection | Yes | [Version Buffer](mariadb-enterprise-columnstore-storage-architecture/#version-buffer) |
| Online Schema changes | Yes | [Online Schema Changes](columnstore-architecture/mariadb-enterprise-columnstore-locking.md#online-schema-changes) |
| Non-locking Reads | Yes | [Lockless Reads](columnstore-architecture/mariadb-enterprise-columnstore-locking.md#lockless-reads) |



# Examples


## Creating a ColumnStore Table


To create a ColumnStore table, use the [CREATE TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/data-definition/create/create-table) statement with the `ENGINE=ColumnStore` option:


```
CREATE DATABASE columnstore_db;

CREATE TABLE columnstore_db.analytics_test (
   id INT,
   str VARCHAR(50)
) ENGINE = ColumnStore;
```

## Multi-Node Configuration


To deploy a multi-node Enterprise ColumnStore deployment, a configuration similar to below is required:


```
[mariadb]
log_error                              = mariadbd.err
character_set_server                   = utf8
collation_server                       = utf8_general_ci
log_bin                                = mariadb-bin
log_bin_index                          = mariadb-bin.index
relay_log                              = mariadb-relay
relay_log_index                        = mariadb-relay.index
log_slave_updates                      = ON
gtid_strict_mode                       = ON

# This must be unique on each cluster node
server_id                              = 1
```

## Configure the Mandatory Utility User Account


To configure the mandatory utility user account, use the mcsSetConfig command:


```
$ sudo mcsSetConfig CrossEngineSupport Host 127.0.0.1
$ sudo mcsSetConfig CrossEngineSupport Port 3306
$ sudo mcsSetConfig CrossEngineSupport User cross_engine
$ sudo mcsSetConfig CrossEngineSupport Password cross_engine_passwd
```


Copyright © 2025 MariaDB

