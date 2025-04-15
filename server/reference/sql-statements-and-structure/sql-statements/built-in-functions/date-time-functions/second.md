
# SECOND

## Syntax


```
SECOND(time)
```

## Description


Returns the second for a given `<code>time</code>` (which can include [microseconds](microseconds-in-mariadb.md)), in the range 0 to 59, or `<code>NULL</code>` if not given a valid time value.


## Examples


```
SELECT SECOND('10:05:03');
+--------------------+
| SECOND('10:05:03') |
+--------------------+
|                  3 |
+--------------------+

SELECT SECOND('10:05:01.999999');
+---------------------------+
| SECOND('10:05:01.999999') |
+---------------------------+
|                         1 |
+---------------------------+
```
