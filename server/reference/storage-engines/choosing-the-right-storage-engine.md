
# Choosing the Right Storage Engine

A high-level overview of the main reasons for choosing a particular storage engine:


## Topic List


### General Purpose


* [InnoDB](innodb/README.md) is a good general transaction storage engine, and the best choice in most cases. It is the default storage engine.
* [Aria](aria/README.md), MariaDB's more modern improvement on [MyISAM](myisam-storage-engine/README.md), has a small footprint and allows for easy copying between systems.
* [MyISAM](myisam-storage-engine/README.md) has a small footprint and allows for easy copying between systems. MyISAM is MySQL's oldest storage engine. There is usually little reason to use it except for legacy purposes. Aria is MariaDB's more modern improvement.
* [XtraDB](innodb/README.md) is no longer available. It was a performance-enhanced fork of InnoDB and was MariaDB's default engine until [MariaDB 10.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-1-series/changes-improvements-in-mariadb-10-1).


### Scaling, Partitioning


When you want to split your database load on several servers or optimize for scaling. We also suggest looking at [Galera](/kb/en/galera/), a synchronous multi-master cluster.


* [Spider](spider/README.md) uses partitioning to provide data sharding through multiple servers.
* [ColumnStore](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/columnstore/) utilizes a massively parallel distributed data architecture and is designed for big data scaling to process petabytes of data.
* The [MERGE](merge.md) storage engine is a collection of identical [MyISAM](myisam-storage-engine/README.md) tables that can be used as one. "Identical" means that all tables have identical column and index information.
* [TokuDB](tokudb/README.md) is a transactional storage engine which is optimized for workloads that do not fit in memory, and provides a good compression ratio. TokuDB has been deprecated by its upstream developers, and is disabled in [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-5-series/what-is-mariadb-105), and removed in [MariaDB 10.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-6-series/what-is-mariadb-106)


### Compression / Archive


* [MyRocks](myrocks/README.md) enables greater compression than InnoDB, as well as less write amplification giving better endurance of flash storage and improving overall throughput.
* The [Archive](archive/README.md) storage engine is, unsurprisingly, best used for archiving.
* [TokuDB](tokudb/README.md) is a transactional storage engine which is optimized for workloads that do not fit in memory, and provides a good compression ratio. TokuDB has been deprecated by its upstream developers, and is disabled in [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-5-series/what-is-mariadb-105), and removed in [MariaDB 10.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-6-series/what-is-mariadb-106)


### Connecting to Other Data Sources


When you want to use data not stored in a MariaDB database.


* [CONNECT](connect/README.md) allows access to different kinds of text files and remote resources as if they were regular MariaDB tables.
* The [CSV](csv/README.md) storage engine can read and append to files stored in CSV (comma-separated-values) format. However, since [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0), CONNECT is a better choice and is more flexibly able to read and write such files.
* [FederatedX](federatedx-storage-engine/README.md) uses libmysql to talk to the data source, the data source being a remote RDBMS. Currently, since FederatedX only uses libmysql, it can only talk to another MySQL RDBMS.
* [CassandraSE](legacy-storage-engines/cassandra/README.md) is a storage engine allowing access to an older version of Apache Cassandra NoSQL DBMS. It was relatively experimental, is no longer being actively developed and has been removed in [MariaDB 10.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-6-series/what-is-mariadb-106).


### Search Optimized


Search engines optimized for search.


* [SphinxSE](sphinx-storage-engine/README.md) is used as a proxy to run statements on a remote Sphinx database server (mainly useful for advanced fulltext searches).
* [Mroonga](mroonga/README.md) provides fast CJK-ready full text searching using column store.


### Cache, Read-only


* [MEMORY](memory-storage-engine.md) does not write data on-disk (all rows are lost on crash) and is best-used for read-only caches of data from other tables, or for temporary work areas. With the default [InnoDB](innodb/README.md) and other storage engines having good caching, there is less need for this engine than in the past.


### Other Specialized Storage Engines


