
# LOWER

## Syntax


```
LOWER(str)
LCASE(str)
```


## Description


Returns the string `<code>str</code>` with all characters changed to lowercase
according to the current character set mapping. The default is latin1
(cp1252 West European).


`<code>LCASE</code>` is a synonym for `<code>LOWER</code>`


## Examples


```
SELECT LOWER('QUADRATICALLY');
+------------------------+
| LOWER('QUADRATICALLY') |
+------------------------+
| quadratically          |
+------------------------+
```

`<code>LOWER()</code>` (and `<code>[UPPER](upper.md)()</code>`) are ineffective when applied to binary
strings (`<code>[BINARY](../../../../storage-engines/innodb/binary-log-group-commit-and-innodb-flushing-performance.md)</code>`, `<code>[VARBINARY](../../../../data-types/string-data-types/varbinary.md)</code>`, `<code>[BLOB](../../../../data-types/string-data-types/blob.md)</code>`). 
To perform lettercase conversion, [CONVERT](../../../../storage-engines/converting-tables-from-myisam-to-innodb.md) the string to a non-binary string:


```
SET @str = BINARY 'North Carolina';

SELECT LOWER(@str), LOWER(CONVERT(@str USING latin1));
+----------------+-----------------------------------+
| LOWER(@str)    | LOWER(CONVERT(@str USING latin1)) |
+----------------+-----------------------------------+
| North Carolina | north carolina                    |
+----------------+-----------------------------------+
```
