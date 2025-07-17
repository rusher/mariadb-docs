# SQL\_MODE=ORACLE

{% include "https://app.gitbook.com/s/GxVnu02ec8KJuFSxmB93/~/reusable/Dn7q74OYovrrC5l3cYgb/" %}

From [MariaDB 10.3](../../old-releases/release-notes-mariadb-10-3-series/what-is-mariadb-103.md), MariaDB's SQL\_MODE = ORACLE setting enables compatibility with Oracle Database SQL syntax and behavior in MariaDB. This feature is particularly useful for organizations looking to migrate applications from Oracle Database to MariaDB while preserving the behavior and syntax of Oracle SQL. By setting the [sql\_mode](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/sql-mode) to `ORACLE`, developers can ensure that their existing SQL scripts, application logic, and database interactions are compatible with MariaDB's behavior, easing the migration process. This page provides detailed information on supported Oracle SQL syntax, behavior differences between Oracle and MariaDB, and tips for adapting applications and scripts to work smoothly under this mode.

```sql
SET SQL_MODE='ORACLE';
```

All traditional MariaDB SQL/PSM syntax should work as before, as long as it does not conflict with Oracle's PL/SQL syntax. All MariaDB functions should be supported in both normal and Oracle modes.

Prior to [MariaDB 10.3](../../old-releases/release-notes-mariadb-10-3-series/what-is-mariadb-103.md), MariaDB does not support Oracle's PL/SQL language, and `SET SQL_MODE=ORACLE` is only an alias for the following [sql\_mode](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/sql-mode) in those versions:

```sql
SET SQL_MODE='PIPES_AS_CONCAT, ANSI_QUOTES, IGNORE_SPACE, NO_KEY_OPTIONS,
NO_TABLE_OPTIONS, NO_FIELD_OPTIONS, NO_AUTO_CREATE_USER';
```

From [MariaDB 10.3](../../old-releases/release-notes-mariadb-10-3-series/what-is-mariadb-103.md), `SET SQL_MODE=ORACLE` is same as:

```sql
SET SQL_MODE='PIPES_AS_CONCAT,ANSI_QUOTES,IGNORE_SPACE,ORACLE,NO_KEY_OPTIONS,
NO_TABLE_OPTIONS,NO_FIELD_OPTIONS,NO_AUTO_CREATE_USER,SIMULTANEOUS_ASSIGNMENT';
```

## Supported Syntax in Oracle Mode

### Stored Procedures and Stored Functions

Oracle mode makes the following changes to [Stored Procedures](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/stored-routines/stored-procedures) and [Stored Functions](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/stored-routines/stored-functions):

