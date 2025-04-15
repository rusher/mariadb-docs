
# IF Function

## Syntax


```
IF(expr1,expr2,expr3)
```


## Description


If `<code>expr1</code>` is `<code>TRUE</code>` (`<code>expr1 <> 0</code>` and `<code>expr1 <> NULL</code>`) then `<code>IF()</code>`
returns `<code>expr2</code>`; otherwise it returns `<code>expr3</code>`. `<code>IF()</code>` returns a numeric
or string value, depending on the context in which it is used.


**Note:** There is also an [IF statement](ifnull.md) which differs from the
`<code>IF()</code>` function described here.


## Examples


```
SELECT IF(1>2,2,3);
+-------------+
| IF(1>2,2,3) |
+-------------+
|           3 |
+-------------+
```

```
SELECT IF(1<2,'yes','no');
+--------------------+
| IF(1<2,'yes','no') |
+--------------------+
| yes                |
+--------------------+
```

```
SELECT IF(STRCMP('test','test1'),'no','yes');
+---------------------------------------+
| IF(STRCMP('test','test1'),'no','yes') |
+---------------------------------------+
| no                                    |
+---------------------------------------+
```

## See Also


There is also an [IF statement](ifnull.md), which differs from the `<code>IF()</code>` function described above.

