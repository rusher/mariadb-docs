
# INT2

`INT2` is a synonym for [SMALLINT](smallint.md).


```
CREATE TABLE t1 (x INT2);

DESC t1;
+-------+-------------+------+-----+---------+-------+
| Field | Type        | Null | Key | Default | Extra |
+-------+-------------+------+-----+---------+-------+
| x     | smallint(6) | YES  |     | NULL    |       |
+-------+-------------+------+-----+---------+-------+
```

## EXAMPLES


```
CREATE TABLE int2_example (
  example INT2
);
```

```
SHOW CREATE TABLE int2_example\G

*************************** 1. row ***************************
       Table: int2_example
Create Table: CREATE TABLE `int2_example` (
  `example` smallint(6) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1
```


CC BY-SA / Gnu FDL


{% @marketo/form formId="4316" %}
