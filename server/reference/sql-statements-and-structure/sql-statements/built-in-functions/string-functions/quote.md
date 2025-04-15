
# QUOTE

## Syntax


```
QUOTE(str)
```

## Description


Quotes a string to produce a result that can be used as a properly escaped data
value in an SQL statement. The string is returned enclosed by single quotes and
with each instance of single quote ("`<code>'</code>`"), backslash ("`<code>\</code>`"),
`<code>ASCII NUL</code>`, and Control-Z preceded by a backslash. If the argument
is `<code>NULL</code>`, the return value is the word "`<code>NULL</code>`" without enclosing single
quotes.


## Examples


```
SELECT QUOTE("Don't!");
+-----------------+
| QUOTE("Don't!") |
+-----------------+
| 'Don\'t!'       |
+-----------------+

SELECT QUOTE(NULL); 
+-------------+
| QUOTE(NULL) |
+-------------+
| NULL        |
+-------------+
```
