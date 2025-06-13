
# NOT BETWEEN

## Syntax


```
expr NOT BETWEEN min AND max
```

## Description


This is the same as NOT (expr [BETWEEN](between-and.md) min AND max).


Note that the meaning of the alternative form `NOT expr BETWEEN min AND max` is affected by the `HIGH_NOT_PRECEDENCE` [SQL_MODE](../../../../server-management/variables-and-modes/sql-mode.md) flag.


## Examples


```
SELECT 1 NOT BETWEEN 2 AND 3;
+-----------------------+
| 1 NOT BETWEEN 2 AND 3 |
+-----------------------+
|                     1 |
+-----------------------+
```

```
SELECT 'b' NOT BETWEEN 'a' AND 'c';
+-----------------------------+
| 'b' NOT BETWEEN 'a' AND 'c' |
+-----------------------------+
|                           0 |
+-----------------------------+
```

NULL:


```
SELECT 1 NOT BETWEEN 1 AND NULL;
+--------------------------+
| 1 NOT BETWEEN 1 AND NULL |
+--------------------------+
|                     NULL |
+--------------------------+
```


<sub>_This page is licensed: GPLv2, originally from [fill\_help\_tables.sql](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)_</sub>


{% @marketo/form formId="4316" %}
