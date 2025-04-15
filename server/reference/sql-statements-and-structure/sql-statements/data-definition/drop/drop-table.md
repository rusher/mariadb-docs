
# DROP TABLE

## Syntax


```
DROP [TEMPORARY] TABLE [IF EXISTS] [/*COMMENT TO SAVE*/]
    tbl_name [, tbl_name] ...
    [WAIT n|NOWAIT]
    [RESTRICT | CASCADE]
```


## Description


`<code>DROP TABLE</code>` removes one or more tables. You must have the `<code>DROP</code>` privilege
for each table. All table data and the table definition are removed, as well as [triggers](../../../../../server-usage/programming-customizing-mariadb/triggers-events/triggers/triggers-and-implicit-locks.md) associated to the table, so be
careful with this statement! If any of the tables named in the argument list do
not exist, MariaDB returns an error indicating by name which non-existing tables
it was unable to drop, but it also drops all of the tables in the list that do
exist.


**Important**: When a table is dropped, user privileges on the table are not
automatically dropped. See [GRANT](../../account-management-sql-commands/grant.md).


If another thread is using the table in an explicit transaction or an autocommit transaction, then the thread acquires a [metadata lock (MDL)](../../transactions/metadata-locking.md) on the table. The `<code>DROP TABLE</code>` statement will wait in the "Waiting for table metadata lock" [thread state](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/buffers-caches-and-threads/thread-states/README.md) until the MDL is released. MDLs are released in the following cases:


* If an MDL is acquired in an explicit transaction, then the MDL will be released when the transaction ends.
* If an MDL is acquired in an autocommit transaction, then the MDL will be released when the statement ends.
* Transactional and non-transactional tables are handled the same.


Note that for a partitioned table, `<code>DROP TABLE</code>` permanently removes the table
definition, all of its partitions, and all of the data which was stored in
those partitions. It also removes the partitioning definition (.par) file
associated with the dropped table.


For each referenced table, `<code>DROP TABLE</code>` drops a temporary table with that name, if it exists. If it does not exist, and the `<code>TEMPORARY</code>` keyword is not used, it drops a non-temporary table with the same name, if it exists. The `<code>TEMPORARY</code>` keyword ensures that a non-temporary table will not accidentally be dropped.


Use `<code>IF EXISTS</code>` to prevent an error from occurring for tables that do not
exist. A `<code>NOTE</code>` is generated for each non-existent table when using
`<code>IF EXISTS</code>`. See [SHOW WARNINGS](../../administrative-sql-statements/show/show-warnings.md).


If a [foreign key](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/optimization-and-indexes/foreign-keys.md) references this table, the table cannot be dropped. In this case, it is necessary to drop the foreign key first.


`<code>RESTRICT</code>` and `<code>CASCADE</code>` are allowed to make porting from other database systems easier. In MariaDB, they do nothing.


The comment before the table names (`<code>/*COMMENT TO SAVE*/</code>`) is stored in the [binary log](../../../../storage-engines/innodb/binary-log-group-commit-and-innodb-flushing-performance.md). That feature can be used by replication tools to send their internal messages.


It is possible to specify table names as `<code>db_name</code>`.`<code>tab_name</code>`. This is useful to delete tables from multiple databases with one statement. See [Identifier Qualifiers](../../../sql-language-structure/identifier-qualifiers.md) for details.


