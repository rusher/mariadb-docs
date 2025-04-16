
# hash_join_cardinality optimizer_switch Flag


##### MariaDB starting with [10.6.13](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-10-6-13-release-notes.md)
The hash_join_cardinality optimizer_switch flag was added in  [MariaDB 11.0.2](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-0-series/mariadb-11-0-2-release-notes.md), [MariaDB 10.11.3](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-11-series/mariadb-10-11-3-release-notes.md),  [MariaDB 10.10.4](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-10-series/mariadb-10-10-4-release-notes.md), [MariaDB 10.9.6](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-9-series/mariadb-10-9-6-release-notes.md), [MariaDB 10.8.8](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-8-series/mariadb-10-8-8-release-notes.md) and [MariaDB 10.6.13](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-10-6-13-release-notes.md).


In MySQL and MariaDB, the output cardinality of a part of query has historically been tied to the used access method(s). This is different from the approach used in database textbooks. There, the cardinality "x JOIN y" is the same regardless of which access methods are used to compute it.


## Example


Consider a query joining customers with their orders:


```
select * 
from 
  customer, orders, ...
where 
  customer.id = orders.customer_id and ...
```

Suppose, table orders has an index `IDX` on `orders.customer_id`.


If the query plan is using this index to fetch orders for each customer, the optimizer will use index statistics from `IDX` to estimate the number of rows in the customer-joined-with-orders.


On the other hand, if the optimizer considers a query plan that joins customer with orders without use of indexes, it will ignore the `customer.id = orders.customer_id` equality completely and will compute the 
output cardinality as if customer was cross-joined with orders.


## Hash Join


MariaDB supports [Block Hash Join](../../../../reference/mariadb-internals/mariadb-internals-documentation-query-optimizer/block-based-join-algorithms.md#block-hash-join). It is not enabled by default, one needs to set it [join_cache_level](../system-variables/server-system-variables.md#join_cache_level) to 3 or a bigger value to enable it.


Before [MDEV-30812](https://jira.mariadb.org/browse/MDEV-30812), Query optimization for Block Hash Join would work as described in the above example: It would assume that the join operation is a cross join.


[MDEV-30812](https://jira.mariadb.org/browse/MDEV-30812) introduces a new [optimizer_switch](../system-variables/server-system-variables.md#optimizer_switch) flag, `hash_join_cardinality`. In MariaDB versions before 11.0, it is off by default.


If one sets it to ON, the optimizer will make use of column histograms when computing the cardinality of hash join operation output.


One can see the computation in the Optimizer Trace, search for `hash_join_cardinality`.

<span></span>
