
# _rowid

## Syntax


_rowid


## Description


The `<code>_rowid</code>` pseudo column is mapped to the primary key in the related table. This can be used as a replacement of the `<code>rowid</code>` pseudo column in other databases. Another usage is to simplify sql queries as one doesn't have to know the name of the primary key.


## Examples


```
create table t1 (a int primary key, b varchar(80));
insert into t1 values (1,"one"),(2,"two");
select * from t1 where _rowid=1;
```

```
+---+------+
| a | b    |
+---+------+
| 1 | one  |
+---+------+
```

```
update t1 set b="three" where _rowid=2;
select * from t1 where _rowid>=1 and _rowid<=10;
```

```
+---+-------+
| a | b     |
+---+-------+
| 1 | one   |
| 2 | three |
+---+-------+
```
