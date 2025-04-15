
# InnoDB DYNAMIC Row Format

`<code>DYNAMIC</code>` is the default InnoDB row format.



The `<code>DYNAMIC</code>` row format is similar to the `<code>COMPACT</code>` row format, but tables using the `<code>DYNAMIC</code>` row format can store even more data on overflow pages than tables using the `<code>COMPACT</code>` row format. This results in more efficient data storage than tables using the `<code>COMPACT</code>` row format, especially for tables containing columns using the [VARBINARY](../../../data-types/string-data-types/varbinary.md), [VARCHAR](../../../data-types/string-data-types/varchar.md), [BLOB](../../../data-types/string-data-types/blob.md) and [TEXT](../../../data-types/string-data-types/text.md) data types. While InnoDB tables using the `<code>COMPRESSED</code>` row format can result in even greater space-efficiency, COMPRESSED requires substantially more memory and CPU to both read and write, so there is a significant performance and concurrency trade-off for that space-efficiency gain. COMPRESSED tables are not recommended for production use in most situations, while DYNAMIC row format scales well in high-performance environments.


The `<code>DYNAMIC</code>` row format was originally introduced in [MariaDB 5.5](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5.md).


## Using the DYNAMIC Row Format


The default row format is `<code>DYNAMIC</code>`, as long as the [innodb_default_row_format](../innodb-system-variables.md#innodb_default_row_format) system variable has not been modified. Therefore, in these versions, the easiest way to create an InnoDB table that uses the `<code>DYNAMIC</code>` row format is by **not** setting the [ROW_FORMAT](../../../sql-statements-and-structure/vectors/create-table-with-vectors.md#row_format) table option at all in a [CREATE TABLE](../../../sql-statements-and-structure/vectors/create-table-with-vectors.md) or [ALTER TABLE](../../../sql-statements-and-structure/sql-statements/data-definition/alter/alter-tablespace.md) statement.


It is recommended to set the [innodb_strict_mode](../innodb-system-variables.md#innodb_strict_mode) system variable to `<code>ON</code>` when using this row format.


For example:


```
SET SESSION innodb_strict_mode=ON;

SET GLOBAL innodb_default_row_format='dynamic';

CREATE TABLE tab (
   id int,
   str varchar(50)
) ENGINE=InnoDB;
```

## Index Prefixes with the DYNAMIC Row Format


The `<code>DYNAMIC</code>` row format supports index prefixes up to 3072 bytes. In earlier versions of MariaDB, the [innodb_large_prefix](../innodb-system-variables.md#innodb_large_prefix) system variable is used to configure the maximum index prefix length. In these versions, if [innodb_large_prefix](../innodb-system-variables.md#innodb_large_prefix) is set to `<code>ON</code>`, then the maximum prefix length is 3072 bytes, and if it is set to `<code>OFF</code>`, then the maximum prefix length is 767 bytes.


## Overflow Pages with the DYNAMIC Row Format


All InnoDB row formats can store certain kinds of data in overflow pages. This allows for the maximum row size of an InnoDB table to be larger than the maximum amount of data that can be stored in the row's main data page. See [Maximum Row Size](#maximum-row-size) for more information about the other factors that can contribute to the maximum row size for InnoDB tables.


In the `<code>DYNAMIC</code>` row format variable-length columns, such as columns using the [VARBINARY](../../../data-types/string-data-types/varbinary.md), [VARCHAR](../../../data-types/string-data-types/varchar.md), [BLOB](../../../data-types/string-data-types/blob.md) and [TEXT](../../../data-types/string-data-types/text.md) data types, can be completely stored in overflow pages.


InnoDB only considers using overflow pages if the table's row size is greater than half of [innodb_page_size](../innodb-system-variables.md#innodb_page_size). If the row size is greater than this, then InnoDB chooses variable-length columns to be stored on overflow pages until the row size is less than half of [innodb_page_size](../innodb-system-variables.md#innodb_page_size).


For [BLOB](../../../data-types/string-data-types/blob.md) and [TEXT](../../../data-types/string-data-types/text.md) columns, only values longer than 40 bytes are considered for storage on overflow pages. For [VARBINARY](../../../data-types/string-data-types/varbinary.md) and [VARCHAR](../../../data-types/string-data-types/varchar.md) columns, only values longer than 255 bytes are considered for storage on overflow pages. Bytes that are stored to track a value's length do not count towards these limits. These limits are only based on the length of the actual column's data.


These limits differ from the limits for the `<code>COMPACT</code>` row format, where the limit is 767 bytes for all types.


Fixed-length columns greater than 767 bytes are encoded as variable-length columns, so they can also be stored in overflow pages if the table's row size is greater than half of [innodb_page_size](../innodb-system-variables.md#innodb_page_size). Even though a column using the [CHAR](../../../sql-statements-and-structure/sql-statements/built-in-functions/secondary-functions/information-functions/charset.md) data type can hold at most 255 characters, a [CHAR](../../../sql-statements-and-structure/sql-statements/built-in-functions/secondary-functions/information-functions/charset.md) column can still exceed 767 bytes in some cases. For example, a `<code>char(255)</code>` column can exceed 767 bytes if the [character set](../../../data-types/string-data-types/character-sets/README.md) is `<code>utf8mb4</code>`.


If a column is chosen to be stored on overflow pages, then the entire value of the column is stored on overflow pages, and only a 20-byte pointer to the column's first overflow page is stored on the main page. Each overflow page is the size of [innodb_page_size](../innodb-system-variables.md#innodb_page_size). If a column is too large to be stored on a single overflow page, then it is stored on multiple overflow pages. Each overflow page contains part of the data and a 20-byte pointer to the next overflow page, if a next page exists.


This behavior differs from the behavior of the `<code>COMPACT</code>` row format, which always stores the column prefix on the main page. This allows tables using the `<code>DYNAMIC</code>` row format to contain a high number of columns using the [VARBINARY](../../../data-types/string-data-types/varbinary.md), [VARCHAR](../../../data-types/string-data-types/varchar.md), [BLOB](../../../data-types/string-data-types/blob.md) and [TEXT](../../../data-types/string-data-types/text.md) data types.

