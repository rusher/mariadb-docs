# Spider Differences Between SpiderForMySQL and MariaDB

### SQL Syntax

* With `SpiderForMySQL`, the [CREATE TABLE](../../../reference/sql-statements/data-definition/create/create-table.md) statement uses `CONNECTION` to define spider table variables whereas MariaDB uses `COMMENT`.

### Features

* `[HANDLER](../../sql-statements-and-structure/nosql/handler/README.md)` can not be translated to SQL in MariaDB
* Concurrent background search is not yet implemented in MariaDB
* Vertical partitioning storage engine VP is not implemented in MariaDB
* `CREATE TABLE` can use [table discovery](../storage-engines-storage-engine-development/table-discovery.md) in MariaDB
* `[JOIN](../../sql-statements-and-structure/sql-statements/data-manipulation/selecting-data/joins-subqueries/joins/join-syntax.md)` performance improvement using `[join_cache_level](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#join_cache_level)>1` and `[join_buffer_size](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#join_buffer_size)` in MariaDB

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
