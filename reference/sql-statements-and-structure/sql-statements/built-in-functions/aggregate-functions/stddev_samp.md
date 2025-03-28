# STDDEV_SAMP

#

# Syntax

```
STDDEV_SAMP(expr)
```

#

# Description

Returns the sample standard deviation of `expr` (the square root of [VAR_SAMP()](var_samp.md)).

It is an [aggregate function](../special-functions/window-functions/aggregate-functions-as-window-functions.md), and so can be used with the [GROUP BY](../../data-manipulation/selecting-data/group-by.md) clause.

STDDEV_SAMP() can be used as a [window function](../special-functions/window-functions/window-functions-overview.md).

STDDEV_SAMP() returns `NULL` if there were no matching rows.