
# INT3

`<code>INT3</code>` is a synonym for [MEDIUMINT](mediumint.md).


```
CREATE TABLE t1 (x INT3);

DESC t1;
+-------+--------------+------+-----+---------+-------+
| Field | Type         | Null | Key | Default | Extra |
+-------+--------------+------+-----+---------+-------+
| x     | mediumint(9) | YES  |     | NULL    |       |
+-------+--------------+------+-----+---------+-------+
```

## EXAMPLES


```
CREATE TABLE int3_example (
  example INT3
);
```

```
SHOW CREATE TABLE int3_example\G

*************************** 1. row ***************************
       Table: int3_example
Create Table: CREATE TABLE `int3_example` (
  `example` mediumint(9) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1
```
