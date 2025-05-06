
# SLEEP

## Syntax


```
SLEEP(duration)
```

## Description


Sleeps (pauses) for the number of seconds given by the duration argument, then
returns `0`. If `SLEEP()` is interrupted, it
returns `1`. The duration may have a fractional part given in
microseconds.


Statements using the SLEEP() function are not [safe for statement-based replication](../../../../../../server-usage/replication-cluster-multi-master/standard-replication/unsafe-statements-for-statement-based-replication.md).


## Example


```
SELECT SLEEP(5.5);
+------------+
| SLEEP(5.5) |
+------------+
|          0 |
+------------+
1 row in set (5.50 sec)
```


GPLv2 fill_help_tables.sql

