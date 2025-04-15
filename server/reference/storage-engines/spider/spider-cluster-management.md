# Spider Cluster Management

#

# Direct SQL

Direct SQL is a way to map reduced execution on remote backends and store the results in a local table. This can either be sequential, using the UDF function [spider_direct_sql](spider-functions/spider_direct_sql.md), or concurrently, using [spider_bg_direct_sql](spider-functions/spider_bg_direct_sql.md).

```
spider1 backend << EOF 
CREATE TEMPORARY TABLE res
(
 id int(10) unsigned NOT NULL,
 k int(10) unsigned NOT NULL DEFAULT '0',
 c char(120) NOT NULL DEFAULT '',
 pad char(60) NOT NULL DEFAULT ''
) ENGINE=MEMORY;

SELECT spider_direct_sql(
'SELECT * FROM sbtest s WHERE s.id IN(10,12,13)',
 'res', 
 concat('host "', host, '", port "', port, '", user "', username, '", password "', password, '", database "', tgt_db_name, '"')
) a 
FROM 
 mysql.spider_tables 
WHERE 
 db_name = 'backend' and table_name like 'sbtest#P#pt%';

SELECT * FROM res; 
EOF
```

Or if you are using a [SERVER](../../sql-statements-and-structure/sql-statements/data-definition/create/create-server.md):

```
SELECT spider_direct_sql( 
 'SELECT * FROM sbtest s WHERE s.id IN(10,12,13)',
 'res',
 concat('server "', server, '"')
) a
 FROM mysql.spider_tables
 WHERE db_name = 'backend' and table_name like 'sbtest#P#pt%' ;
```

The default for [spider_bg_direct_sql](spider-functions/spider_bg_direct_sql.md) is to access concurrently all backends. If you have multiple partitions store inside a single backend, you still can increase parallelism affecting different channels to each partitions.

```
CREATE TEMPORARY TABLE res
(
 id int(10) unsigned NOT NULL , 
 col_microsec DATETIME(6) default NOW(8),
 db varchar(20)
) ENGINE=MEMORY;

SELECT spider_bg_direct_sql( 'SELECT count(*) ,min(NOW(6)),min(DATABASE())) FROM sbtest', 'res', concat('srv "', server,'" cch ',@rn:=@rn+1 ) ) a FROM mysql.spider_tables,(SELECT @rn:=1) t2 WHERE db_name = 'bsbackend' and table_name like 'sbtest#P#pt%';
```

#

# Direct Handler Socket

#

#### MariaDB starting with [10.8.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/release-notes-mariadb-10-8-series/mariadb-1081-release-notes)

