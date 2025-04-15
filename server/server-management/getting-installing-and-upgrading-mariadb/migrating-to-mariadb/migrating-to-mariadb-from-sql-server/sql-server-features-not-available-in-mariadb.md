
# SQL Server Features Not Available in MariaDB


When planning a migration between different DBMSs, one of the most important aspects to consider is that the new database system will probably miss some features supported by the old one. This is not relevant for all users. The most widely used features are supported by most DBMSs. However, it is important to make a list of unsupported features and check which of them are currently used by applications. In most cases it is possible to implement such features on the application side, or simply stop using them.


This page has a list of SQL Server features that are not supported in MariaDB. The list is not exhaustive.


## Introduced in SQL Server versions older than 2016


* Full outer joins.
* `<code>GROUP BY CUBE</code>` syntax.
* `<code>MERGE</code>` statement.
* In MariaDB, indexes are always ascending. Defining them as `<code>ASC</code>` or `<code>DESC</code>` has no effect.

  * For single-column indexes, the performance difference between an `<code>ORDER BY ... ASC</code>` and `<code>DESC</code>` is negligible.
  * For multiple-column indexes, an index may be unusable for certain queries because `<code>DESC</code>` is not supported. In some cases, a [generated column](../../../../reference/sql-statements-and-structure/sql-statements/data-definition/create/generated-columns.md) can be used to invert the order of an index (for example, the expression `<code>0 - price</code>` can be indexed to index the prices in a descending order).
* The [WITH](../../../../reference/sql-statements-and-structure/geographic-geometric-features/geometry-relations/within.md) syntax is currently only supported for the `<code>SELECT</code>` statement.
* Filtered indexes (`<code>CREATE INDEX ... WHERE</code>`).
* Autonomous transactions.
* User-defined types.
* Rules.
* [Triggers](../../../../server-usage/programming-customizing-mariadb/triggers-events/triggers/triggers-and-implicit-locks.md) don't support the following features:

  * Triggers on DDL and login.
  * `<code>INSTEAD OF</code>` triggers.
  * The `<code>DISABLE TRIGGER</code>` syntax.
* [Cursors](../../../../server-usage/programming-customizing-mariadb/programmatic-compound-statements/programmatic-compound-statements-cursors/README.md) advanced features.

  * Global cursors.
  * `<code>DELETE ... CURRENT OF</code>`, `<code>UPDATE ... CURRENT OF</code>` statements: MariaDB cursors are read-only.
  * Specifying a direction (MariaDB cursors can only advance by one row).
* Synonyms.
* Table variables.
* Queues.
* XML indexes, XML schema collection, XQuery.
* User access to system functionalities, for example:

  * Running system commands (`<code>xp_cmdshell()</code>`).
  * Sending emails (`<code>sp_send_dbmail()</code>`).
  * Sending HTTP requests.
* External languages, external libraries (MariaDB only supports procedural SQL and PL/SQL).
* Negative permissions (the `<code>DENY</code>` command).
* Snapshot replication. See [Provisioning a Slave](mariadb-replication-overview-for-sql-server-users.md#provisioning-a-slave).


## Introduced in SQL Server 2016


* Native data masking
* PolyBase (however, [MariaDB 10.5](../../../../../release-notes/mariadb-community-server/what-is-mariadb-105.md) supports accessing Amazon S3 via the [S3 storage engine](../../../../reference/storage-engines/s3-storage-engine/s3-storage-engine-status-variables.md) and several DBMSs via [CONNECT](../../../../../connectors/mariadb-connector-nodejs/connector-nodejs-pipelining.md))
* R and Python services
* ColumnStore indexes. MariaDB has a storage engine called [ColumnStore](../../../../../columnstore/using-mariadb-columnstore/mariadb-columnstore-with-spark.md), but this is a completely different feature.


## Introduced in SQL Server 2017


* Adaptive joins
* Graph SQL


## See Also


* [SQL Server Features Implemented Differently in MariaDB](sql-server-features-implemented-differently-in-mariadb.md)

