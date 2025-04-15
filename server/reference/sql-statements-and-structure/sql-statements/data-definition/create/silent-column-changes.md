
# Silent Column Changes

When a [CREATE TABLE](../../../vectors/create-table-with-vectors.md) or [ALTER TABLE](../alter/alter-tablespace.md) command is issued, MariaDB will silently change a column specification in the following cases:


* [PRIMARY KEY](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/optimization-and-indexes/getting-started-with-indexes.md#primary-key) columns are always NOT NULL.
* Any trailing spaces from [SET](../../../../data-types/string-data-types/set-data-type.md) and [ENUM](../../../../data-types/string-data-types/enum.md) values are discarded.
* [TIMESTAMP](../../built-in-functions/date-time-functions/timestamp-function.md) columns are always NOT NULL, and display sizes are discarded
* A row-size limit of 65535 bytes applies
* If [strict SQL mode](../../../../../server-management/variables-and-modes/sql-mode.md#strict-mode) is not enabled (it is enabled by default from [MariaDB 10.2](../../../../../../release-notes/mariadb-community-server/what-is-mariadb-102.md)), a [VARCHAR](../../../../data-types/string-data-types/varchar.md) column longer than 65535 become [TEXT](../../../../data-types/string-data-types/text.md), and a [VARBINARY](../../../../data-types/string-data-types/varbinary.md) columns longer than 65535 becomes a [BLOB](../../../../data-types/string-data-types/blob.md). If strict mode is enabled the silent changes will not be made, and an error will occur.
* If a USING clause specifies an index that's not permitted by the storage engine, the engine will instead use another available index type that can be applied without affecting results.
* If the CHARACTER SET binary attribute is specified, the column is created as the matching binary data type. A TEXT becomes a BLOB, CHAR a BINARY and VARCHAR a VARBINARY. ENUMs and SETs are created as defined.


To ease imports from other RDBMSs, MariaDB will also silently map the following data types:



| Other Vendor Type | MariaDB Type |
| --- | --- |
| Other Vendor Type | MariaDB Type |
| BOOL | [TINYINT](../../../../data-types/data-types-numeric-data-types/tinyint.md) |
| BOOLEAN | [TINYINT](../../../../data-types/data-types-numeric-data-types/tinyint.md) |
| CHARACTER VARYING(M) | [VARCHAR](../../../../data-types/string-data-types/varchar.md)(M) |
| FIXED | [DECIMAL](../../../../data-types/data-types-numeric-data-types/decimal.md) |
| FLOAT4 | [FLOAT](../../../../data-types/data-types-numeric-data-types/float.md) |
| FLOAT8 | [DOUBLE](../../../../data-types/data-types-numeric-data-types/double.md) |
| INT1 | [TINYINT](../../../../data-types/data-types-numeric-data-types/tinyint.md) |
| INT2 | [SMALLINT](../../../../data-types/data-types-numeric-data-types/smallint.md) |
| INT3 | [MEDIUMINT](../../../../data-types/data-types-numeric-data-types/mediumint.md) |
| INT4 | [INT](../../../../../../general-resources/learning-and-training/video-presentations-and-screencasts/interviews-related-to-mariadb.md) |
| INT8 | [BIGINT](../../../../data-types/data-types-numeric-data-types/bigint.md) |
| LONG VARBINARY | [MEDIUMBLOB](../../../../data-types/string-data-types/mediumblob.md) |
| LONG VARCHAR | [MEDIUMTEXT](../../../../data-types/string-data-types/mediumtext.md) |
| LONG | [MEDIUMTEXT](../../../../data-types/string-data-types/mediumtext.md) |
| MIDDLEINT | [MEDIUMINT](../../../../data-types/data-types-numeric-data-types/mediumint.md) |
| NUMERIC | [DECIMAL](../../../../data-types/data-types-numeric-data-types/decimal.md) |



Currently, all MySQL types are supported in MariaDB.


For type mapping between Cassandra and MariaDB, see [Cassandra storage engine](../../../../storage-engines/legacy-storage-engines/cassandra/cassandra-storage-engine-issues.md#datatypes).


## Example


Silent changes in action:


```
CREATE TABLE SilenceIsGolden
   (
    f1 TEXT CHARACTER SET binary,
    f2 VARCHAR(15) CHARACTER SET binary,
    f3 CHAR CHARACTER SET binary,
    f4 ENUM('x','y','z') CHARACTER SET binary,
    f5 VARCHAR (65536),
    f6 VARBINARY (65536),
    f7 INT1
   );
Query OK, 0 rows affected, 2 warnings (0.31 sec)

SHOW WARNINGS;
+-------+------+-----------------------------------------------+
| Level | Code | Message                                       |
+-------+------+-----------------------------------------------+
| Note  | 1246 | Converting column 'f5' from VARCHAR to TEXT   |
| Note  | 1246 | Converting column 'f6' from VARBINARY to BLOB |
+-------+------+-----------------------------------------------+

DESCRIBE SilenceIsGolden;
+-------+-------------------+------+-----+---------+-------+
| Field | Type              | Null | Key | Default | Extra |
+-------+-------------------+------+-----+---------+-------+
| f1    | blob              | YES  |     | NULL    |       |
| f2    | varbinary(15)     | YES  |     | NULL    |       |
| f3    | binary(1)         | YES  |     | NULL    |       |
| f4    | enum('x','y','z') | YES  |     | NULL    |       |
| f5    | mediumtext        | YES  |     | NULL    |       |
| f6    | mediumblob        | YES  |     | NULL    |       |
| f7    | tinyint(4)        | YES  |     | NULL    |       |
+-------+-------------------+------+-----+---------+-------+
```
