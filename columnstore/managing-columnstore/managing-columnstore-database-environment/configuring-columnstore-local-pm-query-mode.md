
# Configuring ColumnStore Local PM Query Mode

MariaDB ColumnStore has the ability to query data from just a single [PM](../../columnstore-architecture/columnstore-performance-module.md) instead of the whole database through the [UM](../../columnstore-architecture/columnstore-user-module.md). In order to accomplish this, the infinidb_local_query variable in the my.cnf configuration file is used and maybe set as a default at system wide or set at the session level.


 
1. [Enable local PM query during installation "Enable local PM query during installation"](#enable-local-pm-query-during-installation)
1. [Enable local PM query systemwide "Enable local PM query systemwide"](#enable-local-pm-query-systemwide)
1. [Enable/disable local PM query at the session level "Enable/disable local PM query at the session level"](#enabledisable-local-pm-query-at-the-session-level)
1. [Local PM Query Examples "Local PM Query Examples"](#local-pm-query-examples) 

  1. [Example 1 - SELECT from a single table on local PM to import back on local PM: "Example 1 - SELECT from a single table on local PM to import back on local PM:"](#example-1-select-from-a-single-table-on-local-pm-to-import-back-on-local-pm)
  1. [Example 2 - SELECT involving a join between a fact table on the PM node and dimension table across all the nodes to import back on local PM: "Example 2 - SELECT involving a join between a fact table on the PM node and dimension table across all the nodes to import back on local PM:"](#example-2-select-involving-a-join-between-a-fact-table-on-the-pm-node-and-dimension-table-across-all-the-nodes-to-import-back-on-local-pm)






### Enable local PM query during installation


Local PM query can be enabled system wide during the install process when running the install script postConfigure. Answer 'y' to this prompt during the install process.


```
NOTE: Local Query Feature allows the ability to query data from a single Performance
      Module. Check MariaDB ColumnStore Admin Guide for additional information.

Enable Local Query feature? [y,n] (n) >
```

[installing-and-configuring-a-multi-server-columnstore-system-11x.md](../../columnstore-getting-started/preparing-and-installing-mariadb-columnstore-11x/installing-and-configuring-a-multi-server-columnstore-system-11x.md)


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

At the session level, this variable applies only to executing a query on an individual [PM](../../columnstore-architecture/columnstore-performance-module.md) and will error if executed on the [UM](../../columnstore-architecture/columnstore-user-module.md). The PM must be set up with the local query option during installation.


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


The query is structured so that the UM process on the PM node gets the fact table data locally from the PM node (as indicated by the use of the [idbLocalPm()](../../columnstore-sql-structure-and-commands/columnstore-information-functions.md) function), while the dimension table data is extracted from all the PM nodes.


Then you can execute the script to pipe it directly into cpimport:


```
mcsmysql source_schema -N < extract_query_script.sql | /usr/local/mariadb/columnstore/bin/cpimport target_schema target_table -s '\t' –n1
```
