
# VARCHAR


## Syntax


```
[NATIONAL] VARCHAR(M) [CHARACTER SET charset_name] [COLLATE collation_name]
```

## Description


A variable-length string. M represents the maximum column length in
characters. The range of M is 0 to 65,532. The effective maximum
length of a VARCHAR is subject to the maximum row size and the character set used. For
example, utf8 characters can require up to three bytes per character,
so a VARCHAR column that uses the utf8 character set can be declared
to be a maximum of 21,844 characters.



#### Note:

For the [ColumnStore](../../../../columnstore/columnstore-data-ingestion/columnstore-remote-bulk-data-import-mcsimport.md) engine, M represents the maximum column length in
bytes.


MariaDB stores VARCHAR values as a one-byte or two-byte length prefix
plus data. The length prefix indicates the number of bytes in the
value. A VARCHAR column uses one length byte if values require no more
than 255 bytes, two length bytes if values may require more than 255
bytes.


MariaDB follows the standard SQL specification, and does not remove trailing spaces from VARCHAR values.


VARCHAR(0) columns can contain 2 values: an empty string or NULL. Such columns cannot be part of an index. The [CONNECT](../../../../connectors/mariadb-connector-nodejs/connector-nodejs-pipelining.md) storage engine does not support VARCHAR(0).


VARCHAR is shorthand for CHARACTER VARYING. NATIONAL VARCHAR is the
standard SQL way to define that a VARCHAR column should use some
predefined character set. MariaDB uses utf8 as this
predefined character set, as does MySQL 4.1 and up.
NVARCHAR is shorthand for NATIONAL VARCHAR.


For MariaDB, a number of [NO PAD collations](character-sets/supported-character-sets-and-collations.md#no-pad-collations) are available.


If a unique index consists of a column where trailing pad characters are stripped or ignored, inserts into that column where values differ only by the number of trailing pad characters will result in a duplicate-key error.


### SYNONYMS


The following are synonyms for VARCHAR:


* CHAR VARYING
* CHARACTER VARYING
* VARCHAR2
* VARCHARACTER


## Examples


The following are equivalent:


```
VARCHAR(30) CHARACTER SET utf8
NATIONAL VARCHAR(30)
NVARCHAR(30)
NCHAR VARCHAR(30)
NATIONAL CHARACTER VARYING(30)
NATIONAL CHAR VARYING(30)
```

### Trailing spaces


```
CREATE TABLE strtest (v VARCHAR(10));
INSERT INTO strtest VALUES('Maria   ');

SELECT v='Maria',v='Maria   ' FROM strtest;
+-----------+--------------+
| v='Maria' | v='Maria   ' |
+-----------+--------------+
|         1 |            1 |
+-----------+--------------+

SELECT v LIKE 'Maria',v LIKE 'Maria   ' FROM strtest;
+----------------+-------------------+
| v LIKE 'Maria' | v LIKE 'Maria   ' |
+----------------+-------------------+
|              0 |                 1 |
+----------------+-------------------+
```

### VARCHAR


For our example of VARCHAR we picked a maximum size that avoids overflowing the maximum row size (65535). Keep in mind that a multi-byte character set would need more space in the row than a single-byte character set. We also avoid the auto-conversion of a VARCHAR into a TEXT, MEDIUMTEXT, or LONGTEXT that can happen when STRICT_TRANS_TABLES is not set in the SQL_MODE.


The example:


```
CREATE TABLE varchar_example (
   description VARCHAR(20),
   example VARCHAR(65511)
) DEFAULT CHARSET=latin1; -- One byte per char makes the examples clearer
```

```
INSERT INTO varchar_example VALUES
   ('Normal foo', 'foo'),
   ('Trailing spaces foo', 'foo      '),
   ('NULLed', NULL),
   ('Empty', ''),
   ('Maximum', RPAD('', 65511, 'x'));
```

```
SELECT description, LENGTH(example) AS length
   FROM varchar_example;
```

```
+---------------------+--------+
| description         | length |
+---------------------+--------+
| Normal foo          |      3 |
| Trailing spaces foo |      9 |
| NULLed              |   NULL |
| Empty               |      0 |
| Maximum             |  65511 |
+---------------------+--------+
```

### Data Too Long


When SQL_MODE is strict (the default) a value is considered "too long" when its length exceeds the size of the data type, and an error is generated.


Example of data too long behavior for VARCHAR:


```
TRUNCATE varchar_example;

INSERT INTO varchar_example VALUES
   ('Overflow', RPAD('', 65512, 'x'));
```

```
ERROR 1406 (22001): Data too long for column 'example' at row 1
```

## Truncation


* Depending on whether or not [strict sql mode](../../../server-management/variables-and-modes/sql-mode.md#strict-mode) is set, you will either get a warning or an error if you try to insert a string that is too long into a VARCHAR column. If the extra characters are spaces, the spaces that can't fit will be removed and you will always get a warning, regardless of the [sql mode](../../../../release-notes/mariadb-community-server/compatibility-and-differences/sql_modemssql.md) setting.


## Difference Between VARCHAR and [TEXT](text.md)


* VARCHAR columns can be fully indexed. [TEXT](text.md) columns can only be indexed over a specified length.
* Using [TEXT](text.md) or [BLOB](blob.md) in a [SELECT](../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/benchmarks-and-long-running-tests/benchmark-results/select-random-ranges-and-select-random-point.md) query that uses temporary tables for storing intermediate results will force the temporary table to be disk based (using the [Aria storage engine](../../storage-engines/aria/aria-storage-engine.md) instead of the [memory storage engine](../../storage-engines/memory-storage-engine.md), which is a bit slower. This is not that bad as the [Aria storage engine](../../storage-engines/aria/aria-storage-engine.md) caches the rows in memory. To get the benefit of this, one should ensure that the [aria_pagecache_buffer_size](../../storage-engines/aria/aria-system-variables.md#aria_pagecache_buffer_size) variable is big enough to hold most of the row and index data for temporary tables.


## Oracle Mode


In [Oracle mode](../../../../release-notes/mariadb-community-server/compatibility-and-differences/sql_modeoracle.md), `VARCHAR2` is a synonym.


### For Storage Engine Developers


* Internally the full length of the VARCHAR column is allocated inside each TABLE objects record[] structure. As there are three such buffers, each open table will allocate 3 times max-length-to-store-varchar bytes of memory.
* [TEXT](text.md) and [BLOB](blob.md) columns are stored with a pointer (4 or 8 bytes) + a 1-4 bytes length. The [TEXT](text.md) data is only stored once. This means that internally `TEXT` uses less memory for each open table but instead has the additional overhead that each `TEXT` object needs to be allocated and freed for each row access (with some caching in between).


## See Also


* [VARBINARY](varbinary.md)
* [TEXT](text.md)
* [CHAR](../../sql-statements-and-structure/sql-statements/built-in-functions/secondary-functions/information-functions/charset.md)
* [Character Sets and Collations](character-sets/README.md)
* [Data Type Storage Requirements](../data-type-storage-requirements.md)
* [Oracle mode from MariaDB 10.3](../../../../release-notes/mariadb-community-server/compatibility-and-differences/sql_modeoracle.md)

