
# TIME_FORMAT

## Syntax


```
TIME_FORMAT(time,format)
```

## Description


This is used like the [DATE_FORMAT()](date_format.md) function, but the format string
may contain format specifiers only for hours, minutes, and seconds.
Other specifiers produce a NULL value or 0.


## Examples


```
SELECT TIME_FORMAT('100:00:00', '%H %k %h %I %l');
+--------------------------------------------+
| TIME_FORMAT('100:00:00', '%H %k %h %I %l') |
+--------------------------------------------+
| 100 100 04 04 4                            |
+--------------------------------------------+
```


<sub>_This page is licensed: GPLv2, originally from [fill\_help\_tables.sql](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)_</sub>


{% @marketo/form formId="4316" %}
