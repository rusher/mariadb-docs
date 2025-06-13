
# GET_FORMAT

## Syntax


```
GET_FORMAT({DATE|DATETIME|TIME}, {'EUR'|'USA'|'JIS'|'ISO'|'INTERNAL'})
```

## Description


Returns a format string. This function is useful in combination with
the [DATE_FORMAT()](date_format.md) and the [STR_TO_DATE()](str_to_date.md) functions.


Possible result formats are:



| Function Call | Result Format |
| --- | --- |
| Function Call | Result Format |
| GET_FORMAT(DATE,'EUR') | '%d.%m.%Y' |
| GET_FORMAT(DATE,'USA') | '%m.%d.%Y' |
| GET_FORMAT(DATE,'JIS') | '%Y-%m-%d' |
| GET_FORMAT(DATE,'ISO') | '%Y-%m-%d' |
| GET_FORMAT(DATE,'INTERNAL') | '%Y%m%d' |
| GET_FORMAT(DATETIME,'EUR') | '%Y-%m-%d %H.%i.%s' |
| GET_FORMAT(DATETIME,'USA') | '%Y-%m-%d %H.%i.%s' |
| GET_FORMAT(DATETIME,'JIS') | '%Y-%m-%d %H:%i:%s' |
| GET_FORMAT(DATETIME,'ISO') | '%Y-%m-%d %H:%i:%s' |
| GET_FORMAT(DATETIME,'INTERNAL') | '%Y%m%d%H%i%s' |
| GET_FORMAT(TIME,'EUR') | '%H.%i.%s' |
| GET_FORMAT(TIME,'USA') | '%h:%i:%s %p' |
| GET_FORMAT(TIME,'JIS') | '%H:%i:%s' |
| GET_FORMAT(TIME,'ISO') | '%H:%i:%s' |
| GET_FORMAT(TIME,'INTERNAL') | '%H%i%s' |



## Examples


Obtaining the string matching to the standard European date format:


```
SELECT GET_FORMAT(DATE, 'EUR');
+-------------------------+
| GET_FORMAT(DATE, 'EUR') |
+-------------------------+
| %d.%m.%Y                |
+-------------------------+
```

Using the same string to format a date:


```
SELECT DATE_FORMAT('2003-10-03',GET_FORMAT(DATE,'EUR'));
+--------------------------------------------------+
| DATE_FORMAT('2003-10-03',GET_FORMAT(DATE,'EUR')) |
+--------------------------------------------------+
| 03.10.2003                                       |
+--------------------------------------------------+

SELECT STR_TO_DATE('10.31.2003',GET_FORMAT(DATE,'USA'));
+--------------------------------------------------+
| STR_TO_DATE('10.31.2003',GET_FORMAT(DATE,'USA')) |
+--------------------------------------------------+
| 2003-10-31                                       |
+--------------------------------------------------+
```


<sub>_This page is licensed: GPLv2, originally from [fill\_help\_tables.sql](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)_</sub>


{% @marketo/form formId="4316" %}
