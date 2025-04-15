
# ACOS

## Syntax


```
ACOS(X)
```


## Description


Returns the arc cosine of `<code>X</code>`, that is, the value whose cosine is `<code>X</code>`.
Returns `<code>NULL</code>` if `<code>X</code>` is not in the range `<code>-1</code>` to `<code>1</code>`.


## Examples


```
SELECT ACOS(1);
+---------+
| ACOS(1) |
+---------+
|       0 |
+---------+

SELECT ACOS(1.0001);
+--------------+
| ACOS(1.0001) |
+--------------+
|         NULL |
+--------------+

SELECT ACOS(0);
+-----------------+
| ACOS(0)         |
+-----------------+
| 1.5707963267949 |
+-----------------+

SELECT ACOS(0.234);
+------------------+
| ACOS(0.234)      |
+------------------+
| 1.33460644244679 |
+------------------+
```
