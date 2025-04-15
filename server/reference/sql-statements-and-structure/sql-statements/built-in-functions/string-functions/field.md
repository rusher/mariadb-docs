
# FIELD

## Syntax


```
FIELD(pattern, str1[,str2,...])
```

## Description


Returns the index position of the string or number matching the given pattern. Returns `<code>0</code>` in the event that none of the arguments match the pattern. Raises an Error 1582 if not given at least two arguments.


When all arguments given to the `<code>FIELD()</code>` function are strings, they are treated as case-insensitive. When all the arguments are numbers, they are treated as numbers. Otherwise, they are treated as doubles.


If the given pattern occurs more than once, the	`<code>FIELD()</code>` function only returns the index of the first instance. If the given pattern is `<code>NULL</code>`, the function returns `<code>0</code>`, as a `<code>NULL</code>` pattern always fails to match.


This function is complementary to the `<code>[ELT()](elt.md)</code>` function.


## Examples


```
SELECT FIELD('ej', 'Hej', 'ej', 'Heja', 'hej', 'foo') 
   AS 'Field Results';
+---------------+
| Field Results | 
+---------------+
|             2 |
+---------------+

SELECT FIELD('fo', 'Hej', 'ej', 'Heja', 'hej', 'foo')
   AS 'Field Results';
+---------------+
| Field Results | 
+---------------+
|             0 |
+---------------+

SELECT FIELD(1, 2, 3, 4, 5, 1) AS 'Field Results';
+---------------+
| Field Results |
+---------------+
|             5 |
+---------------+

SELECT FIELD(NULL, 2, 3) AS 'Field Results';
+---------------+
| Field Results |
+---------------+
|             0 |
+---------------+

SELECT FIELD('fail') AS 'Field Results';
Error 1582 (42000): Incorrect parameter count in call
to native function 'field'
```

## See also


* [ELT()](elt.md) function. Returns the N'th element from a set of strings.

