
# LOWER

## Syntax


```
LOWER(str)
LCASE(str)
```


## Description


Returns the string `str` with all characters changed to lowercase
according to the current character set mapping. The default is latin1
(cp1252 West European).


`LCASE` is a synonym for `LOWER`


## Examples


```
SELECT LOWER('QUADRATICALLY');
+------------------------+
| LOWER('QUADRATICALLY') |
+------------------------+
| quadratically          |
+------------------------+
```

`LOWER()` (and `[UPPER](upper.md)()`) are ineffective when applied to binary
strings (`[BINARY](../../../../data-types/string-data-types/binary.md)`, `[VARBINARY](../../../../data-types/string-data-types/varbinary.md)`, `[BLOB](../../../../data-types/string-data-types/blob.md)`). 
To perform lettercase conversion, [CONVERT](convert.md) the string to a non-binary string:


```
SET @str = BINARY 'North Carolina';

SELECT LOWER(@str), LOWER(CONVERT(@str USING latin1));
+----------------+-----------------------------------+
| LOWER(@str)    | LOWER(CONVERT(@str USING latin1)) |
+----------------+-----------------------------------+
| North Carolina | north carolina                    |
+----------------+-----------------------------------+
```
