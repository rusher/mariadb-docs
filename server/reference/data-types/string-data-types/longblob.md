
# LONGBLOB


## Syntax


```
LONGBLOB
```

## Description


A [BLOB](blob.md) column with a 
maximum length of 4,294,967,295 bytes or 4GB (232 - 1). The effective maximum length of LONGBLOB columns depends on the
configured maximum packet size in the client/server protocol and
available memory. Each LONGBLOB value is stored using a four-byte
length prefix that indicates the number of bytes in the value.


### Oracle Mode


In [Oracle mode](../../../../release-notes/mariadb-community-server/compatibility-and-differences/sql_modeoracle.md), `<code>BLOB</code>` is a synonym for `<code>LONGBLOB</code>`.


## EXAMPLES


### LONGBLOB


Example of LONGBLOB:


```
CREATE TABLE longblob_example (
   description VARCHAR(20),
   example LONGBLOB
) DEFAULT CHARSET=latin1; -- One byte per char makes the examples clearer
```

Note that the maximum size of a LONGBLOB is so large that it cannot be sent to the server without breaking the value up into chunks (something that the command-line client cannot do). For values larger than 16M you can increase the max_allowed_packet size up to a maximum of 1024M to increase the allowed size of non-chunked values.


```
INSERT INTO longblob_example VALUES
   ('Normal foo', 'foo'),
   ('Trailing spaces foo', 'foo      '),
   ('NULLed', NULL),
   ('Empty', ''),
   ('Maximum', RPAD('', 4294967295, CHAR(7)));
```

```
ERROR 1301 (HY000): Result of rpad() was larger than max_allowed_packet (16777216) - truncated
```

### Data Too Long


When SQL_MODE is strict (the default) a value is considered "too long" when its length exceeds the size of the data type, and an error is generated.


Example of data too long behavior for LONGBLOB:


```
TRUNCATE longblob_example;

INSERT INTO longblob_example VALUES
   ('Overflow', RPAD('', 4294967296, CHAR(7)));
```

```
ERROR 1301 (HY000): Result of rpad() was larger than max_allowed_packet (16777216) - truncated
```

## See Also


* [BLOB](blob.md)
* [BLOB and TEXT Data Types](blob-and-text-data-types.md)
* [Data Type Storage Requirements](../data-type-storage-requirements.md)
* [Oracle mode from MariaDB 10.3](../../../../release-notes/mariadb-community-server/compatibility-and-differences/sql_modeoracle.md)

