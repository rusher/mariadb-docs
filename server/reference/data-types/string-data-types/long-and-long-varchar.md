
# LONG and LONG VARCHAR

`<code>LONG</code>` and `<code>LONG VARCHAR</code>` are synonyms for [MEDIUMTEXT](mediumtext.md).


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
