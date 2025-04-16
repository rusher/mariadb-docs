
# INT8

`INT8` is a synonym for [BIGINT](bigint.md).


```
CREATE TABLE t1 (x INT8);

DESC t1;
+-------+------------+------+-----+---------+-------+
| Field | Type       | Null | Key | Default | Extra |
+-------+------------+------+-----+---------+-------+
| x     | bigint(20) | YES  |     | NULL    |       |
+-------+------------+------+-----+---------+-------+
```

## EXAMPLES


```
CREATE TABLE int8_example (
  example INT8
);
```

```
SHOW CREATE TABLE int8_example\G

*************************** 1. row ***************************
       Table: int8_example
Create Table: CREATE TABLE `int8_example` (
  `example` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1
```
