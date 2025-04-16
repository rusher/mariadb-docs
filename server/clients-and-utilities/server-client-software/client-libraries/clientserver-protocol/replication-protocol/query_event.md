
# QUERY_EVENT

This event is written into the binary log file for:


* STATEMENT based replication (updating statements)
* DDLs
* COMMIT related to non transactional engines ([MyISAM](../../../../../reference/storage-engines/myisam-storage-engine/myisam-system-variables.md), [BLACKHOLE](../../../../../reference/storage-engines/blackhole.md) etc)


### Header


* Event Type = 0x02


### Fields


Fixed data part:



* [uint<4>](../protocol-data-types.md#fixed-length-integers) The ID of the thread that issued this statement on the master.
* [uint<4>](../protocol-data-types.md#fixed-length-integers) The time in seconds that the statement took to execute.
* [uint<1>](../protocol-data-types.md#fixed-length-integers) The length of the name of the database which was the default database when the statement was executed. This name appears later, in the variable data part. It is necessary for statements such as INSERT INTO t VALUES(1) that don't specify the database and rely on the default database previously selected by USE.
* [uint<2>](../protocol-data-types.md#fixed-length-integers) The error code resulting from execution of the statement on the master.
* [uint<2>](../protocol-data-types.md#fixed-length-integers) The length of the status variable block.



Variable data part:


* [byte<n>](../protocol-data-types.md#fixed-length-bytes) Zero or more status variables. Each status variable consists of one byte code identifying the variable stored, followed by the value of the variable. The format of the value is variable-specific.
The number of bytes 'n' is the length of the status variable block (read in fixed data part)
* [string<NUL>](../protocol-data-types.md#fixed-length-bytes) The default database name (null-terminated).
* [string<EOF>](../protocol-data-types.md#fixed-length-bytes) The SQL statement. By subtraction the size of the statement can be known.


#### Status variables


**Q_FLAGS2_CODE** (0x00):


* [uint<4>](../protocol-data-types.md#fixed-length-integers) bitmask



|   |   |
| --- | --- |
| Value | Option |
| 0x00004000 | OPTION_AUTO_IS_NULL |
| 0x00080000 | OPTION_NOT_AUTOCOMMIT |
| 0x04000000 | OPTION_NO_FOREIGN_KEY_CHECKS |
| 0x08000000 | OPTION_RELAXED_UNIQUE_CHECKS |



**Q_SQL_MODE_CODE** (0x01):


* [uint<8>](../protocol-data-types.md#fixed-length-integers) 8-byte bitmask



|   |   |
| --- | --- |
| Value | SQL_MODE |
| 0x00000001 | MODE_REAL_AS_FLOAT |
| 0x00000002 | MODE_PIPES_AS_CONCAT |
| 0x00000004 | MODE_ANSI_QUOTES |
| 0x00000008 | MODE_IGNORE_SPACE |
| 0x00000010 | MODE_NOT_USED |
| 0x00000020 | MODE_ONLY_FULL_GROUP_BY |
| 0x00000040 | MODE_NO_UNSIGNED_SUBTRACTION |
| 0x00000080 | MODE_NO_DIR_IN_CREATE |
| 0x00000100 | MODE_POSTGRESQL |
| 0x00000200 | MODE_ORACLE |
| 0x00000400 | MODE_MSSQL |
| 0x00000800 | MODE_DB2 |
| 0x00001000 | MODE_MAXDB |
| 0x00002000 | MODE_NO_KEY_OPTIONS |
| 0x00004000 | MODE_NO_TABLE_OPTIONS |
| 0x00008000 | MODE_NO_FIELD_OPTIONS |
| 0x00010000 | MODE_MYSQL323 |
| 0x00020000 | MODE_MYSQL40 |
| 0x00040000 | MODE_ANSI |
| 0x00080000 | MODE_NO_AUTO_VALUE_ON_ZERO |
| 0x00100000 | MODE_NO_BACKSLASH_ESCAPES |
| 0x00200000 | MODE_STRICT_TRANS_TABLES |
| 0x00400000 | MODE_STRICT_ALL_TABLES |
| 0x00800000 | MODE_NO_ZERO_IN_DATE |
| 0x01000000 | MODE_NO_ZERO_DATE |
| 0x02000000 | MODE_INVALID_DATES |
| 0x04000000 | MODE_ERROR_FOR_DIVISION_BY_ZERO |
| 0x08000000 | MODE_TRADITIONAL |
| 0x10000000 | MODE_NO_AUTO_CREATE_USER |
| 0x20000000 | MODE_HIGH_NOT_PRECEDENCE |
| 0x40000000 | MODE_NO_ENGINE_SUBSTITUTION |
| 0x80000000 | MODE_PAD_CHAR_TO_FULL_LENGTH |



**Q_CATALOG_NZ_CODE** (0x02):


* [uint<1>](../protocol-data-types.md#fixed-length-integers) length
* [string<length +1>](../protocol-data-types.md#fixed-length-bytes) catalog name + '\0'


**Q_AUTO_INCREMENT** (0x03):


* [uint<2>](../protocol-data-types.md#fixed-length-integers) auto_increment increment
* [uint<2>](../protocol-data-types.md#fixed-length-integers) auto_increment offset


**Q_CHARSET_CODE** (0x04):


* [uint<2>](../protocol-data-types.md#fixed-length-integers) client character set
* [uint<2>](../protocol-data-types.md#fixed-length-integers) collation_connection
* [uint<2>](../protocol-data-types.md#fixed-length-integers) collation_server


**Q_TIMEZONE_CODE** (0x05):


* [uint<1>](../protocol-data-types.md#fixed-length-integers) length
* [string<length>](../protocol-data-types.md#fixed-length-bytes) time zone


**Q_CATALOG_NZ_CODE** (0x06):


* [uint<1>](../protocol-data-types.md#fixed-length-integers) length
* [string<length>](../protocol-data-types.md#fixed-length-bytes) catalog


**Q_LC_TIME_NAMES_CODE** (0x07):


* [uint<2>](../protocol-data-types.md#fixed-length-integers) code
The mapping between code and names are defined in sql_locale.cc.


**Q_CHARSET_DATABASE_CODE** (0x08)


* [uint<2>](../protocol-data-types.md#fixed-length-integers) database collation


**Q_TABLE_MAP_FOR_UPDATE_CODE** (0x09)


* [uint<8>](../protocol-data-types.md#fixed-length-integers) table bittmask
Every bit of this variable represents a table, and is set to 1 if the corresponding table is to be updated by this statement.


**Q_MASTER_DATA_WRITTEN_CODE** (0x0A): #not in use anymore


* [uint<4>](../protocol-data-types.md#fixed-length-integers) original event length


**Q_INVOKER** (0x0B|):


* [uint<1>](../protocol-data-types.md#fixed-length-integers) user name length
* [string<length>](../protocol-data-types.md#fixed-length-bytes) user name
* [uint<1>](../protocol-data-types.md#fixed-length-integers) host name length
* [string<length>](../protocol-data-types.md#fixed-length-bytes) host name


**Q_UPDATED_DB_NAMES** (0x0C): MySQL only


* [uint<1>](../protocol-data-types.md#fixed-length-integers) count
* for (i=0;i < count; i++)

  * [string<NULL>](../protocol-data-types.md#fixed-length-bytes) Null terminated database name


**Q_MICROSECONDS** (0x0D): MySQL only


* [uint<3>](../protocol-data-types.md#fixed-length-integers) microsecond part


**Q_HRNOW** (0x80): MariaDB only


* [uint<3>](../protocol-data-types.md#fixed-length-integers) microsecond part


**Q_XID** (0x81): MariaDB only


* [uint<8>](../protocol-data-types.md#fixed-length-integers) xid


### Example With CRC32


```
71 17 28 5a 02 8c 27 00  00 55 00 00 00 01 09 00  q.(Z..'..U......
00 00 00 66 01 00 00 00  00 00 00 00 00 00 1a 00  ...f............
00 00 00 00 00 01 00 00  00 50 00 00 00 00 06 03  .........P......
73 74 64 04 08 00 08 00  08 00 00 54 52 55 4e 43  std........TRUNC
41 54 45 20 54 41 42 4c  45 20 74 65 73 74 2e 74  ATE TABLE test.t
34 4a 69 9e ed                                    4Ji..
```


### Header, 19 Bytes


* Event Time[4] = 71 17 28 5a ===> 1512576881
* Event Type[1] = 2
* Server_id[4] = 8c 27 00 00 ===> 10124
* Event Size = 55 00 00 00 ===> 85
* Next Pos = 01 09 00 00 ===> 2305
* Flags = 00 00 => 0


### Content, Variable Data


* Thread ID[4] = 66 01 00 00 ===> 358
* Execution Time[4] = 00 00 00 00 => 0 seconds
* Statement default database name len[1] = 00 => 0 (no default db)
* Error code[2] = 00 00 => 0 (no errors)
* Status variable block len[2] = 1a 00 => 26
* Status variables[n] = 00 ... 08 00
* The default database[string<NUL>] = 00 = 0 (no default db)
* The SQL statement[string<EOF>] = TRUNCATE TABLE test.t4


### CRC32, 4 Bytes


* 4a 69 9e ed


### Example With Default db and CRC32


```
MariaDB []> use test;
Database changed
MariaDB [test]> TRUNCATE TABLE t4;
...

ce 22 28 5a 02 8c 27 00  00 54 00 00 00 87 0c 00  ."(Z..'..T......
00 00 00 66 01 00 00 01  00 00 00 04 00 00 1a 00  ...f............
00 00 00 00 00 01 00 00  00 50 00 00 00 00 06 03  .........P......
73 74 64 04 08 00 08 00  08 00 74 65 73 74 00 54  std.......test.T
52 55 4e 43 41 54 45 20  54 41 42 4c 45 20 74 34  RUNCATE TABLE t4
08 f1 09 16                                       ....
```


### Content, Variable Data


* Thread ID[4] = 66 01 00 00 ===> 358
* Execution Time[4] = 10 00 00 00 => 1 second
* Statement default database name len[1] = 04 => 4 (default db is "test")
* Error code[2] = 00 00 => 0 (no errors)
* Status variable block len[2] = 1a 00 => 26
* Status variables[n] = 00 ... 08 00
* The default database[string<NUL>] = 74 65 73 74 00 =>test
* The SQL statement[string<EOF>] = TRUNCATE TABLE test.t4

<span></span>
