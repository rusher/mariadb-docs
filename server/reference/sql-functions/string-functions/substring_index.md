
# SUBSTRING_INDEX

## Syntax


```
SUBSTRING_INDEX(str,delim,count)
```


## Description


Returns the substring from string *`str`* before count occurrences of the
delimiter *`delim`*. If *`count`* is positive, everything to the left
of the final delimiter (counting from the left) is returned. If *`count`*
is negative, everything to the right of the final delimiter (counting from the
right) is returned. `SUBSTRING_INDEX()` performs a case-sensitive match when
searching for *`delim`*.


If any argument is `NULL`, returns `NULL`.


For example


```
SUBSTRING_INDEX('www.mariadb.org', '.', 2)
```

means "Return all of the characters up to the 2nd occurrence of ."


## Examples


```
SELECT SUBSTRING_INDEX('www.mariadb.org', '.', 2);
+--------------------------------------------+
| SUBSTRING_INDEX('www.mariadb.org', '.', 2) |
+--------------------------------------------+
| www.mariadb                                |
+--------------------------------------------+

SELECT SUBSTRING_INDEX('www.mariadb.org', '.', -2);
+---------------------------------------------+
| SUBSTRING_INDEX('www.mariadb.org', '.', -2) |
+---------------------------------------------+
| mariadb.org                                 |
+---------------------------------------------+
```

## See Also


* [INSTR()](instr.md) - Returns the position of a string within a string
* [LOCATE()](locate.md) - Returns the position of a string within a string
* [SUBSTRING()](substring.md) - Returns a string based on position


<sub>_This page is licensed: GPLv2, originally from [fill\_help\_tables.sql](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)_</sub>


{% @marketo/form formId="4316" %}
