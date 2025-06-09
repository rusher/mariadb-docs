
# DO

## Syntax


```
DO expr [, expr] ...
```

## Description


`DO` executes the expressions but does not return any
results. In most respects, `DO` is shorthand for
 `SELECT expr, ...,` but has the advantage that it is slightly
faster when you do not care about the result.


`DO` is useful primarily with functions that have side
 effects, such as `[RELEASE_LOCK()](../built-in-functions/secondary-functions/miscellaneous-functions/release_lock.md)`.


GPLv2 fill_help_tables.sql


{% @marketo/form formId="4316" %}
