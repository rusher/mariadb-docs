
# INT1

`INT1` is a synonym for [TINYINT](tinyint.md).


```
CREATE TABLE t1 (x INT1);

DESC t1;
+-------+------------+------+-----+---------+-------+
| Field | Type       | Null | Key | Default | Extra |
+-------+------------+------+-----+---------+-------+
| x     | tinyint(4) | YES  |     | NULL    |       |
+-------+------------+------+-----+---------+-------+
```

## EXAMPLES


```
CREATE TABLE int1_example (
  example INT1
);
```

```
SHOW CREATE TABLE int1_example\G
```

```
*************************** 1. row ***************************
       Table: int1_example
Create Table: CREATE TABLE `int1_example` (
  `example` tinyint(4) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1
```


CC BY-SA / Gnu FDL

