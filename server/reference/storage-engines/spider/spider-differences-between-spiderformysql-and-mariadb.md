
# Spider Differences Between SpiderForMySQL and MariaDB


### SQL Syntax


* With `<code>SpiderForMySQL</code>`, the [CREATE TABLE](../../sql-statements-and-structure/vectors/create-table-with-vectors.md) statement uses `<code>CONNECTION</code>` to define spider table variables whereas MariaDB uses `<code>COMMENT</code>`.


### Features


* `<code>[HANDLER](../../sql-statements-and-structure/nosql/handler/handler-commands.md)</code>` can not be translated to SQL in MariaDB
* Concurrent background search is not yet implemented in MariaDB
* Vertical partitioning storage engine VP is not implemented in MariaDB
* `<code>CREATE TABLE</code>` can use [table discovery](../storage-engines-storage-engine-development/table-discovery.md) in MariaDB
* `<code>[JOIN](../../sql-statements-and-structure/sql-statements/data-manipulation/selecting-data/joins-subqueries/joins/join-syntax.md)</code>` performance improvement using `<code>[join_cache_level](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#join_cache_level)>1</code>` and `<code>[join_buffer_size](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#join_buffer_size)</code>` in MariaDB

