# PACKET_BINDATA

In contrast to the text protocol, the binary protocol transfers the data according to the format of the field types returned in PACKET_METADATA.

| Field type | Representation |
| --- | --- |
| Field type | Representation |
| MYSQL_TYPE_BIT | str_LEC |
| MYSQL_TYPE_BLOB | str_LEC |
| MYSQL_TYPE_DATE MYSQL_TYPE_DATETIME MYSQL_TYPE_TIMESTAMP | int_11 (default)int_7 (no microseconds)int_4 (no time values)int_0 (no values) |
| MYSQL_TYPE_DECIMAL | str_LEC |
| MYSQL_TYPE_DOUBLE | int_8 |
| MYSQL_TYPE_ENUM | str_LEC |
| MYSQL_TYPE_FLOAT | int_4 |
| MYSQL_TYPE_GEOMETRY | str_LEC |
| MYSQL_TYPE_INT24 | int_4 |
| MYSQL_TYPE_JSON | str_LEC |
| MYSQL_TYPE_LONGLONG | int_8 |
| MYSQL_TYPE_LONG_BLOB | str_LEC |
| MYSQL_TYPE_LONG | int_4 |
| MYSQL_TYPE_MEDIUM_BLOB | str_LEC |
| MYSQL_TYPE_NEWDECIMAL | str_LEC |
| MYSQL_TYPE_NULL | stored in bitmap |
| MYSQL_TYPE_SET | str_LEC |
| MYSQL_TYPE_STRING | str_LEC |
| MYSQL_TYPE_SHORT | int_2 |
| MYSQL_TYPE_TINY_BLOB | str_LEC |
| MYSQL_TYPE_TINY | int_1 |
| MYSQL_TYPE_VARCHAR | str_LEC |
| MYSQL_TYPE_VAR_STRING | str_LEC |
| MYSQL_TYPE_YEAR | int_4 |

#

### Fields

```
(column_count + 7)/8 null bitmap
while (!eof) {
 for (i=0; i < column_count; i++)
 {
 data (length depends on the data type)
 }
}
```