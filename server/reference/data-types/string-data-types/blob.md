
# BLOB

## Syntax


```
BLOB[(M)]
```


## Description


A `<code>BLOB</code>` column with a maximum length of `<code>65,535</code>` (`<code>2<sup>16</sup> - 1</code>`) bytes. Each
`<code>BLOB</code>` value is stored using a two-byte length prefix that indicates the
number of bytes in the value.


An optional length `<code>M</code>` can be given for this type. If this is done,
MariaDB creates the column as the smallest `<code>BLOB</code>` type large enough to
hold values *`<code>M</code>`* bytes long.


BLOBS can also be used to store [dynamic columns](../../sql-statements-and-structure/nosql/dynamic-columns-api.md).


`<code>BLOB</code>` and `<code>TEXT</code>` columns can both be assigned a [DEFAULT](../../sql-statements-and-structure/vectors/create-table-with-vectors.md#default) value.


### Indexing


On a column that uses the `<code>BLOB</code>` data type, setting a unique index is now possible.



#### Note

In previous releases, setting a unique index on a column that uses the `<code>BLOB</code>` data type was not possible. Index would only guarantee the uniqueness of a fixed number of characters.


### Oracle Mode


In [Oracle mode](../../../../release-notes/mariadb-community-server/compatibility-and-differences/sql_modeoracle.md), `<code>BLOB</code>` is a synonym for `<code>LONGBLOB</code>`.


## EXAMPLES


### BLOB


Example of BLOB:


```
CREATE TABLE blob_example (
   description VARCHAR(20),
   example BLOB
) DEFAULT CHARSET=latin1; -- One byte per char makes the examples clearer
```

```
INSERT INTO blob_example VALUES
   ('Normal foo', 'foo'),
   ('Trailing spaces foo', 'foo      '),
   ('NULLed', NULL),
   ('Empty', ''),
   ('Maximum', RPAD('', 65535, CHAR(7)));
```

```
SELECT description, LENGTH(example) AS length
   FROM blob_example;

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

## Data Too Long


When SQL_MODE is strict (the default) a value is considered "too long" when its length exceeds the size of the data type, and an error is generated.


Example of data too long behavior for BLOB:


```
TRUNCATE blob_example;

INSERT INTO blob_example VALUES
   ('Overflow', RPAD('', 65536, CHAR(7)));

ERROR 1406 (22001): Data too long for column 'example' at row 1
```

## See Also


* [BLOB and TEXT Data Types](blob-and-text-data-types.md)
* [Data Type Storage Requirements](../data-type-storage-requirements.md)
* [Oracle mode from MariaDB 10.3](../../../../release-notes/mariadb-community-server/compatibility-and-differences/sql_modeoracle.md)

