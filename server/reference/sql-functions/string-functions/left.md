
# LEFT

## Syntax


```
LEFT(str,len)
```

## Description


Returns the leftmost `len` characters from the string `str`, or NULL if
any argument is NULL.


## Examples


```
SELECT LEFT('MariaDB', 5);
+--------------------+
| LEFT('MariaDB', 5) |
+--------------------+
| Maria              |
+--------------------+
```


<sub>_This page is licensed: GPLv2, originally from [fill\_help\_tables.sql](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)_</sub>


{% @marketo/form formId="4316" %}