The [DROP privilege](../../account-management-sql-commands/grant.md#table-privileges) is required to use `<code>DROP TABLE</code>` on non-temporary tables. For temporary tables, no privilege is required, because such tables are only visible for the current session.


**Note:** `<code>DROP TABLE</code>` automatically commits the current active transaction,
unless you use the `<code>TEMPORARY</code>` keyword.



##### MariaDB starting with [10.5.4](../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1054-release-notes.md)
From [MariaDB 10.5.4](../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1054-release-notes.md), `<code>DROP TABLE</code>` reliably deletes table remnants inside a storage engine even if the `<code>.frm</code>` file is missing. Before then, a missing `<code>.frm</code>` file would result in the statement failing.


### WAIT/NOWAIT


Set the lock wait timeout. See [WAIT and NOWAIT](../../transactions/wait-and-nowait.md).


## DROP TABLE in replication


`<code>DROP TABLE</code>` has the following characteristics in [replication](../../administrative-sql-statements/replication-statements/README.md):


* `<code class="highlight fixed" style="white-space:pre-wrap">DROP TABLE IF EXISTS</code>` are always logged.
* `<code class="highlight fixed" style="white-space:pre-wrap">DROP TABLE</code>` without `<code class="highlight fixed" style="white-space:pre-wrap">IF EXISTS</code>` for tables that don't exist are not written to the [binary log](../../../../storage-engines/innodb/binary-log-group-commit-and-innodb-flushing-performance.md).
* Dropping of `<code class="highlight fixed" style="white-space:pre-wrap">TEMPORARY</code>` tables are prefixed in the log with `<code class="highlight fixed" style="white-space:pre-wrap">TEMPORARY</code>`. These drops are only logged when running [statement](../../../../../server-management/server-monitoring-logs/binary-log/binary-log-formats.md#statement-based) or [mixed mode](../../../../../server-management/server-monitoring-logs/binary-log/binary-log-formats.md#mixed) replication.
* One `<code class="highlight fixed" style="white-space:pre-wrap">DROP TABLE</code>` statement can be logged with up to 3 different `<code class="highlight fixed" style="white-space:pre-wrap">DROP</code>` statements:

  * `<code class="highlight fixed" style="white-space:pre-wrap">DROP TEMPORARY TABLE list_of_non_transactional_temporary_tables</code>`
  * `<code class="highlight fixed" style="white-space:pre-wrap">DROP TEMPORARY TABLE list_of_transactional_temporary_tables</code>`
  * `<code class="highlight fixed" style="white-space:pre-wrap">DROP TABLE list_of_normal_tables</code>`


`<code class="highlight fixed" style="white-space:pre-wrap">DROP TABLE</code>` on the primary is treated on the replica as `<code class="highlight fixed" style="white-space:pre-wrap">DROP TABLE IF EXISTS</code>`. You can change that by setting [slave-ddl-exec-mode](../../../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md) to `<code class="highlight fixed" style="white-space:pre-wrap">STRICT</code>`.


## Dropping an Internal #sql-... Table


From [MariaDB 10.6](../../../../../../release-notes/mariadb-community-server/what-is-mariadb-106.md), [DROP TABLE is atomic](#atomic-drop-table) and the following does not apply. Until [MariaDB 10.5](../../../../../../release-notes/mariadb-community-server/what-is-mariadb-105.md), if the [mariadbd process](../../../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md) is killed during an [ALTER TABLE](../alter/alter-tablespace.md) you may find a table named #sql-... in your data directory. These temporary tables will always be deleted automatically.


If you want to delete one of these tables explicitly you can do so by using the following syntax:


```
DROP TABLE `#mysql50##sql-...`;
```

When running an `<code>ALTER TABLE…ALGORITHM=INPLACE</code>` that rebuilds the table, InnoDB will create an internal `<code>#sql-ib</code>` table.


The same name as the .frm file is used for the intermediate copy of the table. The #sql-ib names are used by TRUNCATE and delayed DROP.


The #sql-ib tables will be deleted automatically.


## Dropping All Tables in a Database


The best way to drop all tables in a database is by executing [DROP DATABASE](drop-database.md), which will drop the database itself, and all tables in it.


However, if you want to drop all tables in the database, but you also want to keep the database itself and any other non-table objects in it, then you would need to execute `<code>DROP TABLE</code>` to drop each individual table. You can construct these `<code>DROP TABLE</code>` commands by querying the [TABLES](../../administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-tables-table.md) table in the [information_schema](../../administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-tablespaces-table.md) database. For example:


```
SELECT CONCAT('DROP TABLE IF EXISTS `', TABLE_SCHEMA, '`.`', TABLE_NAME, '`;')
FROM information_schema.TABLES
WHERE TABLE_SCHEMA = 'mydb';
```

## Atomic DROP TABLE



##### MariaDB starting with [10.6.1](../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-1061-release-notes.md)
From [MariaDB 10.6](../../../../../../release-notes/mariadb-community-server/what-is-mariadb-106.md), `<code>DROP TABLE</code>` for a single table is atomic ([MDEV-25180](https://jira.mariadb.org/browse/MDEV-25180)) for most engines, including InnoDB, MyRocks, MyISAM and Aria.
This means that if there is a crash (server down or power outage) during `<code>DROP TABLE</code>`, all tables
that have been processed so far will be completely dropped, including related trigger files and status entries, and the [binary log](../../../../storage-engines/innodb/binary-log-group-commit-and-innodb-flushing-performance.md) will include a `<code>DROP TABLE</code>` statement for the dropped tables.
Tables for which the drop had not started will be left intact.
In older MariaDB versions, there was a small chance that, during a server crash happening in the middle of `<code>DROP TABLE</code>`, some storage engines that were using multiple storage files, like [MyISAM](../../../../storage-engines/myisam-storage-engine/README.md), could have only a part of its internal files dropped.
In [MariaDB 10.5](../../../../../../release-notes/mariadb-community-server/what-is-mariadb-105.md), `<code>DROP TABLE</code>` was extended to be able to delete a table that was only partly dropped ([MDEV-11412](https://jira.mariadb.org/browse/MDEV-11412)) as explained above. Atomic `<code>DROP TABLE</code>` is the final piece to make `<code>DROP TABLE</code>` fully reliable.
Dropping multiple tables is crash-safe.
See [Atomic DDL](../atomic-ddl.md) for more information.


## Examples


```
DROP TABLE Employees, Customers;
```

## Notes


Beware that `<code>DROP TABLE</code>` can drop both tables and [sequences](../../../sequences/create-sequence.md). This is mainly done to allow old tools like [mariadb-dump](../../../../../clients-and-utilities/backup-restore-and-import-clients/mariadb-dump.md) (previously mysqldump) to work with sequences.


## See Also


* [CREATE TABLE](../../../vectors/create-table-with-vectors.md)
* [ALTER TABLE](../alter/alter-tablespace.md)
* [SHOW CREATE TABLE](../../administrative-sql-statements/show/show-create-table.md)
* [DROP SEQUENCE](../../../sequences/drop-sequence.md)
* Variable [slave-ddl-exec-mode](../../../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md).

