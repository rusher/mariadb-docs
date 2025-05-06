
# MariaDB Enterprise ColumnStore Data Loading with LOAD DATA INFILE


# Overview


MariaDB Enterprise ColumnStore automatically translates `LOAD DATA [ LOCAL ] INFILE` statements into bulk data loads. By default, it translates the statement into a bulk data load that uses cpimport.bin, which is an internal wrapper around the cpimport tool.


# Intended Use Cases


You can load data using the [LOAD DATA INFILE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/data-manipulation/inserting-loading-data/load-data-into-tables-or-index/load-data-infile) statement in the following cases:


* You are loading data into a ColumnStore table from a text file stored on the primary node's file system.
* You are loading data into a ColumnStore table from a text file stored on the client's file system. In this case, `LOAD DATA LOCAL INFILE` must be used.


# Batch Insert Mode


![ECStoreDataLoadingS3FlowChart](../.gitbook/assets/mariadb-enterprise-columnstore-data-loading-with-load-data-infile/+image/ecstoredataloadings3flowchart.png "ECStoreDataLoadingS3FlowChart")


MariaDB Enterprise ColumnStore enables batch insert mode by default.


When batch insert mode is enabled, MariaDB Enterprise ColumnStore has special handling for [LOAD DATA INFILE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/data-manipulation/inserting-loading-data/load-data-into-tables-or-index/load-data-infile) statements.


Enterprise ColumnStore uses the following rules:


* If the statement is executed outside of a transaction, Enterprise ColumnStore loads the data using [cpimport](mariadb-enterprise-columnstore-data-loading-with-cpimport.md), which is a command-line utility that is designed to efficiently load data in bulk. Enterprise ColumnStore executes cpimport using a wrapper called `cpimport.bin`.
* If the statement is executed inside of a transaction, Enterprise ColumnStore loads the data using the DML interface, which is slower.


Batch insert mode can be disabled by setting the `columnstore_use_import_for_batchinsert` system variable to OFF. When batch insert mode is disabled, Enterprise ColumnStore executes the statements using the DML interface, which is slower.


# Insert Cache


Starting with MariaDB Enterprise ColumnStore 6, an insert cache can be enabled to speed up [LOAD DATA INFILE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/data-manipulation/inserting-loading-data/load-data-into-tables-or-index/load-data-infile) statements.


The insert cache is disabled by default, but it can be enabled by configuring `columnstore_cache_inserts=ON`:


```
[mariadb]
...
columnstore_cache_inserts=ON\
```

The cache is flushed to ColumnStore in the following scenarios:


When the number of cached rows exceeds the value of `columnstore_cache_flush_threshold`


When a statement other than [INSERT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/data-manipulation/inserting-loading-data/insert) or [LOAD DATA INFILE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/data-manipulation/inserting-loading-data/load-data-into-tables-or-index/load-data-infile) is executed


[cpimport](mariadb-enterprise-columnstore-data-loading-with-cpimport.md) is used to flush the insert cache to ColumnStore when `columnstore_cache_use_import=ON` is configured.


# Locking


MariaDB Enterprise ColumnStore requires a write metadata lock (MDL) on the table when a bulk data load is performed with [cpimport](mariadb-enterprise-columnstore-data-loading-with-cpimport.md).


When a bulk data load is running:


* Read queries will not be blocked.
* Write queries and concurrent bulk data loads on the same table will be blocked until the bulk data load operation is complete, and the write metadata lock on the table has been released.
* The write metadata lock (MDL) can be monitored with the [METADATA_LOCK_INFO plugin](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/other-plugins/metadata-lock-info-plugin).


# Import the Schema


Before data can be imported into the tables, the schema must be created.


1. Connect to the primary server using [MariaDB Client](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/mariadb-client/):


```
$ mariadb --host 192.168.0.100 --port 5001 \
      --user db_user --password \
      --default-character-set=utf8
```

After the command is executed, it will prompt you for a password.


2. For each database that you are importing, create the database with the [CREATE DATABASE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/data-definition/create/create-database) statement:


```
CREATE DATABASE inventory;
```

For each table that you are importing, create the table with the [CREATE TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/data-definition/create/create-table) statement:


```
CREATE TABLE inventory.products (
   product_name varchar(11) NOT NULL DEFAULT '',
   supplier varchar(128) NOT NULL DEFAULT '',
   quantity varchar(128) NOT NULL DEFAULT '',
   unit_cost varchar(128) NOT NULL DEFAULT ''
) ENGINE=Columnstore DEFAULT CHARSET=utf8;
```

**Note:** To get the best performance from Enterprise ColumnStore, make sure to follow Enterprise ColumnStore's best practices for schema design. 


# Appends Data


