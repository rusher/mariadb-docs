
# CHAR BYTE

## Description


The `<code>CHAR BYTE</code>` data type is an alias for the 
`<code>[BINARY](../../storage-engines/innodb/binary-log-group-commit-and-innodb-flushing-performance.md)</code>` data type. This is a
compatibility feature.


## EXAMPLES


```
CREATE TABLE char_byte_example (
  example CHAR BYTE
);
```

```
SHOW CREATE TABLE char_byte_example\G
```

```
*************************** 1. row ***************************
       Table: char_byte_example
Create Table: CREATE TABLE `char_byte_example` (
  `example` binary(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1
```
