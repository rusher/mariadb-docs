
# ColumnStore Disk-Based Joins

 
1. [Introduction "Introduction"](#introduction)
1. [Per user join memory limit "Per user join memory limit"](#per-user-join-memory-limit)






### Introduction


Joins are performed in-memory on the [UM](../../columnstore-architecture/columnstore-user-module.md) node. When a join operation exceeds the memory allocated on the UM for query joins, the query is aborted with an error code IDB-2001.
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