The Spider Handler Socket support has been removed, see [MDEV-26858](https://jira.mariadb.org/browse/MDEV-26858).

Check that [Handler Socket](../../sql-statements-and-structure/nosql/handlersocket/handlersocket-external-resources.md) is running on the backend nodes

```
:~

# backend2 -e "show variables like 'handler%'"

+-------------------------------+---------------+
| Variable_name | Value |
+-------------------------------+---------------+
| handlersocket_accept_balance | 0 |
| handlersocket_address | 192.168.0.201 |
| handlersocket_backlog | 32768 |
| handlersocket_epoll | 1 |
| handlersocket_plain_secret | |
| handlersocket_plain_secret_wr | |
| handlersocket_port | 20500 |
| handlersocket_port_wr | 20501 |
| handlersocket_rcvbuf | 0 |
| handlersocket_readsize | 0 |
| handlersocket_sndbuf | 0 |
| handlersocket_threads | 4 |
| handlersocket_threads_wr | 1 |
| handlersocket_timeout | 300 |
| handlersocket_verbose | 10 |
| handlersocket_wrlock_timeout | 12 |
+-------------------------------+---------------+
```

```
spider1 backend << EOF 
CREATE TEMPORARY TABLE res
(
 id int(10) unsigned NOT NULL,
 k int(10) unsigned NOT NULL DEFAULT '0',
 c char(120) NOT NULL DEFAULT '',
 pad char(60) NOT NULL DEFAULT ''
) ENGINE=MEMORY;

SELECT spider_direct_sql('1\t=\t1\t2\t100000\t0','res', 'host "192.168.0.202", table "sbtest", database "test", port "20500", access_mode "1"');
```

#

# Inter Nodes Copy Table

#

#### MariaDB starting with [10.8.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/release-notes-mariadb-10-8-series/mariadb-1081-release-notes)

The UDF spider_copy_tables relies on Spider's high availability feature, which has been deprecated ([MDEV-28479](https://jira.mariadb.org/browse/MDEV-28479)), and will be deleted. Please use other high availability solutions like [replication](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/mariadb-releases/compatibility-differences/replication-compatibility-between-mariadb-and-mysql) or [galera-cluster](../../../server-usage/replication-cluster-multi-master/galera-cluster/galera-cluster-status-variables.md).

The UDF function [spider_copy_tables](spider-functions/spider_copy_tables.md) is available for copying table data from the source link ID to the destination link ID list without stopping your service for copying

`spider_copy_tables(Spider table name, source link ID, destination link ID list[, parameters])`

* `Returns 1` if copying data succeeded.
* `Returns 0` if copying data failed.

If the Spider table is partitioned, you must set "Spider table name" with a part name such as "table_name#P#part_name".

You can check the table name and the link ID with the part name using the following SQL:

```
SELECT table_name FROM mysql.spider_tables;
```

#

# General Log

To capture all queries sent to remote backends on a `Spider Node` :

```
SET GLOBAL general_log=ON; 
SET GLOBAL spider_general_log=ON;
SET GLOBAL spider_log_result_errors=1;
SET GLOBAL spider_log_result_error_with_sql=3;
```

#

# Compiling in Debug Mode

See [Compiling MariaDB for Debugging](https://app.gitbook.com/s/iJPrPCGi329TSR8WIXJW/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/debugging-mariadb/compiling-mariadb-for-debugging) and [Creating a Trace File](https://app.gitbook.com/s/iJPrPCGi329TSR8WIXJW/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/debugging-mariadb/creating-a-trace-file).

Report the issue in [MariaDB JIRA](https://jira.mariadb.org) (see [Reporting Bugs](../../bug-tracking/reporting-bugs.md)) or to the MariaDB Corporation support center.

#

# Compiling in Static

Available since version 3.1.14

To activate spider as a static plugin change "MODULE_ONLY" to "MANDATORY" in storage/spider/CMakeList.txt before compiling

Note that Spider UDF functions will not work with such settings.

#

# Status Variables

A number of new [status variables](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-status-variables.md) have been introduced, see [Spider Status Variables](/en/spider-server-status-variables/) for a complete list.

#

# Information Schema Tables

* A new [Information Schema](../../../server-usage/programming-customizing-mariadb/views/information-schema-views-table.md) table is installed - [SPIDER_ALLOC_MEM](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-spider_alloc_mem-table.md).

```
+-------------------+---------------------+------+-----+---------+-------+
| Field | Type | Null | Key | Default | Extra |
+-------------------+---------------------+------+-----+---------+-------+
| ID | int(10) unsigned | NO | | 0 | |
| FUNC_NAME | varchar(64) | YES | | NULL | |
| FILE_NAME | varchar(64) | YES | | NULL | |
| LINE_NO | int(10) unsigned | YES | | NULL | |
| TOTAL_ALLOC_MEM | bigint(20) unsigned | YES | | NULL | |
| CURRENT_ALLOC_MEM | bigint(20) | YES | | NULL | |
| ALLOC_MEM_COUNT | bigint(20) unsigned | YES | | NULL | |
| FREE_MEM_COUNT | bigint(20) unsigned | YES | | NULL | |
+-------------------+---------------------+------+-----+---------+-------+
```

From [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/what-is-mariadb-105), Spider installs another Information Schema table, [SPIDER_WRAPPER_PROTOCOLS](information-schema-spider_wrapper_protocols-table.md).

#

# Performance Schema

The [Performance schema](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/performance-schema/performance-schema-status-variables.md) is commonly used to troubleshoot issues that consume time inside your workload. The Performance schema should not be activated for servers that are experimenting constant heavy load, but most of time it is acceptable to lose 5% to 20% additional CPU to keep track of server internals execution.

To activate the performance schema, use the [performance_schema](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/performance-schema/performance-schema-system-variables.md#performance_schema) system variable and add the following to the server section of the [MariaDB configuration file](/en/configuring-mariadb-with-mycnf/).

```
performance_schema=on
```

Activate the Spider probes to be monitored.

```
UPDATE performance_schema.setup_instruments SET 
 ENABLED='YES', TIMED='yes' WHERE NAME LIKE '%spider%';
```

Run your queries ...

And check the performance metrics. Remove specific Spider metrics to have a more global view.

```
SELECT * FROM performance_schema.events_waits_summary_global_by_event_name 
 WHERE COUNT_STAR<>0 AND EVENT_NAME LIKE '%spider%' 
 ORDER BY SUM_TIMER_WAIT DESC LIMIT 10;
```