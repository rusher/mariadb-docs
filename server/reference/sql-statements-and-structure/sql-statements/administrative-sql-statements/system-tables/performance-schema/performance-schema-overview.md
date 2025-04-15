
# Performance Schema Overview

The Performance Schema is a feature for monitoring server performance.


## Introduction


It is implemented as a storage engine, and so will appear in the list of storage engines available.


```
SHOW ENGINES;
+--------------------+---------+----------------------------------+--------------+------+------------+
| Engine             | Support | Comment                          | Transactions | XA   | Savepoints |
+--------------------+---------+----------------------------------+--------------+------+------------+
| ...                |         |                                  |              |      |            |
| PERFORMANCE_SCHEMA | YES     | Performance Schema               | NO           | NO   | NO         |
| ...                |         |                                  |              |      |            |
+--------------------+---------+----------------------------------+--------------+------+------------+
```

However, `<code>performance_schema</code>` is not a regular storage engine for storing data, it's a mechanism for implementing the Performance Schema feature.


The storage engine contains a database called `<code>performance_schema</code>`, which in turn consists of a number of tables that can be queried with regular SQL statements, returning specific performance information.


```
USE performance_schema
```

```
SHOW TABLES;
+----------------------------------------------------+
| Tables_in_performance_schema                       |
+----------------------------------------------------+
| accounts                                           |
...
| users                                              |
+----------------------------------------------------+
80 rows in set (0.00 sec)
```

See [List of Performance Schema Tables](performance-schema-tables/list-of-performance-schema-tables.md) for a full list and links to detailed descriptions of each table. From [MariaDB 10.5](../../../../../../../release-notes/mariadb-community-server/what-is-mariadb-105.md), there are 80 Performance Schema tables.


## Activating the Performance Schema


The performance schema is disabled by default for performance reasons. You can check its current status by looking at the value of the [performance_schema](performance-schema-system-variables.md#performance_schema) system variable.


```
SHOW VARIABLES LIKE 'performance_schema';
+--------------------+-------+
| Variable_name      | Value |
+--------------------+-------+
| performance_schema | ON    |
+--------------------+-------+
```

The performance schema cannot be activated at runtime - it must be set when the server starts by adding the following line in your `<code>my.cnf</code>` configuration file.


```
performance_schema=ON
```

From [MariaDB 10.5](../../../../../../../release-notes/mariadb-community-server/what-is-mariadb-105.md), some memory is allocated dynamically, depending on load, number of connections, number of tables open etc.


## Enabling the Performance Schema


You need to set up all consumers (starting collection of data) and instrumentations (what to collect):


```
UPDATE performance_schema.setup_consumers SET ENABLED = 'YES';
UPDATE performance_schema.setup_instruments SET ENABLED = 'YES', TIMED = 'YES';
```

You can decide what to enable/disable with `<code>WHERE NAME like "%what_to_enable"</code>`;
You can disable instrumentations by setting `<code>ENABLED</code>` to `<code>"NO"</code>`.


You can also do this in your my.cnf file.
The following enables all instrumentation of all stages (computation units) in MariaDB:


```
[mysqld]
performance_schema=ON
performance-schema-instrument='stage/%=ON'
performance-schema-consumer-events-stages-current=ON
performance-schema-consumer-events-stages-history=ON
performance-schema-consumer-events-stages-history-long=ON
```

## Listing Performance Schema Variables


```
SHOW VARIABLES LIKE "perf%";
+--------------------------------------------------------+-------+
| Variable_name                                          | Value |
+--------------------------------------------------------+-------+
| performance_schema                                     | ON    |
...
| performance_schema_users_size                          | 100   |
+--------------------------------------------------------+-------+
```

See [Performance Schema System Variables](performance-schema-system-variables.md) for a full list of available system variables.


Note that the "consumer" events are not shown on this list, as they are only available as options, not as system variables, and they can only be enabled at [startup](../../../../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md).


## Column Comments



##### MariaDB starting with [10.7.1](../../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-7-series/mariadb-1071-release-notes.md)
From [MariaDB 10.7.1](../../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-7-series/mariadb-1071-release-notes.md), comments have been added to table columns in the Performance Schema. These can be viewed with, for example:

```
SELECT column_name, column_comment FROM information_schema.columns 
  WHERE table_schema='performance_schema' AND table_name='file_instances';
...
*************************** 2. row ***************************
   column_name: EVENT_NAME
column_comment: Instrument name associated with the file.
*************************** 3. row ***************************
   column_name: OPEN_COUNT
column_comment: Open handles on the file. A value of greater than zero means 
                that the file is currently open.
...
```


## See Also


* [Performance schema options](../../../../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md)
* [SHOW ENGINE STATUS](../../show/show-engine-innodb-status.md)
* [SHOW PROFILE](../../show/show-profile.md)`<code>
</code>`
* [ANALYZE STATEMENT](../../analyze-and-explain-statements/analyze-statement.md)
* [Performance schema in MySQL 5.6](https://dev.mysql.com/doc/refman/5.6/en/performance-schema.html). All things here should also work for MariaDB.

