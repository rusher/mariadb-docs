
# Writing Logs Into Tables

By default, all logs are disabled or written into files. The [general query log](general-query-log.md) and the [slow query log](slow-query-log/slow-query-log-overview.md) can also be written to special tables in the `mysql` database. During the startup, entries will always be written into files.


Note that [EXPLAIN output](slow-query-log/explain-in-the-slow-query-log.md) will only be recorded if the slow query log is written to a file and not to a table.


To write logs into tables, the [log_output](../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#log_output) server system variable is used. Allowed values are `FILE`, `TABLE` and `NONE`. It is possible to specify multiple values, separated with commas, to write the logs into both tables and files. `NONE` disables logging and has precedence over the other values.


So, to write logs into tables, one of the following settings can be used:


```
SET GLOBAL log_output = 'TABLE';
SET GLOBAL log_output = 'FILE,TABLE';
```

The general log will be written into the [general_log](../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/the-mysql-database-tables/mysqlgeneral_log-table.md) table, and the slow query log will be written into the [slow_log](../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/the-mysql-database-tables/mysql-slow_log-table.md) table. Only a limited set of operations are supported for those special tables. For example, direct DML statements (like `INSERT`) on those tables will fail with an error similar to the following:


```
ERROR 1556 (HY000): You can't use locks with log tables.
```

To flush data to the tables, use [FLUSH TABLES](../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/flush-commands/flush-tables-for-export.md) instead of [FLUSH LOGS](../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/flush-commands/flush-tables-for-export.md).


To empty the contents of the log tables, [TRUNCATE TABLE](../../reference/sql-statements-and-structure/sql-statements/table-statements/truncate-table.md) can be used.


The log tables use the [CSV](../../reference/storage-engines/csv/csv-overview.md) storage engine by default. This allows an external program to read the files if needed: normal CSV files are stored in the `mysql` subdirectory, in the data dir. However that engine is slow because it does not support indexes, so you can convert the tables to [MyISAM](../../reference/storage-engines/myisam-storage-engine/myisam-system-variables.md) (but not other storage engines). To do so, first temporarily disable logging:


```
SET GLOBAL general_log = 'OFF';
ALTER TABLE mysql.general_log ENGINE = MyISAM;
ALTER TABLE mysql.slow_log ENGINE = MyISAM;
SET GLOBAL general_log = @old_log_state;
```

[CHECK TABLE](../../reference/sql-statements-and-structure/sql-statements/table-statements/check-table.md) and [CHECKSUM TABLE](../../reference/sql-statements-and-structure/sql-statements/table-statements/checksum-table.md) are supported.


[CREATE TABLE](../../reference/sql-statements-and-structure/vectors/create-table-with-vectors.md) is supported. [ALTER TABLE](../../reference/sql-statements-and-structure/sql-statements/data-definition/alter/alter-tablespace.md), [RENAME TABLE](../../reference/sql-statements-and-structure/sql-statements/data-definition/rename-table.md) and [DROP TABLE](../../reference/sql-statements-and-structure/sql-statements/data-definition/drop/drop-tablespace.md) are supported when logging is disabled, but log tables cannot be partitioned.


Contents of log tables are not logged in the [binary log](../../reference/storage-engines/innodb/binary-log-group-commit-and-innodb-flushing-performance.md), thus cannot be replicated.

<span></span>
