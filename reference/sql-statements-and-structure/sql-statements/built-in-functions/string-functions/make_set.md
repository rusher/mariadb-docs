# MAKE_SET

#

# Syntax

```
MAKE_SET(bits,str1,str2,...)
```

#

# Description

Returns a set value (a string containing substrings separated by ","
characters) consisting of the strings that have the corresponding bit
in bits set. *`str1`* corresponds to bit 0, *`str2`* to bit 1, and so on. NULL
values in *`str1`*, *`str2`*, ... are not appended to the result.

#

# Examples

```
SELECT MAKE_SET(1,'a','b','c');
+-------------------------+
| MAKE_SET(1,'a','b','c') |
+-------------------------+
| a |
+-------------------------+

SELECT MAKE_SET(1 | 4,'hello','nice','world');
+----------------------------------------+
| MAKE_SET(1 | 4,'hello','nice','world') |
+----------------------------------------+
| hello,world |
+----------------------------------------+

SELECT MAKE_SET(1 | 4,'hello','nice',NULL,'world');
+---------------------------------------------+
| MAKE_SET(1 | 4,'hello','nice',NULL,'world') |
+---------------------------------------------+
| hello |
+---------------------------------------------+

SELECT QUOTE(MAKE_SET(0,'a','b','c'));
+--------------------------------+
| QUOTE(MAKE_SET(0,'a','b','c')) |
+--------------------------------+
| '' |
+--------------------------------+
```