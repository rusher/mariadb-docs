
# TINYTEXT


## Syntax


```
TINYTEXT [CHARACTER SET charset_name] [COLLATE collation_name]
```

## Description


A [TEXT](text.md) column with a maximum length of 255 (`28 - 1`) characters. The effective maximum length is less if the value contains multi-byte characters. Each TINYTEXT value is stored using a one-byte length prefix that indicates the number of bytes in the value.


## EXAMPLES


### TINYTEXT


Example of TINYTEXT:


```
CREATE TABLE tinytext_example (
   description VARCHAR(20),
   example TINYTEXT
) DEFAULT CHARSET=latin1; -- One byte per char makes the examples clearer
```

```
INSERT INTO tinytext_example VALUES
   ('Normal foo', 'foo'),
   ('Trailing spaces foo', 'foo      '),
   ('NULLed', NULL),
   ('Empty', ''),
   ('Maximum', RPAD('', 255, 'x'));
```

```
SELECT description, LENGTH(example) AS length
   FROM tinytext_example;
```

```
+---------------------+--------+
| description         | length |
+---------------------+--------+
| Normal foo          |      3 |
| Trailing spaces foo |      9 |
| NULLed              |   NULL |
| Empty               |      0 |
| Maximum             |    255 |
+---------------------+--------+
```

### Data Too Long


When SQL_MODE is strict (the default) a value is considered "too long" when its length exceeds the size of the data type, and an error is generated.


Example of data too long behavior for TINYTEXT:


```
TRUNCATE tinytext_example;

INSERT INTO tinytext_example VALUES
   ('Overflow', RPAD('', 256, 'x'));
```

```
ERROR 1406 (22001): Data too long for column 'example' at row 1
```

## See Also


* [TEXT](text.md)
* [BLOB and TEXT Data Types](blob-and-text-data-types.md)
* [Data Type Storage Requirements](../data-type-storage-requirements.md)


GPLv2 fill_help_tables.sql


{% @marketo/form formId="4316" %}
