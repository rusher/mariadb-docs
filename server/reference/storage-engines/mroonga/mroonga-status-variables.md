
# Mroonga Status Variables


This page documents status variables related to the [Mroonga storage engine](mroonga-user-defined-functions/mroonga_snippet_html.md). See [Server Status Variables](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-status-variables.md) for a complete list of status variables that can be viewed with [SHOW STATUS](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-status.md).


#### `Mroonga_count_skip`


* Description: Incremented each time the 'fast line count feature' is used. Can be used to check if the feature is working after enabling it.
* Data Type: `numeric`



#### `Mroonga_fast_order_limit`


* Description: Incremented each time the 'fast ORDER BY LIMIT feature' is used. Can be used to check if the feature is working after enabling it.
* Data Type: `numeric`


