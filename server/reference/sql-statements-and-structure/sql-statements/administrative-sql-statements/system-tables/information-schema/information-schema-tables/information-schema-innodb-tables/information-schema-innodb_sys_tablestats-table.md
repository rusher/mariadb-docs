
# Information Schema INNODB_SYS_TABLESTATS Table

The [Information Schema](../../../../../../../mariadb-internals/information-schema-plugins-show-and-flush-statements.md) `<code>INNODB_SYS_TABLESTATS</code>` table contains InnoDB status information. It can be used for developing new performance-related extensions, or high-level performance monitoring.


The `<code>PROCESS</code>` [privilege](../../../../../account-management-sql-commands/grant.md) is required to view the table.


Note that the MySQL InnoDB and Percona XtraDB versions of the tables differ (see [XtraDB and InnoDB](../../../../../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/innodb-upgrade-tests/README.md)).


It contains the following columns:



| Column | Description |
| --- | --- |
| Column | Description |
| TABLE_ID | Table ID, matching the [INNODB_SYS_TABLES.TABLE_ID](information-schema-innodb_sys_tables-table.md) value. |
| SCHEMA | Database name (XtraDB only). |
| NAME | Table name, matching the [INNODB_SYS_TABLES.NAME](information-schema-innodb_sys_tables-table.md) value. |
| STATS_INITIALIZED | Initialized if statistics have already been collected, otherwise Uninitialized. |
| NUM_ROWS | Estimated number of rows currently in the table. Updated after each statement modifying the data, but uncommited transactions mean it may not be accurate. |
| CLUST_INDEX_SIZE | Number of pages on disk storing the clustered index, holding InnoDB table data in primary key order, or NULL if not statistics yet collected. |
| OTHER_INDEX_SIZE | Number of pages on disk storing secondary indexes for the table, or NULL if not statistics yet collected. |
| MODIFIED_COUNTER | Number of rows modified by statements modifying data. |
| AUTOINC | [Auto_increment](../../../../../../../storage-engines/innodb/auto_increment-handling-in-innodb.md) value. |
| REF_COUNT | Countdown to zero, when table metadata can be removed from the table cache. (InnoDB only) |
| MYSQL_HANDLES_OPENED | (XtraDB only). |


