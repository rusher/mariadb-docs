
# OQGRAPH System and Status Variables


This page documents system and status variables related to the [OQGRAPH storage engine](../../../../ref/storage-engines/oqgraph-storage-engine/oqgraph-examples.md). See [Server Status Variables](server-status-variables.md) and [Server System Variables](server-system-variables.md) for complete list of all system and status variables.


## System Variables


#### `oqgraph_allow_create_integer_latch`


* Description: Created when the [OQGRAPH](../../../../ref/storage-engines/oqgraph-storage-engine/oqgraph-examples.md) storage engine is installed, if set to `1` (`0` is default), permits the `latch` field to be an integer (see [OQGRAPH Overview](../../../../ref/storage-engines/oqgraph-storage-engine/oqgraph-overview.md#creating-a-table)). This deprecated feature was removed in [MariaDB 11.5](../../../../../release-notes/mariadb-community-server/what-is-mariadb-115.md).
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `0`
* Removed: [MariaDB 11.5](../../../../../release-notes/mariadb-community-server/what-is-mariadb-115.md).



## Status Variables


#### `Oqgraph_boost_version`


* Description: [OQGRAPH](../../../../ref/storage-engines/oqgraph-storage-engine/oqgraph-examples.md) boost version.
* Scope: Global, Session
* Data Type: `string`



#### `Oqgraph_compat_mode`


* Description: Whether or not legacy tables with integer latches are supported.
* Scope: Global, Session
* Data Type: `string`



#### `Oqgraph_verbose_debug`


* Description: Whether or not verbose debugging is enabled. If it is, performance may be adversely impacted
* Scope: Global, Session
* Data Type: `string`


