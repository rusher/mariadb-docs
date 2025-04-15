
# ROWS_EVENT_V1/V2, ROWS_COMPRESSED_EVENT_V1

A ROWS_EVENT_V1 is written for row based replication if data is inserted, deleted or updated


A ROWS_EVENT (version 2) is written for row based replication if data is inserted, deleted or updated if database server is MySQL 5.6 or newer. MariaDB Server doesn't send version 2 row events.


#### Event types



|   |   |
| --- | --- |
| WRITE_ROWS_EVENT_V1 | Insert new row |
| UPDATE_ROWS_EVENT_V1 | Update existing row |
| DELETE_ROWS_EVENT_V1 | Delete existing row |
| WRITE_ROWS_COMPRESSED_EVENT_V1 | Insert new row |
| UPDATE_ROWS_COMPRESSED_EVENT_V1 | Update existing row |
| DELETE_ROWS_COMPRESSED_EVENT_V1 | Delete existing row |
| WRITE_ROWS_EVENT | Insert new row (version 2, MySQL only) |
| UPDATE_ROWS_EVENT | Update existing row (version 2, MySQL only) |
| DELETE_ROWS_EVENT | Delete existing row (version 2, MySQL only) |



#### Header


* WRITE_ROWS_EVENT_V1: Event Type is 23 (0x17)
* UPDATE_ROWS_EVENT_V1: Event Type is 24 (0x18)
* DELETE_ROWS_EVENT_V1: Event Type is 25 (0x19)
* WRITE_ROWS_EVENT: Event Type is 30 (0xFD)
* UPDATE_ROWS_EVENT: Event Type is 31 (0xFE)
* DELETE_ROWS_EVENT: Event Type is 32 (0x20)
* WRITE_ROWS_COMPRESSED_EVENT_V1: Event Type is 166 (0xA6)
* UPDATE_ROWS_COMPRESSED_EVENT_V1: Event Type is 167 (0xA7)
* DELETE_ROWS_COMPRESSED_EVENT_V1: Event Type is 168 (0xA8)


#### Fields



