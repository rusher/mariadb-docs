---
hidden: true
---

# TO\_DATE

{% hint style="info" %}
This function is available from MariaDB 12.3.
{% endhint %}

## Syntax

```sql
TO_DATE(expression[, format])
```

## Description

`TO_DATE` converts an _expression_ to a value of [DATE](../../data-types/date-and-time-data-types/date.md) type, optionally providing a _format_ for the date and time. Available date and time formats can be found [here](date_format.md#date-formatting-options).

## Examples

Convert a textual date and time to `DATE` format:

```sql
SELECT TO_DATE('February 5, 2026, 20:56','%Y-%m-%e')
+-----------------------------------------------+
| TO_DATE('February 5, 2026, 20:56','%Y-%m-%e') |
+-----------------------------------------------+
| 2026-02-05                                    |
+-----------------------------------------------+
```

