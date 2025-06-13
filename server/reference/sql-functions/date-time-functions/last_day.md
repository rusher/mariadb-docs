
# LAST_DAY

## Syntax


```
LAST_DAY(date)
```

## Description


Takes a date or datetime value and returns the corresponding value for
the last day of the month. Returns NULL if the argument is invalid.


## Examples


```
SELECT LAST_DAY('2003-02-05');
+------------------------+
| LAST_DAY('2003-02-05') |
+------------------------+
| 2003-02-28             |
+------------------------+

SELECT LAST_DAY('2004-02-05');
+------------------------+
| LAST_DAY('2004-02-05') |
+------------------------+
| 2004-02-29             |
+------------------------+

SELECT LAST_DAY('2004-01-01 01:01:01');
+---------------------------------+
| LAST_DAY('2004-01-01 01:01:01') |
+---------------------------------+
| 2004-01-31                      |
+---------------------------------+

SELECT LAST_DAY('2003-03-32');
+------------------------+
| LAST_DAY('2003-03-32') |
+------------------------+
| NULL                   |
+------------------------+
1 row in set, 1 warning (0.00 sec)

Warning (Code 1292): Incorrect datetime value: '2003-03-32'
```


<sub>_This page is licensed: GPLv2, originally from [fill\_help\_tables.sql](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)_</sub>


{% @marketo/form formId="4316" %}
