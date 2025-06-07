# Setting Character Sets and Collations

Prior to [MariaDB 11.6.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-6-rolling-releases/mariadb-11-6-0-release-notes), the default [character set](./) is `latin1` and the default collation is `latin1_swedish_ci`. From [MariaDB 11.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-6-rolling-releases/what-is-mariadb-116), the default character set is `utf8mb4` and the default collation is `utf8mb4_uca1400_ai_ci`.\
This may differ in some distros, see for example [Differences in MariaDB in Debian](../../../../server-management/install-and-upgrade-mariadb/troubleshooting-installation-issues/installation-issues-on-debian-and-ubuntu/differences-in-mariadb-in-debian-and-ubuntu.md).

The character sets and the collations can be specified from the server right down to the column level, as well as for client-server connections. When changing a character set and not specifying a collation, the default collation for the new character set is always used.

Character sets and collations always cascade down, so a column without a specified collation will look for the table default, the table for the database, and the database for the server. It's therefore possible to have extremely fine-grained control over all the character sets and collations used in your data.

Default collations for each character set can be viewed with the [SHOW COLLATION](../../../sql-statements/administrative-sql-statements/show/show-collation.md) statement, for example, to find the default collation for the latin2 character set:

```
SHOW COLLATION LIKE 'latin2%';
+---------------------+---------+----+---------+----------+---------+
| Collation           | Charset | Id | Default | Compiled | Sortlen |
+---------------------+---------+----+---------+----------+---------+
| latin2_czech_cs     | latin2  |  2 |         | Yes      |       4 |
| latin2_general_ci   | latin2  |  9 | Yes     | Yes      |       1 |
| latin2_hungarian_ci | latin2  | 21 |         | Yes      |       1 |
| latin2_croatian_ci  | latin2  | 27 |         | Yes      |       1 |
| latin2_bin          | latin2  | 77 |         | Yes      |       1 |
+---------------------+---------+----+---------+----------+---------+
```

## Server Level

