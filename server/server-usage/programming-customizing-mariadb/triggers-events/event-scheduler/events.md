
# Events Overview

[Events](https://mariadb.com/kb/en/stored-programs-and-views-event) are named database objects containing SQL statements that are to be executed at a later stage, either once off, or at regular intervals.


They function very similarly to the Windows Task Scheduler or Unix cron jobs.


Creating, modifying or deleting events requires the [EVENT privilege](../../../../reference/sql-statements-and-structure/sql-statements/account-management-sql-commands/grant.md#database-privileges).


## Creating Events


Events are created with the [CREATE EVENT](../../../../reference/sql-statements-and-structure/sql-statements/data-definition/create/create-event.md) statement.


### Example


```
CREATE EVENT test_event 
  ON SCHEDULE EVERY 1 MINUTE DO 
   UPDATE test.t1 SET a = a + 1;
```

## Executing Events


Events are only executed if the event scheduler is running. This is determined by the value of the [event_scheduler](../../../replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#event_scheduler) system variable, which needs to be set to `On` for the event scheduler to be running.


You can check if the Event scheduler is running with:


```
SHOW PROCESSLIST;
+----+-----------------+-----------+------+---------+------+-----------------------------+------------------+----------+
| Id | User            | Host      | db   | Command | Time | State                       | Info             | Progress |
+----+-----------------+-----------+------+---------+------+-----------------------------+------------------+----------+
| 40 | root            | localhost | test | Sleep   | 4687 |                             | NULL             |    0.000 |
| 41 | root            | localhost | test | Query   |    0 | init                        | SHOW PROCESSLIST |    0.000 |
| 42 | event_scheduler | localhost | NULL | Daemon  |   30 | Waiting for next activation | NULL             |    0.000 |
+----+-----------------+-----------+------+---------+------+-----------------------------+------------------+----------+
```

If the event scheduler is not running and `event_scheduler` has been set to `OFF`, use:


```
SET GLOBAL event_scheduler = ON;
```

to activate it. If `event_scheduler` has been set to `Disabled`, you cannot change the value at runtime. Changing the value of the `event_scheduler` variable requires the SUPER privilege.


Since [MariaDB 10.0.22](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/mariadb-10022-release-notes), setting the [event_scheduler](../../../replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#event_scheduler) system variable will also try to reload the [mysql.event table](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/the-mysql-database-tables/mysql-event-table.md) if it was not properly loaded at startup.


## Viewing Current Events


A list of current events can be obtained with the [SHOW EVENTS](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-events.md) statement. This only shows the event name and interval - the full event details, including the SQL, can be seen by querying the [Information Schema EVENTS table](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-events-table.md), or with [SHOW CREATE EVENT](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-create-event.md).


If an event is currently being executed, it can be seen by querying the [Information Schema PROCESSLIST table](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-processlist-table.md), or with the [SHOW PROCESSLIST](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-processlist.md) statement.


### Example


```
SHOW EVENTS\G;
*************************** 1. row ***************************
                  Db: test
                Name: test_event
             Definer: root@localhost
           Time zone: SYSTEM
                Type: RECURRING
          Execute at: NULL
      Interval value: 1
      Interval field: MINUTE
              Starts: 2013-05-20 13:46:56
                Ends: NULL
              Status: ENABLED
          Originator: 1
character_set_client: utf8
collation_connection: utf8_general_ci
  Database Collation: latin1_swedish_ci
```

```
SHOW CREATE EVENT test_event\G
*************************** 1. row ***************************
               Event: test_event
            sql_mode: 
           time_zone: SYSTEM
        Create Event: CREATE DEFINER=`root`@`localhost` EVENT `test_event` ON SCHEDULE EVERY 1 MINUTE STARTS '2013-05-20 13:46:56' ON COMPLETION NOT PRESERVE ENABLE DO UPDATE test.t1 SET a = a + 1
character_set_client: utf8
collation_connection: utf8_general_ci
  Database Collation: latin1_swedish_ci
```

## Altering Events


An event can be changed with the [ALTER EVENT](alter-event.md) statement.


### Example


```
ALTER EVENT test_event ON SCHEDULE EVERY '2:3' DAY_HOUR;
```

## Dropping Events


Events are dropped with the [DROP EVENT](../../../../reference/sql-statements-and-structure/sql-statements/data-definition/drop/drop-event.md) statement. Events are also also automatically dropped once they have run for the final time according to their schedule, unless the ON COMPLETION PRESERVE clause has been specified.


### Example


```
DROP EVENT test_event;
Query OK, 0 rows affected (0.00 sec)
```

## See Also


* [CREATE EVENT](../../../../reference/sql-statements-and-structure/sql-statements/data-definition/create/create-event.md)
* [SHOW CREATE EVENT](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-create-event.md)
* [ALTER EVENT](alter-event.md)
* [DROP EVENT](../../../../reference/sql-statements-and-structure/sql-statements/data-definition/drop/drop-event.md)
* [Event Limitations](event-limitations.md)
* [Automating MariaDB Tasks with Events](../../../../server-management/getting-installing-and-upgrading-mariadb/binary-packages/automated-mariadb-deployment-and-administration/automating-mariadb-tasks-with-events.md)


CC BY-SA / Gnu FDL

