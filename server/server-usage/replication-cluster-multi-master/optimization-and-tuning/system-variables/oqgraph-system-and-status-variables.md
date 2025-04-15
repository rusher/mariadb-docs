
# OQGRAPH System and Status Variables


This page documents system and status variables related to the [OQGRAPH storage engine](../../../../reference/storage-engines/oqgraph-storage-engine/oqgraph-examples.md). See [Server Status Variables](server-status-variables.md) and [Server System Variables](server-system-variables.md) for complete list of all system and status variables.


## System Variables


#### `<code>oqgraph_allow_create_integer_latch</code>`


* Description: Created when the [OQGRAPH](../../../../reference/storage-engines/oqgraph-storage-engine/oqgraph-examples.md) storage engine is installed, if set to `<code>1</code>` (`<code>0</code>` is default), permits the `<code>latch</code>` field to be an integer (see [OQGRAPH Overview](../../../../reference/storage-engines/oqgraph-storage-engine/oqgraph-overview.md#creating-a-table)). This deprecated feature was removed in [MariaDB 11.5](../../../../../release-notes/mariadb-community-server/what-is-mariadb-115.md).
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>0</code>`
* Removed: [MariaDB 11.5](../../../../../release-notes/mariadb-community-server/what-is-mariadb-115.md).



## Status Variables


#### `<code>Oqgraph_boost_version</code>`


* Description: [OQGRAPH](../../../../reference/storage-engines/oqgraph-storage-engine/oqgraph-examples.md) boost version.
* Scope: Global, Session
* Data Type: `<code>string</code>`



#### `<code>Oqgraph_compat_mode</code>`


* Description: Whether or not legacy tables with integer latches are supported.
* Scope: Global, Session
* Data Type: `<code>string</code>`



#### `<code>Oqgraph_verbose_debug</code>`


* Description: Whether or not verbose debugging is enabled. If it is, performance may be adversely impacted
* Scope: Global, Session
* Data Type: `<code>string</code>`


