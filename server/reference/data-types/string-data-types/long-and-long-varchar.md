
# LONG and LONG VARCHAR

`LONG` and `LONG VARCHAR` are synonyms for [MEDIUMTEXT](mediumtext.md).


```
CREATE TABLE t1 (a LONG, b LONG VARCHAR);

DESC t1;
+-------+------------+------+-----+---------+-------+
| Field | Type       | Null | Key | Default | Extra |
+-------+------------+------+-----+---------+-------+
| a     | mediumtext | YES  |     | NULL    |       |
| b     | mediumtext | YES  |     | NULL    |       |
+-------+------------+------+-----+---------+-------+
```


CC BY-SA / Gnu FDL

