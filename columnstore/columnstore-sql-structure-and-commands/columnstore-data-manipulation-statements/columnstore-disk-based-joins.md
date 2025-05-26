# ColumnStore Disk-Based Joins

1. [Introduction "Introduction"](columnstore-disk-based-joins.md#introduction)
2. [Per user join memory limit "Per user join memory limit"](columnstore-disk-based-joins.md#per-user-join-memory-limit)

### Introduction

Joins are performed in memory unless disk-based joins are enabled via AllowDiskBasedJoin in the columnstore.xml. When a join operation exceeds the memory allocated for query joins, the query is aborted with an error code IDB-2001.\
Disk-based joins enable such queries to use disk for intermediate join data in case when the memory needed for the join exceeds the memory limit. Although slower in performance as compared to a fully in-memory join and bound by the temporary space on disk, it does allow such queries to complete.

**Note: Disk-based joins do not include aggregation and DML joins.**

The following variables in the _HashJoin_ element in the Columnstore.xml configuration file relate the o disk-based joins. Columnstore.xml resides in the etc directory for your installation (/usr/local/mariadb/columnstore/etc).

* AllowDiskBasedJoin—Option to use disk-based joins. Valid values are Y (enabled) or N (disabled). The default is disabled.
* TempFileCompression—Option to use compression for disk join files. Valid values are Y (use compressed files) or N (use non-compressed files).
* TempFilePath—The directory path used for the disk joins. By default, this path is the tmp directory for your installation (i.e., /tmp/columnstore\_tmp\_files/joins/). Files in this directory will be created and cleaned on an as-needed basis. The entire directory is removed and recreated by ExeMgr at startup.)

**Note: When using disk-based joins, it is strongly recommended that the TempFilePath reside on its partition, as the partition may fill up as queries are executed.**

### Per user join memory limit

In addition to the system-wide flags at the SQL global and session levels, the following system variables exist for managing per-user memory limits for joins.

* columnstore\_um\_mem\_limit - A value for memory limit in MB per user. When this limit is exceeded by a join, it will switch to a disk-based join. By default, the limit is not set (value of 0).

For modification at the global level:\
In my.cnf file (example: /etc/my.cnf.d/server.cnf):

```
[mysqld]
...
columnstore_um_mem_limit = value
where value is the value in Mb for in memory limitation per user.
```

For modification at the session level, before issuing your join query from the SQL client, set the session variable as follows.

```
set columnstore_um_mem_limit = value
```

CC BY-SA / Gnu FDL
