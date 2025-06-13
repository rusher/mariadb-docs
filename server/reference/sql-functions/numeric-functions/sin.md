
# SIN

## Syntax


```
SIN(X)
```

## Description


Returns the sine of X, where X is given in radians.


## Examples


```
SELECT SIN(1.5707963267948966);
+-------------------------+
| SIN(1.5707963267948966) |
+-------------------------+
|                       1 |
+-------------------------+

SELECT SIN(PI());
+----------------------+
| SIN(PI())            |
+----------------------+
| 1.22460635382238e-16 |
+----------------------+

SELECT ROUND(SIN(PI()));
+------------------+
| ROUND(SIN(PI())) |
+------------------+
|                0 |
+------------------+
```


<sub>_This page is licensed: GPLv2, originally from [fill\_help\_tables.sql](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)_</sub>


{% @marketo/form formId="4316" %}
