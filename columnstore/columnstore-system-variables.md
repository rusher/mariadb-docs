
# ColumnStore System Variables

 
1. [Variables "Variables"](#variables)
1. [Compression mode "Compression mode"](#compression-mode)
1. [ColumnStore decimal to double math "ColumnStore decimal to double math"](#columnstore-decimal-to-double-math)
1. [Disk-based joins "Disk-based joins"](#disk-based-joins)
1. [Batch insert mode for INSERTS "Batch insert mode for INSERTS"](#batch-insert-mode-for-inserts)
1. [Local PM query mode "Local PM query mode"](#local-pm-query-mode)
1. [Operating mode "Operating mode"](#operating-mode)





## Variables



| Name | Cmd-Line | Scope | Data type | Default Value | Range |
| --- | --- | --- | --- | --- | --- |
| Name | Cmd-Line | Scope | Data type | Default Value | Range |
| [infinidb_compression_type](#compression-mode) | Yes | Both | enumeration | 2 | 0,2 |
| [infinidb_decimal_scale](#columnstore-decimal-scale) | Yes | Both | numeric | 8 |  |
| [infinidb_diskjoin_bucketsize](#disk-based-joins) | Yes | Both | numeric | 100 |  |
| [infinidb_diskjoin_largesidelimit](#disk-based-joins) | Yes | Both | numeric | 0 |  |
| [infinidb_diskjoin_smallsidelimit](#disk-based-joins) | Yes | Both | numeric | 0 |  |
| [infinidb_double_for_decimal_math](#columnstore-decimal-to-double-math) | Yes | Both | enumeration | OFF | OFF, ON |
| [infinidb_import_for_batchinsert_delimiter](#batch-insert-mode-for-inserts) | Yes | Both | numeric | 7 |  |
| [infinidb_import_for_batchinsert_enclosed_by](#batch-insert-mode-for-inserts) | Yes | Both | numeric | 17 |  |
| [infinidb_local_query](#local-pm-query-mode) | Yes | Both | enumeration | 0 | 0,1 |
| infinidb_ordered_only | Yes | Both | enumeration | OFF | OFF, ON |
| infinidb_string_scan_threshold | Yes | Both | numeric | 10 |  |
| infinidb_stringtable_threshold | Yes | Both | numeric | 20 |  |
| [infinidb_um_mem_limit](#disk-based-joins) | Yes | Both | numeric | 0 |  |
| [infinidb_use_decimal_scale](#columnstore-decimal-scale) | Yes | Both | enumeration | OFF | OFF, ON |
| [infinidb_use_import_for_batchinsert](#batch-insert-mode-for-inserts) | Yes | Both | enumeration | ON | OFF, ON |
| infinidb_varbin_always_hex | Yes | Both | enumeration | ON | OFF, ON |
| [infinidb_vtable_mode](#operating-mode) | Yes | Both | enumeration | 1 | 0,1,2 |



`<code class="unknown_macro"><<<span class="macro_name">toc</span><span class="macro_arg_string"></span>>></code>`


## Compression mode


MariaDB ColumnStore has the ability to compress data and this is controlled through a compression mode. This compression mode may be set as a default for the instance or set at the session level.


To set the compression mode at the session level, the following command is used. Once the session has ended, any subsequent session will return to the default for the instance.


```
set infinidb_compression_type = n
```

where n is:


* 0) compression is turned off. Any subsequent table create statements run will have compression turned off for that table unless any statement overrides have been performed. Any alter statements run to add a column will have compression turned off for that column unless any statement override has been performed.
* 2) compression is turned on. Any subsequent table create statements run will have compression turned on for that table unless any statement overrides have been performed. Any alter statements run to add a column will have compression turned on for that column unless any statement override has been performed. ColumnStore uses snappy compression in this mode.


## ColumnStore decimal to double math


`<code class="unknown_macro"><<<span class="macro_name">toc</span><span class="macro_arg_string"> title='' layout=standalone</span>>></code>`
MariaDB ColumnStore has the ability to change intermediate decimal mathematical results from decimal type to double. The decimal type has approximately 17-18 digits of precision, but a smaller maximum range. Whereas the double type has approximately 15-16 digits of precision, but a much larger maximum range. 
In typical mathematical and scientific applications, the ability to avoid overflow in intermediate results with double math is likely more beneficial than the additional two digits of precisions. In banking applications, however, it may be more appropriate to leave in the default decimal setting to ensure accuracy to the least significant digit.


### Enable/Disable decimal to double math


The infinidb_double_for_decimal_math variable is used to control the data type for intermediate decimal results. This decimal for double math may be set as a default for the instance, set at the session level, or at the statement level by toggling this variable on and off.


To enable/disable the use of the decimal to double math at the session level, the following command is used. Once the session has ended, any subsequent session will return to the default for the instance.


```
set infinidb_double_for_decimal_math = on
```

where n is:


* off (disabled, default)
* on (enabled)


### ColumnStore decimal scale


ColumnStore has the ability to support varied internal precision on decimal calculations. *infinidb_decimal_scale* is used internally by the ColumnStore engine to control how many significant digits to the right of the decimal point are carried through in suboperations on calculated columns. If, while running a query, you receive the message ‘aggregate overflow’, try reducing *infinidb_decimal_scale* and running the query again. Note that,as you decrease *infinidb_decimal_scale*, you may see reduced accuracy in the least significant digit(s) of a returned calculated column. *infinidb_use_decimal_scale* is used internally by the ColumnStore engine to turn the use of this internal precision on and off. These two system variables may be set as a default for the instance or set at the session level.


#### Enable/disable decimal scale


To enable/disable the use of the decimal scale at the session level, the following command is used. Once the session has ended, any subsequent session will return to the default for the instance.


```
set infinidb_use_decimal_scale = on
```

where *n* is off (disabled) or on (enabled).


#### Set decimal scale level


To set the decimal scale at the session level, the following command is used. Once the session has ended, any subsequent session will return to the default for the instance.


```
set infinidb_decimal_scale = n
```

where *n* is the amount of precision desired for calculations.


## Disk-based joins


`<code class="unknown_macro"><<<span class="macro_name">toc</span><span class="macro_arg_string"> title='' layout=standalone</span>>></code>`


### Introduction


Joins are performed in-memory on the [UM](columnstore-architecture/columnstore-user-module.md) node. When a join operation exceeds the memory allocated on the UM for query joins, the query is aborted with an error code IDB-2001.
Disk-based joins enable such queries to use disk for intermediate join data in case when the memory needed for join exceeds the memory limit on the UM. Although slower in performance as compared to a fully in-memory join, and bound by the temporary space on disk, it does allow such queries to complete. 
**Note:Disk-based joins does not include aggregation and DML joins.**


The following variables in the *HashJoin* element in the Columnstore.xml configuration file relate to disk-based joins. Columnstore.xml resides in the etc directory for your installation(/usr/local/mariadb/columnstore/etc).


* AllowDiskBasedJoin – Option to use disk-based joins. Valid values are Y (enabled) or N (disabled). Default is disabled.
* TempFileCompression – Option to use compression for disk join files. Valid values are Y (use compressed files) or N (use non-compressed files).
* TempFilePath – The directory path used for the disk joins. By default, this path is the tmp directory for your installation (i.e., /usr/local/mariadb/columnstore/tmp). Files (named infinidb-join-data*) in this directory will be created and cleaned on an as needed basis. The entire directory is removed and recreated by ExeMgr at startup.)


**Note: When using disk-based joins, it is strongly recommended that the TempFilePath reside on its own partition as the partition may fill up as queries are executed.**


### Per user join memory limit


In addition to the system wide flags, at SQL global and session level, the following system variables exists for managing per user memory limit for joins.


* infinidb_um_mem_limit - A value for memory limit in MB per user. When this limit is exceeded by a join, it will switch to a disk-based join. By default the limit is not set (value of 0).


For modification at the global level:
In my.cnf file (typically /usr/local/mariadb/columnstore/mysql):


```
[mysqld]
...
infinidb_um_mem_limit = value
where value is the value in Mb for in memory limitation per user.
```

For modification at the session level, before issuing your join query from the SQL client, set the session variable as follows.


```
set infinidb_um_mem_limit = value
```


## Batch insert mode for INSERTS


`<code class="unknown_macro"><<<span class="macro_name">toc</span><span class="macro_arg_string"> title='' layout=standalone</span>>></code>`


### Introduction


MariaDB ColumnStore has the ability to utilize the cpimport fast data import tool for non-transactional [LOAD DATA INFILE](../server/reference/sql-statements-and-structure/sql-statements/data-manipulation/inserting-loading-data/load-data-into-tables-or-index/load-data-infile.md) and [INSERT INTO SELECT FROM](../server/reference/sql-statements-and-structure/sql-statements/built-in-functions/string-functions/insert-function.md) SQL statements. Using this method results in a significant increase in performance in loading data through these two SQL statements. This optimization is independent of the storage engine used for the tables in the select statement.


### Enable/disable using cpimport for batch insert


The infinidb_use_import_for_batchinsert variable is used to control if cpimport is used for these statements. This variable may be set as a default for the instance, set at the session level, or at the statement level by toggling this variable on and off.


To enable/disable the use of the use cpimport for batch insert at the session level, the following command is used. Once the session has ended, any subsequent session will return to the default for the instance.


```
set infinidb_use_import_for_batchinsert = n
where n is:
* 0 (disabled)
* 1 (enabled)
```

### Changing default delimiter for INSERT SELECT


* The infinidb_import_for_batchinsert_delimiter variable is used internally by MariaDB ColumnStore on a non-transactional INSERT INTO SELECT FROM statement as the default delimiter passed to the cpimport tool. With a default value ascii 7, there should be no need to change this value unless your data contains ascii 7 values.


To change this variable value at the at the session level, the following command is used. Once the session has ended, any subsequent session will return to the default for the instance.


```
set infinidb_import_for_batchinsert_delimiter = ascii_value
where ascii_value is an ascii value representation of the delimiter desired.
```

Note that this setting may cause issues with multi byte character set data. It is recommended to utilize UTF8 files directly with cpimport.


### Version buffer file management


If the following error is received, most likely with a transaction LOAD DATA INFILE or INSERT INTO SELECT then it is recommended to break up the load into multiple smaller chunks, increase the VersionBufferFileSize setting, or consider a non transactional LOAD DATA INFILE or to use cpimport.


```
ERROR 1815 (HY000) at line 1 in file: 'ldi.sql': Internal error: CAL0006: IDB-2008: The version buffer overflowed. Increase VersionBufferFileSize or limit the rows to be processed.
```

The VersionBufferFileSize setting is updated in the ColumnStore.xml typically located under /usr/local/mariadb/columnstore/etc. This dictates the size of the version buffer file on disk which provides DML transactional consistency. The default value is '1GB' which reserves up to a 1 Gigabyte file size. Modify this on the PM1 node and restart the system if you require a larger value.


## Local PM query mode


MariaDB ColumnStore has the ability to query data from just a single [PM](columnstore-architecture/columnstore-performance-module.md) instead of the whole database through the [UM](columnstore-architecture/columnstore-user-module.md). In order to accomplish this, the infinidb_local_query variable in the my.cnf configuration file is used and maybe set as a default at system wide or set at the session level.


`<code class="unknown_macro"><<<span class="macro_name">toc</span><span class="macro_arg_string"> title='' layout=standalone</span>>></code>`


### Enable local PM query during installation


Local PM query can be enabled system wide during the install process when running the install script postConfigure. Answer 'y' to this prompt during the install process.


```
NOTE: Local Query Feature allows the ability to query data from a single Performance
      Module. Check MariaDB ColumnStore Admin Guide for additional information.

Enable Local Query feature? [y,n] (n) >
```

[installing-and-configuring-a-multi-server-columnstore-system-11x.md](columnstore-getting-started/preparing-and-installing-mariadb-columnstore-11x/installing-and-configuring-a-multi-server-columnstore-system-11x.md)


### Enable local PM query systemwide


To enable the use of the local PM Query at the instance level, specify `<code>infinidb_local_query =1</code>` (enabled) in the my.cnf configuration file at /usr/local/mariadb/columnstore/mysql. The default is 0 (disabled).


### Enable/disable local PM query at the session level


To enable/disable the use of the local PM Query at the session level, the following command is used. Once the session has ended, any subsequent session will return to the default for the instance.


```
set infinidb_local_query = n
where n is:
* 0 (disabled)
* 1 (enabled)
```

At the session level, this variable applies only to executing a query on an individual [PM](columnstore-architecture/columnstore-performance-module.md) and will error if executed on the [UM](columnstore-architecture/columnstore-user-module.md). The PM must be set up with the local query option during installation.


### Local PM Query Examples


#### Example 1 - SELECT from a single table on local PM to import back on local PM:


With the infinidb_local_query variable set to 1 (default with local PM Query):


```
mcsmysql -e 'select * from source_schema.source_table;' –N | /usr/local/Calpont/bin/cpimport target_schema target_table -s '\t' –n1
```

#### Example 2 - SELECT involving a join between a fact table on the PM node and dimension table across all the nodes to import back on local PM:


With the infinidb_local_query variable set to 0 (default with local PM Query):


Create a script (i.e., extract_query_script.sql in our example) similar to the following:


```
set infinidb_local_query=0;
select fact.column1, dim.column2 
from fact join dim using (key) 
where idbPm(fact.key) = idbLocalPm();
```

The infinidb_local_query is set to 0 to allow query across all PMs.


The query is structured so that the UM process on the PM node gets the fact table data locally from the PM node (as indicated by the use of the [idbLocalPm()](columnstore-sql-structure-and-commands/columnstore-information-functions.md) function), while the dimension table data is extracted from all the PM nodes.


Then you can execute the script to pipe it directly into cpimport:


```
mcsmysql source_schema -N < extract_query_script.sql | /usr/local/mariadb/columnstore/bin/cpimport target_schema target_table -s '\t' –n1
```


## Operating mode


ColumnStore has the ability to support full MariaDB query syntax through an operating mode. This operating mode may be set as a default for the instance or set at the session level. To set the operating mode at the session level, the following command is used. Once the session has ended, any subsequent session will return to the default for the instance.


```
set infinidb_vtable_mode = n
```

where n is:


* 0) a generic, highly compatible row-by-row processing mode. Some WHERE clause components can be processed by ColumnStore, but joins are processed entirely by mysqld using a nested-loop join mechanism.
* 1) (the default) query syntax is evaluated by ColumnStore for compatibility with distributed execution and incompatible queries are rejected. Queries executed in this mode take advantage of distributed execution and typically result in higher performance.
* 2) auto-switch mode: ColumnStore will attempt to process the query internally, if it cannot, it will automatically switch the query to run in row-by-row mode.

