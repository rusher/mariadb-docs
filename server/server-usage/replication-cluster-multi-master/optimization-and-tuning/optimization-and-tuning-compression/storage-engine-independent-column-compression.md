
# Storage-Engine Independent Column Compression


Storage-engine independent column compression enables [TINYBLOB](../../../../reference/data-types/string-data-types/tinyblob.md), [BLOB](../../../../reference/data-types/string-data-types/blob.md), [MEDIUMBLOB](../../../../reference/data-types/string-data-types/mediumblob.md), [LONGBLOB](../../../../reference/data-types/string-data-types/longblob.md), [TINYTEXT](../../../../reference/data-types/string-data-types/tinytext.md), [TEXT](../../../../reference/data-types/string-data-types/text.md), [MEDIUMTEXT](../../../../reference/data-types/string-data-types/mediumtext.md), [LONGTEXT](../../../../reference/data-types/string-data-types/longtext.md), [VARCHAR](../../../../reference/data-types/string-data-types/varchar.md) and [VARBINARY](../../../../reference/data-types/string-data-types/varbinary.md) columns to be compressed.


This is performed by means of a new COMPRESSED [column attribute](../../../../reference/sql-statements-and-structure/vectors/create-table-with-vectors.md#column-and-index-definitions):
`<code>COMPRESSED[=<compression_method>]</code>`


Currently the only supported compression method is `<code>zlib</code>`.


### Field Length Compatibility


When using the `<code>COMPRESSED</code>` attribute, note that FIELD LENGTH is reduced by 1; for example, a BLOB has a length of 65535, while BLOB COMPRESSED has 65535-1. See [MDEV-15592](https://jira.mariadb.org/browse/MDEV-15592).


### New System Variables


#### `<code>column_compression_threshold</code>`


* Description: Minimum column data length eligible for compression.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--column-compression-threshold=#</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>100</code>`
* Range: `<code>0</code>` to `<code>4294967295</code>`



#### `<code>column_compression_zlib_level</code>`


* Description: zlib compression level (1 gives best speed, 9 gives best compression).
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--column-compression-zlib-level=#</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>6</code>`
* Range: `<code>1</code>` to `<code>9</code>`



#### `<code>column_compression_zlib_strategy</code>`


* Description: The strategy parameter is used to tune the compression algorithm. Use the value `<code>DEFAULT_STRATEGY</code>` for normal data, `<code>FILTERED</code>` for data produced by a filter (or predictor), `<code>HUFFMAN_ONLY</code>` to force Huffman encoding only (no string match), or `<code>RLE</code>` to limit match distances to one (run-length encoding). Filtered data consists mostly of small values with a somewhat random distribution. In this case, the compression algorithm is tuned to compress them better. The effect of `<code>FILTERED</code>` is to force more Huffman coding and less string matching; it is somewhat intermediate between `<code>DEFAULT_STRATEGY</code>` and `<code>HUFFMAN_ONLY</code>`. `<code>RLE</code>` is designed to be almost as fast as `<code>HUFFMAN_ONLY</code>`, but give better compression for PNG image data. The strategy parameter only affects the compression ratio but not the correctness of the compressed output even if it is not set appropriately. `<code>FIXED</code>` prevents the use of dynamic Huffman codes, allowing for a simpler decoder for special applications.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--column-compression-zlib-strategy=#</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>enum</code>`
* Default Value: `<code>DEFAULT_STRATEGY</code>`
* Valid Values: `<code>DEFAULT_STRATEGY</code>`, `<code>FILTERED</code>`, `<code>HUFFMAN_ONLY</code>`, `<code>RLE</code>`, `<code>FIXED</code>`



#### `<code>column_compression_zlib_wrap</code>`


* Description: If set to `<code>1</code>` (`<code>0</code>` is default), generate zlib header and trailer and compute adler32 check value. It can be used with storage engines that don't provide data integrity verification to detect data corruption.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--column-compression-zlib-wrap{=0|1}</code>`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>boolean</code>`
* Default Value: `<code>OFF</code>`



### New Status Variables


#### `<code>Column_compressions</code>`


* Description: Incremented each time field data is compressed.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`



#### `<code>Column_decompressions</code>`


* Description: Incremented each time field data is decompressed.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`



### Limitations


* The only supported method currently is zlib.
* The [CSV](../../../../reference/storage-engines/csv/csv-overview.md) storage engine stores data uncompressed on-disk even if the COMPRESSED attribute is present.
* It is not possible to create indexes over compressed columns.


### Comparison with InnoDB Page Compression


Storage-independent column compression is different to [InnoDB Page Compression](../../../../reference/storage-engines/innodb/innodb-page-compression.md) in a number of ways.


* It is storage engine independent, while InnoDB page compression applies to InnoDB only.
* By being specific to a column, one can access non-compressed fields without the decompression overhead.
* Only zlib is available, while InnoDB page compression can offer alternative compression algorithms.
* It is not recommended to use multiple forms of compression over the same data.
* It is intended for compressing large blobs, while InnoDB page compression is suitable for a more general case.
* Columns cannot be indexed, while with InnoDB page compression indexes are possible as usual.


### Examples


```
CREATE TABLE cmp (i TEXT COMPRESSED);

CREATE TABLE cmp2 (i TEXT COMPRESSED=zlib);
```

### See Also


* [InnoDB Page Compression](../../../../reference/storage-engines/innodb/innodb-page-compression.md)
* [InnoDB Compressed Row Format](../../../../reference/storage-engines/innodb/innodb-row-formats/innodb-compressed-row-format.md)

