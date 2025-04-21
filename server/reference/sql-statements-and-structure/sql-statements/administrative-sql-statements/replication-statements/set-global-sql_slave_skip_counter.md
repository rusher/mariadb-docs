
# SET GLOBAL SQL_SLAVE_SKIP_COUNTER

## Syntax


```
SET GLOBAL sql_slave_skip_counter = N
```


## Description


This statement skips the next `N` events from the primary. This is useful
for recovering from [replication](../../../../../server-usage/replication-cluster-multi-master/README.md) stops caused by a statement.


If multi-source replication is used, this statement applies to the default connection. It could be necessary to change the value of the [default_master_connection](../../../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md) system variable.


Note that, if the event is a [transaction](../../transactions/README.md), the whole transaction will be skipped. With non-transactional engines, an event is always a single statement.


This statement is valid only when the replica threads are not running.
Otherwise, it produces an error.


The statement does not automatically restart the replica threads.


## Example


```
SHOW SLAVE STATUS \G
...
SET GLOBAL sql_slave_skip_counter = 1;
START SLAVE;
```

Multi-source replication:


```
SET @@default_master_connection = 'master_01';
SET GLOBAL SQL_SLAVE_SKIP_COUNTER = 1;
START SLAVE;
```

## Multiple Replication Domains


`sql_slave_skip_counter` can't be used to skip transactions on a replica if [GTID replication](../../../../../server-usage/replication-cluster-multi-master/standard-replication/gtid.md) is in use and if [gtid_slave_pos](../../../../../server-usage/replication-cluster-multi-master/standard-replication/gtid.md#gtid_slave_pos) contains multiple [gtid_domain_id](../../../../../server-usage/replication-cluster-multi-master/standard-replication/gtid.md#gtid_domain_id) values. In that case, you'll get an error like the following:


```
ERROR 1966 (HY000): When using parallel replication and GTID with multiple 
 replication domains, @@sql_slave_skip_counter can not be used. Instead, 
 setting @@gtid_slave_pos explicitly can be  used to skip to after a given GTID 
 position.
```

In order to skip transactions in cases like this, you will have to manually change [gtid_slave_pos](../../../../../server-usage/replication-cluster-multi-master/standard-replication/gtid.md#gtid_slave_pos).


## See Also


* [Selectively Skipping Replication of Binlog Events](../../../../../server-usage/replication-cluster-multi-master/standard-replication/selectively-skipping-replication-of-binlog-events.md)

