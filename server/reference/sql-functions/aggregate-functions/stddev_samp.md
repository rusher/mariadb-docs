# STDDEV\_SAMP

## Syntax

```
STDDEV_SAMP(expr)
```

## Description

Returns the sample standard deviation of `expr` (the square root of [VAR\_SAMP()](var_samp.md)).

It is an [aggregate function](./), and so can be used with the [GROUP BY](../../sql-statements/data-manipulation/selecting-data/group-by.md) clause.

STDDEV\_SAMP() can be used as a [window function](../special-functions/window-functions/).

STDDEV\_SAMP() returns `NULL` if there were no matching rows.

<sub>_This page is licensed: GPLv2, originally from [fill\_help\_tables.sql](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)_</sub>

{% @marketo/form formId="4316" %}
