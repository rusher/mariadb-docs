
# MAKETIME

## Syntax


```
MAKETIME(hour,minute,second)
```

## Description


Returns a time value calculated from the `<code>hour</code>`, `<code>minute</code>`, and `<code>second</code>` arguments.


If `<code>minute</code>` or `<code>second</code>` are out of the range 0 to 60, NULL is returned. The `<code>hour</code>` can be in the range -838 to 838, outside of which the value is truncated with a warning.


## Examples


```
SELECT MAKETIME(13,57,33);
+--------------------+
| MAKETIME(13,57,33) |
+--------------------+
| 13:57:33           |
+--------------------+

SELECT MAKETIME(-13,57,33);
+---------------------+
| MAKETIME(-13,57,33) |
+---------------------+
| -13:57:33           |
+---------------------+

SELECT MAKETIME(13,67,33);
+--------------------+
| MAKETIME(13,67,33) |
+--------------------+
| NULL               |
+--------------------+

SELECT MAKETIME(-1000,57,33);
+-----------------------+
| MAKETIME(-1000,57,33) |
+-----------------------+
| -838:59:59            |
+-----------------------+
1 row in set, 1 warning (0.00 sec)

SHOW WARNINGS;
+---------+------+-----------------------------------------------+
| Level   | Code | Message                                       |
+---------+------+-----------------------------------------------+
| Warning | 1292 | Truncated incorrect time value: '-1000:57:33' |
+---------+------+-----------------------------------------------+
```
