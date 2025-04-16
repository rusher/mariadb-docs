
# Relay Log

The relay log is a set of log files created by a replica during [replication](../../../server-usage/replication-cluster-multi-master/standard-replication/README.md).


It's the same format as the [binary log](../../../reference/storage-engines/innodb/binary-log-group-commit-and-innodb-flushing-performance.md), containing a record of events that affect the data or structure; thus, [mariadb-binlog](../../../../connectors/mariadb-connector-c/mariadb-binlogreplication-api-reference.md) can be used to display its contents. It consists of a set of relay log files and an index file containing a list of all relay log files.


Events are read from the primary's binary log and written to the replica's relay log. They are then performed on the replica. Old relay log files are automatically removed once they are no longer needed.


## Creating Relay Log Files


New relay log files are created by the replica at the following times:


* when the IO thread starts
* when the logs are flushed, with [FLUSH LOGS](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/flush-commands/flush-tables-for-export.md) or [mariadb-admin flush-logs](../../../clients-and-utilities/mariadb-admin.md).
* when the maximum size, determined by the [max_relay_log_size](../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md) system variable, has been reached


## Relay Log Names


By default, the relay log will be given a name `host_name-relay-bin.nnnnnn`, with `host_name` referring to the server's host name, and #nnnnnn` the sequence number.`


This will cause problems if the replica's host name changes, returning the error `Failed to open the relay log` and `Could not find target log during relay log initialization`. To prevent this, you can specify the relay log file name by setting the [relay_log](../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md) and [relay_log_index](../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md) system variables.


If you need to overcome this issue while replication is already underway,you can stop the replica, prepend the old relay log index file to the new relay log index file, and restart the replica.


For example:


```
shell> cat NEW_relay_log_name.index >> OLD_relay_log_name.index
shell> mv OLD_relay_log_name.index NEW_relay_log_name.index
```

## Viewing Relay Logs


The [SHOW RELAYLOG EVENTS](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-relaylog-events.md) shows events in the relay log, and, since relay log files are the same format as binary log files, they can be read with the [mariadb-binlog](../../../../connectors/mariadb-connector-c/mariadb-binlogreplication-api-reference.md) utility.


## Removing Old Relay Logs


Old relay logs are automatically removed once all events have been implemented on the replica, and the relay log file is no longer needed. This behavior can be changed by adjusting the [relay_log_purge](../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md) system variable from its default of `1` to `0`, in which case the relay logs will be left on the server.


Relay logs are also removed by the [CHANGE MASTER](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md) statement unless a [relay log option](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md#relay_log_options) is used.


One can also flush the logs with the [FLUSH RELAY LOGS](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/flush-commands/flush-tables-for-export.md) commands.


If the relay logs are taking up too much space on the replica, the [relay_log_space_limit](../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md) system variable can be set to limit the size. The IO thread will stop until the SQL thread has cleared the backlog. By default there is no limit.


## See also


* [FLUSH RELAY LOGS](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/flush-commands/flush-tables-for-export.md)

