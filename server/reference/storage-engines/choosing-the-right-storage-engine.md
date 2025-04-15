
# Choosing the Right Storage Engine

A high-level overview of the main reasons for choosing a particular storage engine:


## Topic List


### General Purpose


* [InnoDB](../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/innodb-upgrade-tests/README.md) is a good general transaction storage engine, and the best choice in most cases. It is the default storage engine.
* [Aria](s3-storage-engine/aria_s3_copy.md), MariaDB's more modern improvement on [MyISAM](myisam-storage-engine/myisam-system-variables.md), has a small footprint and allows for easy copying between systems.
* [MyISAM](myisam-storage-engine/myisam-system-variables.md) has a small footprint and allows for easy copying between systems. MyISAM is MySQL's oldest storage engine. There is usually little reason to use it except for legacy purposes. Aria is MariaDB's more modern improvement.
* [XtraDB](../../server-usage/replication-cluster-multi-master/standard-replication/obsolete-replication-information/xtradb-option-innodb-release-locks-early.md) is no longer available. It was a performance-enhanced fork of InnoDB and was MariaDB's default engine until [MariaDB 10.1](../../../release-notes/mariadb-community-server/what-is-mariadb-1010.md).


### Scaling, Partitioning


When you want to split your database load on several servers or optimize for scaling. We also suggest looking at [Galera](../sql-statements-and-structure/sql-statements/built-in-functions/special-functions/galera-functions/README.md), a synchronous multi-master cluster.


* [Spider](spider/spider-functions/spider_copy_tables.md) uses partitioning to provide data sharding through multiple servers.
* [ColumnStore](../../../columnstore/columnstore-data-ingestion/columnstore-remote-bulk-data-import-mcsimport.md) utilizes a massively parallel distributed data architecture and is designed for big data scaling to process petabytes of data.
* The [MERGE](merge.md) storage engine is a collection of identical [MyISAM](myisam-storage-engine/myisam-system-variables.md) tables that can be used as one. "Identical" means that all tables have identical column and index information.
* [TokuDB](tokudb/tokudb-resources.md) is a transactional storage engine which is optimized for workloads that do not fit in memory, and provides a good compression ratio. TokuDB has been deprecated by its upstream developers, and is disabled in [MariaDB 10.5](../../../release-notes/mariadb-community-server/what-is-mariadb-105.md), and removed in [MariaDB 10.6](../../../release-notes/mariadb-community-server/what-is-mariadb-106.md)


### Compression / Archive


* [MyRocks](myrocks/myrocks-in-mariadb-102-vs-mariadb-103.md) enables greater compression than InnoDB, as well as less write amplification giving better endurance of flash storage and improving overall throughput.
* The [Archive](archive/README.md) storage engine is, unsurprisingly, best used for archiving.
* [TokuDB](tokudb/tokudb-resources.md) is a transactional storage engine which is optimized for workloads that do not fit in memory, and provides a good compression ratio. TokuDB has been deprecated by its upstream developers, and is disabled in [MariaDB 10.5](../../../release-notes/mariadb-community-server/what-is-mariadb-105.md), and removed in [MariaDB 10.6](../../../release-notes/mariadb-community-server/what-is-mariadb-106.md)


### Connecting to Other Data Sources


When you want to use data not stored in a MariaDB database.


* [CONNECT](../../../connectors/mariadb-connector-nodejs/connector-nodejs-pipelining.md) allows access to different kinds of text files and remote resources as if they were regular MariaDB tables.
* The [CSV](csv/csv-overview.md) storage engine can read and append to files stored in CSV (comma-separated-values) format. However, since [MariaDB 10.0](../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md), CONNECT is a better choice and is more flexibly able to read and write such files.
* [FederatedX](federatedx-storage-engine/README.md) uses libmysql to talk to the data source, the data source being a remote RDBMS. Currently, since FederatedX only uses libmysql, it can only talk to another MySQL RDBMS.
* [CassandraSE](legacy-storage-engines/cassandra/cassandra-storage-engine-issues.md) is a storage engine allowing access to an older version of Apache Cassandra NoSQL DBMS. It was relatively experimental, is no longer being actively developed and has been removed in [MariaDB 10.6](../../../release-notes/mariadb-community-server/what-is-mariadb-106.md).


### Search Optimized


Search engines optimized for search.


* [SphinxSE](sphinx-storage-engine/README.md) is used as a proxy to run statements on a remote Sphinx database server (mainly useful for advanced fulltext searches).
* [Mroonga](mroonga/mroonga-user-defined-functions/mroonga_snippet_html.md) provides fast CJK-ready full text searching using column store.


### Cache, Read-only


* [MEMORY](memory-storage-engine.md) does not write data on-disk (all rows are lost on crash) and is best-used for read-only caches of data from other tables, or for temporary work areas. With the default [InnoDB](../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/innodb-upgrade-tests/README.md) and other storage engines having good caching, there is less need for this engine than in the past.


### Other Specialized Storage Engines


