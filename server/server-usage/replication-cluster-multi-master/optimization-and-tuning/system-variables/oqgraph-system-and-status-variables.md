
# OQGRAPH System and Status Variables


This page documents system and status variables related to the [OQGRAPH storage engine](../../../../reference/storage-engines/oqgraph-storage-engine/README.md). See [Server Status Variables](server-status-variables.md) and [Server System Variables](server-system-variables.md) for complete list of all system and status variables.


## System Variables


#### `oqgraph_allow_create_integer_latch`


* Description: Created when the [OQGRAPH](../../../../reference/storage-engines/oqgraph-storage-engine/README.md) storage engine is installed, if set to `1` (`0` is default), permits the `latch` field to be an integer (see [OQGRAPH Overview](../../../../reference/storage-engines/oqgraph-storage-engine/oqgraph-overview.md#creating-a-table)). This deprecated feature was removed in [MariaDB 11.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-5-rolling-releases/what-is-mariadb-115).
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `0`
* Removed: [MariaDB 11.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-5-rolling-releases/what-is-mariadb-115).



## Status Variables


#### `Oqgraph_boost_version`


* Description: [OQGRAPH](../../../../reference/storage-engines/oqgraph-storage-engine/README.md) boost version.
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


