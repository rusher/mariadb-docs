
# ASIN

## Syntax


```
ASIN(X)
```


## Description


Returns the arc sine of X, that is, the value whose sine is X. Returns
NULL if X is not in the range -1 to 1.


## Examples


```
SELECT ASIN(0.2);
+--------------------+
| ASIN(0.2)          |
+--------------------+
| 0.2013579207903308 |
+--------------------+

SELECT ASIN('foo');
+-------------+
| ASIN('foo') |
+-------------+
|           0 |
+-------------+

SHOW WARNINGS;
+---------+------+-----------------------------------------+
| Level   | Code | Message                                 |
+---------+------+-----------------------------------------+
| Warning | 1292 | Truncated incorrect DOUBLE value: 'foo' |
+---------+------+-----------------------------------------+
```


GPLv2 fill_help_tables.sql


{% @marketo/form formId="4316" %}
