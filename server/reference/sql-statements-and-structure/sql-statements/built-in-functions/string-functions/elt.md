
# ELT

## Syntax


```
ELT(N, str1[, str2, str3,...])
```

## Description


Takes a numeric argument and a series of string arguments. Returns the string that corresponds to the given numeric position. For instance, it returns `<code>str1</code>` if `<code>N</code>` is 1, `<code>str2</code>` if `<code>N</code>` is 2, and so on. If the numeric argument is a `<code>[FLOAT](../../../../data-types/data-types-numeric-data-types/float.md)</code>`, MariaDB rounds it to the nearest `<code>[INTEGER](../../../../../../general-resources/learning-and-training/video-presentations-and-screencasts/interviews-related-to-mariadb.md)</code>`. If the numeric argument is less than 1, greater than the total number of arguments, or not a number, `<code>ELT()</code>` returns `<code>NULL</code>`. It must have at least two arguments.


It is complementary to the `<code>[FIELD()](field.md)</code>` function.


## Examples


```
SELECT ELT(1, 'ej', 'Heja', 'hej', 'foo');
+------------------------------------+
| ELT(1, 'ej', 'Heja', 'hej', 'foo') |
+------------------------------------+
| ej                                 |
+------------------------------------+

SELECT ELT(4, 'ej', 'Heja', 'hej', 'foo');
+------------------------------------+
| ELT(4, 'ej', 'Heja', 'hej', 'foo') |
+------------------------------------+
| foo                                |
+------------------------------------+
```

## See also


* [FIND_IN_SET()](find_in_set.md) function. Returns the position of a string in a set of strings.
* [FIELD()](field.md) function. Returns the index position of a string in a list.

