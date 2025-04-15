
# DROP INDEX

## Syntax


```
DROP INDEX [IF EXISTS] index_name ON tbl_name 
    [WAIT n |NOWAIT]
```


## Description


`<code>DROP INDEX</code>` drops the [index](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/optimization-and-indexes/README.md) named `<code>index_name</code>` from the table `<code>tbl_name</code>`.
This statement is mapped to an `<code>ALTER TABLE</code>` statement to drop the
index.


If another connection is using the table, a [metadata lock](../../transactions/metadata-locking.md) is active, and this statement will wait until the lock is released. This is also true for non-transactional tables.


See [ALTER TABLE](../alter/alter-tablespace.md).


Another shortcut, [CREATE INDEX](../create/create-index.md), allows the creation of an index.


To remove the primary key, `<code>`PRIMARY`</code>` must be specified as index_name. Note that [the quotes](../../../sql-language-structure/identifier-qualifiers.md) are necessary, because `<code>PRIMARY</code>` is a keyword.


## Privileges


Executing the `<code>DROP INDEX</code>` statement requires the `<code>[INDEX](../../account-management-sql-commands/grant.md#table-privileges)</code>` privilege for the table or the database.


## Online DDL


Online DDL is used by default with InnoDB, when the drop index operation supports it.


See [InnoDB Online DDL Overview](../../../../storage-engines/innodb/innodb-online-ddl/innodb-online-ddl-overview.md) for more information on online DDL with [InnoDB](../../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/innodb-upgrade-tests/README.md).


## DROP INDEX IF EXISTS ...


If the `<code>IF EXISTS</code>` clause is used, then MariaDB will return a warning instead of an error if the index does not exist.


## WAIT/NOWAIT


Sets the lock wait timeout. See [WAIT and NOWAIT](../../transactions/wait-and-nowait.md).


## Progress Reporting


MariaDB provides progress reporting for `<code>DROP INDEX</code>` statement for clients
that support the new progress reporting protocol. For example, if you were using the [mariadb](../../../../../clients-and-utilities/mariadb-client/mariadb-command-line-client.md) client, then the progress report might look like this::


## See Also


* [Getting Started with Indexes](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/optimization-and-indexes/getting-started-with-indexes.md)
* [CREATE INDEX](../create/create-index.md)
* [ALTER TABLE](../alter/alter-tablespace.md)