When MariaDB Enterprise ColumnStore performs a bulk data load, it appends data to the table in the order in which the data is read. Appending data reduces the I/O requirements of bulk data loads, so that larger data sets can be loaded very efficiently.


While the bulk load is in progress, the newly appended data is temporarily hidden from queries.


After the bulk load is complete, the newly appended data is visible to queries.


# Sort the Input File


When MariaDB Enterprise ColumnStore performs a bulk data load, it appends data to the table in the order in which the data is read.


The order of data can have a significant effect on performance with Enterprise ColumnStore, so it can be helpful to sort the data in the input file prior to importing it.


For additional information, see "[Load Ordered Data in Proper Order](../columnstore-performance-tuning/columnstore-query-tuning/query-tuning-recommendations-for-mariadb-enterprise-columnstore.md#load-ordered-data-in-proper-order)".


# Confirm the Field Delimiter


Before importing a file into MariaDB Enterprise ColumnStore, confirm that the field delimiter is not present in the data.


The field delimiter is determined by the `columnstore_import_for_batchinsert_delimiter` system variable. By default, Enterprise ColumnStore sets the field delimiter to the `ASCII value 7`, which corresponds to the `BEL` character.


To use another delimiter, you can set the field delimiter.


# Load a Local Input File on the Client


If you are loading a file located on the client, you can use the [LOAD DATA LOCAL INFILE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/data-manipulation/inserting-loading-data/load-data-into-tables-or-index/load-data-infile) statement. However, for this statement to work, the client must explicitly enable usage of a local infile.


If you are using [MariaDB Client](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/mariadb-client/) the `--local-infile` option can be used:


```
$ mariadb --host 192.168.0.1 \
      --user db_user --password \
      --default-character-set=utf8 \
      --local-infile
```

If you are using [MariaDB Connector/C](/en/about-mariadb-connector-c/), the `MYSQL_OPT_LOCAL_INFILE` option can be set with the `mysql_optionsv()` function:


```
/* enable local infile */
unsigned int enable_local_infile = 1;
mysql_optionsv(mysql, MYSQL_OPT_LOCAL_INFILE, (void *) &enable_local_infile);
```

If you are using [MariaDB Connector/J](/en/about-mariadb-connector-j/), the `allowLocalInfile` parameter can be set for the connection:


```
Connection connection = DriverManager.getConnection("jdbc:mariadb://192.168.0.1/test?user=test_user&password=myPassword&allowLocalInfile=true");
```

If you are using [MariaDB Connector/Node.js](/en/about-mariadb-connector-nodejs/), the `permitLocalInfile` parameter can be set for the connection:


```
mariadb.createConnection({
   host: '192.168.0.1',
   user:'test_user',
   password: 'myPassword',
   permitLocalInfile: 'true'
 });
```

If you are using [MariaDB Connector/Python](/en/mariadb-connector-python/), the `local_infile` parameter can be set for the connection:


```
conn = mariadb.connect(
   user="test_user",
   password="myPassword",
   host="192.168.0.1",
   port=3306,
   local_infile=true)
Set the Field Delimiter
```

The default field delimiter for the [LOAD DATA INFILE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/data-manipulation/inserting-loading-data/load-data-into-tables-or-index/load-data-infile) statement is a tab.


If your data file uses a different field delimiter, you can specify the field delimiter with the `FIELDS TERMINATED BY` clause.


To load a `TSV (tab-separated values)` file:


```
LOAD DATA INFILE 'inventory-products.tsv'
INTO TABLE inventory.products;
To load a CSV (comma-separated values) file:
```

```
LOAD DATA LOCAL INFILE 'inventory-products.csv'
INTO TABLE accounts.contacts
FIELDS TERMINATED BY ',';
```

# Set the Quoting Style


By default, the [LOAD DATA INFILE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/data-manipulation/inserting-loading-data/load-data-into-tables-or-index/load-data-infile) statement does not expect fields to be quoted.


If your data file uses quotes around fields, you can specify the quote character with the `FIELDS [OPTIONALLY] ENCLOSED BY` clause.


To load a `TSV (tab-separated values)` file that uses double quotes:


```
LOAD DATA INFILE 'inventory-products.tsv'
INTO TABLE inventory.products
FIELDS ENCLOSED BY '"';
To load a CSV (comma-separated values) file that uses optional single quotes:
```

```
LOAD DATA LOCAL INFILE 'inventory-products.csv'
INTO TABLE accounts.contacts
FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '\'';
```

# Special Handling


## ON DUPLICATE KEY


MariaDB Enterprise ColumnStore ignores the `ON DUPLICATE KEY` clause.


Please ensure that duplicate data is removed prior to performing a bulk data load.


Copyright © 2025 MariaDB

