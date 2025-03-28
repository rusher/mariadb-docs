# DATETIME

#

# Syntax

```
DATETIME [(microsecond precision)]
```

#

# Description

A date and time combination.

MariaDB displays `DATETIME` values in '`YYYY-MM-DD HH:MM:SS.ffffff`' format, but
allows assignment of values to `DATETIME` columns using either strings or
numbers. For details, see [date and time literals](../../sql-statements-and-structure/sql-language-structure/date-and-time-literals.md).

DATETIME columns also accept [CURRENT_TIMESTAMP](../../sql-statements-and-structure/sql-statements/built-in-functions/date-time-functions/now.md) as the default value.

[MariaDB 10.1.2](/kb/en/mariadb-1012-release-notes/) introduced the [--mysql56-temporal-format](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#mysql56_temporal_format) option, on by default, which allows MariaDB to store DATETMEs using the same low-level format MySQL 5.6 uses. For more information, see [Internal Format](#internal-format), below.

For storage requirements, see [Data Type Storage Requirements](../data-type-storage-requirements.md).

#

# Supported Values

MariaDB stores values that use the `DATETIME` data type in a format that supports values between `1000-01-01 00:00:00.000000` and `9999-12-31 23:59:59.999999`.

MariaDB can also store [microseconds](../../sql-statements-and-structure/sql-statements/built-in-functions/date-time-functions/microseconds-in-mariadb.md) with a precision between 0 and 6. If no microsecond precision is specified, then 0 is used by default.

MariaDB also supports '`0000-00-00`' as a special *zero-date* value, unless [NO_ZERO_DATE](../../../server-management/variables-and-modes/sql-mode.md#no_zero_date) is specified in the [SQL_MODE](../../../server-management/variables-and-modes/sql-mode.md). Similarly, individual components of a date can be set to `0` (for example: '`2015-00-12`'), unless [NO_ZERO_IN_DATE](../../../server-management/variables-and-modes/sql-mode.md#no_zero_in_date) is specified in the [SQL_MODE](../../../server-management/variables-and-modes/sql-mode.md). In many cases, the result of en expression involving a zero-date, or a date with zero-parts, is `NULL`. If the [ALLOW_INVALID_DATES](../../../server-management/variables-and-modes/sql-mode.md#allow_invalid_dates) SQL_MODE is enabled, if the day part is in the range between 1 and 31, the date does not produce any error, even for months that have less than 31 days.

#

# Oracle Mode

In [Oracle mode](/kb/en/sql_modeoracle-from-mariadb-103/#synonyms-for-basic-sql-types), `DATE` with a time portion is a synonym for `DATETIME`. See also [mariadb_schema](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/mariadb_schema.md).

#

# Internal Format

In [MariaDB 10.1.2](/kb/en/mariadb-1012-release-notes/) a new temporal format was introduced from MySQL 5.6 that alters how the `TIME`, `DATETIME` and `TIMESTAMP` columns operate at lower levels. These changes allow these temporal data types to have fractional parts and negative values. You can disable this feature using the [mysql56_temporal_format](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#mysql56_temporal_format) system variable.

Tables that include `TIMESTAMP` values that were created on an older version of MariaDB or that were created while the [mysql56_temporal_format](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#mysql56_temporal_format) system variable was disabled continue to store data using the older data type format.

In order to update table columns from the older format to the newer format, execute an [ALTER TABLE... MODIFY COLUMN](../../sql-statements-and-structure/sql-statements/data-definition/alter/alter-table.md#modify-column) statement that changes the column to the *same* data type. This change may be needed if you want to export the table's tablespace and import it onto a server that has `mysql56_temporal_format=ON` set (see [MDEV-15225](https://jira.mariadb.org/browse/MDEV-15225)).

For instance, if you have a `DATETIME` column in your table:

```
SHOW VARIABLES LIKE 'mysql56_temporal_format';

+-------------------------+-------+
| Variable_name | Value |
+-------------------------+-------+
| mysql56_temporal_format | ON |
+-------------------------+-------+

ALTER TABLE example_table MODIFY ts_col DATETIME;
```

When MariaDB executes the [ALTER TABLE](../../sql-statements-and-structure/sql-statements/data-definition/alter/alter-table.md) statement, it converts the data from the older temporal format to the newer one.

In the event that you have several tables and columns using temporal data types that you want to switch over to the new format, make sure the system variable is enabled, then perform a dump and restore using `mysqldump`. The columns using relevant temporal data types are restored using the new temporal format.

Starting from [MariaDB 10.5.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/release-notes-mariadb-105-series/mariadb-1051-release-notes) columns with old temporal formats are marked with a `/* mariadb-5.3 */` comment in the output of [SHOW CREATE TABLE](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-create-table.md), [SHOW COLUMNS](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-columns.md), [DESCRIBE](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/describe.md) statements, as well as in the `COLUMN_TYPE` column of the [INFORMATION_SCHEMA.COLUMNS Table](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-columns-table.md).

```
SHOW CREATE TABLE mariadb5312_datetime\G
*************************** 1. row ***************************
 Table: mariadb5312_datetime
Create Table: CREATE TABLE `mariadb5312_datetime` (
 `dt0` datetime /* mariadb-5.3 */ DEFAULT NULL,
 `dt6` datetime(6) /* mariadb-5.3 */ DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1
```

#

# Examples

```
CREATE TABLE t1 (d DATETIME);

INSERT INTO t1 VALUES ("2011-03-11"), ("2012-04-19 13:08:22"),
 ("2013-07-18 13:44:22.123456");

SELECT * FROM t1;
+---------------------+
| d |
+---------------------+
| 2011-03-11 00:00:00 |
| 2012-04-19 13:08:22 |
| 2013-07-18 13:44:22 |
+---------------------+
```

```
CREATE TABLE t2 (d DATETIME(6));

INSERT INTO t2 VALUES ("2011-03-11"), ("2012-04-19 13:08:22"),
 ("2013-07-18 13:44:22.123456");

SELECT * FROM t2;
+----------------------------+
| d |
+----------------------------+
| 2011-03-11 00:00:00.000000 |
| 2012-04-19 13:08:22.000000 |
| 2013-07-18 13:44:22.123456 |
+----------------------------++
```

Strings used in datetime context are automatically converted to datetime(6). If you want to have a datetime without seconds, you should use [CONVERT(..,datetime)](../../sql-statements-and-structure/sql-statements/built-in-functions/string-functions/convert.md).

```
SELECT CONVERT('2007-11-30 10:30:19',datetime);
+-----------------------------------------+
| CONVERT('2007-11-30 10:30:19',datetime) |
+-----------------------------------------+
| 2007-11-30 10:30:19 |
+-----------------------------------------+

SELECT CONVERT('2007-11-30 10:30:19',datetime(6));
+--------------------------------------------+
| CONVERT('2007-11-30 10:30:19',datetime(6)) |
+--------------------------------------------+
| 2007-11-30 10:30:19.000000 |
+--------------------------------------------+
```

#

# See Also

* [Data Type Storage Requirements](../data-type-storage-requirements.md)
* [CONVERT()](../../sql-statements-and-structure/sql-statements/built-in-functions/string-functions/convert.md)
* [Oracle mode from MariaDB 10.3](/kb/en/sql_modeoracle-from-mariadb-103/#synonyms-for-basic-sql-types)
* [mariadb_schema](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/mariadb_schema.md) data type qualifier