* [uint<6>](../protocol-data-types.md#fixed-length-integers) The table id
* [uint<2>](../protocol-data-types.md#fixed-length-integers) Flags
* if rows_event is version 2

  * [uint<2>](../protocol-data-types.md#fixed-length-integers) Extra data length
  * [string<len>](../protocol-data-types.md#fixed-length-strings) Extra data
* [uint<lenenc>](../protocol-data-types.md#fixed-length-integers) Number of columns
* [byte<n>](../protocol-data-types.md#fixed-length-bytes)Columns used. n = (number_of_columns + 7)/8
* if (event_type == UPDATE_ROWS_EVENT_v1

  * [byte<n>](../protocol-data-types.md#fixed-length-bytes) Columns used (Update). n = (number_of_columns + 7)/8


* if *_COMPRESSED_EVENT_V1

  * byte<1> header

    * algorithm: (header & 0x07) >> 4 (always 0=zlib)
    * header_size: header & 0x07
  * byte<header_size>uncompressed length, stored in MyISAM format:


* [byte<n>](../protocol-data-types.md#fixed-length-bytes) Null Bitmap (n = (number_of_columns + 7)/8)
* [string<len>](../protocol-data-types.md#fixed-length-strings) Column data. The length needs to be calculated by checking the column types from referring TABLE_MAP_EVENT.
* if (event_type == UPDATE_ROWS_EVENT_v1

  * [byte<n>](../protocol-data-types.md#fixed-length-bytes) Null Bitmap_Update. n = (number_of_columns + 7)/8
  * [string<len>](../protocol-data-types.md#fixed-length-strings) Update Column data. The length needs to be calculated by checking the used colums bitmap and column types from referring TABLE_MAP_EVENT.



#### Table id


Table id refers to a table defined by [TABLE_MAP_EVENT](table_map_event.md). The special value 0xFFFFFF should have "end of statement flag" (0x0001) set and indicates that table maps can be freed.


#### Flags



|   |   |
| --- | --- |
| 0x0001 | End of statement |
| 0x0002 | No foreign key checks |
| 0x0004 | No unique key checks |
| 0x0008 | Indicates that rows in this event are complete |
| 0x0010 | No check constraints |



#### Extra data length (version 2)


The length of extra data


#### Extra data (version 2)


Extra data, length is extra data length - 2


## Column Data Formats


The row data is stored in a packed format where each field is encoded in a particular format. The encoding is almost identical to the binary protocol but there are a few differences.


The field metadata is stored in the metadata block of the [TABLE_MAP_EVENT](table_map_event.md). The metadata is required to decode the events. The following list shows number of bytes a field uses from the metadata block.


* 2 bytes

  * MYSQL_TYPE_BIT
  * MYSQL_TYPE_ENUM
  * MYSQL_TYPE_SET
  * MYSQL_TYPE_NEWDECIMAL
  * MYSQL_TYPE_DECIMAL
  * MYSQL_TYPE_VARCHAR
  * MYSQL_TYPE_VAR_STRING
  * MYSQL_TYPE_STRING


* 1 byte

  * MYSQL_TYPE_TINY_BLOB
  * MYSQL_TYPE_MEDIUM_BLOB
  * MYSQL_TYPE_LONG_BLOB
  * MYSQL_TYPE_BLOB
  * MYSQL_TYPE_TIMESTAMP2
  * MYSQL_TYPE_DATETIME2
  * MYSQL_TYPE_TIME2
  * MYSQL_TYPE_FLOAT
  * MYSQL_TYPE_DOUBLE


The types that aren't listed here do not store data in the the metadata block.


#### Simple Types



|   |   |
| --- | --- |
| MYSQL_TYPE_NULL | Bit set in null bitmap, no value in row data |
| MYSQL_TYPE_TINY | 1 byte integer |
| MYSQL_TYPE_YEAR | 1 byte integer (year = value + 1900) |
| MYSQL_TYPE_SHORT | 2 byte integer |
| MYSQL_TYPE_INT24 | 3 byte integer |
| MYSQL_TYPE_LONG | 4 byte integer |
| MYSQL_TYPE_LONGLONG | 8 byte integer |
| MYSQL_TYPE_FLOAT | 4 byte floating point value (stored as a C float type) |
| MYSQL_TYPE_DOUBLE | 8 byte floating point value (stored as a C double type) |



#### `<code>MYSQL_TYPE_BLOB</code>` and other blob types


Stored as a length-encoded string where the string is preceded by a variable-sized integer that stores the length of the blob. The size of the preceding integer in bytes is stored as a one byte integer in the table metadata that is a part of the table map event.


For example if the value 4 is stored in the table metadata the length is stored as a 4 byte integer (e.g. `<code>uint32_t</code>`) followed by the data.


The exact column_type can be determined by the metadata length:



|   |   |
| --- | --- |
| Length | Type |
| 1 | MYSQL_TYPE_TINY_BLOB |
| 2 | MYSQL_TYPE_BLOB |
| 3 | MYSQL_TYPE_MEDIUM_BLOB |
| 4 | MYSQL_TYPE_LONG_BLOB |



#### `<code>MYSQL_TYPE_STRING</code>`, `<code>MYSQL_TYPE_SET</code>` and `<code>MYSQL_TYPE_ENUM</code>`


Stored as a fixed-length string with the length of the string stored in the second byte of the table metadata. All three of these types are stored as `<code>MYSQL_TYPE_STRING</code>` in the binlog and the real type of the field is stored in the first byte of the metadata.


#### `<code>MYSQL_TYPE_VARCHAR</code>` and other variable length string types


Stored as a length-encoded string where the string is preceded by a variable-sized integer that stores the length of the string. The field length is stored as a two byte integer in the table metadata.


If the field length is larger than 255, the string length is stored as a two byte integer. If the value is equal to or less than 255, the string length is stored as a one byte integer.


#### `<code>MYSQL_TYPE_DATETIME</code>`


**Note**: This field type is only used in MariaDB if global variable mysql56_temporal_format was set to OFF.
Stored as a 8 byte value with the values stored as multiples of 100. This means that the stored value is in the format YYYYMMDDHHMMSS and can be easily extracted by repeatedly calculating the remainder of dividing the value by 100 and dividing the value by 100. The following pseudo-code demonstrates extracting the value.


```
value = read_8_byte_value(row_data)
date_val= value / 1000000
time_val= value % 1000000

year = (date_val / 100) / 100
month = (date_val / 100) % 100
day = date_val % 100
hour= (time_val / 100) / 100
minute = (time_val / 100) % 100
second = time_val % 100
```


#### `<code>MYSQL_TYPE_TIME</code>`


**Note**: This field type is only used in MariaDB if global variable mysql56_temporal_format was set to OFF.
Stored as a 3 byte value with the values stored as multiples of 100. This means that the stored value is in the format HHMMSS and can be easily extracted the same way a `<code>MYSQL_TYPE_DATETIME</code>` is extracted. The following pseudo-code demonstrates extracting the value.


```
time_val = read_3_byte_value(row_data); /* myisam pack format */
hour= (time_val / 100) / 100;
minute = (time_val / 100) % 100;
second = time_val % 100;
```


#### `<code>MYSQL_TYPE_DATETIME2</code>`


Stored as 4-byte value The number of decimals for the fractional part is stored in the table metadata as a one byte value. The number of bytes that follow the 5 byte datetime value can be calculated with the following formula: `<code>(decimals + 1) / 2</code>`


```
val = read_5_byte_value(row_data) - 0x8000000000
d_val= val >> 17;
t_val = val % (1 << 17);

day= d_val % (1 << 5);
month= (d_val >> 5) % 13;
year= (d_val >> 5) / 13;
second= t_val % (1 << 6);
minute= (t_val >> 6) % (1 << 6);
hour= (t_val)(time_part >> 12);
```


#### `<code>MYSQL_TYPE_TIME2</code>`


Stored as 3-byte value The number of decimals for the fractional part is stored in the table metadata as a one byte value. The number of bytes that follow the 3 byte time value can be calculated with the following formula: `<code>(decimals + 1) / 2</code>`


```
t_val = read_3_byte_value(row_data) - 0x800000
if (t_val < 0)
{
  signed= 1;
  t_val= - tval;
}
hour= (t_val >> 12) % (1 << 10);
minute= (t_val >> 6) % (1 << 6);
second= t_val % (1 << 6);
```


#### `<code>MYSQL_TYPE_TIMESTAMP2</code>`


Stored as a 4 byte UNIX timestamp (number of seconds since 00:00, Jan 1 1970 UTC) followed by the fractional second parts. The number of decimals for the fractional part is stored in the table metadata as a one byte value. The number of bytes that follow the 4 byte timestamp can be calculated with the following formula: `<code>(decimals + 1) / 2</code>`


##### Microseconds for MYSQL_TYPE_DATETIME2, MYSQL_TYPE_TIME2 and MYSQL_TYPE_TIMESTAMP


```
len = (decimals + 1) / 2
  val= read_len_byte_value(row_data)
  llen= 0: microseconds= 0
  len = 1 or 2: microseconds = val * 10000
  len = 3 or 4: microseconds = 2-bytes val in myisam pack format
  len = 5 or 6: microseconds = 3-bytes val in myisam pack format
```


#### `<code>MYSQL_TYPE_DATE</code>`


Stored as a 3 byte value where bits 1 to 5 store the day, bits 6 to 9 store the month and the remaining bits store the year.


#### `<code>MYSQL_TYPE_TIMESTAMP</code>`


Stored as a 4 byte UNIX timestamp (number of seconds since 00:00, Jan 1 1970 UTC).


#### Example From mysqlbinlog Utility, CRC32


```
# at 1680
#180611  9:50:51 server id 1  end_log_pos 1754 CRC32 0x5415a8fb 	Write_rows: table id 23 flags: STMT_END_F

BINLOG '
2ykeWxMBAAAAPgAAAJAGAAAAABcAAAAAAAEABHRlc3QACWJ1bGtfbnVsbAAFDwMFE/YGFAAIAAMB
H1bULg8=
2ykeWxcBAAAASgAAANoGAAAAABcAAAAAAAEABf/gATMDAAAAAAAAAAAACECAAACDAP/gATMDAAAA
AAAAAAAACECAAACDAPuoFVQ=
'/*!*/;
```


#### Example Event As It's Written In The Binlog File


```
db 29 1e 5b 17 01 00 00 00 4a 00       .).[.....J.
00 00 da 06 00 00 00 00 17 00 00 00 00 00 01 00  ................
05 ff e0 01 33 03 00 00 00 00 00 00 00 00 00 08  ....3...........
40 80 00 00 83 00 ff e0 01 33 03 00 00 00 00 00  @........3......
00 00 00 00 08 40 80 00 00 83 00 fb a8 15 54     .....@........T                                   ....
```

