# BLOB and TEXT Data Types

#

# Description

A `BLOB` is a binary large object that can hold a variable amount of
data. The four `BLOB` types are

* [TINYBLOB](/kb/en/sql_language-data_types-tinyblob/),
* [BLOB](/kb/en/sql_language-data_types-blob/),
* [MEDIUMBLOB](/kb/en/sql_language-data_types-mediumblob/), and
* [LONGBLOB](/kb/en/sql_language-data_types-longblob/).

These differ only in the maximum length of the values they can hold.

The `TEXT` types are

* [TINYTEXT](/kb/en/sql_language-data_types-tinytext/),
* [TEXT](/kb/en/sql_language-data_types-text/),
* [MEDIUMTEXT](/kb/en/sql_language-data_types-mediumtext/), and
* [LONGTEXT](/kb/en/sql_language-data_types-longtext/).
* [JSON](json-data-type.md) (alias for LONGTEXT)

These correspond to the four `BLOB` types and have the same
maximum lengths and [storage requirements](../data-type-storage-requirements.md).

`BLOB` and `TEXT` columns can have a `DEFAULT` value.

#

### Note

It is possible to set a unique index on columns that use the BLOB or TEXT data types.

#

# See Also

* [Store a column as compressed](../../sql-statements-and-structure/sql-statements/data-definition/create/create-tablespace.md#compressed)