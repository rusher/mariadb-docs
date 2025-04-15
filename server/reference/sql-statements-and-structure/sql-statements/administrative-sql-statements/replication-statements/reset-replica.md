
# RESET REPLICA

The terms *master* and *slave* have historically been used in replication, and MariaDB has begun the process of adding *primary* and *replica* synonyms. The old terms will continue to be used to maintain backward compatibility - see [MDEV-18777](https://jira.mariadb.org/browse/MDEV-18777) to follow progress on this effort.



## Syntax


```
RESET REPLICA ["connection_name"] [ALL]  [FOR CHANNEL "connection_name"].
```


## Description


RESET REPLICA makes the replica forget its [replication](README.md) position in the
master's [binary log](../../../../storage-engines/innodb/binary-log-group-commit-and-innodb-flushing-performance.md). This statement is meant to be used for a clean
start. It deletes the master.info and relay-log.info files, all the
[relay log](../../../../../server-management/server-monitoring-logs/binary-log/relay-log.md) files, and starts a new relay log file. To use RESET REPLICA,
the replica threads must be stopped (use [STOP REPLICA](stop-replica.md) if
necessary).


Note: All relay log files are deleted, even if they have not been
completely executed by the replica SQL thread. (This is a condition
likely to exist on a replication replica if you have issued a STOP REPLICA
statement or if the replica is highly loaded.)


Note: `<code class="highlight fixed" style="white-space:pre-wrap">RESET REPLICA</code>` does not reset the global
`<code class="highlight fixed" style="white-space:pre-wrap">gtid_slave_pos</code>` variable. This means that a replica
server configured with `<code class="highlight fixed" style="white-space:pre-wrap">CHANGE MASTER TO MASTER_USE_GTID=slave_pos</code>`
will not receive events with GTIDs occurring before the state saved in
`<code class="highlight fixed" style="white-space:pre-wrap">gtid_slave_pos</code>`. If the intent is to reprocess these events,
`<code class="highlight fixed" style="white-space:pre-wrap">gtid_slave_pos</code>` must be manually reset, e.g. by executing
`<code class="highlight fixed" style="white-space:pre-wrap">set global gtid_slave_pos=""</code>`.


Connection information stored in the master.info file is immediately
reset using any values specified in the corresponding startup options.
This information includes values such as master host, master port,
master user, and master password. If the replica SQL thread was in the
middle of replicating temporary tables when it was stopped, and RESET
REPLICA is issued, these replicated temporary tables are deleted on the
replica.


The `<code class="highlight fixed" style="white-space:pre-wrap">ALL</code>` also resets the `<code class="highlight fixed" style="white-space:pre-wrap">PORT</code>`, `<code class="highlight fixed" style="white-space:pre-wrap">HOST</code>`, `<code class="highlight fixed" style="white-space:pre-wrap">USER</code>` and `<code class="highlight fixed" style="white-space:pre-wrap">PASSWORD</code>` parameters for the replica. If you are using a connection name, it will permanently delete it and it will not show up anymore in [SHOW ALL REPLICAS STATUS](../show/show-replica-status.md).


#### connection_name


The `<code>connection_name</code>` option is used for [multi-source replication](../../../../../server-usage/replication-cluster-multi-master/standard-replication/multi-source-replication.md).


If there is only one nameless primary, or the default primary (as specified by the [default_master_connection](../../../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md) system variable) is intended, `<code>connection_name</code>` can be omitted. If provided, the `<code>RESET REPLICA</code>` statement will apply to the specified primary. `<code>connection_name</code>` is case-insensitive.



##### MariaDB starting with [10.7.0](../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-7-series/mariadb-1070-release-notes.md)
The `<code>FOR CHANNEL</code>` keyword was added for MySQL compatibility. This is identical as
using the channel_name directly after `<code>RESET REPLICA</code>`.



##### MariaDB starting with [11.6.0](https://mariadb.com/kb/en/mariadb-1160-release-notes/)
From [MariaDB 11.6](../../../../../../release-notes/mariadb-community-server/what-is-mariadb-116.md), RESET REPLICA resets the Master/Slave_last_event_time values (see [SHOW REPLICA STATUS](../show/show-replica-status.md)).


## See Also


* [STOP REPLICA](stop-replica.md) stops the replica, but it can be restarted with [START REPLICA](start-replica.md) or after next MariaDB server restart.

