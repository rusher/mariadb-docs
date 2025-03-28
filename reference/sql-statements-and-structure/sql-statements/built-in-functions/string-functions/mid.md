# MID

#

# Syntax

```
MID(str,pos,len)
```

#

# Description

MID(str,pos,len) is a synonym for [SUBSTRING(str,pos,len)](substring.md).

#

# Examples

```
SELECT MID('abcd',4,1);
+-----------------+
| MID('abcd',4,1) |
+-----------------+
| d |
+-----------------+

SELECT MID('abcd',2,2);
+-----------------+
| MID('abcd',2,2) |
+-----------------+
| bc |
+-----------------+
```

A negative starting position:

```
SELECT MID('abcd',-2,4);
+------------------+
| MID('abcd',-2,4) |
+------------------+
| cd |
+------------------+
```