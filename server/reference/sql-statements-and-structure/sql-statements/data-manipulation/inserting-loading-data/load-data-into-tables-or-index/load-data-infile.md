
# LOAD DATA INFILE

## Syntax


```
LOAD DATA [LOW_PRIORITY | CONCURRENT] [LOCAL] INFILE 'file_name'
    [REPLACE | IGNORE]
    INTO TABLE tbl_name
    [CHARACTER SET charset_name]
    [{FIELDS | COLUMNS}
        [TERMINATED BY 'string']
        [[OPTIONALLY] ENCLOSED BY 'char']
        [ESCAPED BY 'char']
    ]
    [LINES
        [STARTING BY 'string']
        [TERMINATED BY 'string']
    ]
    [IGNORE number {LINES|ROWS}]
    [(col_name_or_user_var,...)]
    [SET col_name = expr,...]
```


## Description


`LOAD DATA INFILE` is [unsafe](../../../../../../server-usage/replication-cluster-multi-master/standard-replication/unsafe-statements-for-statement-based-replication.md) for statement-based replication.


Reads rows from a text file into the designated table on the database at a very high speed. The file name must be given as a literal string.


Files are written to disk using the [SELECT INTO OUTFILE](../../selecting-data/select-into-outfile.md) statement. You can then read the files back into a table using the `LOAD DATA INFILE` statement. The `FIELDS` and `LINES` clauses are the same in both statements and by default fields are expected to be terminated with tabs (`\t`) and lines with newlines (`\n`). These clauses are optional, but if both are specified then the `FIELDS` clause must precede `LINES`.


Executing this statement activates `INSERT` [triggers](../../../../../../server-usage/programming-customizing-mariadb/triggers-events/triggers/triggers-and-implicit-locks.md).


