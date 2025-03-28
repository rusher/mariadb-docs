# Selectively Skipping Replication of Binlog Events

The terms *master* and *slave* have historically been used in replication, and MariaDB has begun the process of adding *primary* and *replica* synonyms. The old terms will continue to be used to maintain backward compatibility - see [MDEV-18777](https://jira.mariadb.org/browse/MDEV-18777) to follow progress on this effort.

Normally, all changes that are logged as events in the [binary log](../../programming-customizing-mariadb/stored-routines/binary-logging-of-stored-routines.md) are also
replicated to all replicas (though still subject to filtering by
[replicate-do-db](replication-and-binary-log-system-variables.md#replicate_do_db), [replicate-ignore-db](replication-and-binary-log-system-variables.md#replicate_ignore_db),
and similar options). However, sometimes it may be desirable to have certain
events be logged into the binlog, but not be replicated to all or a subset of
replicas, where the distinction between events that should be replicated or not
is under the control of the application making the changes.

This could be useful if an application does some replication external to the
server outside of the built-in replication, or if it has some data that should
not be replicated for whatever reason.

This is possible with the following [system variables](../optimization-and-tuning/system-variables/server-system-variables.md).

#

# Primary Session Variable: skip_replication

When the [skip_replication](/en/replication-and-binary-log-server-system-variables/#skip_replication) variable is set to true, changes are logged into the [binary log](../../programming-customizing-mariadb/stored-routines/binary-logging-of-stored-routines.md) with the flag `@@skip_replication` set. Such events will not be replicated by replicas that run with
`--replicate-events-marked-for-skip` set different from its default of `REPLICATE`.

| Variable Name | Scope | Access Type | Data Type | Default Value |
| --- | --- | --- | --- | --- |
| Variable Name | skip_replication |
| Scope | Session only |
| Access Type | Dynamic |
| Data Type | bool |
| Default Value | OFF |

The `skip_replication` option only has effect if [binary logging](../../programming-customizing-mariadb/stored-routines/binary-logging-of-stored-routines.md) is enabled
and [sql_log_bin](/en/replication-and-binary-log-server-system-variables/#skip_replication) is true.

Attempting to change `@@skip_replication` in the middle of a transaction will
fail; this is to avoid getting half of a transaction replicated while the other
half is not replicated. Be sure to end any current transaction with
`COMMIT`/`ROLLBACK` before changing the variable.

#

# Replica Option: --replicate-events-marked-for-skip

The [replicate_events_marked_for_skip](/en/replication-and-binary-log-server-system-variables/#replicate_events_marked_for_skip) option tells the replica whether to replicate events that are marked with
the `@@skip_replication` flag. Default is `REPLICATE`, to ensure that all
changes are replicated to the replica. If set to `FILTER_ON_SLAVE`, events so
marked will be skipped on the replica and not replicated. If set to
`FILTER_ON_MASTER`, the filtering will be done on the primary, saving on
network bandwidth as the events will not be received by the replica at all.

| Variable Name | Scope | Access Type | Data Type | Default Value |
| --- | --- | --- | --- | --- |
| Variable Name | replicate_events_marked_for_skip |
| Scope | Global |
| Access Type | Dynamic |
| Data Type | enum: REPLICATE | FILTER_ON_SLAVE | FILTER_ON_MASTER |
| Default Value | REPLICATE |

**Note:** `replicate_events_marked_for_skip` is a dynamic variable (it can be
changed without restarting the server), however the replica threads must be
stopped when it is changed, otherwise an error will be thrown.

When events are filtered due to `@@skip_replication`, the filtering happens
on the primary side; in other words, the event is never sent to the replica. If
many events are filtered like this, a replica can sit a long time without
receiving any events from the primary. This is not a problem in itself, but must
be kept in mind when inquiring on the replica about events that are filtered. For
example `START SLAVE UNTIL <some position>` will stop when the first event
that is **not** filtered is encountered at the given position or beyond. If the
event at the given position is filtered, then the replica thread will only stop
when the next non-filtered event is encountered. In effect, if an event is
filtered, to the replica it appears that it was never written to the binlog on
the primary.

Note that when events are filtered for a replica, the data in the database will
be different on the replica and on the primary. It is the responsibility of the
application to replicate the data outside of the built-in replication or
otherwise ensure consistency of operation. If this is not done, it is possible
for replication to encounter, for example,
`[UNIQUE](/en/constraint_type-unique-constraint/)` contraint violations or
other problems which will cause replication to stop and require manual
intervention to fix.

The session variable `@@skip_replication` can be changed without requiring
special privileges. This makes it possible for normal applications to control
it without requiring `SUPER` privileges. But it must be kept in mind when using
replicas with `--replicate-events-marked-for-skip` set different
from `REPLICATE`, as it allows any connection to do changes that are not
replicated.

#

# skip_replication and sql_log_bin

`[@@sql_log_bin](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/set-commands/set-sql_log_bin.md)` and `@@skip_replication` are somewhat
related, as they can both be used to prevent a change on the primary from being
replicated to the replica. The difference is that with `@@skip_replication`,
changes are still written into the binlog, and replication of the events is
only skipped on replicas that explicitly are configured to do so, with
`--replicate-events-marked-for-skip` different from
`REPLICATE`. With `@@sql_log_bin`, events are not logged into the binlog,
and so are not replicated by any replica.

#

# skip_replication and the Binlog

When events in the binlog are marked with the `@@skip_replication` flag, the
flag will be preserved if the events are dumped by the [mariadb-binlog](../../../clients-and-utilities/mariadb-binlog/mariadb-binlog-options.md)
program and re-applied against a server with the
[mariadb client](../../../clients-and-utilities/mariadb-client/mariadb-command-line-client.md) program. Similarly, the
[BINLOG](../../../clients-and-utilities/server-client-software/client-libraries/clientserver-protocol/replication-protocol/binlog_checkpoint_event.md) statement will preserve the flag from the
event being replayed. And a replica which runs with
`--log-slave-updates` and does not filter events
(`--replicate-events-marked-for-skip=REPLICATE`) will also
preserve the flag in the events logged into the binlog on the replica.

#

# See Also

* [Using SQL_SLAVE_SKIP_COUNTER](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-commands/set-global-sql_slave_skip_counter.md) - How to skip a number of events on the replica