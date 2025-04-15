
# Vector System Variables


##### MariaDB starting with [11.7.1](/kb/en/mariadb-1171-release-notes/)
Vectors were introduced in [MariaDB 11.7.1](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-7-rolling-releases/mariadb-11-7-1-release-notes.md)


This page documents system variables related to [Vectors](README.md).


See [Server System Variables](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md) for a complete list of system variables and instructions on setting them.


Also see the [Full list of MariaDB options, system and status variables](../../../server-management/variables-and-modes/full-list-of-mariadb-options-system-and-status-variables.md).


#### `<code>mhnsw_default_distance</code>`


* Description: Specifies the default distance metric for MHNSW vector indexing. This is used when the `<code>DISTANCE</code>` option is not explicitly defined during index creation.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--mhnsw-default-distance=val</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>enum</code>`
* Default Value: `<code>euclidean</code>`
* Valid Values:

  * `<code>euclidean</code>` Calculates straight-line distance between vectors. Best for spatial data, images, etc, when absolute magnitude matters.
  * `<code>cosine</code>` Measures directional similarity between vectors. Ideal for text embeddings, semantic search, and when vector magnitude is less important.
* Introduced: [MariaDB 11.7.1](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-7-rolling-releases/mariadb-11-7-1-release-notes.md)



#### `<code>mhnsw_default_m</code>`


* Description: Defines the default value for the M parameter in MHNSW vector indexing. The `<code>M</code>` parameter controls the number of connections per layer in the graph structure, influencing the balance between search performance and index size.

  * Larger `<code>M</code>` → Better search accuracy, but larger index size and slower updates and searches.
  * Smaller `<code>M</code>` → Faster updates and searches, smaller index, but potentially less accurate search.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--mhnsw-default-m=#</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>int unsigned</code>`
* Default Value: `<code>6</code>`
* Range: `<code>3</code>` to `<code>200</code>`
* Introduced: [MariaDB 11.7.1](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-7-rolling-releases/mariadb-11-7-1-release-notes.md)



#### `<code>mhnsw_ef_search</code>`


* Description: Defines the minimal number of result candidates to look for in the vector index for ORDER BY ... LIMIT N queries. The search will never search for less rows than that, even if LIMIT is smaller. This notably improves the search quality at low LIMIT values, at the expense of search time. Higher values may increase search quality but will also impact query performance.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--mhnsw-ef-search=#</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>int unsigned</code>`
* Default Value: `<code>20</code>`
* Range: `<code>1</code>` to `<code>10000</code>`
* Introduced: [MariaDB 11.7.1](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-7-rolling-releases/mariadb-11-7-1-release-notes.md)



#### `<code>mhnsw_max_cache_size</code>`


* Description: Upper limit for one MHNSW vector index cache. This limits the amount of memory that can be used for caching the index, ensuring efficient memory utilization.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--mhnsw-max-cache-size=#</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>bigint unsigned</code>`
* Default Value: `<code>16777216</code>` (16 MB)
* Range: `<code>1048576</code>` to `<code>18446744073709551615</code>`
* Introduced: [MariaDB 11.7.1](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-7-rolling-releases/mariadb-11-7-1-release-notes.md)


