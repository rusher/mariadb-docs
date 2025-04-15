
# TEXT

## Syntax


```
TEXT[(M)] [CHARACTER SET charset_name] [COLLATE collation_name]
```


## Description


A `<code>TEXT</code>` column with a maximum length of `<code>65,535</code>` (`<code>2<sup>16</sup> - 1</code>`)
characters. The effective maximum length is less if the value contains
multi-byte characters. Each `<code>TEXT</code>` value is stored using a two-byte length
prefix that indicates the number of bytes in the value. If you need a bigger storage, consider using [MEDIUMTEXT](mediumtext.md) instead.


An optional length `<code>M</code>` can be given for this type. If this is done, MariaDB
creates the column as the smallest `<code>TEXT</code>` type large enough to hold values
`<code>M</code>` characters long.


`<code>BLOB</code>` and `<code>TEXT</code>` columns can be assigned a [DEFAULT](../../sql-statements-and-structure/vectors/create-table-with-vectors.md#default) value.


## Examples


### Trailing spaces:


```
CREATE TABLE strtest (d TEXT(10));
INSERT INTO strtest VALUES('Maria   ');

SELECT d='Maria',d='Maria   ' FROM strtest;
+-----------+--------------+
| d='Maria' | d='Maria   ' |
+-----------+--------------+
|         1 |            1 |
+-----------+--------------+

SELECT d LIKE 'Maria',d LIKE 'Maria   ' FROM strtest;
+----------------+-------------------+
| d LIKE 'Maria' | d LIKE 'Maria   ' |
+----------------+-------------------+
|              0 |                 1 |
+----------------+-------------------+
```

### Example of TEXT:


```
CREATE TABLE text_example (
   description VARCHAR(20),
   example TEXT
) DEFAULT CHARSET=latin1; -- One byte per char makes the examples clearer
```

```
INSERT INTO text_example VALUES
   ('Normal foo', 'foo'),
   ('Trailing spaces foo', 'foo      '),
   ('NULLed', NULL),
   ('Empty', ''),
   ('Maximum', RPAD('', 65535, 'x'));
```

```
SELECT description, LENGTH(example) AS length
   FROM text_example;
```

```
+---------------------+--------+
| description         | length |
+---------------------+--------+
| Normal foo          |      3 |
| Trailing spaces foo |      9 |
| NULLed              |   NULL |
| Empty               |      0 |
| Maximum             |  65535 |
+---------------------+--------+
```

### Data Too Long


When SQL_MODE is strict (the default) a value is considered "too long" when its length exceeds the size of the data type, and an error is generated.


Example of data too long behavior for TEXT:


```
TRUNCATE text_example;

INSERT INTO text_example VALUES
   ('Overflow', RPAD('', 65536, 'x'));
```

```
ERROR 1406 (22001): Data too long for column 'example' at row 1
```

## Indexing


A [unique index](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/optimization-and-indexes/getting-started-with-indexes.md#unique-index) can be created on a `<code>TEXT</code>` column. This was not possible prior to [MariaDB 10.4](../../../../release-notes/mariadb-community-server/what-is-mariadb-104.md)


Internally, this uses hash indexing to quickly check the values and if a hash collision is found, the actual stored values are compared in order to retain the uniqueness.


## Difference between [VARCHAR](varchar.md) and TEXT


* [VARCHAR](varchar.md) columns can be fully indexed. `<code>TEXT</code>` columns can only be indexed over a specified length.
* Using TEXT or [BLOB](blob.md) in a [SELECT](../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/benchmarks-and-long-running-tests/benchmark-results/select-random-ranges-and-select-random-point.md) query that uses temporary tables for storing intermediate results will force the temporary table to be disk based (using the [Aria storage engine](../../storage-engines/aria/aria-storage-engine.md) instead of the [memory storage engine](../../storage-engines/memory-storage-engine.md), which is a bit slower. This is not that bad as the [Aria storage engine](../../storage-engines/aria/aria-storage-engine.md) caches the rows in memory. To get the benefit of this, one should ensure that the [aria_pagecache_buffer_size](../../storage-engines/aria/aria-system-variables.md#aria_pagecache_buffer_size) variable is big enough to hold most of the row and index data for temporary tables.


### For Storage Engine Developers


* Internally the full length of the [VARCHAR](varchar.md) column is allocated inside each TABLE objects record[] structure. As there are three such buffers, each open table will allocate 3 times max-length-to-store-varchar bytes of memory.
* `<code>TEXT</code>` and `<code>BLOB</code>` columns are stored with a pointer (4 or 8 bytes) + a 1-4 bytes length. The `<code>TEXT</code>` data is only stored once. This means that internally `<code>TEXT</code>` uses less memory for each open table but instead has the additional overhead that each `<code>TEXT</code>` object needs to be allocated and freed for each row access (with some caching in between).


## See Also


* [BLOB and TEXT Data Types](blob-and-text-data-types.md)
* [MEDIUMTEXT](mediumtext.md)
* [Data Type Storage Requirements](../data-type-storage-requirements.md)

