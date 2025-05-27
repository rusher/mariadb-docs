
# MINUTE

## Syntax


```
MINUTE(time)
```

## Description


Returns the minute for *time*, in the range 0 to 59.


## Examples


```
SELECT MINUTE('2013-08-03 11:04:03');
+-------------------------------+
| MINUTE('2013-08-03 11:04:03') |
+-------------------------------+
|                             4 |
+-------------------------------+

 SELECT MINUTE ('23:12:50');
+---------------------+
| MINUTE ('23:12:50') |
+---------------------+
|                  12 |
+---------------------+
```


GPLv2 fill_help_tables.sql

