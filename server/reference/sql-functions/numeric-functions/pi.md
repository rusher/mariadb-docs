
# PI

## Syntax


```
PI()
```

## Description


Returns the value of π (pi). The default number of decimal places
displayed is six, but MariaDB uses the full double-precision value
internally.


## Examples


```
SELECT PI();
+----------+
| PI()     |
+----------+
| 3.141593 |
+----------+

SELECT PI()+0.0000000000000000000000;
+-------------------------------+
| PI()+0.0000000000000000000000 |
+-------------------------------+
|      3.1415926535897931159980 |
+-------------------------------+
```


<sub>_This page is licensed: GPLv2, originally from [fill\_help\_tables.sql](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)_</sub>


{% @marketo/form formId="4316" %}
