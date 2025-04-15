
# FLUSH TABLES FOR EXPORT

## Syntax


```
FLUSH TABLE[S] table_name [, table_name] FOR EXPORT
```


## Description


`<code>FLUSH TABLES ... FOR EXPORT</code>` flushes changes to the specified tables to disk so that binary copies can be made while the server is still running. This works for [Archive](../../../../storage-engines/archive/README.md), [Aria](../../../../storage-engines/s3-storage-engine/aria_s3_copy.md), [CSV](../../../../storage-engines/csv/csv-overview.md), [InnoDB](../../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/innodb-upgrade-tests/README.md), [MyISAM](../../../../storage-engines/myisam-storage-engine/myisam-system-variables.md) and [MERGE](../../../../storage-engines/merge.md) tables.


The table is read locked until one has issued [UNLOCK TABLES](../../transactions/transactions-unlock-tables.md).


If a storage engine does not support `<code>FLUSH TABLES FOR EXPORT</code>`, a 1031 error ([SQLSTATE](../../../../../server-usage/programming-customizing-mariadb/programmatic-compound-statements/programmatic-compound-statements-diagnostics/sqlstate.md) 'HY000') is produced.


If `<code>FLUSH TABLES ... FOR EXPORT</code>` is in effect in the session, the following statements will produce an error if attempted:


* `<code>FLUSH TABLES WITH READ LOCK</code>`
* `<code>FLUSH TABLES ... WITH READ LOCK</code>`
* `<code>FLUSH TABLES ... FOR EXPORT</code>`
* Any statement trying to update any table


If any of the following statements is in effect in the session, attempting `<code> FLUSH TABLES ... FOR EXPORT</code>` will produce an error.


* `<code>FLUSH TABLES ... WITH READ LOCK</code>`
* `<code>FLUSH TABLES ... FOR EXPORT</code>`
* `<code>LOCK TABLES ... READ</code>`
* `<code>LOCK TABLES ... WRITE</code>`


`<code>FLUSH FOR EXPORT</code>` is not written to the [binary log](../../../../storage-engines/innodb/binary-log-group-commit-and-innodb-flushing-performance.md).


This statement requires the [RELOAD](../../account-management-sql-commands/grant.md#global-privileges) and the [LOCK TABLES](../../account-management-sql-commands/grant.md#database-privileges) privileges.


If one of the specified tables cannot be locked, none of the tables will be locked.


If a table does not exist, an error like the following will be produced:


```
ERROR 1146 (42S02): Table 'test.xxx' doesn't exist
```

If a table is a view, an error like the following will be produced:


```
ERROR 1347 (HY000): 'test.v' is not BASE TABLE
```

## Example


```
FLUSH TABLES test.t1 FOR EXPORT;
#  Copy files related to the table (see below)
UNLOCK TABLES;
```

For a full description, please see [copying MariaDB tables](../../../../../server-management/copying-tables-between-different-mariadb-databases-and-mariadb-servers.md).


## See Also


* [FLUSH TABLES](flush-tables-for-export.md)
* [Copying Tables Between Different MariaDB Databases and MariaDB Servers](../../../../../server-management/copying-tables-between-different-mariadb-databases-and-mariadb-servers.md)
* [Copying Transportable InnoDB Tablespaces](../../../../storage-engines/innodb/innodb-tablespaces/innodb-file-per-table-tablespaces.md#copying-transportable-tablespaces)
* [myisampack](../../../../../clients-and-utilities/myisam-clients-and-utilities/myisampack.md) - Compressing the MyISAM data file for easier distribution.
* [aria_pack](../../../../../clients-and-utilities/aria-clients-and-utilities/aria_pack.md) - Compressing the Aria data file for easier distribution

