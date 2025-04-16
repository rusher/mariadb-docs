
# Information Schema INNODB_SYS_DATAFILES Table


##### MariaDB until [10.5](../../../../../../../../../release-notes/mariadb-community-server/what-is-mariadb-105.md)
The `INNODB_SYS_DATAFILES` table was removed in [MariaDB 10.6.0](../../../../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-1060-release-notes.md).


The [Information Schema](../../../../../../../mariadb-internals/information-schema-plugins-show-and-flush-statements.md) `INNODB_SYS_DATAFILES` table contains information about InnoDB datafile paths. It was intended to provide metadata for tablespaces inside InnoDB tables, which was never implemented in MariaDB and was removed in [MariaDB 10.6](../../../../../../../../../release-notes/mariadb-community-server/what-is-mariadb-106.md). The `PROCESS` [privilege](../../../../../account-management-sql-commands/grant.md) is required to view the table.


It contains the following columns:



| Column | Description |
| --- | --- |
| Column | Description |
| SPACE | Numeric tablespace. Matches the [INNODB_SYS_TABLES.SPACE](information-schema-innodb_sys_tables-table.md) value. |
| PATH | Tablespace datafile path. |



## Example


```
SELECT * FROM INNODB_SYS_DATAFILES;
+-------+--------------------------------+
| SPACE | PATH                           |
+-------+--------------------------------+
|    19 | ./test/t2.ibd                  |
|    20 | ./test/t3.ibd                  |
...
|    68 | ./test/animals.ibd             |
|    69 | ./test/animal_count.ibd        |
|    70 | ./test/t.ibd                   |
+-------+--------------------------------+
```