* [S3 Storage Engine](s3-storage-engine/s3-storage-engine-status-variables.md) is a read-only storage engine that stores its data in Amazon S3.
* [Sequence](sequence-storage-engine.md) allows the creation of ascending or descending sequences of numbers (positive integers) with a given starting value, ending value and increment, creating virtual, ephemeral tables automatically when you need them.
* The [BLACKHOLE](blackhole.md) storage engine accepts data but does not store it and always returns an empty result. This can be useful in [replication](../sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/README.md) environments, for example, if you want to run complex filtering rules on a slave without incurring any overhead on a master.
* [OQGRAPH](oqgraph-storage-engine/oqgraph-examples.md) allows you to handle hierarchies (tree structures) and complex graphs (nodes having many connections in several directions).


## Alphabetical List


* The [Archive](archive/README.md) storage engine is, unsurprisingly, best used for archiving.
* [Aria](s3-storage-engine/aria_s3_copy.md), MariaDB's more modern improvement on MyISAM, has a small footprint and allows for easy copy between systems.
* The [BLACKHOLE](blackhole.md) storage engine accepts data but does not store it and always returns an empty result. This can be useful in [replication](../sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/README.md) environments, for example, if you want to run complex filtering rules on a slave without incurring any overhead on a master.
* [CassandraSE](legacy-storage-engines/cassandra/cassandra-storage-engine-issues.md) is a storage engine allowing access to an older version of Apache Cassandra NoSQL DBMS. It was relatively experimental, is no longer being actively developed and has been removed in [MariaDB 10.6](../../../release-notes/mariadb-community-server/what-is-mariadb-106.md).
* [ColumnStore](../../../columnstore/columnstore-data-ingestion/columnstore-remote-bulk-data-import-mcsimport.md) utilizes a massively parallel distributed data architecture and is designed for big data scaling to process petabytes of data.
* [CONNECT](../../../connectors/mariadb-connector-nodejs/connector-nodejs-pipelining.md) allows access to different kinds of text files and remote resources as if they were regular MariaDB tables.
* The [CSV](csv/csv-overview.md) storage engine can read and append to files stored in CSV (comma-separated-values) format. However, since [MariaDB 10.0](../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md), CONNECT is a better choice and is more flexibly able to read and write such files.
* [FederatedX](federatedx-storage-engine/README.md) uses libmysql to talk to the data source, the data source being a remote RDBMS. Currently, since FederatedX only uses libmysql, it can only talk to another MySQL RDBMS.
* [InnoDB](../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/innodb-upgrade-tests/README.md) is a good general transaction storage engine, and the best choice in most cases. It is the default storage engine.
* The [MERGE](merge.md) storage engine is a collection of identical MyISAM tables that can be used as one. "Identical" means that all tables have identical column and index information.
* [MEMORY](memory-storage-engine.md) does not write data on-disk (all rows are lost on crash) and is best-used for read-only caches of data from other tables, or for temporary work areas. With the default [InnoDB](../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/innodb-upgrade-tests/README.md) and other storage engines having good caching, there is less need for this engine than in the past.
* [Mroonga](mroonga/mroonga-user-defined-functions/mroonga_snippet_html.md) provides fast CJK-ready full text searching using column store.
* [MyISAM](myisam-storage-engine/myisam-system-variables.md) has a small footprint and allows for easy copying between systems. MyISAM is MySQL's oldest storage engine. There is usually little reason to use it except for legacy purposes. Aria is MariaDB's more modern improvement.
* [MyRocks](myrocks/myrocks-in-mariadb-102-vs-mariadb-103.md) enables greater compression than InnoDB, as well as less write amplification giving better endurance of flash storage and improving overall throughput.
* [OQGRAPH](oqgraph-storage-engine/oqgraph-examples.md) allows you to handle hierarchies (tree structures) and complex graphs (nodes having many connections in several directions).
* [S3 Storage Engine](s3-storage-engine/s3-storage-engine-status-variables.md) is a read-only storage engine that stores its data in Amazon S3.
* [Sequence](sequence-storage-engine.md) allows the creation of ascending or descending sequences of numbers (positive integers) with a given starting value, ending value and increment, creating virtual, ephemeral tables automatically when you need them.
* [SphinxSE](sphinx-storage-engine/README.md) is used as a proxy to run statements on a remote Sphinx database server (mainly useful for advanced fulltext searches).
* [Spider](spider/spider-functions/spider_copy_tables.md) uses partitioning to provide data sharding through multiple servers.
* [TokuDB](tokudb/tokudb-resources.md) is a transactional storage engine which is optimized for workloads that do not fit in memory, and provides a good compression ratio. TokuDB has been deprecated by its upstream developers, and is disabled in [MariaDB 10.5](../../../release-notes/mariadb-community-server/what-is-mariadb-105.md), and removed in [MariaDB 10.6](../../../release-notes/mariadb-community-server/what-is-mariadb-106.md)
* [XtraDB](../../server-usage/replication-cluster-multi-master/standard-replication/obsolete-replication-information/xtradb-option-innodb-release-locks-early.md) is no longer available. It was a performance-enhanced fork of InnoDB and was MariaDB's default engine until [MariaDB 10.1](../../../release-notes/mariadb-community-server/what-is-mariadb-1010.md).

