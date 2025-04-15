# BLOB

#

# Syntax

```
BLOB[(M)]
```

#

# Description

A `BLOB` column with a maximum length of `65,535` (`216 - 1`) bytes. Each
`BLOB` value is stored using a two-byte length prefix that indicates the
number of bytes in the value.

An optional length `M` can be given for this type. If this is done,
MariaDB creates the column as the smallest `BLOB` type large enough to
hold values *`M`* bytes long.

BLOBS can also be used to store [dynamic columns](../../sql-statements-and-structure/nosql/dynamic-columns-api.md).

`BLOB` and `TEXT` columns can both be assigned a [DEFAULT](../../sql-statements-and-structure/sql-statements/data-definition/create/create-tablespace.md#default) value.

#

## Indexing

On a column that uses the `BLOB` data type, setting a unique index is now possible.

#

### Note

In previous releases, setting a unique index on a column that uses the `BLOB` data type was not possible. Index would only guarantee the uniqueness of a fixed number of characters.

#

## Oracle Mode

In [Oracle mode](/kb/en/sql_modeoracle-from-mariadb-103/#synonyms-for-basic-sql-types), `BLOB` is a synonym for `LONGBLOB`.

#

# See Also

* [BLOB and TEXT Data Types](blob-and-text-data-types.md)
* [Data Type Storage Requirements](../data-type-storage-requirements.md)
* [Oracle mode from MariaDB 10.3](/kb/en/sql_modeoracle-from-mariadb-103/#synonyms-for-basic-sql-types)