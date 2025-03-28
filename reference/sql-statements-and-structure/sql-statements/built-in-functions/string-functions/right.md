# RIGHT

#

# Syntax

```
RIGHT(str,len)
```

#

# Description

Returns the rightmost *`len`* characters from the string *`str`*, or NULL if
any argument is NULL.

#

# Examples

```
SELECT RIGHT('MariaDB', 2);
+---------------------+
| RIGHT('MariaDB', 2) |
+---------------------+
| DB |
+---------------------+
```