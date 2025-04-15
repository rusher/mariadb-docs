
# ColumnStore Information Functions

 
1. [Functions "Functions"](#functions)
1. [Example "Example"](#example)





## Functions


MariaDB ColumnStore Information Functions are selectable pseudo functions that return MariaDB ColumnStore specific “meta” information to ensure queries can be locally directed to a specific node. These functions can be specified in the projection (SELECT), WHERE, GROUP BY, HAVING and ORDER BY portions of the SQL statement and will be processed in a distributed manner.


| Function | Description |
| --- | --- |
| Function | Description |
| idbBlockId(column) | The Logical Block Identifier (LBID) for the block containing the physical row |
| idbDBRoot(column) | The DBRoot where the physical row resides |
| idbExtentId(column) | The Logical Block Identifier (LBID) for the first block in the extent containing the physical row |
| idbExtentMax(column) | The max value from the extent map entry for the extent containing the physical row |
| idbExtentMin(column) | The min value from the extent map entry for the extent containing the physical row |
| idbExtentRelativeRid(column) | The row id (1 to 8,388,608) within the column's extent |
| idbLocalPm() | The PM from which the query was launched. This function will return NULL if the query is launched from a standalone UM |
| idbPartition(column) | The three part partition id (Directory.Segment.DBRoot) |
| idbPm(column) | The PM where the physical row resides |
| idbSegmentDir(column) | The lowest level directory id for the column file containing the physical row |
| idbSegment(column) | The number of the segment file containing the physical row |


## Example


SELECT involving a join between a fact table on the PM node and dimension table across all the nodes to import back on local PM:


With the [infinidb_local_query](../managing-columnstore/managing-columnstore-database-environment/configuring-columnstore-local-pm-query-mode.md) variable set to 0 (default with [local PM Query](../managing-columnstore/managing-columnstore-database-environment/configuring-columnstore-local-pm-query-mode.md) ):


Create a script (i.e., extract_query_script.sql in our example) similar to the following:


```
set infinidb_local_query=0;
select fact.column1, dim.column2 
from fact join dim using (key) 
where idbPm(fact.key) = idbLocalPm();
```

The [infinidb_local_query](../managing-columnstore/managing-columnstore-database-environment/configuring-columnstore-local-pm-query-mode.md) is set to 0 to allow query across all PMs.


The query is structured so that the UM process on the PM node gets the fact table data locally from the PM node (as indicated by the use of the idbLocalPm() function), while the dimension table data is extracted from all the PM nodes.


Then you can execute the script to pipe it directly into cpimport:


```
mcsmysql source_schema -N < extract_query_script.sql | /usr/local/mariadb/columnstore/bin/cpimport target_schema target_table -s '\t' –n1
```
