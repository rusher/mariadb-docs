
# FROM_DAYS

## Syntax


```
FROM_DAYS(N)
```

## Description


Given a day number N, returns a DATE value. The day count is based on the number of days from the start of the standard calendar (0000-00-00).


The function is not designed for use with dates before the advent of the Gregorian calendar in October 1582. Results will not be reliable since it doesn't account for the lost days when the calendar changed from the Julian calendar.


This is the converse of the [TO_DAYS()](to_days.md) function.


## Examples


```
SELECT FROM_DAYS(730669);
+-------------------+
| FROM_DAYS(730669) |
+-------------------+
| 2000-07-03        |
+-------------------+
```


<sub>_This page is licensed: GPLv2, originally from [fill\_help\_tables.sql](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)_</sub>


{% @marketo/form formId="4316" %}
