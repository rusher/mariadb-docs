
# ISNULL

## Syntax


```
ISNULL(expr)
```

## Description


If *`expr`* is NULL, ISNULL() returns 1, otherwise it returns 0.


See also [NULL Values in MariaDB](../../../data-types/null-values.md).


## Examples


```
SELECT ISNULL(1+1);
+-------------+
| ISNULL(1+1) |
+-------------+
|           0 |
+-------------+

SELECT ISNULL(1/0);
+-------------+
| ISNULL(1/0) |
+-------------+
|           1 |
+-------------+
```


GPLv2 fill_help_tables.sql


{% @marketo/form formId="4316" %}
