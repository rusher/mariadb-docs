# TIME_FORMAT

#

# Syntax

```
TIME_FORMAT(time,format)
```

#

# Description

This is used like the [DATE_FORMAT()](date_format.md) function, but the format string
may contain format specifiers only for hours, minutes, and seconds.
Other specifiers produce a NULL value or 0.

#

# Examples

```
SELECT TIME_FORMAT('100:00:00', '%H %k %h %I %l');
+--------------------------------------------+
| TIME_FORMAT('100:00:00', '%H %k %h %I %l') |
+--------------------------------------------+
| 100 100 04 04 4 |
+--------------------------------------------+
```