The [character\_set\_server](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#character_set_server) system variable can be used to change the default server character set. It can be set both on startup or dynamically, with the [SET](../../../sql-statements/administrative-sql-statements/set-commands/set.md) command:

```
SET character_set_server = 'latin2';
```

Similarly, the [collation\_server](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#collation_server) variable is used for setting the default server collation.

```
SET collation_server = 'latin2_czech_cs';
```

## Database Level

The [CREATE DATABASE](../../../sql-statements/data-definition/create/create-database.md) and [ALTER DATABASE](../../../sql-statements/data-definition/alter/alter-database.md) statements have optional character set and collation clauses. If these are left out, the server defaults are used.

```
CREATE DATABASE czech_slovak_names 
  CHARACTER SET = 'keybcs2'
  COLLATE = 'keybcs2_bin';
```

```
ALTER DATABASE czech_slovak_names COLLATE = 'keybcs2_general_ci';
```

To determine the default character set used by a database, use:

```
SHOW CREATE DATABASE czech_slovak_names;
+--------------------+--------------------------------------------------------------------------------+
| Database           | Create Database                                                                |
+--------------------+--------------------------------------------------------------------------------+
| czech_slovak_names | CREATE DATABASE `czech_slovak_names` /*!40100 DEFAULT CHARACTER SET keybcs2 */ |
+--------------------+--------------------------------------------------------------------------------+
```

or alternatively, for the character set and collation:

```
SELECT * FROM INFORMATION_SCHEMA.SCHEMATA;
+--------------+--------------------+----------------------------+------------------------+----------+
| CATALOG_NAME | SCHEMA_NAME        | DEFAULT_CHARACTER_SET_NAME | DEFAULT_COLLATION_NAME | SQL_PATH |
+--------------+--------------------+----------------------------+------------------------+----------+
| def          | czech_slovak_names | keybcs2                    | keybcs2_general_ci     | NULL     |
| def          | information_schema | utf8                       | utf8_general_ci        | NULL     |
| def          | mysql              | latin1                     | latin1_swedish_ci      | NULL     |
| def          | performance_schema | utf8                       | utf8_general_ci        | NULL     |
| def          | test               | latin1                     | latin1_swedish_ci      | NULL     |
+--------------+--------------------+----------------------------+------------------------+----------+
```

It is also possible to specify only the collation, and, since each collation only applies to one character set, the associated character set will automatically be specified.

```
CREATE DATABASE danish_names COLLATE 'utf8_danish_ci';

SHOW CREATE DATABASE danish_names;
+--------------+----------------------------------------------------------------------------------------------+
| Database     | Create Database                                                                              |
+--------------+----------------------------------------------------------------------------------------------+
| danish_names | CREATE DATABASE `danish_names` /*!40100 DEFAULT CHARACTER SET utf8 COLLATE utf8_danish_ci */ |
+--------------+----------------------------------------------------------------------------------------------+
```

Although there are [character\_set\_database](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#character_set_database) and [collation\_database](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#collation_database) system variables which can be set dynamically, these are used for determining the character set and collation for the default database, and should only be set by the server.

## Table Level

The [CREATE TABLE](../../../sql-statements/data-definition/create/create-table.md) and [ALTER TABLE](../../../sql-statements/data-definition/alter/alter-table.md) statements support optional character set and collation clauses, a MariaDB and MySQL extension to standard SQL.

```
CREATE TABLE english_names (id INT, name VARCHAR(40)) 
  CHARACTER SET 'utf8' 
  COLLATE 'utf8_icelandic_ci';
```

If neither character set nor collation is provided, the database default will be used. If only the character set is provided, the default collation for that character set will be used . If only the collation is provided, the associated character set will be used. See [Supported Character Sets and Collations](supported-character-sets-and-collations.md).

```
ALTER TABLE table_name
 CONVERT TO CHARACTER SET charset_name [COLLATE collation_name];
```

If no collation is provided, the collation will be set to the default collation for that character set. See [Supported Character Sets and Collations](supported-character-sets-and-collations.md).

For [VARCHAR](../varchar.md) or [TEXT](../text.md) columns, CONVERT TO CHARACTER SET changes the data type if needed to ensure the new column is long enough to store as many characters as the original column.

For example, an ascii TEXT column requires a single byte per character, so the column can hold up to 65,535 characters. If the column is converted to utf8mb4 (default from [MariaDB 11.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-6-rolling-releases/what-is-mariadb-116)), 4 bytes can be required for each character, so the column will be converted to [MEDIUMTEXT](../mediumtext.md) to be able to hold the same number of characters.

`CONVERT TO CHARACTER SET binary` will convert [CHAR](../char.md), [VARCHAR](../varchar.md) and [TEXT](../text.md) columns to [BINARY](../binary.md), [VARBINARY](../varbinary.md) and [BLOB](../blob.md) respectively, and from that point will no longer have a character set, or be affected by future `CONVERT TO CHARACTER SET` statements.

To avoid data type changes resulting from `CONVERT TO CHARACTER SET`, use `MODIFY` on the individual columns instead. For example:

```
ALTER TABLE table_name MODIFY ascii_text_column TEXT CHARACTER SET utf8;
ALTER TABLE table_name MODIFY ascii_varchar_column VARCHAR(M) CHARACTER SET utf8;
```

## Column Level

Character sets and collations can also be specified for columns that are character types CHAR, TEXT or VARCHAR. The [CREATE TABLE](../../../sql-statements/data-definition/create/create-table.md) and [ALTER TABLE](../../../sql-statements/data-definition/alter/alter-table.md) statements support optional character set and collation clauses for this purpose - unlike those at the table level, the column level definitions are standard SQL.

```
CREATE TABLE european_names (
  croatian_names VARCHAR(40) COLLATE 'cp1250_croatian_ci',
  greek_names VARCHAR(40) CHARACTER SET 'greek');
```

If neither collation nor character set is provided, the table default is used. If only the character set is specified, that character set's default collation is used, while if only the collation is specified, the associated character set is used.

When using [ALTER TABLE](../../../sql-statements/data-definition/alter/alter-table.md) to change a column's character set, you need to ensure the character sets are compatible with your data. MariaDB will map the data as best it can, but it's possible to lose data if care is not taken.

The [SHOW CREATE TABLE](../../../sql-statements/administrative-sql-statements/show/show-create-table.md) statement or INFORMATION SCHEMA database can be used to determine column character sets and collations.

```
SHOW CREATE TABLE european_names\G
*************************** 1. row ***************************
       Table: european_names
Create Table: CREATE TABLE `european_names` (
  `croatian_names` varchar(40) CHARACTER SET cp1250 COLLATE cp1250_croatian_ci DEFAULT NULL,
  `greek_names` varchar(40) CHARACTER SET greek DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_danish_ci
```

```
SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME LIKE 'european%'\G
*************************** 1. row ***************************
           TABLE_CATALOG: def
            TABLE_SCHEMA: danish_names
              TABLE_NAME: european_names
             COLUMN_NAME: croatian_names
        ORDINAL_POSITION: 1
          COLUMN_DEFAULT: NULL
             IS_NULLABLE: YES
               DATA_TYPE: varchar
CHARACTER_MAXIMUM_LENGTH: 40
  CHARACTER_OCTET_LENGTH: 40
       NUMERIC_PRECISION: NULL
           NUMERIC_SCALE: NULL
      DATETIME_PRECISION: NULL
      CHARACTER_SET_NAME: cp1250
          COLLATION_NAME: cp1250_croatian_ci
             COLUMN_TYPE: varchar(40)
              COLUMN_KEY: 
                   EXTRA: 
              PRIVILEGES: select,insert,update,references
          COLUMN_COMMENT: 
*************************** 2. row ***************************
           TABLE_CATALOG: def
            TABLE_SCHEMA: danish_names
              TABLE_NAME: european_names
             COLUMN_NAME: greek_names
        ORDINAL_POSITION: 2
          COLUMN_DEFAULT: NULL
             IS_NULLABLE: YES
               DATA_TYPE: varchar
CHARACTER_MAXIMUM_LENGTH: 40
  CHARACTER_OCTET_LENGTH: 40
       NUMERIC_PRECISION: NULL
           NUMERIC_SCALE: NULL
      DATETIME_PRECISION: NULL
      CHARACTER_SET_NAME: greek
          COLLATION_NAME: greek_general_ci
             COLUMN_TYPE: varchar(40)
              COLUMN_KEY: 
                   EXTRA: 
              PRIVILEGES: select,insert,update,references
          COLUMN_COMMENT:
```

## Filenames

Since [MariaDB 5.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-1-series/changes-improvements-in-mariadb-5-1), the [character\_set\_filesystem](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#character_set_filesystem) system variable has controlled interpretation of file names that are given as literal strings. This affects the following statements and functions:

* [SELECT INTO DUMPFILE](../../../sql-statements/data-manipulation/selecting-data/select-into-dumpfile.md)
* SELECT INTO OUTFILE
* [LOAD DATA INFILE](../../../sql-statements/data-manipulation/inserting-loading-data/load-data-into-tables-or-index/load-data-infile.md)
* [LOAD XML](../../../sql-statements/data-manipulation/inserting-loading-data/load-data-into-tables-or-index/load-xml.md)
* [LOAD\_FILE()](../../../sql-functions/string-functions/load_file.md)

## Literals

By default, the character set and collation used for literals is determined by the [character\_set\_connection](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#character_set_connection) and [collation\_connection](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#collation_connection) system variables. However, they can also be specified explicitly:

```
[_charset_name]'string' [COLLATE collation_name]
```

The character set of string literals that do not have a character set introducer is determined by the [character\_set\_connection](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#character_set_connection) system variable.

This query:

```
SELECT CHARSET('a'), @@character_set_connection;
```

always returns the same character set name in both columns.

[character\_set\_client](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#character_set_client) and [character\_set\_connection](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#character_set_connection) are normally (e.g. during handshake, or after a SET NAMES query) are set to equal values. However, it's possible to set to different values.

### Examples

Examples when setting @@character\_set\_client and @@character\_set\_connection\
to different values can be useful:

Example 1:

Suppose, we have a utf8 database with this table:

```
CREATE TABLE t1 (a VARCHAR(10)) CHARACTER SET utf8 COLLATE utf8_general_ci;
INSERT INTO t1 VALUES ('oe'),('ö');
```

Now we connect to it using "mysql.exe", which uses the DOS character set\
(cp850 on a West European machine), and want to fetch all records that\
are equal to 'ö' according to the German phonebook rules.

It's possible with the following:

```
SET @@character_set_client=cp850, @@character_set_connection=utf8;
SELECT a FROM t1 WHERE a='ö' COLLATE utf8_german2_ci;
```

This will return:

```
+------+
| a    |
+------+
| oe   |
| ö    |
+------+
```

It works as follows:

1. The client sends the query using cp850.
2. The server, when parsing the query, creates a utf8 string literal by converting 'ö' from @@character\_set\_client (cp850) to @@character\_set\_connection (utf8)
3. The server applies the collation "utf8\_german2\_ci" to this string literal.
4. The server uses utf8\_german2\_ci for comparison.

Note, if we rewrite the script like this:

```
SET NAMES cp850;
SELECT a FROM t1 WHERE a='ö' COLLATE utf8_german2_ci;
```

we'll get an error:

```
ERROR 1253 (42000): COLLATION 'utf8_german2_ci' is not valid for CHARACTER SET 'cp850'
```

because:

* on step #2, the literal is not converted to utf8 any more and is created using cp850.
* on step #3, the server fails to apply utf8\_german2\_ci to an cp850 string literal.

Example 2:

Suppose we have a utf8 database and use "mysql.exe" from a West European machine again.

We can do this:

```
SET @@character_set_client=cp850, @@character_set_connection=utf8;
CREATE TABLE t2 AS SELECT 'ö';
```

It will create a table with a column of the type `VARCHAR(1) CHARACTER SET utf8`.

Note, if we rewrite the query like this:

```
SET NAMES cp850;
CREATE TABLE t2 AS SELECT 'ö';
```

It will create a table with a column of the type `VARCHAR(1) CHARACTER SET cp850`, which is probably not a good idea.

### N

Also, `N` or `n` can be used as prefix to convert a literal into the National Character set (which in MariaDB is always utf8).

For example:

```
SELECT _latin2 'Müller';
+-----------+
| MĂźller   |
+-----------+
| MĂźller   |
+-----------+
```

Prior to [MariaDB 10.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-6-series/what-is-mariadb-106):

```
SELECT CHARSET(N'a string');
+----------------------+
| CHARSET(N'a string') |
+----------------------+
| utf8                 |
+----------------------+
```

From [MariaDB 10.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-6-series/what-is-mariadb-106):

```
SELECT CHARSET(N'a string');
+----------------------+
| CHARSET(N'a string') |
+----------------------+
| utf8mb3              |
+----------------------+
```

```
SELECT 'Mueller' = 'Müller' COLLATE 'latin1_german2_ci';
+---------------------------------------------------+
| 'Mueller' = 'Müller' COLLATE 'latin1_german2_ci'  |
+---------------------------------------------------+
|                                                 1 |
+---------------------------------------------------+
```

## Stored Programs and Views

The literals which occur in stored programs and views, by default, use the character set and collation which was specified by the [character\_set\_connection](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#character_set_connection) and [collation\_connection](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#collation_connection) system variables when the stored program was created. These values can be seen using the SHOW CREATE statements. To change the character sets used for literals in an existing stored program, it is necessary to drop and recreate the stored program.

For stored routines parameters and return values, a character set and a collation can be specified via the CHARACTER SET and COLLATE clauses. Before 5.5, specifying a collation was not supported.

The following example shows that the character set and collation are determined at the time of creation:

```
SET @@local.character_set_connection='latin1';

DELIMITER ||
CREATE PROCEDURE `test`.`x`()
BEGIN
	SELECT CHARSET('x');
END;
||
Query OK, 0 rows affected (0.00 sec)

DELIMITER ;
SET @@local.character_set_connection='utf8';

CALL `test`.`x`();
+--------------+
| CHARSET('x') |
+--------------+
| latin1       |
+--------------+
```

The following example shows how to specify a function parameters character set and collation:

```
CREATE FUNCTION `test`.`y`(`str` TEXT CHARACTER SET utf8 COLLATE utf8_bin)
	RETURNS TEXT CHARACTER SET latin1 COLLATE latin1_bin
BEGIN
	SET @param_coll = COLLATION(`str`);
	RETURN `str`;
END;

-- return value's collation:
SELECT COLLATION(`test`.`y`('Hello, planet!'));
+-----------------------------------------+
| COLLATION(`test`.`y`('Hello, planet!')) |
+-----------------------------------------+
| latin1_bin                              |
+-----------------------------------------+

-- parameter's collation:
SELECT @param_coll;
+-------------+
| @param_coll |
+-------------+
| utf8_bin    |
+-------------+
```

## Changing Default Collation

**MariaDB starting with** [**11.2.1**](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-2-series/mariadb-11-2-1-release-notes)

From [MariaDB 11.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-2-series/what-is-mariadb-112), it is possible to change the default collation associated with a particular character set. The [character\_set\_collations](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#character_set_collations) system variable accepts a comma-delimited list of character sets and new default collations, for example:

```
SET @@character_set_collations = 'utf8mb4=uca1400_ai_ci, latin2=latin2_hungarian_ci';
```

The new variable will take effect in all cases where a character set is explicitly or implicitly specified without an explicit COLLATE clause, including but not limited to:

* Column collation
* Table collation
* Database collation
* CHAR(expr USING csname)
* CONVERT(expr USING csname)
* CAST(expr AS CHAR CHARACTER SET csname)
* '' - character string literal
* \_utf8mb3'text' - a character string literal with an introducer
* \_utf8mb3 X'61' - a character string literal with an introducer with hex notation
* \_utf8mb3 0x61 - a character string literal with an introducer with hex hybrid notation
* @@collation\_connection after a SET NAMES without COLLATE

## Example: Changing the Default Character Set To UTF-8

To change the default character set from latin1 (prior to [MariaDB 11.6.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-6-rolling-releases/mariadb-11-6-0-release-notes)) to UTF-8, the following settings should be specified in the my.cnf configuration file.

```
[mysql]
...
default-character-set=utf8mb4
...
[mysqld]
...
collation-server = utf8mb4_unicode_ci
init-connect='SET NAMES utf8mb4'
character-set-server = utf8mb4
...
```

Note that the `default-character-set` option is a client option, not a server option.

## See Also

* [String literals](../../../sql-structure/sql-language-structure/string-literals.md)
* [CAST()](../../../sql-functions/string-functions/cast.md)
* [CONVERT()](../../../sql-functions/string-functions/convert.md)
* [Operator Precedence](../../../sql-structure/operators/operator-precedence.md)

CC BY-SA / Gnu FDL
