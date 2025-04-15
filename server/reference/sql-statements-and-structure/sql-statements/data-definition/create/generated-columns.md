
# Generated (Virtual and Persistent/Stored) Columns

## Syntax


```
<type>  [GENERATED ALWAYS]  AS   ( <expression> )
[VIRTUAL | PERSISTENT | STORED]  [UNIQUE] [UNIQUE KEY] [COMMENT <text>]
```


MariaDB's generated columns syntax is designed to be similar to the syntax for [Microsoft SQL Server's computed columns](https://docs.microsoft.com/en-us/sql/relational-databases/tables/specify-computed-columns-in-a-table?view=sql-server-2017) and [Oracle Database's virtual columns](https://oracle-base.com/articles/11g/virtual-columns-11gr1). In [MariaDB 10.2](../../../../../../release-notes/mariadb-community-server/what-is-mariadb-102.md) and later, the syntax is also compatible with the syntax for [MySQL's generated columns](https://dev.mysql.com/doc/refman/5.7/en/create-table-generated-columns.html).


## Description


A generated column is a column in a table that cannot explicitly be set to a specific value in a [DML query](../../data-manipulation/README.md). Instead, its value is automatically generated based on an expression. This expression might generate the value based on the values of other columns in the table, or it might generate the value by calling [built-in functions](../../built-in-functions/README.md) or [user-defined functions (UDFs)](../../../../../server-usage/programming-customizing-mariadb/user-defined-functions/user-defined-functions-security.md).


There are two types of generated columns:


* `<code>PERSISTENT</code>` (a.k.a. `<code>STORED</code>`): This type's value is actually stored in the table.
* `<code>VIRTUAL</code>`: This type's value is not stored at all. Instead, the value is generated dynamically when the table is queried. This type is the default.


Generated columns are also sometimes called computed columns or virtual columns.


## Supported Features


### Storage Engine Support


* Generated columns can only be used with storage engines which support them. If you try to use a storage engine that does not support them, then you will see an error similar to the following:


```
ERROR 1910 (HY000): TokuDB storage engine does not support computed columns
```

* [InnoDB](../../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/innodb-upgrade-tests/README.md), [Aria](../../../../storage-engines/s3-storage-engine/aria_s3_copy.md), [MyISAM](../../../../storage-engines/myisam-storage-engine/myisam-system-variables.md) and [CONNECT](../../../../storage-engines/connect/using-connect/using-connect-virtual-and-special-columns.md) support generated columns.


* A column in a [MERGE](../../../../storage-engines/merge.md) table can be built on a `<code>PERSISTENT</code>` generated column.

  * However, a column in a MERGE table can not be defined as a `<code>VIRTUAL</code>` and `<code>PERSISTENT</code>` generated column.


### Data Type Support


* All data types are supported when defining generated columns.


* Using the [ZEROFILL](../../../vectors/create-table-with-vectors.md#zerofill-column-option) column option is supported when defining generated columns.


* Using the [AUTO_INCREMENT](../../../../storage-engines/innodb/auto_increment-handling-in-innodb.md) column option is not supported when defining generated columns. Until [MariaDB 10.2.25](../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-10225-release-notes.md), it was supported, but this support was removed, because it would not work correctly. See [MDEV-11117](https://jira.mariadb.org/browse/MDEV-11117).


### Index Support


* Using a generated column as a table's primary key is not supported. See [MDEV-5590](https://jira.mariadb.org/browse/MDEV-5590) for more information. If you try to use one as a primary key, then you will see an error similar to the following:


```
ERROR 1903 (HY000): Primary key cannot be defined upon a computed column
```

* Using `<code>PERSISTENT</code>` generated columns as part of a [foreign key](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/optimization-and-indexes/foreign-keys.md) is supported.


* Referencing `<code>PERSISTENT</code>` generated columns as part of a [foreign key](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/optimization-and-indexes/foreign-keys.md) is also supported.

  * However, using the `<code>ON UPDATE CASCADE</code>`, `<code>ON UPDATE SET NULL</code>`, or `<code>ON DELETE SET NULL</code>` clauses is not supported. If you try to use an unsupported clause, then you will see an error similar to the following:


```
ERROR 1905 (HY000): Cannot define foreign key with ON UPDATE SET NULL clause on a computed column
```

* Defining indexes on both `<code>VIRTUAL</code>` and `<code>PERSISTENT</code>` generated columns is supported.

  * If an index is defined on a generated column, then the optimizer considers using it in the same way as indexes based on "real" columns.
* From [MariaDB 11.8](../../../../../../release-notes/mariadb-community-server/what-is-mariadb-118.md), the optimizer can recognize use of indexed virtual column expressions in the WHERE clause and use them to construct range and ref(const) accesses. See [Virtual Column Support in the Optimizer](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/query-optimizations/virtual-column-support-in-the-optimizer.md).


### Statement Support


* Generated columns are used in [DML queries](../../data-manipulation/README.md) just as if they were "real" columns.

  * However, `<code>VIRTUAL</code>` and `<code>PERSISTENT</code>` generated columns differ in how their data is stored.

    * Values for `<code>PERSISTENT</code>` generated columns are generated whenever a [DML queries](../../data-manipulation/README.md) inserts or updates the row with the special `<code>DEFAULT</code>` value. This generates the columns value, and it is stored in the table like the other "real" columns. This value can be read by other [DML queries](../../data-manipulation/README.md) just like the other "real" columns.
    * Values for `<code>VIRTUAL</code>` generated columns are not stored in the table. Instead, the value is generated dynamically whenever the column is queried. If other columns in a row are queried, but the `<code>VIRTUAL</code>` generated column is not one of the queried columns, then the column's value is not generated.


* The [SELECT](../../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/benchmarks-and-long-running-tests/benchmark-results/select-random-ranges-and-select-random-point.md) statement supports generated columns.


* Generated columns can be referenced in the [INSERT](../../built-in-functions/string-functions/insert-function.md), [UPDATE](../../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/tools/buildbot/buildbot-setup/buildbot-setup-for-virtual-machines/buildbot-setup-for-virtual-machines-additional-steps/update-debian-4-mirrors-for-buildbot-vms.md), and [DELETE](../../data-manipulation/changing-deleting-data/delete.md) statements.

  * However, `<code>VIRTUAL</code>` or `<code>PERSISTENT</code>` generated columns cannot be explicitly set to any other values than `<code>NULL</code>` or [DEFAULT](../../built-in-functions/secondary-functions/information-functions/default.md). If a generated column is explicitly set to any other value, then the outcome depends on whether [strict mode](../../../../../server-management/variables-and-modes/sql-mode.md#strict-mode) is enabled in [sql_mode](../../../../../server-management/variables-and-modes/sql-mode.md). If it is not enabled, then a warning will be raised and the default generated value will be used instead. If it is enabled, then an error will be raised instead.


* The [CREATE TABLE](../../../vectors/create-table-with-vectors.md) statement has limited support for generated columns.

  * It supports defining generated columns in a new table.
  * It supports using generated columns to [partition tables](../../../../../server-management/partitioning-tables/README.md).
  * It does not support using the [versioning clauses](../../../temporal-tables/system-versioned-tables.md) with generated columns.


* The [ALTER TABLE](../alter/alter-tablespace.md) statement has limited support for generated columns.

  * It supports the `<code>MODIFY</code>` and `<code>CHANGE</code>` clauses for `<code>PERSISTENT</code>` generated columns.
  * It does not support the `<code>MODIFY</code>` clause for `<code>VIRTUAL</code>` generated columns if [ALGORITHM](../alter/alter-tablespace.md#algorithm) is not set to `<code>COPY</code>`. See [MDEV-15476](https://jira.mariadb.org/browse/MDEV-15476) for more information.
  * It does not support the `<code>CHANGE</code>` clause for `<code>VIRTUAL</code>` generated columns if [ALGORITHM](../alter/alter-tablespace.md#algorithm) is not set to `<code>COPY</code>`. See [MDEV-17035](https://jira.mariadb.org/browse/MDEV-17035) for more information.
  * It does not support altering a table if [ALGORITHM](../alter/alter-tablespace.md#algorithm) is not set to `<code>COPY</code>` if the table has a `<code>VIRTUAL</code>` generated column that is indexed. See [MDEV-14046](https://jira.mariadb.org/browse/MDEV-14046) for more information.
  * It does not support adding a `<code>VIRTUAL</code>` generated column with the `<code>ADD</code>` clause if the same statement is also adding other columns if [ALGORITHM](../alter/alter-tablespace.md#algorithm) is not set to `<code>COPY</code>`. See [MDEV-17468](https://jira.mariadb.org/browse/MDEV-17468) for more information.
  * It also does not support altering an existing column into a `<code>VIRTUAL</code>` generated column.
  * It supports using generated columns to [partition tables](../../../../../server-management/partitioning-tables/README.md).
  * It does not support using the [versioning clauses](../../../temporal-tables/system-versioned-tables.md) with generated columns.


* The [SHOW CREATE TABLE](../../administrative-sql-statements/show/show-create-table.md) statement supports generated columns.


* The [DESCRIBE](../../administrative-sql-statements/describe.md) statement can be used to check whether a table has generated columns.

  * You can tell which columns are generated by looking for the ones where the `<code>Extra</code>` column is set to either `<code>VIRTUAL</code>` or `<code>PERSISTENT</code>`. For example:


```
DESCRIBE table1;
+-------+-------------+------+-----+---------+------------+
| Field | Type        | Null | Key | Default | Extra      |
+-------+-------------+------+-----+---------+------------+
| a     | int(11)     | NO   |     | NULL    |            |
| b     | varchar(32) | YES  |     | NULL    |            |
| c     | int(11)     | YES  |     | NULL    | VIRTUAL    |
| d     | varchar(5)  | YES  |     | NULL    | PERSISTENT |
+-------+-------------+------+-----+---------+------------+
```

* Generated columns can be properly referenced in the `<code>NEW</code>` and `<code>OLD</code>` rows in [triggers](../../../../../server-usage/programming-customizing-mariadb/triggers-events/triggers/triggers-and-implicit-locks.md).


* [Stored procedures](../../../../../server-usage/programming-customizing-mariadb/stored-routines/stored-procedures/README.md) support generated columns.


* The [HANDLER](../../../nosql/handler/handler-commands.md) statement supports generated columns.


### Expression Support


* Most legal, deterministic expressions which can be calculated are supported in expressions for generated columns.


* Most [built-in functions](../../built-in-functions/README.md) are supported in expressions for generated columns.

  * However, some [built-in functions](../../built-in-functions/README.md) can't be supported for technical reasons. For example, If you try to use an unsupported function in an expression, an error is generated similar to the following:


```
ERROR 1901 (HY000): Function or expression 'dayname()' cannot be used in the GENERATED ALWAYS AS clause of `v`
```

* [Subqueries](../../data-manipulation/selecting-data/joins-subqueries/subqueries/subqueries-and-all.md) are not supported in expressions for generated columns because the underlying data can change.


* Using anything that depends on data outside the row is not supported in expressions for generated columns.


* [Stored functions](../../../../../server-usage/programming-customizing-mariadb/stored-routines/stored-functions/README.md) are not supported in expressions for generated columns. See [MDEV-17587](https://jira.mariadb.org/browse/MDEV-17587) for more information.


* Non-deterministic [built-in functions](../../built-in-functions/README.md) are supported in expressions for not indexed `<code>VIRTUAL</code>` generated columns.


* Non-deterministic [built-in functions](../../built-in-functions/README.md) are not supported in expressions for `<code>PERSISTENT</code>` or indexed `<code>VIRTUAL</code>` generated columns.


* [User-defined functions (UDFs)](../../../../../server-usage/programming-customizing-mariadb/user-defined-functions/user-defined-functions-security.md) are supported in expressions for generated columns.

  * However, MariaDB can't check whether a UDF is deterministic, so it is up to the user to be sure that they do not use non-deterministic UDFs with `<code>VIRTUAL</code>` generated columns.


* Defining a generated column based on other generated columns defined before it in the table definition is supported. For example:


```
CREATE TABLE t1 (a int as (1), b int as (a));
```

* However, defining a generated column based on other generated columns defined after in the table definition is not supported in expressions for generation columns because generated columns are calculated in the order they are defined.


* Using an expression that exceeds 255 characters in length is supported in expressions for generated columns. The new limit for the entire table definition, including all expressions for generated columns, is 65,535 bytes.


* Using constant expressions is supported in expressions for generated columns. For example:


```
CREATE TABLE t1 (a int as (1));
```

### Making Stored Values Consistent


When a generated column is `<code>PERSISTENT</code>` or indexed, the value of the expression needs to be consistent regardless of the [SQL Mode](../../../../../server-management/variables-and-modes/sql-mode.md) flags in the current session. If it is not, then the table will be seen as corrupted when the value that should actually be returned by the computed expression and the value that was previously stored and/or indexed using a different [sql_mode](../../../../../server-management/variables-and-modes/sql-mode.md) setting disagree.


There are currently two affected classes of inconsistencies: character padding and unsigned subtraction:


* For a `<code>VARCHAR</code>` or `<code>TEXT</code>` generated column the length of the value returned can vary depending on the PAD_CHAR_TO_FULL_LENGTH [sql_mode](../../../../../server-management/variables-and-modes/sql-mode.md) flag. To make the value consistent, create the generated column using an RTRIM() or RPAD() function. Alternately, create the generated column as a `<code>CHAR</code>` column so that its data is always fully padded.


* If a `<code>SIGNED</code>` generated column is based on the subtraction of an `<code>UNSIGNED</code>` value, the resulting value can vary depending on how large the value is and the NO_UNSIGNED_SUBTRACTION [sql_mode](../../../../../server-management/variables-and-modes/sql-mode.md) flag. To make the value consistent, use [CAST()](../../built-in-functions/string-functions/cast.md) to ensure that each `<code>UNSIGNED</code>` operand is `<code>SIGNED</code>` before the subtraction.



##### MariaDB starting with [10.5](../../../../../../release-notes/mariadb-community-server/what-is-mariadb-105.md)
Beginning in [MariaDB 10.5](../../../../../../release-notes/mariadb-community-server/what-is-mariadb-105.md), there is a fatal error generated when trying to create a generated column whose value can change depending on the [SQL Mode](../../../../../server-management/variables-and-modes/sql-mode.md) when its data is `<code>PERSISTENT</code>` or indexed.
For an existing generated column that has a potentially inconsistent value, a warning about a bad expression is generated the first time it is used (if warnings are enabled).
Beginning in [MariaDB 10.4.8](../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-4-series/mariadb-1048-release-notes.md), [MariaDB 10.3.18](../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-10318-release-notes.md), and [MariaDB 10.2.27](../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-10227-release-notes.md) a potentially inconsistent generated column outputs a warning when created or first used (without restricting their creation).


Here is an example of two tables that would be rejected in [MariaDB 10.5](../../../../../../release-notes/mariadb-community-server/what-is-mariadb-105.md) and warned about in the other listed versions:


```
CREATE TABLE bad_pad (
  txt CHAR(5),
  -- CHAR -> VARCHAR or CHAR -> TEXT can't be persistent or indexed:
  vtxt VARCHAR(5) AS (txt) PERSISTENT
);

CREATE TABLE bad_sub (
  num1 BIGINT UNSIGNED,
  num2 BIGINT UNSIGNED,
  -- The resulting value can vary for some large values
  vnum BIGINT AS (num1 - num2) VIRTUAL,
  KEY(vnum)
);
```

The warnings for the above tables look like this:


```
Warning (Code 1901): Function or expression '`txt`' cannot be used in the GENERATED ALWAYS AS clause of `vtxt`
Warning (Code 1105): Expression depends on the @@sql_mode value PAD_CHAR_TO_FULL_LENGTH

Warning (Code 1901): Function or expression '`num1` - `num2`' cannot be used in the GENERATED ALWAYS AS clause of `vnum`
Warning (Code 1105): Expression depends on the @@sql_mode value NO_UNSIGNED_SUBTRACTION
```

To work around the issue, force the padding or type to make the generated column's expression return a consistent value. For example:


```
CREATE TABLE good_pad (
  txt CHAR(5),
  -- Using RTRIM() or RPAD() makes the value consistent:
  vtxt VARCHAR(5) AS (RTRIM(txt)) PERSISTENT,
  -- When not persistent or indexed, it is OK for the value to vary by mode:
  vtxt2 VARCHAR(5) AS (txt) VIRTUAL,
  -- CHAR -> CHAR is always OK:
  txt2 CHAR(5) AS (txt) PERSISTENT
);

CREATE TABLE good_sub (
  num1 BIGINT UNSIGNED,
  num2 BIGINT UNSIGNED,
  -- The indexed value will always be consistent in this expression:
  vnum BIGINT AS (CAST(num1 AS SIGNED) - CAST(num2 AS SIGNED)) VIRTUAL,
  KEY(vnum)
);
```

### MySQL Compatibility Support


* The `<code>STORED</code>` keyword is supported as an alias for the `<code>PERSISTENT</code>` keyword.


* Tables created with MySQL 5.7 or later that contain [MySQL's generated columns](https://dev.mysql.com/doc/refman/5.7/en/create-table-generated-columns.html) can be imported into MariaDB without a dump and restore.


## Implementation Differences


Generated columns are subject to various constraints in other DBMSs that are not present in MariaDB's implementation. Generated columns may also be called computed columns or virtual columns in different implementations. The various details for a specific implementation can be found in the documentation for each specific DBMS.


### Implementation Differences Compared to Microsoft SQL Server


MariaDB's generated columns implementation does not enforce the following
restrictions that are present in [Microsoft SQL Server's computed columns](https://docs.microsoft.com/en-us/sql/relational-databases/tables/specify-computed-columns-in-a-table?view=sql-server-2017) implementation:


* MariaDB allows [server variables](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/system-and-status-variables-added-by-major-release/system-and-status-variables-added-by-major-unmaintained-release/system-variables-added-in-mariadb-11-1.md) in generated column expressions, including those that change dynamically, such as [warning_count](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#warning_count).
* MariaDB allows the [CONVERT_TZ()](../../built-in-functions/date-time-functions/convert_tz.md) function to be called with a named [time zone](../../../../data-types/string-data-types/character-sets/internationalization-and-localization/time-zones.md) as an argument, even though time zone names and time offsets are configurable.
* MariaDB allows the [CAST()](../../built-in-functions/string-functions/cast.md) function to be used with non-unicode [character sets](../../../../data-types/string-data-types/character-sets/README.md), even though character sets are configurable and differ between binaries/versions.
* MariaDB allows [FLOAT](../../../../data-types/data-types-numeric-data-types/float.md) expressions to be used in generated columns. Microsoft SQL Server considers these expressions to be "imprecise" due to potential cross-platform differences in floating-point implementations and precision.
* Microsoft SQL Server requires the [ARITHABORT](https://docs.microsoft.com/en-us/sql/t-sql/statements/set-arithabort-transact-sql?view=sql-server-2017) mode to be set, so that division by zero returns an error, and not a NULL.
* Microsoft SQL Server requires `<code>QUOTED_IDENTIFIER</code>` to be set in [sql_mode](../../../../../server-management/variables-and-modes/sql-mode.md). In MariaDB, if data is inserted without `<code>ANSI_QUOTES</code>` set in [sql_mode](../../../../../server-management/variables-and-modes/sql-mode.md), then it will be processed and stored differently in a generated column that contains quoted identifiers.


Microsoft SQL Server enforces the above restrictions by doing one of the following things:


* Refusing to create computed columns.
* Refusing to allow updates to a table containing them.
* Refusing to use an index over such a column if it can not be guaranteed that the expression is fully deterministic.


In MariaDB, as long as the [sql_mode](../../../../../server-management/variables-and-modes/sql-mode.md), language, and other settings that were in effect during the CREATE TABLE remain unchanged, the generated column expression will always be evaluated the same. If any of these things change, then please be aware that the generated column expression might not be
evaluated the same way as it previously was.


If you try to update a virtual column, you will get an error if the default [strict mode](../../../../../server-management/variables-and-modes/sql-mode.md#strict-mode) is enabled in [sql_mode](../../../../../server-management/variables-and-modes/sql-mode.md), or a warning otherwise.


## Development History


Generated columns was originally developed by Andrey Zhakov. It was then modified by Sanja Byelkin and Igor Babaev at Monty Program for inclusion in MariaDB. Monty did the work on [MariaDB 10.2](../../../../../../release-notes/mariadb-community-server/what-is-mariadb-102.md) to lift a some of the old limitations.


## Examples


Here is an example table that uses both `<code class="fixed" style="white-space:pre-wrap">VIRTUAL</code>` and
`<code class="fixed" style="white-space:pre-wrap">PERSISTENT</code>` virtual columns:


```
USE TEST;

CREATE TABLE table1 (
     a INT NOT NULL,
     b VARCHAR(32),
     c INT AS (a mod 10) VIRTUAL,
     d VARCHAR(5) AS (left(b,5)) PERSISTENT);
```

If you describe the table, you can easily see which columns are virtual by
looking in the "Extra" column:


```
DESCRIBE table1;
+-------+-------------+------+-----+---------+------------+
| Field | Type        | Null | Key | Default | Extra      |
+-------+-------------+------+-----+---------+------------+
| a     | int(11)     | NO   |     | NULL    |            |
| b     | varchar(32) | YES  |     | NULL    |            |
| c     | int(11)     | YES  |     | NULL    | VIRTUAL    |
| d     | varchar(5)  | YES  |     | NULL    | PERSISTENT |
+-------+-------------+------+-----+---------+------------+
```

To find out what function(s) generate the value of the virtual column you can use `<code class="fixed" style="white-space:pre-wrap">SHOW CREATE TABLE</code>`:


```
SHOW CREATE TABLE table1;

| table1 | CREATE TABLE `table1` (
  `a` int(11) NOT NULL,
  `b` varchar(32) DEFAULT NULL,
  `c` int(11) AS (a mod 10) VIRTUAL,
  `d` varchar(5) AS (left(b,5)) PERSISTENT
) ENGINE=MyISAM DEFAULT CHARSET=latin1 |
```

If you try to insert non-default values into a virtual column, you will receive
a warning and what you tried to insert will be ignored and the derived value
inserted instead:


```
WARNINGS;
Show warnings enabled.

INSERT INTO table1 VALUES (1, 'some text',default,default);
Query OK, 1 row affected (0.00 sec)

INSERT INTO table1 VALUES (2, 'more text',5,default);
Query OK, 1 row affected, 1 warning (0.00 sec)

Warning (Code 1645): The value specified for computed column 'c' in table 'table1' has been ignored.

INSERT INTO table1 VALUES (123, 'even more text',default,'something');
Query OK, 1 row affected, 2 warnings (0.00 sec)

Warning (Code 1645): The value specified for computed column 'd' in table 'table1' has been ignored.
Warning (Code 1265): Data truncated for column 'd' at row 1

SELECT * FROM table1;
+-----+----------------+------+-------+
| a   | b              | c    | d     |
+-----+----------------+------+-------+
|   1 | some text      |    1 | some  |
|   2 | more text      |    2 | more  |
| 123 | even more text |    3 | even  |
+-----+----------------+------+-------+
3 rows in set (0.00 sec)
```

If the `<code>ZEROFILL</code>` clause is specified, it should be placed directly after the type definition, before the `<code>AS (<expression>)</code>`:


```
CREATE TABLE table2 (a INT, b INT ZEROFILL AS (a*2) VIRTUAL);
INSERT INTO table2 (a) VALUES (1);

SELECT * FROM table2;
+------+------------+
| a    | b          |
+------+------------+
|    1 | 0000000002 |
+------+------------+
1 row in set (0.00 sec)
```

You can also use virtual columns to implement a "poor man's partial index". See example at the end of [Unique Index](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/optimization-and-indexes/getting-started-with-indexes.md#unique-index).


## See Also


* [Putting Virtual Columns to good use](https://mariadb.com/blog/putting-virtual-columns-good-use) on the mariadb.com blog.

