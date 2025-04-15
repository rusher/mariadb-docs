
# InnoDB COMPRESSED Row Format


In [MariaDB 10.1](../../../../../release-notes/mariadb-community-server/what-is-mariadb-1010.md) and later, an alternative (and usually superior) way to compress InnoDB tables is by using [InnoDB Page Compression](../innodb-page-compression.md). See [Comparison with the COMPRESSED Row Format](../innodb-page-compression.md#comparison-with-the-compressed-row-format).


The `<code>COMPRESSED</code>` row format is similar to the `<code>COMPACT</code>` row format, but tables using the `<code>COMPRESSED</code>` row format can store even more data on overflow pages than tables using the `<code>COMPACT</code>` row format. This results in more efficient data storage than tables using the `<code>COMPACT</code>` row format, especially for tables containing columns using the [VARBINARY](../../../data-types/string-data-types/varbinary.md), [VARCHAR](../../../data-types/string-data-types/varchar.md), [BLOB](../../../data-types/string-data-types/blob.md) and [TEXT](../../../data-types/string-data-types/text.md) data types.


The `<code>COMPRESSED</code>` row format also supports compression of all data and index pages.


## Using the `<code>COMPRESSED</code>` Row Format


An InnoDB table that uses the `<code>COMPRESSED</code>` row format can be created by setting the [ROW_FORMAT](../../../sql-statements-and-structure/vectors/create-table-with-vectors.md#row_format) table option to `<code>COMPRESSED</code>` and by setting the [KEY_BLOCK_SIZE](../../../sql-statements-and-structure/vectors/create-table-with-vectors.md#key_block_size) table option to one of the following values in a [CREATE TABLE](../../../sql-statements-and-structure/vectors/create-table-with-vectors.md) or [ALTER TABLE](../../../sql-statements-and-structure/sql-statements/data-definition/alter/alter-tablespace.md) statement, where the units are in `<code>KB</code>`:


* `<code>1</code>`
* `<code>2</code>`
* `<code>4</code>`
* `<code>8</code>`
* `<code>16</code>`


`<code>16k</code>` is the default value of the [innodb_page_size](../innodb-system-variables.md#innodb_page_size) system variable, so using `<code>16</code>` will usually result in minimal compression unless one of the following is true:


* The table has many columns that can be stored in overflow pages, such as columns that use the [VARBINARY](../../../data-types/string-data-types/varbinary.md), [VARCHAR](../../../data-types/string-data-types/varchar.md), [BLOB](../../../data-types/string-data-types/blob.md) and [TEXT](../../../data-types/string-data-types/text.md) data types.
* The server is using a non-default [innodb_page_size](../innodb-system-variables.md#innodb_page_size) value that is greater than `<code>16k</code>`.


In [MariaDB 10.1](../../../../../release-notes/mariadb-community-server/what-is-mariadb-1010.md) and later, the value of the [innodb_page_size](../innodb-system-variables.md#innodb_page_size) system variable can be set to `<code>32k</code>` and `<code>64k</code>`. This is especially useful because the larger page size permits more columns using the [VARBINARY](../../../data-types/string-data-types/varbinary.md), [VARCHAR](../../../data-types/string-data-types/varchar.md), [BLOB](../../../data-types/string-data-types/blob.md) and [TEXT](../../../data-types/string-data-types/text.md) data types. Regardless, even when the value of the [innodb_page_size](../innodb-system-variables.md#innodb_page_size) system variable is set to some value higher than `<code>16k</code>`, `<code>16</code>` is still the maximum value for the [KEY_BLOCK_SIZE](../../../sql-statements-and-structure/vectors/create-table-with-vectors.md#key_block_size) table option for InnoDB tables using the `<code>COMPRESSED</code>` row format.


The `<code>COMPRESSED</code>` row format cannot be set as the default row format with the [innodb_default_row_format](../innodb-system-variables.md#innodb_default_row_format) system variable.


The `<code>COMPRESSED</code>` row format is only supported by the `<code>Barracuda</code>` [file format](../innodb-file-format.md). As a side effect, in [MariaDB 10.1](../../../../../release-notes/mariadb-community-server/what-is-mariadb-1010.md) and before, the `<code>COMPRESSED</code>` row format is only supported if the [InnoDB file format](../innodb-file-format.md) is `<code>Barracuda</code>`. Therefore, the [innodb_file_format](../innodb-system-variables.md#innodb_file_format) system variable must be set to `<code>Barracuda</code>` to use these row formats in those versions.


In [MariaDB 10.1](../../../../../release-notes/mariadb-community-server/what-is-mariadb-1010.md) and before, the `<code>COMPRESSED</code>` row format is also only supported if the table is in a [file per-table](../innodb-tablespaces/innodb-file-per-table-tablespaces.md) tablespace. Therefore, the [innodb_file_per_table](../innodb-system-variables.md#innodb_file_per_table) system variable must be set to `<code>ON</code>` to use this row format in those versions.


It is also recommended to set the [innodb_strict_mode](../innodb-system-variables.md#innodb_strict_mode) system variable to `<code>ON</code>` when using this row format.


InnoDB automatically uses the `<code>COMPRESSED</code>` row format for a table if the [KEY_BLOCK_SIZE](../../../sql-statements-and-structure/vectors/create-table-with-vectors.md#key_block_size) table option is set to some value in a [CREATE TABLE](../../../sql-statements-and-structure/vectors/create-table-with-vectors.md) or [ALTER TABLE](../../../sql-statements-and-structure/sql-statements/data-definition/alter/alter-tablespace.md) statement. For example:


```
SET SESSION innodb_strict_mode=ON;

SET GLOBAL innodb_file_per_table=ON;

SET GLOBAL innodb_file_format='Barracuda';

CREATE TABLE tab (
   id int,
   str varchar(50)
) ENGINE=InnoDB KEY_BLOCK_SIZE=4;
```

If the [KEY_BLOCK_SIZE](../../../sql-statements-and-structure/vectors/create-table-with-vectors.md#key_block_size) table option is **not** set to some value, but the [ROW_FORMAT](../../../sql-statements-and-structure/vectors/create-table-with-vectors.md#row_format) table option is set to `<code>COMPRESSED</code>` in a [CREATE TABLE](../../../sql-statements-and-structure/vectors/create-table-with-vectors.md) or [ALTER TABLE](../../../sql-statements-and-structure/sql-statements/data-definition/alter/alter-tablespace.md) statement, then InnoDB uses a default value of `<code>8</code>` for the [KEY_BLOCK_SIZE](../../../sql-statements-and-structure/vectors/create-table-with-vectors.md#key_block_size) table option. For example:


```
SET SESSION innodb_strict_mode=ON;

SET GLOBAL innodb_file_per_table=ON;

SET GLOBAL innodb_file_format='Barracuda';

CREATE TABLE tab (
   id int,
   str varchar(50)
) ENGINE=InnoDB ROW_FORMAT=COMPRESSED;
```

## Compression with the `<code>COMPRESSED</code>` Row Format


The `<code>COMPRESSED</code>` row format supports compression of all data and index pages.


To avoid compressing and uncompressing pages too many times, InnoDB tries to keep both compressed and uncompressed pages in the [buffer pool](../innodb-buffer-pool.md) when there is enough room. This results in a bigger cache. When there is not enough room, an adaptive LRU algorithm is used to decide whether compressed or uncompressed pages should be evicted from the buffer: for CPU-bound workloads, the compressed pages are evicted first; for I/O-bound workloads, the uncompressed pages are evicted first. Of course, when necessary, both the compressed and uncompressed version of the same data can be evicted from the buffer.


Each compressed page has an uncompressed *modification log*, stored within the page itself. InnoDB writes small changes into it. When the space in the modification log runs out, the page is uncompressed, changes are applied, and the page is recompressed again. This is done to avoid some unnecessary decompression and compression operations.


Sometimes a *compression failure* might happen, because the data has grown too much to fit the page. When this happens, the page (and the index node) is split into two different pages. This process can be repeated recursively until the data fit the pages. This can be CPU-consuming on some busy servers which perform many write operations.


Before writing a compressed page into a data file, InnoDB writes it into the [redo log](../innodb-redo-log.md). This ensures that the [redo log](../innodb-redo-log.md) can always be used to recover tables after a crash, even if the compression library is updated and some incompatibilities are introduced. But this also means that the [redo log](../innodb-redo-log.md) will grow faster and might need more space, or the frequency of checkpoints might need to increase.


## Monitoring Performance of the `<code>COMPRESSED</code>` Row Format


The following `<code>INFORMATION_SCHEMA</code>` tables can be used to monitor the performances of InnoDB compressed tables:


* [INNODB_CMP and INNODB_CMP_RESET](../../../sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb_cmp-and-innodb_cmp_reset-tables.md)
* [INNODB_CMP_PER_INDEX and INNODB_CMP_PER_INDEX_RESET](../../../sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb-tables-information-schema-innodb_cmp_per_index-an.md)
* [INNODB_CMPMEM and INNODB_CMPMEM_RESET](../../../sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb_cmpmem-and-innodb_cmpmem_reset-tables.md)


## Index Prefixes with the `<code>COMPRESSED</code>` Row Format


The `<code>COMPRESSED</code>` row format supports index prefixes up to 3072 bytes. In [MariaDB 10.2](../../../../../release-notes/mariadb-community-server/what-is-mariadb-102.md) and before, the [innodb_large_prefix](../innodb-system-variables.md#innodb_large_prefix) system variable is used to configure the maximum index prefix length. In these versions, if [innodb_large_prefix](../innodb-system-variables.md#innodb_large_prefix) is set to `<code>ON</code>`, then the maximum prefix length is 3072 bytes, and if it is set to `<code>OFF</code>`, then the maximum prefix length is 767 bytes.


## Overflow Pages with the `<code>COMPRESSED</code>` Row Format


All InnoDB row formats can store certain kinds of data in overflow pages. This allows for the maximum row size of an InnoDB table to be larger than the maximum amount of data that can be stored in the row's main data page. See [Maximum Row Size](#maximum-row-size) for more information about the other factors that can contribute to the maximum row size for InnoDB tables.


In the `<code>COMPRESSED</code>` row format variable-length columns, such as columns using the [VARBINARY](../../../data-types/string-data-types/varbinary.md), [VARCHAR](../../../data-types/string-data-types/varchar.md), [BLOB](../../../data-types/string-data-types/blob.md) and [TEXT](../../../data-types/string-data-types/text.md) data types, can be completely stored in overflow pages.


InnoDB only considers using overflow pages if the table's row size is greater than half of [innodb_page_size](../innodb-system-variables.md#innodb_page_size). If the row size is greater than this, then InnoDB chooses variable-length columns to be stored on overflow pages until the row size is less than half of [innodb_page_size](../innodb-system-variables.md#innodb_page_size).


For [BLOB](../../../data-types/string-data-types/blob.md) and [TEXT](../../../data-types/string-data-types/text.md) columns, only values longer than 40 bytes are considered for storage on overflow pages. For [VARBINARY](../../../data-types/string-data-types/varbinary.md) and [VARCHAR](../../../data-types/string-data-types/varchar.md) columns, only values longer than 255 bytes are considered for storage on overflow pages. Bytes that are stored to track a value's length do not count towards these limits. These limits are only based on the length of the actual column's data.


These limits differ from the limits for the `<code>COMPACT</code>` row format, where the limit is 767 bytes for all types.


Fixed-length columns greater than 767 bytes are encoded as variable-length columns, so they can also be stored in overflow pages if the table's row size is greater than half of [innodb_page_size](../innodb-system-variables.md#innodb_page_size). Even though a column using the [CHAR](../../../sql-statements-and-structure/sql-statements/built-in-functions/secondary-functions/information-functions/charset.md) data type can hold at most 255 characters, a [CHAR](../../../sql-statements-and-structure/sql-statements/built-in-functions/secondary-functions/information-functions/charset.md) column can still exceed 767 bytes in some cases. For example, a `<code>char(255)</code>` column can exceed 767 bytes if the [character set](../../../data-types/string-data-types/character-sets/README.md) is `<code>utf8mb4</code>`.


If a column is chosen to be stored on overflow pages, then the entire value of the column is stored on overflow pages, and only a 20-byte pointer to the column's first overflow page is stored on the main page. Each overflow page is the size of [innodb_page_size](../innodb-system-variables.md#innodb_page_size). If a column is too large to be stored on a single overflow page, then it is stored on multiple overflow pages. Each overflow page contains part of the data and a 20-byte pointer to the next overflow page, if a next page exists.


This behavior differs from the behavior of the `<code>COMPACT</code>` row format, which always stores the column prefix on the main page. This allows tables using the `<code>COMPRESSED</code>` row format to contain a high number of columns using the [VARBINARY](../../../data-types/string-data-types/varbinary.md), [VARCHAR](../../../data-types/string-data-types/varchar.md), [BLOB](../../../data-types/string-data-types/blob.md) and [TEXT](../../../data-types/string-data-types/text.md) data types.


## Read-Only



##### MariaDB starting with [10.6](../../../../../release-notes/mariadb-community-server/what-is-mariadb-106.md)
From [MariaDB 10.6.0](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-1060-release-notes.md) until [MariaDB 10.6.5](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-1065-release-notes.md), tables that are of the `<code>COMPRESSED</code>` row format are read-only by default. This was intended to be the first step towards removing write support and deprecating the feature.
This plan has been scrapped, and from [MariaDB 10.6.6](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-1066-release-notes.md), `<code>COMPRESSED</code>` tables are no longer read-only by default.
From [MariaDB 10.6.0](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-1060-release-notes.md) to [MariaDB 10.6.5](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-1065-release-notes.md), set the  [innodb_read_only_compressed](../innodb-system-variables.md#innodb_read_only_compressed) variable to `<code>OFF</code>` to make the tables writable.


## See Also


* [InnoDB Page Compression](../innodb-page-compression.md)
* [Storage-Engine Independent Column Compression](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/optimization-and-tuning-compression/storage-engine-independent-column-compression.md)

