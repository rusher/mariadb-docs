# SHOW CREATE TABLE

## Syntax

```
SHOW CREATE TABLE tbl_name
```

## Description

Shows the [CREATE TABLE](../../data-definition/create/create-table.md) statement that creates the given table. The statement requires the [SELECT privilege](../../data-manipulation/selecting-data/select.md) for the table. This statement also works with [views](../../../../server-usage/views/) and [SEQUENCE](../../../sql-structure/sequences/create-sequence.md).

`SHOW CREATE TABLE` quotes table and\
column names according to the value of the [sql\_quote\_show\_create](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#sql_quote_show_create) server system variable.

Certain [SQL\_MODE](../../../../server-management/variables-and-modes/sql-mode.md) values can result in parts of the original CREATE statement not being included in the output. MariaDB-specific table options, column options, and index options are not included in the output of this statement if the [NO\_TABLE\_OPTIONS](../../../../server-management/variables-and-modes/sql-mode.md#no_table_options), [NO\_FIELD\_OPTIONS](../../../../server-management/variables-and-modes/sql-mode.md#no_field_options) and [NO\_KEY\_OPTIONS](../../../../server-management/variables-and-modes/sql-mode.md#no_key_options) [SQL\_MODE](../../../../server-management/variables-and-modes/sql-mode.md) flags are used. All MariaDB-specific table attributes are also not shown when a non-MariaDB/MySQL emulation mode is used, which includes [ANSI](../../../../server-management/variables-and-modes/sql-mode.md#ansi), [DB2](../../../../server-management/variables-and-modes/sql-mode.md#db2), [POSTGRESQL](../../../../server-management/variables-and-modes/sql-mode.md#postgresql), [MSSQL](../../../../server-management/variables-and-modes/sql-mode.md#mssql), [MAXDB](../../../../server-management/variables-and-modes/sql-mode.md#maxdb) or [ORACLE](../../../../server-management/variables-and-modes/sql-mode.md#oracle).

Invalid table options, column options and index options are normally commented out (note, that it is possible to create a table with invalid options, by altering a table of a different engine, where these options were valid). To have them uncommented, enable the [IGNORE\_BAD\_TABLE\_OPTIONS](../../../../server-management/variables-and-modes/sql-mode.md#ignore_bad_table_options) [SQL\_MODE](../../../../server-management/variables-and-modes/sql-mode.md). Remember that replaying a [CREATE TABLE](../../data-definition/create/create-table.md) statement with uncommented invalid options will fail with an error, unless the [IGNORE\_BAD\_TABLE\_OPTIONS](../../../../server-management/variables-and-modes/sql-mode.md#ignore_bad_table_options) [SQL\_MODE](../../../../server-management/variables-and-modes/sql-mode.md) is in effect.

Note that `SHOW CREATE TABLE` is not meant to provide metadata about a table. It provides information about how the table was declared, but the real table structure could differ a bit. For example, if an index has been declared as `HASH`, the `CREATE TABLE` statement returned by `SHOW CREATE TABLE` will declare that index as `HASH`; however, it is possible that the index is in fact a `BTREE`, because the storage engine does not support `HASH`.

MariaDB permits [TEXT](../../../data-types/string-data-types/text.md) and [BLOB](../../../data-types/string-data-types/blob.md) data types to be assigned a [DEFAULT](../../data-definition/create/create-table.md#default) value. As a result, `SHOW CREATE TABLE` will append a `DEFAULT NULL` to nullable TEXT or BLOB fields if no specific default is provided.

Numbers are no longer quoted in the `DEFAULT` clause in `SHOW CREATE` statement. Prior to [MariaDB 10.2.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1022-release-notes), MariaDB quoted numbers.

### Index Order

Indexes are sorted and displayed in the following order, which may differ from the order of the CREATE TABLE statement.

* PRIMARY KEY
* UNIQUE keys where all column are NOT NULL
* UNIQUE keys that don't contain partial segments
* Other UNIQUE keys
* LONG UNIQUE keys
* Normal keys
* Fulltext keys

See sql/sql\_table.cc for details.

## Examples

```
SHOW CREATE TABLE t\G
*************************** 1. row ***************************
       Table: t
Create Table: CREATE TABLE `t` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `s` char(60) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1
```

With [sql\_quote\_show\_create](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#sql_quote_show_create) off:

```
SHOW CREATE TABLE t\G
*************************** 1. row ***************************
       Table: t
Create Table: CREATE TABLE t (
  id int(11) NOT NULL AUTO_INCREMENT,
  s char(60) DEFAULT NULL,
  PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1
```

Unquoted numeric DEFAULTs, from [MariaDB 10.2.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1022-release-notes):

```
CREATE TABLE td (link TINYINT DEFAULT 1);

SHOW CREATE TABLE td\G
*************************** 1. row ***************************
       Table: td
Create Table: CREATE TABLE `td` (
  `link` tinyint(4) DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=latin1
```

Quoted numeric DEFAULTs, until [MariaDB 10.2.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1021-release-notes):

```
CREATE TABLE td (link TINYINT DEFAULT 1);

SHOW CREATE TABLE td\G
*************************** 1. row ***************************
       Table: td
Create Table: CREATE TABLE `td` (
  `link` tinyint(4) DEFAULT '1'
) ENGINE=InnoDB DEFAULT CHARSET=latin1
```

[SQL\_MODE](../../../../server-management/variables-and-modes/sql-mode.md) impacting the output:

```
SELECT @@sql_mode;
+-------------------------------------------------------------------------------------------+
| @@sql_mode                                                                                |
+-------------------------------------------------------------------------------------------+
| STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION |
+-------------------------------------------------------------------------------------------+

CREATE TABLE `t1` (
       `id` int(11) NOT NULL AUTO_INCREMENT,
       `msg` varchar(100) DEFAULT NULL,
       PRIMARY KEY (`id`)
     ) ENGINE=InnoDB DEFAULT CHARSET=latin1
;

SHOW CREATE TABLE t1\G
*************************** 1. row ***************************
       Table: t1
Create Table: CREATE TABLE `t1` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `msg` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1

SET SQL_MODE=ORACLE;

SHOW CREATE TABLE t1\G
*************************** 1. row ***************************
       Table: t1
Create Table: CREATE TABLE "t1" (
  "id" int(11) NOT NULL,
  "msg" varchar(100) DEFAULT NULL,
  PRIMARY KEY ("id")
```

## See Also

* [SHOW CREATE SEQUENCE](show-create-sequence.md)
* [SHOW CREATE VIEW](show-create-view.md)

GPLv2 fill\_help\_tables.sql

{% @marketo/form formId="4316" %}