One must have the [FILE](../../../account-management-sql-commands/grant.md#file) privilege to be able to execute LOAD DATA INFILE. This is to ensure normal users cannot read system files. LOAD DATA LOCAL INFILE does not have this requirement.


If the [secure_file_priv](../../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#secure_file_priv) system variable is set (by default it is not), the loaded file must be present in the specified directory.


Note that MariaDB's [systemd](../../../../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/systemd.md) unit file restricts access to `/home`, `/root`, and `/run/user` by default. See [Configuring access to home directories](../../../../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/systemd.md#configuring-access-to-home-directories).


### `LOAD DATA LOCAL INFILE`


When you execute the `LOAD DATA INFILE` statement, MariaDB Server attempts to read the input file from its own file system. By contrast, when you execute the `LOAD DATA LOCAL INFILE` statement, the client attempts to read the input file from its file system, and it sends the contents of the input file to the MariaDB Server. This allows you to load files from the client's local file system into the database.


If you don't want to permit this operation (perhaps for security reasons), you can disable the `LOAD DATA LOCAL INFILE` statement on either the server or the client.


* The `LOAD DATA LOCAL INFILE` statement can be disabled on the server by setting the [local_infile](../../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#local_infile) system variable to `0`.
* The `LOAD DATA LOCAL INFILE` statement can be disabled on the client. If you are using [MariaDB Connector/C](../../../../../../../connectors/mariadb-connector-c/about-mariadb-connector-c.md), this can be done by unsetting the `CLIENT_LOCAL_FILES` capability flag with the [mysql_real_connect](../../../../../../../connectors/mariadb-connector-c/mariadb-connectorc-api-functions/mysql_real_connect.md) function or by unsetting the `MYSQL_OPT_LOCAL_INFILE` option with [mysql_optionsv](../../../../../../../connectors/mariadb-connector-c/mariadb-connectorc-api-functions/mysql_optionsv.md) function. If you are using a different client or client library, then see the documentation for your specific client or client library to determine how it handles the `LOAD DATA LOCAL INFILE` statement.


* The `LOAD DATA LOCAL INFILE` strict modes like `STRICT_TRANS_TABLES` are disabled with keyword "local". ([MDEV-11235](https://jira.mariadb.org/browse/MDEV-11235))


If the `LOAD DATA LOCAL INFILE` statement is disabled by either the server or the client and if the user attempts to execute it, then the server will cause the statement to fail with the following error message:


```
The used command is not allowed with this MariaDB version
```

Note that it is not entirely accurate to say that the MariaDB version does not support the command. It would be more accurate to say that the MariaDB configuration does not support the command. See [MDEV-20500](https://jira.mariadb.org/browse/MDEV-20500) for more information.


From [MariaDB 10.5.2](../../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1052-release-notes.md), the error message is more accurate:


```
The used command is not allowed because the MariaDB server or client 
  has disabled the local infile capability
```

### `REPLACE` and `IGNORE`


If you load data from a file into a table that already contains data and has a [primary key](../../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/optimization-and-indexes/getting-started-with-indexes.md#primary-key), you may encounter issues where the statement attempts to insert a row with a primary key that already exists. When this happens, the statement fails with Error 1064, protecting the data already on the table. If you want MariaDB to overwrite duplicates, use the `REPLACE` keyword.


The `REPLACE` keyword works like the [REPLACE](../../../built-in-functions/string-functions/replace-function.md) statement. Here, the statement attempts to load the data from the file. If the row does not exist, it adds it to the table. If the row contains an existing primary key, it replaces the table data. That is, in the event of a conflict, it assumes the file contains the desired row.


This operation can cause a degradation in load speed by a factor of 20 or more if the part that has already been loaded is larger than the capacity of the [InnoDB Buffer Pool](../../../../../storage-engines/innodb/innodb-buffer-pool.md). This happens because it causes a lot of turnaround in the buffer pool.


Use the `IGNORE` keyword when you want to skip any rows that contain a conflicting primary key. Here, the statement attempts to load the data from the file. If the row does not exist, it adds it to the table. If the row contains an existing primary key, it ignores the addition request and moves on to the next. That is, in the event of a conflict, it assumes the table contains the desired row.


### `IGNORE number {LINES|ROWS}`


The `IGNORE number LINES` syntax can be used to ignore a number of rows from the beginning of the file. Most often this is needed when the file starts with one row that includes the column headings.


### Character-sets


When the statement opens the file, it attempts to read the contents using the default character-set, as defined by the [character_set_database](../../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#character_set_database) system variable.


In the cases where the file was written using a character-set other than the default, you can specify the character-set to use with the `CHARACTER SET` clause in the statement. It ignores character-sets specified by the [SET NAMES](../../../../../data-types/string-data-types/character-sets/set-names.md) statement and by the [character_set_client](../../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#character_set_client) system variable. Setting the `CHARACTER SET` clause to a value of `binary` indicates "no conversion."


The statement interprets all fields in the file as having the same character-set, regardless of the column data type. To properly interpret file contents, you must ensure that it was written with the correct character-set. If you write a data file with [mariadb-dump -T](../../../../../../clients-and-utilities/backup-restore-and-import-clients/mariadb-dump.md) or with the [SELECT INTO OUTFILE](../../selecting-data/select-into-outfile.md) statement with the [mariadb](../../../../../../clients-and-utilities/mariadb-client/mariadb-command-line-client.md) client, be sure to use the `--default-character-set` option, so that the output is written with the desired character-set.


When using mixed character sets, use the `CHARACTER SET` clause in both [SELECT INTO OUTFILE](../../selecting-data/select-into-outfile.md) and `LOAD DATA INFILE` to ensure that MariaDB correctly interprets the escape sequences.


The [character_set_filesystem](../../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#character_set_filesystem) system variable controls the interpretation of the filename.
It is currently not possible to load data files that use the `ucs2` character set.


### Preprocessing Inputs


*col_name_or_user_var* can be a column name, or a user variable. In the case of a variable, the [SET](../../../../../../../connectors/mariadb-connector-cpp/setup-for-connector-cpp-examples.md) statement can be used to preprocess the value before loading into the table.


### Priority and Concurrency


In storage engines that perform table-level locking ([MyISAM](../../../../../storage-engines/myisam-storage-engine/myisam-system-variables.md), [MEMORY](../../../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/mariadb-fault-finding/memory-is-leaking.md) and [MERGE](../../../../../storage-engines/merge.md)), using the [LOW_PRIORITY](../../changing-deleting-data/high_priority-and-low_priority.md) keyword, MariaDB delays insertions until no other clients are reading from the table. Alternatively, when using the [MyISAM](../../../../../storage-engines/myisam-storage-engine/myisam-system-variables.md) storage engine, you can use the [CONCURRENT](../concurrent-inserts.md) keyword to perform concurrent insertion.


The `LOW_PRIORITY` and `CONCURRENT` keywords are mutually exclusive.  They cannot be used in the same statement.


### Progress Reporting


The `LOAD DATA INFILE` statement supports [progress reporting](../../../../../mariadb-internals/using-mariadb-with-your-programs-api/progress-reporting.md). You may find this useful when dealing with long-running operations. Using another client you can issue a [SHOW PROCESSLIST](../../../administrative-sql-statements/show/show-processlist.md) query to check the progress of the data load.


### Using mariadb-import


MariaDB ships with a separate utility for loading data from files: [mariadb-import](../../../../../../clients-and-utilities/backup-restore-and-import-clients/mariadb-import.md) (or `mysqlimport` before [MariaDB 10.5](../../../../../../../release-notes/mariadb-community-server/what-is-mariadb-105.md)). It operates by sending `LOAD DATA INFILE` statements to the server.


Using [mariadb-import](../../../../../../clients-and-utilities/backup-restore-and-import-clients/mariadb-import.md) you can compress the file using the `--compress` option, to get better performance over slow networks, providing both the client and server support the compressed protocol. Use the `--local` option to load from the local file system.


### Indexing


In cases where the storage engine supports [ALTER TABLE... DISABLE KEYS](../../../data-definition/alter/alter-tablespace.md#enable-disable-keys) statements ([MyISAM](../../../../../storage-engines/myisam-storage-engine/myisam-system-variables.md) and [Aria](../../../../../storage-engines/s3-storage-engine/aria_s3_copy.md)), the `LOAD DATA INFILE` statement automatically disables indexes during the execution.


## Examples


You have a file with this content (note the the separator is ',', not tab, which is the default):


```
2,2
3,3
4,4
5,5
6,8
```

```
CREATE TABLE t1 (a int, b int, c int, d int, PRIMARY KEY (a));
LOAD DATA LOCAL INFILE 
 '/tmp/loaddata7.dat' INTO TABLE t1 FIELDS TERMINATED BY ',' (a,b) SET c=a+b;
SELECT * FROM t1;
+------+------+------+
| a    | b    | c    |
+------+------+------+
|    2 |    2 |    4 |
|    3 |    3 |    6 |
|    4 |    4 |    8 |
|    5 |    5 |   10 |
|    6 |    8 |   14 |
+------+------+------+
```

Another example, given the following data (the separator is a tab):


```
1       a
2       b
```

The value of the first column is doubled before loading:


```
LOAD DATA INFILE 'ld.txt' INTO TABLE ld (@i,v) SET i=@i*2;

SELECT * FROM ld;
+------+------+
| i    | v    |
+------+------+
|    2 | a    |
|    4 | b    |
+------+------+
```

## See Also


* [How to quickly insert data into MariaDB](../../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/query-optimizations/how-to-quickly-insert-data-into-mariadb.md)
* [Character Sets and Collations](../../../../../data-types/string-data-types/character-sets/supported-character-sets-and-collations.md)
* [SELECT ... INTO OUTFILE](../../selecting-data/select-into-outfile.md)
* [mariadb-import](../../../../../../clients-and-utilities/backup-restore-and-import-clients/mariadb-import.md)

