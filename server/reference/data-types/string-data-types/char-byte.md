
# CHAR BYTE

## Description


The `CHAR BYTE` data type is an alias for the 
`[BINARY](../../storage-engines/innodb/binary-log-group-commit-and-innodb-flushing-performance.md)` data type. This is a
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
