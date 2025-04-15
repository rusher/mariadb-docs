
# mariadb_schema

`<code>mariadb_schema</code>` is a data type qualifier that allows one to create MariaDB native date types in an [SQL_MODE](../../../../../server-management/variables-and-modes/sql-mode.md) that has conflicting data type translations.


`<code>mariadb_schema</code>` was introduced in [MariaDB 10.3.24](../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-10324-release-notes.md), [MariaDB 10.4.14](../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-4-series/mariadb-10414-release-notes.md) and [MariaDB 10.5.5](../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1055-release-notes.md).


For example, in [SQL_MODE=ORACLE](../../../../../../release-notes/mariadb-community-server/compatibility-and-differences/sql_modeoracle.md), if one creates a table with the [DATE](../../../sql-language-structure/date-and-time-literals.md) type, it will actually create a [DATETIME](../../../../data-types/date-and-time-data-types/datetime.md#oracle-mode) column to match what an Oracle user is expecting. To be able to create a MariaDB DATE in Oracle mode one would have to use `<code>mariadb_schema</code>`:


```
CREATE TABLE t1 (d mariadb_schema.DATE);
```

`<code>mariadb_schema</code>` is also shown if one creates a table with `<code>DATE</code>` in MariaDB native mode and then does a [SHOW CREATE TABLE](../show/show-create-table.md) in `<code>ORACLE</code>` mode:


```
SET sql_mode=DEFAULT;
CREATE OR REPLACE TABLE t1 (
  d DATE
);
SET SQL_mode=ORACLE;
SHOW CREATE TABLE t1;
+-------+--------------------------------------------------------------+
| Table | Create Table                                                 |
+-------+--------------------------------------------------------------+
| t1    | CREATE TABLE "t1" (
  "d" mariadb_schema.date DEFAULT NULL
) |
+-------+--------------------------------------------------------------+
```

When the server sees the `<code>mariadb_schema</code>` qualifier, it disables sql_mode-specific data type translation and interprets the data type literally, so for example `<code>mariadb_schema.DATE</code>` is interpreted as the traditional MariaDB `<code>DATE</code>` data type, no matter what the current sql_mode is.


The `<code>mariadb_schema</code>` prefix is displayed only when the data type name would be ambiguous otherwise. The prefix is displayed together with MariaDB `<code>DATE</code>` when [SHOW CREATE TABLE](../show/show-create-table.md) is executed in [SQL_MODE=ORACLE](../../../../../../release-notes/mariadb-community-server/compatibility-and-differences/sql_modeoracle.md). The prefix is not displayed when [SHOW CREATE TABLE](../show/show-create-table.md) is executed in SQL_MODE=DEFAULT, or when a non-ambiguous data type is displayed.


Note, the `<code>mariadb_schema</code>` prefix can be used with any data type, including non-ambiguous ones:


```
CREATE OR REPLACE TABLE t1 (a mariadb_schema.INT);
SHOW CREATE TABLE t1;
+-------+--------------------------------------------------+
| Table | Create Table                                     |
+-------+--------------------------------------------------+
| t1    | CREATE TABLE "t1" (
  "a" int(11) DEFAULT NULL
) |
+-------+--------------------------------------------------+
```

Currently the `<code>mariadb_schema</code>` prefix is only used in the following case:


* For a MariaDB native [DATE](../../../sql-language-structure/date-and-time-literals.md) type when running [SHOW CREATE TABLE](../show/show-create-table.md) in [Oracle mode](../../../../../../release-notes/mariadb-community-server/compatibility-and-differences/sql_modeoracle.md).


## History


When running with [SQL_MODE=ORACLE](../../../../../../release-notes/mariadb-community-server/compatibility-and-differences/sql_modeoracle.md), MariaDB server translates the data type `<code>DATE</code>` to `<code>DATETIME</code>`, for better Oracle compatibility:


```
SET SQL_mode=ORACLE;
CREATE OR REPLACE TABLE t1 (
  d DATE
);
SHOW CREATE TABLE t1;
+-------+---------------------------------------------------+
| Table | Create Table                                      |
+-------+---------------------------------------------------+
| t1    | CREATE TABLE "t1" (
  "d" datetime DEFAULT NULL
) |
+-------+---------------------------------------------------+
```

Notice, `<code>DATE</code>` was translated to `<code>DATETIME</code>`.


This translation may cause some ambiguity. Suppose a user creates a table with a column of the traditional MariaDB `<code>DATE</code>` data type using the default sql_mode, but then switches to [SQL_MODE=ORACLE](../../../../../../release-notes/mariadb-community-server/compatibility-and-differences/sql_modeoracle.md) and runs a [SHOW CREATE TABLE](../show/show-create-table.md) statement:


```
SET sql_mode=DEFAULT;
CREATE OR REPLACE TABLE t1 (
  d DATE
);
SET SQL_mode=ORACLE;
SHOW CREATE TABLE t1;
```

Before `<code>mariadb_schema</code>` was introduced, the above script displayed:


```
CREATE TABLE "t1" (
  "d" date DEFAULT NULL
);
```

which had two problems:


* It was confusing for the reader: its not clear if it is the traditional MariaDB `<code>DATE</code>`, or is it Oracle-alike date (which is actually `<code>DATETIME</code>`);
* It broke replication and caused data type mismatch on the master and on the slave (see [MDEV-19632](https://jira.mariadb.org/browse/MDEV-19632)).


To address this problem, starting from the mentioned versions, MariaDB uses the idea of qualified data types:


```
SET sql_mode=DEFAULT;
CREATE OR REPLACE TABLE t1 (
  d DATE
);
SET SQL_mode=ORACLE;
SHOW CREATE TABLE t1;
+-------+--------------------------------------------------------------+
| Table | Create Table                                                 |
+-------+--------------------------------------------------------------+
| t1    | CREATE TABLE "t1" (
  "d" mariadb_schema.date DEFAULT NULL
) |
+-------+--------------------------------------------------------------+
```
