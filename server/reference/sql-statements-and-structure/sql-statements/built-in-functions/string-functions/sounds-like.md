
# SOUNDS LIKE

## Syntax


```
expr1 SOUNDS LIKE expr2
```

## Description


This is the same as `<code>[SOUNDEX](soundex.md)(expr1) = SOUNDEX(expr2)</code>`.


## Example


```
SELECT givenname, surname FROM users WHERE givenname SOUNDS LIKE "robert";
+-----------+---------+
| givenname | surname |
+-----------+---------+
| Roberto   | Castro  |
+-----------+---------+
```