| Oracle syntax                                                  | Description                                                                                                                                                                                                                                                                                    |
| -------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `CREATE PROCEDURE p1 (param OUT INT)`                          | ANSI uses `(OUT param INT)`                                                                                                                                                                                                                                                                    |
| `CREATE PROCEDURE p1 (a IN OUT INT)`                           | ANSI uses `(INOUT param INT)`                                                                                                                                                                                                                                                                  |
| `AS` before function body                                      | `CREATE FUNCTION f1 RETURN NUMBER AS BEGIN...`                                                                                                                                                                                                                                                 |
| `IS` before function body                                      | `CREATE FUNCTION f1 RETURN NUMBER IS BEGIN...`                                                                                                                                                                                                                                                 |
| If function has no parameters then parentheses must be omitted | Example: `CREATE PROCEDURE p1 AS BEGIN NULL; END;`                                                                                                                                                                                                                                             |
| `CREATE PROCEDURE p1 AS BEGIN END p1;`                         | Optional routine name after `END` keyword. [MDEV-12089](https://jira.mariadb.org/browse/MDEV-12089)                                                                                                                                                                                            |
| `CREATE FUNCTION f1(a VARCHAR)`                                | [VARCHAR](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/string-data-types/varchar) can be used without length for routine parameters and RETURN clause. The length is inherited from the argument at call time. [MDEV-10596](https://jira.mariadb.org/browse/MDEV-10596) |
| `CREATE AGGREGATE FUNCTION f1( )`                              | Creates an [aggregate function](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/stored-routines/stored-functions/stored-aggregate-functions), which performs the function against a set of rows and returns one aggregate result.                                                  |
| No `CALL` needed in Stored Procedures                          | In Oracle mode one can call other stored procedures with name only. [MDEV-12107](https://jira.mariadb.org/browse/MDEV-12107)                                                                                                                                                                   |
| `RETURN`. Can also be used in stored procedures                | ANSI uses `RETURNS`. MariaDB mode only supports `RETURNS` in stored functions                                                                                                                                                                                                                  |

### Cursors

Oracle mode makes the following changes to [Cursors](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/programmatic-compound-statements/programmatic-compound-statements-cursors):

| Oracle syntax                                                                          | Description                                                                                                                                                                                                   |
| -------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `CREATE PROCEDURE p1 AS CURSOR cur IS (SELECT a, b FROM t1); BEGIN FOR rec IN cur ...` | Explicit cursor with [FOR loop](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/programmatic-compound-statements/for). [MDEV-10581](https://jira.mariadb.org/browse/MDEV-10581)       |
| `CREATE PROCEDURE p1 AS rec IN (SELECT a, b FROM t1)`                                  | Implicit cursor with [FOR loop](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/programmatic-compound-statements/for). [MDEV-12098](https://jira.mariadb.org/browse/MDEV-12098)       |
| `CURSOR c(prm_a VARCHAR2, prm_b VARCHAR2) ... OPEN c(1,2)`                             | Cursor with parameters. [MDEV-10597](https://jira.mariadb.org/browse/MDEV-10597)                                                                                                                              |
| `CURSOR c(prm_a VARCHAR2, prm_b VARCHAR2) ... FOR rec in c(1,2)`                       | Cursor with parameters and [FOR loop](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/programmatic-compound-statements/for). [MDEV-12314](https://jira.mariadb.org/browse/MDEV-12314) |
| `s %ISOPEN, %ROWCOUNT, %FOUND, %NOTFOUND`                                              | Explicit cursor attributes. [MDEV-10582](https://jira.mariadb.org/browse/MDEV-10582)                                                                                                                          |

### LOOP

Oracle mode makes the following changes to [LOOP](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/programmatic-compound-statements/loop):

| Oracle syntax                                                                 | Description                                                                                                                                                                               |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `FOR i IN 1..10 LOOP ... END LOOP`                                            | Numeric [FOR loop](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/programmatic-compound-statements/for). [MDEV-10580](https://jira.mariadb.org/browse/MDEV-10580)            |
| `GOTO`                                                                        | [GOTO statement](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/programmatic-compound-statements/goto). [MDEV-10697](https://jira.mariadb.org/browse/MDEV-10697) |
| `<<label>>` used with GOTO                                                    | ANSI uses `label:`. [MDEV-10697](https://jira.mariadb.org/browse/MDEV-10697)                                                                                                              |
| To leave loop block: `EXIT [ label ] [ WHEN bool_expr ]`                      | ANSI syntax is `IF bool_expr THEN LEAVE label`                                                                                                                                            |
| `[<<label>>] WHILE boolean_expression LOOP statement... END LOOP [ label ] ;` | Oracle style `WHILE` loop                                                                                                                                                                 |
| `CONTINUE [ label ] [ WHEN boolean_expression]`                               | `CONTINUE` is only valid inside a loop                                                                                                                                                    |

### Variables

<table><thead><tr><th>Oracle syntax</th><th width="85.4444580078125">Version</th><th>Description</th></tr></thead><tbody><tr><td><code>var:= 10;</code> Can also be used with MariaDB systemvariables</td><td>10.3</td><td>MariaDB uses <code>SET var= 10;</code></td></tr><tr><td><code>var INT := 10</code></td><td>10.3</td><td>Default variable value</td></tr><tr><td><code>var1 table_name.column_name%TYPE</code></td><td>10.3</td><td>Take data type from a table column. <a href="https://jira.mariadb.org/browse/MDEV-10577">MDEV-10577</a></td></tr><tr><td><code>var2 var1%TYPE</code></td><td>10.3</td><td>Take data type from another variable</td></tr><tr><td><code>rec1 table_name%ROWTYPE</code></td><td>10.3</td><td>Take ROW structure from a table. <a href="https://jira.mariadb.org/browse/MDEV-12133">MDEV-12133</a></td></tr><tr><td><code>rec2 rec1%ROWTYPE</code></td><td>10.3</td><td>Take ROW structure from ROW variable</td></tr><tr><td><code>CURSOR c1 IS SELECT a,b FROM t1; rec1 c1%ROWTYPE;</code></td><td>10.3</td><td>Take ROW structure from a cursor. <a href="https://jira.mariadb.org/browse/MDEV-12011">MDEV-12011</a></td></tr><tr><td>Variables can be declared after cursor declarations</td><td>10.3</td><td>In MariaDB mode, variables must be declared before cursors. <a href="https://jira.mariadb.org/browse/MDEV-10598">MDEV-10598</a></td></tr><tr><td>Triggers uses <code>:NEW</code> and <code>:OLD</code></td><td>10.3</td><td>ANSI uses NEW and OLD. <a href="https://jira.mariadb.org/browse/MDEV-10579">MDEV-10579</a></td></tr><tr><td><code>SQLCODE</code></td><td>10.3</td><td>Returns the number code of the most recent exception. Can only be used in Stored Procedures. <a href="https://jira.mariadb.org/browse/MDEV-10578">MDEV-10578</a></td></tr><tr><td><code>SQLERRM</code></td><td>10.3</td><td>Returns the error message associdated to it's error number argument or <code>SQLCODE</code> if no argument is given. Can only be used in Stored Procedures. <a href="https://jira.mariadb.org/browse/MDEV-10578">MDEV-10578</a></td></tr><tr><td><code>SQL%ROWCOUNT</code></td><td>10.3</td><td>Almost same as <a href="https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/secondary-functions/information-functions/row_count">ROW_COUNT()</a>. <a href="https://jira.mariadb.org/browse/MDEV-10583">MDEV-10583</a></td></tr><tr><td><a href="https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/secondary-functions/information-functions/rownum">ROWNUM</a></td><td>10.6.1</td><td>Returns number of accepted rows</td></tr></tbody></table>

### Exceptions

| Oracle syntax                                                         | Description                                                                                                     |
| --------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| `BEGIN ... EXCEPTION WHEN OTHERS THEN BEGIN .. END; END;`             | Exception handlers are declared at the end of a block                                                           |
| `TOO_MANY_ROWS, NO_DATA_FOUND, DUP_VAL_ON_INDEX`                      | Predefined exceptions. [MDEV-10839](https://jira.mariadb.org/browse/MDEV-10839)                                 |
| `RAISE TOO_MANY_ROWS ; .... EXCEPTION WHEN TOO_MANY_ROWS THEN ...`    | Exception can be used with RAISE and EXCEPTION...WHEN. [MDEV-10840](https://jira.mariadb.org/browse/MDEV-10840) |
| `CREATE OR REPLACE FUNCTION f1 (a INT) RETURN INT AS e1 EXCEPTION...` | User defined exceptions. [MDEV-10587](https://jira.mariadb.org/browse/MDEV-10587)                               |

### BEGIN Blocks

| Oracle syntax                                                   | Description                                                                                                                                                                                                                         |
| --------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `BEGIN` to start a block                                        | MariaDB uses [BEGIN NOT ATOMIC](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/programmatic-compound-statements/begin-end) for anyonymous blocks. [MDEV-10655](https://jira.mariadb.org/browse/MDEV-10655) |
| `DECLARE` is used before `BEGIN`                                | `DECLARE a INT; b VARCHAR(10); BEGIN v:= 10; END;`                                                                                                                                                                                  |
| `WHEN DUP_VAL_ON_INDEX THEN NULL ; NULL; WHEN OTHERS THEN NULL` | Do not require `BEGIN..END` in multi-statement exception handlers in `THEN` clause. [MDEV-12088](https://jira.mariadb.org/browse/MDEV-12088)                                                                                        |

### Simple Syntax Compatibility

<table><thead><tr><th>Oracle syntax</th><th width="72.407470703125">Version</th><th>Description</th></tr></thead><tbody><tr><td><code>ELSIF</code></td><td>10.3</td><td>ANSI uses <a href="https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/programmatic-compound-statements/if">ELSEIF</a></td></tr><tr><td><code>SELECT UNIQUE</code></td><td>10.3</td><td>Same as <a href="https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/select#distinct">SELECT DISTINCT</a>. <a href="https://jira.mariadb.org/browse/MDEV-12086">MDEV-12086</a></td></tr><tr><td><code>TRUNCATE TABLE t1 [DROP STORAGE] or [REUSE STORAGE]</code></td><td>10.3</td><td><code>DROP STORAGE</code> and <code>REUSE STORAGE</code> are allowed as optional keywords for <a href="https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/table-statements/truncate-table">TRUNCATE TABLE</a>. <a href="https://jira.mariadb.org/browse/MDEV-10588">MDEV-10588</a></td></tr><tr><td><a href="https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/joins-subqueries/subqueries/subqueries-in-a-from-clause-derived-tables">Subqueries in a FROM clause</a> without an alias</td><td>10.6</td><td><code>SELECT * FROM (SELECT 1 FROM DUAL), (SELECT 2 FROM DUAL)</code></td></tr><tr><td><a href="https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/joins-subqueries/union">UNION</a>, <a href="https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/joins-subqueries/except">EXCEPT</a> and <a href="https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/joins-subqueries/intersect">INTERSECT</a> all have the same precedence.</td><td>10.3</td><td><a href="https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/joins-subqueries/intersect">INTERSECT</a> has higher precedence than <a href="https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/joins-subqueries/union">UNION</a> and <a href="https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/joins-subqueries/except">EXCEPT</a> in non-Oracle modes.</td></tr><tr><td><code>MINUS</code></td><td>10.6</td><td>MINUS is a synonym for <a href="https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/joins-subqueries/except">EXCEPT</a>.</td></tr></tbody></table>

### Functions

<table><thead><tr><th width="286.5926513671875">Oracle syntax</th><th width="84.25927734375">Version</th><th>Description</th></tr></thead><tbody><tr><td><a href="https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/date-time-functions/add_months">ADD_MONTHS()</a></td><td>10.6.1</td><td>Added as a wrapper for <a href="https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/date-time-functions/date_add">DATE_ADD()</a> to enhance Oracle compatibility. All modes.</td></tr><tr><td><a href="https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/string-functions/cast">CAST(expr as VARCHAR(N))</a></td><td>10.3</td><td>Cast expression to a VARCHAR(N). <a href="https://jira.mariadb.org/browse/MDEV-11275">MDEV-11275</a></td></tr><tr><td><a href="https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/secondary-functions/encryption-hashing-and-compression-functions/decode">DECODE</a></td><td>10.3</td><td>In Oracle mode, compares and matches search expressions</td></tr><tr><td><code>LENGTH()</code> is same as <a href="https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/string-functions/char_length">CHAR_LENGTH()</a></td><td>10.3</td><td>MariaDB translates <a href="https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/string-functions/length">LENGTH()</a> to <a href="https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/string-functions/octet_length">OCTET_LENGTH()</a>. In all modes one can use LENGTHB() as a synonym to OCTET_LENGTH()</td></tr><tr><td><a href="https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/string-functions/chr">CHR(num)</a></td><td>10.3</td><td>Returns a <code>VARCHAR(1)</code> with character set and collation according to <code>@@character_set_database</code> and <code>@@collation_database</code></td></tr><tr><td><code>substr('abc',0 ,3) same as substr('abc', 1 ,3)</code></td><td>10.3</td><td>Position <code>0</code> for <a href="https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/string-functions/substring">substr()</a> is same as position <code>1</code></td></tr><tr><td><a href="https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/secondary-functions/miscellaneous-functions/sys_guid">SYS_GUID</a></td><td>10.6.1</td><td>Generates a globally unique identifier. Similar to <a href="https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/secondary-functions/miscellaneous-functions/uuid">UUID</a> but without the -. All modes.</td></tr><tr><td><a href="https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/string-functions/to_char">TO_CHAR</a></td><td>10.6.1</td><td>Added to enhance Oracle compatibility. All modes.</td></tr><tr><td><a href="https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/string-functions/trim">TRIM</a>, <a href="https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/string-functions/ltrim">LTRIM</a>, <a href="https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/string-functions/rtrim">RTRIM</a>, <a href="https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/string-functions/lpad">LPAD</a> and <a href="https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/string-functions/rpad">RPAD</a></td><td>10.3</td><td>Returns <code>NULL</code> instead of an empty string if returning an empty result. These functions can also be accessed outside of <code>ORACLE</code> mode by suffixing <code>_ORACLE</code> onto the end of the function name, such as <code>TRIM_ORACLE</code>.</td></tr></tbody></table>

### Prepared Statements

Oracle mode makes the following changes to [Prepared Statements](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/prepared-statements):

| Oracle syntax                                                             | Description                                                                    |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| `PREPARE stmt FROM 'SELECT :1, :2'`                                       | ANSI uses `?`. [MDEV-10801](https://jira.mariadb.org/browse/MDEV-10801)        |
| `EXECUTE IMMEDIATE 'INSERT INTO t1 SELECT (:x,:y) FROM DUAL' USING 10,20` | Dynamic placeholders. [MDEV-10801](https://jira.mariadb.org/browse/MDEV-10801) |

### Synonyms for Basic SQL Types

| Oracle type                | MariaDB synonym                                                                                                           |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| `VARCHAR2`                 | [VARCHAR](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/string-data-types/varchar)                  |
| `NUMBER(M[,D])`            | [DECIMAL(M\[,D\])](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/numeric-data-types/decimal)        |
| `NUMBER`                   | [DOUBLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/numeric-data-types/double)                   |
| `DATE` (with time portion) | MariaDB [DATETIME](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/date-and-time-data-types/datetime) |
| `RAW`                      | [VARBINARY](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/string-data-types/varbinary)              |
| `CLOB`                     | [LONGTEXT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/string-data-types/longtext)                |
| `BLOB`                     | [LONGBLOB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/string-data-types/longblob)                |

This was implemented as part of [MDEV-10343](https://jira.mariadb.org/browse/MDEV-10343).

If one does a [SHOW CREATE TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-create-table) in `ORACLE` mode on a table that has a native MariaDB `DATE` column, it will be displayed as [mariadb\_schema.date](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/system-tables/mariadb_schema) to not conflict with the Oracle `DATE` type.

### Packages

The following syntax has been supported since [MariaDB 10.3.5](../../old-releases/release-notes-mariadb-10-3-series/mariadb-1035-release-notes.md):

* [CREATE PACKAGE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/create/create-package)
* [CREATE PACKAGE BODY](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/create/create-package-body)
* [DROP PACKAGE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/drop/drop-package)
* [DROP PACKAGE BODY](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/drop/drop-package-body)
* [SHOW CREATE PACKAGE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-create-package)
* [SHOW CREATE PACKAGE BODY](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-create-package-body)

### NULL Handling

Oracle mode makes the following changes to [NULL handling](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/null-values):

#### NULL As a Statement

`NULL` can be used as a statement:

```sql
IF a=10 THEN NULL; ELSE NULL; END IF
```

#### Translating Empty String Literals to NULL

In Oracle, empty string ('') and NULL are the same thing,

By using `sql_mode=EMPTY_STRING_IS_NULL` you can get a similar\
experience in MariaDB:

```sql
SET sql_mode=EMPTY_STRING_IS_NULL;
SELECT '' IS NULL; -- returns TRUE
INSERT INTO t1 VALUES (''); -- inserts NULL
```

#### Concat Operator Ignores NULL

[CONCAT()](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/string-functions/concat) and [||](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/operators/logical-operators/or) ignore NULL in Oracle mode. Can also be accessed outside of ORACLE mode by using CONCAT\_OPERATOR\_ORACLE. [MDEV-11880](https://jira.mariadb.org/browse/MDEV-11880) and [MDEV-12143](https://jira.mariadb.org/browse/MDEV-12143).

### Reserved Words

There are a number of [extra reserved words](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/sql-language-structure/reserved-words#oracle-mode) in Oracle mode.

### SHOW CREATE TABLE

The [SHOW CREATE TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-create-table) statement will not display MariaDB-specific table options, such as AUTO\_INCREMENT or CHARSET, when Oracle mode is set.

&#x20;

## See Also

* [mariadb\_schema](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/system-tables/mariadb_schema)
* [Using SEQUENCEs](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/sequences)
* [SQL\_MODE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/sql-mode) EMPTY\_STRING\_IS\_NULL
* [SQL\_MODE=MSSQL](sql_modemssql.md)
* [Migration from Oracle to MariaDB with no application change - Pickup Li - FOSDEM 2021](https://www.youtube.com/watch?v=kQXpjCSt1So) (video)
* [A user story: migrating from Oracle to MariaDB - Lixun Peng - MariaDB Server Fest 2020](https://www.youtube.com/watch?v=5pqEZ91zHsA) (video)
* [Curious case of the disappearing commercial databases (13 minute offset) - Monty Widenius - MariaDB Server Fest 2021](https://www.youtube.com/watch?v=0nysJV3pozg) (video)
* [Sqlines - Oracle to MariaDB migration tool](https://sqlines.com/oracle-to-mariadb)

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