* [S3 Storage Engine](s3-storage-engine/README.md) is a read-only storage engine that stores its data in Amazon S3.
* [Sequence](sequence-storage-engine.md) allows the creation of ascending or descending sequences of numbers (positive integers) with a given starting value, ending value and increment, creating virtual, ephemeral tables automatically when you need them.
* The [BLACKHOLE](blackhole.md) storage engine accepts data but does not store it and always returns an empty result. This can be useful in [replication](../../server-usage/replication-cluster-multi-master/README.md) environments, for example, if you want to run complex filtering rules on a slave without incurring any overhead on a master.
* [OQGRAPH](oqgraph-storage-engine/README.md) allows you to handle hierarchies (tree structures) and complex graphs (nodes having many connections in several directions).


## Alphabetical List


* The [Archive](archive/README.md) storage engine is, unsurprisingly, best used for archiving.
* [Aria](aria/README.md), MariaDB's more modern improvement on MyISAM, has a small footprint and allows for easy copy between systems.
* The [BLACKHOLE](blackhole.md) storage engine accepts data but does not store it and always returns an empty result. This can be useful in [replication](../../server-usage/replication-cluster-multi-master/README.md) environments, for example, if you want to run complex filtering rules on a slave without incurring any overhead on a master.
* [CassandraSE](legacy-storage-engines/cassandra/README.md) is a storage engine allowing access to an older version of Apache Cassandra NoSQL DBMS. It was relatively experimental, is no longer being actively developed and has been removed in [MariaDB 10.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-6-series/what-is-mariadb-106).
* [ColumnStore](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/columnstore/) utilizes a massively parallel distributed data architecture and is designed for big data scaling to process petabytes of data.
* [CONNECT](connect/README.md) allows access to different kinds of text files and remote resources as if they were regular MariaDB tables.
* The [CSV](csv/csv-overview.md) storage engine can read and append to files stored in CSV (comma-separated-values) format. However, since [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0), CONNECT is a better choice and is more flexibly able to read and write such files.
* [FederatedX](federatedx-storage-engine/README.md) uses libmysql to talk to the data source, the data source being a remote RDBMS. Currently, since FederatedX only uses libmysql, it can only talk to another MySQL RDBMS.
* [InnoDB](innodb/README.md) is a good general transaction storage engine, and the best choice in most cases. It is the default storage engine.
* The [MERGE](merge.md) storage engine is a collection of identical MyISAM tables that can be used as one. "Identical" means that all tables have identical column and index information.
* [MEMORY](memory-storage-engine.md) does not write data on-disk (all rows are lost on crash) and is best-used for read-only caches of data from other tables, or for temporary work areas. With the default [InnoDB](innodb/README.md) and other storage engines having good caching, there is less need for this engine than in the past.
* [Mroonga](mroonga/README.md) provides fast CJK-ready full text searching using column store.
* [MyISAM](myisam-storage-engine/README.md) has a small footprint and allows for easy copying between systems. MyISAM is MySQL's oldest storage engine. There is usually little reason to use it except for legacy purposes. Aria is MariaDB's more modern improvement.
* [MyRocks](myrocks/README.md) enables greater compression than InnoDB, as well as less write amplification giving better endurance of flash storage and improving overall throughput.
* [OQGRAPH](oqgraph-storage-engine/README.md) allows you to handle hierarchies (tree structures) and complex graphs (nodes having many connections in several directions).
* [S3 Storage Engine](s3-storage-engine/README.md) is a read-only storage engine that stores its data in Amazon S3.
* [Sequence](sequence-storage-engine.md) allows the creation of ascending or descending sequences of numbers (positive integers) with a given starting value, ending value and increment, creating virtual, ephemeral tables automatically when you need them.
* [SphinxSE](sphinx-storage-engine/README.md) is used as a proxy to run statements on a remote Sphinx database server (mainly useful for advanced fulltext searches).
* [Spider](spider/README.md) uses partitioning to provide data sharding through multiple servers.
* [TokuDB](tokudb/README.md) is a transactional storage engine which is optimized for workloads that do not fit in memory, and provides a good compression ratio. TokuDB has been deprecated by its upstream developers, and is disabled in [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-5-series/what-is-mariadb-105), and removed in [MariaDB 10.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-6-series/what-is-mariadb-106)
* [XtraDB](innodb/README.md) is no longer available. It was a performance-enhanced fork of InnoDB and was MariaDB's default engine until [MariaDB 10.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-1-series/changes-improvements-in-mariadb-10-1).


CC BY-SA / Gnu FDL

