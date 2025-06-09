# Mroonga Status Variables

This page documents status variables related to the [Mroonga storage engine](./). See [Server Status Variables](../../../ha-and-performance/optimization-and-tuning/system-variables/server-status-variables.md) for a complete list of status variables that can be viewed with [SHOW STATUS](../../sql-statements/administrative-sql-statements/show/show-status.md).

#### `Mroonga_count_skip`

* Description: Incremented each time the 'fast line count feature' is used. Can be used to check if the feature is working after enabling it.
* Data Type: `numeric`

#### `Mroonga_fast_order_limit`

* Description: Incremented each time the 'fast ORDER BY LIMIT feature' is used. Can be used to check if the feature is working after enabling it.
* Data Type: `numeric`

CC BY-SA / Gnu FDL

{% @marketo/form formId="4316" %}
