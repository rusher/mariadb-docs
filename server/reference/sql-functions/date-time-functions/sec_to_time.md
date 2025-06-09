# SEC\_TO\_TIME

## Syntax

```
SEC_TO_TIME(seconds)
```

## Description

Returns the seconds argument, converted to hours, minutes, and\
seconds, as a TIME value. The range of the result is constrained to\
that of the [TIME data type](../../data-types/date-and-time-data-types/time.md). A warning occurs if the argument\
corresponds to a value outside that range.

The time will be returned in the format `hh:mm:ss`, or `hhmmss` if used in a numeric calculation.

## Examples

```
SELECT SEC_TO_TIME(12414);
+--------------------+
| SEC_TO_TIME(12414) |
+--------------------+
| 03:26:54           |
+--------------------+

SELECT SEC_TO_TIME(12414)+0;
+----------------------+
| SEC_TO_TIME(12414)+0 |
+----------------------+
|                32654 |
+----------------------+

SELECT SEC_TO_TIME(9999999);
+----------------------+
| SEC_TO_TIME(9999999) |
+----------------------+
| 838:59:59            |
+----------------------+
1 row in set, 1 warning (0.00 sec)

SHOW WARNINGS;
+---------+------+-------------------------------------------+
| Level   | Code | Message                                   |
+---------+------+-------------------------------------------+
| Warning | 1292 | Truncated incorrect time value: '9999999' |
+---------+------+-------------------------------------------+
```

GPLv2 fill\_help\_tables.sql

{% @marketo/form formId="4316" %}
