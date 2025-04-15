
# EXPORT_SET

## Syntax


```
EXPORT_SET(bits, on, off[, separator[, number_of_bits]])
```

## Description


Takes a minimum of three arguments. Returns a string where each bit in the given `<code>bits</code>` argument is returned, with the string values given for `<code>on</code>` and `<code>off</code>`.


Bits are examined from right to left, (from low-order to high-order bits). Strings are added to the result from left to right, separated by a separator string (defaults as '`<code>,</code>`'). You can optionally limit the number of bits the `<code>EXPORT_SET()</code>` function examines using the `<code>number_of_bits</code>` option.


If any of the arguments are set as `<code>NULL</code>`, the function returns `<code>NULL</code>`.


## Examples


```
SELECT EXPORT_SET(5,'Y','N',',',4);
+-----------------------------+
| EXPORT_SET(5,'Y','N',',',4) |
+-----------------------------+
| Y,N,Y,N                     |
+-----------------------------+

SELECT EXPORT_SET(6,'1','0',',',10);
+------------------------------+
| EXPORT_SET(6,'1','0',',',10) |
+------------------------------+
| 0,1,1,0,0,0,0,0,0,0          |
+------------------------------+
```
