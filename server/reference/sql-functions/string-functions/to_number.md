# TO\_NUMBER

{% hint style="info" %}
This function is available from MariaDB 12.2.1.
{% endhint %}

Converts an expression to a numeric data type.

## Syntax

```sql
TO_NUMBER(expression [, format])
```

## Description

This function converts an expression to a numeric data type. The expression can be a number value of [`CHAR`](../../data-types/string-data-types/char.md), [`VARCHAR`](../../data-types/string-data-types/varchar.md), [`NATIONAL CHAR`](../../data-types/string-data-types/national-char.md), [`NATIONAL VARCHAR`](../../data-types/string-data-types/national-varchar.md), or [`BINARY`](../../data-types/string-data-types/binary.md) data type. For data types other than `BINARY`, you can optionally specify a format, like `'2025-11-17'` for a `DATE` type. (Valid format strings for date and time [can be found here](../../sql-structure/sql-language-structure/date-and-time-literals.md).)

## Examples

```sql
SELECT TO_NUMBER('100.00');
+---------------------+
| TO_NUMBER('100.00') |
+---------------------+
| 100.00              |
+---------------------+
```
