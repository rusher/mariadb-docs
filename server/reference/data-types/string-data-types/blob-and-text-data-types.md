# BLOB and TEXT Data Types

## Description

A `BLOB` is a binary large object that can hold a variable amount of\
data. The four `BLOB` types are

* [TINYBLOB](tinyblob.md),
* [BLOB](blob.md),
* [MEDIUMBLOB](mediumblob.md), and
* [LONGBLOB](longblob.md).

These differ only in the maximum length of the values they can hold.

The `TEXT` types are

* [TINYTEXT](tinytext.md),
* [TEXT](text.md),
* [MEDIUMTEXT](mediumtext.md), and
* [LONGTEXT](longtext.md).
* [JSON](json.md) (alias for LONGTEXT)

These correspond to the four `BLOB` types and have the same\
maximum lengths and [storage requirements](../data-type-storage-requirements.md).

`BLOB` and `TEXT` columns can have a `DEFAULT` value.

#### Note

It is possible to set a unique index on columns that use the BLOB or TEXT data types.

## See Also

* [Store a column as compressed](../../sql-statements/data-definition/create/create-table.md#compressed)

GPLv2 fill\_help\_tables.sql
