
# TIME_MS column in INFORMATION_SCHEMA.PROCESSLIST

In MariaDB, an extra column `TIME_MS` has been added to the
[INFORMATION_SCHEMA.PROCESSLIST](information-schema-tables/information-schema-processlist-table.md) table. This column shows the same information as the column '`TIME`', but in units of
milliseconds with microsecond precision (the unit and precision of the
`TIME` column is one second).


For details about microseconds support in MariaDB, see [microseconds in MariaDB](../../../built-in-functions/date-time-functions/microseconds-in-mariadb.md).


The value displayed in the `TIME` and
`TIME_MS` columns is the period of time that the given
thread has been in its current state. Thus it can be used to check for example
how long a thread has been executing the current query, or for how long it has
been idle.


```
select id, time, time_ms, command, state from
   information_schema.processlist, (select sleep(2)) t;
+----+------+----------+---------+-----------+
| id | time | time_ms  | command | state     |
+----+------+----------+---------+-----------+
| 37 |    2 | 2000.493 | Query   | executing |
+----+------+----------+---------+-----------+
```

Note that as a difference to MySQL, in MariaDB the `TIME`
column (and also the `TIME_MS` column) are not affected by
any setting of [@TIMESTAMP](../../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#timestamp). This means that it can be
reliably used also for threads that change `@TIMESTAMP` (such
as the [replication](../../replication-statements/README.md) SQL thread). See also [MySQL Bug #22047](https://bugs.mysql.com/bug.php?id=22047).


As a consequence of this, the `TIME` column of 
`SHOW FULL PROCESSLIST` and
`INFORMATION_SCHEMA.PROCESSLIST` can not be used to determine
if a slave is lagging behind. For this, use instead the
`Seconds_Behind_Master` column in the output of 
[SHOW SLAVE STATUS](../../show/show-replica-status.md).


The addition of the TIME_MS column is based on the microsec_process patch,
developed by [Percona](https://www.percona.com/).

