
# SQL Server Features Implemented Differently in MariaDB


Modern DBMSs implement several advanced features. While an SQL standard exists, the complete feature list is different for every database system. Sometimes different features allow achieving the same purpose, but with a different logic and different limitations. This is something to take into account when planning a migration.


Some features are implemented by different DBMSs, with a similar logic and similar syntax. But there could be important differences that users should be aware of.


This page has a list of SQL Server features that MariaDB implements in a different way, and SQL Server features for which MariaDB has an alternative feature. Minor differences are not taken into account here. The list is not exhaustive.


## SQL


* The list of supported [data types](../../../../ref/data-types/data-types-overview/data-types-subcategory/data-types-dec.md) is different.
* There are relevant [differences in transaction isolation levels](mariadb-transactions-and-isolation-levels-for-sql-server-users.md#isolation-levels-and-locks).
* `SNAPSHOT` isolation level is not supported. Instead, you can use `START TRANSACTION WITH CONSISTENT SNAPSHOT` to acquire a snapshot at the beginning of the transaction. This is compatible with all isolation levels. See [How Isolation Levels are Implemented in MariaDB](mariadb-transactions-and-isolation-levels-for-sql-server-users.md#how-isolation-levels-are-implemented-in-mariadb).
* JSON support is [different](sql-server-and-mariadb-types-comparison.md#json).


## Indexes and Performance


* Clustered indexes. In MariaDB, the physical order of rows is delegated to the storage engine. InnoDB uses the primary key as a clustered index.
* Hash indexes. Only some storage engines support `HASH` indexes.

  * The [InnoDB](../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/innodb-upgrade-tests/README.md) storage engine has a feature called adaptive hash index, enabled by default. It means that in InnoDB all indexes are created as `BTREE`, and depending on how they are used, InnoDB could convert them from BTree to hash indexes, or the other way around. This happens in the background.
  * The [MEMORY](../../../../ref/storage-engines/memory-storage-engine.md) storage engine uses hash indexes by default, if we don't specify the `BTREE` keyword.
  * See [Storage Engine Index Types](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/optimization-and-indexes/storage-engine-index-types.md) for more information.
* Query store. MariaDB allows query performance analysis using the [slow log](../../../server-monitoring-logs/slow-query-log/slow-query-log-overview.md) and [performance_schema](../../../../ref/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/performance-schema/performance-schema-tables/performance-schema-table_handles-table.md). Some open source or commercial 3rd party tools read that information to produce statistics and make it easy to identify slow queries.


## Tables


* Computed columns are called [generated columns](../../../../ref/sql-statements-and-structure/sql-statements/data-definition/create/generated-columns.md) in MariaDB and are created with a different syntax. See also [Implementation Differences Compared to Microsoft SQL Server](../../../../ref/sql-statements-and-structure/sql-statements/data-definition/create/generated-columns.md#implementation-differences-compared-to-microsoft-sql-server).
* [Temporal tables](../../../../ref/sql-statements-and-structure/temporal-tables/system-versioned-tables.md) use a different (more standard) syntax on MariaDB. In MariaDB, the history is stored in the same table as current data (but optionally in different partitions). MariaDB supports both [SYSTEM_TIME](../../../../ref/sql-statements-and-structure/temporal-tables/system-versioned-tables.md) and [APPLICATION_TIME](../../../../ref/sql-statements-and-structure/temporal-tables/system-versioned-tables.md).
* Hidden columns are [Invisible columns](../../../../ref/sql-statements-and-structure/sql-statements/data-definition/create/invisible-columns.md) in MariaDB.
* [Temporary tables](../../../../ref/sql-statements-and-structure/vectors/create-table-with-vectors.md#create-temporary-table) are implemented and used differently.


## High Availability


* `NOT FOR REPLICATION`

  * MariaDB supports [replication filters](../../../../server-usage/replication-cluster-multi-master/standard-replication/replication-filters.md) to exclude some tables or databases from replication
  * It is possible to keep a table empty in a slave (or in the master) by using the [BLACKHOLE storage engine](../../../../ref/storage-engines/blackhole.md).
  * The master can have columns that are not present in a slave (the other way around is also supported). Before using this feature, carefully read the [Replication When the Master and Slave Have Different Table Definitions](../../../../server-usage/replication-cluster-multi-master/standard-replication/replication-when-the-primary-and-replica-have-different-table-definitions.md) page.
  * With MariaDB it's possible to [prevent a trigger from running on slaves](../../../../server-usage/replication-cluster-multi-master/standard-replication/running-triggers-on-the-replica-for-row-based-events.md).
  * It's possible to run [events](../../../../server-usage/programming-customizing-mariadb/triggers-events/event-scheduler/README.md) without replicating them. The same applies to some administrative statements.
  * MariaDB superusers can run statements without replicating them, by using the [sql_log_bin](../../../../ref/sql-statements-and-structure/sql-statements/administrative-sql-statements/set-commands/set-sql_log_bin.md) system variable.
  * Constraints and triggers cannot be disabled for replication, but it is possible to drop them on the slaves.
  * The `IF EXISTS` syntax allows one to easily create a table on the master that already exists (possibly in a different version) on a slave.
* pollinginterval option. See [Delayed Replication](../../../../server-usage/replication-cluster-multi-master/standard-replication/delayed-replication.md).


## Security


* The list of [permissions](../../../../ref/sql-statements-and-structure/sql-statements/account-management-sql-commands/grant.md#privilege-levels) is different.
* Security policies. MariaDB allows one to achieve the same results by assigning permissions on views and stored procedures. However, this is not a common practice and it's more complicated than defining security policies. See [Other Uses of Views](../../../../../general-resources/learning-and-training/training-and-tutorials/basic-mariadb-articles/creating-using-views.md#other-uses-of-views).
* MariaDB does not support an `OUTPUT` clause. Instead, we can use [DELETE RETURNING](../../../../ref/sql-statements-and-structure/sql-statements/data-manipulation/changing-deleting-data/delete.md) and, since [MariaDB 10.5](../../../../../release-notes/mariadb-community-server/what-is-mariadb-105.md), [INSERT RETURNING](../../../../ref/sql-statements-and-structure/sql-statements/data-manipulation/inserting-loading-data/insertreturning.md) and [REPLACE RETURNING](../../../../ref/sql-statements-and-structure/sql-statements/data-manipulation/changing-deleting-data/replacereturning.md).


## Other Features


* Linked servers. MariaDB supports storage engines to read from, and write to, remote tables. When using the [CONNECT](../../../../../connectors/mariadb-connector-nodejs/connector-nodejs-pipelining.md) engine, those tables could be in different DBMSs, including SQL Server.
* Job scheduler: MariaDB uses an [event scheduler](../../../../server-usage/programming-customizing-mariadb/triggers-events/event-scheduler/README.md) to schedule events instead.


## See Also


* [SQL Server features not available in MariaDB](sql-server-features-not-available-in-mariadb.md)

