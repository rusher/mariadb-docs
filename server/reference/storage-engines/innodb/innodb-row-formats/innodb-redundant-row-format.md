# InnoDB REDUNDANT Row Format

The `REDUNDANT` row format is the original non-compacted row format.

The `REDUNDANT` row format was the only available row format before MySQL 5.0.3. In that release, this row format was retroactively named the `REDUNDANT` row format. In the same release, the `COMPACT` row format was introduced as the new default row format.

#

# Using the `REDUNDANT` Row Format

The easiest way to create an InnoDB table that uses the `REDUNDANT` row format is by setting the [ROW_FORMAT](../../../sql-statements-and-structure/sql-statements/data-definition/create/create-tablespace.md#row_format) table option to `REDUNDANT` in a [CREATE TABLE](../../../sql-statements-and-structure/sql-statements/data-definition/create/create-tablespace.md) or [ALTER TABLE](../../../sql-statements-and-structure/sql-statements/data-definition/alter/alter-table.md) statement.

It is recommended to set the [innodb_strict_mode](../innodb-system-variables.md#innodb_strict_mode) system variable to `ON` when using this format.

The `REDUNDANT` row format is supported by both the `Antelope` and the `Barracuda` [file formats](../innodb-file-format.md), so tables with this row format can be created regardless of the value of the [innodb_file_format](../innodb-system-variables.md#innodb_file_format) system variable.

For example:

```
SET SESSION innodb_strict_mode=ON;

CREATE TABLE tab (
 id int,
 str varchar(50)
) ENGINE=InnoDB ROW_FORMAT=REDUNDANT;
```

#

# Index Prefixes with the `REDUNDANT` Row Format

The `REDUNDANT` row format supports index prefixes up to 767 bytes.

#

# Overflow Pages with the `REDUNDANT` Row Format

All InnoDB row formats can store certain kinds of data in overflow pages. This allows for the maximum row size of an InnoDB table to be larger than the maximum amount of data that can be stored in the row's main data page. See [Maximum Row Size](innodb-row-formats-overview.md#maximum-row-size) for more information about the other factors that can contribute to the maximum row size for InnoDB tables.

In the `REDUNDANT` row format variable-length columns, such as columns using the [VARBINARY](../../../data-types/string-data-types/varbinary.md), [VARCHAR](../../../data-types/string-data-types/varchar.md), [BLOB](../../../data-types/string-data-types/blob.md) and [TEXT](../../../data-types/string-data-types/text.md) data types, can be partially stored in overflow pages.

InnoDB only considers using overflow pages if the table's row size is greater than half of [innodb_page_size](../innodb-system-variables.md#innodb_page_size). If the row size is greater than this, then InnoDB chooses variable-length columns to be stored on overflow pages until the row size is less than half of [innodb_page_size](../innodb-system-variables.md#innodb_page_size).

For [VARBINARY](../../../data-types/string-data-types/varbinary.md), [VARCHAR](../../../data-types/string-data-types/varchar.md), [BLOB](../../../data-types/string-data-types/blob.md) and [TEXT](../../../data-types/string-data-types/text.md) columns, only values longer than 767 bytes are considered for for storage on overflow pages. Bytes that are stored to track a value's length do not count towards this limit. This limit is only based on the length of the actual column's data.

Fixed-length columns greater than 767 bytes are encoded as variable-length columns, so they can also be stored in overflow pages if the table's row size is greater than half of [innodb_page_size](../innodb-system-variables.md#innodb_page_size). Even though a column using the [CHAR](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/query-optimizations/charset-narrowing-optimization.md) data type can hold at most 255 characters, a [CHAR](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/query-optimizations/charset-narrowing-optimization.md) column can still exceed 767 bytes in some cases. For example, a `char(255)` column can exceed 767 bytes if the [character set](/en/character-sets/) is `utf8mb4`.

If a column is chosen to be stored on overflow pages, then the first 767 bytes of the column's value and a 20-byte pointer to the column's first overflow page are stored on the main page. Each overflow page is the size of [innodb-system-variables#innodb_page_size|innodb_page_size]]. If a column is too large to be stored on a single overflow page, then it is stored on multiple overflow pages. Each overflow page contains part of the data and a 20-byte pointer to the next overflow page, if a next page exists.