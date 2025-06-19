
# SOUNDS LIKE

## Syntax


```
expr1 SOUNDS LIKE expr2
```

## Description


This is the same as [SOUNDEX](soundex.md)(expr1) = SOUNDEX(expr2).


## Example


```
SELECT givenname, surname FROM users WHERE givenname SOUNDS LIKE "robert";
+-----------+---------+
| givenname | surname |
+-----------+---------+
| Roberto   | Castro  |
+-----------+---------+
```


<sub>_This page is licensed: GPLv2, originally from [fill\_help\_tables.sql](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)_</sub>


{% @marketo/form formId="4316" %}
