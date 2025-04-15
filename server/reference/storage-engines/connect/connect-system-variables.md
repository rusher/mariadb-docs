
# CONNECT System Variables

This page documents system variables related to the [CONNECT storage engine](../../../../connectors/mariadb-connector-nodejs/connector-nodejs-pipelining.md). See [Server System Variables](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md) for a complete list of system variables and instructions on setting them.


See also the [Full list of MariaDB options, system and status variables](../../../server-management/variables-and-modes/full-list-of-mariadb-options-system-and-status-variables.md).


#### `<code>connect_class_path</code>`


* Description: Java class path
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--connect-class-path=value</code>`
* Scope: Global
* Dynamic:
* Data Type: `<code>string</code>`
* Default Value:



#### `<code>connect_cond_push</code>`


* Description: Enable condition pushdown
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--connect-cond-push={0|1}</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>ON</code>`



#### `<code>connect_conv_size</code>`


* Description: The size of the [VARCHAR](../../data-types/string-data-types/varchar.md) created when converting from a [TEXT](../../data-types/string-data-types/text.md) type. See [connect_type_conv](#connect_type_conv).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--connect-conv-size=#</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value:

  * >= [MariaDB 10.4.8](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-4-series/mariadb-1048-release-notes.md): `<code>1024</code>`
  * <= [MariaDB 10.4.7](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-4-series/mariadb-1047-release-notes.md): `<code>8192</code>`
* Range: `<code>0</code>` to `<code>65500</code>`



#### `<code>connect_default_depth</code>`


* Description: Default depth used by Json, XML and Mongo discovery.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--connect-default-depth=#</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value:`<code>5</code>`
* Range: `<code>-1</code>` to `<code>16</code>`
* Introduced: [MariaDB 10.5.7](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1057-release-notes.md), [MariaDB 10.4.16](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-4-series/mariadb-10416-release-notes.md)



#### `<code>connect_default_prec</code>`


* Description: Default precision used for doubles.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--connect-default-prec=#</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value:`<code>6</code>`
* Range: `<code>0</code>` to `<code>16</code>`
* Introduced: [MariaDB 10.5.9](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1059-release-notes.md), [MariaDB 10.4.18](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-4-series/mariadb-10418-release-notes.md)



#### `<code>connect_enable_mongo</code>`


* Description: Enable the [Mongo table type](connect-table-types/connect-mongo-table-type.md).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--connect-enable-mongo={0|1}</code>`
* Scope: Global, Session
* Dynamic:
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`
* Introduced: [MariaDB 10.3.2](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1032-release-notes.md), [MariaDB 10.2.9](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1029-release-notes.md)
* Removed: [MariaDB 10.3.3](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1033-release-notes.md)



#### `<code>connect_exact_info</code>`


* Description: Whether the CONNECT engine should return an exact record number value to information queries. It is OFF by default because this information can take a very long time for large variable record length tables or for remote tables, especially if the remote server is not available. It can be set to ON when exact values are desired, for instance when querying the repartition of rows in a partition table.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--connect-exact-info={0|1}</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`



#### `<code>connect_force_bson</code>`


* Description: Force using BSON for JSON tables. Starting with these releases, the internal way JSON was parsed and handled was changed. The main advantage of the new way is to reduce the memory required to parse JSON (from 6 to 10 times the size of the JSON source to now only 2 to 4 times). However, this is in Beta mode and JSON tables are still handled using the old mode. To use the new mode, tables should be created with TABLE_TYPE=BSON, or by setting this session variable to 1 or ON. Then, all JSON tables will be handled as BSON. This is temporary until the new way replaces the old way by default.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--connect-force-bson={0|1}</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`
* Introduced: [MariaDB 10.5.9](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1059-release-notes.md), [MariaDB 10.4.18](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-4-series/mariadb-10418-release-notes.md)



#### `<code>connect_indx_map</code>`


* Description: Enable file mapping for index files. To accelerate the indexing process, CONNECT makes an index structure in memory from the index file. This can be done by reading the index file or using it as if it was in memory by “file mapping”. Set to 0 (file read, the default) or 1 (file mapping).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--connect-indx-map=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`



#### `<code>connect_java_wrapper</code>`


* Description: Java wrapper.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--connect-java-wrapper=val</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>string</code>`
* Default Value: `<code>wrappers/JdbcInterface</code>`



#### `<code>connect_json_all_path</code>`


* Description: Discovery to generate json path for all columns if ON (the default) or do not when the path is the column name.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--connect-json-all-path={0|1}</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Data Type: `<code>boolean</code>`
* Default Value: `<code>ON</code>`
* Introduced: [MariaDB 10.5.7](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1057-release-notes.md), [MariaDB 10.4.16](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-4-series/mariadb-10416-release-notes.md)



#### `<code>connect_json_grp_size</code>`


* Description: Max number of rows for JSON aggregate functions.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--connect-json-grp-size=#</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>50</code>` (>= Connect 1.7.0003), `<code>10</code>` (<= Connect 1.7.0002)
* Range: `<code>1</code>` to `<code>2147483647</code>`



#### `<code>connect_json_null</code>`


* Description: Representation of JSON null values.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--connect-json-null=value</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>string</code>`
* Default Value: `<code><null></code>`



#### `<code>connect_jvm_path</code>`


* Description: Path to JVM library.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--connect-jvm_path=value</code>`
* Scope: Global
* Dynamic:
* Data Type: `<code>string</code>`
* Default Value:



#### `<code>connect_type_conv</code>`


* Description: Determines the handling of [TEXT](../../data-types/string-data-types/text.md) columns.

  * `<code>NO</code>`: The default until Connect 1.06.005, no conversion takes place, and a TYPE_ERROR is returned, resulting in a “not supported” message.
  * `<code>YES</code>`: The default from Connect 1.06.006. The column is internally converted to a column declared as VARCHAR(n), `<code>n</code>` being the value of [connect_conv_size](#connect_conv_size).
  * `<code>FORCE</code>` (>= Connect 1.06.006): Also convert ODBC blob columns to TYPE_STRING.
  * `<code>SKIP</code>`: No conversion. When the column declaration is provided via Discovery (meaning the CONNECT table is created without a column description), this column is not generated. Also applies to ODBC tables.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--connect-type-conv=#</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>enum</code>`
* Valid Values: `<code>NO</code>`, `<code>YES</code>`, `<code>FORCE</code>` or `<code>SKIP</code>`
* Default Value: `<code>YES</code>`



#### `<code>connect_use_tempfile</code>`


* Description:

  * `<code>NO</code>`: The first algorithm is always used. Because it can cause errors when updating variable record length tables, this value should be set only for testing.
  * `<code>AUTO</code>`: This is the default value. It leaves CONNECT to choose the algorithm to use. Currently it is equivalent to `<code>NO</code>`, except when updating variable record length tables ([DOS](connect-table-types/connect-table-types-data-files.md#dos-and-fix-table-types), [CSV](connect-table-types/connect-table-types-data-files.md#csv-and-fmt-table-types) or [FMT](connect-table-types/connect-table-types-data-files.md#fmt-type)) with file mapping forced to OFF.
  * `<code>YES</code>`: Using a temporary file is chosen with some exceptions. These are when file mapping is ON, for [VEC](connect-table-types/connect-table-types-data-files.md#vec-table-type-vector) tables and when deleting from [DBF](connect-table-types/connect-table-types-data-files.md#dbf-type) tables (soft delete). For variable record length tables, file mapping is forced to OFF.
  * `<code>FORCE</code>`: Like YES but forces file mapping to be OFF for all table types.
  * `<code>TEST</code>`: Reserved for CONNECT development.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--connect-use-tempfile=#</code>`
* Scope: Session
* Dynamic: Yes
* Data Type: `<code>enum</code>`
* Default Value: `<code>AUTO</code>`



#### `<code>connect_work_size</code>`


* Description: Size of the CONNECT work area used for memory allocation. Permits allocating a larger memory sub-allocation space when dealing with very large if sub-allocation fails. If the specified value is too big and memory allocation fails, the size of the work area remains but the variable value is not modified and should be reset.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--connect-work-size=#</code>`
* Scope: Global, Session (Session-only from CONNECT 1.03.005)
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>67108864</code>`
* Range: `<code>4194304</code>` upwards, depending on the physical memory size



#### `<code>connect_xtrace</code>`


* Description: Console trace value. Set to `<code>0</code>` (no trace), or to other values if a console tracing is desired. Note that to test this handler, MariaDB should be executed with the [--console](../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md) parameter because CONNECT prints some error and trace messages on the console. In some Linux versions, this is re-routed into the error log file. Console tracing can be set on the command line or later by names or values. Valid values (from Connect 1.06.006) include:

  * `<code>0</code>`: No trace
  * `<code>YES</code>` or `<code>1</code>`: Basic trace
  * `<code>MORE</code>` or `<code>2</code>`: More tracing
  * `<code>INDEX</code>` or `<code>4</code>`: Index construction
  * `<code>MEMORY</code>` or `<code>8</code>`: Allocating and freeing memory
  * `<code>SUBALLOC</code>` or `<code>16</code>`: Sub-allocating in work area
  * `<code>QUERY</code>` or `<code>32</code>`: Constructed query sent to external server
  * `<code>STMT</code>` or `<code>64</code>`: Currently executing statement
  * `<code>HANDLER</code>` or `<code>128</code>`: Creating and dropping CONNECT handlers
  * `<code>BLOCK</code>` or `<code>256</code>`: Creating and dropping CONNECT objects
  * `<code>MONGO</code>` or `<code>512</code>`: Mongo and REST (from [Connect 1.06.0010](../../../../connectors/mariadb-connector-nodejs/connector-nodejs-pipelining.md)) tracing
* For example: 

  * `<code>set global connect_xtrace=0; <em> No trace</em></code>`
  * `<code>set global connect_xtrace='YES'; <em> By name</em></code>`
  * `<code>set global connect_xtrace=1; <em> By value</em></code>`
  * `<code>set global connect_xtrace='QUERY,STMT'; <em> By name</em></code>`
  * `<code>set global connect_xtrace=96; <em> By value</em></code>`
  * `<code>set global connect_xtrace=1023; <em> Trace all</em></code>`
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--connect-xtrace=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>set</code>`
* Default Value: `<code>0</code>`
* Valid Values: See description


