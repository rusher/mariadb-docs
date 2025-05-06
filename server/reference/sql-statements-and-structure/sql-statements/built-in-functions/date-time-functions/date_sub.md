
# DATE_SUB

## Syntax


```
DATE_SUB(date,INTERVAL expr unit)
```

## Description


Performs date arithmetic. The *date* argument specifies the
starting date or datetime value. *expr* is an expression specifying the
interval value to be subtracted from the starting date. *expr* is a
string; it may start with a "`-`" for negative intervals. *unit* is a
keyword indicating the units in which the expression should be interpreted. See [Date and Time Units](date-and-time-units.md) for a complete list of permitted units.


See also `[DATE_ADD()](date_add.md)`.


## Examples


```
SELECT DATE_SUB('1998-01-02', INTERVAL 31 DAY);
+-----------------------------------------+
| DATE_SUB('1998-01-02', INTERVAL 31 DAY) |
+-----------------------------------------+
| 1997-12-02                              |
+-----------------------------------------+
```

```
SELECT DATE_SUB('2005-01-01 00:00:00', INTERVAL '1 1:1:1' DAY_SECOND);
+----------------------------------------------------------------+
| DATE_SUB('2005-01-01 00:00:00', INTERVAL '1 1:1:1' DAY_SECOND) |
+----------------------------------------------------------------+
| 2004-12-30 22:58:59                                            |
+----------------------------------------------------------------+
```


GPLv2 fill_help_tables.sql

