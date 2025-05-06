
# Result Set Packets


MariaDB Server sends the following packets as part of a result set:
A resultset consists of different packets:


* [Resultset metadata](#ResultSet-metadata)

  * 1 [Column count packet](#column-count-packet)


* if not (`MARIADB_CLIENT_CACHE_METADATA` capability set) OR (send metadata == 1)

  * for each column (i.e column_count times) 

    * [Column Definition packet](#column-definition-packet)
* if not (`CLIENT_DEPRECATE_EOF` capability set) [EOF_Packet](eof_packet.md)
* n [resultset row](resultset-row.md)
* if error 

  * [ERR_Packet](err_packet.md)
* else 

  * if `CLIENT_DEPRECATE_EOF` capability 

    * [OK_Packet](ok_packet.md) with a 0xFE header
  * else [EOF_Packet](eof_packet.md)





It would be unsafe to assume that any packet with a 0xFE header is an [OK packet (OK_Packet)](ok_packet.md) or an [EOF packet (EOF_Packet)](eof_packet.md), because [result-set row packets (ResultsetRow)](resultset-row.md) can also begin with 0xFE when using the text protocol with a field length greater than 0xFFFFFF.
To safely confirm that a packet with a 0xFE header is an [OK packet (OK_Packet)](ok_packet.md) or an [EOF packet (EOF_Packet)](eof_packet.md), you must also check that the packet length is less than 0xFFFFFF.


## Column Count Packet


The column count packet describes the number of columns in the result set. It uses the following format:



* [int<lenenc>](../protocol-data-types.md#length-encoded-integers) column count
* if (`MARIADB_CLIENT_CACHE_METADATA` capability set)

  * int<1> metadata follows (0 / 1)



The metadata indicator byte is only present if both the client and the server declare the `MARIADB_CLIENT_CACHE_METADATA` capability.


If the metadata byte is set to 1, the normal metadata will follow the column definitions. If the metadata byte is set to 0, the Column Count Packet is immediately followed by the second [EOF packet (EOF_Packet)](eof_packet.md) or the resultset rows if the `CLIENT_DEPRECATE_EOF` capability is set.


## Column Definition Packet


A column definition packet describes a column in the result set. It uses the following format:



* [string<lenenc>](../protocol-data-types.md#length-encoded-strings) catalog (always 'def')
* [string<lenenc>](../protocol-data-types.md#length-encoded-strings) schema
* [string<lenenc>](../protocol-data-types.md#length-encoded-strings) table alias
* [string<lenenc>](../protocol-data-types.md#length-encoded-strings) table
* [string<lenenc>](../protocol-data-types.md#length-encoded-strings) column alias
* [string<lenenc>](../protocol-data-types.md#length-encoded-strings) column
* if extended type supported (see `MARIADB_CLIENT_EXTENDED_METADATA` ) 

  * [string<lenenc>](../protocol-data-types.md#length-encoded-strings) [extended metadata](#extended-metadata)
* [int<lenenc>](../protocol-data-types.md#length-encoded-integers) length of fixed fields (=0xC)
* [int<2>](../protocol-data-types.md#fixed-length-integers) character set number
* [int<4>](../protocol-data-types.md#fixed-length-integers) max. column size
* [int<1>](../protocol-data-types.md#fixed-length-integers) [Field types](#field-types)
* [int<2>](../protocol-data-types.md#fixed-length-integers) [Field detail flag](#field-details-flag)
* [int<1>](../protocol-data-types.md#fixed-length-integers) decimals
* [int<2>](../protocol-data-types.md#fixed-length-integers) - unused -



### Field types


The column type field in the column definition packet describes the base type of the column. It also indicates how the values are encoded for COM_STMT_EXECUTE parameters and binary resultset rows.



| Value | Protocol Column Type | Encoding |
| --- | --- | --- |
| Value | Protocol Column Type | Encoding |
| 0 | MYSQL_TYPE_DECIMAL | [byte<lenenc> encoding](../protocol-data-types.md#length-encoded-bytes) |
| 1 | MYSQL_TYPE_TINY | [TINYINT Binary encoding](resultset-row.md#tinyint-binary-encoding) |
| 2 | MYSQL_TYPE_SHORT | [SMALLINT Binary encoding](resultset-row.md#smallint-binary-encoding) |
| 3 | MYSQL_TYPE_LONG | [INTEGER Binary encoding](resultset-row.md#integer-binary-encoding) |
| 4 | MYSQL_TYPE_FLOAT | [FLOAT Binary encoding](resultset-row.md#float-binary-encoding) |
| 5 | MYSQL_TYPE_DOUBLE | [DOUBLE Binary encoding](resultset-row.md#double-binary-encoding) |
| 6 | MYSQL_TYPE_NULL | Not used, nullness is indicated by the NULL-bitmap in the result |
| 7 | MYSQL_TYPE_TIMESTAMP | [TIMESTAMP Binary encoding](resultset-row.md#timestamp-binary-encoding) |
| 8 | MYSQL_TYPE_LONGLONG | [BIGINT Binary encoding](resultset-row.md#bigint-binary-encoding) |
| 9 | MYSQL_TYPE_INT24 | [INTEGER Binary encoding](resultset-row.md#integer-binary-encoding) |
| 10 | MYSQL_TYPE_DATE | [TIMESTAMP Binary encoding](resultset-row.md#timestamp-binary-encoding) |
| 11 | MYSQL_TYPE_TIME | [TIME Binary encoding](resultset-row.md#time-binary-encoding) |
| 12 | MYSQL_TYPE_DATETIME | [TIMESTAMP Binary encoding](resultset-row.md#timestamp-binary-encoding) |
| 13 | MYSQL_TYPE_YEAR | [SMALLINT Binary encoding](resultset-row.md#smallint-binary-encoding) |
| 14 | MYSQL_TYPE_NEWDATE | [byte<lenenc> encoding](../protocol-data-types.md#length-encoded-bytes) |
| 15 | MYSQL_TYPE_VARCHAR | [byte<lenenc> encoding](../protocol-data-types.md#length-encoded-bytes) |
| 16 | MYSQL_TYPE_BIT | [byte<lenenc> encoding](../protocol-data-types.md#length-encoded-bytes) |
| 17 | MYSQL_TYPE_TIMESTAMP2 | Used only in the replication protocol |
| 18 | MYSQL_TYPE_DATETIME2 | Used only in the replication protocol |
| 19 | MYSQL_TYPE_TIME2 | Used only in the replication protocol |
| 245 | MYSQL_TYPE_JSON | [byte<lenenc> encoding](../protocol-data-types.md#length-encoded-bytes) (only used with MySQL, MariaDB uses MYSQL_TYPE_STRING for JSON) |
| 246 | MYSQL_TYPE_NEWDECIMAL | [byte<lenenc> encoding](../protocol-data-types.md#length-encoded-bytes) |
| 247 | MYSQL_TYPE_ENUM | [byte<lenenc> encoding](../protocol-data-types.md#length-encoded-bytes) |
| 248 | MYSQL_TYPE_SET | [byte<lenenc> encoding](../protocol-data-types.md#length-encoded-bytes) |
| 249 | MYSQL_TYPE_TINY_BLOB | [byte<lenenc> encoding](../protocol-data-types.md#length-encoded-bytes) |
| 250 | MYSQL_TYPE_MEDIUM_BLOB | [byte<lenenc> encoding](../protocol-data-types.md#length-encoded-bytes) |
| 251 | MYSQL_TYPE_LONG_BLOB | [byte<lenenc> encoding](../protocol-data-types.md#length-encoded-bytes) |
| 252 | MYSQL_TYPE_BLOB | [byte<lenenc> encoding](../protocol-data-types.md#length-encoded-bytes) |
| 253 | MYSQL_TYPE_VAR_STRING | [byte<lenenc> encoding](../protocol-data-types.md#length-encoded-bytes) |
| 254 | MYSQL_TYPE_STRING | [byte<lenenc> encoding](../protocol-data-types.md#length-encoded-bytes) |
| 255 | MYSQL_TYPE_GEOMETRY | [byte<lenenc> encoding](../protocol-data-types.md#length-encoded-bytes) |



### Field Details Flag


The column details flag describes certain column attributes and whether certain column options are set.


It is a bitmask with the following flags:



| Flag Value | Flag Name | Flag Description |
| --- | --- | --- |
| Flag Value | Flag Name | Flag Description |
| 1 | NOT_NULL | field cannot be null |
| 2 | PRIMARY_KEY | field is a primary key |
| 4 | UNIQUE_KEY | field is unique |
| 8 | MULTIPLE_KEY | field is in a multiple key |
| 16 | BLOB | is this field a Blob |
| 32 | UNSIGNED | is this field unsigned |
| 64 | ZEROFILL_FLAG | is this field a zerofill |
| 128 | BINARY_COLLATION | whether this field has a binary collation |
| 256 | ENUM | Field is an enumeration |
| 512 | AUTO_INCREMENT | field auto-increment |
| 1024 | TIMESTAMP | field is a timestamp value |
| 2048 | SET | field is a SET |
| 4096 | NO_DEFAULT_VALUE_FLAG | field doesn't have default value |
| 8192 | ON_UPDATE_NOW_FLAG | field is set to NOW on UPDATE |
| 32768 | NUM_FLAG | field is num |



The `BLOB` flag cannot be used to determine if a column has binary data, because `[BINARY](../../../../../reference/data-types/string-data-types/binary.md)` and `[VARBINARY](../../../../../reference/data-types/string-data-types/varbinary.md)` columns are treated as strings, instead of blobs.
The `BINARY_COLLATION` flag can be used to determine if a string column has binary data.


### Extended metadata


This extended column type information can be used to find out more specific details about the column type.


For example:


* For a `[POINT](../../../../../reference/sql-statements-and-structure/geographic-geometric-features/geometry-constructors/point.md)` column, the column type field will be `MYSQL_TYPE_GEOMETRY`, but the extended type will indicate 'point'.
* For a `[JSON](../../../../../reference/data-types/string-data-types/json.md)` column, the column type field will be `MYSQL_TYPE_STRING`, but the extended type will indicate 'json'.



* while string has data

  * [int<1>](../protocol-data-types.md#fixed-length-integers) data type: 0x00:type, 0x01: format
  * [string<lenenc>](../protocol-data-types.md#length-encoded-strings) value




CC BY-SA / Gnu FDL

