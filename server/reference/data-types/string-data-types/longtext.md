
# LONGTEXT


## Syntax


```
LONGTEXT [CHARACTER SET charset_name] [COLLATE collation_name]
```

## Description


A [TEXT](text.md) column with a maximum length of 4,294,967,295 or 4GB (`2<sup>32</sup> - 1`) characters. The effective maximum length is less if the value contains multi-byte characters. The effective maximum length of LONGTEXT columns also depends on the configured maximum packet size in the client/server protocol and available memory. Each LONGTEXT value is stored using a four-byte length prefix that indicates the number of bytes in the value.


JSON is an alias for LONGTEXT. See [JSON Data Type](../../storage-engines/connect/json-sample-files.md) for details.


## Oracle Mode


In [Oracle mode](../../../../release-notes/mariadb-community-server/compatibility-and-differences/sql_modeoracle.md), [CLOB](https://mariadb.com/kb/en/clob/) is a synonym for `LONGTEXT`.


## EXAMPLES


### LONGTEXT


Example of LONGTEXT:


```
CREATE TABLE longtext_example (
   description VARCHAR(20),
   example LONGTEXT
) DEFAULT CHARSET=latin1; -- One byte per char makes the examples clearer
```


#### Note:

The maximum size of a `LONGTEXT` is so large that it cannot be sent to the server without breaking the value up into chunks (something that the command-line client cannot do). For values larger than `16M`, you can increase the `max_allowed_packet` size up to a maximum of `1024M` to increase the allowed size of non-chunked values.


```
INSERT INTO longtext_example VALUES
   ('Normal foo', 'foo'),
   ('Trailing spaces foo', 'foo      '),
   ('NULLed', NULL),
   ('Empty', ''),
   ('Maximum', RPAD('', 4294967295, 'x'));
```

```
ERROR 1301 (HY000): Result of rpad() was larger than max_allowed_packet (16777216) - truncated
```

### Data Too Long


When SQL_MODE is strict (the default) a value is considered "too long" when its length exceeds the size of the data type, and an error is generated.


Example of data too long behavior for LONGTEXT:


```
TRUNCATE longtext_example;

INSERT INTO longtext_example VALUES
   ('Overflow', RPAD('', 4294967296, 'x'));
```

```
ERROR 1301 (HY000): Result of rpad() was larger than max_allowed_packet (16777216) - truncated
```

## See Also


* [TEXT](text.md)
* [BLOB and TEXT Data Types](blob-and-text-data-types.md)
* [Data Type Storage Requirements](../data-type-storage-requirements.md)
* [JSON Data Type](../../storage-engines/connect/json-sample-files.md)
* [Oracle mode from MariaDB 10.3](../../../../release-notes/mariadb-community-server/compatibility-and-differences/sql_modeoracle.md)

