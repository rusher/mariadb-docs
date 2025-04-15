
# CREATE TABLE

## Syntax


```
[
```


## Description


Use the `<code>CREATE TABLE</code>` statement to create a table with the given name.


In its most basic form, the `<code>CREATE TABLE</code>` statement provides a table name
followed by a list of columns, indexes, and constraints. By default, the table
is created in the default database. Specify a database with `<code><em>db_name</em>.<em>tbl_name</em></code>`.
If you quote the table name, you must quote the database name and table name
separately as `<code>`<em>db_name</em>`.`<em>tbl_name</em>`</code>`. This is particularly useful for [CREATE TABLE ... SELECT](#create-table-select), because it allows to create a table into a database, which contains data from other databases. See [Identifier Qualifiers](../../../sql-language-structure/identifier-qualifiers.md).


If a table with the same name exists, error 1050 results. Use [IF NOT EXISTS](#create-table-if-not-exists)
to suppress this error and issue a note instead. Use [SHOW WARNINGS](../../administrative-sql-statements/show/show-warnings.md)
to see notes.


The `<code>CREATE TABLE</code>` statement automatically commits the current transaction,
except when using the [TEMPORARY](#create-temporary-table) keyword.


For valid identifiers to use as table names, see [Identifier Names](../../../sql-language-structure/identifier-names.md).


**Note:** if the default_storage_engine is set to ColumnStore then it needs setting on all UMs. Otherwise when the tables using the default engine are replicated across UMs they will use the wrong engine. You should therefore not use this option as a session variable with ColumnStore.


[Microsecond precision](../../built-in-functions/date-time-functions/microseconds-in-mariadb.md) can be between 0-6. If no precision is specified it is assumed to be 0, for backward compatibility reasons.


## Privileges


Executing the `<code>CREATE TABLE</code>` statement requires the [CREATE](../../account-management-sql-commands/grant.md#table-privileges) privilege for the table or the database.


## CREATE OR REPLACE


If the `<code>OR REPLACE</code>` clause is used and the table already exists, then instead of returning an error, the server will drop the existing table and replace it with the newly defined table.


This syntax was originally added to make [replication](../../../../../server-usage/replication-cluster-multi-master/standard-replication/README.md) more robust if it has to rollback and repeat statements such as `<code>CREATE ... SELECT</code>` on replicas.


```
CREATE OR REPLACE TABLE table_name (a int);
```

is basically the same as:


```
DROP TABLE IF EXISTS table_name;
CREATE TABLE table_name (a int);
```

with the following exceptions:


* If `<code class="highlight fixed" style="white-space:pre-wrap">table_name</code>` was locked with [LOCK TABLES](../../transactions/lock-tables.md) it will continue to be locked after the statement.
* Temporary tables are only dropped if the `<code class="highlight fixed" style="white-space:pre-wrap">TEMPORARY</code>` keyword was used. (With [DROP TABLE](../drop/drop-tablespace.md), temporary tables are preferred to be dropped before normal tables).


### Things to be Aware of With CREATE OR REPLACE


* The table is dropped first (if it existed), after that the `<code class="highlight fixed" style="white-space:pre-wrap">CREATE</code>` is done. Because of this, if the `<code class="highlight fixed" style="white-space:pre-wrap">CREATE</code>` fails, then the table will not exist anymore after the statement. If the table was used with `<code class="highlight fixed" style="white-space:pre-wrap">LOCK TABLES</code>` it will be unlocked.
* One can't use `<code class="highlight fixed" style="white-space:pre-wrap">OR REPLACE</code>` together with `<code class="highlight fixed" style="white-space:pre-wrap">IF EXISTS</code>`.
* [Replicas](../../../../../server-usage/replication-cluster-multi-master/standard-replication/README.md) will by default use `<code class="highlight fixed" style="white-space:pre-wrap">CREATE OR REPLACE</code>` when replicating `<code class="highlight fixed" style="white-space:pre-wrap">CREATE</code>` statements that don''t use `<code class="highlight fixed" style="white-space:pre-wrap">IF EXISTS</code>`. This can be changed by setting the variable [slave-ddl-exec-mode](../../../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md) to `<code class="highlight fixed" style="white-space:pre-wrap">STRICT</code>`.


## CREATE TABLE IF NOT EXISTS


If the `<code>IF NOT EXISTS</code>` clause is used, then the table will only be created if a table with the same name does not already exist. If the table already exists, then a warning will be triggered by default.


## CREATE TEMPORARY TABLE


Use the `<code>TEMPORARY</code>` keyword to create a temporary table that is only available to the current session. Temporary tables are dropped when the session ends. Temporary table names are specific to the session. They will not conflict with other temporary tables from other sessions even if they share the same name. They will shadow names of non-temporary tables or views, if they are identical. A temporary table can have the same name as a non-temporary table which is located in the same database. In that case, their name will reference the temporary table when used in SQL statements. You must have the [CREATE TEMPORARY TABLES](../../account-management-sql-commands/grant.md#database-privileges) privilege on the database to create temporary tables. If no storage engine is specified, the [default_tmp_storage_engine](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#default_tmp_storage_engine) setting will determine the engine.


[ROCKSDB](../../../../storage-engines/myrocks/myrocks-in-mariadb-102-vs-mariadb-103.md) temporary tables cannot be created by setting the [default_tmp_storage_engine](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#default_tmp_storage_engine) system variable, or using `<code>CREATE TEMPORARY TABLE LIKE</code>`. Before [MariaDB 10.7](../../../../../../release-notes/mariadb-community-server/what-is-mariadb-107.md), they could be specified, but would silently fail, and a MyISAM table would be created instead. From [MariaDB 10.7](../../../../../../release-notes/mariadb-community-server/what-is-mariadb-107.md) an error is returned. Explicitly creating a temporary table with `<code>ENGINE=ROCKSDB</code>` has never been permitted.


## CREATE TABLE ... LIKE


Use the `<code>LIKE</code>` clause instead of a full table definition to create an empty table with the same definition as another table, including columns, indexes, and table options. Foreign key definitions, as well as any DATA DIRECTORY or INDEX DIRECTORY table options specified on the original table, will not be created.


`<code>LIKE</code>` does not preserve the `<code>TEMPORARY</code>` status of the original table. To make the new table `<code>TEMPORARY</code>` as well, use `<code>CREATE TEMPORARY TABLE ... LIKE</code>`.


`<code>LIKE</code>` does not work with [views](../../../../../server-usage/programming-customizing-mariadb/views/README.md), only base tables. Attempting to use it on a view will result in an error:


```
CREATE VIEW v (mycol) AS SELECT 'abc';

CREATE TABLE v2 LIKE v;
ERROR 1347 (HY000): 'test.v' is not of type 'BASE TABLE'
```

The same version of the table storage format as found in the original table is used for the new table.


`<code>CREATE TABLE ... LIKE</code>` performs the same checks as `<code>CREATE TABLE</code>`. So a statement may fail if a change in the [SQL_MODE](../../../../../server-management/variables-and-modes/sql-mode.md) renders it invalid. For example:


```
CREATE OR REPLACE TABLE x (d DATE DEFAULT '0000-00-00');

SET SQL_MODE='NO_ZERO_DATE';

CREATE OR REPLACE TABLE y LIKE x;
ERROR 1067 (42000): Invalid default value for 'd'
```

## CREATE TABLE ... SELECT


You can create a table containing data from other tables using the `<code>CREATE ... SELECT</code>` statement. Columns will be created in the table for each field returned by the `<code>SELECT</code>` query.


You can also define some columns normally and add other columns from a `<code>SELECT</code>`. You can also create columns in the normal way and assign them some values using the query, this is done to force a certain type or other field characteristics. The columns that are not named in the query will be placed before the others. For example:


```
CREATE TABLE test (a INT NOT NULL, b CHAR(10)) ENGINE=MyISAM
    SELECT 5 AS b, c, d FROM another_table;
```

Remember that the query just returns data. If you want to use the same indexes, or the same columns attributes (`<code>[NOT] NULL</code>`, `<code>DEFAULT</code>`, `<code>AUTO_INCREMENT</code>`) in the new table, you need to specify them manually. Types and sizes are not automatically preserved if no data returned by the `<code>SELECT</code>` requires the full size, and `<code>VARCHAR</code>` could be converted into `<code>CHAR</code>`. The [CAST()](../../built-in-functions/string-functions/cast.md) function can be used to forcee the new table to use certain types.


Aliases (`<code>AS</code>`) are taken into account, and they should always be used when you `<code>SELECT</code>` an expression (function, arithmetical operation, etc).


If an error occurs during the query, the table will not be created at all.


If the new table has a primary key or `<code>UNIQUE</code>` indexes, you can use the [IGNORE](../../data-manipulation/inserting-loading-data/ignore.md) or `<code>REPLACE</code>` keywords to handle duplicate key errors during the query. `<code>IGNORE</code>` means that the newer values must not be inserted an identical value exists in the index. `<code>REPLACE</code>` means that older values must be overwritten.


If the columns in the new table are more than the rows returned by the query, the columns populated by the query will be placed after other columns. Note that if the strict `<code>SQL_MODE</code>` is on, and the columns that are not names in the query do not have a `<code>DEFAULT</code>` value, an error will raise and no rows will be copied.


[Concurrent inserts](../../data-manipulation/inserting-loading-data/concurrent-inserts.md) are not used during the execution of a `<code>CREATE ... SELECT</code>`.


If the table already exists, an error similar to the following will be returned:


```
ERROR 1050 (42S01): Table 't' already exists
```

If the `<code>IF NOT EXISTS</code>` clause is used and the table exists, a note will be produced instead of an error.


To insert rows from a query into an existing table, [INSERT ... SELECT](../../data-manipulation/inserting-loading-data/insert-select.md) can be used.


## Column Definitions


```
|
```


#### Note:

MariaDB accepts the shortcut format with a REFERENCES clause only in ALTER TABLE and CREATE TABLE statements, but that syntax does nothing. For example:

```
CREATE TABLE b(for_key INT REFERENCES a(not_key));
```
From [MariaDB 10.5](../../../../../../release-notes/mariadb-community-server/what-is-mariadb-105.md), MariaDB will attempt to apply the constraint. See [Foreign Keys examples](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/optimization-and-indexes/foreign-keys.md#references).


Each definition either creates a column in the table or specifies and index or
constraint on one or more columns. See [Indexes](#indexes) below for details
on creating indexes.


Create a column by specifying a column name and a data type, optionally
followed by column options. See [Data Types](../../../../data-types/data-types-overview/data-types-subcategory/data-types-dec.md) for a full list
of data types allowed in MariaDB.


### NULL and NOT NULL


Use the `<code>NULL</code>` or `<code>NOT NULL</code>` options to specify that values in the column
may or may not be `<code>NULL</code>`, respectively. By default, values may be `<code>NULL</code>`. See also [NULL Values in MariaDB](../../../../data-types/null-values.md).


### DEFAULT Column Option


Specify a default value using the `<code>DEFAULT</code>` clause. If you don't specify `<code>DEFAULT</code>` then the following rules apply:


* If the column is not defined with `<code>NOT NULL</code>`, `<code>AUTO_INCREMENT</code>` or `<code>TIMESTAMP</code>`, an explicit `<code>DEFAULT NULL</code>` will be added.
Note that in MySQL, you may get an explicit `<code>DEFAULT</code>` for primary key parts, if not specified with NOT NULL.


The default value will be used if you [INSERT](../../built-in-functions/string-functions/insert-function.md) a row without specifying a value for that column, or if you specify [DEFAULT](../../built-in-functions/secondary-functions/information-functions/default.md) for that column.


[CURRENT_TIMESTAMP](../../built-in-functions/date-time-functions/now.md) may also be used as
the default value for a [DATETIME](../../../../data-types/date-and-time-data-types/datetime.md)


You can use most functions in `<code>DEFAULT</code>`. Expressions should have parentheses around them. If you use a non deterministic function in `<code>DEFAULT</code>` then all inserts to the table will be [replicated](../../administrative-sql-statements/replication-statements/README.md) in [row mode](../../../../../server-management/server-monitoring-logs/binary-log/binary-log-formats.md#row-based). You can even refer to earlier columns in the `<code>DEFAULT</code>` expression (excluding `<code>AUTO_INCREMENT</code>` columns):


```
CREATE TABLE t1 (a int DEFAULT (1+1), b int DEFAULT (a+1));
CREATE TABLE t2 (a bigint primary key DEFAULT UUID_SHORT());
```

The `<code>DEFAULT</code>` clause cannot contain any [stored functions](../../../../../server-usage/programming-customizing-mariadb/stored-routines/stored-functions/README.md) or [subqueries](../../data-manipulation/selecting-data/joins-subqueries/subqueries/subqueries-and-all.md), and a column used in the clause must already have been defined earlier in the statement.


It is possible to assign [BLOB](../../../../data-types/string-data-types/blob.md) or [TEXT](../../../../data-types/string-data-types/text.md) columns a `<code>DEFAULT</code>` value.


You can also use DEFAULT ([NEXT VALUE FOR sequence](../../../sequences/sequence-functions/next-value-for-sequence_name.md))


### AUTO_INCREMENT Column Option


Use [AUTO_INCREMENT](../../../../storage-engines/innodb/auto_increment-handling-in-innodb.md) to create a column whose value can
can be set automatically from a simple counter. You can only use `<code>AUTO_INCREMENT</code>`
on a column with an integer type. The column must be a key, and there can only be
one `<code>AUTO_INCREMENT</code>` column in a table. If you insert a row without specifying
a value for that column (or if you specify `<code>0</code>`, `<code>NULL</code>`, or [DEFAULT](../../built-in-functions/secondary-functions/information-functions/default.md)
as the value), the actual value will be taken from the counter, with each insertion
incrementing the counter by one. You can still insert a value explicitly. If you
insert a value that is greater than the current counter value, the counter is
set based on the new value. An `<code>AUTO_INCREMENT</code>` column is implicitly `<code>NOT NULL</code>`.
Use [LAST_INSERT_ID](../../built-in-functions/secondary-functions/information-functions/last_insert_id.md) to get the [AUTO_INCREMENT](../../../../storage-engines/innodb/auto_increment-handling-in-innodb.md) value
most recently used by an [INSERT](../../built-in-functions/string-functions/insert-function.md) statement.


### ZEROFILL Column Option


If the `<code>ZEROFILL</code>` column option is specified for a column using a [numeric](../../../../data-types/data-types-numeric-data-types/numeric-data-type-overview.md) data type, then the column will be set to `<code>UNSIGNED</code>` and the spaces used by default to pad the field are replaced with zeros. `<code>ZEROFILL</code>` is ignored in expressions or as part of a [UNION](../../data-manipulation/selecting-data/joins-subqueries/union.md). `<code>ZEROFILL</code>` is a non-standard MySQL and MariaDB enhancement.


### PRIMARY KEY Column Option


Use `<code>PRIMARY KEY</code>` to make a column a primary key. A primary key is a special type of a unique key. There can be at most one primary key per table, and it is implicitly `<code>NOT NULL</code>`.


Specifying a column as a unique key creates a unique index on that column. See the [Index Definitions](#index-definitions) section below for more information.


### UNIQUE KEY Column Option


Use `<code>UNIQUE KEY</code>` (or just `<code>UNIQUE</code>`) to specify that all values in the column
must be distinct from each other. Unless the column is `<code>NOT NULL</code>`, there may be
multiple rows with `<code>NULL</code>` in the column.


Specifying a column as a unique key creates a unique index on that column.


See the [Index Definitions](#index-definitions) section below for more information.


### COMMENT Column Option


You can provide a comment for each column using the `<code>COMMENT</code>` clause. The maximum length is 1024 characters. Use
the [SHOW FULL COLUMNS](../../administrative-sql-statements/show/show-columns.md) statement to see column comments.


### REF_SYSTEM_ID


`<code>REF_SYSTEM_ID</code>` can be used to specify Spatial Reference System IDs for spatial data type columns. For example:


```
CREATE TABLE t1(g GEOMETRY(9,4) REF_SYSTEM_ID=101);
```

### Generated Columns


A generated column is a column in a table that cannot explicitly be set to a specific value in a [DML query](../../data-manipulation/README.md). Instead, its value is automatically generated based on an expression. This expression might generate the value based on the values of other columns in the table, or it might generate the value by calling [built-in functions](../../built-in-functions/README.md) or [user-defined functions (UDFs)](../../../../../server-usage/programming-customizing-mariadb/user-defined-functions/user-defined-functions-security.md).


There are two types of generated columns:


* `<code>PERSISTENT</code>` or `<code>STORED</code>`: This type's value is actually stored in the table.
* `<code>VIRTUAL</code>`: This type's value is not stored at all. Instead, the value is generated dynamically when the table is queried. This type is the default.


Generated columns are also sometimes called computed columns or virtual columns.


For a complete description about generated columns and their limitations, see [Generated (Virtual and Persistent/Stored) Columns](generated-columns.md).


### COMPRESSED


Certain columns may be compressed. See [Storage-Engine Independent Column Compression](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/optimization-and-tuning-compression/storage-engine-independent-column-compression.md).


### INVISIBLE


Columns may be made invisible, and hidden in certain contexts. See [Invisible Columns](invisible-columns.md).


### WITH SYSTEM VERSIONING Column Option


Columns may be explicitly marked as included from system versioning. See [System-versioned tables](../../../temporal-tables/system-versioned-tables.md) for details.


### WITHOUT SYSTEM VERSIONING Column Option


Columns may be explicitly marked as excluded from system versioning. See [System-versioned tables](../../../temporal-tables/system-versioned-tables.md) for details.


## Index Definitions


```
index_definition:
    {INDEX|KEY} [index_name] [index_type] (index_col_name,...) [index_option] ...
  {{{|}}} {FULLTEXT|SPATIAL} [INDEX|KEY] [index_name] (index_col_name,...) [index_option] ...
  {{{|}}} [CONSTRAINT [symbol]] PRIMARY KEY [index_type] (index_col_name,...) [index_option] ...
  {{{|}}} [CONSTRAINT [symbol]] UNIQUE [INDEX|KEY] [index_name] [index_type] (index_col_name,...) [index_option] ...
  {{{|}}} [CONSTRAINT [symbol]] FOREIGN KEY [index_name] (index_col_name,...) reference_definition

index_col_name:
    col_name [(length)] [ASC | DESC]

index_type:
    USING {BTREE | HASH | RTREE}

index_option:
    [ KEY_BLOCK_SIZE [=] value
  {{{|}}} index_type
  {{{|}}} WITH PARSER parser_name
  {{{|}}} VISIBLE
  {{{|}}} COMMENT 'string'
  {{{|}}} CLUSTERING={YES| NO} ]
  [ IGNORED | NOT IGNORED ]

reference_definition:
    REFERENCES tbl_name (index_col_name,...)
      [MATCH FULL | MATCH PARTIAL | MATCH SIMPLE]
      [ON DELETE reference_option]
      [ON UPDATE reference_option]

reference_option:
    RESTRICT | CASCADE | SET NULL | NO ACTION
```

`<code>INDEX</code>` and `<code>KEY</code>` are synonyms.


Index names are optional, if not specified an automatic name will be assigned. Index name are needed to drop indexes and appear in error messages when a constraint is violated.


For limits on InnoDB indexes, see [InnoDB Limitations](../../../../storage-engines/innodb/innodb-limitations.md).


### Index Categories


#### Plain Indexes


Plain indexes are regular indexes that are not unique, and are not acting as a primary key or a foreign key. They are also not the "specialized" `<code>FULLTEXT</code>` or `<code>SPATIAL</code>` indexes.


See [Getting Started with Indexes: Plain Indexes](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/optimization-and-indexes/getting-started-with-indexes.md#plain-indexes) for more information.


#### PRIMARY KEY


For `<code>PRIMARY KEY</code>` indexes, you can specify a name for the index, but it is ignored, and the name of the index is always `<code>PRIMARY</code>`. A warning is explicitly issued if a name is specified. Before then, the name was silently ignored.


See [Getting Started with Indexes: Primary Key](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/optimization-and-indexes/getting-started-with-indexes.md#primary-key) for more information.


#### UNIQUE


The `<code>UNIQUE</code>` keyword means that the index will not accept duplicated values, except for NULLs. An error will raise if you try to insert duplicate values in a UNIQUE index.


For `<code>UNIQUE</code>` indexes, you can specify a name for the constraint, using the `<code>CONSTRAINT</code>` keyword. That name will be used in error messages.



##### MariaDB starting with [10.5](../../../../../../release-notes/mariadb-community-server/what-is-mariadb-105.md)
Unique, if index type is not specified, is normally a BTREE index that can also be used by the optimizer to find rows. If the key is longer than the max key length for the used storage engine, a HASH key will be created. This enables MariaDB to enforce uniqueness for any type or number of columns.


See [Getting Started with Indexes: Unique Index](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/optimization-and-indexes/getting-started-with-indexes.md#unique-index) for more information.


#### FOREIGN KEY


For `<code>FOREIGN KEY</code>` indexes, a reference definition must be provided.


For `<code>FOREIGN KEY</code>` indexes, you can specify a name for the constraint, using the `<code>CONSTRAINT</code>` keyword. That name will be used in error messages.


First, you have to specify the name of the target (parent) table and a column or a column list which must be indexed and whose values must match to the foreign key's values. The `<code>MATCH</code>` clause is accepted to improve the compatibility with other DBMS's, but has no meaning in MariaDB. The `<code>ON DELETE</code>` and `<code>ON UPDATE</code>` clauses specify what must be done when a `<code>DELETE</code>` (or a `<code>REPLACE</code>`) statements attempts to delete a referenced row from the parent table, and when an `<code>UPDATE</code>` statement attempts to modify the referenced foreign key columns in a parent table row, respectively. The following options are allowed:


* `<code>RESTRICT</code>`: The delete/update operation is not performed. The statement terminates with a 1451 error (SQLSTATE '2300').
* `<code>NO ACTION</code>`: Synonym for `<code>RESTRICT</code>`.
* `<code>CASCADE</code>`: The delete/update operation is performed in both tables.
* `<code>SET NULL</code>`: The update or delete goes ahead in the parent table, and the corresponding foreign key fields in the child table are set to `<code>NULL</code>`. (They must not be defined as `<code>NOT NULL</code>` for this to succeed).
* `<code>SET DEFAULT</code>`: This option is currently implemented only for the PBXT storage engine, which is disabled by default and no longer maintained. It sets the child table's foreign key fields to their `<code>DEFAULT</code>` values when the referenced parent table key entries are updated or deleted.


If either clause is omitted, the default behavior for the omitted clause is `<code>RESTRICT</code>`.


See [Foreign Keys](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/optimization-and-indexes/foreign-keys.md) for more information.


#### FULLTEXT


Use the `<code>FULLTEXT</code>` keyword to create full-text indexes.


See [Full-Text Indexes](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/optimization-and-indexes/full-text-indexes/README.md) for more information.


#### SPATIAL


Use the `<code>SPATIAL</code>` keyword to create geometric indexes.


See [SPATIAL INDEX](../../../geographic-geometric-features/spatial-index.md) for more information.


### Index Options


#### KEY_BLOCK_SIZE Index Option


The `<code>KEY_BLOCK_SIZE</code>` index option is similar to the [KEY_BLOCK_SIZE](#key_block_size) table option.


With the [InnoDB](../../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/innodb-upgrade-tests/README.md) storage engine, if you specify a non-zero value for the `<code>KEY_BLOCK_SIZE</code>` table option for the whole table, then the table will implicitly be created with the [ROW_FORMAT](#row_format) table option set to `<code>COMPRESSED</code>`. However, this does not happen if you just set the `<code>KEY_BLOCK_SIZE</code>` index option for one or more indexes in the table. The [InnoDB](../../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/innodb-upgrade-tests/README.md) storage engine ignores the `<code>KEY_BLOCK_SIZE</code>` index option. However, the [SHOW CREATE TABLE](../../administrative-sql-statements/show/show-create-table.md) statement may still report it for the index.


For information about the `<code>KEY_BLOCK_SIZE</code>` index option, see the [KEY_BLOCK_SIZE](#key_block_size) table option below.


#### Index Types


Each storage engine supports some or all index types. See [Storage Engine Index Types](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/optimization-and-indexes/storage-engine-index-types.md) for details on permitted index types for each storage engine.


Different index types are optimized for different kind of operations:


* `<code>BTREE</code>` is the default type, and normally is the best choice. It is supported by all storage engines. It can be used to compare a column's value with a value using the =, >, >=, <, <=, `<code>BETWEEN</code>`, and `<code>LIKE</code>` operators. `<code>BTREE</code>` can also be used to find `<code>NULL</code>` values. Searches against an index prefix are possible.
* `<code>HASH</code>` is only supported by the MEMORY storage engine. `<code>HASH</code>` indexes can only be used for =, <=, and >= comparisons. It can not be used for the `<code>ORDER BY</code>` clause. Searches against an index prefix are not possible.
* `<code>RTREE</code>` is the default for [SPATIAL](../../../geographic-geometric-features/spatial-index.md) indexes, but if the storage engine does not support it `<code>BTREE</code>` can be used.


Index columns names are listed between parenthesis. After each column, a prefix length can be specified. If no length is specified, the whole column will be indexed. `<code>ASC</code>` and `<code>DESC</code>` can be specified. Prior to [MariaDB 10.8](../../../../../../release-notes/mariadb-community-server/what-is-mariadb-108.md), this was only for compatibility with other DBMSs, but had no meaning in MariaDB. From [MariaDB 10.8](../../../../../../release-notes/mariadb-community-server/what-is-mariadb-108.md), individual columns in the index can now be explicitly sorted in ascending or descending order. This can be useful for optimizing certain ORDER BY cases ([MDEV-13756](https://jira.mariadb.org/browse/MDEV-13756), [MDEV-26938](https://jira.mariadb.org/browse/MDEV-26938), [MDEV-26939](https://jira.mariadb.org/browse/MDEV-26939), [MDEV-26996](https://jira.mariadb.org/browse/MDEV-26996)). From [MariaDB 11.4.0](../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-4-series/mariadb-11-4-0-release-notes.md), not only ascending, but also descending, indexes can now be used to optimize [MIN()](../../../../mariadb-internals/mariadb-internals-documentation-query-optimizer/minmax-optimization.md) and [MAX()](../../../../../../maxscale/mariadb-maxscale-14/maxscale-14-tutorials/maxscale-connection-routing-with-mysql-replication.md) ([MDEV-27576](https://jira.mariadb.org/browse/MDEV-27576)).


The maximum number of parts in an index is 32.


#### WITH PARSER Index Option


The `<code>WITH PARSER</code>` index option only applies to [FULLTEXT](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/optimization-and-indexes/full-text-indexes/README.md) indexes and contains the fulltext parser name. The fulltext parser must be an installed plugin.


#### VISIBLE Index Option



##### MariaDB starting with [10.5.3](../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1053-release-notes.md)
From [MariaDB 10.5.3](../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1053-release-notes.md), indexes can be declared visible. This is the default and it shows up in [SHOW CREATE TABLE](../../administrative-sql-statements/show/show-create-table.md).


#### COMMENT Index Option


A comment of up to 1024 characters is permitted with the `<code>COMMENT</code>` index option.


The `<code>COMMENT</code>` index option allows you to specify a comment with user-readable text describing what the index is for. This information is not used by the server itself.


#### CLUSTERING Index Option


The `<code>CLUSTERING</code>` index option is only valid for tables using the [TokuDB](../../../../storage-engines/tokudb/tokudb-resources.md) storage engine.


#### IGNORED / NOT IGNORED



##### MariaDB starting with [10.6.0](../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-1060-release-notes.md)
From [MariaDB 10.6.0](../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-1060-release-notes.md), indexes can be specified to be ignored by the optimizer. See [Ignored Indexes](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/optimization-and-indexes/ignored-indexes.md).


## Periods


```
period_definition:
    PERIOD FOR [time_period_name | SYSTEM_TIME] (start_column_name, end_column_name)
```

MariaDB supports [System-versioned tables](../../../temporal-tables/system-versioned-tables.md), [Application-time-period tables](../../../temporal-tables/application-time-periods.md) or [Bitemporal Tables](../../../temporal-tables/bitemporal-tables.md).


## Constraint Expressions


MariaDB introduced two ways to define a constraint:


* `<code>CHECK(expression)</code>` given as part of a column definition.
* `<code>CONSTRAINT [constraint_name] CHECK (expression)</code>`


Before a row is inserted or updated, all constraints are evaluated in the order they are defined. If any constraints fails, then the row will not be updated.
One can use most deterministic functions in a constraint, including [UDFs](../../../../../server-usage/programming-customizing-mariadb/user-defined-functions/user-defined-functions-security.md).


```
create table t1 (a int check(a>0) ,b int check (b> 0), constraint abc check (a>b));
```

If you use the second format and you don't give a name to the constraint, then the constraint will get a auto generated name. This is done so that you can later delete the constraint with [ALTER TABLE DROP constraint_name](../alter/alter-tablespace.md).


One can disable all constraint expression checks by setting the variable `<code>check_constraint_checks</code>` to `<code>OFF</code>`. This is useful for example when loading a table that violates some constraints that you want to later find and fix in SQL.


See [CONSTRAINT](../constraint.md) for more information.


## Table Options


For each individual table you create (or alter), you can set some table options. The general syntax for setting options is:


<OPTION_NAME> = <option_value>, [<OPTION_NAME> = <option_value> ...]


The equal sign is optional.


Some options are supported by the server and can be used for all tables, no matter what storage engine they use; other options can be specified for all storage engines, but have a meaning only for some engines. Also, engines can [extend CREATE TABLE with new options](../../../../storage-engines/storage-engines-storage-engine-development/engine-defined-new-tablefieldindex-attributes.md).


If the `<code>IGNORE_BAD_TABLE_OPTIONS</code>` [SQL_MODE](../../../../../server-management/variables-and-modes/sql-mode.md) is enabled, wrong table options generate a warning; otherwise, they generate an error.


```
|
```

### [STORAGE] ENGINE


`<code>[STORAGE] ENGINE</code>` specifies a [storage engine](../../../../../../general-resources/learning-and-training/video-presentations-and-screencasts/storage-engines-and-plugins-videos.md) for the table. If this option is not used, the default storage engine is used instead. That is, the [default_storage_engine](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#default_storage_engine) session option value if it is set, or the value specified for the `<code>--default-storage-engine</code>` [mariadbd startup option](../../../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md), or the default storage engine, [InnoDB](../../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/innodb-upgrade-tests/README.md). If the specified storage engine is not installed and active, the default value will be used, unless the `<code>NO_ENGINE_SUBSTITUTION</code>` [SQL MODE](../../../../../server-management/variables-and-modes/sql-mode.md) is set (default). This is only true for `<code>CREATE TABLE</code>`, not for `<code>ALTER TABLE</code>`. For a list of storage engines that are present in your server, issue a [SHOW ENGINES](../../administrative-sql-statements/show/show-engines.md).


### AUTO_INCREMENT


`<code>AUTO_INCREMENT</code>` specifies the initial value for the [AUTO_INCREMENT](../../../../storage-engines/innodb/auto_increment-handling-in-innodb.md) primary key. This works for MyISAM, Aria, InnoDB, MEMORY, and ARCHIVE tables. You can change this option with `<code>ALTER TABLE</code>`, but in that case the new value must be higher than the highest value which is present in the `<code>AUTO_INCREMENT</code>` column. If the storage engine does not support this option, you can insert (and then delete) a row having the wanted value - 1 in the `<code>AUTO_INCREMENT</code>` column.


### AVG_ROW_LENGTH


`<code>AVG_ROW_LENGTH</code>` is the average rows size. It only applies to tables using [MyISAM](../../../../storage-engines/myisam-storage-engine/myisam-system-variables.md) and [Aria](../../../../storage-engines/aria/aria-storage-engine.md) storage engines that have the [ROW_FORMAT](#row_format) table option set to `<code>FIXED</code>` format.


MyISAM uses `<code>MAX_ROWS</code>` and `<code>AVG_ROW_LENGTH</code>` to decide the maximum size of a table (default: 256TB, or the maximum file size allowed by the system).


### [DEFAULT] CHARACTER SET/CHARSET


`<code>[DEFAULT] CHARACTER SET</code>` (or `<code>[DEFAULT] CHARSET</code>`) is used to set a default character set for the table. This is the character set used for all columns where an explicit character set is not specified. If this option is omitted or `<code>DEFAULT</code>` is specified, the database's default character set will be used (except for the [JSON data type](../../../../storage-engines/connect/json-sample-files.md), which is utf8mb4 by default). See [Setting Character Sets and Collations](../../../../data-types/string-data-types/character-sets/setting-character-sets-and-collations.md) for details on setting the [character sets](../../../../data-types/string-data-types/character-sets/README.md).


### CHECKSUM/TABLE_CHECKSUM


`<code>CHECKSUM</code>` (or `<code>TABLE_CHECKSUM</code>`) can be set to 1 to maintain a live checksum for all table's rows. This makes write operations slower, but [CHECKSUM TABLE](../../table-statements/checksum-table.md) will be very fast. This option is only supported for [MyISAM](../../../../storage-engines/myisam-storage-engine/myisam-system-variables.md) and [Aria tables](../../../../storage-engines/aria/aria-storage-engine.md).


### [DEFAULT] COLLATE


`<code>[DEFAULT] COLLATE</code>` is used to set a default collation for the table. This is the collation used for all columns where an explicit character set is not specified. If this option is omitted or `<code>DEFAULT</code>` is specified, the database's default option will be used (except for the [JSON data type](../../../../storage-engines/connect/json-sample-files.md), which uses utf8mb4_bin by default). See [Setting Character Sets and Collations](../../../../data-types/string-data-types/character-sets/setting-character-sets-and-collations.md) for details on setting the [collations](../../../../data-types/string-data-types/character-sets/README.md)


### COMMENT


`<code>COMMENT</code>` is a comment for the table. The maximum length is 2048 characters. Also used to define table parameters when creating a [Spider](../../../../storage-engines/spider/spider-functions/spider_copy_tables.md) table.


### CONNECTION


`<code>CONNECTION</code>` is used to specify a server name or a connection string for a [Spider](../../../../storage-engines/spider/spider-functions/spider_copy_tables.md), [CONNECT](../../../../../../connectors/mariadb-connector-nodejs/connector-nodejs-pipelining.md), [Federated or FederatedX table](../../../../storage-engines/federatedx-storage-engine/about-federatedx.md).


### DATA DIRECTORY/INDEX DIRECTORY


`<code>DATA DIRECTORY</code>` and `<code>INDEX DIRECTORY</code>` are supported for MyISAM and Aria, and DATA DIRECTORY is also supported by InnoDB if the [innodb_file_per_table](../../../../storage-engines/innodb/innodb-system-variables.md#innodb_file_per_table) server system variable is enabled, but only in CREATE TABLE, not in [ALTER TABLE](../alter/alter-tablespace.md). So, carefully choose a path for InnoDB tables at creation time, because it cannot be changed without dropping and re-creating the table. These options specify the paths for data files and index files, respectively. If these options are omitted, the database's directory will be used to store data files and index files. Note that these table options do not work for [partitioned](../../../../../server-management/partitioning-tables/README.md) tables (use the partition options instead), or if the server has been invoked with the [--skip-symbolic-links startup option](../../../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md). To avoid the overwriting of old files with the same name that could be present in the directories, you can use [the --keep_files_on_create option](../../../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md) (an error will be issued if files already exist). These options are ignored if the `<code>NO_DIR_IN_CREATE</code>` [SQL_MODE](../../../../../server-management/variables-and-modes/sql-mode.md) is enabled (useful for replicas). Also note that symbolic links cannot be used for InnoDB tables.


`<code>DATA DIRECTORY</code>` works by creating symlinks from where the table would normally have been (inside the [datadir](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#datadir)) to where the option specifies. For security reasons, to avoid bypassing the privilege system, the server does not permit symlinks inside the datadir. Therefore, `<code>DATA DIRECTORY</code>` cannot be used to specify a location inside the datadir. An attempt to do so will result in an error `<code>1210 (HY000) Incorrect arguments to DATA DIRECTORY</code>`.


### DELAY_KEY_WRITE


`<code>DELAY_KEY_WRITE</code>` is supported by MyISAM and Aria, and can be set to 1 to speed up write operations. In that case, when data are modified, the indexes are not updated until the table is closed. Writing the changes to the index file altogether can be much faster. However, note that this option is applied only if the `<code>delay_key_write</code>` server variable is set to 'ON'. If it is 'OFF' the delayed index writes are always disabled, and if it is 'ALL' the delayed index writes are always used, disregarding the value of `<code>DELAY_KEY_WRITE</code>`.


### ENCRYPTED


The `<code>ENCRYPTED</code>` table option can be used to manually set the encryption status of an [InnoDB](../../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/innodb-upgrade-tests/README.md) table. See [InnoDB Encryption](../../../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/innodb-encryption/innodb-encryption-troubleshooting.md) for more information.


Aria does not support the `<code>ENCRYPTED</code>` table option. See [MDEV-18049](https://jira.mariadb.org/browse/MDEV-18049).


See [Data-at-Rest Encryption](../../../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/README.md) for more information.


### ENCRYPTION_KEY_ID


The `<code>ENCRYPTION_KEY_ID</code>` table option can be used to manually set the encryption key of an [InnoDB](../../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/innodb-upgrade-tests/README.md) table. See [InnoDB Encryption](../../../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/innodb-encryption/innodb-encryption-troubleshooting.md) for more information.


Aria does not support the `<code>ENCRYPTION_KEY_ID</code>` table option. See [MDEV-18049](https://jira.mariadb.org/browse/MDEV-18049).


See [Data-at-Rest Encryption](../../../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/README.md) for more information.


### IETF_QUOTES


For the [CSV](../../../../storage-engines/csv/csv-overview.md) storage engine, the `<code>IETF_QUOTES</code>` option, when set to `<code>YES</code>`, enables IETF-compatible parsing of embedded quote and comma characters. Enabling this option for a table improves compatibility with other tools that use CSV, but is not compatible with MySQL CSV tables, or MariaDB CSV tables created without this option. Disabled by default.


### INSERT_METHOD


`<code>INSERT_METHOD</code>` is only used with [MERGE](../../../../storage-engines/merge.md) tables. This option determines in which underlying table the new rows should be inserted. If you set it to 'NO' (which is the default) no new rows can be added to the table (but you will still be able to perform `<code>INSERT</code>`s directly against the underlying tables). `<code>FIRST</code>` means that the rows are inserted into the first table, and `<code>LAST</code>` means that thet are inserted into the last table.


### KEY_BLOCK_SIZE


`<code>KEY_BLOCK_SIZE</code>` is used to determine the size of key blocks, in bytes or kilobytes. However, this value is just a hint, and the storage engine could modify or ignore it. If `<code>KEY_BLOCK_SIZE</code>` is set to 0, the storage engine's default value will be used.


With the [InnoDB](../../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/innodb-upgrade-tests/README.md) storage engine, if you specify a non-zero value for the `<code>KEY_BLOCK_SIZE</code>` table option for the whole table, then the table will implicitly be created with the [ROW_FORMAT](#row_format) table option set to `<code>COMPRESSED</code>`.


### MIN_ROWS/MAX_ROWS


`<code>MIN_ROWS</code>` and `<code>MAX_ROWS</code>` let the storage engine know how many rows you are planning to store as a minimum and as a maximum. These values will not be used as real limits, but they help the storage engine to optimize the table. `<code>MIN_ROWS</code>` is only used by MEMORY storage engine to decide the minimum memory that is always allocated. `<code>MAX_ROWS</code>` is used to decide the minimum size for indexes.


### PACK_KEYS


`<code>PACK_KEYS</code>` can be used to determine whether the indexes will be compressed. Set it to 1 to compress all keys. With a value of 0, compression will not be used. With the `<code>DEFAULT</code>` value, only long strings will be compressed. Uncompressed keys are faster.


### PAGE_CHECKSUM


`<code>PAGE_CHECKSUM</code>` is only applicable to [Aria](../../../../storage-engines/s3-storage-engine/aria_s3_copy.md) tables, and determines whether indexes and data should use page checksums for extra safety.


### PAGE_COMPRESSED


`<code>PAGE_COMPRESSED</code>` is used to enable [InnoDB page compression](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/optimization-and-tuning-compression/compression-plugins.md) for [InnoDB](../../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/innodb-upgrade-tests/README.md) tables.


### PAGE_COMPRESSION_LEVEL


`<code>PAGE_COMPRESSION_LEVEL</code>` is used to set the compression level for [InnoDB page compression](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/optimization-and-tuning-compression/compression-plugins.md) for [InnoDB](../../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/innodb-upgrade-tests/README.md) tables. The table must also have the [PAGE_COMPRESSED](#page_compressed) table option set to `<code>1</code>`.


Valid values for `<code>PAGE_COMPRESSION_LEVEL</code>` are 1 (the best speed) through 9 (the best compression), .


### PASSWORD


`<code>PASSWORD</code>` is unused.


### RAID_TYPE


`<code>RAID_TYPE</code>` is an obsolete option, as the raid support has been disabled since MySQL 5.0.


### ROW_FORMAT


The `<code>ROW_FORMAT</code>` table option specifies the row format for the data file. Possible values are engine-dependent.


#### Supported MyISAM Row Formats


For [MyISAM](../../../../storage-engines/myisam-storage-engine/myisam-system-variables.md), the supported row formats are:


* `<code>FIXED</code>`
* `<code>DYNAMIC</code>`
* `<code>COMPRESSED</code>`


The `<code>COMPRESSED</code>` row format can only be set by the [myisampack](../../../../../clients-and-utilities/myisam-clients-and-utilities/myisampack.md) command line tool.


See [MyISAM Storage Formats](../../../../storage-engines/myisam-storage-engine/myisam-storage-formats.md) for more information.


#### Supported Aria Row Formats


For [Aria](../../../../storage-engines/aria/aria-storage-engine.md), the supported row formats are:


* `<code>PAGE</code>`
* `<code>FIXED</code>`
* `<code>DYNAMIC</code>`.


See [Aria Storage Formats](../../../../storage-engines/aria/aria-storage-formats.md) for more information.


#### Supported InnoDB Row Formats


For [InnoDB](../../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/innodb-upgrade-tests/README.md), the supported row formats are:


* `<code>COMPACT</code>`
* `<code>REDUNDANT</code>`
* `<code>COMPRESSED</code>`
* `<code>DYNAMIC</code>`.


If the `<code>ROW_FORMAT</code>` table option is set to `<code>FIXED</code>` for an InnoDB table, then the server will either return an error or a warning depending on the value of the [innodb_strict_mode](../../../../storage-engines/innodb/innodb-system-variables.md#innodb_strict_mode) system variable. If the [innodb_strict_mode](../../../../storage-engines/innodb/innodb-system-variables.md#innodb_strict_mode) system variable is set to `<code>OFF</code>`, then a warning is issued, and MariaDB will create the table using the default row format for the specific MariaDB server version. If the [innodb_strict_mode](../../../../storage-engines/innodb/innodb-system-variables.md#innodb_strict_mode) system variable is set to `<code>ON</code>`, then an error will be raised.


See [InnoDB Storage Formats](../../../../storage-engines/innodb/innodb-row-formats/innodb-row-formats-overview.md) for more information.


#### Other Storage Engines and ROW_FORMAT


Other storage engines do not support the `<code>ROW_FORMAT</code>` table option.


### SEQUENCE


If the table is a [sequence](../../../sequences/README.md), then it will have the `<code>SEQUENCE</code>` set to `<code>1</code>`.


### STATS_AUTO_RECALC


`<code>STATS_AUTO_RECALC</code>` indicates whether to automatically recalculate persistent statistics (see `<code>STATS_PERSISTENT</code>`, below) for an InnoDB table.
If set to `<code>1</code>`, statistics will be recalculated when more than 10% of the data has changed. When set to `<code>0</code>`, stats will be recalculated only when an [ANALYZE TABLE](../../table-statements/analyze-table.md) is run. If set to `<code>DEFAULT</code>`, or left out, the value set by the [innodb_stats_auto_recalc](../../../../storage-engines/innodb/innodb-system-variables.md#innodb_stats_auto_recalc) system variable applies. See [InnoDB Persistent Statistics](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/query-optimizations/statistics-for-optimizing-queries/innodb-persistent-statistics.md).


### STATS_PERSISTENT


`<code>STATS_PERSISTENT</code>` indicates whether the InnoDB statistics created by [ANALYZE TABLE](../../table-statements/analyze-table.md) will remain on disk or not. It can be set to `<code>1</code>` (on disk), `<code>0</code>` (not on disk, the pre-MariaDB 10 behavior), or `<code>DEFAULT</code>` (the same as leaving out the option), in which case the value set by the [innodb_stats_persistent](../../../../storage-engines/innodb/innodb-system-variables.md#innodb_stats_persistent) system variable will apply. Persistent statistics stored on disk allow the statistics to survive server restarts, and provide better query plan stability. See [InnoDB Persistent Statistics](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/query-optimizations/statistics-for-optimizing-queries/innodb-persistent-statistics.md).


### STATS_SAMPLE_PAGES


`<code>STATS_SAMPLE_PAGES</code>` indicates how many pages are used to sample index statistics. If 0 or DEFAULT, the default value, the [innodb_stats_sample_pages](../../../../storage-engines/innodb/innodb-system-variables.md#innodb_stats_sample_pages) value is used. See [InnoDB Persistent Statistics](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/query-optimizations/statistics-for-optimizing-queries/innodb-persistent-statistics.md).


### TRANSACTIONAL


`<code>TRANSACTIONAL</code>` is only applicable for Aria tables. In future Aria tables created with this option will be fully transactional, but currently this provides a form of crash protection. See [Aria Storage Engine](../../../../storage-engines/aria/aria-storage-engine.md) for more details.


### UNION


`<code>UNION</code>` must be specified when you create a MERGE table. This option contains a comma-separated list of MyISAM tables which are accessed by the new table. The list is enclosed between parenthesis. Example: `<code>UNION = (t1,t2)</code>`


### WITH SYSTEM VERSIONING


`<code>WITH SYSTEM VERSIONING</code>` is used for creating [System-versioned tables](../../../temporal-tables/system-versioned-tables.md).


## Partitions


```
|
```

If the `<code>PARTITION BY</code>` clause is used, the table will be [partitioned](../../../../../server-management/partitioning-tables/README.md). A partition method must be explicitly indicated for partitions and subpartitions. Partition methods are:


* `<code>[LINEAR] [HASH](../../../../../server-management/partitioning-tables/partitioning-types/hash-partitioning-type.md)</code>` creates a hash key which will be used to read and write rows. The partition function can be any valid SQL expression which returns an `<code>INTEGER</code>` number. Thus, it is possible to use the [HASH](../../../../../server-management/partitioning-tables/partitioning-types/hash-partitioning-type.md) method on an integer column, or on functions which accept integer columns as an argument. However, `<code>VALUES LESS THAN</code>` and `<code>VALUES IN</code>` clauses can not be used with [HASH](../../../../../server-management/partitioning-tables/partitioning-types/hash-partitioning-type.md). An example:


```
CREATE TABLE t1 (a INT, b CHAR(5), c DATETIME)
    PARTITION BY HASH ( YEAR(c) );
```

`<code>[LINEAR] [HASH](../../../../../server-management/partitioning-tables/partitioning-types/hash-partitioning-type.md)</code>` can be used for subpartitions, too.


* `<code>[LINEAR] [KEY](../../../../../server-management/partitioning-tables/partitioning-types/key-partitioning-type.md)</code>` is similar to [HASH](../../../../../server-management/partitioning-tables/partitioning-types/hash-partitioning-type.md), but the index has an even distribution of data. Also, the expression can only be a column or a list of columns. `<code>VALUES LESS THAN</code>` and `<code>VALUES IN</code>` clauses can not be used with [KEY](../../../../../server-management/partitioning-tables/partitioning-types/key-partitioning-type.md).
* [RANGE](../../../../../server-management/partitioning-tables/partitioning-types/range-partitioning-type.md) partitions the rows using on a range of values, using the `<code>VALUES LESS THAN</code>` operator. `<code>VALUES IN</code>` is not allowed with `<code>RANGE</code>`. The partition function can be any valid SQL expression which returns a single value.
* [LIST](../../../../../server-management/partitioning-tables/partitioning-types/list-partitioning-type.md) assigns partitions based on a table's column with a restricted set of possible values. It is similar to `<code>RANGE</code>`, but `<code>VALUES IN</code>` must be used for at least 1 columns, and `<code>VALUES LESS THAN</code>` is disallowed.
* `<code>SYSTEM_TIME</code>` partitioning is used for [System-versioned tables](../../../temporal-tables/system-versioned-tables.md) to store historical data separately from current data.


Only [HASH](../../../../../server-management/partitioning-tables/partitioning-types/hash-partitioning-type.md) and [KEY](../../../../../server-management/partitioning-tables/partitioning-types/key-partitioning-type.md) can be used for subpartitions, and they can be `<code>[LINEAR]</code>`.


It is possible to define up to 8092 partitions and subpartitions.


The number of defined partitions can be optionally specified as `<code>PARTITION count</code>`. This can be done to avoid specifying all partitions individually. But you can also declare each individual partition and, additionally, specify a `<code>PARTITIONS count</code>` clause; in the case, the number of `<code>PARTITION</code>`s must equal count.


Also see [Partitioning Types Overview](../../../../../server-management/partitioning-tables/partitioning-types/partitioning-types-overview.md).



##### MariaDB starting with [10.7.1](../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-7-series/mariadb-1071-release-notes.md)
From [MariaDB 10.7](../../../../../../release-notes/mariadb-community-server/what-is-mariadb-107.md), the PARTITION keyword is now optional as part of the partition definition, for example, instead of:

```
create or replace table t1 (x int)
  partition by range(x) (
    partition p1 values less than (10),
    partition p2 values less than (20),
    partition p3 values less than (30),
    partition p4 values less than (40),
    partition p5 values less than (50),
    partition pn values less than maxvalue);
```
the following can also be used:

```
create or replace table t1 (x int)
  partition by range(x) (
    p1 values less than (10),
    p2 values less than (20),
    p3 values less than (30),
    p4 values less than (40),
    p5 values less than (50),
    pn values less than maxvalue);
```


## Sequences


`<code>CREATE TABLE</code>` can also be used to create a [SEQUENCE](../../../sequences/README.md). See [CREATE SEQUENCE](../../../sequences/create-sequence.md) and [Sequence Overview](../../../sequences/sequence-overview.md).


## Atomic DDL



##### MariaDB starting with [10.6.1](../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-1061-release-notes.md)
[MariaDB 10.6.1](../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-1061-release-notes.md) supports [Atomic DDL](../atomic-ddl.md). `<code>CREATE TABLE</code>` is atomic, except for `<code>CREATE OR REPLACE</code>`, which is only crash safe. 


## Examples


```
create table if not exists test (
a bigint auto_increment primary key,
name varchar(128) charset utf8,
key name (name(32))
) engine=InnoDB default charset latin1;
```

This example shows a couple of things:


* Usage of `<code class="highlight fixed" style="white-space:pre-wrap">IF NOT EXISTS</code>`; If the table already existed, it will not be created. There will not be any error for the client, just a warning.
* How to create a `<code class="highlight fixed" style="white-space:pre-wrap">PRIMARY KEY</code>` that is [automatically generated](../../../../storage-engines/innodb/auto_increment-handling-in-innodb.md).
* How to specify a table-specific [character set](../../../../data-types/string-data-types/character-sets/README.md) and another for a column.
* How to create an index (`<code class="highlight fixed" style="white-space:pre-wrap">name</code>`) that is only partly indexed (to save space).


The following clauses will work:


```
CREATE TABLE t1(
  a int DEFAULT (1+1),
  b int DEFAULT (a+1),
  expires DATETIME DEFAULT(NOW() + INTERVAL 1 YEAR),
  x BLOB DEFAULT USER()
);
```

## See Also


* [Identifier Names](../../../sql-language-structure/identifier-names.md)
* [ALTER TABLE](../alter/alter-tablespace.md)
* [DROP TABLE](../drop/drop-tablespace.md)
* [Character Sets and Collations](../../../../data-types/string-data-types/character-sets/supported-character-sets-and-collations.md)
* [SHOW CREATE TABLE](../../administrative-sql-statements/show/show-create-table.md)
* [CREATE TABLE with Vectors](../../../vectors/create-table-with-vectors.md)
* Storage engines can add their own [attributes for columns, indexes and tables](../../../../storage-engines/storage-engines-storage-engine-development/engine-defined-new-tablefieldindex-attributes.md)
* Variable [slave-ddl-exec-mode](../../../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md)
* [InnoDB Limitations](https://mariadb.com/kb/en/InnoDB_Limitations)

