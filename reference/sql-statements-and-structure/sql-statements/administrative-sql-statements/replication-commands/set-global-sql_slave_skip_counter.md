# SET GLOBAL SQL_SLAVE_SKIP_COUNTER

#

# Syntax

```
SET GLOBAL sql_slave_skip_counter = N
```

#

# Description

This statement skips the next `N` events from the primary. This is useful
for recovering from [replication](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/mariadb-releases/compatibility-differences/replication-compatibility-between-mariadb-and-mysql) stops caused by a statement.

If multi-source replication is used, this statement applies to the default connection. It could be necessary to change the value of the [default_master_connection](/en/replication-and-binary-log-server-system-variables/#default_master_connection) system variable.

Note that, if the event is a [transaction](../../transactions/transactions-unlock-tables.md), the whole transaction will be skipped. With non-transactional engines, an event is always a single statement.

This statement is valid only when the replica threads are not running.
Otherwise, it produces an error.

The statement does not automatically restart the replica threads.

#

# Example

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

#

# Multiple Replication Domains

`sql_slave_skip_counter` can't be used to skip transactions on a replica if [GTID replication](../../../../../clients-and-utilities/server-client-software/client-libraries/clientserver-protocol/replication-protocol/gtid_event.md) is in use and if [gtid_slave_pos](../../../../../clients-and-utilities/server-client-software/client-libraries/clientserver-protocol/replication-protocol/gtid_event.md#gtid_slave_pos) contains multiple [gtid_domain_id](../../../../../clients-and-utilities/server-client-software/client-libraries/clientserver-protocol/replication-protocol/gtid_event.md#gtid_domain_id) values. In that case, you'll get an error like the following:

```
ERROR 1966 (HY000): When using parallel replication and GTID with multiple 
 replication domains, @@sql_slave_skip_counter can not be used. Instead, 
 setting @@gtid_slave_pos explicitly can be used to skip to after a given GTID 
 position.
```

In order to skip transactions in cases like this, you will have to manually change [gtid_slave_pos](../../../../../clients-and-utilities/server-client-software/client-libraries/clientserver-protocol/replication-protocol/gtid_event.md#gtid_slave_pos).

#

# See Also

* [Selectively Skipping Replication of Binlog Events](../../../../../server-usage/replication-cluster-multi-master/standard-replication/selectively-skipping-replication-of-binlog-events.md)