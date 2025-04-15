
# CHAR Function

## Syntax


```
CHAR(N,... [USING charset_name])
```

## Description


`<code>CHAR()</code>` interprets each argument as an `<code>[INT](../../../../../../general-resources/learning-and-training/video-presentations-and-screencasts/interviews-related-to-mariadb.md)</code>` and returns a string consisting of the characters given by the code values of those integers. `<code>NULL</code>` values are skipped. By default, `<code>CHAR()</code>` returns a binary string. To produce a string in a given [character set](../../../../data-types/string-data-types/character-sets/README.md), use the optional `<code>USING</code>` clause:


```
SELECT CHARSET(CHAR(0x65)), CHARSET(CHAR(0x65 USING utf8));
+---------------------+--------------------------------+
| CHARSET(CHAR(0x65)) | CHARSET(CHAR(0x65 USING utf8)) |
+---------------------+--------------------------------+
| binary              | utf8                           |
+---------------------+--------------------------------+
```

If `<code>USING</code>` is given and the result string is illegal for the given character set, a warning is issued. Also, if strict [SQL mode](../../../../../../release-notes/mariadb-community-server/compatibility-and-differences/sql_modemssql.md) is enabled, the result from `<code>CHAR()</code>` becomes `<code>NULL</code>`.


## Examples


```
SELECT CHAR(77,97,114,'105',97,'68',66);
+----------------------------------+
| CHAR(77,97,114,'105',97,'68',66) |
+----------------------------------+
| MariaDB                          |
+----------------------------------+

SELECT CHAR(77,77.3,'77.3');
+----------------------+
| CHAR(77,77.3,'77.3') |
+----------------------+
| MMM                  |
+----------------------+
1 row in set, 1 warning (0.00 sec)

Warning (Code 1292): Truncated incorrect INTEGER value: '77.3'
```

## See Also


* [Character Sets and Collations](../../../../data-types/string-data-types/character-sets/README.md)
* [ASCII()](ascii.md) - Return ASCII value of first character
* [ORD()](ord.md) - Return value for character in single or multi-byte character sets
* [CHR](chr.md) - Similar, Oracle-compatible, function

