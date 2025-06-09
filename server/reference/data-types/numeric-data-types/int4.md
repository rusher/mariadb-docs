
# INT4

`INT4` is a synonym for [INT](int.md).


```
CREATE TABLE t1 (x INT4);

DESC t1;
+-------+---------+------+-----+---------+-------+
| Field | Type    | Null | Key | Default | Extra |
+-------+---------+------+-----+---------+-------+
| x     | int(11) | YES  |     | NULL    |       |
+-------+---------+------+-----+---------+-------+
```

## EXAMPLES


```
CREATE TABLE int4_example (
  example INT4
);
```

```
SHOW CREATE TABLE int4_example\G

*************************** 1. row ***************************
       Table: int4_example
Create Table: CREATE TABLE `int4_example` (
  `example` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1
```


CC BY-SA / Gnu FDL


{% @marketo/form formId="4316" %}
